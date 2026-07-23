from __future__ import annotations

from common import FIXTURES, fixture_content_path_exists, result, shortcode_paths


def main() -> int:
    report = (FIXTURES / "sample-report.md").read_text(encoding="utf-8")
    headings = ["# Optimization Report for:", "## Article Analysis", "## Recommended Outgoing Links", "## Recommended Incoming Links", "## Full Markdown Diff / Patch", "## Further Reading"]
    errors = [f"Report fixture is missing {heading}" for heading in headings if heading not in report]
    paths = shortcode_paths(report)
    if not paths:
        errors.append("Report fixture contains no Hugo references")
    if any(not fixture_content_path_exists(path) for path in paths):
        errors.append("Report fixture contains a reference outside the fixture corpus")
    return result(errors, destinations=paths)


if __name__ == "__main__":
    raise SystemExit(main())
