# Editorial Agent PRD and Implementation Plan

**Status:** Draft for review  
**Owner:** CEO Playbook  
**Initial runtime:** Codex  
**Design requirement:** The agent must remain portable to any capable outer agent or harness.

## 1. Product Decision

Build an Editorial Agent that turns an approved editorial backlog item into a governance-compliant, factually supported, on-brand, review-ready content package in the CEO Playbook repository.

The agent owns the work across the editorial process. It does not own publication, final editorial judgment, or merger authority.

The Managing Editor remains a reusable specialist skill. The Editorial Agent decides when to invoke it, research and drafting capabilities, image sourcing, validation, and GitHub operations.

## 2. Goal and Completion Contract

### Goal

> For each approved editorial brief, produce a governance-compliant, factually supported, on-brand, review-ready content package in the CEO Playbook repository, and stop at the defined human approval boundary.

### Completion

A content job is complete when all of the following are true:

1. A leaf bundle exists in the correct section and approved path.
2. The content type, frontmatter, taxonomy, citations, internal links, and AEO elements meet the published rules.
3. The selected featured image is relevant, licensed for use, 16:9 landscape, substantially free of text, and stored in the bundle with required attribution recorded.
4. `notes.md` records the editorial brief, source basis, taxonomy rationale, image candidates and selection, validation outcomes, and unresolved questions.
5. Required deterministic checks, including the Hugo build, pass.
6. The post frontmatter explicitly sets `draft: true`.
7. The work is committed and a GitHub PR linked to the original backlog issue is open.
8. The GitHub issue contains a concise decision log and links to the branch, bundle, validations, and PR.
9. The social-repurposing skill has produced review-ready candidate posts for X and LinkedIn, saved in the repository's `docs/repurposed/` archive and linked from the issue and `notes.md`.
10. Any decision outside agent authority is marked for human review.

The terminal state is **review-ready**. The agent does not publish, merge, distribute social posts, or change `draft` to `false` without a separate, explicit instruction.

### Release policy

Editorial completion and publication are separate events.

1. The Editorial Agent always creates or updates a post with `draft: true`, including when the source material already contains `draft: false`.
2. A reviewed PR can merge to `main` while the post remains a draft and therefore does not appear in the production Hugo build.
3. A human explicitly approves publication after editorial review, using `editorial:publish-approved` or an equivalent explicit instruction.
4. Publication is a small, separately auditable release change that sets only `draft: false` and confirms the production deployment.

## 3. Scope

### In scope

- GitHub Issue backlog intake and state management.
- Ideas, briefs, user-supplied drafts, links, and video URLs as source material.
- Content-type selection across Articles, Labs, Videos, Research, and other supported CEO Playbook sections.
- Research, drafting, editing, frontmatter generation, content provisioning, internal linking, image sourcing, validation, commit, and PR creation.
- Draft social repurposing for X and LinkedIn using the existing `repurpose-social` skill.
- A concise public decision log in GitHub and a local `notes.md` file.
- Deterministic evaluation and limited self-correction.

### Out of scope for the first release

- Automatic merging or publishing.
- Automatic posting to social channels.
- Creation of new categories or tags without human approval.
- Use of private or paid sources unless the issue explicitly grants access and permission.
- Rewriting unrelated published content to create incoming links.

## 4. Operating Model

```text
GitHub issue marked editorial:ready
  → claim job and record start
  → assess source material and content type
  → research and draft, or edit a supplied draft
  → provision branch and leaf bundle against the same issue
  → invoke Managing Editor and supporting skills
  → source and select featured image
  → validate, correct, and revalidate
  → create X and LinkedIn candidate posts
  → commit and open PR
  → record handoff and stop at review-ready
```

The agent is the outer orchestrator. It retains job state and chooses the next action. Its constituent skills own bounded procedures.

## 5. GitHub Editorial Backlog

### One issue per post

One GitHub issue follows each post from idea to merge. It is the durable record for the brief, decisions, branch, PR, and human review.

The existing `content-creator` and `managing-editor` flows must support two modes:

1. **Agent mode:** Receive an existing eligible issue and create the branch, bundle, commit, and PR against that same issue. Do not create another issue.
2. **Direct-use mode:** When invoked without an issue, create a new issue before provisioning the branch and leaf bundle, preserving the current standalone workflow.

### Labels and states

| Label | Meaning | Set by |
| --- | --- | --- |
| `editorial:queued` | Idea exists but lacks enough direction to start. | Human |
| `editorial:ready` | Eligible for autonomous intake. | Human |
| `editorial:in-progress` | Claimed by the agent. | Agent |
| `editorial:blocked` | Missing authority, sources, or a human decision. | Agent or human |
| `editorial:review` | PR is open and review-ready. | Agent |
| `editorial:merged` | PR merged and repository state is complete. | Automation or human |
| `editorial:publish-approved` | A human authorizes the separate release change from `draft: true` to `draft: false`. | Human |
| `editorial:published` | The explicit release change is merged and deployment is confirmed. | Human or approved release automation |

