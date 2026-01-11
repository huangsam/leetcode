#!/usr/bin/env python3

import json
import re
from pathlib import Path

import click
import httpx


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
    variables = {"titleSlug": url_fragment}
    response = httpx.post("https://leetcode.com/graphql", json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()
    click.echo(json.dumps(data, indent=2))


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
    pattern = re.compile(r"^(#|//) (https://leetcode\.com/problems/[^/]+/)")
    urls = {}  # url -> set of languages

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

    for url in sorted(urls):
        langs = sorted(urls[url])
        lang_str = ", ".join(langs)
        click.echo(f"{url} ({lang_str})")


if __name__ == "__main__":
    cli()
