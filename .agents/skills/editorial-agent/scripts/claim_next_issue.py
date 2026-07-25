#!/usr/bin/env python3
"""Claim one eligible Editorial Agent backlog issue."""

import argparse
import json
import subprocess
import sys


def run(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Report the next eligible issue without changing it")
    args = parser.parse_args()

    raw = run([
        "gh", "issue", "list", "--state", "open", "--label", "editorial:ready",
        "--limit", "20", "--json", "number,title,body,labels,url",
    ])
    issues = json.loads(raw)
    eligible = [
        issue for issue in issues
        if "editorial:blocked" not in {label["name"] for label in issue["labels"]}
    ]
    if not eligible:
        print(json.dumps({"status": "empty", "message": "No eligible editorial backlog issues"}))
        return

    issue = sorted(eligible, key=lambda item: item["number"])[0]
    result = {"status": "ready", "issue": issue}
    if args.dry_run:
        print(json.dumps(result))
        return

    number = str(issue["number"])
    run([
        "gh", "issue", "edit", number,
        "--remove-label", "editorial:ready",
        "--add-label", "editorial:in-progress",
    ])
    comment = (
        "## Editorial Agent claim\n\n"
        "- Status: `editorial:in-progress`\n"
        "- Brief assessment: pending intake\n"
        "- Next action: assess source material and select content type\n"
    )
    run(["gh", "issue", "comment", number, "--body", comment])
    result["status"] = "claimed"
    print(json.dumps(result))


if __name__ == "__main__":
    main()
