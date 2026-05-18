import sys
import os
import re
import json

def check_aeo(article_path):
    errors = []
    
    if not os.path.exists(article_path):
        print(json.dumps({"errors": ["File not found"]}))
        return 1

    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and body more reliably
    # Look for the second --- delimiter
    fm_parts = re.split(r'^---', content, maxsplit=2, flags=re.MULTILINE)
    if len(fm_parts) < 3:
        print(json.dumps({"errors": ["Invalid file structure (missing or malformed frontmatter)"]}))
        return 1
    
    body = fm_parts[2]

    # Check Quick Answer
    if "{{< quick-answer >}}" not in body:
        errors.append("Missing required '{{< quick-answer >}}' shortcode")
    else:
        # Check if it's near the top (e.g., before the first H2)
        h2_match = re.search(r'^##\s+', body, re.MULTILINE)
        qa_idx = body.find("{{< quick-answer >}}")
        if h2_match and qa_idx > h2_match.start():
            errors.append("'{{< quick-answer >}}' should be placed before the first H2 heading")

    # Check FAQ
    if "{{< faq >}}" not in body:
        errors.append("Missing required '{{< faq >}}' block")
    else:
        # Check for faq-item (allow both < > and % % variants just in case)
        if "{{% faq-item" not in body and "{{< faq-item" not in body:
            errors.append("'{{< faq >}}' block must contain at least one '{{% faq-item %}}'")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": "AEO compliance (Quick Answer & FAQ) verified"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_aeo(sys.argv[1]))
