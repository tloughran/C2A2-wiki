# SPEC — log time axis + dynamic depth for the Narrative (PRS) Connectome

*Drafted 2026-08-27 in Cowork, at Tom's direction. **Status: PROPOSED, not ratified, not implemented.***
*Evaluated against `wiki/architecture/narrative_prs_connectome.md` (architecturally guiding).*
*Origin: the 2026-08-27 finding that the vertical axis has degenerated — see `project_C2A2_prs_pipeline_stall_2026-08-27` in project memory.*

---

## 1. The defect this answers

`wiki/prs_3d.html` sets node height from a **year**: `yearToZ()` maps 1977–2026 linearly onto z 2→38.

Measured on the live 642-triplet build:

| | |
|---|---|
| triplets with `pub_year == 2026` | **550 of 642 (86%)** — all at z = 38.0 |
| distinct z levels for 642 nodes | **25** |
| next-largest level | 23 nodes |
| triplets in a `(thinker, year)` bucket > 30 | 428 of 642 |
| largest bucket | levin/2026 = 77 |

The axis is asymptotically becoming a constant, because essentially every agent ingest is a 2026 source. This is the same family as the collapse fixed 2026-05-20 (`decisions.md` line 678 — position keyed on `(thinker, year)` put 269 triplets on 47 stacks, 222 hidden). That fix de-overlapped *within* a bucket; it did not stop the buckets themselves from saturating.

**Consequence for the user:** the count rises and the picture does not change. Growth is added to an already-saturated top plane.

## 2. Granularity first, scale second

**A log scale on a year-resolution field cannot separate 550 items that share a year.** Any transform of `pub_year` maps 2026 to one number. So the axis needs finer input *before* it needs a different curve. Three tiers, measured:

| z source | granularity | largest single level | note |
|---|---|---|---|
| `pub_year` (today) | year | **550 (86%)** | current behaviour |
| `date` | day | **79 (12%)** | 58 distinct dates inside the 2026 pile |
| true `source_date` | day, genuine publication | not yet measured | lives in proposal frontmatter, not yet carried through |

`date` is already on every triplet (642/642, 90 distinct, range 1977-06-01 → 2026-08-10). It is a **mixed field**: `extract_prs_data.py:182` reads `(cf or {}).get("date") or date_added` — a hand-curated publication date where the carryforward map has one, the Date-Added otherwise. The residual 79-on-one-day clump is 2026-08-09, which is an *ingestion* date, not a publication event.

Good news for migration: `prs_pub_years.json` **already persists `{"date": ..., "pub_year": ...}` per id** (`extract_prs_data.py:366`), so the carryforward already round-trips a full date. No schema change is needed to move z from `pub_year` to `date`.

**Recommendation: switch z to `date` now (86% → 12% in one line), and open a separate, slower task to carry genuine `source_date` from proposal frontmatter into the triplet so the axis means publication time rather than capture time.** Do not conflate the two — the connectome model says this axis carries *when the narrative entered the world*, not *when we filed it*.

## 3. The log mapping

Log on **age**, not on year — a year has no meaningful logarithm; a time-before-now does.

```
age      = NOW - date                    (days)
u(age)   = ln(1 + age/tau) / ln(1 + ageMax/tau)
z        = zTop - (zTop - zBot) * u
```

`tau` is a **time constant in days**, exposed as a slider:

- `tau -> infinity` recovers the present linear behaviour exactly (useful as the control).
- `tau` small strongly expands the recent end.
- Sensible default: `tau ~ 90` days — roughly the window in which the current corpus actually lives.

Recent narratives, where the coils are actively forming, get vertical room to separate; deep history compresses into a base layer. This is defensible in the connectome model's own terms: it makes association fibres between *recent* modules legible, which is the wiring we are currently unable to see.

Use the `ln(1 + age/tau)` form rather than a bare `log`: it is finite at age 0, monotonic, and has linear as a clean limit rather than a special case.

## 4. The dynamism — "pull the scale down"

A **time window** with two handles `[a0, a1]` over age, renormalised so the window fills the whole column:

```
u = (ln(1+age/tau) - ln(1+a0/tau)) / (ln(1+a1/tau) - ln(1+a0/tau))     clamped to [0,1]
```

- Pull the handles to the last 90 days and those triplets spread over the full 40-unit height.
- Nodes outside the window **dim, they do not vanish** — consistent with the standing Sociogram ruling that search is a transient highlight lens, not a filter (`project_C2A2_sociogram_search_vs_filter`). Same principle: exploring a sub-range must not silently change the denominator.
- The existing `Showing n / 642` counter keeps reporting the full corpus; add a second readout for the window (`window: 2026-05-01 → 2026-08-10`).

Two controls total: `tau` (curvature) and the window (range). Resist adding more.

## 5. Interaction with the deterministic fan — read before writing

`buildPRSNodes()` fans each `(thinker, year)` group over a `ceil(sqrt(n))` grid **because those triplets share an exact point**. Day-resolution z largely dissolves that premise. Do **not** delete the fan on that assumption:

