#!/usr/bin/env python3
"""Stage human-reviewed X quote-post drafts from published Signals content."""

from __future__ import annotations

import argparse
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
SIGNALS_DIR = ROOT / "content" / "signals"
STATE_PATH = ROOT / "data" / "signals-x-quotes" / "queue.json"
CARD_PATH = ROOT / "docs" / "repurposed" / "signals-x-quote-queue.md"
BASE_URL = "https://januszczak.org"
X_URL = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/[^\s)]+", re.IGNORECASE)
X_SHORTCODE = re.compile(r"{{<\s*(x|x-article)\s+([^>]+?)\s*>}}")
ATTR = re.compile(r'(\w+)="([^"]+)"')


def now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def read_state() -> dict[str, Any]:
    return json.loads(STATE_PATH.read_text()) if STATE_PATH.exists() else {"version": 1, "items": []}


def write_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def frontmatter_and_body(path: Path) -> tuple[dict[str, str], str]:
    raw = path.read_text()
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.DOTALL)
    if not match:
        return {}, raw
    fields = {}
    for line in match.group(1).splitlines():
        parsed = re.match(r"^(\w+):\s*(.*)$", line)
        if parsed:
            fields[parsed.group(1)] = parsed.group(2).strip().strip('"')
    return fields, match.group(2)


def published_signals() -> list[tuple[str, str, Path, str]]:
    posts = []
    for path in SIGNALS_DIR.glob("*/index.md"):
        frontmatter, body = frontmatter_and_body(path)
        date = frontmatter.get("date", "")
        if frontmatter.get("type") == "signals" and frontmatter.get("draft", "false").lower() != "true" and re.match(r"^\d{4}-\d{2}-\d{2}", date):
            posts.append((date, frontmatter.get("title", path.parent.name), path, body))
    return sorted(posts, key=lambda post: post[0], reverse=True)


def field(section: str, label: str) -> str | None:
    found = re.search(rf"^\s*\*\s*\*\*{re.escape(label)}:\*\*\s*(.+)$", section, re.MULTILINE)
    return found.group(1).strip() if found else None


def source(section: str) -> tuple[str, str] | None:
    shortcode = X_SHORTCODE.search(section)
    if shortcode:
        attrs = dict(ATTR.findall(shortcode.group(2)))
        if attrs.get("id") and attrs.get("user"):
            kind = "article" if shortcode.group(1) == "x-article" else "post"
            return kind, f"https://x.com/{attrs['user']}/status/{attrs['id']}"
    link = X_URL.search(section)
    return ("post", link.group(0).rstrip(".,")) if link else None


def candidates() -> list[dict[str, str]]:
    result = []
    for date, title, path, body in published_signals():
        headings = list(re.finditer(r"^###\s+(.+?)\s*$", body, re.MULTILINE))
        for index, heading in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
            section = body[heading.start():end]
            x_source = source(section)
            summary, why, take = field(section, "Summary"), field(section, "Why it Matters"), field(section, "My Take")
            if not x_source or not all((summary, why, take)):
                continue
            kind, source_url = x_source
            result.append({
                "signal_post_url": f"{BASE_URL}/signals/{path.parent.name}/",
                "signal_post_title": title,
                "signal_date": date,
                "source_x_id_or_url": source_url,
                "source_type": kind,
                "section_title": heading.group(1).strip(),
                "summary": summary,
                "why_it_matters": why,
                "my_take": take,
            })
    return result


def make_draft(item: dict[str, str]) -> str:
    return (f"Summary: {item['summary']}\n\nWhy it matters: {item['why_it_matters']}\n\n"
            f"My take: {item['my_take']}\n\nFull Signals: {item['signal_post_url']}")


def find_item(state: dict[str, Any], source_value: str) -> dict[str, Any]:
    for item in state["items"]:
        if item["source_x_id_or_url"] == source_value or source_value in item["source_x_id_or_url"]:
            return item
    raise SystemExit(f"No queue item matches: {source_value}")


