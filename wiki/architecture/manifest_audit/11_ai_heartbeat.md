# AI Heartbeat

**family** table · **manifest entry** NONE (knowledge file only) · **the only surface that detects and announces its own change**

## identity
`wiki/heartbeat/index.html`, 16,572 B. Explorer tab "AI Heartbeat"
(`explorer.html:471`). **Hand-authored page, generated data**:
`heartbeat/backend/export_digest.py` writes `digest.json`, `build_roster.py`
writes `sources_roster.json`, `archive_snapshot.py` writes `snapshots/`,
`enrich_summaries.py` merges `long_summaries.json`, and `backend/stamp_assets.py`
content-hash-stamps the script URLs (`index.html:302-304`). Siblings: `app.js`
(37.9 KB), `data/digest.json` (17.7 KB), 62 files in `data/snapshots/`.

## purpose
A read-only digest of recent AI developments, each scored and tagged for
relevance to C2A2 education, reshaped by a per-reader "lens" of filter and
ranking preferences.

## data sources
**Live-fetched static JSON**, always `?t=Date.now()` with `cache:"no-store"`:
`data/digest.json` (`app.js:662`), `data/sources_roster.json` (`:323`),
`data/snapshots/index.json` (`:330`), `data/snapshots/<file>` (`:362`). Baked
fallback `FALLBACK_DIGEST` (`:34`) used only if the fetch fails. Optional
Supabase from CDN for lens sync (`index.html:301`), configured in
`heartbeat-config.js`, with magic-link sign-in (`auth.js:75`). `localStorage`
`PREFS_KEY` holds the lens (`app.js:123-130`).

**This is the only content surface that fetches its data at runtime.** Every
other page bakes it. That single difference is why it is the only surface with a
working change notice, and it is the architectural lesson for layer 2.

## entities and fields
- **Digest**: `{seed, generated, generated_at, window, schema_ver,
  metrics{sources_reached, items_checked, high_relevance, primary_themes},
  signals[]}` — currently 10 signals, window "weekly", generated
  2026-10-03T14:58:26Z.
- **Signal**: `{title, source, url, relevance (int), tags[], summary,
  implication, published_at, first_seen_at, long_summary,
  summary_provenance{model, generated, kind}}`. All 10 have `long_summary`.
  Tags seen: `capability_jump`, `governance_policy`, `education`,
  `market_platform`.
- **Roster**: 19 sources in 7 lanes, `{key, label, sources[{id, name, home_url}]}`.
- **Snapshot index**: 61 entries, `{date, time, sort_key, generated_at, file,
  window, signals, items_checked, sources_reached, high_relevance,
  primary_themes}`.
- **Lens** (`PREFS`): `lens{sources, exclude_sources, exclude_tags, keywords,
  min_relevance}`, `ranking{sort, priority_tags}`,
  `communication{digest_cadence, channel, length}`,
  `consent{stars, comments, rank}` (`app.js:101-112`, `preferences.schema.json`).

## cut
A real filter cut **plus** an address, and the filter half is already exposed as
a single read/write pair.

| dim | kind | binding |
|---|---|---|
| view | set, 4 (pulse \| history \| lens \| roadmap) | `.hb-tab[data-view]` → `activateView()` (`:531`) — an address |
| query | value, free text | `#signal-search`, read in `renderSignals` (`:275`), applied with the lens |
| lens.sources | set | `#pref-sources`, `#le-sources` chips → `toggleInList` (`:471`) |
| lens.exclude_sources | set | `#le-exsources` |
| lens.exclude_tags | set | `#pref-extags`, `#le-extags` |
| lens.keywords | set of strings | `#le-keywords`, comma-separated, any-match (`:593`, `:208`) |
| lens.min_relevance | value | `#pref-minrel`, `#le-minrel` |
| ranking.sort | value | `#pref-sort`, `#le-sort`; `ranking.priority_tags` set via `#le-pritags` |
| communication.digest_cadence | value | `#pref-cadence`, `#le-cadence` |
| snapshot | address | `#history-dates .hb-hist-item` → `openSnapshot` (`:355`) — selects which baked document is read |
| actions | action | `#hb-refresh`, `#hb-pdf`, `#le-export` / `#le-import` / `#le-reset`, `#pref-reset` |

