---
name: repurpose-social
description: "Repurposes articles into social media posts for X and LinkedIn. Use when the user asks to 'repurpose' or 'extract social posts' from a specific article or their latest content."
---

# Repurpose Social

Extract 3-5 standalone ideas from a selected article and transform them into engaging social media content for X (Twitter) and LinkedIn.

All social drafts must finish with a channel-specific, validated campaign URL.

## Core Workflow

1.  **Identify Content:** 
    -   **New Article:** If the user specifies an article (e.g., "repurpose my latest post"), find the most recent `.md` file in `content/articles/` based on frontmatter `date`.
    -   **Archive Request:** If the user asks to post from "repurposed content" or "archives":
        -   Search `/docs/repurposed/` for the relevant file (e.g., the one matching the current date or a specific topic).
        -   Read the file to identify the `Source Article` and the available social drafts.
        -   Skip to Step 6 (Execution Phase).
    -   **Resolve Campaign Attribution:** Run `scripts/generate_campaign_links.py` with the selected source Markdown file. It calls `hs campaign link` and `hs campaign validate` using the repository's `.hs.toml` policy.
        - Defaults: `content/articles/` uses `thought-leadership`; `content/signals/` uses `weekly-signals`; `content/lab/` uses `tech-lab`.
        - Defaults: X uses source `x`; LinkedIn uses source `linkedin`; both use medium `social`.
        - If the user explicitly supplies a campaign, medium, or source override, pass it through. A `--source` override applies to both channels; use `--x-source` or `--linkedin-source` when the override applies to one channel only.
        - Do not invent a campaign for content outside those three paths. Ask the user which campaign to use.
        - Treat a failed `hs campaign link` or `hs campaign validate` command as a blocker. Do not include an unvalidated URL.

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
    -   End every option with the generated X URL.

4.  **Draft for LinkedIn:**
    -   See [references/voice-guide.md](references/voice-guide.md) for platform-specific styling.
    -   Style: Professional but human, capitalization, clear structure.
    -   Include a "Takeaway" or "So What?" at the end of each post.
    -   End every option with the generated LinkedIn URL.

5.  **Output & Save:**
    -   Save the source path, resolved campaign, medium, and both generated URLs with the final drafts in `/docs/repurposed/YYYY-MM-DD-repurposed.md`.
    -   Present the content to the user for review.

6.  **Execution Phase (Posting):**
    -   **Trigger:** Only proceed if the user gives an explicit Directive to "Post" (e.g., "Post option 2 to X").
    -   **Selection Strategy:**
    -   **User Pick:** If the user specifies an option (e.g., "Post X Option 2"), use that exact text + the resolved article URL.
    -   **Random Pick:** If the user says "Pick one randomly and post to X," select one of the drafted X options.
    -   **Campaign Link Refresh:** For archived drafts, recover the original content Markdown path from the saved metadata, rerun `scripts/generate_campaign_links.py`, and replace the selected draft's final URL with the newly validated URL for that channel. Never reuse an untracked URL or a URL generated for the other platform.
    -   **Action (X/Twitter):**
        1.  Navigate to `https://x.com/compose/post`.
        2.  Wait for the "Post text" field (uid in snapshot).
        3.  **Reliable Entry:** Use `evaluate_script` on the "Post text" field to:
            - Clear any existing content (`el.innerText = ''`).
            - Dispatch an `input` event to reset X's internal state.
            - Use `document.execCommand('insertText', false, text)` to insert the drafted post. This method is preferred over `fill` to avoid desynchronization with X's React-based editor.
            - Dispatch `input`, `change`, and `blur` events to ensure the "Post" button is enabled.
        4.  **Pre-Post Validation:** Before clicking the button, run a final `evaluate_script` to check `el.innerText` and confirm the content is correct and not duplicated.
        5.  Click the "Post" button.
        6.  **Verify:** Take a screenshot of the live post to confirm.

## Reference Material

-   [Voice & Style Guide](references/voice-guide.md): Detailed tone and formatting rules for each platform.

## Evaluation

Run `uv run python .agents/skills/repurpose-social/evals/runner.py`. The report is written to `evals/reports/latest_results.json`.
