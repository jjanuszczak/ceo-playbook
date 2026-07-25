#!/usr/bin/env python3
"""Validate local review-ready artifacts for an Editorial Agent content job."""

import argparse
import json
import re
from pathlib import Path

import yaml


REQUIRED_NOTE_HEADINGS = {
    "Brief and intended reader",
    "Content-type and taxonomy rationale",
    "Research basis and citations",
    "Internal linking record",
    "Featured image candidates and selected asset",
    "Social draft archive",
    "Validation record",
    "Open questions and human decisions",
}


def frontmatter(path: Path):
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        raise ValueError("No YAML frontmatter found")
    return yaml.safe_load(match.group(1)) or {}


def contextual_link_paths(content: str) -> set[str]:
    return set(re.findall(r'\]\(\{\{<\s*(?:ref|relref)\s+"([^"]+)"\s*>\}\}\)', content))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=Path, help="Content leaf bundle directory")
    parser.add_argument("--social-draft", type=Path, required=True)
    args = parser.parse_args()

    errors = []
    bundle = args.bundle
    index = bundle / "index.md"
    notes = bundle / "notes.md"
    needs_contextual_links = False

    if not index.is_file():
        errors.append(f"Missing index.md: {index}")
    else:
        try:
            index_content = index.read_text(encoding="utf-8")
            metadata = frontmatter(index)
            if metadata.get("draft") is not True:
                errors.append("Frontmatter must set draft: true")
            links = contextual_link_paths(index_content)
            if len(links) < 2:
                needs_contextual_links = True
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"Invalid frontmatter: {exc}")

    if not notes.is_file():
        errors.append(f"Missing notes.md: {notes}")
    else:
        headings = {
            line[3:].strip()
            for line in notes.read_text(encoding="utf-8").splitlines()
            if line.startswith("## ")
        }
        missing = sorted(REQUIRED_NOTE_HEADINGS - headings)
        if missing:
            errors.append(f"notes.md missing headings: {', '.join(missing)}")
        elif needs_contextual_links:
            notes_content = notes.read_text(encoding="utf-8")
            if "No contextual-link fit:" not in notes_content:
                errors.append("Missing contextual links or a documented No contextual-link fit exception")

    if not any(bundle.glob("featured.*")):
        errors.append("Missing selected featured image named featured.<extension>")

    if not args.social_draft.is_file():
        errors.append(f"Missing social draft archive: {args.social_draft}")
    else:
        social = args.social_draft.read_text(encoding="utf-8")
        if "## X" not in social or "## LinkedIn" not in social:
            errors.append("Social draft archive must contain X and LinkedIn sections")

    if errors:
        print(json.dumps({"errors": errors}))
        raise SystemExit(1)
    print(json.dumps({"message": "Editorial package is locally review-ready"}))


if __name__ == "__main__":
    main()
