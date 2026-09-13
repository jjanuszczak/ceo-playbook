import os
import sys
import json

def check_navigation(post_path):
    errors = []
    
    try:
        with open(post_path, 'r') as f:
            content = f.read()
            
        deprecated_shortcodes = {
            "subscribe": "{{< subscribe >}}",
            "related-posts": "{{< related-posts",
            "read-next": "{{< read-next",
        }
        for name, marker in deprecated_shortcodes.items():
            if marker in content:
                errors.append(f"Deprecated {name} shortcode found")

    except Exception as e:
        errors.append(f"Failed to read post: {str(e)}")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({"message": "No deprecated footer shortcodes found"}))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_navigation(sys.argv[1]))
