# Nested sub-surfaces

Five documents that are real, reachable, stateful surfaces but live *inside*
another page. None has a manifest entry of its own. Only one of the five is even
acknowledged by the existing manifest (the Community Cards iframe, declared as a
`frames` entry on `community_explorer`).

**Why they belong in the manifest.** Each has its own entities, its own controls
and its own change profile. A layer that consumes "pages" and does not see these
will be wrong about four of them, and one of them — the Level-2 Signal Stream —
is the best layer-2 candidate in the project.

---

## 1. Community Cards directory — **the only working export in the project**
`wiki/community/index.html`, 13.5 KB + `community/data.js` (2.3 MB, 1,006
records). Nested in `community_explorer.html:148` as an iframe with a lazy
`data-src`, shown by the `#tab-cards` sub-tab. Generated data:
`scripts/generate_community_cards_data.py` (855 bulk records from
`data.base.json` + the 156 curated, curated replacing bulk duplicates = 1,006).

**family** table. **Purpose**: the wide door — every community found, each an
inferred *seed* until the community claims it and sharpens its own GPRS
(`architecture/explorer_tabs_complementarity.md`).

**Entities**: the 20-field card record listed in `12_community_explorer.md`.
Cards render as a type pill, an "inferred seed" badge, name, meta and a G/P/R/S
stack (`community-cards.js:106-123`).

**Cut**: roster `#cc-card-grid > button.cc-card`, rendering only the first 60
(`CARD_LIMIT`, `community-cards.js:31`) with the true total read from
`#cc-card-status`. Dimensions, **none of them declared**: `#search-input`,
`#country-select`, `#subtype-select`, `#source-select`, `#sort-select`,
`#manual-only`, `#geo-only`, `#type-pills button.pill`, `#page-size`, the four
`.cc-tab` sub-views (cards | map | prs | overview), `#cc-prs-search`. Pagination
rides on `page` / `size` **URL params** (`app.js:260-261`), so part of this cut
is already linkable.

**Change signal**: new or changed `Community_ID`; a record's PRS statements being
claimed or sharpened — which is the promotion event across the quality membrane
into the graph. Grain: one community. No per-record timestamp exists.

**Export**: **already built and working** — `#download-csv` →
`c2a2_community_explorer_filtered.csv`, `#download-json` →
`c2a2_community_explorer_filtered.json`, both filtered by the live cut, plus
`#copy-share-link` (`app.js:1326-1332`; `index.html:235-237`). Leaflet map and an
Ask-AI path also present.

**Narration**: a shell `descriptions` entry keyed `community/index.html`
(`explorer.html:1040`) that **`showHelp` can never reach**, because it resolves
the community chapter to `community_explorer.html` first (`:1013-1025`)
(inferred). Knowledge file `community_cards.default.md` exists.

**Capability**: no `c2a2*`; its own search is `search-core.js` / `ai-query-core.js`.
Declared in the manifest only as a `frames` entry with excluded and deferred
controls — i.e. the project's one working export is declared as *something to
keep the voice guide away from*.

**Resisted**: nothing. **Judgement: this is the export layer's reference
implementation. Surface it, declare it, and copy it.**

---

## 2. Level-2 Signal Stream — **the best layer-2 candidate**
`wiki/level2_signal_stream.html`, 913,800 B, modified 2026-10-04 04:38. Nested as
`#l2-signal-embed` in `community_interactions.html` Level Two (~`:354`), cache-busted.
**Also read as data by the Metabolism pipeline** for its "cross-tradition
signals/day" axis (`scripts/regen_level2_signals.sh:7-10`), so it is upstream of
another tab.

**Generated** by `scripts/regen_level2_signals.sh`, which calls
`prototypes/extract_signals.py`, then `prototypes/backlog/build_manifest.py`,
`prototypes/harvest_signals.py` and `prototypes/build_prototype.py`
(`:12-17, 57-74`), writing a temp file and promoting only after guards pass
(`:119-124`). It also rebuilds `wiki/voice_guide/grounding.json` from
`signals_grown.json` (`:149-154`) — **so the voice layer already consumes this
page's data, through grounding, while the page itself is invisible to it.**

**family** graph (matrix) + table. **Purpose**: shows dated cross-tradition
"signals" — moments when one tradition's agent, reading another's material,
registered a connection — as a pair matrix, a cumulative timeline and a per-pair
detail list.

**Data**: inline `const SIG = [...]` (`:110`) and `const PAL` (`:111`). Upstream:
`pattern_detector_findings.md`, `cross_program_index.md`, `cross_signals`
batches, and each approved card's "## Cross-Tradition Signals" section. Baseline
`prototypes/level2_build_meta.json`: **1,611 signals, 87 pairs, 2026-04-03 to
2026-09-23**, by source card 1,370 / finding 147 / index 94 — matching the inline
data.

