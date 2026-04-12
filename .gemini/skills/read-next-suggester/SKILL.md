---
name: read-next-suggester
description: Automatically suggests and embeds the "Read Next" shortcode at the end of an article. Use when the user wants to add a "Read Next" section to a post, linking to the latest published content in the same section.
---

# Read Next Suggester

This skill helps you automatically identify and embed a "Read Next" section into a Hugo post.

## Workflow

1.  **Identify Target:** Determine the article that needs a "Read Next" section.
2.  **Find Latest Post:** Run the `find_latest_post.py` script to get the most recent published post in the same content section (e.g., `articles/`, `videos/`).
    ```bash
    python3 .gemini/skills/read-next-suggester/scripts/find_latest_post.py <path/to/article.md>
    ```
    - The script identifies the content section of the target file.
    - It finds the latest non-draft post in that section.
    - If the target file itself is the latest, it returns the previous latest post.
3.  **Embed Shortcode:**
    - Read the target file content.
    - If a `{{< read-next ... >}}` shortcode already exists, ask the user if they want to replace it.
    - Append the `read-next` shortcode to the end of the file.

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
