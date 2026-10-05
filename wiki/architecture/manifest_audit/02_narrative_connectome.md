# Narrative Connectome

**family** graph (data-backed, no DOM roster) · **tier** T1 · **manifest entry** yes, `prs_3d`

## identity
`wiki/prs_3d.html`, 1,226,637 B. Explorer tab "Narrative Connectome"
(`explorer.html:453`; voice words at `:1931`). **Generated**:
`scripts/regen_prs_connectome.sh:35-37` runs
`c2a2-prs-3d/scripts/extract_prs_data.py`, then `generate_prs_3d.py` against
`c2a2-prs-3d/template_prs_3d.html`, then `validate_prs_3d.py`, and copies to
`wiki/prs_3d.html` only after validation. `publish_prs_connectome.sh` is the git
step. **The generator is not idempotent and must never be run against the built
page** (`assumptions.md:3409`, `SPEC_prs_time_axis_2026-08-27.md:104`).

## purpose
A rotating three.js scene in which each thinker's problem-resource-solution
narrative is a vertically time-positioned node cluster, joined by threads,
cross-tradition coils and generative chains, so the reader can see how the
narratives knit across traditions and disciplines.

## data sources
All inlined by the generator as JS vars in the template, no fetch. Template line
numbers: `PRS_TRIPLETS` (`:444`), `CROSS_CONNECTIONS` (`:445`), `FINDINGS`
(`:446`), plus `COILS`, `GENERATIVE`, `DISCIPLINES`, `THINKER_DISC`,
`THINKER_COLORS`, `THINKER_DISPLAY`, `PRS_BUILD_TS`, `TAU_DAYS`. Upstream:
`extract_prs_data.py` over the vault's PRS blocks, and
`c2a2-prs-3d/prs_pub_years.json`, the curated `{date, pub_year}` carryforward
(`regen_prs_connectome.sh:28`). three.js r128 from CDN (`:437`).

## entities and fields
- **Triplet** (962 unique in the live file): `id` (`<thinker>-PRS-NN`),
  `thinker`, `prs_num`, `label`, `problem`, `resource`, `solution`, `date`,
  `pub_year`, `confidence`, `first_seen`. Drawn as 3 meshes sharing one triplet
  id, joined by a thread.
- **Coil** (33): `cross_id, id, label, nature, notes, program_count, programs, year`.
- **Generative chain** (24): `score, shared, source, target, thinker_source, thinker_target`.
- **Cross-connection** (103): `id, question, programs, notes, nature, year`.
- **Finding** (79): `id, date, finding, programs, type`.

## cut
Expressible; the manifest does it by checkbox id.

| dim | kind | binding |
|---|---|---|
| traditions | set | `prsFilterState`, `#prs-chk-{k}`, master `#prs-chk-all` |
| disciplines | set | `prsDiscState`, `#prs-chk-disc-{slug}`, `#prs-chk-all-discs` |
| years (decades) | set | `prsYearState`, `#prs-chk-year-{k}`, `#prs-chk-all-years` |
| edges / coils / generative | 3 bools | `#prs-chk-edges`, `#prs-chk-coils`, `#prs-chk-generative` |
| selection | value | `selectedMesh.userData.triplet.id` |
| camera | value | `cameraTheta`, `cameraPhi`, `cameraRadius` (15-120), `cameraTarget`; `updateCameraPosition`, `resetCamera`, `autoOrbit` |
| search | value | `#prs-search-box` — **dims meshes only, records nothing** |
| labels | toggle | `#btn-labels` |

Read: `prsNodeVisible()` / `applyPRSFilters()` (`:949-985`) compose tradition ∧
discipline ∧ decade; count in `#prs-count` via `updatePrsCount` (`:987`). The
readable cut is the `m.visible` flag per mesh. Continuous and excluded:
`#prs-brightness`, `#prs-year-slider`, `#prs-month-slider`.

