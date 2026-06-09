# Handoff — OpenStory → C2A2 Agent Explorer

_Session date: 2026-06-08. Resume in a fresh session; this is the state + the exact next steps._

## Where we are (done)
1. **OpenStory reinstated, running local-only.** Pulled 89 commits (now at `44dd9fa`). Hit the new hard NATS dependency; sidestepped the Hetzner hub with a local-only config `deploy/nats-local.conf` (no `leafnodes` block). Stack live: NATS `127.0.0.1:4222` (+8222), backend `cargo run -- serve` on `:3002`, Vite UI `:5173`.
2. **One-touch launcher**: `scripts/up-local.sh` + desktop `Launch OpenStory.command` (idempotent; starts NATS→backend→UI, opens browser). Note: after a UI-dep-changing pull, run `cd ui && npm install` once.
3. **MCP connector live in Claude Code.** `.mcp.json` defines stdio server `openstory` → `rs/target/release/open-story-mcp` (release binary built). `claude mcp list` shows `✓ Connected`. (Desktop/Cowork app uses DXT extensions, not a config file — deferred; Claude Code was the fast path.)
4. **Design grounded.** Agent Explorer = subtab 3c of the C2A2 community explorer (`wiki/agents_tab.html`): a table of ~30 agents × days-of-week, click→constitutional markdown, play→narrate across time. Currently authored narration; OpenStory replaces it with observed telemetry. Same generate→inject→validate pipeline as `wiki_narration.html`.
5. **Identity join SOLVED.** OpenStory `sessions.label` = `<scheduled-task name="{taskId}">`; `taskId` == scheduler id == roster key. Maps delivered: `openstory_c2a2_agent_map.md` (human) and `agent_map.json` (machine, for the generator).
6. **Capture gap diagnosed.** OpenStory watches `~/.claude/projects/` (13 files) but agents run as Cowork sessions in `~/Library/Application Support/Claude/local-agent-mode-sessions/` (2,763 files). Result: ~93 agent sessions captured, 4 of 7 thinker pairs at ZERO. Format is identical (same JSONL schema), so no new translator needed.
7. **Fix scoped + validated.** Two parts: (a) recency — `OPEN_STORY_WATCH_BACKFILL_HOURS=0` disables the startup skip (env, no code); (b) structure — `paths.rs` expects `watch_dir/{project}/{session}.jsonl`, but Cowork nests `{uuid}/.claude/projects/{project}/{session}.jsonl`, so use an external **session bridge** (NOT an OpenStory fork — Tom syncs upstream). **Validated empirically: the watcher follows symlinks; a symlinked Cowork session backfilled 11 CloudEvents.** Use symlinks.

## Next steps (resume here)
1. **Build `scripts/openstory-bridge.sh`** (idempotent): for every `~/Library/Application Support/Claude/local-agent-mode-sessions/*/.claude/projects/*/*.jsonl` (and `~/.claude/projects/*/*.jsonl`), create a symlink at `~/openstory-watch/{project}/{session}.jsonl` (carry `subagents/` subdirs too). Re-runnable; later wire as a scheduled task or fswatch for new sessions.
2. **Run a TEST OpenStory** against the bridge without disturbing the running instance: `OPEN_STORY_WATCH_BACKFILL_HOURS=0 open-story serve --watch-dir ~/openstory-watch` (or the watch subcommand) into a scratch data dir.
3. **Verify capture climbs**: re-run the per-slug completeness query (below); confirm the 4 zero-capture thinker pairs + weekly agents populate.
4. **Then build the extractor/generator** for `agents_tab.html`: `extract_openstory_agent_data.py` reads `data/open-story.db`, groups sessions by agent slug × day, computes per-cell stats (sessions, events, eval/apply ratio from `patterns`, errors, duration) + a short narrative; emits JSON consumed by the tab generator. Follow C2A2 house rules (regular strings, `""" + json + """`, single braces, validate with `node --check` + `validate_html.py`). Loosely coupled, graceful fallback to authored narration if data absent. Use `agent_map.json` as the single source of truth.

## Key facts / paths
- OpenStory repo: `~/Documents/Non-Claude Projects/OpenStory` (quote the space). Default upstream branch `master`.
- SQLite store: `~/Documents/Non-Claude Projects/OpenStory/data/open-story.db`. Tables: `sessions` (id, project_name, label, custom_label[empty], branch, first/last_event, host, user, event_count), `events` (session_id, timestamp, subtype, agent_id[opaque hash], payload), `patterns` (eval_apply.* — 26k eval/21k apply/etc.), `plans`, `turns`, `events_fts`.
- Watcher source: `rs/src/watcher.rs`, `rs/src/snapshot_watcher.rs`; path parser `rs/core/src/paths.rs`. Watch-dir default `rs/cli/src/main.rs:207 default_watch_dir()` = `~/.claude/projects`. Skips dotfiles WITHIN watch_dir (so bridge root must be non-dotted, e.g. `~/openstory-watch`).
- Env: `OPEN_STORY_WATCH_BACKFILL_HOURS=0` (full backfill), `OPEN_STORY_MAX_INITIAL_RECORDS`, `OPENSTORY_NATS_URL` (default nats://localhost:4222), `OPENSTORY_DATA_BACKEND=sqlite`, `OPENSTORY_DATA_DIR`.
- Caveat: orchestrator taskId is `c282-wiki-agent-daily-run` (c282/c2a2 typo, baked in — join works; don't rename without migrating history).

## Per-slug completeness query (re-run to verify)
```
cd "$HOME/Documents/Non-Claude Projects/OpenStory"; python3 - <<'PY'
import sqlite3,re,glob,collections
db=glob.glob("./data/*.db")[0]; con=sqlite3.connect(db); cur=con.cursor()
rows=cur.execute("SELECT id,label,first_event,last_event,event_count FROM sessions").fetchall()
def slug(l):
    if not l: return "(empty)"
    m=re.search(r'name="([^"]+)"', l); return m.group(1) if m else "(interactive)"
agg={}; sid2={}
for sid,l,fe,le,ec in rows:
    s=slug(l); sid2[sid]=s; a=agg.setdefault(s,{"n":0,"ev":0,"f":"","t":""})
    a["n"]+=1; a["ev"]+=ec or 0
    if fe and(not a["f"] or fe<a["f"]):a["f"]=fe
    if le and(not a["t"] or le>a["t"]):a["t"]=le
for s,a in sorted(agg.items(),key=lambda x:-x[1]["n"]):
    print(f"{s[:42]:42}{a['n']:>5}{a['ev']:>8}  {a['f'][:10]}..{a['t'][:10]}")
print("slugs",len(agg),"sessions",sum(a['n'] for a in agg.values()))
PY
```

## Artifacts saved (this session, in outputs)
- `openstory_c2a2_agent_map.md`, `agent_map.json` — the canonical mapping (reviewed & approved by Tom).
- `HANDOFF_openstory_c2a2.md` — this note.
- In the OpenStory repo: `deploy/nats-local.conf`, `scripts/up-local.sh`, `~/Desktop/Launch OpenStory.command`.

## Working method note
This session drove Terminal via clipboard-paste (Terminal is tier-"click": no typing). Pattern: write command to clipboard (bring Finder forward first, since clipboard-write is blocked while Terminal is frontmost), Tom pastes + runs, then screenshot to read. A future session with a mounted folder or different access could be faster.
