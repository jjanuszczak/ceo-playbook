from __future__ import annotations

import subprocess
import sys

from common import FIXTURES, SKILL_DIR, digest_tree, result


def main() -> int:
    corpus = FIXTURES / "content" / "articles"
    target = corpus / "target-article" / "index.md"
    before = digest_tree(corpus)
    process = subprocess.run([sys.executable, str(SKILL_DIR / "scripts" / "find_link_candidates.py"), str(target), "--content-dir", str(corpus), "--as-of", "2026-07-15"], capture_output=True, text=True)
    after = digest_tree(corpus)
    errors = []
    if process.returncode != 0:
        errors.append("Candidate helper failed while checking read-only behavior")
    if before != after:
        errors.append("Candidate helper modified the fixture corpus")
    return result(errors)


if __name__ == "__main__":
    raise SystemExit(main())
