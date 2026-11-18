# Cowork Progress Summary — 2026-11-17
*Generated ~23:35 UTC (18:35 EST) for daily walk Chat context*
*Browser delivery (cloud copy): DELIVERED ~23:40 UTC via Claude in Chrome into today's walk chat ("Morning greeting", /chat/261fdb61…), condensed version. Built-in browser still redirects to the claude.ai sign-in page.*
*Caveat: session_info tools (list_sessions/read_transcript) are not in this run's tool set (cloud copy), so no Cowork transcripts were read. Built from wiki files modified today, register max IDs and run logs. No file evidence of an interactive Cowork session today: no TCNL reading log appears in `wiki/` (it may live outside the mounted folders, which this run cannot see). Tuesday's own 14a/14b local pass has not run yet (fires ~04:37 UTC tomorrow).*

## What Was Accomplished Today
- **14a/14b local pass for Mon 11-16 landed overnight** (~04:45 UTC). ASSUMPTION-2129..2135 (+7), PRESUMPTION-1249 (+1, methodological Medium), `metrics/2026-11-16_snapshot.md`.
  - PRESUMPTION-1249: the "significant work not yet captured" clause used three times in ten days, each in a week with nothing in the 30-day window. The clause may be filling quiet weeks rather than catching missed work.
  - ASSUMPTION-2129: the local lit run said the pipeline was "offline for over two weeks", but the lock file shows cloud-lit ran 11-15 and 11-16. Only the local copy is blocked.
  - ASSUMPTION-2130: scheduler health says disable all 27 duplicate local copies; the evening sync's local copy is the only one that reaches Chrome (it delivered to Chat 11-16, first in six days). A blanket disable would break at least two pipelines.
  - ASSUMPTION-2133: reviewer brief reports no Reports/ output for 21 weeks (not verified; Reports/ not mounted).
- **14a/14b cloud copy NO-OP**, 8th night (11-10..11-17, OPEN-299).
- **Lit pipeline:** cloud copy NO-OP (queue had only [IN-HOUSE] items; 0 searched). Local copy skipped again (lock script in `scripts/` unreachable; Desktop Commander auto-declined), 6th straight day.
- **Orchestrator / specialists:** no decision email, 0 ingested. **5 new cards**: 4 Hawkins (Thousand Brains forum talks: latency mismatches, Q4 research roadmap, scale invariance in Monty, variations in learned object models) and 1 Levin (Scale-free Niche Construction, OSF preprint, secondary-sourced, PROP-2026-11-17-005). **Pending now 16.**
- **Agent 16:** nothing due, nothing resolved. Watching 5, stale 3 (WATCH-003/004/006). Duplicate firing no-op.
- **Morning Chat→Cowork scrape succeeded** (covered the 11-16 walk). A walk did happen later today ("Morning greeting", 261fdb61: Project Mini progress, Fabrizio via Vince/Accenture and three candidate projects incl. Uganda biogas, demo-lab manufacturing, C2A2 orchestration); it was not scraped into Cowork and is not summarized here.

## Key Decisions Made
- None. DECISION-085 is still the highest (decisions.md unchanged since 10-28).

## New Open Questions
- None. OPEN-303 is still the highest (unchanged since 11-13).

## Files Created or Modified
- New: 5 pending cards (`inbox/proposals/pending/2026-11-17_*`), `review/2026-11-17_review.html`, `review/2026-11-17_lit-pipeline_second-run_skipped-lock-held.md` (misnamed: lock could not be acquired, not known held), `changelog/2026-11-17_changes.md`, `metrics/2026-11-16_snapshot.md`, `daily_sync/chat_to_cowork/2026-11-17_chat_summary.md`.
- Modified: `architecture/{assumptions,presumptions,for_lit_search}.md`, `changelog/2026-11-16_changes.md` (local pass appended), `deferred/watch_list.md`, `inbox/PROCESSED_LOG.md`, `master/C2A2_master_wiki.md`, dashboards (auto refresh), 15 vault transcripts (Summa batch).

