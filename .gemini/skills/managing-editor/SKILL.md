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

### 0. Phase 0: Ingestion & Normalization
Before applying governance, normalize the input:
1.  **Input Source Identification:**
    - **Case A (File Path):** Read the file contents. If it is a "flat" markdown file (e.g., `articles/my-post.md`), plan to migrate it to a **Leaf Bundle** (`articles/my-post/index.md`).
    - **Case B (Pasted Content):** Treat as a new draft. Generate a URL-friendly `slug` from the title or content.
2.  **Content Sanitization:**
    - Strip redundant H1 titles from the body (the frontmatter `title` field handles this).
    - Identify and preserve any existing metadata (date, author, etc.) if present.

### 1. Phase 1: Context & Governance
Before writing any content, you MUST:
1.  **Identify Content Type:** Determine if the request is for an **Article**, **Video**, or **Lab** entry.
2.  **Read Governance Policies:**
    - Read `.policies/category_governance_policy.md`.
    - Read `.policies/tag_governance_policy.md`.
3.  **Validate Taxonomy:**
    - **Categories:** For Articles and Videos, select ONE category from the strictly enforced list. If the topic doesn't fit, ask for clarification.
    - **Tags:** Compare draft keywords against the canonical list. **Proactive Mapping:** Map common terms to canonical tags (e.g., "AI" → "artificial-intelligence"). Flag any brand-new tags for user approval per the "New Tag Test".

### 2. Phase 2: Bundle Structure & Frontmatter
Always enforce a **Leaf Bundle** structure (`content/<section>/<slug>/index.md`).

#### Common Frontmatter
```yaml
---
title: "User Provided Title"
date: YYYY-MM-DD
draft: true
summary: "Short SEO-friendly summary."
description: "Longer, descriptive text for social cards."
tags: ["governance-checked-tag-1", "governance-checked-tag-2"]
showReadingTime: false
---
```

#### Specific Nuances
*   **Articles:**
    *   Must include `categories: ["Category Name"]`.
    *   If reposting, add `externalUrl: "..."`.
*   **Videos:**
    *   Must include `categories: ["Category Name"]`.
    *   **Body:** Start with: `{{< youtubeLite id="VIDEO_ID" label="Title" >}}`.
*   **Lab:**
    *   Frontmatter: `showTableOfContents: true`.

### 3. Phase 3: Content Generation
*   **Tone:** Professional, C-Suite strategic, first-person ("I").
*   **Images:** Use the shortcode: `{{< figure src="image.png" alt="SEO text" caption="Visible caption" >}}`.
*   **Headings:** Start with H2 (`##`).

### 4. Execution
1.  **Propose:** Show the user the planned file path (`content/.../index.md`) and the generated frontmatter for approval.
2.  **Create/Move:** Use `write_file` for the `index.md`. If migrating a flat file, ensure the old file is deleted after the bundle is created.
3.  **Verify:** Remind the user to run `hugo server -D` to view the draft.

<AVAILABLE_RESOURCES>
*   **Category Policy:** `.policies/category_governance_policy.md`
*   **Tag Policy:** `.policies/tag_governance_policy.md`
</AVAILABLE_RESOURCES>
