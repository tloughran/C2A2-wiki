# RC Document Explorer

**family** reader · **manifest entry** NONE (knowledge file only) · **generator lost**

## identity
`wiki/rc_document_explorer.html`, 1,756,088 B, 4,581 lines. Explorer tab
"RC Document Explorer" (`explorer.html:467`, Education Tools row `#row2-edu`).
**Hybrid, and the generator is gone.** The original is a Claude artifact export
(the inbox copy `wiki/inbox/Resurrecting Civility — Document Explorer.html`,
1,877,060 B, 2026-04-06, differs from the wiki copy). It has been hand- and
script-patched since: the ToC block and 26 ids are now produced by
`wiki/inbox/rc_tome/render_toc_v2.py` (commit `d636792b` "Pilot Tome ToC v2";
`handoffs/explorer-roadmap.md` ~L810-815). No generator rebuilds the whole page;
`handoffs/explorer-roadmap.md` records the original `~/gen_html.py` as lost.
`SPEC_tome_extraction.md` says the file is 1,738,922 B, so it has changed since
the spec was written.

## purpose
A reader for the 471-page Pilot ChatGPT Tome (Tom's founding dialogue with
ChatGPT) that adds a table of contents, a per-thinker problem-resource-solution
view, and a PRS table that detects coils.

## data sources
All inlined; no fetch for content.
- `const TOC = [{level, text, anchor, page}]` (`:4061`) — a pre-v2 array; the
  visible ToC is the v2 DOM (`:348`), so this const is probably stale (inferred).
- `const SD = [{page, text}]` (`:4062`) — per-page text, the search corpus.
- Document DOM in `#doc-pane` (`:1342`): 1,106 `p.doc-body`, 690 `h1..h4.doc-h*`
  (the extractor merged these to 625), 472 `div.page-marker#page-N`, appendix at
  `:3541`.
- PRS is DOM: `div.prs-card[data-thinker][data-implicit]`, `div.prs-row`, plus
  `SP_THINKERS` (`:4387`).
- Only network call: the broker
  (`BROKER_URL=…/functions/v1/cc-broker`, `:3923`) when "Ask AI" is checked.
- Derivatives the page does **not** read, but which are the real data layer:
  `wiki/inbox/rc_tome/{tome_units.csv, tome_headings.csv, toc_v2.csv}`.

## entities and fields
- **Unit** = `p.doc-body`: `unit_id = tome:pPPPhHHsSS`, plus `ord, page,
  heading_id, heading_level, seq, words, text` (SPEC §4-6, and
  `wiki/inbox/rc_tome/tome_extract_log.md`).
- **Heading**: `id` = `pNNN-slug` (**truncated to ~44 chars and not unique**),
  `level`, `toc_role` (123 apparatus / 502 structural), `absorbed[]`.
- **Page marker**: `data-page`, 471 numeric pages.
- **Thinker**: 9 research programs, each with a summary and PRS cards.
- **PRS triplet**: P/R/S text, `data-implicit`. Solved table: 53 P/R/S cells per
  column (`.sp-cell-p/r/s`) plus coil links.

## cut
**There is no filter cut. This is an address-bearing reader, and its address is
computable and unreachable.**

| dim | kind | binding |
|---|---|---|
| view | value (toc \| thinkers \| solved) | `setSidebarView(view)` (`:4064`), `.sv-btn[data-view]` (`:192`) — state held in the DOM only |
| section | address | ToC click (`:4104`) → `target.scrollIntoView` on `#pNNN-slug`. **The handler `preventDefault`s, so `location.hash` is never written.** |
| page | address | `jumpTo(p)` (`:4203`) → `#page-N`; stable, unique, also not written to the hash |
| reading position | read | `dp.scrollTop` on `#doc-pane`; the scroll-spy (`:4088`) computes `_spyCur`, the current heading id — the real "where am I" read |
| thinker | value, 9 | `showThinker(id)` (`:4211`), `#th-scroll` (`:874`); initial `'levin'` |
| toc filter | value, string | `#toc-filter` → `filterToc(q)` (`:4073`), hides `li` for q > 1 char |
| prs jump | action | `:4264` and `#prs-return-btn`, stashing `_prsReturnState` (`:4224`) |
| search query | value | `#chat-input`, `#chat-ai-mode`; `doQuery()` (`:4145`); local path `retrieveCtx` (`:4122`) term-counts over `SD` and **returns pages, not ids**; `hlTerms` (`:4131`) highlights |

So a cut would be the address triple `{view, heading_id, page}` plus `thinker` in
the Thinkers view. Three facts make this the audit's sharpest "almost there":
1. **The per-paragraph ids exist in data and not in the DOM.** The extraction ran
   and passed V1-V8 (SHA-256 `9ecb26fa…`, `tome_extract_log.md`), producing
   `unit_id` per paragraph in `tome_units.csv`. Only ~15 `u-tome-…` ids reached
   the page (`handoffs/explorer-roadmap.md`, ninth entry).
2. **Heading anchors are stable but not unique** (44-char truncation). Absorbed
   ids are kept resolvable, so the collision is fixable from the extraction data.
3. **Nothing writes the hash**, so even the addresses that work are unlinkable.

Stamping the remaining 1,091 unit ids and writing `location.hash` on ToC clicks
would convert a 1.76 MB opaque reader into an addressable, exportable, narratable
corpus. That is the recommendation in main document §7.3.

## change signal
Grain: a section (`h2`/`h3` heading id) — "a new or changed section in the Tome",
or a changed `toc_v2.csv` row. The Tome itself is a frozen historical document,
so page-level and corpus-level signals are not useful; what changes is the
**apparatus** (a re-rendered ToC, a new PRS card, a new coil). The extraction
derivatives are the natural source of truth (inferred).

## export shape
- CSV, unit grain: `unit_id, doc, ord, page, heading_id, heading_level, seq,
  words, text` — **this already exists** as `rc_tome/tome_units.csv`. The export
  layer's job here is to surface a file that is already built, filtered by the
  address, not to invent a serialisation.
- JSON: `{unit_id, page, heading:{id, level, text, toc_role}, text,
  address:"rc_document_explorer.html#<heading_id>"}`.
- View record: `{view, heading_id, page, thinker}`.

## narration
`voice_guide/knowledge/rc_document_explorer.default.md` (affordances, the 3 views,
pathways, answerable questions), mapped at `explorer.html:6164`
(`volatile: none`, "NO state bus"). Shell `descriptions` entry at
`explorer.html:1056` (it is the 650-link-ToC text — correct for this page, and
the text that was wrongly duplicated onto Curriculum Tools; see
`05_curriculum_tools.md`).

## current capability
Contract: **none** — `FIND_TABS` expects it with needle `levin` (`:2493`), so this
row is red. The page's own search is real but page-grained, not id-grained. No
`c2a2Ask`, no export, no state bus. **No manifest entry** (confirmed absent from
the 9). "?" : CSS for `#doc-help-btn` / `#doc-help-pop` and a `toggleDocHelp()`
exist (`:4366`) but no button was found in the HTML — dead code (inferred); the
shell entry is what users get.

## what resisted description
- Whether the `TOC` const is still consulted after the v2 render (inferred stale).
- The original artifact generator is unknown and lost.
- `SPEC_tome_extraction.md` still says the extraction is "NOT YET EXECUTED" while
  `tome_extract_log.md` records V1-V8 PASS. **The spec and the log contradict
  each other about work that shipped**; the spec should be marked done.
- Nothing amorphous. Everything here is an addressing gap, which is the cheapest
  kind.
