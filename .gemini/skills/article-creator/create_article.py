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
        print("Usage: python create_article.py <slug> [content_file]")
        sys.exit(1)

    raw_slug = sys.argv[1]
    slug = clean_slug(raw_slug)
    content = ""
    
    if len(sys.argv) > 2:
        content_file = sys.argv[2]
        if os.path.exists(content_file):
            with open(content_file, 'r') as f:
                content = f.read()

    # 1. Create GitHub Issue
    # Note: This assumes 'gh' CLI is installed and authenticated
    title = f"Enhancement: New Article - {slug.replace('-', ' ').title()}"
    body = f"Proposed new article: {slug}\n\nAutomated issue created by article-creator skill."
    print(f"Creating GitHub issue: {title}")
    issue_output = run_command(f'gh issue create --title "{title}" --body "{body}" --label "enhancement"')
    print(f"Issue created: {issue_output}")

    # 2. Create Feature Branch
    branch_name = f"feature/article-{slug}"
    print(f"Creating feature branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}")

    # 3. Use Hugo new to create the article
    article_path = f"articles/{slug}"
    print(f"Running hugo new for {article_path}")
    run_command(f"hugo new --kind article-bundle {article_path}")

    # 4. Update front matter status to "user-review" and add optional content
    index_path = os.path.join("content", "articles", slug, "index.md")
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            lines = f.readlines()

        new_lines = []
        in_frontmatter = False
        frontmatter_count = 0
        
        for line in lines:
            if line.strip() == "---":
                frontmatter_count += 1
                new_lines.append(line)
                continue
            
            if frontmatter_count == 1:
                if line.startswith("status:"):
                    new_lines.append('status: "user-review"\n')
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        # If content is provided, append it after the front matter
        if content:
            # The archetype index.md ends with a newline and some boilerplate text. 
            # We will append our content at the very end.
            new_lines.append("\n")
            new_lines.append(content)

        with open(index_path, 'w') as f:
            f.writelines(new_lines)

    print(f"\nArticle '{slug}' is available for review at: {index_path}")
    print(f"Branch: {branch_name}")

if __name__ == "__main__":
    main()
