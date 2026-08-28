# Cowork Progress Summary — 2026-08-27
*Generated 18:45 EDT for daily walk Chat context*

> ## ⚠ BROWSER DELIVERY FAILED — READ THIS FILE DIRECTLY
> Chrome MCP unreachable at 18:47 EDT; two connection attempts, both "Claude in Chrome is not
> connected." **This summary was NOT delivered to the daily walk Chat conversation.** Chat has no
> Cowork context for 2026-08-26 or 2026-08-27.
>
> **Both directions failed today** — the 08:52 morning scrape also failed. That is now **six
> consecutive days** of Chrome-MCP failure (08-23, 08-24, 08-25, plus today in both directions),
> which is the whole of OPEN-168.

**Delivery status: FAILED — see the banner above.** The morning scrape in the other
direction (`chat_to_cowork/2026-08-27_chat_summary.md`) FAILED — Chrome MCP unreachable at 08:52,
so today's Cowork sessions ran with no Chat context and fell back to the 08-26 material.

**Reconstruction note:** no interactive session transcript for today was identifiable in the
session list (all 40 most-recent entries are scheduled-task runs). This summary is reconstructed
from vault artifacts — the decision archive, the proposal directories, file mtimes, and the
Agent 16 run log. Treat the narrative as inferred from outputs, not read from a transcript.

## What Was Accomplished Today

**The review gate was cleared. This is the day's headline and it ends a nineteen-day stall.**

`inbox/proposals/pending/` went **80 → 0**. `approved/` went 301 → **378**. The last recorded
disposition before today was 2026-08-08.

It happened in two passes, both recorded in `review/archive/2026-08-27_decisions.md`:

1. **~12:15 — 60 approved en bloc, unread**, on the standing judgment that agent-produced
   source-capture proposals are output rather than candidates for individual review. Three
   duplicate re-proposals were quarantined to `_pending_dupes_resolved/`. Tom gave the approval
   in conversation after being shown the queue's shape (80 pending / 18 escalation-bearing /
   3 duplicates).

2. **Later the same day — the 18 held escalations reviewed and all approved**, recommended
   actions deferred to `DEFERRED_ACTIONS_2026-08-27.md`.

