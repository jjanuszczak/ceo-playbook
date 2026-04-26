# Git & GitHub Workflow for CEO Playbook

**Date:** 2026-04-20
**Status:** Recommended Workflow

## I. The Hub & Spoke Git Workflow
This workflow ensures that the website (**The Hub**) remains the single source of truth while automating distribution to social platforms (**The Spokes**).

### 1. Content Drafting & Research
*   **Branching:** Always create a new branch for each new article, signal, or technical update.
    *   *Command:* `git checkout -b content/signals-week-17` or `git checkout -b article/new-strategy`
*   **Drafting:** Use `hugo new` to create the content. Utilize the `content-research-writer` and `managing-editor` skills to:
    *   Research and cite high-quality sources.
    *   Enforce **Category & Tag Governance** (ensuring all frontmatter aligns with `.policies/`).
    *   Iterate on the "hook" and summary for the newsletter.
*   **Local Preview:** Run `hugo server -D` to verify the rendering, shortcodes, and images in a local browser before pushing.

### 2. Quality Control via Pull Requests (PRs)
*   **Push to GitHub:** Push your branch and open a Pull Request (PR) against the `main` branch.
*   **Automated Validation:** The existing GitHub Action (`gh-pages.yml`) is currently set to deploy on `push` to `main`. 
*   **Review:** Use the PR description to summarize the intent (e.g., "Deep-dive into AI Strategy for C-Suite").

### 3. Deployment & "Signals" Trigger
*   **Merge to Main:** Once the content is ready, merge the PR.
*   **Automated Deployment:** GitHub Actions will automatically:
    1.  Build the site using Hugo Extended.
    2.  Minify assets for performance.
    3.  Deploy to the `gh-pages` branch (hosted at `januszczak.org`).
*   **RSS to Kit:** The merge triggers the RSS feed updates (e.g., `/signals/index.xml`). Kit will detect the new entry and prepare your weekly "Signals" email automatically.

### 4. Atomization & Social Distribution
*   **After Merging:** Once the content is live, use the `repurpose-social` skill to generate:
    *   An **X Thread** (The Pulse) with a low barrier to entry.
    *   A **LinkedIn Post** (The Authority) for professional depth.
    *   Both should link back to the "Hub" article for full details.

---

## II. Infrastructure Recommendations
To make this workflow even more robust, the following can be implemented:

1.  **PR Build Preview:** Add a GitHub Action that uses [GitHub Pages Preview](https://github.com/marketplace/actions/github-pages-deploy-action-preview) or similar to show you exactly how the site will look before you merge.
2.  **Linting & Governance Check:** Add a pre-commit hook or CI step that runs the Python scripts in `.scripts/` (like `update_frontmatter.py`) to ensure no article is missing mandatory metadata.
3.  **Branch Protection:** Enable branch protection on `main` to require at least one successful build before merging.

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