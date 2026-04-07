# Conversation Inbox
*Drop transcripts here for agent ingestion*

---

## How to Use This Inbox

This folder is the input queue for the C2A2 agent network. When you have a conversation transcript — from a human dialogue, an AI-assisted research session, a Mindscape podcast episode summary, or any other source — place it here and the appropriate agent(s) will process it on their next run.

---

## File Naming Convention

```
[YYYY-MM-DD]_[tradition-key]_[brief-description].md
```

**Tradition keys:**
- `levin` — Michael Levin content
- `friston` — Karl Friston content
- `hoffman` — Donald Hoffman content
- `hawkins` — Jeff Hawkins content
- `mcgilchrist` — Iain McGilchrist content
- `fredrickson` — Barbara Fredrickson content
- `stump` — Eleonore Stump content
- `carroll` — Sean Carroll content
- `arkanihamed` — Nima Arkani-Hamed content
- `wolfram` — Stephen Wolfram content
- `kastrup` — Bernardo Kastrup content
- `multi` — Content touching multiple traditions (Master Agent will route)
- `C2A2` — Content about the C2A2 project itself

**Examples:**
```
2026-04-05_levin_mindscape-interview-notes.md
2026-04-07_multi_consciousness-roundtable-transcript.md
2026-04-10_friston_active-inference-paper-summary.md
```

---

## Transcript Format

Paste transcripts in plain markdown. You do not need to pre-format them. The agents will extract PRS triplets from whatever raw material you provide. However, if you want to accelerate processing, you can add a header:

```markdown
# Transcript: [title]
Date: [YYYY-MM-DD]
Tradition(s): [list]
Source: [podcast episode, paper, conversation, etc.]
Priority: [High / Normal]

[raw transcript or notes below]
```

---

## What Agents Do With Transcripts

1. **Program Agent** reads the transcript
2. Extracts Problems, Resources, and Solutions relevant to its tradition
3. Updates its Wiki with new PRS triplets
4. Flags any cross-tradition signals
5. Writes dispatches to `wiki/master/incoming_dispatches.md`
6. **Master Agent** reads dispatches and integrates into master Wiki
7. **Pattern Detector** evaluates flagged candidates

---

## Processed Transcripts

When an agent has processed a transcript, it will add `[PROCESSED by [Agent] on YYYY-MM-DD]` to the top of the file. Do not delete processed transcripts — they form the provenance record of the knowledge network.

---

## Priority Queue

If you want a transcript processed urgently (before the next scheduled run), note `Priority: High` in the header and the next manual agent run will prioritize it.

---
*Inbox initialized: 2026-04-03*
*Transcripts pending: 0*