## Pipeline Status
- Assumptions extracted: max ASSUMPTION-2135 (+7 overnight)
- Presumptions surfaced: max PRESUMPTION-1249 (+1)
- Lit search queue: +4 queued (all [IN-HOUSE]); 0 searched / 0 dispositioned today. [IN-HOUSE] lane still untouched; 15d backlog 151 bare items.
- Deferred items watching: 5 (WATCH-003..007), 3 stale
- Validated premises: validated_premises.md unchanged since 11-01 (not re-verified)

## What's Next
- TCNL reading pass in Cowork, per *Handoff — TCNL Reading Pass* (reading notes only, no introduction draft).
- Review 16 pending cards (approve Wolfram -001, deny duplicate -002; 4 new Hawkins talks; Levin LoRA-NCA and niche-construction cards).
- 11-19: WATCH-007 + MONITOR-719/720. 11-20: WATCH-003/004. 11-21: WATCH-005 goes stale if unmoved; WATCH-006.
- Educating Character Initiative smaller grant: due Dec 15.
- Carried over: REVISE-537..542; Kastrup merge (FPD-009); OPEN-283, OPEN-301/302/303.

## For Morning Discussion
1. **The six questions from the 11-16 sync are still open:** DECISION-086 (no bridge without a sourced structural link); one card-sourcing threshold plus `source_basis` field; scheduler duplicates; sync channel; 15d re-queue lane; Levin LoRA-NCA as metaphor.
2. **Scheduler duplicates, decided per task (OPEN-299 / ASSUMPTION-2124/2130).** Disable the cloud 14a/14b (8 NO-OPs) and the local lit copy (6 days blocked) or pre-approve its lock command / mount `scripts/`. Keep the local evening sync.
3. **Clause creep (PRESUMPTION-1249).** Today's Levin card is secondary-sourced and outside the window; Fredrickson 2022/2023 cards too. Tighten the "not yet captured" clause, or require a `source_basis`?
4. **Pending queue at 16 and climbing.** Worth a 20-minute triage before the TCNL reading starts?
5. **TCNL reading pass:** did it start? If so, where is the reading log kept, so this sync can report on it?

---
## Local-copy addendum (~23:45 UTC / 18:45 EST)
*Added by the local firing of c2a2-evening-cowork-to-chat. This copy has session_info, so it could check today's transcripts. It did not rewrite the summary above, and it did not send a second Chat message.*

- **Transcript check confirms the caveat above.** Every Cowork session active today was a scheduled task: morning walk handoff, scheduler health, morning chat scrape, project status, system health, Summa batch, agents, lit pipeline and self-awareness. No interactive Cowork session took place, so there is nothing to add to "What Was Accomplished".
- **The morning walk handoff (a4ce1ef0) found no walk notes in Gmail.** It added nothing to the queue and wrote `Reports/2026-11-17_morning_briefing.md`. It flagged two passed deadlines still open: Humanity AI (Oct 21) and DELTA (Oct 26). Close them or re-date them.
- **Scheduler health (10:45Z): 28 FAIL, 27 of which are the same double-registration.** All 47 cloud routines were OK at 12:10Z. The remaining FAIL is `com.tomloughran.openstory.ui`, whose plist is in the repo but not installed in launchd.
- **Chat was not sent a second time.** The local copy opened the walk chat in Chrome (/chat/261fdb61-bf11-422b-81bd-9d4d2410723d) and confirmed the cloud copy had already delivered the condensed summary to today's walk chat (~23:40 UTC), and a second near-identical message would just be duplicate noise. This is the double-registration problem from For Morning Discussion item 2, seen live: tonight both copies of this task ran.
- **Possible lead for item 5:** claude.ai Recents shows a chat titled "TCNL reading pass introduction". This copy did not open it. The TCNL work may be happening in Chat or Project Mini rather than in Cowork.
