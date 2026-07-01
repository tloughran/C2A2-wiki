# OpenStory → C2A2 — Session 5 handoff (2026-06-29)

Goal of the larger effort: mine the new OpenStory data into the C2A2 Explorer.
Sequence agreed: **(1) data bridge → (2) telemetry/reports → (3) reasoning-interaction
evidence.** This session did the *foundational prep* (and an unplanned DB recovery);
the build sequence is queued for the next, fresh session.

## What shipped this session

### 1. Attribution gap fixed (`extract_openstory_agent_data.py`)
Non-roster scheduled tasks now **self-attribute as "discovered" agents** (keyed by their
own name, flagged `needs_curation`, surfaced in `_meta.discovered_agents`) instead of
collapsing into one silent `(unmatched)` lump. `agent_map.json` is now an **enrichment
layer, not a gate** — new scheduled tasks attribute automatically, so the roster can't
silently drift (which is what froze the roster view before). Validated on live data:
26 discovered agents, 0 unmatched, all 1552 sessions balance.

### 2. BOSCO isolated out of both feeds (different project)
Single shared helper `is_excluded()` + `EXCLUDED_PROJECT_SUBSTRINGS=("bosco",)` in
`openstory_db.py`. Telemetry routes BOSCO sessions to an `(excluded)` bucket
(`_meta.excluded_sessions`); `extract_agent_node_refs.py` skips them. 43 sessions
isolated, zero leakage. Block is marked **ISOLATE NOW, REMOVE LATER** — delete the
constant + the two call sites when BOSCO is purged from open-story.db.

### 3. open-story.db corruption recovered (the real reason feeds froze since Jun 9)
The DB had persistent on-disk corruption (btree page 484358) — `count(*)` worked but
`GROUP BY` scans failed, aborting the daily refresh at quick_check. Fixed via
`~/Documents/openstory-db-recover.sh --apply` (recover → validate → atomic swap →
feed refresh). Corrupt original archived to
`Non-Claude Projects/OpenStory/data/corrupt-backup-20260629T164421/`. Retention
99.997% (patterns 195002→194997, events 290936→290934; sessions/turns full). Both
feeds refreshed at 16:45 for the first time since Jun 9.

### 4. launchd orphan / restart bug — root cause fixed in `openstory-backend.sh`
`open-story` kept running orphaned (pid 79324) after `launchctl bootout` because the
script did `exec cargo run … serve`: launchd supervised **cargo**, and the real
`open-story` ran as cargo's child — so stop killed cargo and orphaned open-story (and a
restart spawned a second one). Fixed: the script now **builds once, then `exec`s
`rs/target/debug/open-story` directly**, so launchd supervises open-story itself.

## ACTION REQUIRED on the Mac (I could not test launchd from the sandbox)

Apply the backend fix and confirm launchd now owns `open-story` directly:

```sh
# 1. Reload the backend agent so it picks up the edited openstory-backend.sh
launchctl bootout  "gui/$(id -u)/com.tomloughran.openstory.backend" 2>/dev/null
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.tomloughran.openstory.backend.plist

# 2. Verify ONE open-story, and that it is a child of launchd (PPID 1), not of cargo
pgrep -fl open-story
ps -o pid,ppid,comm -p "$(pgrep -f 'open-story serve' | head -1)"   # PPID should be 1

# 3. Prove clean stop (no orphan): bootout, then confirm nothing remains
launchctl bootout "gui/$(id -u)/com.tomloughran.openstory.backend"
pgrep -fl 'open-story serve'   # expect: no output
launchctl bootstrap "gui/$(id -u)" ~/Library/LaunchAgents/com.tomloughran.openstory.backend.plist
```

Notes:
- First start after the edit recompiles (debug) once; subsequent starts are fast.
- The **UI agent** (`openstory-ui.sh` → `exec npm run dev`) has the same parent/child
  shape (npm → vite); not fixed here because it doesn't write the DB. Apply the same
  pattern later if the dashboard ever strands a vite process.
- The old single `com.tomloughran.openstory.plist` is retired
  (`.plist.retired-20260625`); ignore the June-25 `openstory-restart-fix.md`, it predates
  the backend/bridge/ui split.

## Next session — start the build sequence (step 1: the bridge)

Add a third extractor `extract_turn_structure.py` → `turn_structure.json`, reusing the
existing snapshot/fail-loud/validate conventions, pulling per-session:
- `turns` (the eval/apply decomposition: human → thinking → eval → applies, with
  scope_depth, env_delta, duration_ms, stop_reason),
- `turn.sentence` patterns (the narrated turn sentences),
- `agent.delegation` patterns (the subagent spawn graph).

Then wire it into the `openstory-agents-telemetry-refresh` scheduled task. Steps 2
(telemetry/reports) and 3 (reasoning-interaction evidence) build on that JSON.

Open Rule-7 item: the node_refs feed maps non-roster sessions to a single HUMAN node
while telemetry uses `(interactive)`/discovered — reconcile during the build.
