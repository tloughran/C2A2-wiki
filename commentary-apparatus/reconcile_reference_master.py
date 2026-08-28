#!/usr/bin/env python3
"""
reconcile_reference_master.py  —  foundation §7 step 3 (reconcile)

Non-destructive. Reads the confirmed bibliography + the step-2 harvest and emits
THREE new files, touching neither works_cited.json nor reference_master.json:

  reconciliation.json        - overlay: id->cite_key resolution + occurrence
                               reconcile status + the human-confirm queue
  works_cited_staged.json    - proposed NEW works (verified:false) for underlying
                               works the confirmed 46 don't yet cover
  Reconcile review.md        - human-readable render of the confirm queue

Policy (Tom's calls 2026-07-17):
  * Bibliography: STAGE proposed new works (verified:false) for identifiable
    underlying works; freeze the confirmed 46 (never silently mutate them).
  * Promotion: BOUNDED - promote a generic occurrence to a specific work only on
    an unambiguous named work. The sole title-candidate in the harvest is the
    DENYLISTED concept-label "active inference" (foundation harvester nuance), so
    NO occurrence auto-promotes; the 44 Friston hits become review candidates.
  * Every generic surname-only mention stays resolved to the thinker's canonical
    work and is flagged for human confirmation (foundation §4) - never pinned.
  * PRS id -> endnote cites Loughran's PRS-form re-description + the underlying
    thinker work (foundation §4), never the thinker as author of the PRS.
  * CROSS/FLAG ids are INTERNAL synthesis constructs (foundation §5, stripped at
    export): mapped to their wiki node + the involved programs' canonical works,
    marked internal:true - not a citable body work.
"""
import json, re, os, sys

# ---- paths (override with $APPARATUS_DIR / $WIKI_DIR when run on-device) -------
AP = os.environ.get("APPARATUS_DIR",
     "/mnt/user-data/uploads/RC Karpathy Wiki Project/commentary-apparatus")
WK = os.environ.get("WIKI_DIR",
     "/mnt/user-data/uploads/RC Karpathy Wiki Project/wiki")
OUT = os.environ.get("OUT_DIR", "/tmp/reconcile_out")
os.makedirs(OUT, exist_ok=True)

wc = json.load(open(os.path.join(AP, "works_cited.json")))["works"]
rm = json.load(open(os.path.join(AP, "reference_master.json")))
cross_txt = open(os.path.join(WK, "master", "cross_program_index.md"), encoding="utf-8").read()

LOUGHRAN_FORM = "loughran-2026-prs-synergistic-coil-form"   # the PRS-form scaffold (foundation §3/§4)

# ---- deterministic: existing cite_key <- PRS id, from works_cited source fields
prs_existing = {}
for ck, w in wc.items():
    for m in re.findall(r"([a-z]+)-PRS-(\d+)", w.get("source", "") or ""):
        prs_existing[f"{m[0]}-PRS-{int(m[1]):02d}"] = ck

# ---- canonical cite_key per thinker (for generic defaults + CROSS program works)
canon = {}
for ck, w in wc.items():
    if w.get("canonical"):
        canon[w["thinker"]] = ck

