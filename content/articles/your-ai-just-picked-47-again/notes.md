# Editorial Notes

## Brief and intended reader

Issue #176 supplied a complete draft and public source material. This version is for technical executives, engineering leaders, and product managers who need a decision rule for using LLMs safely in production.

## Content-type and taxonomy rationale

Article, Technology. The piece concerns AI as an enabling technology and production-system controls. It uses existing canonical tags: `artificial-intelligence`, `software-engineering`, `systems-thinking`, `programming`, and `data-science`.

## Research basis and citations

- Randy Olson’s [reported informal experiment](https://x.com/randal_olson/status/2112210551137010100), cited as an observation rather than universal evidence.
- [NIST Random Bit Generation](https://csrc.nist.gov/projects/random-bit-generation) for the distinction between generator construction, entropy, and validation.
- Python’s [`secrets` module](https://docs.python.org/3/library/secrets.html) for an example of an operating-system-backed, cryptographically strong source.

## Internal linking record

- `articles/pilot-purgatory`: connects the difference between a demo and production controls.
- `articles/the-next-compiler`: extends the design-time code-generation argument and the need for review.

Both are published, directly relevant, and appear once in the reader path.

## Featured image candidates and selected asset

Pixabay search was attempted with the project key on 2026-10-21 and returned HTTP 403.

1. [Exploration (game) Dice](https://commons.wikimedia.org/wiki/File:Exploration_(game)_Dice.jpg), Smartiperson, CC0 1.0. Selected because it is a real photo, its rights are clear, it is relevant to the argument, and it crops cleanly to 16:9. Downloaded from the Wikimedia Commons file page and saved as `featured.jpg` at 1600×900.
2. [Dice 02138](https://commons.wikimedia.org/wiki/File:Dice_02138.JPG), Tukka, public domain. Real photo and crop-compatible, but less visually precise for this argument.
3. [A pair of dices sitting on top of a desk](https://unsplash.com/photos/a-pair-of-dices-sitting-on-top-of-a-desk-HD22QzPlTi4), Andrew Hampton, Unsplash License. Real photo, but not selected because the CC0 candidate provided clearer reuse terms for an editorial asset.

## Social draft archive

`docs/repurposed/2026-10-21-your-ai-just-picked-47-again.md`

## Validation record

- Managing Editor evaluation: pass.
- Repurpose Social evaluation: pass.
- Editorial package validator with the saved social draft: pass.
- Editorial Agent evaluation, including Hugo build: pass.
- Standalone `hugo --minify`: pass.
- Content Creator provisioner evaluation reports a branch-name mismatch because it expects `feature/article-your-ai-just-picked-47-again`; the issue-linked provisioner correctly created and checked out `feature/176-article-your-ai-just-picked-47-again`. No production-content check failed.

## Open questions and human decisions

None. The article retains `draft: true`.
