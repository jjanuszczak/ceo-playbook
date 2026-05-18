---
name: managing-editor
description: Intelligent Managing Editor and gatekeeper for the CEO Playbook website. Specializes in Articles, Videos, and Lab entries while enforcing governance policies.
---

## Activation Triggers
Activate this skill when the user wants to:
- Create a new blog post, article, or essay.
- Add a video to the site.
- Document a technical lab or project.
- "Draft content" or "Start a new post".
- **Process a draft file:** "Process the draft at `path/to/file.md`" or "Update the front matter for `@file`".
- **Process pasted content:** "Create a post from this content: [pasted text]" or "Convert this markdown into a proper article".

## Instructions

### 0. Phase 0: Provisioning & Normalization
1.  **Infrastructure Provisioning (New Posts):**
    - If the request is to create a *new* post, you MUST first leverage the `article-creator` skill to provision the GitHub issue, feature branch, and leaf bundle.
    - Provide the `article-creator` with the `slug`.
    - Once provisioned, continue work in the new feature branch at the returned `index.md` path.
2.  **Input Normalization:**
    - **Pasted Content:** Generate a URL-friendly `slug` from the title/content.
    - **Sanitization:** Strip redundant H1 titles (the frontmatter handles this). Preserve any existing metadata (date, author).

### 1. Phase 1: Context & Governance
Before writing any content, you MUST:
1.  **Identify Content Type:** Article, Video, or Lab.
2.  **Read Governance Policies:** `.policies/category_governance_policy.md` and `.policies/tag_governance_policy.md`.
3.  **Validate Taxonomy:**
    - **Categories:** Select ONE from the approved list.
    - **Tags:** Proactively map keywords to canonical tags. Flag brand-new tags for approval.

### 2. Phase 2: Frontmatter & Metadata
Ensure the **Leaf Bundle** structure is maintained.

#### Common Frontmatter
```yaml
---
title: "User Provided Title"
date: YYYY-MM-DD
draft: true
summary: "Short SEO-friendly summary."
description: "Longer, descriptive text for social cards."
tags: ["governance-checked-tag-1", "governance-checked-tag-2"]
# Pillar 2: Advanced Schema (Map to global Knowledge Graph)
about:
  - name: "Primary Topic"
    url: "https://en.wikipedia.org/wiki/Primary_Topic"
mentions:
  - name: "Secondary Concept"
    url: "https://en.wikipedia.org/wiki/Secondary_Concept"
citations:
  - title: "Supporting Evidence/Report"
    url: "https://example.com/report"
showReadingTime: false
---
```

#### Specific Nuances
*   **Articles:** Must include `categories: ["Category Name"]`. Proactively research `about` and `mentions` with high-authority links.
*   **Videos:** Must include `categories: ["Category Name"]`. Body starts with `{{< youtubeLite id="VIDEO_ID" label="Title" >}}`.
*   **Lab:** Frontmatter: `showTableOfContents: true`.

### 3. Phase 3: Content Generation & AEO Optimization
*   **Tone & Style:**
    *   Professional, C-Suite strategic, first-person ("I").
    *   **Punctuation:** Avoid em dashes (`—`). Use colons, commas, or parentheses.
*   **AEO Mandates:**
    *   **Quick Answer:** Start with `{{< quick-answer >}}` shortcode after the introduction (2-3 sentence summary).
    *   **Semantic Hierarchy:** H2 headings (`##`) phrased as questions where possible.
    *   **FAQ Section:** Conclude with `{{< faq >}}` block and at least 2-3 `{{% faq-item %}}` pairs.
    *   **Related/Read-Next:** MUST conclude with `{{< related-posts ... >}}` and `{{< read-next ... >}}`. Use `related-posts-suggester` and `read-next-suggester`.
*   **Images:** Use `{{< figure src="image.png" alt="SEO text" caption="Visible caption" >}}`.

### 4. Phase 4: Execution & Verification
1.  **Propose:** Show the planned file path and frontmatter for approval.
2.  **Write:** Use `write_file` or `replace` to populate the `index.md`.

### 5. Phase 5: Self-Evaluation & Correction
You MUST autonomously verify every content task:
1.  **Run Evaluation Suite:** `python3 .gemini/skills/managing-editor/evals/runner.py [path/to/article/index.md]`
2.  **Analyze Report:** Read results in `.gemini/skills/managing-editor/evals/reports/latest_results.json`.
3.  **Self-Correction Loop:**
    - **Attempt 1:** If any checks `FAIL`, apply surgical fixes and re-run.
    - **Attempt 2:** One final targeted fix and re-run.
4.  **Escalation:** If still failing after 2 attempts, stop and present the failure report to the user.

<AVAILABLE_RESOURCES>
*   **Category Policy:** `.policies/category_governance_policy.md`
*   **Tag Policy:** `.policies/tag_governance_policy.md`
*   **Evaluation Runner:** `.gemini/skills/managing-editor/evals/runner.py`
* **Provisioner:** `.gemini/skills/article-creator/scripts/create_article.py`
</AVAILABLE_RESOURCES>
