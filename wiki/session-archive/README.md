# Session Archive

Plain-markdown archives of Cowork conversations for this project.

## Why

Cowork's `MEMORY.md` system persists *facts* across sessions, but not the conversational texture — the back-and-forth that explains *why* a decision got made or what a phrase like "the Pass G slider" referred to. This folder fills that gap.

## How it gets populated

After closing a working session, run from the project root:

```bash
python3 wiki/c2a2-wiki-narration/scripts/archive_session.py --latest
```

That script:

1. Finds the most recently modified Cowork session JSONL (under `$TMPDIR/claude-hostloop-plugins/.../*.jsonl`)
2. Strips system-reminders, tool calls, tool results, and queue noise
3. Writes a clean `YYYY-MM-DD-<topic-slug>.md` here
4. Prepends a one-line entry to `SESSIONS.md`

## Other invocations

```bash
python3 wiki/c2a2-wiki-narration/scripts/archive_session.py --session 8836970b-341f-456e-8382-a09162ffc298
python3 wiki/c2a2-wiki-narration/scripts/archive_session.py --jsonl /path/to/specific.jsonl
```

## Workflow protocol

Tom's three-stage flow becomes four when archive matters:

**Regen → Inspect → Push → Archive.**

The first three keep the wiki right; the fourth keeps the record of how it got that way.

## Privacy

Archives may contain anything that was discussed — decisions, file paths, emails, names. Treat this folder the way you treat the rest of the repo. If you went public with C2A2 but want session archives kept private, add `wiki/session-archive/` to `.gitignore`.