**Entities**: Signal — `a, b` (traditions), `date, strength, weight, nature,
source, sid, card, text, action, source_date`. Strength counts: **Unlabeled 938**,
Moderate 311, Strong 245, Speculative 83, High 34. `source` ∈ finding | index |
card.

**Cut**:

| dim | kind | binding |
|---|---|---|
| strength | value | `<select id="fStrength">` (`:64`) |
| source | value | `<select id="fSource">` (`:69`) |
| onlyCard | value, bool | `#fCard` (`:75`) |
| pair | value | click `rect.cell[data-a][data-b]` in `#matrix` (`drawMatrix`, `:127`), state `selPair`, showing `showPair` (`:190`) and `#selnote` |

Filters run through `filtered()` (`:115`) and one `change` handler redraws
(`:231`). The matrix is symmetric with inert diagonals, so a pair is unordered
(`a<b` key, ~`:138`).

**A real defect, found by attempting the entry**: `#fStrength` offers Moderate /
Strong / Speculative / High and **has no `Unlabeled` option**, while 938 of 1,611
signals (58%) carry that strength. They appear under "all" and cannot be selected
alone. **The cut literally cannot express the majority of the data.**

**Change signal**: new signals, grain per signal or per pair-day. This is the one
surface where subscription is the natural thing to want: the source count is
`signals` in `level2_build_meta.json`, the script carries `LAG_WARN_DAYS=21`
(`:40, 112-116`), the newest signal is 2026-09-23 (11 days stale at last build),
and the script's own header says a frozen artifact looks like a dead pipeline
(`:5-10`).

**Export**: CSV `a, b, date, strength, source, card, source_date, nature, action,
text` (+ `weight`, `sid`); JSON the raw `SIG` item; the matrix is derivable as
pair counts. Nothing exists.

**Narration**: in-page header ("Searchers Becoming Mutually Informed"), `.sub`,
panel notes, and a footer that distinguishes these dated signals from the
Narrative Connectome's static undated cross-edges — a genuinely useful
distinction that exists nowhere else. The Level Two row in the parent page
carries the What/Why/In-practice text.

**Capability**: no `c2a2*`, no export, no "?", no manifest entry. The footer
calls it a "prototype".

**Resisted**: `drawTimeline` and `#tllegend` (`:159-188`) not read in full, so
whether the legend is a control is unknown. How Metabolism reads the file was not
checked.

**Judgement: promote to a tool tab and make it the layer-2 pilot.** It is the
only surface with a dated, keyed, growing record set, an existing staleness
guard, a downstream consumer, and a parent page that misreports its size by a
factor of two.

---

## 3. Inter-Tradition Readout (DET interaction readout)
`wiki/intertradition-readout.html`, 40,834 B. Nested as `#l3-readout-embed` in
`community_interactions.html` Level Three (~`:372`). **Hand-authored static**, and
byte-identical to `hep-det/artifacts/intertradition-readout.html` — i.e. copied
from the HEP-DET artifacts directory (commits `cbb8599f`, `5450285a`).

**Purpose**: animates the first 18 DET (Pilot) steps in two acts — prepare a pair
of traditions, then read the interaction's outcome — so a visitor can step
through the dual-MMA logic.

**Data**: inline only. `OUT5` (5 outcome types with `def` and `diss`, `:272`),
`STEPS` (18, `:291`), `N = STEPS.length` (`:349`). Footer credits Loughran's
"Four Models of Cultural Exchange" (ISME 2022).

**Entities**: Step — `n, act, target, cap, t, d` (text), `a` (physics analogue).
Outcome — `key, name, short, def, diss` (e.g. intractable disagreement,
conversion). Two acts: 1-12 prepare the pair, 13-18 interact / reconcile /
classify / certify. Dual-MMA standards as pills A (step 1) and B (step 9) behind
an AND gate. A glossary (DET, C2A2, MMA, dual MMA, PRS, CCI, AT, FL/1FL, 2FL).

**Cut**: `act` (set, 2-way, `#tabs .tab[data-act]`, `:464-473`); `step` (value,
1-18 or none; state `cur`, `go(i)` `:526`, `next`/`prev` `:586-587`, buttons
`#next #prev #restart` `:194-197`); `playing` (value, bool; `#play`, timer,
`play/stop/toggle` `:588-590`); `speed` (value, 700-2600; `#speed` range);
`outcome` (action; a "?" opens `#poWin` via `openPopout` `:483`); glossary
`<details>`.

