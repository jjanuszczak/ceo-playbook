import sys
import re

def fix_publication(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # If status is published, ensure draft is false
    if re.search(r'^status:\s*("published"|published)', content, re.MULTILINE):
        if re.search(r'^draft:\s*true', content, re.MULTILINE):
            print("Fixing: Setting draft to false for published post.")
            content = re.sub(r'^draft:\s*true', 'draft: false', content, flags=re.MULTILINE)
    
    # If status is review, ensure draft is true
    elif re.search(r'^status:\s*("review"|review)', content, re.MULTILINE):
        if re.search(r'^draft:\s*false', content, re.MULTILINE):
            print("Fixing: Setting draft to true for review post.")
            content = re.sub(r'^draft:\s*false', 'draft: true', content, flags=re.MULTILINE)

    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    fix_publication(sys.argv[1])
