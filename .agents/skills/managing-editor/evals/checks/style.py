import sys
import os
import re
import json

def check_style(article_path):
    errors = []
    
    if not os.path.exists(article_path):
        print(json.dumps({"errors": ["File not found"]}))
        return 1

    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for em dashes (—)
    if "—" in content:
        # Find lines with em dashes for better reporting
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "—" in line:
                errors.append(f"Em dash found on line {i+1}: '{line.strip()}'")

    if errors:
        print(json.dumps({"errors": ["Em dashes are prohibited. Use colons, commas, or parentheses instead."], "details": errors}))
        return 1
    else:
        print(json.dumps({"message": "Style check (no em dashes) passed"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_style(sys.argv[1]))
