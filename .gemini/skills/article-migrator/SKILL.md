# Article Migrator

Automates the migration of external article content (from LinkedIn, Medium, Substack, etc.) into local Hugo bundles, including image harvesting, social noise removal, and internal link resolution.

## Core Workflow

1.  **Discovery & Selection:**
    -   Scan `content/articles/` for `index.md` files with an active `externalUrl` property.
    -   Present a numbered list of articles to the user.
    -   Allow the user to select specific articles or a batch (e.g., "process all from 2024").

2.  **Extraction Strategy:**
    -   Determine the source platform (LinkedIn, Medium, Substack, etc.).
    -   Use platform-specific CSS selectors to identify the main article body and ignore:
        -   "Share this article" blocks.
        -   "Recommended reading" sidebars.
        -   Author bio footers.
        -   Social interactions (Likes, Comments).
    -   Fall back to generic extraction for unknown sites.

3.  **Media Harvesting:**
    -   **Images:** 
        -   Download original images to the article's local directory (the "bundle").
        -   Name them descriptively (e.g., `featured.jpg`, `inline-image-1.jpg`).
        -   Replace external `<img>` tags with Hugo `{{< figure >}}` shortcodes using original `alt` and `caption`.
    -   **Videos:**
        -   Convert YouTube or Vimeo links into Hugo `{{< youtube id >}}` or `{{< vimeo id >}}` shortcodes.

4.  **Semantic Cleanup & Link Resolution:**
    -   **Internal Links:** Detect if the external article links to another URL on `johnjanuszczak.com`. Replace these with Hugo `{{< relref "path" >}}` shortcodes.
    -   **Formatting:** Convert HTML elements (headings, bold, lists) into clean Markdown.
    -   **Attribution:** Add the mandatory attribution line below the front matter: `*This article originally appeared on [Platform](ExternalURL) on YYYY-MM-DD*.`.

5.  **Status Reporting:**
    -   Generate a summary report at the end of the session.
    -   Include:
        -   Articles successfully migrated.
        -   Media assets downloaded.
        -   Internal links resolved.
        -   Errors or access issues encountered.

## Constraints & Standards

-   **Front Matter Integrity:** Comment out the `externalUrl` property but DO NOT change any other front matter values (unless specifically requested).
-   **Bundle Structure:** All assets must be stored within the same directory as the `index.md` file.
-   **Security:** Respect `.gitignore` and do not process files marked for exclusion.
