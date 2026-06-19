import sys
import os
import subprocess
import json

def check_build(article_path):
    # We ignore the article_path because hugo builds the whole site,
    # but we accept it for compatibility with the runner contract.
    
    # Try to find the project root (where hugo.toml is)
    current_dir = os.path.dirname(os.path.abspath(article_path))
    root = None
    path = current_dir
    while path != os.path.dirname(path):
        if os.path.exists(os.path.join(path, "config/_default/hugo.toml")) or os.path.exists(os.path.join(path, "hugo.toml")):
            root = path
            break
        path = os.path.dirname(path)

    if not root:
        print(json.dumps({"errors": ["Could not find Hugo project root to run build check"]}))
        return 1

    try:
        # Run hugo build
        # We use --minify to catch more potential issues and --quiet to reduce noise
        # but we need the error output if it fails.
        result = subprocess.run(
            ["hugo", "--minify"],
            cwd=root,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(json.dumps({"message": "Hugo build successful"}))
            return 0
        else:
            # Extract relevant lines from stderr
            # Hugo errors often look like: "ERROR 2024/05/18 ...: execute of template failed..."
            error_lines = [line.strip() for line in result.stderr.split('\n') if "ERROR" in line or "failed" in line]
            if not error_lines:
                error_lines = [result.stderr.strip()]
                
            print(json.dumps({
                "errors": ["Hugo build failed"],
                "hugo_output": error_lines
            }))
            return 1

    except FileNotFoundError:
        print(json.dumps({"errors": ["'hugo' command not found in PATH"]}))
        return 1
    except Exception as e:
        print(json.dumps({"errors": [f"Unexpected error during build check: {str(e)}"]}))
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_build(sys.argv[1]))
