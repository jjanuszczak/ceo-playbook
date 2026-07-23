from __future__ import annotations

import sys

from common import SKILL_DIR, result


def main() -> int:
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    required = [
        "name: internal-linker", "Hugo Markdown article", "2 to 4 outgoing", "2 to 4 incoming",
        "ref", "relref", "Further Reading", "Full Markdown Diff / Patch",
    ]
    errors = [f"SKILL.md is missing required contract text: {item}" for item in required if item not in skill]
    if not (SKILL_DIR / "scripts" / "find_link_candidates.py").is_file():
        errors.append("Candidate discovery helper is missing")
    return result(errors, checked=required)


if __name__ == "__main__":
    raise SystemExit(main())
