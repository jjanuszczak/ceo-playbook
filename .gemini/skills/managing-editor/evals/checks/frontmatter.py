import sys
import os
import re
import yaml
import json

def get_project_root(current_path):
    # Traverse up to find .git or GEMINI.md
    path = os.path.abspath(current_path)
    while path != os.path.dirname(path):
        if os.path.exists(os.path.join(path, "GEMINI.md")):
            return path
        path = os.path.dirname(path)
    return None

def check_frontmatter(article_path):
    errors = []
    
    if not os.path.exists(article_path):
        print(json.dumps({"errors": ["File not found"]}))
        return 1

    with open(article_path, 'r') as f:
        content = f.read()

    # Extract frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        print(json.dumps({"errors": ["No frontmatter found"]}))
        return 1
    
    fm_raw = match.group(1)
    try:
        fm = yaml.safe_load(fm_raw)
    except Exception as e:
        print(json.dumps({"errors": [f"YAML parse error: {str(e)}"]}))
        return 1

    root = get_project_root(article_path)
    if not root:
        errors.append("Could not determine project root to find governance policies")
    else:
        # Check Category
        category_policy_path = os.path.join(root, ".policies", "category_governance_policy.md")
        if os.path.exists(category_policy_path):
            with open(category_policy_path, 'r') as f:
                cat_policy = f.read()
            
            cats = fm.get('categories', [])
            if not cats:
                errors.append("No categories found in frontmatter")
            else:
                for cat in cats:
                    if f"* {cat}" not in cat_policy and f"- {cat}" not in cat_policy:
                        if cat not in cat_policy:
                            errors.append(f"Category '{cat}' is not in the governance policy")

    # Required Basic fields
    required_fields = ['title', 'date', 'summary', 'description']
    for field in required_fields:
        if field not in fm or not fm[field]:
            errors.append(f"Missing required basic frontmatter field: '{field}'")

    # AEO/SEO Semantic Fields (Advanced Schema)
    aeo_fields = ['about', 'mentions', 'citations']
    for field in aeo_fields:
        if field not in fm:
            errors.append(f"Missing AEO semantic field: '{field}'")
        elif not isinstance(fm[field], list):
            errors.append(f"AEO field '{field}' must be a list")
        elif len(fm[field]) == 0:
            errors.append(f"AEO field '{field}' is empty")
        else:
            # Check structure of items (should have name/title and url)
            for i, item in enumerate(fm[field]):
                if not isinstance(item, dict):
                    errors.append(f"AEO field '{field}' item {i+1} must be an object")
                    continue
                
                name_key = 'name' if field in ['about', 'mentions'] else 'title'
                if name_key not in item or not item[name_key]:
                    errors.append(f"AEO field '{field}' item {i+1} missing '{name_key}'")
                if 'url' not in item or not item['url']:
                    errors.append(f"AEO field '{field}' item {i+1} missing 'url'")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": "Frontmatter is valid and AEO compliant"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_frontmatter(sys.argv[1]))
