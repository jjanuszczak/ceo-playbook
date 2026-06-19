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
            
        # 4. Mandatory sections
        if "Market Observations & Insights" not in content:
            errors.append("Missing heading: Market Observations & Insights")
        
        # 5. Mandatory footer elements
        if "Book a Call" not in content:
            errors.append("Missing mandatory CTA: Book a Call")
            
        if "relref \"signals\"" not in content:
            errors.append("Missing archive link to signals")

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
