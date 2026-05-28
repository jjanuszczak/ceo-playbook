import os
import sys
import yaml
import json
import subprocess
from datetime import datetime

def run_eval(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.yaml")
    
    if not os.path.exists(config_path):
        print(f"Error: Config file not found at {config_path}")
        return 1

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "file_path": file_path,
        "overall_status": "PASS",
        "checks": []
    }
    
    for step in config['pipeline']['steps']:
        script_path = os.path.join(base_dir, step['script'])
        check_id = step['id']
        name = step['name']
        
        print(f"Running check: {name}...")
        
        result = subprocess.run(
            [sys.executable, script_path, file_path],
            capture_output=True,
            text=True
        )
        
        status = "PASS" if result.returncode == 0 else "FAIL"
        
        check_result = {
            "id": check_id,
            "name": name,
            "status": status,
            "output": result.stdout.strip() or result.stderr.strip()
        }
        
        results["checks"].append(check_result)
        
        if status == "FAIL":
            results["overall_status"] = "FAIL"

    # Save report
    report_path = os.path.join(base_dir, "reports", "latest_results.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Evaluation complete. Status: {results['overall_status']}")
    print(f"Report saved to: {report_path}")
    
    return 0 if results["overall_status"] == "PASS" else 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py [path/to/index.md]")
        sys.exit(1)
        
    target_path = sys.argv[1]
    sys.exit(run_eval(target_path))
