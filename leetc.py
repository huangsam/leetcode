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


def get_urls() -> dict[str, set[str]]:
    """Get all LeetCode problem URLs from Python and Java files."""
    pattern = re.compile(r"^(#|//) (https://leetcode\.com/problems/[^/]+/)")
    urls: dict[str, set[str]] = {}  # url -> set of languages

    for dir_name in ["python", "java"]:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            continue
        lang = dir_name.capitalize()  # 'Python' or 'Java'
        for ext in ["*.py", "*.java"]:
            for file_path in dir_path.glob(ext):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            match = pattern.match(line.strip())
                            if match:
                                url = match.group(2)
                                if url not in urls:
                                    urls[url] = set()
                                urls[url].add(lang)
                except Exception as e:
                    click.echo(f"Error reading {file_path}: {e}", err=True)

    return urls


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
    urls = get_urls()
    for url in sorted(urls):
        langs = sorted(urls[url])
        lang_str = ", ".join(langs)
        click.echo(f"{url} ({lang_str})")


@cli.command()
def sync():
    """Sync AGENTS.md with the latest solved problems from Python and Java files."""
    # Read existing AGENTS.md
    agents_path = Path("AGENTS.md")
    if not agents_path.exists():
        click.echo("AGENTS.md not found.", err=True)
        return

    with open(agents_path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    # Get existing slugs and problems
    existing_slugs = set()
    existing_problems = {}
    for line in lines:
        # Parse the full problem row to extract both metadata and slug from URL
        match = re.match(r"\| \[(.*?)\]\(https://leetcode\.com/problems/([^/]+)/\) \| (\d+) \| (.*?) \| (.*?) \|", line)
        if match:
            title = match.group(1)
            slug = match.group(2)
            qid = int(match.group(3))
            diff = match.group(4)
            topics = match.group(5)
            existing_slugs.add(slug)
            existing_problems[qid] = (qid, title, diff, topics, slug)

    # Get all urls
    urls = get_urls()
    all_slugs = set()
    for url in urls:
        match = re.search(r"https://leetcode.com/problems/([^/]+)/", url)
        if match:
            all_slugs.add(match.group(1))

    # New slugs
    new_slugs = all_slugs - existing_slugs
    click.echo(f"Found {len(new_slugs)} new problems.")

    new_problems = []
    for slug in new_slugs:
        try:
            question = get_question_details(slug)
            qid = int(question["questionFrontendId"])
            title = question["title"]
            difficulty = question["difficulty"]
            topics = ", ".join([tag["name"] for tag in question["topicTags"]])
            new_problems.append((qid, title, difficulty, topics, slug))
            click.echo(f"Added {qid}: {title}")
        except Exception as e:
            click.echo(f"Error fetching {slug}: {e}", err=True)

    # Combine and sort
    all_problems = list(existing_problems.values()) + new_problems
    all_problems.sort(key=lambda x: x[0])

    # Generate new content
    header = """# LeetCode Problems Summary

Here are all of the problems that I have solved on the LeetCode platform:

| Problem Name | ID | Difficulty | Topics |
|--------------|----|------------|--------|
"""
    rows = []
    for qid, title, diff, topics, slug in all_problems:
        url = f"https://leetcode.com/problems/{slug}/"
        row = f"| [{title}]({url}) | {qid} | {diff} | {topics} |"
        rows.append(row)

    new_content = header + "\n".join(rows) + "\n"

    # Write back
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    click.echo("AGENTS.md updated successfully.")


if __name__ == "__main__":
    cli()
