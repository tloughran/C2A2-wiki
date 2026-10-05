# Metabolism

**family** chart · **tier** T1 · **manifest entry** yes, `metabolism` — the cleanest sweep, the thinnest model

## identity
`wiki/metabolism/metabolism_view.html`, 1,230,643 B, 407 lines (line 82 is the
1.2 MB `const DATA`), modified 2026-10-04 05:53. Explorer tab "Metabolism"
(`explorer.html:455`). **Generated** by
`wiki/metabolism/scripts/build_metabolism_view.py` ("emits metabolism_data.json
and metabolism_view.html, self-contained, data inlined"; the HTML template is in
that script, `<select id="view">` around `:619`). Regen via
`scripts/metabolism_monitor.py --regen-only`; publish via
`scripts/publish_metabolism.sh`.

## purpose
A time-series view of the agent swarm's daily activity, token flow and vault
output ("yield") since March 2026.

## data sources
**Baked.** `DATA` inline at `:82`; the sibling `metabolism_data.json` (1.82 MB)
is the same data and is used by the publisher's freshness check. No fetch, only
D3 scales and formats. Origin: `OpenStory/data/open-story.db` (read-only
snapshot), vault git history for yield (`compute_vault_yield`),
`architecture/metrics/prs_yield_detail.csv` (DECISION-058), the Level-2 signals
for `yield_signals` (`_meta.signal_source`: 1,611 records, latest 2026-09-23 —
so the metabolism page and the Community Interactions Level-2 embed share one
upstream), and `agent_map.json` for the schedule.

## entities and fields
- `DATA._meta`: `generated, source, db_mtime, lanes` (33), `total_runs` (4,308),
  `t_min, t_max` (newest session START), `t_max_event` (newest EVENT), `note,
  signal_source`.
- `lanes[]`: `key, label, category, thinkers, schedule, runs, out_total,
  all_total, median_gap_h, rows[]`.
- Run row: `sid, t, dur_min, events, in, out, cache_read, cache_creation, total,
  thinking_tokens, thinking_chars, thinking_blocks`.
- `yield_daily[]` (199 days from 2022-07-01): `date, links_added, links_removed,
  files_added, commits, prs_added, prs_articulated, signals, synthesis_essays,
  synthesis_words`.

## cut
Four controls — and the manifest's runtime sweep says they are **the tab's
entire interactive surface**, 4/4 covered, 0 uncovered. That is true and it is
also the problem.

| dim | kind | binding |
|---|---|---|
| view | set (raster \| wave \| dual) | `#view` (`:44-50`) |
| metric ("Amplitude") | set, 12 values | `#metric` (`:51-65`) |
| color | set (category \| cache_ratio) | `#color` (`:67-70`), raster only |
| logy | value, bool | `#logy` (`:73`), hidden in raster |

All four share one `change` listener calling `render()`; `resize` re-renders too.

**(a) Time is not in the cut, and cannot be added by declaration.** The x-axis is
hard-wired to the whole span: `dayAxis()` uses `t0 = floor(meta.t_min)`,
`t1 = ceil(meta.t_max_event || meta.t_max)`; raster uses the same domain. No date
control, no brush, no zoom anywhere. A time-series page whose cut excludes time.

**(b) The four dimensions are not independent.** `setControls(view)` runs on every
`render()` (`:296-316`):
- the five `yield_*` metrics are `disabled` unless `view === 'wave'`, and a
  selected one is **silently reset to `events`**;
- `color` shows only in raster; `logy` is hidden in raster; `metric` is hidden
  entirely in `dual`;
- `logy` is disabled and greyed for wave + a yield metric (those bars use a fixed
  linear scale).

The interlock is real and principled: the yield axes are commit-day bars from git
(a gap means "no commit that day", not zero) while run-side metrics are
per-session telemetry. They are different series on one page, not different
filters on one dataset. **So a cut here is a point in a small dependency graph,
not a tuple of independent assignments**, and §3's model cannot express it. The
runtime already copes — `execKnob` re-reads after writing precisely so the guide
never claims a clamped value (`explorer.html:5486-5490`) — but the manifest has no
`requires` and `_controls_note` does not mention the interlock. See main document
§4.4(b).

`items.kind: none`: a chart has no addressable items. Hover is a transient
tooltip, manifest-excluded.

## change signal
**The best existing implementation in the project.**
- Page-level, already emitted: `meta.t_max_event` and `meta.t_max` drive an
  in-page banner — "no OpenStory events for Nd — ingest is down, not the
  artifact; a regen cannot move the right edge" when event age > 1 day; a second
  warning when only session-start age > 1 day; a third when the snapshot predates
  `t_max_event` tracking (script block `:3-37`). **It distinguishes a dead
  pipeline from an old artifact and says so on the page.** Nothing else does.
- Cadence: daily regen 05:00 (`com.c2a2.metabolism-regen.plist`, no git), weekly
  publish Sun 06:30 (`com.c2a2.metabolism-publish.plist`) which refuses data
  older than 36 h, runs structural + data-sanity validation, commits only the two
  metabolism files and pushes. Latest `publish.log`: `PUSH OK` 2026-10-04 06:30,
  33 lanes, 4,308 runs.
- Subscribable grain: new daily buckets (`t_max_event` advancing); lane
  add/remove; `yield_daily` appends; a staleness verdict (monitor exit 3 =
  "ingest stale >48h").
- Caveat: `metabolism-monitor/findings.md` + `state.json` are Phase 0
  ("baseline then deltas"; deltas "begin at Phase 1") and last ran 2026-07-28.
  Stale for 2+ months, so not currently a live signal.

## export shape
- Wave: one row per day — `date, <selected metric>`; dual: `date, sent, returned`
  (sent = in + cache_read; returned = out, computed in-page).
- Raster: one row per run — `lane, category, sid, t, dur_min, events, in, out,
  cache_read, cache_creation, total, thinking_*`.
- Yield: one `yield_daily` record per row.
- JSON: `DATA`, or one lane record.

## narration
Shell blurb `explorer.html:1080-1083`; `voice_guide/knowledge/metabolism.default.md`
(2,664 B, 2026-08-28, `volatile: none`, sections on the 3 views and the yield
axis); the in-page `<div class="note">` on yield. Current values are not
narrated (no state bus). Per-metric explanation exists only as option labels.

## current capability
Contract: **none**, and it is not in `FIND_TABS`. No `c2a2Ask`, no export, no "?"
in page (shell entry only), no state bus. Manifest: 8 caps (go, back, set, undo,
redo, what, where, help; `reset`/`restore` deferred to "step 2b", reporting
`unsupported_here`), **4 knobs** — the only page where `set` does real work —
`items.kind: none`, no views, `controls_excluded: []`, no `controls_deferred`, no
`dim_coverage`, one gesture (hover, excluded).

## what resisted description
- Raster rendering (`:48-150`) not read in full; lane ordering and mark sizing
  per metric unverified.
- `METABOLISM_MONITOR_AGENT_SPEC.md` is a 2026-06-19 draft and the monitor is
  Phase 0; the spec's phases were not reconciled with what runs.
- `publish_metabolism.sh` references the validator at
  `wiki/c2a2-wiki-narration/scripts/validate_html.py`; that path was not checked.
- The missing time window is amorphous only in that it does not exist — there is
  no control to declare. Adding one would have to interact with `dual` (a days
  list), raster (lane dots) and yield (sparse commit days), none of which expose
  a range.
