#!/usr/bin/env python3
"""Track A QC / dedup report — flags what needs human judgment before apply_prs.py.

For every staged triplet (per tradition), reports:
  - PRS-N, Confidence, Problem (truncated)
  - best-matching EXISTING triplet in traditions/<trad>/prs_triplets.md + score
    (normalized token Jaccard over Problem+Solution)
  - flags: DUP? (score >= --thresh), VACUOUS? (no-net-new / citation-only phrasing),
    PROV? (staged Source does not cite the unit proposal_id)

Deterministic, no model calls. Operator reads this, decides --drop for apply_prs.py.

Usage: python3 qc_prs.py <vault> <manifest.json> <staging_dir> [--tradition T] [--thresh 0.55]
"""
import sys, os, re, json, glob, argparse

STOP = set("the a an of to and or in on for with as is are be that this it its by not "
           "no new we you your they their them from at which what how why into can may "
           "than then but so if all any each per via within without across over under".split())

def toks(s):
    return set(w for w in re.findall(r'[a-z0-9]+', s.lower()) if len(w) > 2 and w not in STOP)

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def existing_triplets(path):
    """Return [(prs_n, problem+solution text)] from a live tradition file."""
    txt = open(path, errors="ignore").read()
    out, cur_n, cur = [], None, []
    for ln in txt.split("\n"):
        m = re.match(r'^PRS-(\d+):', ln)
        if m:
            if cur_n: out.append((cur_n, " ".join(cur)))
            cur_n, cur = "PRS-" + m.group(1), []
        elif re.match(r'^\s*(Problem|Solution):', ln):
            cur.append(re.sub(r'^\s*(Problem|Solution):\s*', '', ln))
    if cur_n: out.append((cur_n, " ".join(cur)))
    return out

def staged_triplets(path):
    lines = open(path, errors="ignore").read().splitlines()
    i = 0
    while i < len(lines) and not re.match(r'^PRS-\d+:', lines[i]): i += 1
    out, cur_n, prob, sol, conf, src = [], None, "", "", "", ""
    def flush():
        if cur_n: out.append(dict(n=cur_n, problem=prob, sol=sol, conf=conf, src=src))
    for ln in lines[i:]:
        m = re.match(r'^PRS-(\d+):', ln)
        if m:
            flush(); cur_n = "PRS-" + m.group(1); prob = sol = conf = src = ""
        elif ln.strip().startswith("Problem:"): prob = ln.split("Problem:",1)[1].strip()
        elif ln.strip().startswith("Solution:"): sol = ln.split("Solution:",1)[1].strip()
        elif ln.strip().startswith("Confidence:"): conf = ln.split("Confidence:",1)[1].strip()
        elif ln.strip().startswith("Source:"): src = ln.split("Source:",1)[1].strip()
    flush()
    return out

VACU = re.compile(r'no new triplet|citation of record|upgrade the citation|'
                  r'no substantively-new|no net-new|placeholder', re.I)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault"); ap.add_argument("manifest"); ap.add_argument("staging")
    ap.add_argument("--tradition"); ap.add_argument("--thresh", type=float, default=0.55)
    a = ap.parse_args()
    units = json.load(open(a.manifest))
    flagged = 0
    for u in sorted(units, key=lambda x: (x["tradition"], x["unit_id"])):
        trad, uid = u["tradition"], u["unit_id"]
        if a.tradition and trad != a.tradition: continue
        sp = os.path.join(a.staging, "%s__%s.txt" % (trad, uid))
        if not os.path.exists(sp): continue
        st = staged_triplets(sp)
        if not st:
            print("[%s] %s  (0 candidates -> nothing to stage)" % (trad, uid)); continue
        ex = existing_triplets(os.path.join(a.vault, "traditions", trad, "prs_triplets.md"))
        print("\n[%s] %s  (%d staged)" % (trad, uid, len(st)))
        for t in st:
            tt = toks(t["problem"] + " " + t["sol"])
            best_n, best = "", 0.0
            for en, etx in ex:
                s = jaccard(tt, toks(etx))
                if s > best: best, best_n = s, en
            fl = []
            if best >= a.thresh: fl.append("DUP~%s(%.2f)" % (best_n, best))
            if VACU.search(t["problem"] + " " + t["sol"]): fl.append("VACUOUS")
            if uid.split("-SUPP")[0] not in t["src"] and uid not in t["src"]: fl.append("PROV")
            if fl: flagged += 1
            print("   %-7s %-11s %s | %s" % (t["n"], t["conf"],
                  " ".join(fl) if fl else "ok", t["problem"][:88]))
    print("\nTOTAL FLAGGED (need judgment):", flagged)

if __name__ == "__main__":
    main()
