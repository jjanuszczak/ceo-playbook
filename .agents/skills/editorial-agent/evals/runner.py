#!/usr/bin/env python3
"""Run Editorial Agent deterministic checks for one content package."""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run(command, cwd=None):
    result = subprocess.run(command, capture_output=True, text=True, cwd=cwd)
    return {
        "status": "PASS" if result.returncode == 0 else "FAIL",
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--social-draft", type=Path, required=True)
    args = parser.parse_args()

    skill_project_root = Path(__file__).resolve().parents[4]
    project_root = Path.cwd().resolve()
    validator = skill_project_root / ".agents/skills/editorial-agent/scripts/validate_editorial_package.py"
    bundle = args.bundle.resolve()
    social_draft = args.social_draft.resolve()
    package = run(
        [sys.executable, str(validator), str(bundle), "--social-draft", str(social_draft)],
        project_root,
    )
    hugo = run(["hugo", "--minify"], project_root)
    report = {
        "timestamp": datetime.now().isoformat(),
        "bundle": str(bundle),
        "social_draft": str(social_draft),
        "overall_status": "PASS" if package["status"] == "PASS" and hugo["status"] == "PASS" else "FAIL",
        "checks": [
            {"id": "editorial_package", "name": "Editorial package validation", **package},
            {"id": "hugo_build", "name": "Hugo build", **hugo},
        ],
    }
    reports = Path(__file__).resolve().parent / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "latest_results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["overall_status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
