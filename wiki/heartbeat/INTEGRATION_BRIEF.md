# C2A2 Heartbeat -> Community AI Education Integration Brief

Date: 2026-06-17

## Latest Working Reference Found

The latest verified Heartbeat runtime is:

`/Users/tloughr1/Documents/C2A2 Heartbeat/c2a2_heartbeat`

It is a dependency-light Python reference implementation with:

- RSS source polling
- SQLite persistence at `data/heartbeat.db`
- risk tags and C2A2 relevance scoring
- `/dashboard`, `/api/events`, `/api/digest`, and `/health`
- public-share helper script using Cloudflare Tunnel

I fixed a local startup problem in `app.py`: Python's default `ThreadingHTTPServer`
called reverse DNS during bind and hung on this Mac before the server became reachable.
The app now uses `LocalThreadingHTTPServer`, which binds without reverse DNS lookup.

Verification after the fix:

- `GET /health` returned OK.
- `GET /api/digest?window=weekly` returned 95 tracked updates.
- Configured source families reached: OpenAI Blog, Hugging Face Blog, Google AI Blog,
  arXiv cs.AI, and The Verge AI.

## Adjacent Code Located

- `/Users/tloughr1/Desktop/C2A2 Community Explorer from laptop/c2a2-community-explorer`
  is the newer public Explorer/Streamlit prototype and is one commit ahead of
  `origin/codex/streamlit-prototype`.
- `/Users/tloughr1/Desktop/C2A2 Community Explorer from laptop/c2a2_stage2_14h_working_tool 3`
  is a Stage 2.14h C2A2 conversation/PRS tool. It is useful context, but it is not the
  Heartbeat runtime.
- `/Users/tloughr1/Downloads/C2A2 Transparency /` contains the design/proposal docs
  for the fuller production architecture.

> **Architecture of record:** the full multi-community vision, its assessment, and the
> phased roadmap now live in `ARCHITECTURE.md`. The condensed list below is a summary;
> `ARCHITECTURE.md` governs scope (what may be built now vs deferred).

## Target Integration Point

The public C2A2 Explorer is in:

`/Users/tloughr1/Documents/GitHub/C2A2-wiki/wiki/explorer.html`

It already had a disabled `Community AI Education` tab. That tab is now wired to:

`wiki/heartbeat/index.html`

This creates a GitHub Pages-safe first integration while the live runtime remains local or
future-backend-backed.

## Architecture Update Applied

The new tab reframes Heartbeat as a Karpathy-style LLM wiki:

1. Raw sources stay immutable.
2. Heartbeat runs fetch, dedupe, summarize, tag, score, and log source health.
3. A compiled markdown wiki preserves durable synthesis.
4. Community lenses apply local preferences, roles, consent rules, and memory.
5. A shared graph receives only permissioned contributions such as stars, comments,
   aggregate rankings, and public citations.

This directly incorporates the multi-community architecture notes:

- authentication and role separation
- user preferences and memory
- computation persistence
- federated search and edge instances
- local data ownership
- selective contribution
- encrypted transport in production
- public shared knowledge graph
- design for thousands of instances

## Recommended Next Slice

1. Export `/api/digest?window=weekly` to a static JSON snapshot under `wiki/heartbeat/data/`.
2. Render that snapshot in the static tab instead of hardcoded sample signals.
3. Add `raw/`, `wiki/`, and `logs/` content directories with real compiled markdown pages.
4. Define a small OpenAPI-style contract for future federated search:
   - `/api/public/heartbeat/search`
   - `/api/public/heartbeat/stars`
   - `/api/public/heartbeat/topic/{id}`
5. Add auth before any write path or per-user preference persistence.
6. Keep GitHub Pages public; put live instance APIs behind a separate authenticated service.
