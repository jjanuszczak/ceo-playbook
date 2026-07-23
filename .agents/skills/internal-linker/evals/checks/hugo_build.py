from __future__ import annotations

import subprocess

from common import ROOT, result


def main() -> int:
    process = subprocess.run(["hugo", "--minify"], cwd=ROOT, capture_output=True, text=True)
    errors = [] if process.returncode == 0 else ["Hugo build failed"]
    details = {"hugo_output": (process.stderr or process.stdout).strip()} if errors else {"message": "Hugo build successful"}
    return result(errors, **details)


if __name__ == "__main__":
    raise SystemExit(main())
