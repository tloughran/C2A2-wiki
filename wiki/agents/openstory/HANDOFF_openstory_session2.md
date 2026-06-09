# Handoff 2 — OpenStory → C2A2 Agent Explorer

_Session 2, 2026-06-08. Supersedes HANDOFF_openstory_c2a2.md for current state. Resume fresh; this is the state + exact next steps._

## Done & verified this session
1. **Bridge built + proven.** `~/Documents/Non-Claude Projects/OpenStory/scripts/openstory-bridge.sh` symlinks Cowork + Claude Code transcripts into a flat `{project}/{session}.jsonl` root (OpenStory's `paths.rs` shape). Idempotent (first-wins, sorted, broken-link repair). Tested against synthetic fixtures (deep nesting, subagents, collisions, idempotency) AND real data: **1,508 symlinks linked**.
   - Real Cowork layout (handoff-1 was wrong about depth): `…/local-agent-mode-sessions/{uuid1}/{uuid2}/local_{id}/.claude/projects/{project}/{session}.jsonl`. Bridge finds `.claude/projects` at any depth.
2. **Capture verified climbs.** Grepping the bridged transcripts (escape-aware: on-disk label is JSON-escaped `<scheduled-task name=\"slug\" …>`; and use `find … | xargs grep`, NOT `grep -R` — BSD grep won't follow symlinks in recursion): **64 agent slugs / 1,069 labeled session-files**, vs 28 slugs / 381 sessions before. The 3 zero-capture thinker pairs now present: carroll-arkanihamed (10), stump-fredrickson (10), mcgilchrist-kastrup (9).
3. **Cutover attempted → root-caused → reverted.** Full backfill (`BACKFILL_HOURS=0`) over the bridge hit NATS `maximum payload exceeded: 13990589 vs 8388608`. Cowork transcripts have multi-MB events; watcher batches 100 events/publish (`watcher.rs BATCH_CHUNK_SIZE`), so batches reached ~14 MB.
   - **Fix applied:** `deploy/nats-local.conf` `max_payload: 8MB → 64MB`.
   - Key correction: publish errors are **non-fatal** — `server/mod.rs:395` logs `Bus publish error` and continues (no `?`). Oversized batches just drop events; they don't crash serve. Earlier "serve down" was my kill commands + early-init timing, not a crash.
4. **Recurring-cost fix (the important one).** serve re-reads byte offsets from memory only → every restart re-publishes all in-window events through NATS before… well, concurrently (watcher is `spawn_blocking`, HTTP binds immediately — `server/mod.rs:78-86, 387`). Cost ∝ events in window. Launcher now defaults to a **bounded 72h window** (`up-local.sh`), so restarts are constant-cost regardless of history growth. One-time seed overrides via env.
5. **Instance healthy.** `3002 UP, API 200`, serving 571 sessions. NATS :4222, UI :5173.

## Agreed architecture (the plan to finish)
Seed once → extractor reads the **DB** (keeps OpenStory-derived eval/apply + turns) → writes a per-slug×day **JSON snapshot into the vault** → `agents_tab.html` reads the JSON (decoupled from serve) → scheduled re-extract + live incremental ingest after first fill. Only thing a pure direct-transcript extractor would lose is eval/apply + turns; everything else (counts, durations, errors, narrative) is computable either way — so we route through OpenStory to keep eval/apply.

## Next steps (resume here)
1. **#8 — Agent-only bridge + one-time seed.**
   - Add `AGENTS_ONLY=1` mode to `openstory-bridge.sh`: link only files where `grep -q -m1 'scheduled-task name=' "$f"` matches, into a separate root `~/openstory-watch-agents`. (Caveat: subagent files lack the label — decide whether to also carry `/subagents/` for labeled parents; v1 can skip, ~49 dirs.) Smaller/cleaner/lower-risk than the full bridge.
   - Seed once: launch serve with `OPENSTORY_WATCH_ROOT=~/openstory-watch-agents OPEN_STORY_WATCH_BACKFILL_HOURS=0 bash scripts/up-local.sh` (API stays up; DB fills in background; 64 MB cap holds). Then set routine launcher watch to the agent bridge so new runs ingest live within the 72h window.
   - Verify with the per-slug query (below) against the DB — confirm the zero pairs now have DB rows.
2. **#5 — Extractor + tab generator.** `extract_openstory_agent_data.py`: read `data/open-story.db`, group sessions by agent slug × day-of-week, per-cell stats (sessions, events, tool-use, errors, duration, eval/apply ratio from `patterns`, short narrative); emit JSON into the vault. Then the `agents_tab.html` generator (subtab 3c of the community explorer) from that JSON. **C2A2 house rules:** regular strings not f-strings, `""" + json + """` concat, single braces, validate with `node --check` + `validate_html.py`; graceful fallback to authored narration. `agent_map.json` is source of truth.
3. **#7 — Scheduled re-extract.** Scheduled task: re-run bridge (link new sessions) + re-run extractor (refresh vault JSON). Confirm cadence with Tom.

## Key paths / facts
- OpenStory repo: `~/Documents/Non-Claude Projects/OpenStory` (quote the space). DB: `data/open-story.db` (idempotent ingest: `events.id` PK + `INSERT OR IGNORE`; `event_count = MAX(...)` on upsert — re-reads never inflate).
- Bridge root (full): `~/openstory-watch` (1,508 links). Planned agent root: `~/openstory-watch-agents`.
- Files changed this session: `scripts/openstory-bridge.sh` (new), `scripts/up-local.sh` (72h window + env overrides), `deploy/nats-local.conf` (64 MB).
- Map files (source of truth): `wiki/agents/openstory/agent_map.json` + `.md`.
- Working method: Terminal is tier-"click" (no typing); relay = write command to clipboard with Finder frontmost → Tom pastes+Enter → screenshot to read. The sandbox CANNOT see `~/Library/…` (Cowork store) — only `~/Documents` is mounted; so the bridge/seed must run on the real machine, but the DB + repo are readable/editable directly via the mount.

## Per-slug verify query (run against the DB after seeding)
```
cd "$HOME/Documents/Non-Claude Projects/OpenStory"; python3 - <<'PY'
import sqlite3,re,glob
db=glob.glob("./data/*.db")[0]; con=sqlite3.connect(db); cur=con.cursor()
rows=cur.execute("SELECT label,event_count FROM sessions").fetchall()
def slug(l):
    if not l: return "(none)"
    m=re.search(r'name="([^"]+)"', l); return m.group(1) if m else "(interactive)"
agg={}
for l,ec in rows:
    a=agg.setdefault(slug(l),[0,0]); a[0]+=1; a[1]+=ec or 0
for s,(n,ev) in sorted(agg.items(),key=lambda x:-x[1][0]): print(f"{s[:42]:42}{n:>5}{ev:>9}")
print("slugs",len(agg),"sessions",sum(v[0] for v in agg.values()))
PY
```
