---
name: related-posts-suggester
description: Identifies related posts based on tag similarity. Use when the user asks for related-post recommendations, without modifying the post.
---

# Related Posts Suggester

This skill identifies related content for a Hugo post based on tag similarity. It is advisory only and must not modify the target file.

## Workflow

1.  **Identify Target:** Determine the article that needs related post suggestions.
2.  **Calculate Similarity:** Run the `find_related_posts.py` script to get the most relevant articles.
    ```bash
    uv run python .agents/skills/related-posts-suggester/scripts/find_related_posts.py <path/to/article.md> --limit <count>
    ```
3.  **Prepare Suggestion:**
    - Read the file content.
    - Show the recommended posts and, optionally, the generated `related-posts` shortcode as copyable text in the response.
    - Never append or otherwise write a `related-posts` shortcode to the target file.

## Guidance

- **Weighting:** The script automatically weights rare tags higher than common tags to ensure more meaningful connections.
- **Default Count:** Suggest 2 related posts by default, unless the user specifies otherwise.
- **Title:** Use "Related Insights" as the default title parameter (e.g., `{{< related-posts title="Related Insights" paths="..." >}}`).
- **Manual Mode:** If requested (e.g., "suggest related posts but don't add them"), simply display the shortcode in the conversation.

## Bundled Resources

- `scripts/find_related_posts.py`: Python script for tag-based similarity analysis.
