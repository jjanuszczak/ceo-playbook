#!/usr/bin/env python3
"""Return horizontal Pixabay photo candidates as structured JSON.

Requires PIXABAY_API_KEY. This script searches only. The Editorial Agent must
record rights and attribution before committing a selected asset.
"""

import argparse
import json
import os
import ssl
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def project_root() -> Path:
    """Return the repository root without relying on the current directory."""
    for directory in Path(__file__).resolve().parents:
        if (directory / ".git").exists():
            return directory
    raise RuntimeError("Could not locate the repository root")


def pixabay_api_key() -> str | None:
    """Read the key from the process environment or the project .env file.

    Environment variables take precedence. The narrow parser intentionally reads
    only PIXABAY_API_KEY and never writes it to stdout or logs.
    """
    key = os.environ.get("PIXABAY_API_KEY")
    if key:
        return key

    env_file = project_root() / ".env"
    if not env_file.is_file():
        return None
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        name, separator, value = line.partition("=")
        if name.strip() != "PIXABAY_API_KEY" or not separator:
            continue
        return value.strip().strip('"').strip("'") or None
    return None


def tls_context() -> ssl.SSLContext:
    """Use the host CA bundle when Python's default store is unavailable."""
    configured_bundle = os.environ.get("SSL_CERT_FILE")
    for candidate in (configured_bundle, "/etc/ssl/cert.pem"):
        if candidate and Path(candidate).is_file():
            return ssl.create_default_context(cafile=candidate)
    return ssl.create_default_context()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Image-search phrase, maximum 100 characters")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()

    key = pixabay_api_key()
    if not key:
        print(json.dumps({"errors": ["PIXABAY_API_KEY is required"]}))
        raise SystemExit(1)
    if not args.query.strip() or len(args.query) > 100:
        parser.error("query must contain 1-100 characters")
    if not 3 <= args.limit <= 20:
        parser.error("limit must be between 3 and 20")

    params = urlencode({
        "key": key,
        "q": args.query,
        "image_type": "photo",
        "orientation": "horizontal",
        "safesearch": "true",
        # Fetch a wider set because Pixabay can tag photo results as AI generated.
        "per_page": min(200, max(20, args.limit * 5)),
    })
    try:
        with urlopen(
            f"https://pixabay.com/api/?{params}", timeout=20, context=tls_context()
        ) as response:
            payload = json.load(response)
    except HTTPError as exc:
        print(json.dumps({"errors": [f"Pixabay API returned HTTP {exc.code}"]}))
        raise SystemExit(1)
    except URLError as exc:
        print(json.dumps({"errors": [f"Pixabay API request failed: {exc.reason}"]}))
        raise SystemExit(1)

    candidates = []
    for hit in payload.get("hits", []):
        tags = hit.get("tags", "")
        if "ai generated" in tags.lower():
            continue
        candidates.append({
            "id": hit["id"],
            "source_url": hit["pageURL"],
            "download_url": hit.get("largeImageURL") or hit.get("webformatURL"),
            "creator": hit.get("user"),
            "creator_url": f"https://pixabay.com/users/{hit.get('user')}-{hit.get('user_id')}/",
            "width": hit.get("imageWidth"),
            "height": hit.get("imageHeight"),
            "tags": tags,
            "license_basis": "Pixabay Content License, verify current terms before selection",
        })
        if len(candidates) == args.limit:
            break
    print(json.dumps({"query": args.query, "candidates": candidates}, indent=2))


if __name__ == "__main__":
    main()
