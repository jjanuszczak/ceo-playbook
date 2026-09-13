---
name: read-next-suggester
description: Suggests a potential next post from the same content section. Use when the user wants a recommendation, without modifying the post.
---

# Read Next Suggester

This skill identifies a potential "Read Next" post for a Hugo post. It is advisory only and must not modify the target file.

## Workflow

1.  **Identify Target:** Determine the article that needs a "Read Next" section.
2.  **Find Latest Post:** Run the `find_latest_post.py` script to get the most recent published post in the same content section (e.g., `articles/`, `videos/`).
    ```bash
    uv run python .agents/skills/read-next-suggester/scripts/find_latest_post.py <path/to/article.md>
    ```
    - The script identifies the content section of the target file.
    - It finds the latest non-draft post in that section.
    - If the target file itself is the latest, it returns the previous latest post.
3.  **Prepare Suggestion:**
    - Read the target file content.
    - If a `{{< read-next ... >}}` shortcode already exists, report that it is present.
    - Show the recommended post and, optionally, the shortcode as copyable text in the response.
    - Never append or otherwise write a `read-next` shortcode to the target file.

## Guidance

- **Sectional Relevance:** Always link to a post within the same content section (e.g., an article should link to another article).
- **Draft Status:** Only suggest published posts (not drafts).
- **Default Parameters:**
    - `title`: "Read Next"
    - `buttonText`: "View More Insights"
- **Shortcode Format:**
    ```markdown
    {{< read-next title="Read Next" link="[link_from_script]" buttonText="View More Insights" >}}
    ```

## Bundled Resources

- `scripts/find_latest_post.py`: Python script to identify the most current published post in a section.
