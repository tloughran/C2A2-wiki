# Plan — restore ~150-word per-article summaries (the "Distill" layer)

*Drafted 2026-06-17. Slated for execution next session. This is the Distill step of
the tab's Detect / Distill / Deliberate / Record quartet, and feeds the Compiled-Wiki
synthesis layer (Pathway 30, §4 Phase 1; durable-memory Pathway 16).*

## Current state (verified)

The runtime's `summarize(title, content, max_sentences=2)` is naive extractive — the
first two sentences of the RSS content, ≤700 chars, falling back to the title. No LLM
anywhere in the pipeline. So `signal.summary` in `digest.json` is a short blurb. The
earlier ~150-word synthesized summary per item did **not** survive into this revision.

## Design (decisions that shape the build)

1. **Generate server-side, store durably — never in the browser.** A ~150-word
   summary is an LLM task (working-agreement Rule 5: summarization is a valid model
   use). Generate once at ingest, persist, and ship in the snapshot. Client-side
   generation would need keys in the browser, be non-deterministic, and re-pay tokens
   every page load. This is also "computation persistence" (durable memory, Pathway 16).

2. **Grounded + honesty-marked.** Feed the LLM the article's own fetched `content`
   and instruct a faithful, extractive ~150-word summary — no facts beyond the source
   (AGENTS.md "never invent source claims"). Mark each as machine-generated
   (honesty layer, Pathway 14), distinct from any community-claimed interpretation,
   and store the model + date in provenance.

3. **Cache by stable id; only summarize what's shown.** Summarize at most the top-N
   items that reach the tab (default 12), keyed by item URL/id, skip if a
   `long_summary` already exists. Bounds cost and makes summaries stable once written.

4. **Route through the existing broker, if practical.** The cc-broker (Pathway 00)
   already provides a rate-limited AI gateway with daily caps in the same Supabase
   project. Prefer it over a raw key so budget/abuse controls are reused. Fallback: a
   direct provider key in the runtime's own env (the runtime is a separate local app).

## Pipeline touchpoints

- **Runtime `app.py`** (the separate local Heartbeat app): add a `long_summary`
  generator (LLM, ~150 words, grounded in `content`), persist it in the events table
  (new column `long_summary TEXT`), and include it in `window_report` `top_stories`.
  Content is already in hand at ingest (`it.get("content")`), so summarize there.
  Keep it optional/guarded so the runtime still works with no key (falls back to the
  current short summary).
- **`export_digest.py`**: pass `long_summary` (+ provenance: model, generated date)
  through in `map_signal`. Keep the export itself deterministic — it copies the field,
  it does not call a model. (If summarizing must happen outside the runtime instead,
  add a *separate* `enrich_summaries.py` step so the export stays model-free.)
- **Tab (`app.js` / `index.html` / `styles.css`)**: render the short `summary` as
  now, with an expandable "Full summary" (~150 words) when `long_summary` is present,
  plus a small "machine-generated" honesty tag. Absent field ⇒ short summary only
  (graceful, matches the current seed).
- **Schema**: add optional `long_summary` (string) and `summary_provenance`
  ({model, generated}) to the signal object in `data/README.md` and the seed.

## Open decisions for Tom (resolve at start of next session)

1. **LLM path:** broker (Pathway 00) vs a direct provider key in the runtime env.
2. **Where summarization lives:** in the runtime at ingest (recommended — content in
   hand, one-time) vs a separate post-export `enrich_summaries.py`.
3. **Scope:** summarize only the top-N shown (cheap) vs every ingested item (richer
   archive, higher cost).
4. **Length/format:** strict 150 words vs a ~120–160 band; one paragraph vs
   lead-plus-implication.

## Success criteria

- Each shown signal carries a faithful ~150-word `long_summary` grounded in its
  source, marked machine-generated, with model+date provenance.
- Summaries are cached (no re-pay on rebuild), bounded in cost, and the tab degrades
  cleanly when a summary is absent.
- The export step remains deterministic; the only model call is in the
  summarization/enrich step.
