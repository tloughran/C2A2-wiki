# Summa Curriculum — Missing-Days & Coverage Gaps

**Generated:** 2026-05-12 from `wiki/vault/refs/summa_index.json` (last sync 2026-05-12 01:00).

Audit of `available` and `day` fields across all 2,648 article entries. Goal: keep the *furthest-progress* number honest. Any day or article below the current high-water mark that is missing is flagged here so the headline "Day N reached" claim stays a real claim about cumulative coverage, not just about how far the index has touched.

---

## Headline numbers

| Metric | Value |
|---|---|
| High-water day (highest day with any content) | **Day 80** |
| Last continuous day with no gaps below it | **Day 34** ⚠ |
| Days populated in range 1-80 | 70 / 80 (87.5%) |
| Days populated in full 308-day plan | 70 / 308 (22.7%) |
| Articles available across all parts | 671 / 2,648 (25.3%) |

The Day-34-vs-Day-80 spread (46 days of distance) is the cost of the gaps below the high-water mark. If you want to be able to honestly tell someone "we've done N days continuously," that N today is **34**, not 80.

**Note on Day 1:** Day 1 is the Introduction lecture — present on disk as `vault/transcripts/Day-001 - Introduction.md` and `vault/synthesis/Day-001 - Introduction - Contemporary.md`, but absent from `summa_index.json` because the index is keyed by `Part.Q.A` and intro days have no Summa article mapping. Day 1 is counted as covered in the headline metrics above and is **not** a gap. If future intro/intermission/recap days appear, they should be treated similarly (see "Open questions" below for the proper architectural fix).

---

## Priority 1 — Day-level gaps below the high-water mark

These break the linearity of progress and should be filled before Day-81+ work proceeds.

| Missing day(s) | Position | Likely covers | Notes |
|---|---|---|---|
| Day 35 | Mid Prima Pars | (between I.Q66 at Day 34 and I.Q69 at Day 36) | Would cover I.Q67-Q68 (see Priority 2 below — these Qs are flagged as skipped) |
| Days 62-65 | End of Prima Pars / pre-I-II | (between I.Q119 at Day 61 and I-II.Q10 at Day 66) | 4-day gap. May be the transition wrap-up of Prima Pars or the formal start of I-II (Q1-9) — see Priority 2 |
| Days 71-75 | Mid I-II | (between I-II.Q19 at Day 70 and I-II.Q30 at Day 76) | 5-day gap. Almost certainly covers I-II.Q20-Q29 (the skip the explorer surfaces) |

**Total: 10 days missing below the high-water mark** (excluding Day 1, which is the intro lecture and is present — see Headline note).

---

## Priority 2 — Question-level skips inside otherwise-done brackets

Questions that sit inside the "done" range of their part but have zero articles marked available.

### Prima Pars (I) — 95.2% done (556/584)
| Skipped Q(s) | Title | Likely day(s) |
|---|---|---|
| I.Q11 | The Unity of God | (would land near Day 7-8) |
| I.Q14 | God's Knowledge | (would land near Day 9-10) |
| I.Q67-Q68 | The work of distinction / The work of the second day | Day 35 (which is itself missing) |

### Prima Secundae (I-II) — 18.7% done (115/616)
| Skipped Q(s) | Title (range) | Likely day(s) |
|---|---|---|
| I-II.Q1-Q9 | Man's last end through Goodness/Malice of the will | (the 308-day series enters I-II at Q10 on Day 66; these may be a deliberate later treatment OR a series-design skip — needs source confirmation) |
| I-II.Q20-Q29 | Goodness/Malice of external acts through Love (passions) | Days 71-75 (missing — see Priority 1) |

---

## Priority 3 — Parts not yet started

| Part | Articles done | Total | % |
|---|---|---|---|
| Secunda Secundae (II-II) | 0 | 908 | 0.0% |
| Tertia Pars (III) | 0 | 540 | 0.0% |

These represent **1,448 articles** of pending work and are the bulk of the remaining 308-day series.

---

## Resolving a gap

When a missing transcript becomes available:

1. Drop the transcript into the Summa-2026 project at the appropriate `Day-NNN - Title.md` path.
2. Re-run the sync job (`sync_vault.sh` runs daily at 21:00 via launchd; manual run also fine).
3. Re-run the curriculum-generation pipeline so `summary` and `available: true` are populated for the affected articles.
4. Re-run this audit (`python3 wiki/vault/refs/missing_days_audit.py`, if scripted) or regenerate this file.
5. The "last continuous day with no gaps below it" should advance.

---

## Open questions for source confirmation

- ~~**Day 1**: does it exist as a recorded lecture?~~ **Resolved 2026-05-12:** Day 1 is the Introduction lecture, present on disk. It just isn't keyed in `summa_index.json` because that index is article-scoped.
- **Days 62-65**: 4-day stretch. Are those four lectures of wrap-up content that haven't been transcribed, or were those days skipped in the original series?
- **Days 71-75**: 5-day stretch covering I-II.Q20-Q29. Same question: recorded but un-transcribed, or genuinely absent from the source?
- **I-II.Q1-Q9 entry point**: was the choice to start I-II at Q10 (Day 66) editorial, or are Q1-Q9 covered earlier in the series under a different framing?

Each of these would either close a gap or let us replace "missing" with "intentionally not covered — see note."

## Architectural follow-up: `days_present.json`

Day 1's status surfaced a structural issue: an article-keyed index can't represent days that have content but no Summa article (intro, intermission, recap, retrospective, etc.). The progress pill in `explorer.html` currently hardcodes `INTRO_DAYS = [1]` as a workaround. The right fix is for the sync pipeline to emit a sibling file — e.g. `wiki/vault/refs/days_present.json` — that lists every `Day-NNN-*.md` actually on disk regardless of its content type. The pill should then read that file as the authoritative roster of present days, and use `summa_index.json` only to decide what kind of content each populated day carries. Until then, the hardcode is correct for Day 1 but will need updating any time another non-article day appears.
