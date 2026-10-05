# Curriculum Tools (Summa Explorer)

**family** reader · **tier** T1 · **manifest entry** yes, `curriculum_tools` — the most complete `items` spec in v1

## identity
`wiki/summa_explorer.html`, 50,634 B, 1,327 lines. Explorer tab "Curriculum
Tools" (`explorer.html:456`; key `curriculum_tools` at `:1934`).
**Hand-authored** — no generator names it; header says "Phase 1".
`scripts/regen_summa_sociogram.sh` does **not** build this page: it rebuilds
`wiki_narration.html` with `--summa` (`:3-4, 45-50`), which this page's Sociogram
sub-view iframes (`:451`, `:1274`, ~29 MB). `wiki/launch_summa.command` is a
4-line launcher that serves the repo and opens `explorer.html`, not this page.
`wiki/SUMMA_EXPLORER_IMPROVEMENTS.md` is a plan (Vault Linker Agent, Sociogram
tab), not current behaviour.

## purpose
A reader for the Summa Theologiae that lets you walk Part → Question → Article
and open each article's lecture transcript or its contemporary synthesis.

## data sources
- `./vault/refs/summa_index.json`, fetched at `:500` — 2,747 entries keyed
  `I.Q1.A1`, of which 2,656 `available`.
- Per-entry markdown under `./vault/transcripts/*.md` and `./vault/synthesis/*.md`
  (307 files each), fetched in `fetchContent` (`:1092-1105`). Note 307 files for
  2,656 articles: the `article.day` → file mapping is many-to-one (inferred).
- A synthetic `Day1` entry injected in JS (`:513-526`) because the index has no
  intro days.
- `marked@9.1.6` from CDN (`:463`). `vault/refs/missing_days.md` and
  `index_summary.md` are documentation only.

**Shared corpus**: `vault/synthesis/Day-NNN - … - Contemporary.md` is also read by
`summa_commentary.html` (307 days, door-reached) and baked as 267
`summa-day-NNN` satellites into TRV Commentary's 11 MB bundle. Three readers,
one corpus, three addresses. See main document §7.2(b).

## entities and fields
- Index entry: `part, part_code, question, question_title, article, title, day,
  transcript, synthesis, latin, english, available`.
- `PART_ORDER` = I, I-II, II-II, III, Suppl (`:466`).
- Hierarchy: 5 parts, ~611 questions, 2,747 articles (spec §R).

## cut
A reader's cut — part address, part toggles. The roster **lives behind a click**,
which is what `voice_guide_redesign.md` §R (`:1095`) was written about.

| dim | kind | binding |
|---|---|---|
| articles | value, bool | `#show-articles` (`:389`) — with it off, a question click jumps to its first article instead of expanding (`onClickQuestion`, `:981`) |
| mode | value, 2-way | `#btn-transcript` / `#btn-synthesis` (`:437-438`) → `switchMode` (`:1076`), state `currentMode`, class `.on` |
| view | set, 2-way | `#subtab-contents` / `#subtab-sociogram` (`:384-385`) → `switchLeftTab` (`:1191`) |
| tree state | set | `partOpen` (`:476`), `qOpen`; `togglePart` (`:961`), `collapseAll()` |
| selection (address) | value | `.a-row.avail` click → `loadArticle` (`:1027`); selected `.a-row.sel`; body `#md-body`; close `#btn-back-index` |

Rows are built eagerly and hidden, so the manifest uses **one flat roster of
visible rows** rather than three level-scoped rosters. Its `_note` gives the
reason, and it is the best piece of reasoning in v1: *"nothing on this page says
which LEVEL a user is walking — there is no such state to read, because a sighted
user is not at a level either, they are looking at an open tree."*

**The manifest already invented `requires`**, locally and under another name:
`requires_knob: {id: 'articles', v: 'on', why: "with it off, a question click
jumps to an article instead of expanding, so `open` would have two meanings"}`.
That is the same relation Metabolism needs (main document §4.4b) — invented once
for one page instead of being a schema field.

The **address** is `I.Q1.A1`, stable and unique, and exists **in the data only**:
the page writes no `location.hash`, so the address is real and unlinkable.
`total` is deliberately undeclared because `#stats-line` counts articles while
the roster counts rows.

## change signal
A new or newly-available article, grain = one `Part.Q.A` ref: `available` going
false→true, or a new `transcript`/`synthesis` path in `summa_index.json`. Day
grain is coarser. Nothing is emitted; there is no stamp.

## export shape
CSV: `ref, part, question, question_title, article, title, day, has_transcript,
has_synthesis, available`. JSON: the index entry plus `ref`, optionally with the
open article's markdown body.

## narration
`voice_guide/knowledge/curriculum_tools.default.md`, mapped at
`explorer.html:6162`; spec §R is written. No in-page "?" popovers.

**The shell blurb describes a different page.** `explorer.html:1049-1050` says
"curriculum dashboard … tracks daily synthesis progress … Austin Habash's Summa
2026 podcast", and `:1058` mentions a 471-page tome. The 471-page tome is
`rc_document_explorer.html`. This page is a Summa article reader with no progress
or coverage-gap display. **A wrong explainer is worse than a missing one, and the
single manifest is what makes this class of error impossible.**

## current capability
Contract: **none** (0 `c2a2` hits in the file), and not in `FIND_TABS`. No
`c2a2Ask`, no export, no in-page "?", no state bus. Manifest: 14 caps, knobs
`articles` + `mode`, views `contents` + `sociogram`, a full `items` spec with
`activate / selected / reads / close / requires_knob / read_variants`,
`controls_excluded`, 2 `controls_deferred` (incl. speaking the availability line,
"curriculum tools increment 2"), gestures, **`dim_coverage` empty**.

Note `voice_guide_redesign.md` §Q (`:1047`) — "when a sub-view and a tab share a
name" — exists because this page's `sociogram` sub-view collides with the
`sociogram` tab. The sub-view wins. That collision is a key-namespace bug, and
it is the same bug the six-table problem produces at the file level.

## what resisted description
- `#stats-line`'s rendering was not inspected beyond what the manifest says.
- Per-entry `latin` / `english` usage not determined (null in the sample read).
- Nothing amorphous. The page is a clean tree reader whose only real gap is that
  its stable address is not written to the URL.
