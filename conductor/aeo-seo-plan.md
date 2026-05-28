# AEO/SEO Optimization Plan: "The 10k Monthly Hits Blueprint"

## Objective
To transform the CEO Playbook website into a high-authority "Answer Engine" and SEO powerhouse, targeting **10,000+ monthly hits** by replicating the success patterns of high-growth technical sites (e.g., Karnot.com).

## Key Findings from Reference (Karnot.com)
*   **FAQ Dominance:** High density of FAQ sections with direct, punchy answers.
*   **Structured Authority:** Aggressive use of Schema.org (JSON-LD) to define products, services, and FAQs.
*   **Semantic Depth:** Targeting technical and high-intent keywords (e.g., "Natural Refrigerant Heat Pumps") rather than generic terms.
*   **Snippet-Ready Content:** Information is presented in modular blocks that search engines can easily "scrape" for featured snippets.

---

## Pillar 1: AEO Content Architecture (Answer Engine Optimization)
*The shift from "writing for readers" to "answering for engines."*

### 1.1 "Quick Answer" Shortcode
*   **Goal:** Secure "Position Zero" (Featured Snippets) and direct answers in ChatGPT/Perplexity/Gemini.
*   **Change:** Implement a `{{< quick-answer >}}` shortcode to be placed at the top of every article. It provides a 2-3 sentence summary of the core answer to the post's title.

### 1.2 Mandatory FAQ Sections
*   **Goal:** Feed Answer Engines the exact Q&A pairs they seek.
*   **Change:** Every major article must end with a "Frequently Asked Questions" section using a dedicated shortcode that also injects `FAQPage` schema.

### 1.3 Semantic Hierarchy (H-Tag Discipline)
*   **Goal:** Ensure LLMs understand the "Knowledge Graph" of your content.
*   **Change:** Enforce strict H1 -> H2 -> H3 structure. H2s should be phrased as questions where possible (e.g., "How does Venture Building differ from CVC?").

---

## Pillar 2: Advanced Structured Data (Schema.org)
*Telling the crawlers exactly what your data means.*

### 2.1 Article & NewsArticle Schema
*   **Upgrade:** Enhance default theme schema with `about`, `mentions`, and `citation` fields.
*   **Benefit:** Links your content to existing entities (e.g., "Fintech," "Southeast Asia," "BSP") in the global knowledge graph.

### 2.2 ProfessionalService & Person Schema
*   **Upgrade:** Expand the current `schema-home.html` to include specific `Offer` items for each advisory area (Venture Building, Market Entry, etc.) and link them to individual service pages.

### 2.3 Breadcrumb & Sitelinks
*   **Upgrade:** Ensure `BreadcrumbList` schema is active on all nested pages to improve "Sitelink" generation in Google Search results.

---

## Pillar 3: Semantic Keyword & Authority Strategy
*Moving beyond keywords to "Topic Clusters."*

### 3.1 Topic Hubs
*   **Strategy:** Create "Pillar Pages" for core categories (Strategy, Fintech, Leadership) that link to all related articles. This creates a "Hub and Spoke" model that builds topical authority.

### 3.2 High-Intent Technical Keywords
*   **Strategy:** Pivot content toward specific technical problems CEOs face (e.g., "Scaling GTV in Southeast Asia," "BSP Regulatory Sandbox Guide") rather than broad topics like "Leadership Tips."

---

## Pillar 4: Technical SEO & Performance
*The baseline for ranking.*

### 4.1 Speed & Web Vitals
*   **Action:** Leverage Hugo's image processing for all content bundles.
*   **Action:** Ensure `enableA11y = true` in `params.toml` for accessibility signals (a minor but real ranking factor).

### 4.2 Internal Linking (Read Next / Related)
*   **Action:** Systematically use the `related-posts-suggester` and `read-next-suggester` skills to increase "Dwell Time" and reduce bounce rates.

---

## Phased Implementation Roadmap

| Phase | Task | Impact |
| :--- | :--- | :--- |
| **Phase 1: Foundation** | Audit existing articles for H-tag discipline; Enable TOCs. | High |
| **Phase 2: AEO Entry** | Create and deploy `{{< quick-answer >}}` and `{{< faq >}}` shortcodes. | Critical |
| **Phase 3: Schema Pro** | Override theme's `schema.html` with advanced JSON-LD. | High |
| **Phase 4: Content Hubs** | Refactor category pages into "Topic Hubs" with descriptive bodies. | Medium |

## Verification & Metrics
*   **Google Search Console:** Track "Featured Snippets" and "FAQ Rich Results."
*   **Perplexity/AI Testing:** Manually query AI engines with specific questions from the site to see if they cite the "Quick Answer" blocks.
*   **Core Web Vitals:** Maintain 95+ scores on Desktop/Mobile.

---
**Status:** Drafted. Ready for review and implementation prioritization.
