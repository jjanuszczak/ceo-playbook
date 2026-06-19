import os
import re
import sys
import argparse
from datetime import datetime

def get_button_text(section):
    mapping = {
        "articles": "View more Insights",
        "signals": "View more Signals",
        "lab": "View more Deep Dives",
        "videos": "View more Media"
    }
    return mapping.get(section, "View more")

def extract_meta(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                fm_content = match.group(1)
                date_match = re.search(r'date:\s*["\']?([\d-]{10})["\']?', fm_content)
                date = datetime.strptime(date_match.group(1), '%Y-%m-%d') if date_match else datetime.min
                draft_match = re.search(r'draft:\s*(true|false)', fm_content)
                draft = draft_match.group(1) == 'true' if draft_match else False
                return {'date': date, 'draft': draft}
    except Exception:
        pass
    return {'date': datetime.min, 'draft': True}

def get_posts_in_section(section_dir, content_root):
    posts = []
    for root, dirs, files in os.walk(section_dir):
        for file in files:
            if file.endswith('.md') and file != '_index.md':
                path = os.path.join(root, file)
                meta = extract_meta(path)
                # Keep track of draft status
                rel_path = os.path.relpath(path, content_root)
                hugo_path = rel_path.replace('/index.md', '').replace('.md', '')
                posts.append({'path': hugo_path, 'date': meta['date'], 'draft': meta['draft']})
    # Sort chronologically (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def main():
    parser = argparse.ArgumentParser(description='Find chronologically previous non-draft post.')
    parser.add_argument('target_file')
    parser.add_argument('--content-dir', default='content')
    args = parser.parse_args()

    target_rel = os.path.relpath(args.target_file, args.content_dir)
    target_hugo = target_rel.replace('/index.md', '').replace('.md', '')
    
    parts = target_rel.split(os.sep)
    if not parts: sys.exit(0)
    
    section = parts[0]
    section_dir = os.path.join(args.content_dir, section)
    
    all_posts = get_posts_in_section(section_dir, args.content_dir)
    
    # Find the current post in the sorted list
    current_index = -1
    for i, post in enumerate(all_posts):
        if post['path'] == target_hugo:
            current_index = i
            break
            
    # Search for the next non-draft post chronologically earlier
    link = None
    if current_index != -1:
        for i in range(current_index + 1, len(all_posts)):
            if not all_posts[i]['draft']:
                link = all_posts[i]['path']
                break
                
    if link:
        button_text = get_button_text(section)
        print(f"{link}|{button_text}")

if __name__ == "__main__":
    main()
