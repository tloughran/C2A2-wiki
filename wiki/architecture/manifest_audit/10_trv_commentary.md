# TRV Commentary

**family** graph + reader · **manifest entry** NONE (knowledge file only) · 11 MB

## identity
`wiki/commentary-explorer/commentary_explorer.html`, 11,016,469 B. Explorer tab
"TRV Commentary" (`explorer.html:470`). **Generated** by
`wiki/commentary-explorer/scripts/generate_html.py` (45 KB), whose input is built
by `scripts/build_bundle.py` (schema `commentary-explorer/1`, `:524`).
`window.BUNDLE` is inlined at `:307` — 10.9 MB of the 11 MB file is that one
line. Both generators are tracked. Sibling data: `data/bundle.json` (10.97 MB),
`ocr_text.json` (329 KB), `page_summaries.json` (121 KB), `chapters.json`,
`pages/` (240 entries, page JPEGs).

## purpose
A force-graph of MacIntyre's *Three Rival Versions of Moral Enquiry* in which
chapter nodes carry Tom's scanned marginal annotations and OCR text, linked to
thinker, PRS and Summa-day satellite notes.

## data sources
Baked, no runtime fetch. `window.BUNDLE` from `data/bundle.json`; D3 7.9.0 and
marked 12.0.2 from cdnjs (`:7-8`). Upstream inputs per `build_bundle.py:6-14, 342`:
the commentary markdown `macintyre_three-rival-versions_1990.md`,
`chapters.json`, `ocr_text.json`. Page scans `pages/pNNN.jpg` feed a lightbox;
the page itself notes the scan sidecar is local-only and not published (`:302`).

**Rebuild needs files outside the repo.** Satellite bodies carry
`source_path: /Users/tomloughran/…/Summa 2026 in a Year/vault/synthesi…`, so the
bundle cannot be rebuilt from the repo alone. That is a reproducibility finding,
and it belongs in the manifest as a `generator.inputs` entry rather than being
discoverable only by reading the data.

## entities and fields
- **Bundle**: `{schema, source, chapters[12], satellites[292], edges[888]}`.
- **source**: `{filename, title, author, year, annotation_count: 3400,
  pages_with_annotations: 236, scan_file, pdf_offset_from_book: 5}`.
- **Chapter**: `{id, number (-1 preface, 0 intro, 1-10), title, pdf_pages[a,b],
  title_confidence, annotated_page_count, annotation_count, pages[]}`.
- **Page**: `{page, summary, ocr_text, annotations[]}`.
- **Annotation**: `{id "221.1", type, content, anchor_text, …}`.
- **Satellite**: `{id, kind, title, color, body_md, source_path, thinker, day}`;
  kinds = summa 267, prs 13, thinker 12.
- **Edge**: `{from, to, weight, kind}` — `chapsat` 212, `satsat` 676 — with
  `evidence[{page, ann, key, snippet}]`. **The edges carry their own evidence**,
  which no other graph surface does, and which makes this the one page where an
  edge export would be genuinely valuable.

## cut
Filter sets compose cleanly; the address does not persist.

| dim | kind | binding |
|---|---|---|
| kind | set (thinker \| prs \| summa \| summa-transcript) | `satKindShown`, `#filters input[data-kind]` (`:369-391`) |
| chapter | set | `chapShown` |
| thinker | set | `thinkerShown` |
| summa day | set, 267 ids | `summaShown` |
| onlyConnected | value, bool | "only satellites connected to visible chapters" |
| — | — | AND-composed in `satVisible` (`:379-390`) |
| camera / layout | action | `#btn-fit`, `#btn-freeze`, `#btn-labels` |
| address | address | `navStack` / `fwdStack` frames `{nodeId, crumbLabel}` (`:607-630`); within a chapter, page + annotation (`jumpToChapterPage`, `wireOcrMarks`, DOM ids `ann-<page>-<id>`, `:853`); Esc goes back (`:661`) |

Addressable in principle by `node id + page + ann id`. **Nothing is serialised**:
no hash, no `localStorage`; filters are in-memory only. So this surface is the
clean illustration of the two families sitting in one page — a graph cut that is
readable and a reader address that is not persisted.

## change signal
Effectively none. The bundle is static and rebuilt by hand (file dated
2026-09-16). The only meaningful change is a new `bundle.json` build, observable
as a change in `source.annotation_count` or `schema`, or a new Summa-day
satellite after a rebuild (267 now). Grain: per annotation (`ann` id) or per
satellite id. `grain: regen` is the honest declaration.

## export shape
- CSV, annotation grain: `chapter_id, page, ann_id, type, anchor_text, content`.
- CSV, edge grain with evidence: `from, to, kind, weight, evidence_page,
  evidence_ann, evidence_snippet` — the one export in the audit that would carry
  an argument rather than a record.
- JSON: an annotation, optionally with its edge `evidence` links.
Nothing exists today.

## narration
`voice_guide/knowledge/trv_commentary.default.md` (2026-08-28, `volatile: none`,
"NO state bus"). Chapter and page `summary` fields are baked per page
(`page_summaries.json`) and are the obvious feed for explainer and narration
text — a per-page authored summary already exists for 236 annotated pages, which
is more narration material than any other surface has.

Discrepancy: the knowledge file mentions "companion views from Eleonore Stump and
N. T. Wright", while the bundle's satellites are thinker 12 / prs 13 / summa 267.
Whether Stump and Wright are among the 12 thinkers was not verified.

## current capability
Contract: none. No `c2a2Ask`, no export, no "?" in page (the `#lightbox` is a
scan viewer); shell `descriptions` entry present. **No manifest entry.** Not in
`FIND_TABS` (`test_voice_shell.cjs:2488-2496`), so no failing row — i.e. the
project's one honest instrument for layer 1 does not watch this surface at all.

## what resisted description
- `generate_html.py` was not read in detail, so whether
  `commentary_explorer.html` regenerates deterministically from `data/` is
  unverified.
- `:877-1045` (satellite and wikilink rendering) not read.
- The 11 MB inlined bundle is a structural constraint: anything reading the page
  must parse the whole bundle, or read `data/bundle.json` instead. A manifest
  `data.sources[].mode: baked` with a pointer to the sidecar would let every
  layer take the cheap road.
- **`commentary-apparatus/` at repo root is NOT this page's apparatus.** It is
  the Summa 2026 referencing / works-cited / reference-master pipeline
  (`Referencing and linking foundation.md:2`). Only `wiki_narration.html`
  references it. Worth recording because the name invites exactly the wrong
  inference.
- No TRV or MacIntyre document exists in `wiki/architecture/` — the only hits
  were `.bak` files. For a tab built on a MacIntyre monograph, in a project whose
  north star is MacIntyre's rival-traditions argument, that is a narration gap
  rather than a technical one.
