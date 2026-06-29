#!/usr/bin/env python3
"""Extract dated cross-tradition signals from the C2A2 review-card layer.
Sources (living, structured):
  - flags/pattern_detector_findings.md   (FINDING-NNN: dated, Programs pair, Confidence, Eval type, Action)
  - master/cross_program_index.md        (CROSS-NNN: Programs (>=2), Nature, First appeared, Status)
  - flags/cross_signals_2026-04-16_batch1.md  (per-card **Other (strength):** with PROP backref)
  - flags/cross_signals_2026-04-16_batch2.md  (### From <Other> + bullets with [PROP-id])
Output: signals.json  (one record per unordered tradition pair occurrence).
"""
import json, re, sys, itertools, os

VAULT = sys.argv[1] if len(sys.argv) > 1 else "."

CANON = {
    "levin":"Levin","friston":"Friston","hoffman":"Hoffman","hawkins":"Hawkins",
    "mcgilchrist":"McGilchrist","fredrickson":"Fredrickson","stump":"Stump",
    "carroll":"Carroll","arkanihamed":"Arkani-Hamed","arkani-hamed":"Arkani-Hamed",
    "wolfram":"Wolfram","kastrup":"Kastrup","rohr":"Rohr","wright":"Wright","loughran":"Loughran",
}
DROP = {"c2a2","master","karpathy","c282"}  # not tradition nodes

def canon(name):
    k = name.strip().lower().replace(" agent","").replace("agent","").strip()
    k = k.replace(" ","").replace(".","")
    if k in DROP: return None
    # try direct and de-hyphenated
    if k in CANON: return CANON[k]
    k2 = k.replace("-","")
    if k2 in CANON: return CANON[k2]
    return None

def strength_to_weight(s):
    s = s.lower()
    if "very strong" in s or s.startswith("high"): return 3.0
    if "strong" in s or "medium-high" in s: return 2.5
    if "moderate" in s or s.startswith("medium"): return 2.0
    if "speculative" in s or "weak" in s or "low" in s: return 1.0
    return 2.0

def strength_label(s):
    s = s.lower()
    if "very strong" in s or s.startswith("high"): return "High"
    if "strong" in s or "medium-high" in s: return "Strong"
    if "moderate" in s or s.startswith("medium"): return "Moderate"
    if "speculative" in s or "weak" in s or "low" in s: return "Speculative"
    return "Moderate"

def prop_date(prop):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", prop or "")
    return m.group(0) if m else None

signals = []

def add(a, b, date, strength, nature, source, sid, text, action=""):
    ca, cb = canon(a), canon(b)
    if not ca or not cb or ca == cb: return
    pair = tuple(sorted([ca, cb]))
    signals.append({
        "a": pair[0], "b": pair[1], "date": date,
        "strength": strength_label(strength), "weight": strength_to_weight(strength),
        "nature": nature.strip() if nature else "", "source": source, "sid": sid,
        "card": (sid if sid and sid.startswith("PROP") else ""),
        "text": (text or "").strip()[:400], "action": action.strip(),
    })

# ---------- pattern_detector_findings.md ----------
fp = os.path.join(VAULT, "flags/pattern_detector_findings.md")
txt = open(fp, encoding="utf-8").read()
for blk in re.split(r"\nFINDING-\d+:", txt):
    if "Programs:" not in blk: continue
    progs = re.search(r"Programs:\s*(.+)", blk)
    if not progs or "[list]" in progs.group(1): continue
    names = [p for p in re.split(r"[,]", progs.group(1)) if p.strip()]
    date = (re.search(r"Date evaluated:\s*([0-9-]+)", blk) or [None,None])[1] if re.search(r"Date evaluated:\s*([0-9-]+)", blk) else None
    conf = (re.search(r"Confidence:\s*(.+)", blk) or [None,""])[1] if re.search(r"Confidence:\s*(.+)", blk) else ""
    nature = (re.search(r"Evaluation type:\s*(.+)", blk) or [None,""])[1] if re.search(r"Evaluation type:\s*(.+)", blk) else ""
    action = (re.search(r"Recommended action:\s*(.+)", blk) or [None,""])[1] if re.search(r"Recommended action:\s*(.+)", blk) else ""
    finding = (re.search(r"Finding:\s*(.+)", blk) or [None,""])[1] if re.search(r"Finding:\s*(.+)", blk) else ""
    sidm = re.search(r"Source candidate:\s*(.+)", blk)
    sid = sidm.group(1).strip() if sidm else ""
    for x, y in itertools.combinations(names, 2):
        add(x, y, date, conf, nature.split("—")[0] if "—" in nature else nature, "finding", sid, finding, action)

