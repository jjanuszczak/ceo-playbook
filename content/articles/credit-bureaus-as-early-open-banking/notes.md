# Editorial Notes

## Brief and intended reader

Issue #122 asked for an article for senior financial services executives explaining credit bureaus as an early form of open banking, with added research and a Philippine/LenderLink example.

## Content-type and taxonomy rationale

Content type: Article. The brief explicitly preferred an article and the content is strategic fintech analysis rather than a technical Lab, video, or research memo.

Category: Fintech. Tags use approved governance terms: open-finance, credit-scoring, financial-inclusion, lending, api-economy, regtech, systems-thinking.

## Research basis and citations

Research used public, high-authority sources and company primary sources:

- Library of Congress, "Dun & Bradstreet Founded": Mercantile Agency, Lewis Tappan, Bradstreet history.
- Equifax UK, "Credit experts since 1899": Retail Credit Company origin.
- FTC, "Fair Credit Reporting Act": consumer reporting rights and obligations.
- World Bank, "Credit Reporting": credit infrastructure and financial inclusion basis.
- BSP, "Open Finance PH": Philippine open finance pilot and API framing.
- CFPB, "Personal Financial Data Rights": U.S. open banking and consumer data-rights context.
- LenderLink platform and FAQ pages: product positioning, consent-driven API exchange, daily refresh, and 45 million-plus records.

## Internal linking record

Applied three contextual links in the article:

- `articles/future-of-finance`: supports the Philippines open-finance and embedded-finance framing.
- `articles/ikbr-ban`: supports the argument that consumer protection should open access without creating blunt exclusion.
- `articles/ai-enabling-bank-infrastructure-matters`: supports the point that AI and underwriting depend on clean data infrastructure.

Incoming-link opportunities were not applied because the Editorial Agent workflow allows edits to the owned draft without approval, but not unrelated published pages.

## Featured image candidates and selected asset

Image search used `scripts/find_pixabay_candidates.py` with the project Pixabay key from the main checkout because `.env` is not copied into linked worktrees.

Candidates:

1. Selected: https://pixabay.com/photos/hands-phone-smartphone-electronics-1851218/ by Pexels. Rights basis: Pixabay Content License, current terms to be verified before publication. Selected because it directly supports mobile-first, consented digital credit access without logos or text.
2. https://pixabay.com/photos/girl-typing-type-use-using-mobile-791570/ by kaboompics. Rights basis: Pixabay Content License, current terms to be verified before publication. Strong mobile-credit metaphor, but less neutral framing than the selected asset.
3. https://pixabay.com/photos/mortgage-house-contract-sign-home-5266520/ by Tumisu. Rights basis: Pixabay Content License, current terms to be verified before publication. Strong credit/loan visual, but more mortgage-specific and less relevant to Philippine mobile lending.

Committed asset: `featured.jpg`, cropped to 1280x720 from the selected Pixabay download.

## Social draft archive

Saved draft-only X and LinkedIn candidates under `docs/repurposed/2026-08-07-credit-bureaus-as-early-open-banking.md`.

## Validation record

Pending. Planned checks: Managing Editor eval, Editorial Agent package eval with social draft, and Hugo build through the editorial eval runner.

## Open questions and human decisions

No blocking human decisions. Before publication, verify current Pixabay license terms and review the LenderLink description for commercial sensitivity.
