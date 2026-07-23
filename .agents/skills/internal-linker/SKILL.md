---
name: internal-linker
description: Analyze a Hugo Markdown article and prepare a ready-to-apply internal-linking optimization report with high-value outgoing and incoming link recommendations, exact Hugo ref or relref edits, a Further Reading section, and limited content polish. Use when improving a Hugo article's SEO, reader paths, topical authority, or internal links without changing the author's voice.
---

# Internal Linking & Content Optimization (Hugo)

Use this skill to make a considered recommendation or an approved edit. Do not add links automatically unless the user asks to apply the report.

## Workflow

1. Identify the target article from the supplied URL or Markdown path. Read its full frontmatter and body.
2. Run the repository discovery helper. Use 4 candidates for each direction unless the user requests another limit.

   ```bash
   uv run python .agents/skills/internal-linker/scripts/find_link_candidates.py \
     content/articles/example/index.md --limit 4
   ```

   Pass `--content-dir content/articles` when the target lives outside the default corpus. The helper ranks published articles with tag, category, keyword, and recency signals. Treat its results as a shortlist, not a decision.
3. Read every shortlisted source file before recommending it. Reject a candidate if the connection is generic, duplicated by an existing internal link, or cannot be justified in the target's own language.
4. Select 2 to 4 outgoing and 2 to 4 incoming recommendations. Favor complementary depth, a prerequisite, a useful extension, or direct supporting evidence. Prefer material published in the past 12 to 18 months when relevance is otherwise comparable.
5. Write exact, minimal suggestions. For outgoing links, quote the nearby text and add a natural transition after the relevant paragraph, bullet, or FAQ answer. For incoming links, identify the precise paragraph in the source article and supply its proposed sentence.
6. Add or improve a `## Further Reading` section only when it improves the reader path. Place it before a trailing teaser or related-content shortcode. Use two to four distinct links.
7. Suggest frontmatter only when the site's existing configuration supports it. Do not invent a `related` parameter or change tags merely to force relevance.

## Hugo Link Rules

- Use page-relative, extensionless references such as `[From Discovery to Knowledge]({{< ref "articles/discovery-to-knowledge" >}})`.
- Use `relref` only when the target must resolve relative to the current page.
- Preserve existing shortcodes and never double-wrap a Hugo link.
- Do not link to drafts, external URL stubs, the target article itself, or the same destination twice.
- Keep the original author voice. Do not list-dump links or add a link without a reason the reader can see.

## Required Report

Return this structure in Markdown. If the user asks to apply the recommendations, show the report first, then make only the approved edits.

# Optimization Report for: <title>

## Article Analysis
- Main themes: <3–6 specific themes>
- Existing internal links: <count and destinations, or none>

## Recommended Outgoing Links (2–4)

1. **Target Article**: <title>
   **Location**: <heading and text anchor>
   **Why it fits**: <specific reader benefit>
   **Suggested insertion**:
   > <exact replacement or added sentence using a Hugo ref>

## Recommended Incoming Links (2–4)

1. **Source Article**: <title>
   **Location**: <heading and text anchor>
   **Suggested insertion**:
   > <exact sentence linking to the target with a Hugo ref>

## Full Markdown Diff / Patch
```diff
<minimal target-article patch only>
```

## Further Reading
```markdown
## Further Reading
- [<title>]({{< ref "articles/path" >}}): <specific reason>
```

## Suggested Frontmatter Additions
<Only show this section if an evidence-based change is useful.>

## Guardrails

- Cap each direction at four links. Fewer is better when the article does not support more.
- Do not recommend a link from a title, tag, or keyword alone. Read the relevant passages.
- Keep link text descriptive. Avoid "here," raw URLs, and SEO-stuffed anchors.
- Propose lightweight polish only: a transition, a concise Quick Answer, or a short FAQ addition that makes an existing point clearer.
- Check that every supplied shortcode path matches a real published content path before reporting it.

## Resource

- `scripts/find_link_candidates.py` produces a transparent JSON shortlist from local Hugo Markdown files. It does not edit content or decide placement.