def write_card(item: dict[str, Any]) -> None:
    CARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    CARD_PATH.write_text(
        "# Signals X Quote-Post Queue\n\n"
        f"**Status:** {item['status']}\n\n"
        f"**Signals:** [{item['signal_post_title']}]({item['signal_post_url']})\n\n"
        f"**Original X source:** {item['source_x_id_or_url']}\n\n"
        f"**Section:** {item['section_title']}\n\n"
        f"**Character count:** {item['character_count']}/280\n\n"
        "## Ready-to-paste quote text\n\n"
        f"{item['draft_text']}\n\n"
        "## Manual publish checklist\n\n"
        "1. Open the original X source above.\n2. Choose Quote in X’s native UI.\n3. Paste the approved text and publish.\n4. Record the result with `mark-posted`.\n"
    )


def stage(_: argparse.Namespace) -> None:
    state = read_state()
    open_items = [item for item in state["items"] if item["status"] in {"ready", "deferred"}]
    if open_items:
        item = open_items[0]
        write_card(item)
        print(f"[ACTION REQUIRED] Existing {item['status']} quote-post draft: {item['source_x_id_or_url']}")
        print(f"Queue card: {CARD_PATH.relative_to(ROOT)} ({item['character_count']}/280 characters)")
        return
    known = {item["source_x_id_or_url"] for item in state["items"]}
    item = next((candidate for candidate in candidates() if candidate["source_x_id_or_url"] not in known), None)
    if not item:
        print("[UPDATE] No eligible unshared X sources found in published Signals posts.")
        return
    item.update({"draft_text": make_draft(item), "status": "ready", "created_at": now(), "approved_at": None, "posted_at": None, "published_x_url": None})
    item["character_count"] = len(item["draft_text"])
    state["items"].append(item)
    write_state(state)
    write_card(item)
    print(f"[ACTION REQUIRED] Staged next Signals quote-post draft: {item['section_title']}")
    print(f"Source: {item['source_x_id_or_url']}")
    print(f"Queue card: {CARD_PATH.relative_to(ROOT)} ({item['character_count']}/280 characters)")
    if item["character_count"] > 280:
        print("[ACTION REQUIRED] Draft exceeds 280 characters. Edit it before using X’s native Quote action.")


def list_items(_: argparse.Namespace) -> None:
    state = read_state()
    if not state["items"]:
        print("[UPDATE] Queue is empty.")
    for item in state["items"]:
        print(f"[{item['status'].upper()}] {item['section_title']} | {item['source_x_id_or_url']}")


def set_draft(args: argparse.Namespace) -> None:
    state = read_state()
    item = find_item(state, args.source)
    item.update({"draft_text": args.text.strip(), "character_count": len(args.text.strip()), "approved_at": now(), "status": "ready"})
    write_state(state)
    write_card(item)
    print(f"[UPDATE] Saved draft ({item['character_count']}/280 characters).")


def transition(args: argparse.Namespace, status: str) -> None:
    state = read_state()
    item = find_item(state, args.source)
    item["status"] = status
    if status == "posted":
        item["posted_at"] = now()
        item["published_x_url"] = args.published_url
    write_state(state)
    print(f"[UPDATE] Marked {item['section_title']} as {status}.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("stage").set_defaults(func=stage)
    commands.add_parser("list").set_defaults(func=list_items)
    draft = commands.add_parser("set-draft")
    draft.add_argument("--source", required=True)
    draft.add_argument("--text", required=True)
    draft.set_defaults(func=set_draft)
    for name, status in (("mark-posted", "posted"), ("skip", "skipped"), ("defer", "deferred")):
        command = commands.add_parser(name)
        command.add_argument("--source", required=True)
        if status == "posted":
            command.add_argument("--published-url", required=True)
        command.set_defaults(func=lambda args, value=status: transition(args, value))
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.func(args)
