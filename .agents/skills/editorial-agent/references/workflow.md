# Editorial Agent Workflow Reference

## Backlog states

| State | Meaning |
| --- | --- |
| `editorial:queued` | Idea needs a usable brief or explicit research authority. |
| `editorial:ready` | Eligible for one agent run. |
| `editorial:in-progress` | Claimed by an active agent. |
| `editorial:blocked` | Waiting for missing authority, material, or a human decision. |
| `editorial:review` | Linked PR is open and ready for review. |
| `editorial:merged` | The content PR merged with `draft: true`. |
| `editorial:publish-approved` | A human has authorized the separate release change. |
| `editorial:published` | The release change merged and deployment was verified. |

## Required issue comments

Use concise, decision-useful updates. Do not expose private reasoning.

### Claim

```markdown
## Editorial Agent claim

- Status: `editorial:in-progress`
- Branch: `<branch>`
- Brief assessment: `<ready, blocked, or clarification needed>`
- Next action: `<research, draft refinement, or provisioning>`
```

### Decision record

```markdown
## Editorial decision record

- Content type: `<type>`
- Rationale: `<one concise paragraph>`
- Research basis: `<primary sources and permitted secondary sources>`
- Taxonomy: `<category and tags, or approval request>`
- Internal links: `<selected target-draft paths and rationale; incoming recommendations if any>`
- Featured image: `<three candidate URLs, rights basis, and selection>`
- Social drafts: `<path>`
```

### Handoff

```markdown
## Review-ready handoff

- Bundle: `<path>`
- Draft status: `true`
- Validation: `<pass or blocker>`
- PR: `<url>`
- Human decisions: `<none or list>`
```

## Featured-image policy

Record three candidates in `notes.md` and the issue. Prefer real photography from an approved source such as Pixabay. Require a direct source URL and rights or attribution basis for every candidate.

Select only an image that is relevant, 16:9 landscape or crop-compatible, and free of substantial text, logos, and watermarks. Store the selected image as `featured.<extension>` in the bundle. Do not use an image with unclear rights.

## Recovery

Correct a failed deterministic check twice. After the second failed correction, label the issue `editorial:blocked`, remove `editorial:in-progress`, post the concise failure report, and stop.