**The auto-play timer is a state that keeps running while a guide speaks**, which
is the hazard `voice_guide_redesign.md` §S flags (inferred). A manifest entry
would need `playback` as a declared dimension, not an action.

**Change / export**: an edit to `STEPS` or `OUT5`; grain one step or outcome;
rare (2 commits, none since 2026-06-30). CSV `n, act, caption, title,
description, physics_analogue`; JSON the `STEPS` item with `OUT5` as a second
table.

**Narration**: extensive in-page — `.lede`, per-step `d` and `a`, outcome
definitions, glossary. No knowledge file.

**Capability**: no `c2a2*`, no export, no manifest entry. **It does have per-outcome
"?" popups — the only in-page explainer in the project with a per-record grain**,
and therefore the precedent layer 3 should look at for anything finer than
per-page help.

---

## 4. Inter-Tradition Matrix (DET 40-step structure matrix)
`wiki/intertradition-matrix.html`, 24,335 B. Nested as `#l4-matrix-embed` in
`community_interactions.html` Level Four (~`:391`). **Hand-authored static**,
byte-identical to `hep-det/artifacts/intertradition-matrix.html` (commits
`cbb8599f`, `5450285a`, `dba6daff`).

**Purpose**: shows the Dialectical Engagement of Traditions algorithm's 40 steps
as a static matrix — each step's type, the mature-member action it calls for, and
how AI accelerates it.

**Data**: inline only — `AI` palette, `TYPE` tints, `ACT` (M/C/K), `MMACT` map,
array `S` of 45 cells, `BANDS` (~`:84-221`).

**Entities**: Step cell — `b` (band), `g` (step number), `sub, label, kind, mma`
(CONSTITUTE | CALIBRATE | DUAL-CERTIFY | …), `ai`/`aiL`, `ait`, `desc`, optional
`basis`. 4 bands: Pilot Stage 1 (1-10, BUILD), Pilot Stage 2 (11-20, READ), Run 1
Stage 1 (21-29, BUILD at scale), Run 1 Stage 2 (30-40, GROW) (`:215-220`). AI
modes: PROBE, PARALLEL, TUTOR, DRAFT, TOOL, INSTRUMENT. Mature-member actions:
model, collaborate, certify.

**Cut**: `band` (set, 4-way; `#tabs` built by `buildTabs` `:241-247`, state
`cur`); `step` (value; click `.cell[data-ix]` via `bindCell` `:302`, state `sel`,
showing `#card` via `showCard` `:310`). `#legend` is display only.

**The cut is by band only, while the data carries three more facets** —
`kind`, `mma`/mature-member action, and AI mode — all of them legend-worthy and
none filterable. For a page whose point is "which steps need a mature member and
which can AI accelerate", not being able to cut by those two fields is a real
limitation, and the kind the manifest exercise surfaces.

**Change / export**: a step added or edited in `S`; grain one step (`g`+`sub`);
static (3 commits in 2 days, none since). CSV `band, step, label, kind, mma,
mature_member_action, ai_mode, ai_text, description, basis`; JSON the `S` cell
plus derived `mmact`.

**Narration**: in-page `.thesis`, `.sub`, per-band `blurb`, `ACT`/`AI` tooltips,
per-step `desc` and `basis`. The Level Four row in the parent introduces it. No
knowledge file.

**Capability**: no `c2a2*`, no export, no "?", no `postMessage`, no manifest entry.

---

## 5. The Sociogram, re-iframed twice
`wiki/wiki_narration.html` is loaded three times under three routes:

| route | parent | preset | size |
|---|---|---|---|
| Sociogram tab | shell | none (default) | 63 MB |
| sociogram sub-view | `agents_tab.html:383, 1626-1631` | `#agents` | ~25 MB |
| sociogram sub-view | `summa_explorer.html:451, 1274` | `applySummaSociogramPreset` (`:1166`), structure group `summa`, applied on entry only | ~29 MB |

**Why it matters to the schema**: without `route.parent` and `route.preset`, the
manifest will say three contradictory things about one file — which is precisely
the mechanism that produced the six-table problem (main document finding 2). It
is also a straightforward performance finding: the same document is fetched and
parsed up to three times in one session.

Note that `voice_guide_redesign.md` §Q (`:1047`) exists because the Curriculum
Tools sub-view and the Sociogram tab **share a name**, and the resolution is that
the sub-view wins. That is a key-collision rule written in prose because the key
namespace is not declared anywhere.

**Resisted**: how the `#agents` preset filters nodes inside the 25 MB artifact was
not traced, on either parent.
