#!/usr/bin/env python3
"""
sim_analyze.py - run Rungs 1 & 2 over a panel of simulated transcripts and report the
pre-registered contrasts (sim_preregistration.md P1-P3). Reuses the SAME deterministic
TF-IDF + role-matched control as rung1_uptake, generalized to arbitrary agent roles.

    python3 sim_analyze.py [sim/transcripts] [out_dir] [--backend manual|anthropic|openai]

Rung 1 (no model): per-transcript CROSS-AGENT uptake lift = mean(real adjacent
cross-agent cosine) - mean(role-matched random-partner cosine), with a 200-shuffle
permutation p. "Listening" = each agent taking up the other.
Rung 2 (cheap model, temp 0, BLIND): classify each agent's move toward the prior turn,
roles anonymized to A/B, no condition tag. Needs an API key (skipped if absent).
"""
import json, sys, os, random
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rung1_uptake import tfidf_vectors, cos, toks, SHUFFLES, SEED

def load_transcript(path):
    rec = json.load(open(path))
    stream = [(t["role"], t["text"]) for t in rec["turns"] if t.get("text", "").strip()]
    return rec["header"], stream

def convener_events(root):
    """Collect the structured cert_events[] from every convene transcript (no text parsing)."""
    cdir = os.path.join(root, "convene")
    evs = []
    if not os.path.isdir(cdir):
        return evs
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith(".json"):
            continue
        rec = json.load(open(os.path.join(cdir, fn)))
        for e in rec.get("cert_events", []):
            e = dict(e); e["_file"] = fn
            evs.append(e)
    return evs

def sub_topic(text):
    """Deterministic, model-free tag placing a point at one of the two registered hard joints
    (sim_preregistration.md A1.6 P3'b) or 'other'. Spacetime cue wins, then consciousness."""
    t = (text or "").lower()
    if any(w in t for w in ("spacetime", "space-time", "space time", "doomed", "locality",
                            "geometry")):
        return "spacetime-fundamentality"
    if any(w in t for w in ("conscious", "experience", "qualia", "awareness", "phenomenal",
                            "subjective")):
        return "consciousness-status"
    if "fundamental" in t:
        return "spacetime-fundamentality"
    return "other"

def convener_report(evs, L):
    """Append the Amendment-1 convener section: C0 gate FIRST, then P3'a / P3'b if C0 passes."""
    p = L.append
    p("\n## Convener - certification of understanding (Amendment 1)\n")
    if not evs:
        p("_No convene transcripts yet. Generate on the Mac:_ "
          "`python3 sim_harness.py --condition convene --seeds 0-4 --backend anthropic`\n")
        return
    faithful = [e for e in evs if not e["is_strawman"]]
    straw    = [e for e in evs if e["is_strawman"]]
    mean = lambda xs: (sum(xs) / len(xs)) if xs else float("nan")
    rate = lambda es: mean([1 if e["verdict"] == "certify" else 0 for e in es])
    cf, cs = rate(faithful), rate(straw)
    disc = cf - cs
    # Restatement fidelity: TF-IDF cosine(R, target_point) over the whole event corpus (no model).
    docs = []
    for e in evs:
        docs.append(toks(e["target_point"])); docs.append(toks(e["restatement"]))
    vecs = tfidf_vectors(docs)
    for i, e in enumerate(evs):
        e["_fid"] = cos(vecs[2 * i], vecs[2 * i + 1])
    fidf, fids = mean([e["_fid"] for e in faithful]), mean([e["_fid"] for e in straw])
    p(f"- Events: **{len(evs)}** ({len(faithful)} faithful, {len(straw)} strawman); "
      f"strawman share {len(straw) / len(evs):.2f} (target 0.33).")
    p(f"- Certify-rate: faithful **{cf:.2f}** vs strawman **{cs:.2f}**.")
    p(f"- Restatement fidelity (cosine to original): faithful **{fidf:.3f}** vs strawman "
      f"**{fids:.3f}**.")
    c0 = (disc > 0.30) and (fidf > fids)
    p(f"\n- **C0 (PRIMARY GATE): discrimination = {disc:+.2f}, fidelity gap = "
      f"{fidf - fids:+.3f}.** "
      + ("PASS - certification carries information; reading the rest."
         if c0 else
         "FAIL - certification is rubber-stamping (strawmen certified ~as often, or fidelity "
         "doesn't separate); the convener measure is VOID. Rest withheld per A1.6."))
    if not c0:
        return
    floor = 0.60
    p(f"- **P3'a (understanding achievable):** faithful certify-rate {cf:.2f} "
      f"{'>' if cf > floor else '<='} floor {floor:.2f} -> "
      + ("PASS - the parties can demonstrate understanding to each other under the protocol."
         if cf > floor else "FAIL - understanding not reliably reached."))
    fails = [e for e in faithful if e["verdict"] == "correct"]
    base = Counter(sub_topic(e["target_point"]) for e in faithful)
    floc = Counter(sub_topic(e["target_point"]) for e in fails)
    hard = ("spacetime-fundamentality", "consciousness-status")
    tot_fail = sum(floc.values()); hard_fail = sum(floc[h] for h in hard)
    p(f"- **P3'b (incommensurability LOCATED, not uniform):** {tot_fail} faithful "
      f"failed-certifications. Failure loci: "
      + (", ".join(f"{k} {floc[k]}" for k in floc) or "none")
      + ". Base faithful mix: " + ", ".join(f"{k} {base[k]}" for k in base) + ".")
    if tot_fail == 0:
        p("  _No failures on faithful events - the located-limit test needs at least one; "
          "the registered response (s.8) is add seeds / add a second seam, re-committed first._")
    else:
        conc = hard_fail / tot_fail
        p(f"  Hard-joint share of failures = {hard_fail}/{tot_fail} = {conc:.2f} -> "
          + ("PASS - failures concentrate on the registered hard joints (spacetime / "
             "consciousness), not uniformly." if conc >= 0.60 else
             "CHECK - failures do not concentrate on the hard joints (falsifier P3'b: apparatus "
             "may be locating noise, not incommensurability)."))

