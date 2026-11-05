#!/usr/bin/env python3
"""Build video/vault-life/data/vault_timeline.json: the dated facts the
vault-life video animates. Deterministic (Rule 5); every date comes from
git history, metabolism_data.json, signals_grown.json or the PRS files.

Run from the repo root:  python3 scripts/video/build_vault_timeline.py
"""
import json, re, subprocess, sys, collections, datetime, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
OUT = "video/vault-life/data/vault_timeline.json"

def group_of(path):
    p = path[len("wiki/"):] if path.startswith("wiki/") else path
    top = p.split("/")[0]
    if top == "traditions":
        parts = p.split("/")
        return "tradition:" + (parts[1] if len(parts) > 1 else "_")
    if top == "vault":
        if "/synthesis/" in p: return "summa:synthesis"
        if "/transcripts/" in p: return "summa:transcript"
        return "summa:other"
    if top in ("synthesis", "flags", "inbox", "agents", "architecture", "master",
               "community", "heartbeat", "voice_guide", "metabolism", "paper_responses",
               "commentary-explorer", "PETER", "deferred", "review", "c2a2-prs-3d",
               "c2a2-wiki-narration"):
        return top
    if p.endswith(".html"): return "interface"
    return "other"

# 1. first-add date of every tracked path under wiki/ (one git call, oldest first)
log = subprocess.run(
    ["git", "log", "--reverse", "--diff-filter=A", "--name-only",
     "--format=@@%ad", "--date=short", "--", "wiki"],
    capture_output=True, text=True, check=True).stdout
first_add = {}
date = None
for line in log.splitlines():
    if line.startswith("@@"):
        date = line[2:].strip(); continue
    line = line.strip()
    if not line or not date: continue
    if line.endswith((".md", ".html", ".json")) and line not in first_add:
        first_add[line] = date
files = [{"p": p, "d": d, "g": group_of(p)} for p, d in first_add.items()]
files.sort(key=lambda f: (f["d"], f["p"]))

# 2. agent lanes: runs per day
met = json.load(open("wiki/metabolism/metabolism_data.json"))
lanes = []
for l in met["lanes"]:
    days = collections.Counter(r["t"][:10] for r in l["rows"])
    lanes.append({"label": l["label"], "category": l["category"],
                  "thinkers": l.get("thinkers", []), "runs": l["runs"],
                  "days": dict(sorted(days.items()))})

# 3. cross-tradition signals (dated)
sig = json.load(open("prototypes/signals_grown.json"))
sig = sig if isinstance(sig, list) else sig.get("signals", [])
signals = [{"a": s["a"], "b": s["b"], "d": s["date"], "s": s.get("strength", "")}
           for s in sig if s.get("date")]
signals.sort(key=lambda s: s["d"])

# 4. PRS triplets: Date Added per tradition
prs = []
for t in sorted(os.listdir("wiki/traditions")):
    f = f"wiki/traditions/{t}/prs_triplets.md"
    if not os.path.isfile(f): continue
    cur = None
    for line in open(f, encoding="utf-8", errors="replace"):
        m = re.match(r"^\s*(PRS-\d+)\s*:", line)
        if m: cur = m.group(1); continue
        m = re.search(r"Date Added:\s*(\d{4}-\d{2}-\d{2})", line)
        if m and cur:
            prs.append({"t": t, "id": cur, "d": m.group(1)}); cur = None
prs.sort(key=lambda x: (x["d"], x["t"], x["id"]))

# 5. Summa: synthesis files by first-add date, with the Day number from the index
sidx = json.load(open("wiki/vault/refs/summa_index.json"))
day_of = {}
for k, v in sidx.items():
    syn = v.get("synthesis") or ""
    if syn and v.get("day"):
        day_of[os.path.basename(syn)[:12]] = int(v["day"])
summa_days = []
for f in files:
    if f["g"] == "summa:synthesis":
        key = os.path.basename(f["p"])[:12]
        summa_days.append({"d": f["d"], "day": day_of.get(key)})

# 6. AI Heartbeat: distinct captured items by first-seen date (snapshots kept since 2026-09)
import glob
hb = {}
def _take(sigs, fallback):
    for x in sigs:
        u = x.get("url") or x.get("title"); t = (x.get("first_seen_at") or fallback or "")[:10]
        if u and t and (u not in hb or t < hb[u]): hb[u] = t
for fn in sorted(glob.glob("wiki/heartbeat/data/snapshots/*.json")):
    try: d = json.load(open(fn))
    except Exception: continue
    _take(d.get("signals", []), d.get("generated_at"))
d = json.load(open("wiki/heartbeat/data/digest.json")); _take(d.get("signals", []), d.get("generated_at"))
heartbeat = sorted(hb.values())

# 7. Summa coverage per day number (articles + questions), so the shelf can count articles
day_articles = collections.defaultdict(set); day_questions = collections.defaultdict(set)
for k, v in sidx.items():
    if v.get("day") and str(v.get("available")) == "True":
        day_articles[int(v["day"])].add(k); day_questions[int(v["day"])].add(k.rsplit(".A", 1)[0])
summa_totals = {"articles": len(sidx), "questions": len({k.rsplit(".A", 1)[0] for k in sidx}),
                "articles_done": sum(len(x) for x in day_articles.values()),
                "questions_done": len(set().union(*day_questions.values())) if day_questions else 0}
for e in summa_days:
    e["articles"] = len(day_articles.get(e["day"], ())) if e["day"] else 0
    e["questions"] = sorted(day_questions.get(e["day"], ())) if e["day"] else []