An automation selects only open issues labelled `editorial:ready`, excludes `editorial:blocked`, and processes one item per run unless explicitly configured otherwise. It posts a claim comment before branch creation to avoid duplicate work.

### Issue template

The backlog template should accept incomplete ideas, but define these fields when known:

```markdown
## Editorial brief
- Objective and reader:
- Core claim or question:
- Source material or full draft:
- Required facts, links, or citations:
- Optional content-type preference:
- Video URL, if applicable:
- Image direction or exclusions:
- Private or paid-source permission, if applicable:
- Approval constraints:
```

`editorial:ready` requires an objective plus usable source material, a full draft, or explicit permission for the agent to research and draft from the idea.

## 6. Content Classification and Drafting

The agent proposes the section based on the brief, available evidence, and intended reader:

| Signal | Likely section |
| --- | --- |
| Strategic thesis or operating lesson | Article |
| Technical experiment, workflow, architecture, or tool learning | Lab |
| A video URL or primary media asset | Video |
| Evidence-led, reference-heavy deep analysis | Research |

The content type is a proposal, not a hidden decision. The issue decision log records the rationale. A human can override it by editing the issue or applying a designated override label before the PR is created.

### Research and drafting

The agent uses a research-and-drafting capability before Managing Editor when the issue does not include a full draft. It must:

1. Prefer primary sources.
2. Use reputable reporting only when primary evidence is unavailable or insufficient.
3. Separate evidence, inference, and opinion.
4. Cite material factual and time-sensitive claims.
5. Preserve supplied drafts unless the brief authorizes substantive rewriting.
6. Draft in the established CEO Playbook voice: direct, first-person where appropriate, specific, operator-led, and free of generic AI language.

Private or paid material is available only when the issue expressly states the permitted source or access route.

## 7. Featured Image Policy

### Objective

Every eligible post receives one featured image suitable for Hugo.

### Selection policy

The agent sources three candidate images and scores them on:

1. Relevance to the post's actual argument.
2. Real-photo preference and editorial quality.
3. License and attribution requirements.
4. 16:9 landscape compatibility.
5. Minimal or no embedded text, logo, watermark, or misleading visual claim.
6. Fit with the CEO Playbook visual character.

The agent records all three candidates, their source URLs, license or attribution basis, and its selection rationale in `notes.md` and the GitHub issue. It commits only the selected image to the content bundle.

### Source order

1. Licensed or freely usable real photography, beginning with Pixabay through an approved API or compliant retrieval path.
2. Another approved stock or first-party source with clear use rights.
3. AI-generated imagery only when suitable real photography cannot communicate the post well and the backlog does not prohibit it.

The implementation must store the original source URL, creator attribution when required, license basis, selected filename, and image dimensions. It must not silently reuse images with unclear rights.

## 8. Audit Record

### GitHub issue comment

The agent posts concise, decision-useful updates. It does not post hidden reasoning or chain-of-thought.

Required entries:

- Job claimed and branch created.
- Content-type decision and rationale.
- Research basis and source list.
- Featured-image candidates and selection rationale.
- Evaluation results and corrections made.
- PR URL, artifact paths, and outstanding human decisions.

### `notes.md` in the leaf bundle

`notes.md` is a review aid, not published content. It should include:

```markdown
# Editorial Notes

## Brief and intended reader
## Content-type and taxonomy rationale
## Research basis and citations
## Featured image candidates and selected asset
## Social draft archive
## Validation record
## Open questions and human decisions
```

The Hugo configuration must exclude `notes.md` from rendered site content, or the agent must use the repository's existing mechanism for non-rendered bundle notes.

## 9. Authority and Human Gates

| Action | Authority |
| --- | --- |
| Claim an eligible issue | Autonomous |
| Choose a section from approved types | Autonomous, with logged rationale |
| Create a branch, leaf bundle, commits, and PR | Autonomous |
| Research public sources and draft | Autonomous |
| Select an approved-license featured image | Autonomous |
| Generate X and LinkedIn candidate posts | Autonomous |
| Create a new tag or category | Human approval required |
| Use private or paid material | Only with explicit issue permission |
| Change `draft` to `false`, publish, merge, alter unrelated published content, or post social content | Explicit human instruction required |
| Continue after repeated unresolved evaluation failures | Human review required |

## 10. Evaluation and Recovery

The Editorial Agent inherits the Managing Editor evaluation suite and adds agent-level checks.

### Existing checks

