#!/usr/bin/env python3
"""Generate and validate campaign URLs for X and LinkedIn social drafts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_CAMPAIGNS = {
    "content/articles": "thought-leadership",
    "content/signals": "weekly-signals",
    "content/lab": "tech-lab",
}
DEFAULT_SOURCES = {"x": "x", "linkedin": "linkedin"}


def project_root(source_file: Path, explicit_root: str | None) -> Path:
    if explicit_root:
        root = Path(explicit_root).resolve()
        if not (root / ".hs.toml").is_file():
            raise ValueError(f"No .hs.toml found in project directory: {root}")
        return root
    for parent in (source_file.resolve(), *source_file.resolve().parents):
        if (parent / ".hs.toml").is_file():
            return parent
    raise ValueError("Could not find a project directory containing .hs.toml")


def default_campaign(source_file: Path, root: Path) -> str:
    try:
        relative = source_file.resolve().relative_to(root)
    except ValueError as error:
        raise ValueError(f"Source file is outside project directory: {source_file}") from error
    normalized = relative.as_posix()
    for prefix, campaign in DEFAULT_CAMPAIGNS.items():
        if normalized == prefix or normalized.startswith(f"{prefix}/"):
            return campaign
    raise ValueError(
        "No default campaign for this content path. Ask the user for a campaign override: "
        f"{relative}"
    )


def run_hs(command: list[str]) -> dict[str, object]:
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(message)
    return json.loads(completed.stdout)


def generate_link(source_file: Path, root: Path, campaign: str, source: str, medium: str) -> dict[str, object]:
    linked = run_hs(
        [
            "hs",
            "campaign",
            "link",
            str(source_file),
            str(root),
            "--campaign",
            campaign,
            "--source",
            source,
            "--medium",
            medium,
            "--format",
            "json",
        ]
    )
    url = str(linked["url"])
    validated = run_hs(["hs", "campaign", "validate", url, str(root), "--format", "json"])
    return {"url": url, "campaign": linked["campaign"], "source": source, "medium": linked["medium"], "validation": validated}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_content_file", type=Path)
    parser.add_argument("--project-directory")
    parser.add_argument("--campaign")
    parser.add_argument("--medium", default="social")
    parser.add_argument("--source", help="Override the source for both channels.")
    parser.add_argument("--x-source")
    parser.add_argument("--linkedin-source")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_file = args.source_content_file.resolve()
    if not source_file.is_file():
        raise ValueError(f"Source content file does not exist: {source_file}")
    root = project_root(source_file, args.project_directory)
    campaign = args.campaign or default_campaign(source_file, root)
    shared_source = args.source
    sources = {
        "x": args.x_source or shared_source or DEFAULT_SOURCES["x"],
        "linkedin": args.linkedin_source or shared_source or DEFAULT_SOURCES["linkedin"],
    }
    links = {
        channel: generate_link(source_file, root, campaign, source, args.medium)
        for channel, source in sources.items()
    }
    print(
        json.dumps(
            {
                "source_content_file": str(source_file),
                "campaign": campaign,
                "medium": args.medium,
                "links": links,
            }
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
