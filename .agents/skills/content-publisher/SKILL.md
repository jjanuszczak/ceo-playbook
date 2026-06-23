# Content Publisher Skill

This skill automates the publication lifecycle of content (Articles, Videos, Lab entries) by managing frontmatter state and ensuring a tracked audit trail via GitHub.

## Workflow: Publishing Content

1.  **Track & Branch:**
    -   Create an enhancement issue and branch using `github-issue-manager`.
    -   Title: `Publish: [Article Title]`
    -   Command: `uv run python .agents/skills/github-issue-manager/scripts/manage_issue.py "Publish: [Article Title]" "Publishing [Article Title]" --type enhancement`

2.  **Transform Content:**
    -   On the new branch, run the publication script to update the frontmatter and timestamp.
    -   Command: `uv run python .agents/skills/content-publisher/scripts/manage_publication.py --publish "[Fuzzy Title or Slug]"`

3.  **Submit for Review:**
    -   Commit and push changes using `git-workflow-lifecycle`.
    -   Command: `uv run python .agents/skills/git-workflow-lifecycle/scripts/submit_work.py --message "chore: publish [slug]"`
    -   The linked issue will automatically close when the PR is merged.

## Workflow: Unpublishing Content (Review Mode)

1.  **Track & Branch:**
    -   Create an issue/branch: `Unpublish: [Article Title]`
2.  **Transform Content:**
    -   Command: `uv run python .agents/skills/content-publisher/scripts/manage_publication.py --unpublish "[Fuzzy Title or Slug]"`
    -   Updates `status` to `"review"` and `draft` to `true`. Timestamp is preserved.
3.  **Submit:**
    -   Submit the PR as usual.

## Instructions

- **Discovery:** The script supports fuzzy matching on both the folder name (slug) and the `title` field in the frontmatter.
- **Validation:** Always run the evaluation suite after a transformation:
    `uv run python .agents/skills/content-publisher/evals/runner.py [path/to/index.md]`
- **Self-Healing Loop:** 
    1. If the runner returns `FAIL`, examine `latest_results.json`.
    2. Based on the failure output, autonomously apply a surgical fix to the frontmatter (e.g., correct `draft` vs `status` mismatch).
    3. Re-run the runner to verify the fix.
    4. If the runner fails after 2 attempts, escalate to the user with the failure report.
- **Draft Protection:** The script will warn if the post is already in the requested state.


## Scripts

-   `scripts/manage_publication.py`: The core transformation engine.

<AVAILABLE_RESOURCES>
-   **Evaluation Runner:** `.agents/skills/content-publisher/evals/runner.py`
</AVAILABLE_RESOURCES>
