# Content Creator (Infrastructure Layer)

Automates the technical provisioning of all site content types (Articles, Research, Videos, Lab, Portfolio, and Signals), including GitHub issue tracking and feature branch isolation. This skill provides the "plumbing" and should be leveraged by the `managing-editor` for all content creation tasks.

## Core Workflow

1.  **Identify Content Type:**
    -   Determine the type of content requested (Article, Research, Video, Lab, Portfolio, or Signals).
    -   If unclear, ask the user for clarification.
2.  **Issue Creation:**
    -   Create a GitHub issue tagged as an `enhancement` for the specific content type.
3.  **Branch Isolation:**
    -   Create a new feature branch in the format `feature/<type>-<slug>`.
4.  **Bundle Provisioning:**
    -   Use `hugo new` with the appropriate archetype kind to generate the physical leaf bundle and `index.md`.

## Instructions

- **Role:** You are an infrastructure provisioner. Do not attempt to validate taxonomy, tone, or AEO standards. Leave all "intelligence" tasks to the `managing-editor`.
- **Slug Formatting:** Slugs should be lowercase and hyphen-separated.
- **Output:** Always provide the path to the newly created `index.md` and the name of the feature branch to the calling skill or user.

## Implementation

To execute this workflow, use the supporting Python script:
`python3 .gemini/skills/content-creator/scripts/create_content.py <content_type> <slug>`

**Available Types:** `article`, `research`, `video`, `lab`, `portfolio`, `signals`.

### 5. Phase 5: Self-Evaluation & Correction
You MUST autonomously verify every provisioning task:
1.  **Run Evaluation Suite:** `python3 .gemini/skills/content-creator/evals/runner.py <content_type> <slug>`
2.  **Analyze Report:** Read results in `.gemini/skills/content-creator/evals/reports/latest_results.json`.
3.  **Self-Correction Loop:**
    - **Attempt 1:** If any checks `FAIL` (e.g., branch not created, issue missing), analyze the error and attempt to fix the provisioning issue.
    - **Attempt 2:** One final targeted fix and re-run.
4.  **Escalation:** If still failing after 2 attempts, stop and present the failure report to the user.

<AVAILABLE_RESOURCES>
*   **Evaluation Runner:** `.gemini/skills/content-creator/evals/runner.py`
</AVAILABLE_RESOURCES>

## Integration Note
This skill is a "downstream" dependency for the `managing-editor`. When asked to create any content, the system should:
1. Call `content-creator` to set up the infrastructure.
2. Call `managing-editor` to populate and validate the content.
