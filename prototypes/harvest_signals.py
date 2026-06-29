#!/usr/bin/env python3
"""Harvest cross-tradition signals already authored in approved cards'
'## Cross-Tradition Signals' sections. Deterministic (Rule 5: code answers).
Model extraction is reserved only for lines that don't map to the roster — those
are flagged, not silently dropped (Rule 12).

Formation-activity date = proposal date (when the agent registered the link).
Source-material date     = card source_date (for the dual-encoding overlay).

Usage: harvest_signals.py <manifest.json> <vault> <existing_signals.json> <out_dir>
Outputs: signals_grown.json (existing + harvested), qc_trace.csv (filled), coverage summary.
"""
import json, re, os, sys, csv, datetime, itertools
from collections import Counter

manifest_p, vault, existing_p, outdir = sys.argv[1:5]
TODAY = datetime.date.today().isoformat()
manifest = json.load(open(manifest_p))
existing = json.load(open(existing_p)) if os.path.exists(existing_p) else []

ROSTER = {"arkanihamed":"Arkani-Hamed","carroll":"Carroll","fredrickson":"Fredrickson",
 "friston":"Friston","hawkins":"Hawkins","hoffman":"Hoffman","kastrup":"Kastrup",
 "levin":"Levin","loughran":"Loughran","macintyre":"MacIntyre","mcgilchrist":"McGilchrist",
 "rohr":"Rohr","stump":"Stump","wolfram":"Wolfram","wright":"Wright"}
# non-thinker targets that legitimately appear; recorded as flags, not pairs
NONTRAD = {"c2a2","master","summa","paradigm","paradigmflags","c282","karpathy","aquinas","habash"}

def canon(name):
    k = re.sub(r"\bagents?\b","",name.strip().lower()).strip()
    k = k.replace(" ","").replace(".","").replace("-","")
    if k in ROSTER: return ROSTER[k]
    for rk in ROSTER:
        if rk in k: return ROSTER[rk]
    return None
def is_nontrad(name):
    k = name.strip().lower().replace(" ","").replace("-","")
    return any(t in k for t in NONTRAD)

def strength(note):
    n = (note or "").lower()
    if "very strong" in n: return "High"
    if "strong" in n: return "Strong"
    if "moderate" in n or "medium" in n: return "Moderate"
    if "weak" in n or "speculative" in n or "tentative" in n: return "Speculative"
    return "Unlabeled"
WEIGHT = {"High":3.0,"Strong":2.5,"Moderate":2.0,"Speculative":1.0,"Unlabeled":1.5}

# bullet with bold label: - **Label (note):** body
LINE = re.compile(r"^\s*[-*]\s*\*\*([^*]+?)\*\*\s*[:：]?\s*(.*)$")
# bullet with plain label: - Friston: body   (label = text before first colon)
LINE_PLAIN = re.compile(r"^\s*[-*]\s*([A-Z][A-Za-z][A-Za-z /&.-]{0,40}?)\s*[:：]\s*(.+)$")
# prose mention fallback: **Name** inside a paragraph
BOLD = re.compile(r"\*\*([^*]+?)\*\*")
PAREN = re.compile(r"\(([^)]*)\)")

def proposal_date(fname):
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", os.path.basename(fname))
    return m.group(1) if m else None

harvested, qc_rows = [], []
flagged_targets = Counter()
seen = set((s["a"], s["b"], s.get("card","")) for s in existing)

