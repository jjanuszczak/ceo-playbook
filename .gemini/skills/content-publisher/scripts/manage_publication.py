import os
import re
import sys
import argparse
from datetime import datetime

CONTENT_DIRS = ["content/articles", "content/videos", "content/lab"]

def find_post(search_term):
    """Fuzzy discovery of a post by slug or title."""
    search_term = search_term.lower()
    matches = []

    for base_dir in CONTENT_DIRS:
        if not os.path.exists(base_dir):
            continue
        
        for entry in os.listdir(base_dir):
            entry_path = os.path.join(base_dir, entry)
            if os.path.isdir(entry_path):
                index_path = os.path.join(entry_path, "index.md")
                if os.path.exists(index_path):
                    # Check slug (folder name)
                    if search_term in entry.lower():
                        matches.append(index_path)
                        continue
                    
                    # Check title in frontmatter
                    with open(index_path, 'r') as f:
                        content = f.read()
                        title_match = re.search(r'^title:\s*"(.*)"', content, re.MULTILINE)
                        if title_match and search_term in title_match.group(1).lower():
                            matches.append(index_path)
    
    return list(set(matches))

def update_frontmatter(file_path, mode):
    """Updates the frontmatter based on publish/unpublish mode."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Verify we have frontmatter
    if not content.startswith("---"):
        print(f"Error: {file_path} does not appear to have valid Hugo frontmatter.")
        return False

    now = datetime.now().astimezone().isoformat(timespec='seconds')

    if mode == "publish":
        # Check if already published
        draft_match = re.search(r'^draft:\s*false', content, re.MULTILINE)
        status_match = re.search(r'^status:\s*("published"|published)', content, re.MULTILINE)
        if draft_match and status_match:
            print(f"Post is already published: {file_path}")
            return True

        # Update draft
        content = re.sub(r'^draft:\s*(true|false)', 'draft: false', content, flags=re.MULTILINE)
        
        # Update/Add status
        if re.search(r'^status:', content, re.MULTILINE):
            content = re.sub(r'^status:\s*.*', 'status: "published"', content, flags=re.MULTILINE)
        else:
            # Add status after draft
            content = re.sub(r'^(draft:\s*false)', r'\1\nstatus: "published"', content, flags=re.MULTILINE)

        # Update date
        content = re.sub(r'^date:\s*.*', f'date: {now}', content, flags=re.MULTILINE)
        print(f"Published: {file_path}")

    elif mode == "unpublish":
        # Check if already in review
        draft_match = re.search(r'^draft:\s*true', content, re.MULTILINE)
        status_match = re.search(r'^status:\s*("review"|review)', content, re.MULTILINE)
        if draft_match and status_match:
            print(f"Post is already unpublished (status: review): {file_path}")
            return True

        # Update draft
        content = re.sub(r'^draft:\s*(true|false)', 'draft: true', content, flags=re.MULTILINE)
        
        # Update/Add status
        if re.search(r'^status:', content, re.MULTILINE):
            content = re.sub(r'^status:\s*.*', 'status: "review"', content, flags=re.MULTILINE)
        else:
            content = re.sub(r'^(draft:\s*true)', r'\1\nstatus: "review"', content, flags=re.MULTILINE)
        
        print(f"Unpublished (status: review): {file_path}")

    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Manage Hugo post publication state.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--publish", help="Fuzzy search term for the post to publish.")
    group.add_argument("--unpublish", help="Fuzzy search term for the post to unpublish.")

    args = parser.parse_args()
    
    search_term = args.publish if args.publish else args.unpublish
    mode = "publish" if args.publish else "unpublish"

    matches = find_post(search_term)

    if not matches:
        print(f"Error: No post found matching '{search_term}'")
        sys.exit(1)
    
    if len(matches) > 1:
        print("Error: Multiple matches found. Please be more specific:")
        for m in matches:
            print(f"  - {m}")
        sys.exit(1)

    target_file = matches[0]
    if update_frontmatter(target_file, mode):
        print(f"Successfully processed {target_file}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
