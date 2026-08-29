#!/usr/bin/env python3
"""Verify hs-generated campaign URLs carry valid default and override UTM values."""

import json
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from common import REPO_ROOT, load_script


def utm(url: str) -> dict[str, list[str]]:
    return parse_qs(urlparse(url).query)


def main() -> None:
    module = load_script()
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / ".hs.toml").write_text((REPO_ROOT / ".hs.toml").read_text())
        (root / "hugo.toml").write_text('baseURL = "https://januszczak.org/"\n')
        signals_index = root / "content/signals/_index.md"
        signals_index.parent.mkdir(parents=True)
        signals_index.write_text("---\ntitle: Signals\n---\n")
        module.ROOT, module.SIGNALS_INDEX_PATH = root, signals_index
        default = module.tracking_url("signals-x-quotes", "social", "x")
        override = module.tracking_url("weekly-signals", "paid_social", "linkedin")
    assert utm(default) == {"utm_campaign": ["signals-x-quotes"], "utm_medium": ["social"], "utm_source": ["x"]}
    assert utm(override) == {"utm_campaign": ["weekly-signals"], "utm_medium": ["paid_social"], "utm_source": ["linkedin"]}
    print(json.dumps({"message": "hs generated and validated default and override campaign links"}))


if __name__ == "__main__":
    main()
