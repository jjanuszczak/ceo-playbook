import sys
import os
import json

def check_structure(article_path):
    # Normalize path
    article_path = os.path.abspath(article_path)
    filename = os.path.basename(article_path)
    
    errors = []
    
    # Check 1: Must be index.md
    if filename != "index.md":
        errors.append(f"File must be named 'index.md' for Leaf Bundle, found '{filename}'")
    
    # Check 2: Must be in a subdirectory of content/
    # Expected: .../content/<section>/<slug>/index.md
    parts = article_path.split(os.sep)
    if "content" not in parts:
        errors.append("File is not located within the 'content/' directory")
    else:
        content_idx = parts.index("content")
        # Ensure there are at least 2 levels below content/ (section and slug)
        if len(parts) - 1 - content_idx < 3:
             errors.append("File is not in a proper Leaf Bundle structure (content/<section>/<slug>/index.md)")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": "Structure is valid Leaf Bundle"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_structure(sys.argv[1]))