def crossagent_lift(stream, rng):
    roles = [r for r, _ in stream]
    vecs = tfidf_vectors([toks(t) for _, t in stream])
    n = len(vecs)
    by_role = defaultdict(list)
    for i, r in enumerate(roles): by_role[r].append(i)
    pairs = [(i + 1, i) for i in range(n - 1) if roles[i] != roles[i + 1]]   # cross-agent
    if not pairs: return None
    real = [cos(vecs[a], vecs[b]) for a, b in pairs]
    real_mean = sum(real) / len(real)
    null_means = []
    for _ in range(SHUFFLES):
        acc = []
        for later, earlier in pairs:
            pool = by_role[roles[earlier]]
            j = earlier
            if len(pool) >= 2:
                while j == later or j == earlier:
                    j = pool[rng.randrange(len(pool))]
            acc.append(cos(vecs[later], vecs[j]))
        null_means.append(sum(acc) / len(acc))
    null_mean = sum(null_means) / len(null_means)
    p = (sum(1 for m in null_means if m >= real_mean) + 1) / (len(null_means) + 1)
    return {"n": n, "real": real_mean, "null": null_mean, "lift": real_mean - null_mean,
            "p": p, "pairs": len(pairs)}

def _rung2_panel(root, backend):
    """Classify each adjacent cross-agent move (later turn toward prior turn), per
    condition. BLIND: the classifier receives only the two texts, never role/condition.
    Idempotent: labels cached in sim/labels_sim.json keyed by condition/file/pair."""
    import rung2_moves as R2
    tax = json.load(open(os.path.join(HERE, "rung2_labels.json")))["taxonomy"]
    classify = R2._model_classifier(backend, tax)
    cache_path = os.path.join(HERE, "sim", "labels_sim.json")
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    CIVIL = ("ack", "steelman", "concede")      # A1.5 civil register
    HOSTILE = ("deflect", "override")            # A1.5 hostile register (taxonomy has no 'dismiss')
    out = {}; civ = {}
    for cond in sorted(os.listdir(root)):
        cdir = os.path.join(root, cond)
        if not os.path.isdir(cdir): continue
        cc = Counter(); pc = Counter(); cache.setdefault(cond, {})
        for fn in sorted(os.listdir(cdir)):
            if not fn.endswith(".json"): continue
            _, stream = load_transcript(os.path.join(cdir, fn))
            labs = cache[cond].setdefault(fn, [])
            pairs = [(i + 1, i) for i in range(len(stream) - 1)
                     if stream[i][0] != stream[i + 1][0]]
            for k, (later, earlier) in enumerate(pairs):
                if k >= len(labs) or not labs[k]:
                    lab = classify(stream[earlier][1][:240], stream[later][1][:240])
                    while len(labs) <= k: labs.append(None)
                    labs[k] = lab
                lab = R2.normalize_label(labs[k])   # canonicalize cached `**probe**` etc.
                if not lab:
                    continue
                cc[lab] += 1
                # P-civility: count only moves MADE BY a principal (later turn is C or H),
                # so the convener T's own trivially-civil turns don't inflate the contrast.
                if stream[later][0] in ("C", "H"):
                    pc["total"] += 1
                    if lab in CIVIL:   pc["civil"] += 1
                    if lab in HOSTILE: pc["hostile"] += 1
        out[cond] = cc; civ[cond] = pc
    json.dump(cache, open(cache_path, "w"), indent=1)
    return out, civ

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    root = a[0] if a else os.path.join(HERE, "sim", "transcripts")
    outdir = a[1] if len(a) > 1 else HERE
    backend = sys.argv[sys.argv.index("--backend") + 1] if "--backend" in sys.argv else "manual"
    rng = random.Random(SEED)

    conditions = {}
    for cond in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        cdir = os.path.join(root, cond)
        if not os.path.isdir(cdir): continue
        rows = []
        for fn in sorted(os.listdir(cdir)):
            if not fn.endswith(".json"): continue
            hdr, stream = load_transcript(os.path.join(cdir, fn))
            m = crossagent_lift(stream, rng)                       # all cross-agent pairs
            # principals-only: drop the bridge B so we measure C<->H uptake specifically.
            # In bridge, B paraphrases both sides and inflates all-pairs cosine by design,
            # so the honest P3 test is whether C and H take EACH OTHER up more with B present.
            pr = crossagent_lift([t for t in stream if t[0] in ("C", "H")], rng)
            if m:
                m["pr_lift"] = pr["lift"] if pr else None
                rows.append((fn, m))
        if rows: conditions[cond] = rows

    L = []; p = L.append
    p("# Simulated rival-tradition dialogue - Rung 1 & 2 panel\n")
    p(f"_Generated {__import__('datetime').datetime.now():%Y-%m-%d %H:%M}. Rung 1: "
      f"TF-IDF role-matched lift, {SHUFFLES} shuffles, seed {SEED}, no model._\n")
    if not conditions:
        p("No transcripts found yet. Generate them on the Mac with sim_harness.py.\n")
        open(os.path.join(outdir, "sim_report.md"), "w").write("\n".join(L) + "\n")
        print("no transcripts; wrote scaffold report"); return

    mean = lambda xs: sum(xs) / len(xs)
    summ = {}
    p("## Rung 1 - cross-agent uptake by condition\n")
    p("| condition | k | mean lift (all) | lift range | mean lift (C<->H only) | mean p | sig (p<.05) |")
    p("|---|---:|---:|---|---:|---:|---:|")
    for cond, rows in conditions.items():
        lifts = [m["lift"] for _, m in rows]; ps = [m["p"] for _, m in rows]
        prs = [m["pr_lift"] for _, m in rows if m.get("pr_lift") is not None]
        summ[cond] = lifts
        sig = sum(1 for x in ps if x < 0.05)
        prtxt = f"{mean(prs):+.3f}" if prs else "-"
        p(f"| {cond} | {len(rows)} | {mean(lifts):+.3f} | "
          f"[{min(lifts):+.3f}, {max(lifts):+.3f}] | {prtxt} | {mean(ps):.3f} | {sig}/{len(rows)} |")
    p("\n## Pre-registered contrasts\n")
    if "listen" in summ and "deaf" in summ:
        d = mean(summ["listen"]) - mean(summ["deaf"])
        sep = min(summ["listen"]) > max(summ["deaf"])
        p(f"- **P1 (listen > deaf):** listen {mean(summ['listen']):+.3f} vs deaf "
          f"{mean(summ['deaf']):+.3f} -> delta **{d:+.3f}**; distributions "
          f"{'SEPARATED (no overlap)' if sep else 'OVERLAP'}. "
          f"{'PASS - instrument detects listening.' if d>0 and sep else 'CHECK - see falsifier P1.'}")
    if "bridge" in summ and "listen" in summ:
        d = mean(summ["bridge"]) - mean(summ["listen"])
        p(f"- **P3 (bridge > listen), ALL cross-agent pairs (confounded):** bridge "
          f"{mean(summ['bridge']):+.3f} vs listen {mean(summ['listen']):+.3f} -> delta "
          f"**{d:+.3f}**. Counts C<->B and B<->H, which B inflates by paraphrasing; not the real test.")
        # principals-only (drop B): the honest P3 test of C<->H acceleration
        prb = [m["pr_lift"] for _, m in conditions["bridge"] if m.get("pr_lift") is not None]
        prl = [m["pr_lift"] for _, m in conditions["listen"] if m.get("pr_lift") is not None]
        if prb and prl:
            dp = mean(prb) - mean(prl)
            sep = min(prb) > max(prl)
            p(f"- **P3 principals-only (C<->H, B dropped) — the registered test:** bridge "
              f"{mean(prb):+.3f} [{min(prb):+.3f},{max(prb):+.3f}] vs listen {mean(prl):+.3f} "
              f"[{min(prl):+.3f},{max(prl):+.3f}] -> delta **{dp:+.3f}**, "
              f"{'separated' if sep else 'OVERLAP'}. "
              f"{'PASS - the bridge raises C<->H uptake.' if dp>0 and sep else ('weak/positive trend, distributions overlap.' if dp>0 else 'NEGATIVE - bridge does not raise C<->H uptake (publishable).')}")
    p("\n_Per-transcript detail:_\n")
    for cond, rows in conditions.items():
        p(f"- **{cond}**: " + "; ".join(f"{fn[:-5]} lift={m['lift']:+.3f} p={m['p']:.3f}"
          for fn, m in rows))
    convener_report(convener_events(root), L)     # C0 gate FIRST, then P3'a / P3'b
    p("\n## Rung 2 - relational moves (blind), by condition\n")
    if backend == "manual":
        p("_Skipped: Rung 2 needs a model backend (run on the Mac with `--backend anthropic`). "
          "Scoring is inherently blind — the classifier sees only the two utterance texts, "
          "never the role or condition (P2)._\n")
    else:
        ENGAGE = ("steelman", "concede", "build_on")   # the MacIntyrean engagement moves
        rung2, civ = _rung2_panel(root, backend)
        p("| condition | pairs | steelman+concede+build_on share | top moves |")
        p("|---|---:|---:|---|")
        shares = {}
        for cond, cc in rung2.items():
            tot = sum(cc.values()) or 1
            eng = sum(cc[m] for m in ENGAGE)
            shares[cond] = eng / tot
            top = ", ".join(f"{m} {n}" for m, n in cc.most_common(5))
            p(f"| {cond} | {tot} | {100*eng/tot:.0f}% | {top} |")
        if "listen" in shares and "deaf" in shares:
            d = shares["listen"] - shares["deaf"]
            p(f"\n- **P2 (engagement-move share: listen > deaf):** listen "
              f"{100*shares['listen']:.0f}% vs deaf {100*shares['deaf']:.0f}% -> delta "
              f"**{100*d:+.0f}pp**. {'PASS - the MacIntyrean moves track engagement.' if d>0 else 'NEGATIVE - moves do not separate listening from deaf.'}")
        if "convene" in civ and "listen" in civ:
            cc, ll = civ["convene"], civ["listen"]
            share = lambda d, k: (d[k] / d["total"]) if d.get("total") else 0.0
            csh, lsh = share(cc, "civil"), share(ll, "civil")
            chs, lhs = share(cc, "hostile"), share(ll, "hostile")
            ok = csh > lsh and chs <= lhs
            p(f"\n- **P-civility (convene > listen civil register; principals only, T excluded):** "
              f"civil share convene {100*csh:.0f}% vs listen {100*lsh:.0f}%; hostile convene "
              f"{100*chs:.0f}% vs listen {100*lhs:.0f}%. "
              f"{'PASS - the convener carries tone into C/H moves.' if ok else 'CHECK - no clear civility gap (falsifier P-civility: T is not doing its pass-through-of-tone job).'}")
    open(os.path.join(outdir, "sim_report.md"), "w").write("\n".join(L) + "\n")
    print(f"wrote {os.path.join(outdir,'sim_report.md')}; conditions: "
          + ", ".join(f"{c}={len(r)}" for c, r in conditions.items()))

if __name__ == "__main__":
    main()