out = {
    "_meta": {"generated": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
              "head": subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                     capture_output=True, text=True).stdout.strip(),
              "files": len(files), "lanes": len(lanes),
              "runs": sum(l["runs"] for l in lanes), "signals": len(signals),
              "prs": len(prs), "summa_synthesis": len(summa_days), "heartbeat_items": len(heartbeat),
              "first_file": files[0]["d"] if files else None,
              "last_file": files[-1]["d"] if files else None},
    "files": files, "lanes": lanes, "signals": signals, "prs": prs,
    "summa": summa_days, "summa_totals": summa_totals, "heartbeat": heartbeat,
    "yield_daily": met["yield_daily"],
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w"), separators=(",", ":"))
print(json.dumps(out["_meta"], indent=1))
print("groups:", collections.Counter(f["g"] for f in files).most_common(25))

# ---------------------------------------------------------------------------
# 8. The live page: wiki/metabolism/vault_life.html (Metabolism > Vault Life).
# Captions are the film's narration with every tally filled from the data
# above (Rule 5: code fills numbers), keyed to vault DATES so they stay in
# place as the clock extends. The chapter start dates are editorial choices.
# Set FILM_URL once the film is hosted; empty hides the link.
# ---------------------------------------------------------------------------
TEMPLATE = "wiki/metabolism/scripts/vault_life_template.html"
PAGE = "wiki/metabolism/vault_life.html"
FILM_URL = ""

def _n(x): return f"{x:,}"

_m = out["_meta"]
_three_weeks = "2026-04-28"
_prs_3wk = sum(1 for p in prs if p["d"] <= _three_weeks)
_lit = sum(1 for f in files if "lit_search_results" in f["p"])
_hb_first = heartbeat[0] if heartbeat else None
_st = summa_totals
_pct = round(100.0 * _st["articles_done"] / _st["articles"], 1) if _st.get("articles") else 0
_as_of = datetime.date.fromisoformat(_m["last_file"]).strftime("%B %-d, %Y")

captions = [
    {"start": "2026-04-06", "title": "C2A2",
     "text": f"This is C2A2. It's a vault. Fifteen thinker-traditions, {_m['lanes']} agents, and their curator have been building it since April 2026. Watch it grow, day by day."},
    {"start": "2026-04-07", "title": "1 · Thinkers arrive",
     "text": f"April seventh. Fifteen traditions come into being at once. Each gets a wiki, and an agent that answers for it. Within three weeks those agents have written {_n(_prs_3wk)} problem-resource-solution triplets: what each program asks, what it brings, what it has settled. {_n(_m['prs'])} to date."},
    {"start": _three_weeks, "title": "2 · Assessment",
     "text": f"The hive wakes up. Every morning the daily run reads what came in overnight and proposes cards for review; a human says yes or no. Thinker-pair agents notice when one program's question is another's answer: those flashes are cross-tradition signals, dated and justified, {_n(_m['signals'])} to date. The gold rail is the Summa commentary, Aquinas read alongside today's science, paced with Austin Habash's Summa in a Year: {_n(_st['articles_done'])} of {_n(_st['articles'])} articles, {_pct}%."},
    {"start": "2026-06-21", "title": "3 · Research",
     "text": f"Summer is for research. The outer ring fills with literature search, {_n(_lit)} files testing the system's own assumptions against the published record, for and against. On the left, the AI Heartbeat watches AI developments: {_n(_m['heartbeat_items'])} items captured since {_hb_first or 'its snapshots began'}. The sewing agent writes bridge essays wherever two traditions touch. Every dot is a document you can open."},
    {"start": "2026-09-01", "title": "4 · Ways in",
     "text": "One search box, the same on every page. Type a name and the graph cuts to it. Ask a question and the answer is grounded in the model, the bridge essays, the triplets, the signals. Or talk to it: the voice guide runs the same commands. Plots can be built live and clicked back into the graph."},
    {"start": "2026-10-01", "title": "5 · Fruits",
     "text": "What comes out: the Summa commentary, complete and published. Responses to papers, written from fifteen traditions and mailed to their authors. A commentary on Magnifica Humanitas in construction. And a record of every decision that shaped the vault, public on purpose."},
    {"start": _m["last_file"], "title": "Today",
     "text": f"As of {_as_of}: {_n(_m['files'])} files, {_n(_m['runs'])} agent runs, {_n(_m['prs'])} triplets, {_n(_m['signals'])} signals. All of it in the open at tinyurl.com/C2A2explorer. The accelerator is running."},
]

def _js(obj):
    return json.dumps(obj, separators=(",", ":")).replace("</", "<\\/")

if os.path.isfile(TEMPLATE):
    tpl = open(TEMPLATE, encoding="utf-8").read()
    for marker in ("/*__DATA__*/", "/*__CAPTIONS__*/", "/*__FILM_URL__*/"):
        if tpl.count(marker) != 1:
            sys.exit(f"ERROR: template must contain {marker} exactly once")
    page = (tpl.replace("/*__DATA__*/", _js(out))
               .replace("/*__CAPTIONS__*/", _js(captions))
               .replace("/*__FILM_URL__*/", _js(FILM_URL)))
    open(PAGE, "w", encoding="utf-8").write(page)
    print("page:", PAGE, len(page), "bytes;", len(captions), "captions")
else:
    sys.stderr.write(f"WARN: {TEMPLATE} not found; page not written\n")