**`HB_getPrefs()` / `HB_setPrefs()` (`app.js:136-137`) already are the cut's
read/write pair** — a declared, serialisable, schema'd (`preferences.schema.json`)
view state, which is more than any other surface has. What is missing: neither
the active view nor the selected snapshot is URL-addressable (no hash handling),
and the snapshot selection is not persisted.

## change signal
**The reference implementation for layer 2, and the only page that acts on it.**
- Grain: one new signal keyed by `url` in `digest.json`, or a new entry in
  `snapshots/index.json`. Metrics (`high_relevance`) are a coarser derived signal.
  `first_seen_at` per signal means "new since I last looked" is computable per
  reader.
- **Not a live pulse** — the name is aspirational. It is a static-first snapshot
  (`data/README.md`; `ai_heartbeat.default.md`: "static digest snapshot … GitHub
  Pages with no live backend").
- **But it polls and announces**: `startLivePoll` refetches `digest.json` every
  60 s, compares a content signature, and renders "New data available (N new) -
  click Refresh" (`app.js:742-760`).
- Data refresh is off-page: `backend/com.c2a2.heartbeat.export.plist` (launchd)
  and `refresh_snapshot.sh`; latest digest and snapshots are 2026-10-03 22:00, so
  roughly daily.
- For a server-side layer: subscribe to `snapshots/index.json`'s newest
  `sort_key`, or diff signals by `url`.

## export shape
- CSV, signal grain: `generated_at, source, title, url, relevance,
  tags(;-joined), published_at, first_seen_at, summary, implication,
  long_summary`.
- JSON: one signal plus the digest's `generated_at`.
- **Existing**: lens-filtered PDF via `window.print()` with a print header
  (`#hb-pdf`, `app.js:545`), and lens JSON export/import (`:424-446`). No
  CSV/JSON export of the signals themselves — i.e. it exports the *query* and not
  the *results*, which is the exact inverse of what the export layer wants.

## narration
`voice_guide/knowledge/ai_heartbeat.default.md` (2026-08-28, `volatile: none` —
"NO state bus on this tab", which is true of the bus but understates the page,
since it polls). Covers purpose, Pulse, the lens, magic-link sign-in and
answerable questions. **Does not mention** History, Roadmap, Refresh, PDF or the
roster. Also `heartbeat/ARCHITECTURE.md` and
`wiki/architecture/30_community_heartbeat.md` (pathway doc, status drafted).

## current capability
Contract: **none** — `FIND_TABS` expects it with needle `agent`
(`test_voice_shell.cjs:2496`) → red. `#signal-search` is a working substring
filter over source, tag and title and is the natural binding for `c2a2Find`. No
`c2a2Ask`. Export: PDF + lens JSON only. "?" : one `#lens-help-btn` "What is a
lens?" (`index.html:111`) plus the shell entry. **No manifest entry.**

## what resisted description
- The scheduler cadence is unverified: the launchd plist is a template with the
  `StartInterval` vs `StartCalendarInterval` choice left to the installer, so what
  actually runs it is unknown even though the data is clearly current.
- Roadmap tab content not read (`index.html:279`).
- `INTEGRATION.md` is partly stale — it refers to a "fourth" sub-tab; the tab is
  now the fifth.
- `C2A2_Heartbeat_Explorer_Update_20260617_bundle/` and the matching `.zip`
  (41,560 B) at repo root are a superseded install bundle, untracked, and
  explicitly flagged "Do NOT apply" explorer.html (`INTEGRATION.md:3`). Not part
  of the live page.
- Nothing amorphous.
