#!/usr/bin/env python3
"""Run deterministic checks for the internal-linker skill."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python runner.py <target-article.md>")
        return 1
    target = str(Path(sys.argv[1]).resolve())
    base_dir = Path(__file__).resolve().parent
    config = yaml.safe_load((base_dir / "config.yaml").read_text(encoding="utf-8"))
    results = {"timestamp": datetime.now().isoformat(), "target_article": target, "overall_status": "PASS", "checks": []}

    for step in config["pipeline"]["steps"]:
        print(f"Running check: {step['name']}...")
        process = subprocess.run([sys.executable, str(base_dir / step["script"]), target], capture_output=True, text=True)
        try:
            details = json.loads(process.stdout.strip())
        except json.JSONDecodeError:
            details = {"message": process.stdout.strip() or process.stderr.strip()}
        status = "PASS" if process.returncode == 0 else "FAIL"
        results["checks"].append({"id": step["id"], "name": step["name"], "status": status, "details": details})
        if status == "FAIL":
            results["overall_status"] = "FAIL"
            if step.get("halt_on_fail", False):
                print(f"Critical failure in {step['name']}. Halting pipeline.")
                break

    report = base_dir / "reports" / "latest_results.json"
    report.parent.mkdir(exist_ok=True)
    report.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Evaluation complete. Status: {results['overall_status']}")
    print(f"Report saved to: {report}")
    return 0 if results["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
