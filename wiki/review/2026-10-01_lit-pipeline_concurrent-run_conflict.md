# Lit-search pipeline, 2026-10-01: two concurrent runs disagreed

**Status: needs Tom.** Nothing from the second run has been applied to the registers.

## What happened

Two instances of `c2a2-lit-search-pipeline` processed the 09-30 intake (PRESUMPTION-1099..1102 plus 9 in-house items) at the same time, between about 00:34 and 00:38. There is no run lock (ASSUMPTION-1699 / MONITOR-631). This is the same split-execution-surface pattern that PRESUMPTION-1099 describes.

- **Instance A** committed first, at 00:38:27. It recorded DISPOSITION-1017..1020, all MONITOR (MONITOR-634..637), and routed the in-house items to MONITOR-638..646.
- **Instance B** (this report) searched independently and reached REVISE on all four items. It applied nothing, to avoid blending or overwriting A's committed run.
- **Side effects of A:** A overwrote B's eight result files, which had the same names. Only the summaries below survive; B's full source lists and STEELMAN blocks are lost. A also stripped the item IDs from 9 in-house header lines in for_lit_search.md. **B restored those IDs** and kept A's tags. queue_scan.py now reads 0 undispositioned items and a bare backlog of 147 (down from 151).

## Why they disagree

**Orientation.** The queue's "Claim to test" lines for 1099–1102 state the critique or remedy, for example "per-environment health checks give false negatives". presumptions.md states the presumption itself, for example "the fleet behaves as if it has one surface and one observer". A tested the queue lines. B tested the presumptions.

On substance the two runs agree: neither found that the presumptions hold. A then held its remedy-claims at MONITOR because the support was indirect. B treated the same evidence as a strong challenge to the presumptions and applied the "presumption + strong challenge → REVISE" heuristic.

