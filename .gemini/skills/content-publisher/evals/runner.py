import sys
import os
import json
import subprocess

def run_checks(file_path):
    results = {
        "summary": {"pass": 0, "fail": 0},
        "details": []
    }

    # Example check: Publication State
    check_cmd = ["python3", ".gemini/skills/content-publisher/evals/checks/publication_check.py", file_path]
    process = subprocess.run(check_cmd, capture_output=True, text=True)
    
    status = "PASS" if process.returncode == 0 else "FAIL"
    results["details"].append({
        "check": "Publication State Check",
        "status": status,
        "output": process.stdout.strip() or process.stderr.strip()
    })
    
    if status == "PASS":
        results["summary"]["pass"] += 1
    else:
        results["summary"]["fail"] += 1

    # Save report
    report_path = ".gemini/skills/content-publisher/evals/reports/latest_results.json"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Evaluation complete. Status: {'PASS' if results['summary']['fail'] == 0 else 'FAIL'}")
    return results["summary"]["fail"] == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 runner.py [path/to/index.md]")
        sys.exit(1)
    
    target = sys.argv[1]
    success = run_checks(target)
    sys.exit(0 if success else 1)
