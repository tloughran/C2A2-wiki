# Commentary Explorer — Stream 02: User-Uploadable Tool

**Launched:** 2026-05-07
**Status:** Scoping
**Owner:** Tom Loughran
**Predecessor:** Stream 01 (the present prototype) — 3rvme single-PDF visualization, complete and functional.

---

## Goal

Generalize Commentary Explorer from a one-off 3rvme renderer into a **drop-in tool** that lets a user upload any annotated-PDF + supplementary markdown and produces a self-contained HTML explorer of the same shape (force graph + chapter nodes + satellite halos + breadcrumb-stacked right panel + OCR pane).

**Constraint:** runs locally, no external wiki dependency at runtime.

---

## What's already built (and reusable)

The end-to-end pipeline already exists in two pieces; Stream 02 mostly wires them together with an upload UI.

**Ingestion side** — already implemented in `~/Documents/RC_Scans/`:

- `commentary_ingest.py` — given a PDF + book-id + author + title + year, runs OCR (Tesseract via OCRmyPDF) + page-image rendering + `claude-sonnet-4-6` calls with image+OCR-text prompt → emits the canonical commentary markdown shape we already parse. Schema and prompt are documented in `RC_Commentary_Pipeline_Technique.md` (V2, April 2026). Cost: $3–6 per 250-page book; runtime: 20–40 min.

- The output markdown sits in `~/Documents/Claude/Projects/RC_Wiki_Karpathy2upgrades/RC_Wiki/sources/[book_id].md` — same format as `macintyre_three-rival-versions_1990.md` on the desktop.

**Rendering side** — Stream 01 (this folder):

- `scripts/build_bundle.py` — parses commentary markdown + chapters.json + satellite scan + OCR JSON into a single bundle.json with chapters, pages, annotations, satellites, edges, and per-annotation OCR matches.
- `scripts/generate_html.py` — emits a single self-contained HTML with D3 force graph, breadcrumb-stack right panel, OCR pane with anchor highlighting.

The two streams' interfaces already match: `commentary_ingest.py`'s output markdown drops directly into `build_bundle.py`'s input slot.

---

## What Stream 02 needs to add

### 1. Upload UX

Given a local-only constraint, the simplest UI is a **small Tkinter or Electron-less HTML form** that runs as a single Python process the user double-clicks. Three input fields:

- **PDF file** (annotated scan; required)
- **Book metadata** (author, title, year; required — used for book-id and the bundle frontmatter)
- **Supplementary markdown** (optional; if supplied, gets rendered as a satellite node with kind `supplementary`)

A "Run" button kicks off ingestion. Progress UI shows the page-by-page ingestion (~10–15 s/page on sonnet-4-6) and then the bundle-and-render step.

A scrappier first cut: a CLI `commentary_explorer.py` that takes the same args as `commentary_ingest.py` plus an optional `--md SUPPLEMENTARY.md` and emits the explorer HTML. UI can come later.

### 2. Chapter-map detection

Stream 01 hand-tooled the chapter map for 3rvme (`data/chapters.json`) by reading PDF page summaries and matching against the user's TOC. For an upload tool we need this **automated or interactive**:

- **Option A (auto):** detect chapter boundaries from the OCR text by scanning for chapter-heading patterns (`CHAPTER\s+[IVX]+`, `^\d+\.?\s+[A-Z][a-z]+`, etc.) and the typographic conventions of the print edition. Robust enough for 80% of academic books.
- **Option B (interactive):** after ingestion, present the user with a UI showing detected page breaks and a few candidate chapter titles per break; user confirms or corrects.
- **Option C (passthrough):** require the user to supply a `chapters.json` alongside the PDF. Simplest, least friendly.

Recommend **Option A with B as fallback**: auto-detect, then a 30-second confirmation step where the user sees the proposed chapter list and clicks through any corrections.

### 3. Satellite-scope decoupling

Stream 01 hard-coded the satellite scan paths to RC's wiki and Summa vault. For a generic tool, satellites need to be **configurable per project**:

- A `commentary-explorer.config.json` per project root, listing satellite directories and per-directory glob patterns.
- A graceful empty-state when no satellite directories are configured: the graph just shows the chapter nodes with no halo. Still useful.

### 4. Extractor generalization

`build_bundle.py` has a few 3rvme-specific assumptions to remove:

