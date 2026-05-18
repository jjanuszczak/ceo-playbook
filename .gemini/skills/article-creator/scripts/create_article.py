import os
import sys
import subprocess
import re

def clean_slug(slug):
    # Remove any non-alphanumeric characters (except hyphens) and convert to lowercase
    slug = slug.lower()
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_article.py <slug>")
        sys.exit(1)

    raw_slug = sys.argv[1]
    slug = clean_slug(raw_slug)

    # 1. Create GitHub Issue
    title = f"Enhancement: New Article - {slug.replace('-', ' ').title()}"
    body = f"Proposed new article: {slug}\n\nInfrastructure provisioned by article-creator skill."
    print(f"Creating GitHub issue: {title}")
    issue_output = run_command(f'gh issue create --title "{title}" --body "{body}" --label "enhancement"')
    print(f"Issue created: {issue_output}")

    # 2. Create Feature Branch
    branch_name = f"feature/article-{slug}"
    print(f"Creating feature branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}")

    # 3. Use Hugo new to create the article bundle
    article_path = f"articles/{slug}"
    print(f"Running hugo new for {article_path}")
    run_command(f"hugo new --kind article-bundle {article_path}")

    index_path = os.path.join("content", "articles", slug, "index.md")
    print(f"\n[INFRASTRUCTURE READY]")
    print(f"File Path: {index_path}")
    print(f"Branch: {branch_name}")

if __name__ == "__main__":
    main()
