#!/usr/bin/env python3
"""Verify the ready-to-paste card promotes My Take's bold lead without duplication."""

import json

from common import load_script


def main() -> None:
    item = {
        "summary": "A concise source summary.",
        "why_it_matters": "Teams need a hard editorial filter.",
        "my_take": "**Curation protects trust.** Keep the bar high.",
        "signals_index_url": "https://januszczak.org/signals/?utm_campaign=signals-x-quotes&utm_medium=social&utm_source=x",
        "callout_intro": "Fyi",
        "callout_adjective": "thoughtful",
    }
    draft = load_script().make_draft(item)
    assert draft.startswith("**Curation protects trust.**")
    assert "Summary:" not in draft
    assert "Why it matters: Teams need a hard editorial filter." in draft
    assert "My take: Keep the bar high." in draft
    assert draft.count("**Curation protects trust.**") == 1
    assert "Fyi I curate, expand on, and share my take on thoughtful content" in draft
    print(json.dumps({"message": "My Take hook, summary label removal, and callout formatting verified"}))


if __name__ == "__main__":
    main()