| Item | A (committed): 15a / 15b → disposition | B (not applied): 15a / 15b → disposition |
|---|---|---|
| 1099 one surface, one observer | PARTIAL Moderate / PARTIAL Weak → MONITOR-634 | PARTIAL Weak / CHALLENGED Strong (Gray Failure, HotOS 2017) → REVISE-495 High |
| 1100 last line = current state | PARTIAL Weak-Mod / NO-CHALLENGE → MONITOR-635 | PARTIAL Weak / CHALLENGED Strong (Fowler 2005, Event Sourcing) → REVISE-496 Medium |
| 1101 defer to absent designer | SUPPORTED Moderate / … → MONITOR-636 | PARTIAL Moderate / PARTIAL-CHALLENGED Moderate → fold into REVISE-486 (same premise as PRESUMPTION-1079) |
| 1102 no-op run is free | PARTIAL Weak-Mod / PARTIAL Moderate → MONITOR-637 | PARTIAL Weak / CHALLENGED Strong (AutoBot-AI #17726; Deng 2026 "vacuous success") → REVISE-497 Medium |

A's 4-of-4 MONITOR result is the sink pattern that REVISE-492 (09-30) describes.

## Decisions for Tom

1. **Which run stands?** Option (a): keep A, the status quo. Option (b): adopt B, which means closing MONITOR-634..637 → REVISE-495..497 plus the REVISE-486 corroboration. B's records are below, ready to paste. Note that DISPOSITION-1017..1020 are A's numbers; adopting B means minting DISPOSITION-1021..1024 as re-dispositions.
2. **Fix the queue format.** The "Claim to test" line should state the presumption itself, or state its orientation explicitly. Otherwise two honest runs can reach opposite results from the same evidence.
3. **Add a run lock.** MONITOR-631 is now a realized failure: two concurrent runs, overwritten files and corrupted headers. A lock file written at start and checked before any write would have prevented it.

---

## Instance B: proposed records (NOT applied)

*These were drafted before the collision was found. Their DISPOSITION numbers (1017–1020) and in-house MONITOR numbers (634–642) collide with A's committed records, so renumber them if adopted. The in-house routing is moot, because A already routed those items, to MONITOR-638..646.*

## 15c — dispositions, 2026-10-01

DISPOSITION-1017:
  Date: 2026-10-01
  Item: PRESUMPTION-1099
  Item type: PRESUMPTION (unstated — surfaced by inference)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: 15a found support only for a different design (one external observer that every surface reports to); nothing supports a surface-local monitor covering the fleet. 15b's gray-failure and meta-monitoring sources describe exactly the observed pattern (Mac watchdog blind to cloud runs; ten weeklies silent with no alarm).
  Disposition: REVISE → REVISE-495
  Reasoning: Presumption + strong challenge + weak, conditional support + realized failure -> REVISE/High per heuristic. Consistent with and extends PREMISE-086 (alarm on age), PREMISE-100 (liveness is not correctness), PREMISE-221 (signal must probe the source) and REVISE-490 (co-located monitors); no contradiction.
  What is at risk: Every scheduled task split across cloud and local schedulers (32 migrated tasks); morning status reports; the weekly agents; OPEN-257 / OPEN-260.
  Recommended action: (1) One fleet manifest: every task, its surface, and its expected cadence. (2) Every run, on either surface, writes a last-seen line to one shared heartbeat file. (3) One absence check ("expected by T, not seen") that reads the manifest and the heartbeat file, run from a surface independent of both schedulers or cross-checked by each. (4) Each surface's monitor states what it cannot see.
  Urgency: High
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

DISPOSITION-1018:
  Date: 2026-10-01
  Item: PRESUMPTION-1100
  Item type: PRESUMPTION (unstated — surfaced by inference)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: Both sides agree on the condition: the latest line is the state only when it is a full, fresh snapshot from one authoritative writer. C2A2's status files hold attempts from several writers, so the condition fails. 15b's event-sourcing and last-writer-wins sources match the observed errors (FAIL over a current PASS; one count reported as 8, 10, 11).
  Disposition: REVISE → REVISE-496
  Reasoning: Presumption + strong challenge; 15a's own condition is the remedy. Urgency Medium, matching 14b's risk rating; ASSUMPTION-1712/1714/1716 (now MONITOR-637/639/640) are the in-house fixes. Consistent with PREMISE-220 and PREMISE-221; no contradiction.
  What is at risk: REFRESH_STATUS.md, QC logs, pending-count reports, morning status; any agent that reads the last line of a shared status file.
  Recommended action: (1) Status files become append-only, each line carrying writer, run ID, timestamp, and separate "attempt outcome" and "state" fields. (2) Current state is computed by one stated rule over those lines, not hand-written. (3) Show the age of every status value. (4) Never infer "did not run" from a missing line without checking the run record.
  Urgency: Medium
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

DISPOSITION-1019:
  Date: 2026-10-01
  Item: PRESUMPTION-1101
  Item type: PRESUMPTION (unstated — surfaced by inference)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Moderate (narrow form) / None ("reviewer is live")
  15b result: PARTIALLY-CHALLENGED | 15b strength: Moderate
  Net assessment: The two sides converge. Deference is supported as a reversible hold on irreversible or high-stakes actions (Off-Switch Game; hold-on-timeout practice; Deng 2026, honest stall beats confident error). It is not supported where it assumes a live reviewer or re-flags routine items: alert-fatigue and ironies-of-automation work show repeated flags to an absent human produce a backlog, not decisions.
  Disposition: REVISE → consolidated into REVISE-486 (no new REVISE number minted)
  Reasoning: Moderate-vs-moderate would ordinarily lean MONITOR, but the item is the same premise as PRESUMPTION-1079 (REVISE-486, 2026-09-24, Strong challenge, still AWAITING TOM), now with 7+ days more evidence. A MONITOR would be the sink pattern named in REVISE-492; a separate REVISE would add one more unread flag for an absent reviewer, which is the failure this item describes. 15c judgment call, stated: corroborate REVISE-486 and raise its evidence, rather than duplicate it.
  What is at risk: Every "flagged for you" run note; Day 076, WATCH-003, PROP-2026-08-14-033, PROP-2026-09-28-001, Summa length flags; PREMISE-093 (already flagged with REVISE-486).
  Recommended action: As REVISE-486, sharpened by this run's evidence: (1) Classify each held item by reversibility. Irreversible or high-stakes items keep the hold. Reversible routine items get a stated default that applies after a timeout and is logged. (2) Flag an item once and again only when it changes; no re-flagging every 4 h. (3) One daily digest of open escalations, ordered by age and risk. (4) An explicit "designer absent" mode, with the policy agreed in advance.
  Urgency: High
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED (via REVISE-486)

DISPOSITION-1020:
  Date: 2026-10-01
  Item: PRESUMPTION-1102
  Item type: PRESUMPTION (unstated — surfaced by inference)
  15a result: PARTIALLY-SUPPORTED | 15a strength: Weak
  15b result: CHALLENGED | 15b strength: Strong
  Net assessment: Support is limited to "one empty poll is cheap" and "exit 0 is success by convention", and 15a's own fetched source is mostly counter-evidence. 15b shows that an empty LLM wake costs a full invocation, and that clean-exit success can hide failure ("vacuous success"). Both apply to the 15-run Summa no-op streak and to full sandbox disks.
  Disposition: REVISE → REVISE-497
  Reasoning: Presumption + strong challenge + weak support -> REVISE. Urgency Medium (14b risk rating), but the disk-full link ties it to REVISE-490 (High). Consistent with PREMISE-100 (liveness is not correctness) and PREMISE-221; no contradiction.
  What is at risk: Summa batch and sweep tasks, reviewer triggers, any high-frequency scheduled task; sandbox disk; log signal-to-noise; token budget.
  Recommended action: (1) A cheap pre-check (file count, mtime, queue length) runs before any model is invoked; on empty, exit without the model. (2) Even then, write one liveness line ("ran, found nothing"), so empty and dead stay distinguishable. (3) Back off after N consecutive no-ops (for example, double the interval) and reset on new work. (4) Track consecutive no-ops as a metric and alarm past a threshold, since a long streak may mean a broken upstream. (5) Log rotation or a cap on log size.
  Urgency: Medium
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

In-house lane (no DISPOSITION numbers minted; precedent 2026-09-22..30): ASSUMPTION-1709 → MONITOR-634, -1710 → MONITOR-635, -1711 → MONITOR-636, -1712 → MONITOR-637, -1713 → MONITOR-638, -1714 → MONITOR-639, -1716 → MONITOR-640, -1718 → MONITOR-641, -1720 → MONITOR-642.

SYSTEMIC-RISK-FLAG (15b, 2026-10-01, High): silence read as health — PRESUMPTION-1099, -1100, -1102 directly, and -1101 in part. File: lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-10-01_silence-read-as-health.md. 15c concurs. This is the same family as PREMISE-100 and the 2026-09-30 self-referential-verification flag. The three new REVISEs (495, 496, 497) share one remedy: an independent, append-only run record that separates "ran", "found nothing" and "succeeded", and that the monitors read.

Running totals after this run: PREMISE-221 | MONITOR-642 | REVISE-497 | DISPOSITION-1020.
This run's distribution (4 new literature items): 0 INCORPORATE, 0 MONITOR, 4 REVISE (3 new + 1 consolidated into REVISE-486). MONITOR share 0% (per REVISE-492 reporting recommendation).

### Proposed revision_flags.md entries

REVISE-495:
  Date: 2026-10-01 | Source item: PRESUMPTION-1099 | DISPOSITION-1017 | Urgency: High
  Premise challenged: the scheduled-task fleet can be monitored as if it had one execution surface and one observer.
  Evidence: 15b CHALLENGED (Strong): Huang et al. 2017, "Gray Failure", HotOS (via fetched Demirbas 2019 review) - differential observability; Grafana 2021 meta-monitoring (search-result level). 15a PARTIALLY-SUPPORTED (Weak): Healthchecks.io (fetched) - one observer works only if every surface reports to it.
  What is at risk: Every scheduled task split across cloud and local schedulers (32 migrated tasks); morning status; the ten silent weekly agents; OPEN-257 / OPEN-260.
  Recommended action (for Tom): (1) One fleet manifest (task, surface, expected cadence). (2) Every run on either surface writes a last-seen line to one shared heartbeat file. (3) One absence check against the manifest, run from outside both schedulers or cross-checked by each. (4) Each surface's monitor states what it cannot see.
  Consistency: Extends PREMISE-086, PREMISE-100, PREMISE-221 and REVISE-490; no contradiction. Member of the 2026-10-01 silence-read-as-health SYSTEMIC-RISK-FLAG.
  Status: AWAITING TOM
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

REVISE-496:
  Date: 2026-10-01 | Source item: PRESUMPTION-1100 | DISPOSITION-1018 | Urgency: Medium
  Premise challenged: the latest line in a status artifact is the current state of the thing it describes.
  Evidence: 15b CHALLENGED (Strong): Fowler 2005, "Event Sourcing" (fetched); last-writer-wins / eventual-consistency literature (search-result level); Kleppmann 2017 (background, not verified). 15a PARTIALLY-SUPPORTED (Weak): holds only for a fresh, full snapshot from one authoritative writer.
  What is at risk: REFRESH_STATUS.md, QC logs, pending-count reports, morning status; any reader of the last line of a shared status file.
  Recommended action (for Tom): (1) Append-only status lines with writer, run ID, timestamp, and separate attempt-outcome and state fields. (2) Current state computed by one stated rule, not hand-written. (3) Age shown next to every status value. (4) No "did not run" inferred from a missing line without checking the run record. In-house fixes already queued: MONITOR-637, -639, -640.
  Consistency: Extends PREMISE-220 and PREMISE-221; no contradiction. Member of the 2026-10-01 silence-read-as-health SYSTEMIC-RISK-FLAG.
  Status: AWAITING TOM
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

REVISE-497:
  Date: 2026-10-01 | Source item: PRESUMPTION-1102 | DISPOSITION-1020 | Urgency: Medium
  Premise challenged: a no-op scheduled run is effectively free and counts as a success.
  Evidence: 15b CHALLENGED (Strong): mrveiss 2026, AutoBot-AI issue #17726 (fetched) - an empty LLM wake costs a full invocation; Deng 2026, arXiv:2606.11688 (abstract fetched) - "vacuous success" on exit 0; Zapier 2013 polling figures (search-result level). 15a PARTIALLY-SUPPORTED (Weak): cheap only at low scale, with a gate before the model.
  What is at risk: Summa batch/sweep tasks (15 consecutive no-ops), reviewer triggers, high-frequency tasks; sandbox disk (see REVISE-490); log signal-to-noise; token budget.
  Recommended action (for Tom): (1) Cheap pre-check before any model call; exit early on empty. (2) Still write one liveness line per run ("ran, found nothing"). (3) Back off after N consecutive no-ops; reset on new work. (4) Alarm on long no-op streaks (possible broken upstream). (5) Log rotation or a size cap.
  Consistency: Extends PREMISE-100 and PREMISE-221; links REVISE-490 (disk). Member of the 2026-10-01 silence-read-as-health SYSTEMIC-RISK-FLAG.
  Status: AWAITING TOM
  PROVENANCE: Origin: 14b | Chain: [14b → 15a, 15b → 15c] | Transform at this step: Net evaluation and disposition | Current status: REVISION-FLAGGED

REVISE-486 — CORROBORATED (2026-10-01) by DISPOSITION-1019 (PRESUMPTION-1101); no new REVISE number minted
  New evidence: 15a PARTIALLY-SUPPORTED (Moderate narrow / None for "reviewer is live"): Pan 2026 (fetched), Hadfield-Menell et al. 2017 Off-Switch Game; 15b PARTIALLY-CHALLENGED (Moderate): Ancker et al. 2017 repeated-alert fatigue, Bainbridge 1983, Elish 2019; Deng 2026 supports a hold over a wrong action.
  In-house: no human input for 7+ days; Day 076 re-flagged every 4 h; WATCH-003 checked 14 times identically; the 25th recommendation to split the watch list.
  Sharpened recommendation: keep the hold only for irreversible or high-stakes items; reversible routine items get a stated timeout default, logged. Flag once, then only on change. One daily digest ordered by age and risk.
  Why consolidated: a separate REVISE would add one more unread flag for an absent reviewer, which is the failure this item describes.
  Status: AWAITING TOM (unchanged)
