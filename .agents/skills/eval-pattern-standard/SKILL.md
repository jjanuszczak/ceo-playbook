---
name: eval-pattern-standard
description: Standardize evaluation suites for new or materially changed repository skills. Use when creating a skill or adding/reworking its evals; require confirmation before deviating from the configured-check pattern.
---

# Eval Pattern Standard

Use this pattern for every new skill with testable behavior and for material changes to an existing skill's eval implementation:

```text
<skill>/
├── SKILL.md
└── evals/
    ├── config.yaml
    ├── runner.py
    ├── checks/
    │   └── <focused>_check.py
    └── reports/
        └── latest_results.json
```

`config.yaml` defines a named pipeline. Each focused check owns one observable invariant, exits nonzero on failure, and prints JSON details. `runner.py` reads the configuration, runs every check, writes a structured `latest_results.json`, and returns a nonzero status when any required check fails.

Keep checks isolated and deterministic. Use temporary fixture projects for commands that would otherwise write production state. Test external integrations through the same public interface used by the skill when that interface is part of the behavior, such as invoking a configured command-line tool. Do not rely only on source-text matching.

Document the eval command and report location in the skill's `SKILL.md`. Run the configured suite after implementing it, inspect the report, and correct failures before completing the task.

## Required confirmation for exceptions

If this evaluation pattern cannot be used, or if a new skill would have no automated evaluation, stop before implementing the exception. Tell the user why the pattern does not fit, identify the risk or lost coverage, propose one or more practical alternatives, and ask for confirmation on the direction. Do not silently substitute a one-off runner, embed all checks in one file, or omit evaluation.
