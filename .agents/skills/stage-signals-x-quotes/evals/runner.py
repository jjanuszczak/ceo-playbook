#!/usr/bin/env python3
"""Run configured checks for the Stage Signals X Quotes skill."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml


def run_eval() -> int:
    base_dir = Path(__file__).resolve().parent
    config = yaml.safe_load((base_dir / "config.yaml").read_text())
    results = {"timestamp": datetime.now().isoformat(), "overall_status": "PASS", "checks": []}
    for step in config["pipeline"]["steps"]:
        print(f"Running check: {step['name']}...")
        result = subprocess.run([sys.executable, str(base_dir / step["script"])], capture_output=True, text=True)
        status = "PASS" if result.returncode == 0 else "FAIL"
        try:
            details = json.loads(result.stdout.strip())
        except json.JSONDecodeError:
            details = {"message": result.stdout.strip() or result.stderr.strip()}
        results["checks"].append({"id": step["id"], "name": step["name"], "status": status, "details": details})
        if status == "FAIL":
            results["overall_status"] = "FAIL"
            if step.get("halt_on_fail", False):
                break
    report_path = base_dir / "reports/latest_results.json"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(results, indent=2) + "\n")
    print(f"Evaluation complete. Status: {results['overall_status']}")
    print(f"Report saved to: {report_path}")
    return 0 if results["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(run_eval())
