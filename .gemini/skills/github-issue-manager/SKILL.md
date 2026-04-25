---
name: github-issue-manager
description: Create GitHub issues and development branches. Use when the user wants to start work on a bug, feature (enhancement), or documentation task and needs a structured way to track it.
---

# GitHub Issue Manager

This skill automates the creation of GitHub issues and the setup of local development branches.

## Workflow

1.  **Create Issue & Branch:** Run the `manage_issue.py` script to create a GitHub issue with appropriate labels and switch to a new branch.
    ```bash
    python3 .gemini/skills/github-issue-manager/scripts/manage_issue.py "Title" "Description" --type <bug|enhancement|documentation>
    ```

## Instructions

- **Issue Types:**
    - `bug`: For reporting errors or unexpected behavior.
    - `enhancement`: For new features or improvements.
    - `documentation`: For updates to READMEs, guides, or site content.
- **Branch Naming:** The script generates a concise branch name in the format `type/abbreviated-title`.
    - `enhancement` maps to `feature/`
    - `bug` maps to `bug/`
    - `documentation` maps to `documentation/`
- **Requirements:** Requires the `gh` (GitHub CLI) to be installed and authenticated.

## Scripts

- `scripts/manage_issue.py`: The core automation script.
