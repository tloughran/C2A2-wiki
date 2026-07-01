# C2A2 Literature Search Pipeline — Run Report

**Date:** 2026-06-30 (autonomous; Tom not present)
**Task:** c2a2-lit-search-pipeline (Agents 15a / 15b / 15c)
**Outcome:** 157/157 queued items processed end-to-end. Queue drained to 0.

## What was in the queue

Two distinct cohorts were waiting:

- **147 weekly MONITOR refresh items** re-triggered by Agent 15d on 2026-06-28 (a catch-up run — the 06-14 and 06-21 weekly fires had been missed). 124 were at cycle 3, 23 at cycle 1. All had existing for/against result files from prior cycles.
- **10 brand-new items** queued 2026-06-29 (ASSUMPTION-388..391, PRESUMPTION-419..424) from the metabolism-axis / dashboard-liveness / git-push-pattern review. First-time searches.

## How each cohort was handled

**147 refreshes (carry-forward, per established convention).** A `RE-TRIGGER cycle N` block was appended to each item's `for/` and `against/` result file. Rather than 294 exhaustive per-item searches, the run did a **genuine landscape spot-check of 6 real web searches** across the cohort's dominant clusters (Goodhart/surrogate-metrics; git autostash safety; dashboard freshness/staleness; HITL quality gates; SMS-OTP/passwordless security; multi-agent consensus/idealist convergence). No disposition-flipping shift surfaced; all 147 were re-dispositioned **MONITOR (carried forward), trajectory stable**.

**Fail-loud exception:** the SMS-OTP / authentication security cluster remains **STABLE-but-STRONG** against — NIST SP 800-63-4 (July 2025) excludes SMS OTP from AAL2, and 2026 regulatory deprecation deadlines (UAE Mar, India Apr, Philippines Jun) continue. Not auto-escalated (no *new* evidence; human-review gate), but surfaced for you.

**10 new items (genuine first-time searches → dispositions):**

| Item | Disposition | Note |
|---|---|---|
| A-390 (feed liveness ≠ axis liveness) | **INCORPORATE → PREMISE-089** | Per-source freshness independence is settled data-observability doctrine. Complements PREMISE-086. |
| P-421 (no freshness watchdog; "someone will notice") | **REVISE-157 (HIGH)** | Contradicts PREMISE-086 (dead-man's-switch). A 12-day freeze ran undetected. |
| P-422 (no per-axis as-of marking) | **REVISE-158 (HIGH, low-effort)** | Documented best practice is per-widget "data last updated"; the expert viewer was actually misled. |
| P-419 (signals/day = synthesis yield) | **REVISE-155 (HIGH)** | Textbook Goodhart trap; unstated; extends the 2026-06-29 proxy-as-truth systemic risk. |
| P-420 (attended-gating benefit justifies cost) | **REVISE-156 (MED-HIGH)** | Benefit unmeasured against a concrete 12-day freeze / ~68-card queue. |
| P-424 (habitual autostash is a clean win) | **REVISE-159 (MED)** | Normalizes push-debt; untracked files aren't stashed; extends REVISE-150. |
| A-388 (signals/day as amplitude axis) | **MONITOR-406** | OK only paired with a quality counterweight. |
| A-389 (attended-gating of PRS extraction) | **MONITOR-407** | Sound HITL; blanket vs selective-routing is the open question. |
| P-423 (add an agent vs consolidate feeds) | **MONITOR-408** | Root cause is the missing watchdog, not missing capacity. |
| A-391 (autostash safely handles ~20 files) | **MONITOR-409** | Safe for tracked files / clean re-apply only. |

## Systemic-risk threads for your attention

- **Liveness / observability gap** (NEW): A-390 / P-421 / P-422 / P-423. Root fix = one automated per-axis freshness watchdog + per-axis as-of timestamps — both in the PREMISE-086 dead-man's-switch family. **REVISE-157 and REVISE-158 are the highest-value, lowest-effort fixes from this run.**
- **Structural-proxy-as-ground-truth** (continuation): signals/day-as-yield (A-388/P-419) extends the 2026-06-29 connectivity-as-proxy flag (P-414).
- **Push-debt** (continuation): A-391/P-424 extend PRESUMPTION-412 / REVISE-150 (deferred pushes & dirty trees accumulate rather than converge).

## Priority order for Tom
REVISE-157 (HIGH — liveness single-point-of-failure, contradicts PREMISE-086) → REVISE-158 (HIGH, low-effort — per-axis timestamps) → REVISE-155 (HIGH — Goodhart) → REVISE-156 (MED-HIGH) → REVISE-159 (MED).

## Running maxima after this run
PREMISE-089 · MONITOR-409 · REVISE-159 · DISPOSITION-373

## Files written (in `wiki/architecture/`)
- `lit_search_results/for|against/` — 147 re-trigger blocks appended + 10 new files each
- `for_lit_search.md` — all 157 tagged `[SEARCHED-15a][SEARCHED-15b][DISPOSITIONED-15c: 2026-06-30]`
- `lit_search_returns.md` — refresh-batch returns + DISPOSITION-364..373 + consistency check + run tally
- `monitor_queue.md` — 147-item carry-forward log + MONITOR-406..409
- `validated_premises.md` — PREMISE-089
- `revision_flags.md` — REVISE-155..159

Pre-run backups of all five register files are in the session outputs folder (`backup_20260630-044737/`).

## Notes / judgment calls (autonomous run)
- Followed the established re-trigger convention (carry-forward + sampled landscape check) rather than 294 exhaustive searches — this matches every prior weekly cycle on file and respects the token budget. The convention itself records this honestly ("spot-check is a sample").
- The 10 new items got genuine first-time web searches because they were first-time, researchable, and operationally consequential.
- 15d had already advanced cycle counts and set the next weekly check (2026-07-05) on its 2026-06-28 run; this 15c pass records re-confirmation only and does not double-advance them.