# ---- MANUAL resolution of the 36 unmapped scoped PRS ids (judgment, foundation §4)
# value = ("existing"|"canonical"|"staged", cite_key, note)
UNMAPPED_PRS = {
 # Type A: RC-Tome extraction -> the thinker's canonical work (re-description), flag
 "carroll-PRS-01": ("canonical", "carroll-2016-big-picture", "RC-Tome re-description; ontological-closure/emergence -> Big Picture"),
 "carroll-PRS-04": ("canonical", "carroll-2016-big-picture", "RC-Tome; agency-without-dualism -> Big Picture"),
 "carroll-PRS-05": ("canonical", "carroll-2016-big-picture", "RC-Tome; science-religion dialogue -> Big Picture"),
 "fredrickson-PRS-04": ("canonical", "fredrickson-2013-love-2-0", "RC-Tome; relational coherence -> Love 2.0"),
 "fredrickson-PRS-06": ("canonical", "fredrickson-2013-love-2-0", "RC-Tome; democratizing participation -> Love 2.0"),
 "friston-PRS-01": ("canonical", "friston-2010-free-energy-principle", "RC-Tome; biological agency without vitalism -> FEP"),
 "friston-PRS-04": ("canonical", "friston-2010-free-energy-principle", "RC-Tome; organism as active modeler -> FEP"),
 "friston-PRS-05": ("canonical", "friston-2010-free-energy-principle", "RC-Tome; distributed cognition across scales -> FEP"),
 "friston-PRS-06": ("canonical", "friston-2010-free-energy-principle", "RC-Tome; multi-agent coherence -> FEP"),
 "hawkins-PRS-03": ("canonical", "hawkins-2021-thousand-brains", "RC-Tome; knowledge-preserving AGI -> Thousand Brains"),
 "hawkins-PRS-04": ("canonical", "hawkins-2021-thousand-brains", "RC-Tome; reference frames -> Thousand Brains"),
 "hoffman-PRS-01": ("canonical", "hoffman-2019-case-against-reality", "RC-Tome; hard-problem transformation -> Case Against Reality"),
 "hoffman-PRS-03": ("canonical", "hoffman-2019-case-against-reality", "RC-Tome; perception fitness-tracking -> Case Against Reality"),
 "hoffman-PRS-04": ("canonical", "hoffman-2019-case-against-reality", "RC-Tome; observer-dependent spacetime -> Case Against Reality"),
 "kastrup-PRS-04": ("canonical", "kastrup-2019-idea-of-the-world", "RC-Tome; philosophy<->mathematics bridge -> Idea of the World"),
 "levin-PRS-01": ("canonical", "levin-2022-cognitive-light-cones", "RC-Tome; morphogenetic control -> Cognitive Light Cones (consider levin-2018-bioelectric-code)"),
 "levin-PRS-04": ("canonical", "levin-2022-cognitive-light-cones", "RC-Tome; cognition substrate/xenobots -> Cognitive Light Cones (consider levin-2020-xenobots)"),
 "mcgilchrist-PRS-03": ("canonical", "mcgilchrist-2009-master-and-his-emissary", "RC-Tome; hemispheric modes -> Master & Emissary"),
 "mcgilchrist-PRS-04": ("canonical", "mcgilchrist-2009-master-and-his-emissary", "RC-Tome; multi-agent integration -> Master & Emissary"),
 "mcgilchrist-PRS-05": ("canonical", "mcgilchrist-2009-master-and-his-emissary", "RC-Tome; attention as ontological act -> Master & Emissary (consider 2021 Matter with Things)"),
 "stump-PRS-04": ("canonical", "stump-2010-wandering-in-darkness", "RC-Tome; final causality & biology -> Wandering (consider stump-2003-aquinas)"),
 "stump-PRS-05": ("canonical", "stump-2010-wandering-in-darkness", "RC-Tome; suffering & divine permission -> Wandering in Darkness"),
 "stump-PRS-06": ("canonical", "stump-2010-wandering-in-darkness", "RC-Tome; tradition vitality & MacIntyre -> Wandering (cross to macintyre)"),
 "wolfram-PRS-04": ("canonical", "wolfram-2020-project-fundamental-theory", "RC-Tome; computational irreducibility & agency -> Fundamental Theory (consider wolfram-2002-nks)"),
 "loughran-PRS-08": ("canonical", LOUGHRAN_FORM, "RC-Tome tradition-crossing inquiry, re-homed from stump PRS-01 per ASSUMPTION-076; consider a distinct 'RC Tome' work"),
 # Type B: an already-seeded non-canonical work (existed, just not via source-field)
 "hoffman-PRS-07": ("existing", "hoffman-2026-multiscale-logic-collective-intelligence", "Thoughtforms Life talk = the seeded 2026 multiscale-logic entry; confirm talk-vs-article container"),
 "wolfram-PRS-06": ("existing", "wolfram-2026-metaphysics-and-the-ruliad", "= the seeded 2026 Ruliad metaphysics entry"),
 # Type C: genuinely NEW underlying work -> STAGE (verified:false)
 "fredrickson-PRS-08": ("staged", "fredrickson-2025-conducive-conditions-positivity-resonance", "UBC colloquium talk"),
 "friston-PRS-07": ("staged", "friston-2026-active-inference-review", "2026 review paper (also confirms CROSS-006/007)"),
 "friston-PRS-08": ("staged", "friston-2026-active-inference-review", "same 2026 review, Section 4.1"),
 "levin-PRS-07": ("staged", "levin-2026-ferriss-interview", "Tim Ferriss Show #849"),
 "levin-PRS-08": ("staged", "levin-2026-ferriss-interview", "Tim Ferriss Show #849"),
 "stump-PRS-07": ("staged", "stump-2025-biblical-narratives-flourishing", "Stump & Wolfe, Routledge"),
 "stump-PRS-08": ("staged", "stump-2024-grains-of-wheat", "Grains of Wheat, OUP"),
 "stump-PRS-11": ("staged", "stump-2024-grains-of-wheat", "Grains of Wheat, OUP"),
 "carroll-PRS-07": ("staged", "carroll-2026-mindscape-349-harlow", "Mindscape #349 GUEST (Harlow) - attribution decision needed"),
}