- Re-key the fan on the **rendered z bucket** rather than the year, so it still catches genuine ties (79 triplets really do share 2026-08-09).
- The fan is deterministic and reproducible across regens by design. Preserve that: index off `PRS_TRIPLETS` order, no randomness.

Also unresolved: **which of `yearToZ` / `dateToZ` `buildPRSNodes` actually calls** — the source read was truncated on 2026-08-27. Both are year-derived and both collapse, so the diagnosis holds either way, but confirm before editing.

## 6. Success criteria + falsifier

Ship a metric, a target, and a control.

- **Metric:** `max_share` = largest fraction of nodes landing on a single rendered z level (round z to render precision before bucketing).
- **Control (must run first):** the metric on the **current** build must report **0.86**. If it does not, the metric is wrong and nothing downstream is trustworthy.
- **Target:** `max_share < 0.10` at default `tau`, with z sourced from `date`.
- **Secondary:** distinct z levels >= 200 of 642 (today: 25).
- **Regression:** at `tau -> infinity` and full window, node positions must match the current build within float tolerance — proves the new path is a superset of the old.

**Make `max_share` a standing check.** This failure was silent and progressive: no freshness gate catches an axis whose input distribution has drifted. It belongs with the janitor / metabolism hygiene run, alongside the same lesson from the Level-2 signals axis reading a flat, honest-looking zero for six weeks.

## 7. Scope discipline

In: z source `pub_year -> date`; the `tau` mapping; the window control; re-keying the fan; the metric + control + standing check.

Out (separate tasks, do not fold in): carrying genuine `source_date` through the extractor; any change to the radial/discipline layout; the tab rename; `wiki/prs_3d_debug.html` (133 triplets, frozen 2026-05-04, **tracked in git and live on origin/main** — untrack it, but as its own decision).

Generator reminders that will bite: the generator is **template-injection and NOT idempotent** — always run against `template_prs_3d.html`, never an already-generated file. Always pass `--carryforward` or ~230 curated pub-years are lost.

---

## MEASURED 2026-08-27 — the control is 0.905, not 0.86, and the migration story above is wrong

Falsifier now implemented: `scripts/prs_axis_max_share.py`, run against the baked
`wiki/prs_3d.html` (642 nodes). Everything below is measured, not asserted.

| z source | max_share | distinct levels | largest level |
|---|---|---|---|
| **rendered (what viewers see today)** | **90.5%** | 23 | z 38.000 = 581 nodes |
| `pub_year` (what this spec measured) | 85.7% | 25 | z 38.000 = 550 nodes |
| `date` at **day** precision | **12.5%** | 83 | z 37.998 = 80 nodes |

### Three corrections

**1. The UNVERIFIED item resolves against this spec.** `buildPRSNodes()` calls
`dateToZ(triplet.date)` (template line 685), not `yearToZ(pub_year)`. So z is
*already* sourced from `date`. But `dateToZ` does `parseInt(dateStr.slice(0,4))`
and hands the year to `yearToZ` — it throws the granularity away immediately.
Worse, `yearToZ` normalises against `minYear`/`maxYear` computed from **`pub_year`**
(`allYears = PRS_TRIPLETS.map(t => t.pub_year || 2020)`). The live axis is a hybrid:
**value from `date`'s year, scale from `pub_year`'s range.** Nobody described it that
way, including this spec.

**2. "Granularity first: `pub_year` -> `date`" is not the fix — it is already the
state, and as a *field* swap it makes things worse.** `date`-year puts 581 nodes on
one plane against `pub_year`'s 550 (90.5% vs 85.7%). The 12.5% figure only appears at
**day** precision. The edit is therefore not "change the source field" but **"stop
truncating the date to its year inside `dateToZ`"** — a different and smaller change
than this spec proposed, in a different function.

**3. The control was measured on the wrong field.** 0.86 is `pub_year`, which the
renderer does not use for placement. **The regression control is 0.905** (rendered).
Any `tau -> infinity` regression test must reproduce *that*.

### And granularity alone does not reach the target

Day precision gives 12.5%, against this spec's own `max_share < 0.10`. It misses by
2.5 points. So the log-on-age transform with the `tau` slider is **not** optional
polish on top of a fix that already works — it is load-bearing for hitting the target.
The residual pile is real: 80 nodes share a single ingestion day (the 2026-08-09
clump), and no monotonic transform of a date separates nodes that carry the same date.
Only a genuine `source_date` would, and:

**`source_date` is present on 0 of 642 nodes.** Not sparse — absent. This spec listed
it as "unmeasured; lives in proposal frontmatter, not yet carried through." It is now
measured, and carrying it is an ingest-pipeline change, not a config flip.

### Standing check

`python3 scripts/prs_axis_max_share.py [path] [--json]`. Run it on every PRS regen.
Bucketing rounds z to 3 decimals (two nodes agreeing to that are coplanar on screen).
It reads the built artifact, not a source file, for the same reason the Level-2 guards
parse the built HTML: the number that matters is the one a viewer actually gets.