**This is the page voice_guide_redesign.md §T was written about** — "THE FIRST
TAB WITH NO ELEMENTS TO WALK" (`manifests.json` `_caps_note`; §T at `:1317`,
"A roster with no elements"). One `<div id="canvas-container">`, WebGL meshes, no
per-node DOM. Consequences, all of which generalise to any future canvas page:
nothing can be cut by scraping DOM or opacities; the cut must be read through
declared dotted paths (`meshes`, `userData.triplet.id`, `visible`,
`prsFilterState`); writes must go through the checkboxes so the page's own
handlers run. §T declares `find` / highlight **deliberately NOT declared**.
§U (`:1439`) added the camera as a third axis.

## change signal
Per triplet by `id` (inferred): a new `<thinker>-PRS-NN`, a changed `date`,
`pub_year` or `confidence`, or a new coil / chain / cross-connection.
`regen_prs_connectome.sh` already counts ids old→new but only as a total printed
to stdout. `prs_pub_years.json` is the persistent per-id record and the natural
diff base. The 2026-08-27 pipeline stall (SPEC §1) shows "count unchanged since
last regen" is itself a signal worth having.

## export shape
None exists. CSV, triplet grain: `id, thinker, prs_num, label, problem, resource,
solution, date, pub_year, confidence, first_seen` (+ discipline from
`THINKER_DISC`). Coils, chains and cross-connections are separate tables. JSON:
a direct dump of `PRS_TRIPLETS` filtered by `m.visible` — i.e. the description
*is* the export query on this page, exactly as the hypothesis predicts, once
something can read the cut.

## narration
`wiki/architecture/narrative_prs_connectome.md` (70 lines) states what the view
is for; `voice_guide/knowledge/narrative_connectome.default.md` is the guide's
grounding; the page has a "How filters work" help panel (`:396`) and a "What is
this view?" pop-up. No TTS or tour narration in the page. A per-view spoken
description would need writing.

## current capability
- Contract: **none**. The only `window.` hook is `window.c2a2PlotSource`
  (`:1618`), data-only, and its own declaration says `cuts: false`.
- `c2a2Ask`: none. Export: none.
- "?" : `#prs-help-btn` / `#prs-help-popover` and a `.prs-pop-btn`, both
  manifest-excluded as chrome; plus a shell `descriptions` entry.
- Manifest: 29 caps (show/hide/only/all/none, set, fit, zoom, pan, rotate, spin,
  plot — **but not find, clear or read-the-cut**), 3 bool knobs, `items.kind:
  data` with `source: meshes` / `where userData.type: prs` / `activate
  prsSearchClickResult` / `total` as a regex on `#prs-count`, 3 filter sections,
  a `camera` block (orbit / dolly / pan / `autoOrbit`), 4 `dim_coverage`, 3
  `controls_deferred` (search box + clear + reset → "connectome increment 2";
  `#btn-labels` needs a `toggle` bind kind; `#prs-left-page .close-btn`), 4
  `controls_excluded`, 5 gestures covered / 1 deferred / 1 excluded.

## what resisted description
1. **Four documents give four triplet counts.** Live file 962; `manifests.json`
   507; `voice_guide_redesign.md` §T 453; `SPEC_prs_time_axis_2026-08-27.md` 642.
   Four different dates, no page-visible build stamp. This is the single clearest
   argument for a `data.counts[].source` field.
2. **Search is genuinely unrecorded as state** — `prsSearch` (`:1108-1126`) fades
   `material.opacity` and keeps no query and no hit list. Not amorphous; the
   manifest names it "increment 2". Until a hook records it there is no cut to
   read, which is why `FIND_TABS` holds this row red.
3. Edges (threads, coils, chains) have no addressable ids.
4. The vertical axis is mid-redesign (SPEC proposes log-age z, status PROPOSED),
   and `date` vs `pub_year` are mixed (SPEC §2), so any export of position must
   state which field it used.
5. `generate_prs_3d.py` and `validate_prs_3d.py` bodies not read.
