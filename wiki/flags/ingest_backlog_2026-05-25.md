---
type: ingest-backlog
detected_on: 2026-05-25
detected_by: c2a2-wiki-daily-run (orchestrator, unattended)
status: OPEN — pending attended PRS-extraction session(s) (Tom directed: "All these belong live")
severity: HIGH (escalated 2026-05-26 17:42 ET → reaffirmed 2026-05-26 EOD)
last_re_checked: 2026-05-26 EOD (Tom approved all 28 today, confirmed go-live intent for the prior 36 as well — total ingest queue now 62 real proposals)
---

## 2026-05-26 17:42 ET — Backlog grew to 61

Tom processed 25 APPROVE decisions in an attended session (review-page state pasted into
Cowork; Gmail decision-email body was unreliable due to a UI workflow misfire — body said
all-PENDING despite the page showing 25 approvals). The 25 approved proposals were moved to
`inbox/proposals/approved/` AND copied to `inbox/` per Phase-0 spec.

**New backlog size: 61 approved-but-not-ingested files** (was 36).

The earlier 36-file backlog (source-dated 2026-04-21 → 2026-05-12) is unchanged in identity.
The 25 new additions are source-dated 2026-04 → 2026-05-25 and span 9 traditions:

| Tradition | Existing 36 | New 25 | Combined |
| --- | --- | --- | --- |
| wolfram | 6 | 4 | 10 |
| levin | 2 | 4 | 6 |
| rohr | 2 | 5 | 7 |
| carroll | 5 | 2 | 7 |
| wright | 3 | 3 | 6 |
| fredrickson | 4 | 2 | 6 |
| mcgilchrist | 2 | 2 | 4 |
| stump | 3 | 1 | 4 |
| hoffman | 3 | 0 | 3 |
| friston | 2 | 1 | 3 |
| kastrup | 2 | 1 | 3 |
| arkanihamed | 2 | 0 | 2 |

Effective unique items: ~60 (subtract the 1 resolved Singer duplicate flagged in the original 36).

**Recommended next action (escalated):** the focused-ingest pass is now the single largest
unblocking action for the network. ~60 files × 12 traditions × full PRS/cross-program/
findings updates is multi-session work; recommend Tom carves out a dedicated 2-3 hour block
and runs ingest in tradition-batches (e.g., wolfram first, then levin, then rohr, etc.)
rather than one monolithic pass.

# Ingest Backlog Detected — 2026-05-25

## Summary

36 files sit in `wiki/inbox/` that are **not** recorded in `PROCESSED_LOG.md` and whose
PRS content is **absent** from the tradition wikis (verified by grep against
`traditions/*/prs_triplets.md` and `wiki.md`). 35 of them are `status: approved`
(approved in Tom's **2026-05-13** decision batch; source-dated 2026-04-21 → 2026-05-12).
They were copied into `inbox/` on approval but the Phase-1 ingest never ran for them.

This was **deliberately deferred, not skipped**, by today's unattended daily run.
Rationale: a 35-file / ~90-triplet mutation across 12 tradition wikis + master +
cross-program index + pattern-detector + log is too large and error-prone to perform
unattended at the tail of the daily cycle. It belongs in a focused (ideally attended)
ingestion session where IDs, counts, and cross-program entries can be reconciled and
verified. (Standing rules: caution over speed; fail loud; surgical changes;
don't silently overrun.)

## Why it happened (likely)

- The **2026-05-13 decision email approved a large batch** (PROP-2026-05-13-001 … -036+).
  Phase 0 copied the approved files into `inbox/`.
- The 2026-05-17 reconciliation only ingested the four **2026-05-13-dated** files.
  The older-dated approved files in the same batch (2026-04-21 → 2026-05-12) were
  never ingested.
- Since 2026-05-13 **no decision emails have been processed**, so the pipeline has
  not cycled and the backlog persisted across the 05-18/19/20/24 runs.

## Backlog by tradition (36 files)

| Tradition | Count | Notes |
| --- | --- | --- |
| wolfram | 6 | |
| carroll | 5 | incl. 1 resolved duplicate (2026-04-21 Singer/Mindscape-351, superseded by approved 2026-05-08 version) |
| fredrickson | 4 | |
| wright | 3 | new-ish tradition; God's Homecoming essay + book + Collins-Oxford |
| stump | 3 | |
| hoffman | 3 | incl. "Hoffman's Law" Edge.org (PRS-CANDIDATE flagged Medium-High) |
| rohr | 2 | |
| mcgilchrist | 2 | |
| levin | 2 | |
| kastrup | 2 | |
| friston | 2 | |
| arkanihamed | 2 | |

Effective unique approved items to ingest: **34** (35 approved minus the 1 resolved
Singer duplicate; the canonical Singer item is the approved 2026-05-08 file).

Full file list is reproducible with:
```
cd "wiki"
find inbox -maxdepth 1 -type f -name '*.md' ! -name PROCESSED_LOG.md ! -name README.md -printf '%f\n' \
  | sort | while read f; do grep -qF "$f" inbox/PROCESSED_LOG.md || echo "$f"; done
```

## Recommended next action

Run a **dedicated backlog-ingest pass** (one tradition at a time, with per-tradition
PRS-ID sequencing, cross-program entries, pattern-detector evaluation, and a count
reconciliation against the master wiki). After ingest, each file's name must be added
to `PROCESSED_LOG.md` so the log is authoritative again.

## Related open items (surfaced same run)

- **28 proposals waiting in `inbox/proposals/pending/`** — no decision email has been
  processed since 2026-05-13. These are separate from the ingest backlog above (these
  are awaiting Tom's APPROVE/DENY, the backlog above is already-approved-but-not-ingested).
