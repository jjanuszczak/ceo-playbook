#!/usr/bin/env python3
"""Rank related published Hugo articles for an internal-linking review."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any

STOPWORDS = {
    "about", "after", "all", "also", "and", "are", "articles", "away", "because",
    "but", "buttontext", "can", "for", "from", "has", "have", "into", "its", "not",
    "our", "that", "the", "their", "this", "was", "what", "will", "with", "you", "your",
}


def frontmatter_and_body(text: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    return (match.group(1), match.group(2)) if match else ("", text)


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?([^\n\"']*)", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""


def values(frontmatter: str, key: str) -> list[str]:
    inline = re.search(rf"^{re.escape(key)}:\s*\[([^]]*)\]", frontmatter, re.MULTILINE)
    if inline:
        return [item.strip().strip("\"'") for item in inline.group(1).split(",") if item.strip()]
    block = re.search(rf"^{re.escape(key)}:\s*\n((?:\s+-\s*[^\n]+\n?)+)", frontmatter, re.MULTILINE)
    if block:
        return [item.strip().strip("\"'") for item in re.findall(r"^\s+-\s*(.+)$", block.group(1), re.MULTILINE)]
    single = scalar(frontmatter, key)
    return [single] if single else []


def tokens(text: str) -> set[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z-]{2,}", text.lower())
    return {word for word in words if word not in STOPWORDS}


def hugo_path(markdown_path: Path, content_dir: Path) -> str:
    relative = markdown_path.relative_to(content_dir).as_posix()
    return relative.removesuffix("/index.md").removesuffix(".md")


def parse_article(path: Path, content_dir: Path) -> dict[str, Any] | None:
    frontmatter, body = frontmatter_and_body(path.read_text(encoding="utf-8"))
    if not frontmatter or scalar(frontmatter, "draft").lower() == "true":
        return None
    if re.search(r"^externalUrl:\s*[\"']?https?://", frontmatter, re.MULTILINE):
        return None
    title = scalar(frontmatter, "title")
    if not title:
        return None
    return {
        "file": str(path), "path": hugo_path(path, content_dir), "title": title,
        "date": scalar(frontmatter, "date"), "tags": values(frontmatter, "tags"),
        "categories": values(frontmatter, "categories"),
        "summary": scalar(frontmatter, "summary") or scalar(frontmatter, "description"),
        "keywords": tokens(" ".join([title, scalar(frontmatter, "summary"), scalar(frontmatter, "description"), body])),
    }


def parsed_date(value: str) -> date | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def recency_score(value: str, as_of: date) -> float:
    published = parsed_date(value)
    if not published:
        return 0.0
    age_days = max((as_of - published).days, 0)
    return math.exp(-age_days / 548)  # Half-life of roughly 18 months.


def candidate(target: dict[str, Any], other: dict[str, Any], tag_frequency: Counter[str], as_of: date) -> dict[str, Any] | None:
    shared_tags = sorted(set(target["tags"]) & set(other["tags"]))
    shared_categories = sorted(set(target["categories"]) & set(other["categories"]))
    overlap = target["keywords"] & other["keywords"]
    if not (shared_tags or shared_categories or overlap):
        return None
    tag_score = sum(1 / math.sqrt(tag_frequency[tag]) for tag in shared_tags)
    keyword_score = min(len(overlap), 12) / 12
    score = tag_score * 3 + len(shared_categories) * 1.5 + keyword_score + recency_score(other["date"], as_of) * 0.5
    rationale = []
    if shared_tags:
        rationale.append("shared tags: " + ", ".join(shared_tags))
    if shared_categories:
        rationale.append("shared categories: " + ", ".join(shared_categories))
    if overlap:
        rationale.append("keyword overlap: " + ", ".join(sorted(overlap)[:6]))
    return {**{key: other[key] for key in ("title", "path", "file", "date", "summary")}, "score": round(score, 3), "rationale": rationale}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Target Hugo Markdown file")
    parser.add_argument("--content-dir", default="content/articles", help="Published article corpus")
    parser.add_argument("--limit", type=int, default=4, choices=range(1, 11), metavar="1-10")
    parser.add_argument("--as-of", help="Use YYYY-MM-DD as the ranking date for reproducible results")
    args = parser.parse_args()
    content_dir = Path(args.content_dir).resolve()
    target_path = Path(args.target).resolve()
    if not content_dir.is_dir() or not target_path.is_file():
        parser.error("target and content directory must exist")
    articles = [article for file in content_dir.rglob("*.md") if (article := parse_article(file, content_dir))]
    target = next((article for article in articles if Path(article["file"]) == target_path), None)
    if not target:
        parser.error("target must be a published Markdown article inside --content-dir")
    try:
        as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
    except ValueError:
        parser.error("--as-of must use YYYY-MM-DD")
    tag_frequency = Counter(tag for article in articles for tag in article["tags"])
    ranked = [candidate(target, article, tag_frequency, as_of) for article in articles if article["path"] != target["path"]]
    ranked = sorted((item for item in ranked if item), key=lambda item: (-item["score"], item["path"]))[: args.limit]
    print(json.dumps({"target": {key: target[key] for key in ("title", "path", "file", "date", "tags", "categories")}, "candidates": ranked}, indent=2))


if __name__ == "__main__":
    main()
