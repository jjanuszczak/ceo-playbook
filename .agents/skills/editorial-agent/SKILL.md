---
name: editorial-agent
description: Turn an approved CEO Playbook GitHub editorial-backlog issue into a review-ready draft package. Use when Codex must claim an `editorial:ready` issue, choose a content section, research or refine a draft, coordinate content skills, source a featured image, prepare social drafts, validate the bundle, and open a linked PR without publishing.
---

# Editorial Agent

Own the editorial job from an eligible GitHub Issue through a review-ready PR. Stop before merging, publishing, or posting to social channels.

Read [workflow.md](references/workflow.md) before starting a job. Read `assets/notes.md` before creating the bundle-local audit record.

## Completion contract

Complete a job only when its post has `draft: true`, the required bundle assets and `notes.md` exist, content checks pass, X and LinkedIn candidates have been saved under `docs/repurposed/`, and a PR linked to the original issue is open.

Never change `draft` to `false`, merge a PR, publish, or post social content unless the user explicitly asks.

## Workflow

1. Claim one open issue labelled `editorial:ready`, confirm it is not `editorial:blocked`, and change its state to `editorial:in-progress`. Post the claim comment from the workflow reference.
2. Read the brief, supplied material, and authority constraints. Stop and mark the issue blocked if the brief lacks usable material and does not authorize research.
3. Propose the content type from the brief. Use Articles for strategic analysis, Labs for technical work, Videos for a primary video URL, and Research for evidence-led analysis. Record the choice in the issue.
4. Invoke `content-research-writer` when the issue needs research or a full draft. Preserve a supplied draft unless substantial rewriting is authorized.
5. Invoke `content-creator` with the existing issue identifier. Do not create a second issue. Create a new issue only when this skill is invoked directly without one.
6. Invoke `managing-editor` to enforce taxonomy, metadata, AEO structure, internal links, and draft status. Run `internal-linker` with `--allow-draft-target`, read its shortlist, and add 2 to 4 relevant contextual Hugo links to the draft itself. Record the selected paths and rationale in `notes.md` and the issue. A `No contextual-link fit:` exception requires a concise rationale. Force `draft: true` regardless of supplied frontmatter.
7. Source three featured-image candidates. Prefer licensed real photography. When `PIXABAY_API_KEY` is available, use `scripts/find_pixabay_candidates.py` and read `references/pixabay.md`. Record candidate URLs, rights basis, and selection rationale. Commit only the selected 16:9 landscape asset. Use image generation only when real photography cannot express the argument and the brief does not prohibit it.
8. Create `notes.md` from the bundled template. Include the concise decision record, not private reasoning.
9. Invoke `repurpose-social` to save X and LinkedIn candidates under `docs/repurposed/`. Draft only. Do not post.
10. Run Managing Editor checks and `uv run python .agents/skills/editorial-agent/evals/runner.py <bundle> --social-draft <path>`. Apply two targeted correction passes. On a third unresolved failure, mark the issue `editorial:blocked`, post the report, and stop.
11. Commit the content package, social draft archive, and audit notes. Open a PR that closes the original issue, apply `editorial:review`, post the handoff comment, and stop.

## Authority

Act without approval only for the issue states, drafting, contextual edits to the draft the agent owns, existing taxonomy, feature-image selection with clear rights, branch creation, validation, and PR creation defined above.

Require human approval for a new category or tag, private or paid sources without explicit issue permission, changing unrelated published posts, publishing, merging, and social posting.

## Resources

- `scripts/claim_next_issue.py`: Find or claim one eligible issue. Use `--dry-run` before scheduling an automation.
- `scripts/find_pixabay_candidates.py`: Return horizontal real-photo candidates when `PIXABAY_API_KEY` is available.
- `scripts/validate_editorial_package.py`: Verify local review-ready artifacts.
- `evals/runner.py`: Run local package validation and the Hugo build, then save a structured report.
- `assets/notes.md`: Copy into the content leaf bundle as `notes.md`.
- `references/workflow.md`: State labels, comment formats, image policy, and recovery rules.