for r in manifest:
    path = os.path.join(vault, r["file"])
    txt = open(path, errors="ignore").read()
    fm = txt.split("---")[1] if txt.startswith("---") else txt[:600]
    pid = (re.search(r"proposal_id:\s*(PROP-[0-9A-Za-z-]+)", fm) or [None, r["card"]])[1] \
          if re.search(r"proposal_id:\s*", fm) else r["card"]
    trad_key = (re.search(r"tradition_key:\s*(\w+)", fm) or [None, r["tradition"]])[1] \
               if re.search(r"tradition_key:\s*", fm) else r["tradition"]
    home = ROSTER.get(trad_key, trad_key.title())
    sdate = r.get("source_date","")
    pdate = proposal_date(r["file"]) or sdate
    sec = re.search(r"##+\s*Cross-?Tradition Signals(.*?)(?=\n##\s|\Z)", txt, re.S | re.I)
    n_emit, flags = 0, []
    def emit_from(label, body, mode="bullet"):
        c = 0
        note = PAREN.search(label)
        strpart = note.group(1) if note else ""
        label_clean = PAREN.sub("", label)
        parts = re.split(r"\s*[/,&]\s*|\s+and\s+", label_clean)  # "Levin / Hoffman"
        for p in parts:
            p = p.strip()
            if not p: continue
            to = canon(p)
            if to and to != home:
                st = strength(strpart + " " + body)
                a, b = sorted([home, to])
                key = (a, b, pid)
                if key in seen: continue
                seen.add(key)
                nat = (strpart.strip() or ("prose mention" if mode=="prose" else "card resonance"))[:60]
                harvested.append({"a":a,"b":b,"date":pdate,"source_date":sdate,
                    "strength":st,"weight":WEIGHT[st],"nature":nat,
                    "source":"card","sid":pid,"card":pid,
                    "text":(p+": "+body).strip()[:400],"action":""})
                c += 1
            elif is_nontrad(p):
                flagged_targets[p.lower().strip()] += 1; flags.append(p.strip())
            elif p and not to and mode=="bullet":
                flagged_targets[p.lower().strip()] += 1; flags.append(p.strip())
        return c
    if sec:
        body_text = sec.group(1)
        for line in body_text.splitlines():
            m = LINE.match(line)                       # - **Label**: body
            if m: n_emit += emit_from(m.group(1), m.group(2)); continue
            m = LINE_PLAIN.match(line)                 # - Friston: body
            if m and canon(PAREN.sub("", m.group(1))): n_emit += emit_from(m.group(1), m.group(2))
        if n_emit == 0:                                # prose fallback: **Name** in paragraphs
            for sent in re.split(r"(?<=[.!?])\s+", body_text):
                for nm in BOLD.findall(sent):
                    if canon(PAREN.sub("", nm)): n_emit += emit_from(nm, sent, mode="prose")
    status = "pass" if (n_emit > 0 and not flags) else ("flag" if (n_emit>0 or flags) else "EMPTY")
    qc_rows.append({"card":pid,"tradition":trad_key,"source_date":sdate,"proposal_date":pdate,
        "processed_by":"harvester","date_processed":TODAY,"signals_emitted":n_emit,
        "nontrad_or_unmapped":"; ".join(sorted(set(flags)))[:120],
        "status":status,"notes":""})

# ---- write grown dataset (existing card/finding/index layers + harvested) ----
grown = existing + harvested
# add source_date to existing records that lack it (so viz overlay is uniform)
for s in grown:
    s.setdefault("source_date", s.get("date",""))
grown = [s for s in grown if s.get("date")]
grown.sort(key=lambda s: s["date"])
json.dump(grown, open(os.path.join(outdir,"signals_grown.json"),"w"), indent=1)

# ---- qc_trace.csv ----
with open(os.path.join(outdir,"qc_trace.csv"),"w",newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(qc_rows[0].keys())); w.writeheader()
    for row in qc_rows: w.writerow(row)

# ---- coverage gate (Rule 12) ----
covered = len(qc_rows)
expected = len(manifest)
empty = [q["card"] for q in qc_rows if q["status"]=="EMPTY"]
flag = [q["card"] for q in qc_rows if q["status"]=="flag"]
print("=== COVERAGE GATE ===")
print(f"cards in manifest: {expected}")
print(f"cards with a qc_trace row: {covered}")
print(f"GATE: {'PASS' if covered==expected else 'FAIL'} ({covered}/{expected})")
print(f"cards emitting >=1 signal: {sum(1 for q in qc_rows if q['signals_emitted']>0)}")
print(f"cards EMPTY (no parseable signal — need model/manual): {len(empty)} {empty[:8]}")
print(f"cards flagged (some non-roster/unmapped targets): {len(flag)}")
print()
print("=== HARVEST ===")
print(f"signals harvested: {len(harvested)}  (added to existing {len(existing)} -> {len(grown)})")
mc = Counter(s["date"][:7] for s in harvested)
print("harvested by PROPOSAL month (formation axis):", dict(sorted(mc.items())))
sc = Counter((s.get("source_date") or '')[:7] for s in harvested)
print("harvested by SOURCE month (overlay):", dict(sorted(x for x in sc.items() if x[0])))
print("top non-roster/unmapped targets (flagged, not dropped):", dict(flagged_targets.most_common(8)))
pairs = Counter((s["a"],s["b"]) for s in grown)
print("top pairs in grown set:", [f'{a}~{b}:{n}' for (a,b),n in pairs.most_common(6)])
