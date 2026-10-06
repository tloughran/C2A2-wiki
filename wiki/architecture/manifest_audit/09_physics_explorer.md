# Physics Explorer

**family** reader (with a chart sub-view) · **manifest entry** NONE (knowledge file only)

## identity
`wiki/physics_explorer.html`, 220,030 B, 2,628 lines. Explorer tab "Physics
Explorer" (`explorer.html:469`). **Hand-authored**; the only generated-looking
part is the inlined `c2a2-search` module (`:717`). Commits `cfa5a756` (48 demos,
KaTeX, Progress-to-PRS), `3136f413`, `1fba4b78`. Superseded candidates sit
untracked at repo root: `physics_explorer_candidate_2026-04-02.html` (185,548 B,
"75 concepts / 6 physicists / PRS") and `_2026-05-01.html` (254,632 B, "48
concepts"); neither is referenced anywhere (not diffed).

## purpose
A teachable undergraduate physics concept library with a historical
problem-resource-solution layer over six physicists and a Kuhnian progress chart,
to show that the PRS lens works on a curriculum.

## data sources
All inlined JS literals, no fetch except the broker.
- `physicists = [...]` (`:1275`): 6 — Newton, Maxwell, Boltzmann, Einstein,
  Feynman, Wolfram.
- `kuhnProgress` (~`:1450`): 7 stages.
- `concepts` in `renderAllConcepts()` (`:1681`): 75.
- `INSTRUCTOR_DEMOS` (`:1679`): 47 concept keys, 48 demos (so one concept has two).
- `addSimulations()` (`:2414`): canvases `shm-canvas`, `wave-canvas`, `rc-canvas`.
- Topic list in `buildConceptsTOC()` (`:1221`): 6 areas.
- KaTeX from jsdelivr (`:8-9`); the broker at `:753` for "Ask AI"
  (`#chat-ai-mode`, `:691`).
Badges on the page say 75 / 6 / 6 (`:634-636`).

## entities and fields
- **Concept**: `id, topic, title, equations, body, cds{c,d,s}, phet, objectives,
  misconceptions`.
- **Physicist**: `name, role, color, summary(html), cds[{c,d,s}],
  prs[{label,p,r,s}], solvedCount, newAnomalies[]`.
- **Kuhn stage**: `label, year, solved, cumulative, color, problems` (cumulative
  solved = 46).
- **Demo**: `title, html, equipment`.

## cut
Mixed filter and address.

| dim | kind | binding |
|---|---|---|
| mode | value (student \| instructor) | `setMode()` (`:898`), `.mode-btn`; toggles `.instructor-only.visible`; state `currentMode` (`:892`) |
| sidebar view | value (concepts \| physicists \| progress) | `setSidebarView()` (`:926`), `.sidebar-tab` |
| concept filter | value, string | `#concept-search` → `filterConcepts()` (`:1033`), over 75 titles |
| physicist | value, 6 | `showPhysicist(idx)` (`:1519`), `.physicist-tab` / `.physicist-card.active`, var `currentPhysicist` |
| chat mode | value | `setChatMode()` (`:916`), `.chat-mode-btn`, var `currentChatMode` |
| concept | address/action | `scrollToSection(anchorId)` (`:1041`), `jumpToConceptFor(c,d,s)` (`:989`), resolvers `exactCardFor` / `bestConceptFor` (`:946-977`) |
| progress stage | action | canvas click `_progressBarHit` (`:1634`) → `progressToPRS(idx)` (`:1648`), with return buttons (`_cdsReturnIdx`, `:988`) |
| search | value | `#chat-input` → `doQuery()` (`:1122`), `retrieveContext(query,n)` (`:1083`), keyword term-count |

Concept ids are stable slugs (`newtons-laws`, `simple-harmonic`) and exist as DOM
ids (`:2416`), but **`location.hash` is never written** — the same gap as RC
Document Explorer. Sidebar view and physicist index are volatile UI state.

Not declared anywhere and probably should be: `addSimulations()` creates numeric
slider knobs in the DOM (`shm-amp`, `shm-freq`, …). On a page with a manifest
these would be a `controls_deferred` entry at minimum; today they are invisible
to the coverage sweep because the page is not swept.

## change signal
Per concept `id` (added, or its `cds` triplet or `INSTRUCTOR_DEMOS` entry
changed) and per physicist (a new `prs` item, a changed `solvedCount`). It is a
curated curriculum that changes by whole-corpus expansion — the 48-concept and
75-concept candidates are the evidence — so `grain: regen` is honest and a
per-concept diff is a bonus (inferred).

## export shape
- CSV, concept grain: `id, topic, title, equations, objectives, misconceptions,
  cds_c, cds_d, cds_s, phet`.
- JSON: the concept object plus `demos:[{title, equipment}]`.
- Physicist: `{name, role, solvedCount, prs:[{label,p,r,s}], cds, newAnomalies}`.
- Progress: a `kuhnProgress` row.

## narration
`voice_guide/knowledge/physics_explorer.default.md` (purpose, contents,
affordances, answerable questions; `volatile: none`, "NO state bus"), mapped at
`explorer.html:6164`. Shell `descriptions` entry at `explorer.html:1064`.

## current capability
Contract: **none** — `FIND_TABS` expects it with needle `newton`
(`test_voice_shell.cjs:2494`) → red. No `c2a2Ask`, no export, no in-page "?", no
state bus, **no manifest entry**.

## what resisted description
- The diff against the two older candidates was not examined.
- The simulation sliders' full id set and ranges were not enumerated.
- The 47-key / 48-demo discrepancy is explained (one concept has two demos) but
  was not confirmed against the data.
- Nothing amorphous.
