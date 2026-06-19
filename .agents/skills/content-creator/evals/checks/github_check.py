import sys
import subprocess
import json

def check_github(content_type, slug):
    # Construct a search query for the issue
    search_query = f"New {content_type.capitalize()} - {slug.replace('-', ' ').title()}"
    
    try:
        # Use gh CLI to search for the issue
        # We look for issues with the expected title
        result = subprocess.run(
            ["gh", "issue", "list", "--search", f'"{search_query}" in:title', "--json", "title,number"],
            capture_output=True,
            text=True,
            check=True
        )
        
        issues = json.loads(result.stdout)
        
        if issues:
            # Found at least one issue matching the title
            print(json.dumps({"message": f"GitHub issue found: #{issues[0]['number']} - {issues[0]['title']}"}))
            return 0
        else:
            print(json.dumps({"errors": [f"No GitHub issue found matching title: '{search_query}'"]}))
            return 1
            
    except Exception as e:
        # If gh CLI fails (e.g. no auth), we report as fail
        print(json.dumps({"errors": [f"GitHub check failed: {str(e)}"]}))
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    sys.exit(check_github(sys.argv[1], sys.argv[2]))
