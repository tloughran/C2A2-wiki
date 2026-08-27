# Cowork Progress Summary — 2026-08-25
*Generated at 18:40 EDT for daily walk Chat context*

> **DELIVERY FAILED — read this file directly.** `list_connected_browsers` returned an
> empty list. This is the **fourth consecutive Chrome failure**: 08-24 morning, 08-24
> evening, 08-25 morning (`chat_to_cowork/2026-08-25_chat_summary.md`), and now tonight.
> The Chat↔Cowork loop has been open at both ends for two full days. Nothing else in the
> pipeline is blocked by this, but Chat has had no Cowork context since 08-23 and Cowork
> has had no walk context for the same span.
>
> Fix: leave Chrome running with the Claude side panel signed in as
> thomas.loughran@gmail.com at 08:50 and 18:40 EDT.
>
> Also standing: Atlassian, Figma, Intercom, Linear, Notion, Slack and Datadog all report
> needing interactive authorization and are unavailable to scheduled runs.

## What Was Accomplished Today

**The infrastructure recovery from the 08-22/08-23 outage held.** Scheduler health is
85 OK / 1 WARN / 2 FAIL, down from 4 FAIL yesterday and 20 on 08-23. Four separate FAILs
cleared overnight: the missed-fire storm, `com.tloughran.summa-vault-sync` exit-1, the
12-day `metabolism_data.json` staleness, and — notably — **the git debris flagged as
yesterday's #1 next step** (stale `ORIG_HEAD.lock`, 254 stranded tmp objects) is gone.

**But the daily run still committed nothing.** It fired 08:34Z and completed every phase;
`commit_check` reports the newest `C2A2 daily run` commit is still 2026-08-24 17:30Z. The
git-debris hypothesis from yesterday has now been falsified — the debris cleared and the
commit still didn't happen. **The cause is something else and is not yet identified.**

**A new failure appeared: OpenStory ingest is stopped.** `com.tomloughran.openstory.watchdog`
FAILED at 05:15 — `/Volumes/H-Drive` is not mounted. Sessions stop being created within
about a day of the volume going away. A restart cannot fix this; the drive has to be
plugged in. `com.c2a2.metabolism-publish` also exited 1 again on its Sunday fire.

**Openstory telemetry was moved onto launchd and proved.** REFRESH_STATUS logs
`2026-08-25T17:40Z PASS — telemetry 33 agents, node_edges current, DB age 6h`. The run
that looked hung was buffered, not stalled (launchd redirects stdout to a file, so Python
block-buffers). `PYTHONUNBUFFERED` was prescribed for the plist after completion.
**Open item: the Cowork scheduled task and the launchd agent now both write the same
files and should not both be enabled.**

**Two Summa passes ran, and both turned up the same defect class.**
- *Commentary reviewer* (18:25–18:32) — Days 236 and 237, both rewritten in place, zero
  escalations. Day 236: Levin PRS-03 was carrying a half-correct gloss — the attractor
  formalism matches, the barrier-removal half appears nowhere in PRS-03. Moved to PRS-49
  (HCN2 electroceutical repair with the causative mutation still present), a *stronger*
  warrant than the one it replaced. Day 237 was the better find: the day's single best
  source sat in frontmatter as an id-less phrase — "Stump corporate-substance node" —
  while the body argued Q.49 a.1 by Levin analogy alone. Stump PRS-14 and PRS-15 answer
  the premise directly and are now cited.
- *QC sweep* — Days 131 and 132, four repairs, **all of them lowering or disclosing
  confidence rather than raising it.** Rohr PRS-03 removed from a file that never cited
  Rohr at all — the fourth "Universal Christ" label trap of the day. Friston PRS-13
  disclosed as a *trauma* record whose formalism transfers but whose clinical evidence
  does not. A Wright enemy-love declination was tested, found honest, and left unfixed
  rather than forced onto a wrong id.
- Both frames confirm: **`length_actual_words` is exact, not understated** — five exact
  readings in two days retires that presumption in both directions. Transcript counts
  remain a separate open question.

**Lit-search pipeline ran overnight and is fully drained.** 26 items searched by 15a,
33 by 15b, **35 dispositioned by 15c** between 00:47 and 01:00. Zero bare-[QUEUED] items
remain. 27 new for/against result pairs written.

**Fourteen new proposals filed** across Levin (3), Friston (3), Rohr (3), Wright (2),
Stump, Hawkins, Carroll. Review page `2026-08-25_review.html` generated at 04:53 with
**74 cards — exact coverage of all 74 pending, zero phantoms.**

## Key Decisions Made

**None recorded.** The register still ends at **DECISION-078 (2026-07-05)** — 51 days.
`decisions.md` has not been written since 08-06. The self-awareness pipeline that would
extract today's decisions fires ~23:30 local, after this file.

## New Open Questions

**None recorded.** The register ends at **OPEN-165 (2026-08-23)**, unchanged and still the
most consequential item standing: *which success criterion governs the accelerator —
overlap or novelty — and until that is settled, what would count as failure?*

Today added a third instance of the same shape, this one methodological rather than
conceptual: the **uncited-frontmatter-source defect is now a standing class, not a series
of incidents** — Rohr PRS-04 (Day 236), Wright PRS-03 (Day 237), Rohr PRS-03 (Day 131),
Fredrickson PRS-01 (Day 132), plus Day 132 this afternoon. Five in one day. And Day 237's
"Stump corporate-substance node" shows the harder version: **a generic parenthetical passes
every id-existence check in the system, because there is no id in it to check.**

