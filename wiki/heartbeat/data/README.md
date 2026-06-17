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
      "implication": "string"
    }
  ]
}
```

- `seed: true` shows a "sample data" banner in the tab. Set it to `false` (or
  drop the key) once this file holds a real export.
- `relevance` is an integer score; higher = more relevant to C2A2 education.
- `tags` drive pill colour: `governance*` -> gold, `capability*` -> rose, else teal.
- `url` must be `http(s)`; anything else is dropped to `#` by the renderer.

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
