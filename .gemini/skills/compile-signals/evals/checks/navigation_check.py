import os
import sys
import json

def check_navigation(post_path):
    errors = []
    
    try:
        with open(post_path, 'r') as f:
            content = f.read()
            
        # 1. Related posts check
        if "related-posts" not in content:
            errors.append("Missing related-posts shortcode")
        
        # 2. Read next check
        if "read-next" not in content:
            errors.append("Missing read-next shortcode")

    except Exception as e:
        errors.append(f"Failed to read post: {str(e)}")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({"message": "Navigation shortcodes found"}))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_navigation(sys.argv[1]))
