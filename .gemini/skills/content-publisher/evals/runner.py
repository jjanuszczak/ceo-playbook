import sys
import os
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
    
    # Self-healing loop: Attempt 1 & 2
    for attempt in range(1, 3):
        failed_checks = []
        all_passed = True

        for step in config['pipeline']['steps']:
            script_path = os.path.join(base_dir, step['script'])
            check_id = step['id']
            name = step['name']
            
            print(f"Attempt {attempt}: Running check: {name}...")
            
            result = subprocess.run(
                [sys.executable, script_path, file_path],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"  Check {name} failed: {result.stdout.strip() or result.stderr.strip()}")
                failed_checks.append(step)
                all_passed = False
            else:
                print(f"  Check {name} passed.")

        if all_passed:
            break
        
        if attempt < 2:
            print(f"Attempt {attempt} failed. Attempting autonomous self-correction...")
            # Trigger fixer script if it exists
            fixer_script = os.path.join(base_dir, "fixer.py")
            if os.path.exists(fixer_script):
                subprocess.run([sys.executable, fixer_script, file_path], capture_output=True)
            else:
                print("No fixer.py found. Escalating.")
                break
        else:
            print("Multiple attempts failed. Escalating to user.")
            results["overall_status"] = "FAIL"

    # Final result logging
    report_path = os.path.join(base_dir, "reports", "latest_results.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    
    return 0 if results["overall_status"] == "PASS" else 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py [path/to/index.md]")
        sys.exit(1)
        
    target_path = sys.argv[1]
    sys.exit(run_eval(target_path))