# ---------- cross_program_index.md ----------
fp = os.path.join(VAULT, "master/cross_program_index.md")
txt = open(fp, encoding="utf-8").read()
for blk in re.split(r"\nCROSS-\d+:", txt):
    if "Programs involved:" not in blk: continue
    progs = re.search(r"Programs involved:\s*(.+)", blk)
    if not progs or "[list" in progs.group(1): continue
    names = [p for p in re.split(r"[,]", progs.group(1)) if p.strip()]
    date = (re.search(r"First appeared:\s*([0-9-]+)", blk) or [None,None])[1] if re.search(r"First appeared:\s*([0-9-]+)", blk) else None
    nature = (re.search(r"Nature of connection:\s*(.+)", blk) or [None,""])[1] if re.search(r"Nature of connection:\s*(.+)", blk) else ""
    insight = (re.search(r"Question/Insight:\s*(.+)", blk) or [None,""])[1] if re.search(r"Question/Insight:\s*(.+)", blk) else ""
    status = (re.search(r"Status:\s*(.+)", blk) or [None,""])[1] if re.search(r"Status:\s*(.+)", blk) else ""
    for x, y in itertools.combinations(names, 2):
        add(x, y, date, "Moderate", nature, "index", "", insight, status)

# ---------- batch1: ## <Trad> Tradition Cross-Signals / ### PROP / **Other (strength):** ----------
fp = os.path.join(VAULT, "flags/cross_signals_2026-04-16_batch1.md")
txt = open(fp, encoding="utf-8").read()
cur_trad = None; cur_prop = None
for line in txt.splitlines():
    m = re.match(r"##\s+(\w[\w-]*)\s+Tradition Cross-Signals", line)
    if m: cur_trad = m.group(1); continue
    m = re.match(r"###\s+(PROP-[0-9A-Za-z-]+)", line)
    if m: cur_prop = m.group(1); continue
    m = re.match(r"\*\*([A-Za-z-]+)\s*\(([^)]+)\):\*\*\s*(.*)", line)
    if m and cur_trad:
        other, strength, text = m.group(1), m.group(2), m.group(3)
        add(cur_trad, other, prop_date(cur_prop) or "2026-04-16", strength, "card resonance", "card", cur_prop, text)

# ---------- batch2: ## <TRAD> / ### From <Other> / - **STRONG: ...** — text [PROP-id] ----------
fp = os.path.join(VAULT, "flags/cross_signals_2026-04-16_batch2.md")
txt = open(fp, encoding="utf-8").read()
cur_trad = None; cur_from = None
for line in txt.splitlines():
    m = re.match(r"##\s+([A-Z][A-Za-z-]+)\b", line)
    if m and "Overview" not in line: cur_trad = m.group(1); continue
    m = re.match(r"###\s+From\s+([A-Za-z-]+)", line)
    if m: cur_from = m.group(1); continue
    m = re.match(r"-\s*\*\*([A-Z ]+):\s*(.+?)\*\*\s*[—-]+\s*(.*)", line)
    if m and cur_trad and cur_from:
        strength, title, rest = m.group(1), m.group(2), m.group(3)
        prop = re.search(r"\[(PROP-[0-9A-Za-z-]+)\]", line)
        pid = prop.group(1) if prop else None
        add(cur_trad, cur_from, prop_date(pid) or "2026-04-16", strength, "card resonance", "card", pid, title + " — " + rest)

# ---------- summary ----------
signals = [s for s in signals if s["date"]]
signals.sort(key=lambda s: s["date"])
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "signals.json")
json.dump(signals, open(out, "w"), indent=1)

from collections import Counter
pairs = Counter((s["a"], s["b"]) for s in signals)
bysrc = Counter(s["source"] for s in signals)
print("total signals:", len(signals))
print("by source:", dict(bysrc))
print("distinct tradition pairs:", len(pairs))
print("top 12 pairs:")
for (a,b),n in pairs.most_common(12): print(f"   {a:14s} {b:14s} {n}")
print("date span:", signals[0]["date"], "->", signals[-1]["date"])
print("with source card:", sum(1 for s in signals if s["card"]))
print("wrote", out)
