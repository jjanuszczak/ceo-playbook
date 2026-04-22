# Article Creator

Automates the creation of new article bundles, including GitHub issue tracking, feature branch isolation, and front matter standardization.

## Core Workflow

1.  **Issue Creation:**
    -   Given an article slug, create a GitHub issue tagged as an `enhancement`.
    -   This ensures the new article is tracked in the project backlog.

2.  **Branch Isolation:**
    -   Create a new feature branch specifically for the new article (e.g., `feature/article-<slug>`).
    -   This keeps the `main` branch clean during the draft and review phase.

3.  **Bundle Generation:**
    -   Use the `hugo new --kind article-bundle articles/<slug>` command to generate a new leaf bundle.
    -   This ensures all required front matter (title, date, categories, tags, etc.) is included.

4.  **Front Matter Initialization:**
    -   Automatically set the `status` property in the front matter to `"user-review"`.
    -   Optionally append provided Markdown content to the `index.md` file.

5.  **User Notification:**
    -   Provide the user with the path to the newly created `index.md` and the name of the feature branch.

## Usage

Provide the article slug (e.g., `my-new-post`) and any initial Markdown content. The skill will handle the infrastructure setup.

## Standards

-   **Slug Formatting:** Slugs should be lowercase and hyphen-separated.
-   **Front Matter:** Always include the governance-checked categories and tags placeholders.
-   **Status:** The initial status for automated creation is always `"user-review"`.
