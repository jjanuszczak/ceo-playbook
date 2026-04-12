import os
import re
import sys
import argparse
from collections import Counter

def has_external_url(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return 'externalUrl:' in f.read()
    except:
        return False

def extract_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                fm_content = match.group(1)
                inline_match = re.search(r'tags:\s*\[(.*?)\]', fm_content)
                if inline_match:
                    tags_raw = inline_match.group(1)
                    return [t.strip(' "\'') for t in tags_raw.split(',') if t.strip()]
                list_match = re.search(r'tags:\s*\n((?:[ ]+-[^\n]*\n?)+)', fm_content)
                if list_match:
                    block = list_match.group(1)
                    tags = re.findall(r'[ ]+-[ ]*["\']?(.*?)["\']?\s*\n', block + '\n')
                    return [t.strip() for t in tags if t.strip()]
                single_match = re.search(r'tags:\s*([^\s\[]+)', fm_content)
                if single_match:
                    return [single_match.group(1).strip(' "\'')]
    except Exception as e:
        pass
    return []

def get_all_posts(content_dir):
    posts = []
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                if has_external_url(path):
                    continue
                tags = extract_tags(path)
                if tags:
                    rel_path = os.path.relpath(path, content_dir)
                    hugo_path = rel_path.replace('/index.md', '').replace('.md', '')
                    posts.append({'path': hugo_path, 'tags': tags})
    return posts

def calculate_tag_weights(all_posts):
    tag_counts = Counter()
    for post in all_posts:
        for tag in post['tags']:
            tag_counts[tag] += 1
    return {tag: 1 / (count ** 0.5) for tag, count in tag_counts.items()}

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

    target_tags = extract_tags(args.target_file)
    if not target_tags: sys.exit(0)
    target_rel = os.path.relpath(args.target_file, args.content_dir)
    target_hugo = target_rel.replace('/index.md', '').replace('.md', '')

    all_posts = get_all_posts(args.content_dir)
    tag_weights = calculate_tag_weights(all_posts)
    related = score_posts(target_tags, all_posts, tag_weights, target_hugo)
    results = [path for path, score in related[:args.limit]]
    if results: print(", ".join(results))

if __name__ == "__main__":
    main()
