import sys
import os
import re
import json

def check_links(article_path):
    errors = []
    
    if not os.path.exists(article_path):
        print(json.dumps({"errors": ["File not found"]}))
        return 1

    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check Related Posts
    if "{{< related-posts" not in content:
        errors.append("Missing '{{< related-posts >}}' shortcode")
    else:
        # Check for paths parameter
        if 'paths="' not in content:
            errors.append("'{{< related-posts >}}' shortcode is missing the 'paths' parameter")
    
    # Check Read Next
    if "{{< read-next" not in content:
        errors.append("Missing '{{< read-next >}}' shortcode")
    else:
        # Check for link parameter
        if 'link="' not in content:
            errors.append("'{{< read-next >}}' shortcode is missing the 'link' parameter")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": "Semantic navigation (Related Posts & Read Next) verified with parameters"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_links(sys.argv[1]))
