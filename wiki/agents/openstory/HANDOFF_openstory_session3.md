# Handoff 3 — OpenStory → C2A2 Agent Explorer

_Session 3, 2026-06-08. Supersedes HANDOFF_openstory_session2.md for current state. Resume cue: "resume the OpenStory work"._

## Decisions locked this session
1. **Sequence: build on the current DB first** (no instance disruption / no Terminal relay). Phase-B seed deferred. (Last session's outage came from perturbing serve; current 571-session DB already has every thinker-pair with real eval/apply, so the pipeline is provable without reseeding.)
2. **Home: evolve `agents_tab.html` into a 3-subtab Agent Explorer.** Subtab 1 = existing schedule animation (now telemetry-enriched). Subtab 2 = sociogram. Subtab 3 = interrogative explorer.
3. **Sociogram edges = shared wiki-node references** (connect agents whose sessions touch the same nodes in the 1647-node narration graph). Chosen for subtab 2; not yet built.

## Done & verified this session
1. **Extractor — `agents/openstory/extract_openstory_agent_data.py`.** Reads the OpenStory DB **read-only** (`mode=ro`, NOT `immutable` — immutable throws "database disk image is malformed" while serve writes concurrently; DB itself is healthy, `quick_check: ok`). Emits `agents/openstory/agent_telemetry.json` (34 agents): sessions, events, eval/apply (+ratio), scope, errors, delegations, tool_use, tool_coverage, tool/model frequency, thinking/prompt counts, by-day-of-week, durations, first/last seen.
   - **Key fix — truncated labels.** `sessions.label` is hard-truncated to 50 chars, so longer thinker-pair slugs lose their tails (`...mcgilchrist-kastr`). Resolver matches the truncated fragment to the canonical taskId by **unique prefix-match** against `agent_map.json`. Deterministic (prefixes are unique); no ambiguous matches.
   - **Verified:** all 7 thinker-pairs' eval/apply reconcile EXACTLY vs independent SQL. Session totals match (572). Only uncaptured roster agent = `execution-assistant` (genuinely no runs). Unmatched labels are all interactive/manual sessions (`1pm-*`, `korbyt-apr*`, `cleanup-*`), not roster agents.
   - **Caveats baked into `_meta.caveats`:** `avg_duration_min` is run-span (inflated for long-lived/append sessions); `tool_coverage` is the fraction of tool_use events exposing `data.tool` — older (pre-tool-field) sessions read 0, so thinker-agent tool maps are sparse until fresh runs land.
2. **Injector — `agents/openstory/inject_telemetry.py`.** Embeds the JSON into `agents_tab.html` between `/* TELEMETRY_DATA_START/END */` markers (file:// can't fetch a sibling JSON — house rule). Idempotent; this is the Phase-B refresh step.
3. **Subtab-1 telemetry integration.** `agents_tab.html` detail panel now renders real telemetry via `telFor(taskId)` (`renderTelemetry()` function). `TELEMETRY_ALIAS` maps the HTML spelling `c2a2-wiki-agent-daily-run` → actual taskId `c282-wiki-agent-daily-run` (baked-in typo; do NOT rename without migrating history).
4. **Roster sync — `agents/openstory/sync_roster.py`.** Appended the 10 agents present in `agent_map.json` but missing from the animation (incl. `summa-qc-sweep`, highest-volume). Derives days/hour/minute from cron (DOW convention: 0=Sun..6=Sat, cron-compatible — confirmed). Surgical (existing 25 entries untouched) + idempotent. Roster now 35 = 34 map agents + `korbyt-tasks` (in viz, no telemetry). `telemetry agents not in roster: []`.
   - Multi-fire agents (`summa-qc-sweep` `*/4`, `summa-commentary-reviewer` hour-list) can't be fully shown by the single-hour animation model — given a representative time + cadence noted in description, tagged `multiDaily:true`.
5. **All validation green:** `node --check` + `validate_html.py` (JS syntax / double-brace / brace-balance) pass after every edit.

## NOT verified
- **Visual canvas render.** Structure/syntax/data validated; the animated canvas was not opened in a browser. Edits are additive/data-driven (low risk). Quick check: open the file, click `summa-qc-sweep`, confirm the "OpenStory telemetry" block shows in the detail panel.

## Next steps (resume here)
1. **Subtab switcher + Subtab 3 (interrogative explorer).** Well-specified, fast. Add a tab bar; wrap the existing `#content-area`+`#narration-strip` as view 1; add view 3 = sortable/filterable table over all 34 agents from `TELEMETRY` (eval/apply, volume, errors, tools, recency, by-day). RISK: the animation is `#app` flex-column (`#content-area` flex:1, `#narration-strip` fixed) — wrap carefully and re-validate render. House rules: regular strings not f-strings if a generator is used, single braces, `node --check` + `validate_html.py`, graceful fallback.
2. **Subtab 2 (sociogram, shared wiki-node references).** Meatiest piece. Need a session→wiki-node extractor: scan each agent session's events for references to vault wiki nodes (the 1647-node narration graph), then edge agents by shared nodes (weight = count). Likely a new script `extract_agent_node_refs.py` writing into `agent_telemetry.json` or a sibling. Then a force-graph subtab.
3. **Phase B — seed (#8) + schedule (#7).** Agent-only bridge mode (`AGENTS_ONLY=1` → `~/openstory-watch-agents`) + one-time seed with `OPEN_STORY_WATCH_BACKFILL_HOURS=0` (Terminal clipboard-relay, real machine; 64 MB cap holds). Then routine watch → agent bridge so new runs ingest live within the 72h window. Scheduled task: re-run extractor + injector for incremental refresh (cadence TBD with Tom).

## Key paths / facts
- DB: `~/Documents/Non-Claude Projects/OpenStory/data/open-story.db` (~1 GB, live; open read-only `mode=ro` only). Tables: events, sessions, patterns, turns, plans (+ FTS). patterns is rich: 46k eval / 37k apply.
- Vault: `~/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/`. Tab: `agents_tab.html`. Scripts + JSON + maps: `wiki/agents/openstory/`. Validator: `wiki/c2a2-wiki-narration/scripts/validate_html.py`.
- `agent_map.json` is the source of truth for the roster (34 agents) + cron/category/thinkers.
- Regen pipeline (run from `wiki/`): `python3 agents/openstory/extract_openstory_agent_data.py` → `python3 agents/openstory/inject_telemetry.py` → (if roster changed) `python3 agents/openstory/sync_roster.py` → `python3 c2a2-wiki-narration/scripts/validate_html.py agents_tab.html`. Scripts default to real-machine `~` paths; pass `--db/--map/--html/--out` to override (e.g. when running against mounts).
- Sandbox CANNOT see `~/Library/...` (Cowork store) — only `~/Documents` is mounted. DB + repo + vault are all under `~/Documents`, fully readable/editable via the mount.