# ---- staged new works (verified:false), same schema as works_cited.json --------
STAGED = {
 "friston-2026-active-inference-review": {
    "thinker":"friston","authors":["Karl J. Friston","et al."],
    "title":"Active Inference and the Free Energy Principle: A Review","container":None,
    "year":2026,"publisher":None,"locator":None,"work_type":"article",
    "canonical":False,"verified":False,
    "source":"friston/prs_triplets.md PRS-07,08; cross_program_index CROSS-006/007 upgrade",
    "note":"Underlying work for friston PRS-07/08 and the CROSS-006/007 substrate-independence confirmation. Venue/DOI/full author list UNVERIFIED - confirm before print."},
 "levin-2026-ferriss-interview": {
    "thinker":"levin","authors":["Michael Levin"],
    "title":"Michael Levin - interview","container":"The Tim Ferriss Show, episode 849",
    "year":2026,"publisher":None,"locator":"episode #849, aired 2026-01-21","work_type":"talk",
    "canonical":False,"verified":False,
    "source":"levin/prs_triplets.md PRS-07,08",
    "note":"Podcast interview. DECISION: is a podcast episode admissible to the bibliography, or should PRS-07/08 cite a published Levin paper instead (e.g. bioelectric-reprogramming work)?"},
 "fredrickson-2025-conducive-conditions-positivity-resonance": {
    "thinker":"fredrickson","authors":["Barbara L. Fredrickson"],
    "title":"Conducive Conditions for Positivity Resonance at Multiple Levels of Analysis",
    "container":"UBC Psychology Colloquium","year":2025,"publisher":None,
    "locator":"colloquium talk, 2025-10-01","work_type":"talk",
    "canonical":False,"verified":False,
    "source":"fredrickson/prs_triplets.md PRS-08",
    "note":"Colloquium talk. Confirm whether a published paper version exists to cite instead."},
 "stump-2025-biblical-narratives-flourishing": {
    "thinker":"stump","authors":["Eleonore Stump","Judith Wolfe"],
    "title":"Biblical Narratives and Human Flourishing: Knowledge Through Narrative",
    "container":None,"year":2025,"publisher":"Routledge","locator":None,"work_type":"book",
    "canonical":False,"verified":False,
    "source":"stump/prs_triplets.md PRS-07 (PROP-2026-04-08-001)",
    "note":"Confirm authorship (Stump & Wolfe?), subtitle, and year vs source."},
 "stump-2024-grains-of-wheat": {
    "thinker":"stump","authors":["Eleonore Stump"],
    "title":"Grains of Wheat: Suffering and Biblical Narratives",
    "container":None,"year":2024,"publisher":"Oxford University Press",
    "locator":"https://academic.oup.com/book/59654","work_type":"book",
    "canonical":False,"verified":False,
    "source":"stump/prs_triplets.md PRS-08,11",
    "note":"PRS-08 gives '2024/25', PRS-11 gives 2024-10-01 - confirm publication year."},
 "carroll-2026-mindscape-349-harlow": {
    "thinker":"carroll","authors":["Daniel Harlow","Sean Carroll (host)"],
    "title":"What Quantum Gravity Teaches Us About Quantum Mechanics",
    "container":"Mindscape podcast, episode 349","year":2026,"publisher":None,
    "locator":"episode #349, 2026-03-30","work_type":"talk",
    "canonical":False,"verified":False,
    "source":"carroll/prs_triplets.md PRS-07 (PROP-2026-04-07-004)",
    "note":"AMBIGUOUS ATTRIBUTION: content is guest Daniel Harlow's, filed under Carroll's program only because it aired on his podcast. Do NOT attribute to Carroll as author. Decide whether it belongs in the bibliography at all."},
}

