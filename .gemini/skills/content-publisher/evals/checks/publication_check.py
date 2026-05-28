import sys
import re

def check_publication(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    draft_match = re.search(r'^draft:\s*(true|false)', content, re.MULTILINE)
    status_match = re.search(r'^status:\s*"?([^"\n]*)"?', content, re.MULTILINE)
    date_match = re.search(r'^date:\s*(.*)', content, re.MULTILINE)

    if not draft_match:
        print("FAIL: 'draft' property missing.")
        return False
    
    if not status_match:
        print("FAIL: 'status' property missing.")
        return False

    if not date_match:
        print("FAIL: 'date' property missing.")
        return False

    draft = draft_match.group(1)
    status = status_match.group(1)

    if status == "published":
        if draft == "true":
            print("FAIL: Status is 'published' but 'draft' is true.")
            return False
    elif status == "review":
        if draft == "false":
            print("FAIL: Status is 'review' but 'draft' is false.")
            return False
    
    print(f"PASS: draft={draft}, status={status}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    
    success = check_publication(sys.argv[1])
    sys.exit(0 if success else 1)
