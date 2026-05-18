# Article Creator (Infrastructure Layer)

Automates the technical provisioning of new article bundles, including GitHub issue tracking and feature branch isolation. This skill provides the "plumbing" for new content and should be leveraged by the `managing-editor` for content creation tasks.

## Core Workflow

1.  **Issue Creation:**
    -   Given an article slug, create a GitHub issue tagged as an `enhancement`.
2.  **Branch Isolation:**
    -   Create a new feature branch specifically for the new article (e.g., `feature/article-<slug>`).
3.  **Bundle Provisioning:**
    -   Use the `hugo new --kind article-bundle articles/<slug>` command to generate the physical leaf bundle directory and `index.md` file.

## Instructions

- **Role:** You are an infrastructure provisioner. Do not attempt to validate taxonomy, tone, or AEO standards. Leave all "intelligence" tasks to the `managing-editor`.
- **Slug Formatting:** Slugs should be lowercase and hyphen-separated.
- **Output:** Always provide the path to the newly created `index.md` and the name of the feature branch to the calling skill or user.

## Implementation

To execute this workflow, use the supporting Python script:
`python3 .gemini/skills/article-creator/create_article.py <slug>`

## Integration Note
This skill is a "downstream" dependency for the `managing-editor`. When asked to create an article, the system should:
1. Call `article-creator` to set up the infrastructure.
2. Call `managing-editor` to populate and validate the content.
