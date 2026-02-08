import json
import re
from pathlib import Path

import click
import httpx


def get_question_details(title_slug: str) -> dict:
    """Get question details from LeetCode GraphQL API."""
    query = """
    query questionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            isPaidOnly
            difficulty
            likes
            dislikes
            topicTags {
                name
                slug
            }
            content
        }
    }
    """
    variables = {"titleSlug": title_slug}
    response = httpx.post("https://leetcode.com/graphql", json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()
    return data["data"]["question"]


def get_urls() -> tuple[dict[str, set[str]], set[str]]:
    """Get all LeetCode problem URLs from Python and Java files, and flag files without links."""
    pattern = re.compile(r"^(#|//) (https://leetcode\.com/problems/[^/]+/)")
    urls: dict[str, set[str]] = {}  # url -> set of languages
    missing_files: set[str] = set()

    for dir_name in ["python", "java"]:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            continue
        lang = dir_name.capitalize()  # 'Python' or 'Java'
        # Only scan files directly in the directory (first layer)
        for file_path in dir_path.iterdir():
            if file_path.is_file() and file_path.suffix in [".py", ".java"]:
                has_url = False
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            match = pattern.match(line.strip())
                            if match:
                                url = match.group(2)
                                if url not in urls:
                                    urls[url] = set()
                                urls[url].add(lang)
                                has_url = True
                                break  # No need to check further lines
                except Exception as e:
                    click.echo(f"Error reading {file_path}: {e}", err=True)
                if not has_url:
                    missing_files.add(str(file_path))

    return urls, missing_files


@click.group()
def cli():
    """LeetCode CLI tool for fetching problem details and user progress.

    Kudos to https://github.com/akarsh1995/leetcode-graphql-queries for
    providing all of the GraphQL queries used in this tool.
    """
    pass


@cli.command()
@click.argument("url_fragment")
def detail(url_fragment: str):
    """Get details for a specific LeetCode problem by URL fragment (titleSlug), including the problem content."""
    question = get_question_details(url_fragment)
    click.echo(json.dumps({"data": {"question": question}}, indent=2))


@cli.command()
@click.argument("username", required=False, default="huangsam")
def progress(username: str):
    """Get user progress summary on LeetCode problems."""
    query = """
    query userProgress($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            problemsSolvedBeatsStats {
                difficulty
                percentage
            }
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """
    variables = {"username": username}
    response = httpx.post("https://leetcode.com/graphql", json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()
    click.echo(json.dumps(data, indent=2))


@cli.command()
def urls():
    """List all LeetCode problem URLs from Python and Java files in the workspace, with language indicators."""
    urls, missing_files = get_urls()

    click.echo("== LeetCode URLs ==")
    for url in sorted(urls):
        langs = sorted(urls[url])
        lang_str = ", ".join(langs)
        click.echo(f"{url} ({lang_str})")

    if missing_files:
        click.echo("\n== Files without LeetCode URLs ==")
        for file in sorted(missing_files):
            click.echo(file)
    else:
        click.echo("\n== All files contain LeetCode URLs ==")


@cli.command()
def sync():
    """Sync problems.json and AGENTS.md with the latest solved problems from Python and Java files."""
    problems_json_path = Path("problems.json")

    # Load existing problems from JSON cache
    existing_problems = {}
    if problems_json_path.exists():
        with open(problems_json_path, "r", encoding="utf-8") as f:
            problems_data = json.load(f)
            for problem in problems_data:
                qid = problem["id"]
                existing_problems[qid] = problem

    existing_slugs = {p["slug"] for p in existing_problems.values()}
    click.echo(f"Loaded {len(existing_problems)} problems from cache.")

    # Get all problem URLs from source files
    urls, _ = get_urls()
    all_slugs = set()
    for url in urls:
        match = re.search(r"https://leetcode.com/problems/([^/]+)/", url)
        if match:
            all_slugs.add(match.group(1))

    # Find new slugs not in cache
    new_slugs = all_slugs - existing_slugs
    click.echo(f"Found {len(new_slugs)} new problems to fetch.")

    # Fetch details for new problems
    for slug in new_slugs:
        try:
            question = get_question_details(slug)
            qid = int(question["questionFrontendId"])
            problem = {
                "id": qid,
                "title": question["title"],
                "slug": slug,
                "difficulty": question["difficulty"],
                "topics": [tag["name"] for tag in question["topicTags"]],
            }
            existing_problems[qid] = problem
            click.echo(f"Fetched {qid}: {problem['title']}")
        except Exception as e:
            click.echo(f"Error fetching {slug}: {e}", err=True)

    # Filter to only problems that exist in source files
    active_problems = {qid: problem for qid, problem in existing_problems.items() if problem["slug"] in all_slugs}

    # Save updated cache to JSON
    problems_list = sorted(active_problems.values(), key=lambda x: x["id"])
    with open(problems_json_path, "w", encoding="utf-8") as f:
        json.dump(problems_list, f, indent=2)

    click.echo(f"Updated problems.json with {len(problems_list)} problems.")

    # Generate AGENTS.md from the cache
    header = """# LeetCode Problems Summary

Here are all of the problems that I have solved on the LeetCode platform:

| Problem Name | ID | Difficulty | Topics |
|--------------|----|------------|--------|
"""
    rows = []
    for problem in problems_list:
        qid = problem["id"]
        title = problem["title"]
        slug = problem["slug"]
        diff = problem["difficulty"]
        topics = ", ".join(problem["topics"])
        url = f"https://leetcode.com/problems/{slug}/"
        row = f"| [{title}]({url}) | {qid} | {diff} | {topics} |"
        rows.append(row)

    new_content = header + "\n".join(rows) + "\n"

    # Write AGENTS.md
    agents_path = Path("AGENTS.md")
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    click.echo("AGENTS.md updated successfully.")


if __name__ == "__main__":
    cli()
