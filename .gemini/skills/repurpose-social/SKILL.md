---
name: repurpose-social
description: "Repurposes articles into social media posts for X and LinkedIn. Use when the user asks to 'repurpose' or 'extract social posts' from a specific article or their latest content."
---

# Repurpose Social

Extract 3-5 standalone ideas from a selected article and transform them into engaging social media content for X (Twitter) and LinkedIn.

## Core Workflow

1.  **Identify Article:** 
    -   If the user specifies an article (e.g., "repurpose my latest post"), find the most recent `.md` file in `content/articles/` based on frontmatter `date`.
    -   If a specific path is provided, use that file.

2.  **Extract Ideas:** 
    -   Identify 3-5 key sections where the author:
        -   Expresses a strong or contrarian opinion.
        -   Shares a specific tactic or framework (e.g., "Density Beats Breadth").
        -   Tells a brief, relatable story or anecdote.
    -   Ensure each idea is standalone and doesn't require the full article context to be understood.

3.  **Draft for X (Twitter):**
    -   See [references/voice-guide.md](references/voice-guide.md) for platform-specific styling.
    -   Style: lowercase, short sentences, punchy hook in line 1.
    -   No hashtags unless specifically requested.

4.  **Draft for LinkedIn:**
    -   See [references/voice-guide.md](references/voice-guide.md) for platform-specific styling.
    -   Style: Professional but human, capitalization, clear structure.
    -   Include a "Takeaway" or "So What?" at the end of each post.

5.  **Output & Save:**
    -   Save the final drafts to `/docs/repurposed/YYYY-MM-DD-repurposed.md`.
    -   Present the content to the user for review.

## Reference Material

-   [Voice & Style Guide](references/voice-guide.md): Detailed tone and formatting rules for each platform.