- Leaf bundle structure.
- Governance-compliant frontmatter.
- Required AEO elements.
- Related and next-reading navigation.
- Style restrictions.
- Hugo build.

### New checks

- Backlog issue exists and is the issue linked by the resulting PR.
- Correct editorial state transitions and decision-log comments.
- `notes.md` exists and contains all required review fields.
- Every cited external source has a title and URL.
- Image is present when required, is landscape 16:9 or compatible with approved crop policy, and has no substantial embedded text.
- Image source, attribution, and license basis are recorded.
- Every agent-created post has `draft: true`, regardless of supplied frontmatter.
- The agent cannot mark a job review-ready or create its PR if `draft: false`.
- A social-draft archive exists for the post and contains X and LinkedIn candidates created by the existing `repurpose-social` skill.
- No duplicate issue is created when the agent begins from an existing backlog issue.
- PR remains in review-ready status and does not merge or publish.

The agent gets two targeted correction passes after a failed evaluation. It reruns only the affected checks when practical. A third unresolved failure changes the issue to `editorial:blocked`, posts the failure report, and stops.

## 11. Harness-Neutral Architecture

The agent specification must describe capabilities, state, inputs, outputs, authority, and terminal conditions without relying on a specific vendor or framework.

| Portable capability | Codex implementation |
| --- | --- |
| Read and update backlog | GitHub CLI or GitHub connector |
| Repository worktree | Codex workspace and shell tools |
| Specialist procedures | Skills such as Managing Editor, Content Creator, research/drafting, linking, and image curation |
| External research and images | Approved web, API, or MCP tools |
| Durable state | GitHub issue, branch, PR, `notes.md`, and the repository |
| Scheduling | Codex automation that prompts the outer agent to claim the next eligible issue |
| Human approval | Issue labels/comments, PR review, and explicit task instructions |

In Codex, a top-level Codex task is the outer agent. The Editorial Agent will be a dedicated orchestration skill or equivalent durable instruction set that the task invokes. `AGENTS.md` retains non-negotiable repository policy. `config.toml` controls runtime configuration, not the agent's editorial logic.

## 12. Implementation Plan

### Phase 1: Specify the contract

1. Approve this PRD and the exact issue-label convention.
2. Add a GitHub Issue template for editorial backlog items.
3. Add a harness-neutral Editorial Agent specification, including input schema, authority rules, state transitions, completion contract, and decision-log format.
4. Define an automation prompt that selects one eligible issue and exits cleanly when the queue is empty.

### Phase 2: Make existing skills issue-aware

1. Update `content-creator` to accept an existing issue identifier and provision without creating a duplicate issue.
2. Update `managing-editor` to receive and preserve the issue context through branch, draft, validation, and PR.
3. Add or adapt a research-and-drafting skill that can draft from a brief or improve a supplied full draft.
4. Add a `notes.md` template and confirm it will not render as public Hugo content.

### Phase 3: Add image curation

1. Create a featured-image curator capability with a source adapter for Pixabay and later approved providers.
2. Add image-candidate scoring, license recording, 16:9 validation, text detection, and attribution output.
3. Add the selected asset to the leaf bundle and link the attribution record to the issue and `notes.md`.
4. Add explicit AI-image fallback rules.

### Phase 4: Agent orchestration and evals

1. Create the Editorial Agent orchestration skill for Codex.
2. Connect the specialist skills in the required sequence with clear handoff inputs and outputs.
3. Invoke `repurpose-social` after the content draft and canonical URL are established, then save its X and LinkedIn candidates in `docs/repurposed/`.
4. Add agent-level validation checks and two-pass recovery logic.
5. Add a dry-run mode that writes a plan and decision log without creating a branch or PR.
6. Test against representative jobs: an idea-only issue, a supplied full draft, a video-based post, and a blocked private-source case.

### Phase 5: Controlled automation

1. Run the automation against one explicitly marked pilot issue at a time.
2. Review the issue log, `notes.md`, PR quality, image selection, and correction behavior.
3. Tighten authority and eval rules before increasing the schedule or concurrency.

## 13. Acceptance Criteria

The first production-ready version succeeds when it can take one `editorial:ready` issue, create no duplicate issue, select or honor the content section, produce a cited draft with `draft: true`, a selected featured image, and X and LinkedIn candidate posts, pass all checks, create one linked PR, write the required audit trail, and stop for human review without publishing, merging, or posting social content.

## 14. Decisions Still Required Before Implementation

1. Confirm the exact GitHub label names and whether the repository already has them.
2. Confirm the source and credential path for Pixabay API use.
3. Confirm the Hugo-safe convention for `notes.md` inside leaf bundles.
4. Decide whether image candidates should be stored as issue-comment URLs only or in a non-published review directory.
5. Select the first pilot backlog issue and the automation cadence.
