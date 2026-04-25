import os
import re
import sys
import argparse
from collections import Counter

def parse_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return None
            fm_content = match.group(1)
            
            # Check for externalUrl
            is_external = 'externalUrl:' in fm_content and re.search(r'externalUrl:\s*["\']?http', fm_content)
            
            # Check for draft
            is_draft = False
            draft_match = re.search(r'^draft:\s*(true|false)', fm_content, re.MULTILINE)
            if draft_match:
                is_draft = draft_match.group(1).lower() == 'true'
            
            # Extract tags
            tags = []
            inline_match = re.search(r'tags:\s*\[(.*?)\]', fm_content)
            if inline_match:
                tags_raw = inline_match.group(1)
                tags = [t.strip(' "\'') for t in tags_raw.split(',') if t.strip()]
            else:
                list_match = re.search(r'tags:\s*\n((?:[ ]+-[^\n]*\n?)+)', fm_content)
                if list_match:
                    block = list_match.group(1)
                    tags = re.findall(r'[ ]+-[ ]*["\']?(.*?)["\']?\s*\n', block + '\n')
                    tags = [t.strip() for t in tags if t.strip()]
                else:
                    single_match = re.search(r'tags:\s*([^\s\[\n]+)', fm_content)
                    if single_match:
                        tags = [single_match.group(1).strip(' "\'')]
            
            return {
                'tags': tags,
                'is_external': is_external,
                'is_draft': is_draft
            }
    except Exception as e:
        pass
    return None

def get_all_posts(content_dir):
    posts = []
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                fm = parse_frontmatter(path)
                if not fm or fm['is_external'] or fm['is_draft']:
                    continue
                if fm['tags']:
                    rel_path = os.path.relpath(path, content_dir)
                    hugo_path = rel_path.replace('/index.md', '').replace('.md', '')
                    posts.append({'path': hugo_path, 'tags': fm['tags']})
    return posts

def calculate_tag_weights(all_posts):
    tag_counts = Counter()
    for post in all_posts:
        for tag in post['tags']:
            tag_counts[tag] += 1
    return {tag: 1 / (count ** 0.5) if count > 0 else 0 for tag, count in tag_counts.items()}

def score_posts(target_tags, all_posts, tag_weights, target_path):
    scored = []
    target_tag_set = set(target_tags)
    for post in all_posts:
        if post['path'] == target_path or post['path'].startswith('signals/'):
            continue
        score = sum(tag_weights.get(tag, 1) for tag in target_tag_set.intersection(set(post['tags'])))
        if score > 0:
            scored.append((post['path'], score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target_file')
    parser.add_argument('--limit', type=int, default=2)
    parser.add_argument('--content-dir', default='content')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    fm = parse_frontmatter(args.target_file)
    if not fm or not fm['tags']: sys.exit(0)
    
    target_rel = os.path.relpath(args.target_file, args.content_dir)
    target_hugo = target_rel.replace('/index.md', '').replace('.md', '')

    all_posts = get_all_posts(args.content_dir)
    tag_weights = calculate_tag_weights(all_posts)
    related = score_posts(fm['tags'], all_posts, tag_weights, target_hugo)
    results = [path for path, score in related[:args.limit]]
    if results: print(", ".join(results))

if __name__ == "__main__":
    main()
