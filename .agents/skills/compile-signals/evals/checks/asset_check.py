import os
import sys
import json
import glob
import re

def check_assets(post_path):
    errors = []
    post_dir = os.path.dirname(post_path)
    
    # 1. Featured image check
    featured_images = glob.glob(os.path.join(post_dir, "featured-week-*.png"))
    if not featured_images:
        errors.append("Missing featured-week-xx-yyyy.png image")

    try:
        with open(post_path, 'r') as f:
            content = f.read()

        figure_sources = re.findall(r'src="([^"]+)"', content)
        local_pngs = [
            src for src in figure_sources
            if not src.startswith("http://") and not src.startswith("https://") and src.lower().endswith(".png")
        ]

        for src in local_pngs:
            asset_path = os.path.join(post_dir, src)
            if not os.path.exists(asset_path):
                errors.append(f"Missing local figure asset: {src}")

        if "## Highlights from the Stacks" in content and not local_pngs:
            errors.append("Highlights section exists but no local PNG figure assets were found")

    except Exception as e:
        errors.append(f"Failed to inspect post assets: {str(e)}")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    
    print(json.dumps({
        "message": "Assets verified",
        "found_images": [os.path.basename(i) for i in featured_images],
        "found_figures": local_pngs if 'local_pngs' in locals() else []
    }))
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_assets(sys.argv[1]))