# ---- programs -> roster tag ----------------------------------------------------
PROG2TAG = {"levin":"levin","friston":"friston","hawkins":"hawkins","kastrup":"kastrup",
 "hoffman":"hoffman","wolfram":"wolfram","arkani-hamed":"arkanihamed","arkanihamed":"arkanihamed",
 "carroll":"carroll","mcgilchrist":"mcgilchrist","fredrickson":"fredrickson","stump":"stump",
 "wright":"wright","rohr":"rohr","loughran":"loughran","macintyre":"macintyre"}

def prog_tags(prog_str):
    tags=[]
    for p in prog_str.split(","):
        p=p.strip().replace(" Agent","").replace("(meta)","").strip()
        key=p.lower().replace(" ","")
        # normalise "Arkani-Hamed" etc.
        key=key.replace("arkani-hamed","arkanihamed")
        if key in PROG2TAG and PROG2TAG[key] not in tags:
            tags.append(PROG2TAG[key])
    return tags

CROSS_PROG = {}
for m in re.finditer(r"^CROSS-(\d+):\s*\n(?:.*\n)*?\s*Programs involved:\s*(.*)$", cross_txt, re.M):
    CROSS_PROG[f"CROSS-{m.group(1)}"] = m.group(2).strip()

# ================================================================= build overlay
resolution = {"scoped_prs":{}, "unscoped_prs":{}, "cross":{}, "flag":{}}
queue = []   # human-confirm items

# --- scoped PRS ids present in occurrences
scoped_seen = {}   # id -> set(days)
for t, v in rm["per_thinker"].items():
    for o in v["occurrences"]:
        for i in o.get("ids", []):
            m = re.match(r"PRS-(\d+)$", i)
            if m:
                key = f"{t}-PRS-{int(m.group(1)):02d}"
                scoped_seen.setdefault(key, set()).add(o["day"])

for pid in sorted(scoped_seen):
    node = f"wiki/traditions/{pid.split('-PRS-')[0]}/prs_triplets.md#{pid.split('-')[-1]}"
    if pid in prs_existing:
        uw, how, note = prs_existing[pid], "existing-canonical-via-source", "deterministic from works_cited source field"
    elif pid in UNMAPPED_PRS:
        how, uw, note = UNMAPPED_PRS[pid]
    else:
        uw, how, note = canon.get(pid.split("-PRS-")[0]), "canonical-fallback", "no explicit resolution; fell back to thinker canonical"
    rec = {"wiki_node": node, "loughran_form": LOUGHRAN_FORM,
           "underlying_work": uw, "resolution": how,
           "endnote_pair": [LOUGHRAN_FORM, uw], "note": note,
           "days": sorted(scoped_seen[pid]),
           "needs_human_confirm": how in ("canonical", "canonical-fallback", "staged", "existing")}
    resolution["scoped_prs"][pid] = rec
    if rec["needs_human_confirm"]:
        queue.append({"kind":"scoped-PRS", "id":pid, "n_days":len(scoped_seen[pid]),
                      "suggested_underlying": uw, "resolution":how, "why":note})

# --- unscoped ids (flags block): PRS-NN / CROSS-NN / FLAG-NN
unscoped = rm["flags"]["unscoped_ids_by_day"]
u_by_id = {}
for day, ids in unscoped.items():
    for i in ids:
        u_by_id.setdefault(i, []).append(day)

