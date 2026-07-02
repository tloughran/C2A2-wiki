#!/usr/bin/env python3
"""
probe_substrate.py - read-only legibility map of the OpenStory data substrate.

Idempotent by construction: it opens a STATIC snapshot of open-story.db
read-only (mode=ro&immutable=1) and writes a markdown report. Run it as often
as you like, against any snapshot, on any machine. It never touches the live DB.

Make a fresh snapshot first (safe while the backend runs - online-backup API):
    SRC="$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story.db"
    DST="$HOME/Documents/Non-Claude Projects/OpenStory/data/open-story-snapshot.db"
    sqlite3 "$SRC" ".backup '$DST'"

Then:
    python3 probe_substrate.py [snapshot.db] [report.md]

Defaults read the snapshot beside the live DB and write legibility_report.md
next to this script. Designed so a researcher from any field can regenerate the
map as the corpus grows, or extend it with their own questions.
"""
import sqlite3, json, sys, os, datetime
from collections import Counter

DEFAULT_DB = os.path.expanduser(
    "~/Documents/Non-Claude Projects/OpenStory/data/open-story-snapshot.db")
DEFAULT_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "legibility_report.md")

def main():
    db = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DB
    out = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT
    if not os.path.exists(db):
        sys.exit(f"snapshot not found: {db}\nMake one with sqlite3 .backup (see header).")

    c = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    q = lambda s, *a: c.execute(s, a).fetchall()
    one = lambda s, *a: c.execute(s, a).fetchone()
    has = lambda t: bool(one("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", t))

    L = []  # report lines
    p = L.append
    p(f"# OpenStory Substrate - Legibility Map")
    p(f"\n_Generated {datetime.datetime.now():%Y-%m-%d %H:%M} from a read-only snapshot._")
    p(f"\n_Snapshot: `{os.path.basename(db)}`_\n")

    # ---- 1. The layered model ----
    p("## 1. The model: one immutable log, many regenerable folds\n")
    p("Everything here is either the **`events`** log (the immutable substrate) or a "
      "**fold** over it (`turns`, `patterns`). The recrystallize replay proved any fold "
      "can be deterministically rebuilt from the log - so every analysis below, and every "
      "future one, is a re-runnable projection, never a baked-in artifact.\n")

    # ---- 2. Inventory / the alphabet ----
    p("## 2. Inventory and the event alphabet\n")
    counts = {n: one('SELECT COUNT(*) FROM "%s"' % n)[0]
              for (n,) in q("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")}
    for t in ("events", "turns", "patterns", "sessions", "plans"):
        if t in counts:
            p(f"- **{t}**: {counts[t]:,}")
    ev_span = one("SELECT MIN(timestamp),MAX(timestamp) FROM events")
    p(f"- **span**: {ev_span[0]} -> {ev_span[1]}")
    p(f"- **distinct hosts / users**: "
      f"{one('SELECT COUNT(DISTINCT host) FROM sessions')[0]} / "
      f"{one('SELECT COUNT(DISTINCT user) FROM sessions')[0]} "
      f"(this corpus is one human across many agent sessions/projects)\n")
    p("\nEvent subtypes (the alphabet the substrate is written in):\n")
    p("| subtype | count |\n|---|---:|")
    for st, ct in q("SELECT subtype, COUNT(*) c FROM events GROUP BY subtype ORDER BY c DESC"):
        p(f"| `{st}` | {ct:,} |")

    # ---- 3. What a turn IS ----
    p("\n## 3. What a 'turn' actually is\n")
    keys = set()
    for (d,) in q("SELECT data FROM turns LIMIT 2000"):
        try: keys |= set(json.loads(d).keys())
        except Exception: pass
    p("A `turn` is one boundary-delimited beat of the working loop, and the row carries "
      "**content, not just counts**. Fields present in `turns.data`:\n")
    p("`" + "`, `".join(sorted(keys)) + "`\n")
    p("The load-bearing point: `human` (the prompt), `thinking`, and `eval` (the response) "
      "are all in the same row as `applies`, `stop_reason`, `scope_depth`, `duration_ms`. "
      "So the substrate is a **content-bearing dialogue record**, not mere activity telemetry.\n")
    # an expanded example
    ex = None
    for sid, tn, d in q("SELECT session_id,turn_number,data FROM turns ORDER BY turn_number"):
        j = json.loads(d)
        if isinstance(j.get("applies"), list) and 2 <= len(j["applies"]) <= 5 \
           and j.get("human", {}).get("content"):
            ex = (sid, tn, j); break
    if ex:
        sid, tn, j = ex
        hc = (j.get("human") or {}).get("content", "")[:300]
        ec = (j.get("eval") or {}).get("content", "")[:300]
        p(f"**Example** (session `{sid[:12]}`, turn {tn}, {len(j.get('applies') or [])} applies, "
          f"stop_reason=`{j.get('stop_reason')}`):\n")
        p(f"> **human:** {hc.strip()}...\n")
        p(f"> **eval:** {ec.strip()}...\n")

    # ---- 4. Data-health: alive / thin / frozen ----
    p("## 4. Data health - what is alive, thin, or frozen\n")
    p("| signal | count | last seen | status |\n|---|---:|---|---|")
    def row(label, count, last, status):
        p(f"| {label} | {count:,} | {last or '-'} | {status} |")
    row("events (substrate)", counts.get("events", 0), ev_span[1], "ALIVE")
    pat = {ty: (ct, mx) for ty, ct, mx in
           q("SELECT type,COUNT(*),MAX(start_time) FROM patterns GROUP BY type")}
    e = pat.get("eval_apply.eval", (0, None)); a = pat.get("eval_apply.apply", (0, None))
    row("eval_apply.eval", e[0], e[1], "ALIVE - core deliberation signal")
    row("eval_apply.apply", a[0], a[1], "ALIVE - core action signal")
    trow = one("SELECT COUNT(*),MAX(timestamp) FROM turns")
    row("turns table", trow[0], trow[1], "ALIVE - content-rich, full history")
    for k, note in [("turn.sentence", "thin - explicit boundaries only"),
                    ("eval_apply.turn_end", "thin - explicit boundaries only"),
                    ("eval_apply.scope_open", "FROZEN - Apr drift, not recovered"),
                    ("eval_apply.scope_close", "FROZEN - Apr drift, not recovered"),
                    ("turn.phase", "FROZEN - Apr drift, not recovered"),
                    ("error.recovery", "FROZEN - Apr drift, not recovered"),
                    ("agent.delegation", "FROZEN - Apr drift, not recovered")]:
        ct, mx = pat.get(k, (0, None)); row(k, ct, mx, note)
    if a[0]:
        p(f"\n**eval:apply ratio = {e[0]/a[0]:.2f}** (slightly more deliberation than action, full history).\n")

    # ---- 5. Coverage and skew ----
    p("## 5. Turn coverage and skew\n")
    tot = counts.get("sessions", 0)
    wt = one("SELECT COUNT(DISTINCT session_id) FROM turns")[0]
    wp = one("SELECT COUNT(DISTINCT session_id) FROM events WHERE subtype='message.user.prompt'")[0]
    gap = one("SELECT COUNT(*) FROM (SELECT DISTINCT session_id FROM events "
              "WHERE subtype='message.user.prompt' EXCEPT SELECT DISTINCT session_id FROM turns)")[0]
    tps = sorted(r[0] for r in q("SELECT COUNT(*) FROM turns GROUP BY session_id"))
    p(f"- sessions total: **{tot:,}**; with >=1 turn: **{wt}**; with >=1 human prompt: **{wp}**")
    p(f"- sessions that have prompts but **no** crystallized turns: **{gap}** (a coverage gap, not empty noise)")
    if tps:
        p(f"- turns/session: median **{tps[len(tps)//2]}**, max **{max(tps):,}** (one session dominates) - heavily skewed\n")
    # monthly recovery
    p("\nTurns by month (the freeze and its recovery, in numbers):\n")
    p("| month | turns |\n|---|---:|")
    for ym, ct in q("SELECT substr(timestamp,1,7) ym, COUNT(*) FROM turns GROUP BY ym ORDER BY ym"):
        p(f"| {ym} | {ct:,} |")

    # ---- 6. Human/AI structure & AI-to-AI ----
    p("\n## 6. Human/AI structure\n")
    bal = {s: one("SELECT COUNT(*) FROM events WHERE subtype=?", s)[0] for s in
           ("message.user.prompt", "message.assistant.text", "message.assistant.thinking",
            "message.assistant.tool_use", "message.user.tool_result", "system.turn.complete")}
    for k, v in bal.items():
        p(f"- `{k}`: {v:,}")
    agid = one("SELECT COUNT(*) FROM sessions WHERE id LIKE 'agent-%'")[0]
    oa = one("SELECT COUNT(*) FROM sessions WHERE origin_agent IS NOT NULL")[0]
    isag = 0
    for (d,) in q("SELECT data FROM turns"):
        try:
            if json.loads(d).get("is_agent"): isag += 1
        except Exception: pass
    p(f"\n- **AI-to-AI is capturable now via lineage**: {agid} `agent-*` sessions, "
      f"`origin_agent` set on {oa}/{tot}. The per-turn `is_agent` flag, by contrast, is "
      f"**{isag}/{trow[0]}** - dead. So agent-to-agent structure lives at the session level, not the flag.\n")
    # content presence
    h = th = ec = n = 0
    for (d,) in q("SELECT data FROM turns"):
        try: j = json.loads(d)
        except Exception: continue
        n += 1
        h += bool((j.get("human") or {}).get("content"))
        th += bool(j.get("thinking"))
        ec += bool((j.get("eval") or {}).get("content"))
    p(f"- of {n:,} turns: **{h:,}** carry the human prompt, **{th:,}** carry AI thinking, "
      f"**{ec:,}** carry the AI response - the relational raw material is already present.\n")

    # ---- 7. Reading: what we have / what we might have ----
    p("## 7. Reading the map\n")
    p("**What we have, robustly:** the event substrate (full alphabet), the eval/apply "
      "cognitive rhythm (full history), and a content-bearing `turns` table spanning "
      "Mar-Jun with the human prompt + AI thinking + AI response in ~75-80% of rows. "
      "Listening/relationship folds can be built directly on `turns.data` - no dependency "
      "on new OpenStory instrumentation.\n")
    p("**What is thin or dark:** the turn-boundary patterns (`turn.sentence`/`turn_end`) "
      "fire only on explicit boundaries (~880), and four detectors "
      "(`scope_*`, `turn.phase`, `error.recovery`, `agent.delegation`) went dark at the "
      "same Apr-7/8 format drift and the replay did **not** revive them - a separate, "
      "still-open signal gap.\n")
    p("**Two questions for OpenStory:** (a) which dropped Claude Code signals fed those "
      "four dark detectors, and can they be re-derived? (b) why do 807 prompt-bearing "
      "sessions crystallize no turns - a fold-coverage gap worth closing before we measure "
      "on top of it.\n")

    with open(out, "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"wrote {out} ({len(L)} lines) from {os.path.basename(db)}")

if __name__ == "__main__":
    main()
