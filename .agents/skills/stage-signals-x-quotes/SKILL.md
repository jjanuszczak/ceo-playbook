---
name: stage-signals-x-quotes
description: Stage the next eligible X post or X Article from a published CEO Playbook Signals post as a human-reviewed, ready-to-paste native X quote-post draft. Use when preparing the Signals promotion queue, reviewing its next item, or marking an X promotion posted, skipped, or deferred. Never use it to access X, publish, or automate a browser.
---

# Stage Signals X Quotes

Create a conservative promotion queue from published Signals posts. Keep the final judgment and native X quote-post action with John.

## Run the queue

Run the staging command from the repository root:

```bash
python3 .agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py stage
```

The command selects the next eligible source from the most recent published Signals post, proceeding in editorial order. It extracts the source, Summary, Why it Matters, and My Take. It writes durable local state to `data/signals-x-quotes/queue.json` and a ready-to-copy Markdown card to `docs/repurposed/signals-x-quote-queue.md`.

Use the original Signals copy for the Summary, Why it Matters, and My Take with only light edits for X readability. Do not trim or rewrite those sections merely to fit X's character limit. End each draft with this generic Signals callout, linking to the Signals section rather than the source post: `I curate, expand on, and share my take on great content like this in my weekly Signals: https://januszczak.org/signals/?utm_campaign=signals-x-quotes&utm_medium=social&utm_source=x`. Flag any character-limit overage for John's review, but retain the full draft. Save an approved manual edit with:

```bash
python3 .agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py set-draft --source <source-url-or-id> --text "..."
```

Inspect existing items with `list`. Update their state only after the human action:

```bash
python3 .agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py mark-posted --source <source-url-or-id> --published-url <x-post-url>
python3 .agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py skip --source <source-url-or-id>
python3 .agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py defer --source <source-url-or-id>
```

## Review and publish

1. Review the queue card and edit the draft if needed.
2. Copy the text and open the original source on X.
3. Use X’s native Quote action, paste the copy, and publish manually.
4. Record the resulting X URL with `mark-posted`.

Do not call the X API, store X credentials, use DrissionPage, scrape X, control an X browser session, or publish automatically. Do not mark an item posted until its native X quote post exists.
