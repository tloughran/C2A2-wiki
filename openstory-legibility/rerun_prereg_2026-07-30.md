# Pre-commitment — Rung 1 re-run on an expanded human corpus

**Committed:** 2026-07-30, local, **before the analysis was executed** and before any new numbers
were observed. The Jun 30 report (`rung1_report.md`, N=14) is the only Rung-1 result seen to date.

## What is being done

Re-running `rung1_uptake.py` **unmodified** (deterministic, TF-IDF, 200 shuffles, seed 1729, no
model) against a fresh static snapshot `open-story-snapshot-2026-07-30.db`, taken by
`sqlite3 .backup` from the live `open-story.db`.

This is a **descriptive re-run of an existing analysis on more observational data**. No parameter,
filter, threshold, or statistic is changed. The script's own dedup (event_ids-keyed) and
well-posedness filter (each role ≥3 utterances, ≥10 total) are untouched.

## Why the corpus changed

No new collection. The original snapshot (2026-06-29) held 223 turn-bearing sessions; the live DB
has since grown to 947. An events-based proxy suggested roughly 172 sessions may now pass the
well-posedness filter, versus 14 before. That proxy is **not** the script's filter and may be
wrong; the run itself is the measurement.

## What we expect, stated before seeing it

1. **Direction holds.** Median real adjacent similarity exceeds the role-matched null, as at N=14
   (median lift +0.053, positive 14/14, p<0.05 in 13/14).
2. **Per-session significance rate falls somewhat.** The original 13/14 came from a small,
   self-selected set of unusually rich dialogues. A larger, less curated population should include
   more marginal sessions, so the *proportion* clearing p<0.05 is expected to drop even if the
   aggregate direction strengthens.
3. **Median lift shrinks or holds; it should not grow much.** Same reasoning.
4. **AI↔AI remains near zero and likely still unmeasurable.** Scheduled agent runs are single-shot
   and should not pass the ≥3-utterances-per-role gate.

## What would falsify / surprise

- Median lift ≤ 0, or the majority of sessions failing to beat their shuffle — would contradict
  the original finding rather than extend it.
- Substantive N coming in near 14 — would mean corpus growth is not dialogue growth, and the
  proxy misled.
- Substantive N wildly above ~172 — would suggest the dedup is not absorbing the 9.64× replay
  inflation and the count is contaminated.

## Discipline note

The risk this file exists to foreclose is authoring predictions *after* seeing results. It does
not claim the status of the study's original preregistration (`sim_preregistration.md`), which
governs the simulation arm. Whether a strengthened human-arm result warrants a formal
re-preregistration before publication is a separate decision, deliberately left open here.
