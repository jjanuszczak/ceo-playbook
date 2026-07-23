from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
SKILL_DIR = Path(__file__).resolve().parents[2]
FIXTURES = SKILL_DIR / "evals" / "fixtures"


def result(errors: list[str], **details: object) -> int:
    print(json.dumps(({"errors": errors} if errors else {"message": "Check passed"}) | details))
    return 1 if errors else 0


def content_path_exists(hugo_path: str) -> bool:
    normalized = hugo_path.strip().strip('"\'').strip("/")
    for suffix in ("/index.md", ".md"):
        if (ROOT / "content" / f"{normalized}{suffix}").is_file():
            return True
    return False


def fixture_content_path_exists(hugo_path: str) -> bool:
    normalized = hugo_path.strip().strip('"\'').strip("/")
    if normalized.startswith("articles/"):
        normalized = normalized.removeprefix("articles/")
    fixture_articles = FIXTURES / "content" / "articles"
    return any((fixture_articles / f"{normalized}{suffix}").is_file() for suffix in ("/index.md", ".md"))


def shortcode_paths(text: str) -> list[str]:
    return re.findall(r'{{<\s*(?:ref|relref)\s+["\']([^"\']+)["\']\s*>}}', text)


def digest_tree(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        digest.update(path.relative_to(directory).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()
