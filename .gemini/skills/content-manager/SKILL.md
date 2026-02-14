---
name: content-manager
description: Intelligent content manager and gatekeeper for the CEO Playbook website. Specializes in Articles, Videos, and Lab entries while enforcing governance policies.
---

## Activation Triggers
Activate this skill when the user wants to:
- Create a new blog post, article, or essay.
- Add a video to the site.
- Document a technical lab or project.
- "Draft content" or "Start a new post".

## Instructions

### 1. Phase 1: Context & Governance
Before writing any content, you MUST:
1.  **Identify Content Type:** Determine if the request is for an **Article**, **Video**, or **Lab** entry.
2.  **Read Governance Policies:**
    - Read `.policies/category_governance_policy.md`.
    - Read `.policies/tag_governance_policy.md`.
3.  **Validate Taxonomy:**
    - **Categories:** For Articles and Videos, select ONE category from the strictly enforced list (Strategy, Leadership, Fintech, Energy Transition, Technology, Venture Building, Essays). If the user's topic doesn't fit, ask for clarification. *Note: Lab entries generally do not use strict categories unless they fit 'Technology'.*
    - **Tags:** Check user-suggested keywords against existing tags. If a tag is new, flag it to the user and ask if they want to create a new governance entry or map to an existing tag.

### 2. Phase 2: Bundle Structure & Frontmatter
Always create a **Leaf Bundle** (`content/<section>/<slug>/index.md`).

#### Common Frontmatter
```yaml
---
title: "User Provided Title"
date: YYYY-MM-DD
draft: true
summary: "Short SEO-friendly summary."
description: "Longer, descriptive text for social cards."
tags: ["governance-checked-tag-1", "governance-checked-tag-2"]
showReadingTime: false # Default to false unless requested
---
```

#### Specific Nuances
*   **Articles:**
    *   Must include `categories: ["Category Name"]`.
    *   If reposting, add `externalUrl: "..."`.
*   **Videos:**
    *   Must include `categories: ["Category Name"]`.
    *   **Body:** Start immediately with the shortcode: `{{< youtubeLite id="VIDEO_ID" label="Title" >}}`.
    *   **Structure:** Follow with "Key Takeaways" (bullets) and "Transcript/Summary".
*   **Lab:**
    *   Frontmatter: `showTableOfContents: true`.
    *   Tone: Technical, "Practitioner's Walkthrough".

### 3. Phase 3: Content Generation
*   **Tone:** Professional, C-Suite strategic, first-person ("I").
*   **Images:**
    *   Do not use standard Markdown images `![alt](url)`.
    *   Use the shortcode: `{{< figure src="image.png" alt="SEO text" caption="Visible caption" >}}`.
    *   Remind the user to place image files in the bundle directory.
*   **Headings:** Start with H2 (`##`).

### 4. Execution
1.  **Propose:** Show the user the planned file path (`content/.../index.md`) and the generated frontmatter for approval.
2.  **Create:** Use `write_file` to create the `index.md`.
3.  **Verify:** Remind the user about the draft status (`hugo server -D` to view).