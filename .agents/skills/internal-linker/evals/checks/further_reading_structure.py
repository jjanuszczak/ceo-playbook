from __future__ import annotations

import re
import sys
from pathlib import Path

from common import result, shortcode_paths


def main() -> int:
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    section = re.search(r"^## Further Reading\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.MULTILINE)
    if not section:
        return result([], message="No Further Reading section to validate")
    body = section.group(1)
    paths = shortcode_paths(body)
    errors = []
    if not 2 <= len(paths) <= 4:
        errors.append("Further Reading must contain two to four Hugo links")
    if len(paths) != len(set(paths)):
        errors.append("Further Reading destinations must be unique")
    navigation_positions = [text.find("{{< related-posts"), text.find("{{< read-next")]
    if not any(position > section.start() for position in navigation_positions):
        errors.append("Further Reading must appear before related-content navigation")
    if re.search(r"https?://", body):
        errors.append("Further Reading must not contain bare external URLs")
    return result(errors, destinations=paths)


if __name__ == "__main__":
    raise SystemExit(main())
