import os
import sys
import json

def check_structure(post_path):
    errors = []
    
    if not os.path.exists(post_path):
        errors.append(f"Post file not found: {post_path}")
    else:
        post_dir = os.path.dirname(post_path)
        if not os.path.isdir(post_dir):
            errors.append(f"Parent directory not found for: {post_path}")
        
        filename = os.path.basename(post_path)
        if filename != "index.md":
             errors.append(f"Filename should be index.md, found: {filename}")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({"message": "Directory and file structure valid"}))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_structure(sys.argv[1]))
