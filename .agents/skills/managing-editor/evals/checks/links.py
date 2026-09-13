import sys
import os
import re
import json


CONTEXTUAL_LINK = re.compile(r'\]\(\{\{<\s*(?:ref|relref)\s+"([^"]+)"\s*>\}\}\)')

def check_links(article_path):
    errors = []
    
    if not os.path.exists(article_path):
        print(json.dumps({"errors": ["File not found"]}))
        return 1

    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()

    contextual_paths = set(CONTEXTUAL_LINK.findall(content))

    if len(contextual_paths) < 2:
        notes_path = os.path.join(os.path.dirname(article_path), "notes.md")
        no_fit_exception = False
        if os.path.isfile(notes_path):
            with open(notes_path, 'r', encoding='utf-8') as f:
                no_fit_exception = "No contextual-link fit:" in f.read()
        if not no_fit_exception:
            errors.append("Missing at least two contextual Hugo ref or relref links")

    if errors:
        print(json.dumps({"errors": errors}))
        return 1
    else:
        print(json.dumps({"message": f"Contextual linking verified with {len(contextual_paths)} Hugo links"}))
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    sys.exit(check_links(sys.argv[1]))
