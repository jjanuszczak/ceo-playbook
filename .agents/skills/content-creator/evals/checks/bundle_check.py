import sys
import os
import json

# Mapping consistent with create_content.py
CONTENT_TYPE_MAP = {
    "article": "articles",
    "research": "research",
    "video": "videos",
    "lab": "lab",
    "portfolio": "portfolio",
    "signals": "signals"
}

def check_bundle(content_type, slug):
    if content_type not in CONTENT_TYPE_MAP:
        print(json.dumps({"errors": [f"Unknown content type: {content_type}"]} ))
        return 1
        
    dir_name = CONTENT_TYPE_MAP[content_type]
    
    # Expected relative path: content/<dir>/<slug>/index.md
    # We assume we are running from project root
    bundle_path = os.path.join("content", dir_name, slug)
    index_path = os.path.join(bundle_path, "index.md")
    
    errors = []
    
    if not os.path.exists(bundle_path):
        errors.append(f"Bundle directory not found: '{bundle_path}'")
    elif not os.path.isdir(bundle_path):
        errors.append(f"Path exists but is not a directory: '{bundle_path}'")
        
    if not os.path.exists(index_path):
        errors.append(f"index.md not found in bundle: '{index_path}'")
        
    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": f"Hugo bundle verified at {index_path}"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    sys.exit(check_bundle(sys.argv[1], sys.argv[2]))
