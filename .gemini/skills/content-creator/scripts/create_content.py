import os
import sys
import subprocess
import re

# Mapping of user-friendly names to Hugo archetype kinds and content directories
CONTENT_TYPE_MAP = {
    "article": {"kind": "article-bundle", "dir": "articles"},
    "research": {"kind": "research-bundle", "dir": "research"},
    "video": {"kind": "video-bundle", "dir": "videos"},
    "lab": {"kind": "lab-bundle", "dir": "lab"},
    "portfolio": {"kind": "portfolio-bundle", "dir": "portfolio"},
    "signals": {"kind": "signals-bundle", "dir": "signals"}
}

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
    if len(sys.argv) < 3:
        print("Usage: python create_content.py <content_type> <slug>")
        print(f"Available types: {', '.join(CONTENT_TYPE_MAP.keys())}")
        sys.exit(1)

    content_type = sys.argv[1].lower()
    raw_slug = sys.argv[2]
    
    if content_type not in CONTENT_TYPE_MAP:
        print(f"Error: Unknown content type '{content_type}'")
        print(f"Available types: {', '.join(CONTENT_TYPE_MAP.keys())}")
        sys.exit(1)

    slug = clean_slug(raw_slug)
    type_info = CONTENT_TYPE_MAP[content_type]

    # 1. Create GitHub Issue
    title = f"Enhancement: New {content_type.capitalize()} - {slug.replace('-', ' ').title()}"
    body = f"Proposed new {content_type}: {slug}\n\nInfrastructure provisioned by content-creator skill."
    print(f"Creating GitHub issue: {title}")
    issue_output = run_command(f'gh issue create --title "{title}" --body "{body}" --label "enhancement"')
    print(f"Issue created: {issue_output}")

    # 2. Create Feature Branch
    branch_name = f"feature/{content_type}-{slug}"
    print(f"Creating feature branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}")

    # 3. Use Hugo new to create the content bundle
    hugo_path = f"{type_info['dir']}/{slug}"
    print(f"Running hugo new for {hugo_path} using kind {type_info['kind']}")
    run_command(f"hugo new --kind {type_info['kind']} {hugo_path}")

    index_path = os.path.join("content", type_info['dir'], slug, "index.md")
    print(f"\n[INFRASTRUCTURE READY]")
    print(f"Content Type: {content_type}")
    print(f"File Path: {index_path}")
    print(f"Branch: {branch_name}")

if __name__ == "__main__":
    main()
