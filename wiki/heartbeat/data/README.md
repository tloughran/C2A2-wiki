# Heartbeat digest snapshot

`digest.json` is the static data the Pulse view renders. It is a snapshot of the
Heartbeat runtime's `/api/digest` output, trimmed to the fields the tab needs.
The tab works on GitHub Pages with no live backend, and falls back to an embedded
copy in `app.js` if this file can't be loaded (e.g. opened over `file://`).

## Schema

```json
{
  "seed": false,
  "generated": "YYYY-MM-DD",
  "window": "weekly",
  "metrics": {
    "sources_reached": 0,
    "items_checked": 0,
    "high_relevance": 0,
    "primary_themes": "short phrase"
  },
  "signals": [
    {
      "title": "string",
      "source": "string (e.g. arXiv cs.AI, OpenAI Blog)",
      "url": "https://...",
      "relevance": 2,
      "tags": ["capability_jump", "governance_policy", "education", "market_platform"],
      "summary": "string",
      "implication": "string",
      "long_summary": "string (optional; ~150-word machine-generated Distill summary)",
      "summary_provenance": {
        "model": "string",
        "generated": "YYYY-MM-DD",
        "kind": "machine-generated"
      }
    }
  ]
}
```

- `seed: true` shows a "sample data" banner in the tab. Set it to `false` (or
  drop the key) once this file holds a real export.
- `relevance` is an integer score; higher = more relevant to C2A2 education.
- `tags` drive pill colour: `governance*` -> gold, `capability*` -> rose, else teal.
- `url` must be `http(s)`; anything else is dropped to `#` by the renderer.
- `long_summary` + `summary_provenance` are **optional** (the Distill layer). When
  present, the tab shows an expandable "Full summary" with a machine-generated
  honesty tag; when absent, the tab shows the short `summary` only (graceful).
  They are NOT written by the runtime or the exporter — they are merged in from
  `long_summaries.json` by `backend/enrich_summaries.py` (see below).

## Distill layer (`long_summaries.json` + `enrich_summaries.py`)

The ~150-word summaries are model-written (summarization is a valid model use per
the working agreement), but the *merge into the snapshot is model-free*. The split:

- `long_summaries.json` — sidecar, keyed by signal `url`, each entry holding
  `long_summary`, `model`, `generated`, `kind`. A model writes these from each
  item's fetched content, grounded only in the source (never invented).
- `backend/enrich_summaries.py` — deterministic, stdlib-only. Merges matching
  sidecar entries into `digest.json` (and the dated snapshot) and strips the
  `arXiv:… Announce Type:… Abstract:` boilerplate from the short `summary`.
  Idempotent; signals with no sidecar entry are left untouched.

```bash
python3 backend/enrich_summaries.py --data-dir data        # merge + clean
python3 backend/enrich_summaries.py --data-dir data --check # report only
```

### Auto-generating summaries (cc-broker, Pathway 00)

`backend/generate_summaries.py` is the MODEL step: it fills the sidecar for any
signal URL not already present, by calling the broker's `action=enrich`
(`Origin` + `X-CC-Device` headers; the broker holds the OpenRouter key and meters
a daily cap, so this script sends NO secret). It is incremental + idempotent —
existing entries are never overwritten — so hand-written summaries survive and
only genuinely new items cost tokens. Graceful on cap/down (stops, leaves the
rest for next run).

```bash
python3 backend/generate_summaries.py --data-dir data --max-new 12
python3 backend/generate_summaries.py --self-test     # one broker call, writes nothing
```

## History manifest (`snapshots/index.json`)

The History tab needs an explicit list of snapshots (Pages has no directory
listing). `backend/build_manifest.py` scans `snapshots/digest-*.json` and writes
`snapshots/index.json` (newest first, with each snapshot's headline counts).
Deterministic, idempotent.

```bash
python3 backend/build_manifest.py --data-dir data
```

## Full refresh pipeline

`backend/refresh_snapshot.sh` runs the whole chain (Mac-side, runtime must be up):

```
export_digest.py  →  generate_summaries.py  →  enrich_summaries.py  →  build_manifest.py
   (deterministic)      (model, via broker)       (deterministic)        (deterministic)
```

## Regenerating from the live runtime

Reference runtime: `/Users/tloughr1/Documents/C2A2 Heartbeat/c2a2_heartbeat`
(included in the original update bundle under `reference-runtime/`).

Use `backend/export_digest.py` (stdlib only, deterministic field map — no model).
Run it on the Mac next to the runtime; it writes `digest.json` (latest, what the
tab loads) plus a dated `snapshots/digest-YYYY-MM-DD.json` for historical depth,
and sets `seed:false`.

```bash
# 1. start the runtime (uses the LocalThreadingHTTPServer bind fix)
cd "/path/to/c2a2_heartbeat"
python3 app.py            # serves /health, /api/digest, /dashboard

# 2a. fetch directly:
python3 wiki/heartbeat/backend/export_digest.py \
  --url "http://127.0.0.1:<port>/api/digest?window=weekly"

# 2b. or from a saved response:
curl -s "http://127.0.0.1:<port>/api/digest?window=weekly" > /tmp/digest.raw.json
python3 wiki/heartbeat/backend/export_digest.py --from-file /tmp/digest.raw.json
```

Add `--token <T>` if the runtime requires one, `--limit N` to cap signals
(default 12), `--data-dir PATH` to target a different data folder. Schedule 2a
(launchd / cron) to keep the snapshot fresh.

## Note on the current seed

The shipped `digest.json` is **sample data** (`seed: true`). Sources are attributed
to families (arXiv cs.AI, Google AI Blog) and links point to source-family landing
pages rather than fabricated article IDs, per the `AGENTS.md` "never invent source
claims" rule. Replace with a real export before treating any figure as factual.
