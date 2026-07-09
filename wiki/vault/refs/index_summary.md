---
generated: 2026-07-09
---

# Summa Index — Summary

## Coverage

- **Total articles indexed:** 2,747
- **Articles with vault content:** 2656  (96.7%)
- **Articles pending:** 91

## Breakdown by Part

| Part | Full name | Questions | Articles | Available |
|---|---|---:|---:|---:|
| `I` | Prima Pars | 119 | 584 | 572 |
| `I-II` | Prima Secundae | 114 | 616 | 616 |
| `II-II` | Secunda Secundae | 189 | 908 | 898 |
| `III` | Tertia Pars | 90 | 540 | 472 |
| `Suppl` | Supplementum | 99 | 99 | 98 |

## Notes

- Article titles are `null` in this release (newadvent.org is not on the network allowlist).
  Run `build_index.py --fetch-titles` once the allowlist is updated.
- The Supplement (Supplementum Tertiae Partis, Q.1-99) IS included at
  question-level granularity (one article row per question); exact Leonine
  per-question article counts are a future refinement. Titles from NewAdvent summa/5.htm.
- Overlapping question ranges in Days.md (Q58, Q69, Q70, Q72) are resolved by
  assigning each question to its first-appearing day.

## Key Format Comparison: Major Digital Editions

| Edition | Format | Example |
|---|---|---|
| **This project** | `I.Q1.A1` | `I-II.Q90.A1` |
| NewAdvent | URL path: `summa/1001.htm` (PPQAAA) | `1001.htm` = PP Q1 A1 |
| Corpus Thomisticum | `Ia q.1 a.1` / `Ia-IIae q.1 a.1` | Latin abbreviation |
| CATENA / Aquinas Institute | `ST.I.Q1.A1` | `ST.I-II.Q90.A1` |
| Documenta Catholica Omnia | Folder `I/1/1` | numeric hierarchy |
| GitHub: sed-ml/summa-theologica | JSON path `parts[0].treatises[0].questions[0].articles[0]` | array indices |

**Recommendation for cross-reference alignment:** The Aquinas Institute / CATENA
format `ST.I.Q1.A1` is most widely used in academic cross-referencing tools and
TEI/XML exports. To align with that standard, prefix keys with `ST.` when exporting
edge data for the graph. Internally, the short form `I.Q1.A1` is used here for
readability and to match the vault's `pars/q/` tag convention.