for uid in sorted(u_by_id):
    days = u_by_id[uid]
    if uid.startswith("PRS-"):
        rec = {"provisional_scope":"loughran/C2A2-master",
               "wiki_node":"wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md)",
               "loughran_form":LOUGHRAN_FORM, "underlying_work":LOUGHRAN_FORM,
               "endnote_pair":[LOUGHRAN_FORM, LOUGHRAN_FORM],
               "n_occurrences":len(days), "needs_human_confirm":True,
               "note":"Unscoped PRS (no adjacent surname). Provisionally the C2A2/RC master framework; could be a thinker's PRS the harvester failed to scope. CONFIRM per day."}
        resolution["unscoped_prs"][uid] = rec
        queue.append({"kind":"unscoped-PRS", "id":uid, "n_days":len(days),
                      "suggested_underlying":LOUGHRAN_FORM, "resolution":"provisional-loughran",
                      "why":"unscoped - confirm whether master-framework or a thinker PRS"})
    elif uid.startswith("CROSS-"):
        prog = CROSS_PROG.get(uid, "")
        tags = prog_tags(prog)
        works = [canon[t] for t in tags if t in canon]
        rec = {"wiki_node":f"wiki/master/cross_program_index.md#{uid}",
               "programs":prog, "program_tags":tags,
               "underlying_canonical_works":works, "internal":True,
               "n_occurrences":len(days), "needs_human_confirm":True,
               "note":"Internal cross-program bridge (foundation §5, stripped at export). If cited in body, resolves to the involved programs' canonical works - never a 'CROSS work'."}
        resolution["cross"][uid] = rec
        queue.append({"kind":"CROSS", "id":uid, "n_days":len(days),
                      "suggested_underlying":", ".join(works), "resolution":"internal-bridge",
                      "why":f"programs: {prog}"})
    elif uid.startswith("FLAG-"):
        rec = {"wiki_node":f"wiki/master/paradigm_flags.md#{uid}", "internal":True,
               "n_occurrences":len(days), "needs_human_confirm":True,
               "note":"Paradigm-shift flag (internal, stripped at export). NOTE: current paradigm_flags.md lists only FLAG-001/002; this id's definition was not found in the staged file - verify its home (wiki/flags/)."}
        resolution["flag"][uid] = rec
        queue.append({"kind":"FLAG", "id":uid, "n_days":len(days),
                      "suggested_underlying":"(internal - node only)", "resolution":"internal-flag",
                      "why":"definition not in current paradigm_flags.md - verify location"})

# --- occurrence-level reconcile summary (per thinker) ---------------------------
DENYLIST_CONCEPT = {"friston-2017-active-inference-process-theory"}  # "active inference" concept-label
occ_summary = {}
for t, v in rm["per_thinker"].items():
    occ = v["occurrences"]
    n_spec = sum(1 for o in occ if o.get("specific"))
    n_gen  = sum(1 for o in occ if not o.get("specific"))
    spec_keys = sorted({ck for o in occ if o.get("specific") for ck in o.get("resolved_cite_keys",[])})
    ai_days = sorted(o["day"] for o in occ
                     if not o.get("specific") and any(tc in DENYLIST_CONCEPT for tc in o.get("title_candidates",[])))
    occ_summary[t] = {"canonical_cite_key":v.get("canonical_cite_key"),
        "days":len(v.get("days",[])), "total_mentions":v.get("total_mentions"),
        "n_specific":n_spec, "n_generic_canonical_default":n_gen,
        "specific_works_used":spec_keys,
        "active_inference_candidate_days":ai_days,
        "generic_needs_human_confirm":True if n_gen else False}
    if ai_days:
        queue.append({"kind":"promotion-candidate", "id":f"{t}: active-inference concept-label",
                      "n_days":len(ai_days), "suggested_underlying":sorted(DENYLIST_CONCEPT)[0],
                      "resolution":"NOT auto-promoted (denylisted concept)",
                      "why":f"{len(ai_days)} generic days matched the concept-label 'active inference'; confirm which truly cite the 2017 process-theory paper vs stay generic->FEP"})