- `EXTRA_THINKER_KEYS` (Stump → Aquinas/Aristotle/etc., Loughran → historical figures + MacIntyre) is hand-curated. For a generic tool, this becomes a per-project config or is dropped entirely (let satellites match by their own match-keys, no project-specific overrides).
- `GENERIC_TITLE_BLOCKLIST` (Summa-day phrases too generic to be edges) is also project-specific. Same answer: per-project config or per-satellite-kind.
- The thinker registry is RC-specific. Generic tool would derive thinker names from the satellite directory structure (one folder per thinker, with a `meta.json` listing match-keys).

### 5. Reusable HTML template

`generate_html.py` has its title and header text hard-coded for TRV. Stream 02 swaps these for `bundle.source.title` / `bundle.source.author` / `bundle.source.year` from the inlined frontmatter.

---

## Open questions

1. **Authoring chapter titles when none exist.** Some uploaded PDFs may not have a TOC, just chapters with numbers. Should the auto-detector pull chapter titles from chapter-opening paragraphs (using a Claude call), or default to "Chapter N"?

2. **Satellite scanning depth.** RC scans `traditions/*/wiki.md` — flat. A generic tool might need to traverse arbitrary directory structures. Use globs in the config.

3. **OCR quality threshold.** Stream 01's anchor-location rate is 39% on Tesseract output of a 1990 print. For sharper modern PDFs the rate would be closer to 90%. We may want a minimum quality bar before showing the OCR pane (or always show it with the disclaimer we already render).

4. **Multi-PDF projects.** Should one explorer instance hold multiple PDFs (e.g., your full annotated MacIntyre canon — *After Virtue*, *Whose Justice?*, TRV)? If yes, the chapter cluster becomes book-clusters and edges span books. Worth scoping.

5. **Where does the upload-tool process live?** A Python launcher in `~/Documents/Claude/Projects/Commentary Explorer/` (new top-level project), or stays here as `commentary-explorer/upload/`? Cleaner long-term to peel it out so it doesn't carry RC's wiki assumptions.

---

## Suggested next sessions

**Session A — CLI generalization (~2 hours):**
Take `build_bundle.py` + `generate_html.py`, factor out the RC-specific hardcodes into a `config.json`, add a top-level `commentary_explorer.py` that runs `commentary_ingest.py` + the bundle/HTML pipeline end-to-end. Outcome: `python3 commentary_explorer.py book.pdf --author "X" --title "Y" --year YYYY` emits a working HTML.

**Session B — Auto chapter detection (~3 hours):**
Add a chapter-detection pass to the ingest pipeline that scans the OCR text for chapter-heading patterns. Output a draft chapters.json. Wire an interactive confirmation step (HTML form or terminal prompt).

**Session C — Upload UI (~4 hours):**
Build a minimal local web UI: a Python web server (Flask or FastAPI) that hosts an upload form, a progress page (live-updates from the ingest process via SSE), and a final "Open Explorer" link. Or, simpler, a Tkinter window — depends on preference.

**Session D — Multi-PDF (deferred):**
Bundle two or more books into one explorer; promote chapter cluster to book-cluster; cross-book edges. Defer until A–C are working and you want it.

---

## Dependencies to confirm

- `pdftotext` (poppler-utils) — present on macOS via `brew install poppler`. Used by both ingest and the OCR-extraction pass in Stream 01.
- `OCRmyPDF` + `tesseract` — needed for ingest if PDF lacks a text layer. Already used in `commentary_ingest.py`.
- `anthropic` Python SDK — already a dependency of `commentary_ingest.py`.
- D3 v7 + marked.js — currently loaded from cdnjs in the rendered HTML. For truly-offline operation, inline both libraries into the HTML at generate-time (~250 KB + 50 KB).

---

## Files touched in Stream 01 (reference)

- `wiki/commentary-explorer/scripts/build_bundle.py`
- `wiki/commentary-explorer/scripts/generate_html.py`
- `wiki/commentary-explorer/data/chapters.json`
- `wiki/commentary-explorer/data/page_summaries.json`
- `wiki/commentary-explorer/data/ocr_text.json`
- `wiki/commentary-explorer/data/bundle.json`
- `wiki/commentary-explorer/commentary_explorer.html`

The `~/Documents/RC_Scans/` siblings (predecessor pipeline):
- `commentary_ingest.py`
- `RC_Commentary_Pipeline_Technique.md`
- `3RVME.pdf` (raw scan)
- `3RVME_ocr.pdf` (OCR'd, with text layer)
