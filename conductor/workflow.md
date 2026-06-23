# Git & GitHub Workflow for CEO Playbook

**Date:** 2026-04-20
**Status:** Recommended Workflow

## I. The Hub & Spoke Git Workflow
This workflow ensures that the website (**The Hub**) remains the single source of truth while automating distribution to social platforms (**The Spokes**).

### 1. Content Drafting & Research
*   **Branching:** Use the `github-issue-manager` skill to provision a new branch and link it to a GitHub issue.
    *   *Command:* `uv run python .agents/skills/github-issue-manager/scripts/manage_issue.py "Title" "Description" --type enhancement`
*   **Drafting:** Utilize the `content-research-writer` and `managing-editor` skills to:
    *   Research and cite high-quality sources.
    *   Enforce **Category & Tag Governance** (automatically validated via `managing-editor` evals).
    *   Implement **AEO Optimization** (Quick Answer, FAQ blocks).
*   **Local Preview:** Run `hugo server -D` to verify rendering before submission.

### 2. Quality Control & Submission
*   **Submit Work:** Use the `git-workflow-lifecycle` skill to stage changes, commit, push, and create a Pull Request.
    *   *Command:* `uv run python .agents/skills/git-workflow-lifecycle/scripts/submit_work.py --message "feat: description"`
*   **Automated Validation:** PRs are automatically checked for structural integrity and governance alignment via the `managing-editor` evaluation suite.

### 3. Deployment & Cleanup
*   **Merge to Main:** Merge the PR once all checks pass.
*   **Cleanup:** Use the `git-workflow-lifecycle` skill to sync `main` and delete the feature branch.
    *   *Command:* `uv run python .agents/skills/git-workflow-lifecycle/scripts/cleanup_branch.py`

---

## II. Infrastructure & Automation
To maintain high standards, we rely on the following:

1.  **Skill-Based Governance:** The `managing-editor` skill enforces taxonomy rules found in `.policies/`, replacing legacy manual scripts.
2.  **Evaluation Suites:** Every automated task (Issue creation, Content drafting, PR submission) has a corresponding `evals/runner.py` that confirms success and compliance.
3.  **Automated Deployment:** GitHub Actions automatically builds and deploys to `januszczak.org` upon every merge to `main`.

---

## III. Weekly Cadence Summary
| Day | Action | Git/GitHub Stage |
| :--- | :--- | :--- |
| **Mon** | Write Deep-Dive/Lab | `git checkout -b`, `hugo server -D` |
| **Tue/Wed** | Refine & Review | `git push`, Open PR |
| **Thu** | Merge & Deploy | `git merge main`, GH Action triggers |
| **Fri** | Social & Newsletter | `repurpose-social`, Kit RSS Automation |

## IV. Content Status

| Status Code | Owner | Meaning |
| :--- | :--- | :--- |
| `agent_queued` | System | The idea exists, but the agent hasn't started research yet. |
| `agent_researching` | Agent | Agent is actively using search/research skills. |
| `agent_drafting` | Agent | Content is being written to the Hugo Leaf Bundle. |
| `human_review` | Human | The Pause. Agent is finished; waiting for your edits. |
| `human_revised` | Human | You've finished editing and want the agent to take it back. |
| `agent_optimizing` | Agent | Agent is performing SEO, linking, or image alt-text skills. |
| `agent_finalizing` | Agent | Agent is running hugo build checks and Git staging. |
| `published` | None | The post is live and the branch is merged.
