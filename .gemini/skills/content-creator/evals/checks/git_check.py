import sys
import subprocess
import json

def check_git(content_type, slug):
    expected_branch = f"feature/{content_type}-{slug}"
    
    try:
        # Get current branch
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        current_branch = result.stdout.strip()
        
        if current_branch == expected_branch:
            print(json.dumps({"message": f"Correctly on branch '{current_branch}'"}))
            return 0
        else:
            # Check if the branch exists at all
            check_exists = subprocess.run(
                ["git", "branch", "--list", expected_branch],
                capture_output=True,
                text=True
            )
            if expected_branch in check_exists.stdout:
                 print(json.dumps({"errors": [f"Branch '{expected_branch}' exists but is not checked out. Current: '{current_branch}'"]}))
            else:
                 print(json.dumps({"errors": [f"Branch '{expected_branch}' does not exist"]} ))
            return 1
            
    except Exception as e:
        print(json.dumps({"errors": [f"Git check failed: {str(e)}"]}))
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    sys.exit(check_git(sys.argv[1], sys.argv[2]))
