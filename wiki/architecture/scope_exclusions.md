# Scope exclusions

Projects that appear in this vault's historical record but are NOT part of C2A2.
Their entries stand as history. They are out of scope going forward, and should not be
treated as C2A2 work items, carried forward into planning, or surfaced in the Explorer.

## KSGA-sociogram (Keough School faculty sociogram)

- Separate repository, separate project. Recorded here 2026-08-05 by Tom.
- **Historical references remain and should stay.** They are in `assumptions.md` (ASSUMPTION-217),
  `decisions.md` (DECISION-045), `for_lit_search.md`, and the dated changelog / cowork-summary /
  metrics records for May 2026.
- **Do not delete them.** 14a measures `assumptions.md` against five dated backups and restores any
  block that goes missing. It did exactly that on 2026-08-05 and logged the event as
  ASSUMPTION-764: *"block restored verbatim; recorded rather than silently repaired."* The
  gitignored `.bak` files are the evidence base it heals from, so deletion cannot win, and a
  rewritten or tombstoned entry would trip the same check. Annotate additively instead — this file
  is that annotation.
- PRESUMPTION-236 is KSGA-derived but never names KSGA. Left in place; it is cited by
  `monitor_queue.md`, `for_lit_search.md`, and two bootstrap backlink censuses.
- **Front-of-house pages and the pathway files carry no KSGA references**, and nothing there heals
  itself. That is where a reader actually is, and it is the boundary worth keeping clean.
- `wiki_narration.html` is generated and still contains KSGA text. Never hand-edit it — the content
  sits in an embedded JSON blob on one line. It clears on the next `regen_sociogram.sh --summa`.
