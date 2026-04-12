---
name: related-posts-suggester
description: Automatically identifies and embeds related posts based on tag similarity. Use when the user asks for "related posts" or "related content" for a specific article.
---

# Related Posts Suggester

This skill helps you automatically identify and embed related content into a Hugo post based on tag similarity.

## Workflow

1.  **Identify Target:** Determine the article that needs related post suggestions.
2.  **Calculate Similarity:** Run the `find_related_posts.py` script to get the most relevant articles.
    ```bash
    python3 .gemini/skills/related-posts-suggester/scripts/find_related_posts.py <path/to/article.md> --limit <count>
    ```
3.  **Automatic Embedding (Default):**
    Unless the user explicitly asks to "show" or "suggest" without inserting, automatically append the generated `related-posts` shortcode to the target article.
    
    **Placement Strategy:**
    - Read the file content.
    - If a `{{< read-next ... >}}` shortcode exists, insert the `related-posts` shortcode *immediately before* it.
    - Otherwise, append it to the very end of the file.

## Guidance

- **Weighting:** The script automatically weights rare tags higher than common tags to ensure more meaningful connections.
- **Default Count:** Suggest 2 related posts by default, unless the user specifies otherwise.
- **Title:** Use "Related Insights" as the default title parameter (e.g., `{{< related-posts title="Related Insights" paths="..." >}}`).
- **Manual Mode:** If requested (e.g., "suggest related posts but don't add them"), simply display the shortcode in the conversation.

## Bundled Resources

- `scripts/find_related_posts.py`: Python script for tag-based similarity analysis.
