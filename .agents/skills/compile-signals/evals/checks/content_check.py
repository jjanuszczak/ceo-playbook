import os
import sys
import json
import re

def check_content(post_path):
    errors = []
    
    try:
        with open(post_path, 'r') as f:
            content = f.read()
            
        # 1. Frontmatter check
        if not content.startswith('---'):
            errors.append("Missing YAML frontmatter start")
        
        # 2. Required fields in frontmatter
        required_fields = ["title:", "date:", "type: signals", "tags:"]
        for field in required_fields:
            if field not in content:
                errors.append(f"Missing required frontmatter field: {field}")
        
        # 3. Mandatory tags
        if "reading-list" not in content:
            errors.append("Missing mandatory tag: reading-list")

        # 4. Required intro paragraph after frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3 or not parts[2].strip():
            errors.append("Missing post body after frontmatter")
        else:
            body = parts[2].lstrip()
            if not body or body.startswith("## "):
                errors.append("Missing intro paragraph before first section heading")

        # 5. Mandatory sections
        required_headings = [
            "## Market Observations & Insights",
            "## Deep Reads from the Library",
            "## Highlights from the Stacks",
        ]
        for heading in required_headings:
            if heading not in content:
                errors.append(f"Missing heading: {heading}")

        # 6. Require at least one X embed and one x-article or x embed overall section content
        if "{{< x " not in content and "{{< x-article " not in content:
            errors.append("Missing X or X-article embeds in Market Observations section")

        # 7. Require deep read structure
        if "**Author:**" not in content:
            errors.append("Missing author lines in Deep Reads section")

        # 8. Require highlight structure
        if "{{< figure" not in content:
            errors.append("Missing figure shortcode in Highlights section")

        if "> " not in content:
            errors.append("Missing markdown blockquotes for highlights")

    except Exception as e:
        errors.append(f"Failed to read post: {str(e)}")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({"message": "Core content and shortcodes verified"}))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_content(sys.argv[1]))
