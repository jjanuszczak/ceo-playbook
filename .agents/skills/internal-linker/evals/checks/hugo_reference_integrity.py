from __future__ import annotations

import sys
from pathlib import Path

from common import content_path_exists, result, shortcode_paths


def main() -> int:
    target = Path(sys.argv[1])
    if not target.is_file():
        return result(["Target article does not exist"])
    paths = shortcode_paths(target.read_text(encoding="utf-8"))
    errors = []
    if not paths:
        errors.append("Target article contains no Hugo ref or relref links")
    if len(paths) != len(set(paths)):
        errors.append("Target article repeats an internal shortcode destination")
    if any(not content_path_exists(path) for path in paths):
        errors.append("One or more Hugo shortcode destinations do not exist")
    target_slug = target.parent.name
    if any(path.strip("/").endswith(target_slug) for path in paths):
        errors.append("Target article links to itself")
    return result(errors, destinations=paths)


if __name__ == "__main__":
    raise SystemExit(main())