## Files Created or Modified

- `review/2026-08-25_review.html` — new, 872 KB, 74 cards
- `inbox/proposals/pending/2026-08-25_*.md` — 14 new proposals
- `architecture/lit_search_results/{for,against}/` — 27 new pairs (ASSUMPTION-1160–1203, PRESUMPTION-690–876)
- `architecture/for_lit_search.md`, `lit_search_returns.md`, `monitor_queue.md`, `revision_flags.md` — updated
- `agents/openstory/agent_telemetry.json`, `agent_node_edges.json`, `REFRESH_STATUS.md` — refreshed 13:43–17:40
- `agents_tab.html`, `review_log.html`, `level2_signal_stream.html`, `master/C2A2_master_wiki.md` — rebuilt 04:55–13:43
- `deferred/watch_list.md` — 2 checks run, 2 stale flags raised, 0 resolved
- `vault/_index/QC log.md` — 4 Summa day-pairs repaired

## Pipeline Status

- **Lit search queue:** 1788 items (870 assumptions, 823 presumptions); 1879 disposition
  records; **0 bare-[QUEUED]** — the search and disposition stages are drained
- **Validated premises:** 43
- **Pending proposals:** **74** — was 60 yesterday, 54 on 08-18. **+14 in one day**
- **Deferred items watching:** 2 active, **both flagged STALE** (WATCH-002, WATCH-003);
  next checks 2026-09-01 at count 7 each
- **Summa QC queue:** 307 pairs, 99 flagged needs_review — all 99 for the same reason
  (`QC older than 7 days`), zero frontmatter or static issues, zero never-reviewed
- **Agent telemetry:** 33 agents, fresh as of 17:40Z, now on launchd
- **Scheduler:** 85 OK / 1 WARN / 2 FAIL
- **Days since last daily-run commit:** 1 (but 11 of the last 12 days had none)

## What's Next

1. **Plug in the H-Drive.** OpenStory ingest is stopped and nothing else can restart it.
   Data loss begins within ~24 hours of the volume going away — this is the only item on
   the list with a clock on it.
2. **Run the review pass.** 74 proposals, oldest untouched since 08-08, page ready and
   exactly covering the queue. This is now day 17 of the gap and the queue grew 23% today.
3. **Find the real reason the daily run commits nothing.** Yesterday's git-debris theory
   is dead — the debris cleared and the behavior didn't change.
4. **Disable one of the two Openstory refresh paths** before they race on the same files.
5. **Restore Chrome** — the sync has now failed four times running.
6. Choose the bridging metric (carried from 08-24, undecided).
7. `com.c2a2.metabolism-publish` exit 1, second Sunday running.

## For Morning Discussion

**The review gate is now the whole story, and today it moved backwards.** Every automated
stage around it is green — lit search fully drained, telemetry fresh, scheduler recovered,
git debris cleared. The one stage with a human in it has been silent seventeen days, and
today the queue went 60 → 74 while nothing left it. The agents keep clearing their own
blockers and handing you a larger pile. **The daily-run agent's Phase 2 self-narrowing from
08-24 still awaits your ratification or reversal** — it named the rule it chose not to
follow and has had no answer.

**Today produced the cleanest evidence yet that the wiki's citation layer has a systematic
hole.** Five uncited-frontmatter defects in one day, and one of them — Day 237's "Stump
corporate-substance node" — is uncatchable by any check the system currently runs, because
a phrase with no id in it can't fail an id-existence test. Two ideas surfaced independently:
the **unused-source check** (flag frontmatter ids that appear nowhere in the body — cheap,
and on Day 132 it caught the expensive article-coverage gap for free), and the
**article-coverage differ** (which must report a ratio and name omissions, *not* flag
uniformly — Day 131's 8-of-20 coverage is explicitly licensed by `Summa.md`). Four
deterministic candidates have now been named across five runs and **none is built.** This
is a small amount of code that would close a defect class you are currently finding by hand.

**Every Summa repair today lowered confidence.** Four repairs, four downward. Combined with
yesterday's two-corrected-downward result, that's six consecutive corrections that made the
wiki claim *less*. That is either the system working exactly as designed, or a sign the
original synthesis pass was systematically over-confident — and which of those it is bears
directly on OPEN-165, because it is a question about what the register's evidence claims
are actually worth.

**Budget: fifteenth consecutive breach on the Summa cap.** Both runs report again that
6 pairs and 30k tokens cannot both hold at body-verification standard; 2–4 is the honest
ceiling. The agents are surfacing this loudly every run rather than silently cutting
corners, which is the behavior you asked for, and it has now gone fifteen runs without a
ruling. Raise the budget, lower the cap, or lower the standard.

**Carried and still unanswered:** OPEN-165 (overlap vs. novelty — what counts as failure);
OPEN-164 (the agent-invented addendum convention, unratified); the INTEGRITY FLAG ruling
that would close WATCH-003 and half of WATCH-002; the Channel 2 question, standing since
08-23; and the `watch_list.md` run-log split — the file is now **493 KB** and cannot be
opened with the Read tool at all, so Agent 16 works entirely through shell greps.

---
*Sources: session transcripts (Summa commentary reviewer, Summa qc sweep, Openstory agents
telemetry refresh, Scheduler health check); vault files under `architecture/`, `deferred/`,
`agents/openstory/`, `inbox/proposals/pending/`, `review/`.*