**The hold on those 18 turned out to be a classifier defect, and the diagnosis is the most
useful thing on today's record.** The classifier keyed on the strings "Recommend" and "needs a
human check." Of the 17 flagged passages, 11 were under `## Cross-Tradition Signals` —
agent-to-agent dispatch recommendations, not requests for a human decision. Six were
`SOURCE-READ NOTE` fail-loud provenance disclosures. **Exactly one** (#16, PROP-2026-08-23-002)
was a genuine request for a ruling on wiki state.

So the heuristic held proposals *for containing the richest cross-tradition content in the batch* —
which is precisely what `prototypes/harvest_signals.py` harvests into the Level-2 signal stream.
It suppressed the signal stream's best input for nineteen days. The archive records the ruling
explicitly: **do not re-apply that heuristic.**

**Downstream regenerations followed within the half hour**, which reads as the release working:

- `level2_signal_stream.html` regenerated **12:30**, ~15 min after the en-bloc approval.
- `metabolism/metabolism_data.json` + `metabolism_view.html` regenerated **12:42** —
  33 lanes, 3,260 runs, from openstory-db (db_mtime 12:38).
- `prs_3d.html` + `c2a2-prs-3d/template_prs_3d.html` rebuilt **13:26**.

**Second substantive piece: the PRS 3D time axis was materially corrected.**
`c2a2-prs-3d/prs_pub_years.json` went **231 → 562 entries** (+331 new, 0 removed), with
**104 existing entries changed**. The changes are the meaningful part — they move dates off
wiki-filing dates and onto real publication dates. Examples: `fredrickson-PRS-11` 2026-04-13 →
2025-01-01; `fredrickson-PRS-09` 2026-04-08 → 2025-12-10; `friston-PRS-15` 2026-05-13 →
2026-04-28. Prior to this, roughly a fifth of the dated PRS set was plotting on the day it was
filed rather than the year it was published. A `.bak` was kept.

**Also today:** Agent 16 (deferred/watch list) ran clean at 02:33 — no checks due, no intake in
any channel; `agents_tab.html` and the openstory telemetry/node-edge JSONs refreshed 06:18–06:29
(REFRESH_STATUS: PASS, 33 agents, DB age 13h).

## Key Decisions Made

No new `DECISION-NNN` entries were appended to `architecture/decisions.md` today — the register
still ends at **DECISION-078 (2026-07-05)**. The decisions below were made in conversation and
recorded only in `review/archive/2026-08-27_decisions.md`. **They are not on the decision
register.** That gap is itself a finding.

- **Approve 60 source-capture proposals en bloc, unread** — standing judgment that these are
  agent output, not review candidates.
- **Approve all 18 held escalations; defer the recommended actions** to
  `DEFERRED_ACTIONS_2026-08-27.md`.
- **Retire the "Recommend"/"needs a human check" hold heuristic.** It inverted — it held the
  highest-value cross-tradition content.
- **Do not fabricate an email entry in `provenance/decision_emails.json`** for this batch. The
  approval came through conversation, not the review-page email path, and that store's contract
  is verbatim email. Correct call; worth noting because it means this batch is invisible to any
  instrument that reads the email store as the decision record.
- **PROP-2026-08-17-003 — approve in principle, file stays quarantined.** Approving an escalation
  does not restore a duplicate.

## New Open Questions

No new `OPEN-NNN` entries were filed today. The register still ends at **OPEN-171 (2026-08-25)**;
165 unique headers against a max of 171 — the **46-id offset is carried, undiagnosed, fourth
consecutive record to state it and not file it.** "Max OPEN-171" is not a count.

Three questions on the register were **materially changed by today's events and should be updated**:

- **OPEN-171** (should proposal intake see the gate's depth?) — the gate emptied without any
  coupling being built. The question is now about whether the *next* stall gets caught, not this one.
- **OPEN-168** (notification channel of record when Chrome MCP is down) — **worsened; this is now
  day six**. Today's morning scrape failed again.
- **OPEN-165 / OPEN-164 / OPEN-170** (agent remit, unratified conventions) — the classifier that
  held the 18 is a concrete instance: an agent-side heuristic, never ratified, that cost nineteen
  days of signal-stream input.

## Files Created or Modified

- `review/archive/2026-08-27_decisions.md` — **new**; both batches, 77 approvals, 3 duplicates.
- `inbox/proposals/pending/` → empty; `approved/` 301 → 378; 77 files staged into `inbox/`.
- `c2a2-prs-3d/prs_pub_years.json` (+ `.bak`), `c2a2-prs-3d/template_prs_3d.html`, `prs_3d.html`.
- `level2_signal_stream.html`, `metabolism/metabolism_data.json`, `metabolism/metabolism_view.html`.
- `agents_tab.html`, `agents/openstory/agent_telemetry.json`, `agent_node_edges.json`, `REFRESH_STATUS.md`.
- `deferred/watch_list.md` — Agent 16 run appended (file now **>504 KB**; archival still unexecuted).
- **Not found in the mounted vault:** `PENDING_ESCALATIONS_2026-08-27.md` and
  `DEFERRED_ACTIONS_2026-08-27.md`. Both are referenced by the archive as living at repo root,
  which is above the mount. Unverified from here — **please confirm they exist on the Mac.**

## Pipeline Status

- Assumptions on register: **1,220** (no additions today)
- Presumptions on register: **886** (no additions today)
- Open questions: max **OPEN-171**, 165 unique headers, 46-id offset undiagnosed
- Decisions on register: max **DECISION-078**; today's 5 rulings **not yet filed**
- Lit search queue: 1,564 queued / ~1,893 dispositioned by 15c / **159 queued but never searched**
- Review gate: **pending 0** (was 80) · approved **378** · denied 1 · needs_review 1
- Deferred items watching: **2** (WATCH-002, WATCH-003), both stale-flagged, both next due 2026-09-01
- Metabolism: 33 lanes, 3,260 runs logged

## What's Next

1. **File today's five rulings as DECISION-079…083.** The register hasn't moved since 07-05 and
   the largest disposition batch in the project's history is currently recorded only in an archive
   file. This is the highest-value hour available tomorrow.
2. **Verify the two root-level docs exist** (`PENDING_ESCALATIONS_`, `DEFERRED_ACTIONS_`) — the
   deferred recommendations from 17 proposals are parked in one of them.
3. **Check that the Level-2 signal stream actually picked up the 17 released proposals.** It
   regenerated at 12:30, *before* the second batch landed. It may need a re-run.
4. **Watch the gate refill.** The tradition agents file daily and nothing was built to slow them.
   At the observed ~6–14/day rate the queue will be back near 80 inside two weeks.
5. WATCH-002 / WATCH-003 come due **2026-09-01** — five days out; both need a ruling first.

## For Morning Discussion

**1. The classifier inversion is the interesting object, not the backlog.**
A rule meant to protect human judgment held back exactly the material with the most cross-tradition
content, and it did so silently for nineteen days. Nobody wrote that rule as policy. It's the same
shape as OPEN-164 and OPEN-170 — an agent's local convention, never ratified, doing epistemic work
nobody authorized. Worth asking on the walk: *how many other unratified heuristics are filtering
the pipeline right now, and what would it take to enumerate them?*

**2. "Approved unread" — is that a review, and does the system know the difference?**
Sixty proposals were approved without being read, on a defensible standing judgment. But the
archive now records them identically to the 17 Tom actually read. Downstream, nothing can tell
them apart. Should the approval record carry the distinction — and if the answer is that
source-capture proposals don't need review, should they be routed around the gate entirely
rather than through it unread?

**3. The decision register is not the decision record.**
Today's rulings live only in `review/archive/`. `decisions.md` ends 07-05; `decision_emails.json`
correctly has nothing. Three stores, none of them complete. This connects to OPEN-169's question
about which instrument owns a number — same shape, applied to decisions instead of citations.

**4. OPEN-167 — the vault-root question, still the cheapest fix on the register.**
Three root forms are still live in scheduled task files. This task file still carries the
capital-`W` form. Corrected by hand again tonight; that's now five consecutive runs. It costs
about ten minutes to fix and it will keep costing a correction every night until someone does.

**5. OPEN-168 — day six with no working notification channel.**
Chrome MCP failed again this morning. Gmail draft creation demonstrably works from scheduled
tasks and isn't being used. This is a decision Tom can make in about thirty seconds on the walk:
*name the fallback channel.*

---

### Delivery note
Chrome MCP availability was not confirmed at generation time. If the browser delivery step below
this line did not run, **this file is the deliverable** — read it directly. The morning scrape in
the opposite direction already failed today, so treat Chat as having no Cowork context for
2026-08-26 or 2026-08-27 unless this message appears there.
