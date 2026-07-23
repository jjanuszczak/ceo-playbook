from __future__ import annotations

import json
import subprocess
import sys

from common import FIXTURES, SKILL_DIR, result


def main() -> int:
    corpus = FIXTURES / "content" / "articles"
    target = corpus / "target-article" / "index.md"
    command = [sys.executable, str(SKILL_DIR / "scripts" / "find_link_candidates.py"), str(target), "--content-dir", str(corpus), "--limit", "4", "--as-of", "2026-07-15"]
    process = subprocess.run(command, capture_output=True, text=True)
    errors: list[str] = []
    try:
        output = json.loads(process.stdout)
    except json.JSONDecodeError:
        return result(["Candidate helper did not return JSON"], stderr=process.stderr)
    candidates = output.get("candidates", [])
    paths = [candidate.get("path") for candidate in candidates]
    expected = json.loads((FIXTURES / "expected-candidates.json").read_text(encoding="utf-8"))["paths"]
    if process.returncode != 0:
        errors.append("Candidate helper exited unsuccessfully")
    if output.get("target", {}).get("path") != "target-article":
        errors.append("Candidate helper returned the wrong target")
    if paths != expected:
        errors.append(f"Expected fixture ranking {expected}, received {paths}")
    if len(paths) != len(set(paths)):
        errors.append("Candidate paths must be unique")
    banned = {"draft-post", "external-post", "target-article"}
    if banned & set(paths):
        errors.append("Draft, external, or target content appeared in candidates")
    if any(not candidate.get("rationale") for candidate in candidates):
        errors.append("Every candidate must include ranking rationale")
    return result(errors, candidates=paths)


if __name__ == "__main__":
    raise SystemExit(main())
