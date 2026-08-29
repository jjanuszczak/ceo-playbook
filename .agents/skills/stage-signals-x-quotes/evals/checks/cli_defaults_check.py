#!/usr/bin/env python3
"""Verify the public stage command exposes documented attribution defaults."""

import json

from common import load_script


def main() -> None:
    args = load_script().build_parser().parse_args(["stage"])
    assert (args.campaign, args.medium, args.source) == ("signals-x-quotes", "social", "x")
    print(json.dumps({"message": "Stage defaults are configured", "defaults": {
        "campaign": args.campaign, "medium": args.medium, "source": args.source,
    }}))


if __name__ == "__main__":
    main()
