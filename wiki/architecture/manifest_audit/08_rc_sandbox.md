# RC Sandbox (Quodlibet Notebook)

**family** reader · **manifest entry** NONE · **`KNOWLEDGE` value is literally `null`** · **generator lost**

*This is the audit's headline page: it has the best-engineered cut in the
project, already serialised, already read back in prose, already written to the
URL — and it is the only live surface with no manifest entry, no knowledge file
and no regenerator.*

## identity
`wiki/rc_sandbox_notebook.html`, 1,783,288 B, 11,645 lines, title "Quodlibet
Notebook" (`:3`). Explorer tab "RC Sandbox" (`explorer.html:468`).
**Generated, generator GONE**: `handoffs/explorer-roadmap.md` ~L479 records it as
built by session-scratch `~/gen_html.py`, marked "GONE" at L845;
`gen_notebook.py` is only planned (L47). The committed page is now maintained by
idempotent patch scripts — `scripts/rc_sandbox_figures_patch.py` inserts figure
bios into the Figures index. The markdown source is regenerable via
`wiki/inbox/rc_sandbox/gen_sandbox.py`; there is no HTML generator on disk.
Predecessor copy `wiki/inbox/rc_sandbox/quodlibet_notebook.html` (1,670,644 B,
2026-09-05) is older and orphaned.

## purpose
A verbatim, read-only reordering of Tom's "TL sandbox" spreadsheet tab — 2,191
cells under a 36-node outline — with figure, discipline and voice indexes and a
revision-date timeline.

## data sources
Fully inlined. 2,191 `article.cell` (`#rNcM`) in `<main>`; rail outline
checkboxes `.rail input[data-cut]`; index sections at `:11127`
(`#index-figures`, `#index-disciplines`, `#index-voices`). Figure bios come from
`wiki/rc_sandbox_figures.json` (66,936 B; `_comment, generated, count, figures`),
verified by `scripts/rc_sandbox_figures_check.py` (which reads
`scripts/rc_sandbox_figures_draft.json` and `wiki/whos_who.json`, and writes the
json plus `scripts/rc_sandbox_figures_review.md`) and patched in by
`rc_sandbox_figures_patch.py`. Upstream, not read by the page:
`wiki/inbox/rc_sandbox/{assignments.csv, tl_sandbox_cells.json, cell_dates.json,
TL_sandbox_reordered.md}`. External: Google Fonts (`:4`). State:
`localStorage` key `qn`.

## entities and fields
- **Cell** `article.cell#r8c4`: `data-date`, `data-date-lo` (a sheet-history
  bracket; "live" = present in no saved copy), `data-tdate-raw` (an in-text
  date), `data-sec` / `data-div` (added at runtime, ~`:11449`), class `quoted`.
  Contents: `.gutter` (cid, "row N", "seq S · Ww"), `.meta .tag(.fig)`,
  `.voice`, `.txt`.
- **Node** `h3.node#i-1` (`.nid`, count line); **division** `div.division#i|ii|iii|z`;
  **row block** `section.rowblock#row-N` (created in By-row mode).
- **Figure** `div.idxrow#fig-slug` with `details.bio` — 203 figures, 63 with
  drafted bios.

## cut
**Strongly set-structured, fully expressible, and already implemented.** The
runtime reads the whole thing in `run()` (`:11508`).

| dim | kind | binding |
|---|---|---|
| section set | set, 36 nodes (leaves + divisions) | `.rail input[data-cut]`, `cutOf`, `leaves`, `on(id)`; change handler on `cuts` (~`:11555`), `syncDivs()`, `all`/`none` via `.cutbar a[data-all]` |
| text search | value | `#q`, 160 ms debounce `deb()`; plain substring over `id + textContent` lowercased (`cache`, `build()`) — matches cell ids and figure names, unranked |
| quoted only | value, bool | `#fq` `aria-pressed`, tests class `quoted` |
| by row | value, bool (layout) | `#fv` → `setRows()` (`:11503`), regroups the same elements into `#rows` |
| read-through | value, bool | `#fr` → `body.read`, hides furniture and drops empty sections |
| timeline bracket | action | `#tl a.br`, scrolls to the bracket's first visible cell and writes `history.replaceState("#"+id)` (`:11589`) |
| outline jump | action | `.rail .row a`, with a By-row redirect (`:11603`) |
| index peek | action | `openPeek()` (`:11609`), `#peek`, Esc closes |
| **read-out** | read | `#hits` ("N of 2,191") and `#scope`, both written by `run()` |

Three things already exist here that the five-layer plan intends to build:

1. **A serialised cut**: `localStorage.qn = {s, q, r, v, x:[unchecked leaf ids]}`
   (`:11545`). That is `c2a2ReadCut`/`c2a2WriteState` in all but name — and
   unlike the Sociogram's `c2a2ReadCut`, it covers the **filters**, not just the
   highlight.
2. **A prose read-out of the cut**: `#hits` + `#scope`. That is `describe_view`
   in all but name.
3. **A written address**: `#rNcM`, `#row-N`, `#<node>`, stable, unique, and
   pushed with `history.replaceState`. One of three surfaces in the project whose
   address is linkable.

What it does **not** have: the cut is in `localStorage`, not in the URL, so it is
per-browser and unshareable; and visible, scroll-relative position is not tracked.

## change signal
Grain: a cell id (`rNcM`), or a changed node assignment. The corpus is edited via
the Google Sheet — `data-date-lo`/`-hi` bracket the last-written time — so the
natural subscribable unit is **a sheet revision bracket**: one timeline entry =
one change. New figure bios are a secondary signal. Nothing is emitted today.

## export shape
- CSV, cell grain: `cell_id, row, seq, node, division, words, voice, figures,
  disciplines, date_lo, date_hi, text` — **the same columns as the upstream
  `assignments.csv`**, which is the cleanest "the description is the export
  query" case in the audit.
- JSON: `{id:"r8c4", row:8, seq:2, section:"i-1", voice, figures:[], date:[lo,hi],
  text}`.
- Cut export: `{q, quoted, byRow, readThrough, excludedLeaves:[…]}` — i.e. dump
  `qn`.

## narration
Shell `descriptions` entry at `explorer.html:1060` (names the Timeline and the
bios, commit `a19d39bf`); in-page "How to read this" `#about` (`:237`).
**No `voice_guide/knowledge` file**: `explorer.html:6167` maps
`'rc_sandbox_notebook.html': null`. It is the only entry in that map with a null
value, i.e. the one page the voice layer explicitly knows it cannot speak about.

## current capability
Contract: **none**, and `FIND_TABS` expects it with needle `levin`
(`test_voice_shell.cjs:2495`) → red. No `c2a2Ask`, no export button, no in-page
"?", no state bus, **no manifest entry**.

## what resisted description
- **The generator is lost.** You cannot regenerate the page you most want to
  change; every change must go through the patch scripts or by hand. This is the
  real finding, and the reason main document §7.3 recommends rebuilding from
  `assignments.csv` + `tl_sandbox_cells.json` rather than extending the page.
- How `data-tdate` entries are produced — not determined.
- The 36 node ids were not enumerated from the rail.
- Nothing amorphous. The gap between how well this page is built and how
  invisible it is to every layer is the audit's clearest single argument that the
  manifest should be derived from pages rather than hand-listed.