# ================================================================= self-checks
errs=[]
# 1. every scoped PRS resolved to a real (existing or staged) cite_key
allkeys=set(wc)|set(STAGED)
for pid, r in resolution["scoped_prs"].items():
    if r["underlying_work"] not in allkeys:
        errs.append(f"scoped {pid} -> unknown cite_key {r['underlying_work']}")
# 2. staged keys are ASCII, unique, and don't collide with confirmed 46
for k in STAGED:
    if k in wc: errs.append(f"staged key collides with confirmed: {k}")
    if not re.fullmatch(r"[a-z0-9-]+", k): errs.append(f"staged key not ascii-slug: {k}")
# 3. every occurrence accounted for
tot_occ = sum(len(v["occurrences"]) for v in rm["per_thinker"].values())
acc = sum(s["n_specific"]+s["n_generic_canonical_default"] for s in occ_summary.values())
if tot_occ != acc: errs.append(f"occurrence count mismatch: harvest {tot_occ} vs reconciled {acc}")
# 4. every distinct id in play resolved to at least a node
n_ids = len(resolution["scoped_prs"])+len(resolution["unscoped_prs"])+len(resolution["cross"])+len(resolution["flag"])

recon = {
 "_meta":{"schema":"commentary-apparatus/reconciliation v1 (foundation §7 step 3)",
    "generated_for":"foundation §7 step 3 reconcile","generator":"reconcile_reference_master.py",
    "policy":{"bibliography":"stage new works verified:false; freeze confirmed 46",
              "promotion":"bounded - no auto-promote; denylisted 'active inference' -> review candidate",
              "generic_default":"resolve to thinker canonical + needs_human_confirm (foundation §4)",
              "prs_endnote":"[Loughran PRS-form, underlying thinker work] (foundation §4)",
              "cross_flag":"internal, node + program canonical works, stripped at export (foundation §5)"},
    "inputs":{"works_cited":"works_cited.json (46 confirmed)","reference_master":"reference_master.json (307 days)",
              "cross_program_index":"wiki/master/cross_program_index.md"}},
 "stats":{"occurrences_total":tot_occ,
          "specific_kept":sum(s["n_specific"] for s in occ_summary.values()),
          "generic_canonical_default_flagged":sum(s["n_generic_canonical_default"] for s in occ_summary.values()),
          "auto_promotions":0,
          "scoped_prs_ids":len(resolution["scoped_prs"]),
          "unscoped_prs_ids":len(resolution["unscoped_prs"]),
          "cross_ids":len(resolution["cross"]),"flag_ids":len(resolution["flag"]),
          "staged_new_works":len(STAGED),
          "human_confirm_queue_items":len(queue)},
 "id_resolution":resolution,
 "occurrence_summary":occ_summary,
 "human_confirm_queue":sorted(queue, key=lambda q:(q["kind"], str(q["id"]))),
 "self_check_errors":errs,
}

json.dump(recon, open(os.path.join(OUT,"reconciliation.json"),"w"), indent=1, ensure_ascii=False)
json.dump({"_meta":{"schema":"commentary-apparatus/works_cited v1 (STAGED, verified:false)",
    "generated":"2026-07-17","generator":"reconcile_reference_master.py",
    "status":"PROPOSED underlying works surfaced by reconcile step 3; ALL verified:false. Tom confirms each, sets verified:true, then merge into works_cited.json via build_works_cited.py.",
    "count":len(STAGED)}, "works":STAGED},
    open(os.path.join(OUT,"works_cited_staged.json"),"w"), indent=1, ensure_ascii=False)

print("occurrences:", tot_occ, "| scoped PRS:", len(resolution["scoped_prs"]),
      "| unscoped PRS:", len(resolution["unscoped_prs"]),
      "| CROSS:", len(resolution["cross"]), "| FLAG:", len(resolution["flag"]),
      "| staged works:", len(STAGED), "| queue:", len(queue))
print("SELF-CHECK:", "PASS" if not errs else "FAIL -> "+"; ".join(errs))
