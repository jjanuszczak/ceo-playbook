# Editorial Notes

## Brief and intended reader

Issue #166 asks for an editorial essay / manifesto-explainer arguing that algorithmic feeds collapse news, trends, and creator-audience relationships into restatement loops. Intended reader: builders, writers, and creators who feel the feed is broken and want a practical frame rather than a product tour.

## Content-type and taxonomy rationale

Content type: Article.

Category: Technology, because the piece analyzes feed infrastructure, AI, RSS, and platform product incentives as enabling systems rather than as a personal reflection or pure strategy post.

Tags: `artificial-intelligence`, `knowledge-management`, `platform-economics`, `systems-thinking`, `open-source`.

## Research basis and citations

Primary brief materials:

- Origin X post: https://x.com/oldstackjournal/status/2103952778406318474
- Jack Conte SXSW 2024 keynote: https://youtu.be/5zUndMfMInc
- Issue notes on X news/trend restatement loops and RSS as decentralized follow infrastructure.

Public sources used:

- Pew Research Center, "Sizing Up Twitter Users": top 10% of U.S. adult Twitter users produced 80% of tweets.
- Pew Research Center, "The Behaviors and Attitudes of U.S. Adults on Twitter": top 25% produced 97% of tweets in the observed sample; original posts were 14% of tweets from this high-volume group.
- Google Developers Blog, "Announcing turndown of the Google Feed API": feed API history and 2016 shutdown.

## Internal linking record

Applied contextual links:

- `articles/building-an-audience`: supports the point that owned audience paths and reasons to return matter more than rented reach.
- `articles/is-ai-killing-book-reading`: supports the distinction between AI summaries and independent judgment.
- `articles/discovery-to-knowledge`: selected from the internal-linker shortlist; supports the distinction between fast source discovery and earned understanding.
- `articles/architecture-of-attention`: supports the article's information-architecture and signal/noise frame.

Incoming-link recommendations should be handled separately after editorial review; no published posts were edited in this run.

## Featured image candidates and selected asset

Pixabay attempt:

- `python3 .agents/skills/editorial-agent/scripts/find_pixabay_candidates.py "newspaper reader train station" --limit 3` failed in sandbox with DNS.
- The same command with network approval reached Pixabay but returned HTTP 403 with the project key. Fallback used licensed real photography from Unsplash/Wikimedia.

Candidates:

1. Selected: https://unsplash.com/photos/a-person-reading-a-newspaper-next-to-a-laptop-1RVduxIDdY4 by Anna Keibalo. Rights basis: Unsplash License, source page states free to use under the Unsplash License. Selected because it shows a person reading news beside a laptop, which fits the old/new feed argument without fake trend screenshots, logos, or AI-brain imagery. Downloaded and cropped to 1280x720 as `featured.jpg`.
2. https://unsplash.com/photos/a-man-reading-a-newspaper-while-using-a-laptop-lZVozQJ5wfY by Sortter. Rights basis: Unsplash License. Rejected because the Bitcoin chart creates a narrower crypto/investing signal that would distract from the reader-infrastructure argument.
3. https://commons.wikimedia.org/wiki/File:Joe_Frazier_reading_newspaper.jpg by Hans Peters/Anefo, Nationaal Archief. Rights basis: CC0 1.0 Universal Public Domain Dedication. Rejected because the named public figure and airport context are less relevant to user-owned reading infrastructure.

## Social draft archive

Saved under `docs/repurposed/2026-09-30-the-restatement-loop-repurposed.md`.

## Validation record

Provisioning:

- Content creator provisioner reused issue #166 and created branch `feature/166-article-the-restatement-loop`.
- Content creator eval reported a branch-name mismatch because it expected `feature/article-the-restatement-loop`, while the editorial workflow intentionally uses an issue-linked branch.

Editorial validation:

- Managing Editor eval passed on 2026-09-30.
- Repurpose Social eval passed on 2026-09-30.
- Editorial Agent package validation and Hugo build passed on 2026-09-30. Hugo reported 462 pages, 276 non-page files, 48 static files, 528 processed images, 126 aliases, and total build time of 3884 ms.

## Open questions and human decisions

No blocking human decisions. Before publication, verify current Unsplash license terms and decide whether to add any incoming internal links from published posts.
