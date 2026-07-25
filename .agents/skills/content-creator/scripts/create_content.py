#!/usr/bin/env python3
"""Provision a Hugo content bundle, optionally against an existing GitHub issue."""

import argparse
import json
import os
import re
import subprocess
import sys


CONTENT_TYPE_MAP = {
    "article": {"kind": "article-bundle", "dir": "articles"},
    "research": {"kind": "research-bundle", "dir": "research"},
    "video": {"kind": "video-bundle", "dir": "videos"},
    "lab": {"kind": "lab-bundle", "dir": "lab"},
    "portfolio": {"kind": "portfolio-bundle", "dir": "portfolio"},
    "signals": {"kind": "signals-bundle", "dir": "signals"},
}


def clean_slug(slug):
    slug = re.sub(r"[^a-z0-9-]", "-", slug.lower())
    return re.sub(r"-+", "-", slug).strip("-")


def run(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        print(f"Error executing command: {' '.join(command)}", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout.strip()


def create_issue(content_type, slug):
    title = f"Enhancement: New {content_type.capitalize()} - {slug.replace('-', ' ').title()}"
    body = f"Proposed new {content_type}: {slug}\n\nInfrastructure provisioned by content-creator skill."
    issue_url = run(["gh", "issue", "create", "--title", title, "--body", body, "--label", "enhancement"])
    return int(issue_url.rstrip("/").split("/")[-1]), issue_url


def main():
    parser = argparse.ArgumentParser(description="Provision a Hugo content bundle")
    parser.add_argument("content_type", choices=CONTENT_TYPE_MAP)
    parser.add_argument("slug")
    parser.add_argument("--issue", type=int, help="Reuse this existing GitHub backlog issue")
    parser.add_argument("--branch", help="Branch name when reusing an existing issue")
    args = parser.parse_args()

    content_type = args.content_type
    slug = clean_slug(args.slug)
    if not slug:
        parser.error("slug must contain letters or numbers")

    type_info = CONTENT_TYPE_MAP[content_type]
    hugo_path = f"{type_info['dir']}/{slug}"
    index_path = os.path.join("content", type_info["dir"], slug, "index.md")

    if os.path.exists(index_path):
        parser.error(f"content bundle already exists: {index_path}")

    if args.issue:
        issue_number = args.issue
        issue_url = run(["gh", "issue", "view", str(issue_number), "--json", "url", "--jq", ".url"])
        branch_name = args.branch or f"feature/{issue_number}-{content_type}-{slug}"
        print(f"Reusing GitHub issue #{issue_number}: {issue_url}")
        print(f"Creating linked branch: {branch_name}")
        run(["gh", "issue", "develop", str(issue_number), "--name", branch_name, "--checkout"])
    else:
        issue_number, issue_url = create_issue(content_type, slug)
        branch_name = f"feature/{content_type}-{slug}"
        print(f"Created GitHub issue #{issue_number}: {issue_url}")
        print(f"Creating feature branch: {branch_name}")
        run(["git", "checkout", "-b", branch_name])

    print(f"Running hugo new for {hugo_path} using kind {type_info['kind']}")
    run(["hugo", "new", "--kind", type_info["kind"], hugo_path])
    print(json.dumps({
        "content_type": content_type,
        "slug": slug,
        "issue": issue_number,
        "issue_url": issue_url,
        "branch": branch_name,
        "index_path": index_path,
    }))


if __name__ == "__main__":
    main()
