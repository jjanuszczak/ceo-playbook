import os
import sys
import json
import glob

def check_assets(post_path):
    errors = []
    post_dir = os.path.dirname(post_path)
    
    # 1. Featured image check
    featured_images = glob.glob(os.path.join(post_dir, "featured-week-*.png"))
    if not featured_images:
        errors.append("Missing featured-week-xx-yyyy.png image")
    
    # Optional: could check for other images if they are referenced in the post

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({"message": "Assets verified", "found_images": [os.path.basename(i) for i in featured_images]}))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_assets(sys.argv[1]))
