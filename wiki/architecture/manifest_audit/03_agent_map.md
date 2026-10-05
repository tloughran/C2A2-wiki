# Agent Map

**family** chart (schedule) + table (explorer) · **tier** T1 · **manifest entry** yes, `agents_tab` — thin

## identity
`wiki/agents_tab.html`, 158,439 B, modified 2026-10-04 06:20. Explorer tab
"Agent Map" (`explorer.html:454`). **Hybrid**: hand-written HTML/CSS/JS and the
`AGENTS` roster (`:456-740`); the `TELEMETRY` const at `:444` (74.5 KB) is
injected by `agents/openstory/inject_telemetry.py` between
`/* TELEMETRY_DATA_START/END */` markers (`:441-445`, "do not hand-edit the
block"); `sync_roster.py` appends missing agents to `AGENTS`.

## purpose
Shows the scheduled autonomous agents three ways: a weekly animated schedule, a
co-reference sociogram, and a sortable telemetry table.

## data sources
**Baked, not fetched.** `TELEMETRY` generated 2026-10-04T06:20 — 4,644 sessions,
2.09M events — from `OpenStory/data/open-story.db` via
`extract_openstory_agent_data.py` and `agents/openstory/agent_map.json`.
`inject_telemetry.py:5-6` states the reason: `file://` cannot fetch a sibling
JSON. Staging copy: `agent_telemetry.json` (107,897 B). `AGENTS` is baked and
hand-edited, with a hardcoded alias `c2a2-wiki-agent-daily-run` →
`c282-wiki-agent-daily-run` (`:447`). The sociogram sub-view lazily iframes
`wiki_narration.html#agents` (~25 MB, `:383`, `:1626-1631`), which carries
`agent_node_edges.json` (913,743 B, regenerated 2026-10-04 06:36 by
`extract_agent_node_refs.py`: `_meta`, `agent_nodes` 28, `coref_substrate` 6,010,
`coref_projected` 307, `flow` 56).

## entities and fields
- **Roster agent** (`AGENTS`): `taskId, description, schedule, category, days[],
  hour, minute, narration, multiDaily, thinkers[]`.
- **Telemetry agent** (`TELEMETRY.agents[taskId]`): `category, schedule, cron,
  thinkers, constitutions, captured, sessions, events, eval, apply,
  eval_apply_ratio, scope_open/close, errors, delegations, tool_use,
  tool_use_named, thinking, prompts, first_seen, last_seen, by_dow[7], tools{},
  tool_coverage`. Plus `discovered`, `buckets`, `_meta` (roster 33, captured 32,
  discovered 28).
- **Category** (`CAT`, `:740`): 6, with labels and colours.

## cut
Sub-view dependent.

- **view** (set, 3): `.subtab-btn[data-view]` → `switchView` (`:1606-1618`):
  schedule | sociogram | explorer. Declared in the manifest as `views`.
- **Explorer sub-view** (family: table) — *the real cut, and the one the
  manifest does not declare*:
  - text filter (value): `#exp-search` (`:389`, listener `:1654`), matching
    `taskId + friendly name + category`.
  - category (set of 6): `#exp-cat` (`:390`, `:1655`); options are raw category
    keys, not display labels.
  - sort (value: key + direction): `.exp-table th[data-key]`, module vars
    `sortKey` / `sortAsc` (`:1670`, `:1700-1706`), default `events` desc, 9
    columns (`COLS`).
  - read: `#exp-count` ("N / M agents"); row select `tr[data-task]` →
    `showDetail` (`:1273`, `:1708-1714`).
- **Schedule sub-view** (family: chart; canvas-drawn, agents are not DOM):
  playback actions `#btn-play` / `#btn-pause` / `#btn-reset` / `#btn-narrate` /
  `#btn-skip`; speed `#speed-select` (10 | 60 | 360 | 720, `:295-302`); time
  `#progress-bar-wrap` scrub over `currentMin` (`:822`), range 0-10,080;
  legend read `#legend-items`.
- **Sociogram sub-view**: `items.kind: none`; it has no cut of its own here.
- **Detail panel**: `selectedAgent` (`:824`), `#det-*`.

**Time is not a dimension.** `TOTAL_MIN = 7*24*60` (`:799`) is a weekly playhead,
not a range filter, and telemetry is all-time aggregates (`by_dow`, `first_seen`,
`last_seen`) with no date-range control. The playhead is a position in an
animation — nothing would subscribe to it, export it or narrate it. Declare the
table; mark the animation `kind: action, inverse: null`, which §3 of the spec
already provides for.

## change signal
- **Page level, best candidate**: `TELEMETRY._meta.generated` and `db_mtime`,
  which move when `refresh_openstory_feeds.sh` passes. `REFRESH_STATUS.md` is a
  one-line PASS/FAIL and **currently reads FAIL** — sandbox `useradd: No space
  left on device`, Mac-shell fallback auto-declined, last PASS 2026-10-04T10:15Z.
- **Per agent**: `last_seen`, `sessions`/`events` deltas, `errors`, `captured`
  flipping false→true, roster add/remove.
- **Cadence**: feed refreshed daily by a scheduled task (inferred);
  `refresh_openstory_feeds.sh:6-8` is the Mac runner; **publish is manual** —
  the script's closing lines say "Publish is manual: git add/commit
  agents_tab.html + agent_node_edges.json".
- **Nothing on the page emits anything.** The baked data can silently lag the DB,
  and right now it does. Metabolism, the adjacent tab, warns in exactly this
  case; this one does not. Same failure class, opposite handling.

## export shape
- CSV, agent grain: the Explorer table's 9 columns — `name, category, sessions,
  events, eval_apply_total, eval_apply_ratio, errors, tool_coverage, last_seen`
  (+ `schedule`, `cron`, `thinkers`).
- JSON: `TELEMETRY.agents[taskId]` merged with the matching `AGENTS` entry.
- Edges: from `agent_node_edges.json` as `source, target, weight, layer`.

## narration
Per-agent `narration:` strings in `AGENTS` (`:462-467`) — in the samples read
they merely duplicate `description`. `PRODUCES` per category (`:749`). Shell
blurb `explorer.html:1076-1078`. Knowledge:
`voice_guide/knowledge/agent_map.default.md` (2,115 B, 2026-08-28,
`volatile: none`, "NO state bus"), which forbids claiming any agent's current
health — correctly, given the FAIL above. Needs writing: per-sub-view narration
and anything telemetry-aware.

## current capability
Contract: **none** (`FIND_TABS` expects it, needle `summa` → red). No `c2a2Ask`,
no export, no in-page "?" (shell `descriptions` entry only), no state bus.
Manifest `agents_tab`: 11 caps (go, back, what, where, help, pick, next,
previous, read, summarize, stop), `knobs: []`, 3 views, 3 `items` entries
(explorer rows as `agent` with a total regex; schedule legend as `category`;
sociogram `none`), **`dim_coverage` = `tab` only**, 5 `controls_deferred`, no
`controls_excluded`, 4 gestures. `voice_guide_redesign.md` §O (`:945`) records
3 covered / 10 deferred / 0 uncovered — the first tab that needed a declaration
and no code.

**Judgement**: a fully declarative, filterable, sortable 9-column table is
declared to the manifest as "a tab you can go to". This is the single largest
gap between what a page *is* and what the manifest *says it is*, and the F5
family work should start here.

## what resisted description
- Exact roster size: 38 `taskId:` matches in the file vs 33-34 in the telemetry
  and the spec.
- How the `#agents` preset filters nodes inside the 25 MB sociogram artifact —
  not traced.
- The scheduled-task definition that runs the telemetry refresh — not located.
- Amorphous only in the schedule canvas's DOM-lessness; its underlying data
  (`AGENTS[].days/hour/minute`) is plain JS. Everything else is undocumented.
