#!/usr/bin/env python3
"""Exercise campaign URL generation through the public hs CLI."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[5]
GENERATOR = REPO_ROOT / ".agents/skills/repurpose-social/scripts/generate_campaign_links.py"


def write_fixture(root: Path, path: str) -> Path:
    content = root / path
    content.parent.mkdir(parents=True, exist_ok=True)
    content.write_text("---\ntitle: Fixture\ndate: 2026-01-01\n---\nFixture body.\n")
    return content


def run_generator(content_file: Path, root: Path, *overrides: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(GENERATOR), str(content_file), "--project-directory", str(root), *overrides],
        capture_output=True,
        text=True,
    )


def assert_link(link: dict[str, object], campaign: str, source: str, medium: str) -> None:
    query = parse_qs(urlparse(str(link["url"])).query)
    assert query == {"utm_campaign": [campaign], "utm_source": [source], "utm_medium": [medium]}
    assert link["campaign"] == campaign
    assert link["source"] == source
    assert link["medium"] == medium
    assert link["validation"]["campaign"] == campaign
    assert link["validation"]["medium"] == medium


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / ".hs.toml").write_text((REPO_ROOT / ".hs.toml").read_text())
        (root / "hugo.toml").write_text('baseURL = "https://januszczak.org/"\n')
        defaults = {
            "content/articles/example/index.md": "thought-leadership",
            "content/signals/example/index.md": "weekly-signals",
            "content/lab/example/index.md": "tech-lab",
        }
        checked = []
        for path, campaign in defaults.items():
            completed = run_generator(write_fixture(root, path), root)
            assert completed.returncode == 0, completed.stderr
            payload = json.loads(completed.stdout)
            assert payload["campaign"] == campaign
            assert_link(payload["links"]["x"], campaign, "x", "social")
            assert_link(payload["links"]["linkedin"], campaign, "linkedin", "social")
            checked.append(campaign)

        overridden = run_generator(
            write_fixture(root, "content/articles/override/index.md"),
            root,
            "--campaign",
            "weekly-signals",
            "--medium",
            "paid_social",
            "--linkedin-source",
            "messenger",
        )
        assert overridden.returncode == 0, overridden.stderr
        payload = json.loads(overridden.stdout)
        assert_link(payload["links"]["x"], "weekly-signals", "x", "paid_social")
        assert_link(payload["links"]["linkedin"], "weekly-signals", "messenger", "paid_social")

        invalid = run_generator(
            write_fixture(root, "content/articles/invalid/index.md"), root, "--medium", "email"
        )
        assert invalid.returncode != 0
        assert "not approved" in invalid.stderr
    print(json.dumps({"campaigns_checked": checked, "overrides_checked": True, "invalid_override_rejected": True}))


if __name__ == "__main__":
    main()
