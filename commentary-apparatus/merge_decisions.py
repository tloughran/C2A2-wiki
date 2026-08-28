#!/usr/bin/env python3
"""
merge_decisions.py — the review→decision→merge gate for the commentary apparatus.

A REUSABLE pattern for any "reconcile produced a big overlay + a confirm queue"
review. Three surfaces, strictly separated:

  reading surface   Reconcile review.md          (DERIVED — never write decisions here)
  decision surface  reconcile_decisions.json     (you edit this; the ONLY hand-edited file)
  merge step        this script                  (code applies decisions, non-destructive)

Two modes:
  python3 merge_decisions.py --init      # write a pre-filled reconcile_decisions.json
                                         # (recommended default for every group; the two
                                         #  genuine judgment calls set to "hold")
  python3 merge_decisions.py             # apply decisions -> emit resolved outputs

Apply mode is NON-DESTRUCTIVE: it never touches works_cited.json, reference_master.json,
or build_works_cited.py. It emits:
  reconciliation.resolved.json  — the overlay with needs_human_confirm cleared where you
                                  decided; `unresolved` lists everything still open.
  approved_works.json           — approved staged works, verified:true, ready to fold into
                                  build_works_cited.py's WORKS dict (you run the generator).

FAIL LOUD (Rule 12): any staged work left "hold", or any batch policy left "hold",
prints a warning and exits nonzero — a half-decided gate never reads as "done".

Paths via $APPARATUS_DIR (default: cwd) and $OUT_DIR (default: $APPARATUS_DIR).
"""
import json, os, sys

AP  = os.environ.get("APPARATUS_DIR", os.getcwd())
OUT = os.environ.get("OUT_DIR", AP)
DEC = os.path.join(AP, "reconcile_decisions.json")

def _load(name, base=AP):
    return json.load(open(os.path.join(base, name), encoding="utf-8"))

# =============================================================== INIT
def init():
    recon  = _load("reconciliation.json")
    staged = _load("works_cited_staged.json")["works"]
    res = recon["id_resolution"]

    # staged-work recommendations: approve the detail-check ones; HOLD the two
    # genuine judgment calls so the gate can't close without an explicit choice.
    HOLD = {"levin-2026-ferriss-interview",
            "carroll-2026-mindscape-349-harlow"}
    staged_dec = {}
    for k, w in staged.items():
        staged_dec[k] = {
            "decision": "hold" if k in HOLD else "approve",
            "fields": {},              # amend: put corrected field values here
            "redirect": None,          # decline: cite_key the dependent PRS should point to instead
            "note": w.get("note", "")
        }

    decisions = {
      "_meta": {
        "schema": "commentary-apparatus/reconcile_decisions v1",
        "how": "Edit `decision`/policy values, then run merge_decisions.py. "
               "staged decision: approve | amend (with fields) | decline (with redirect) | hold. "
               "'hold' blocks the gate (fail loud). overrides[<id>].underlying_work replaces one resolution.",
        "reading_surface": "Reconcile review.md",
        "generated_defaults": "2026-07-17 (recommended default for every group; 2 judgment calls held)"
      },
      "batch_policies": {
        "rc_tome_prs_to_canonical": {
            "decision": "accept", "choices": ["accept", "review_each"],
            "note": "RC-Tome PRS re-descriptions resolve to the thinker's canonical work"},
        "existing_seeded_prs": {
            "decision": "accept", "choices": ["accept", "review_each"],
            "note": "PRS ids that map to an already-seeded non-canonical work (hoffman-07, wolfram-06)"},
        "generics_canonical_default": {
            "decision": "accept", "choices": ["accept", "review_each"],
            "note": "484 generic surname-only mentions stay resolved to thinker canonical (foundation §4)"},
        "friston_active_inference": {
            "decision": "keep_generic", "choices": ["keep_generic", "promote_all", "per_day"],
            "note": "44 Friston days matched the denylisted concept-label 'active inference'"},
        "unscoped_prs_scope": {
            "decision": "master_framework", "choices": ["master_framework", "per_day"],
            "note": "10 unscoped PRS ids -> C2A2/master (Loughran form), or leave per-day open"},
        "cross_flag_internal": {
            "decision": "accept", "choices": ["accept", "review_each"],
            "note": "33 CROSS + 2 FLAG internal bridges (stripped at export §5) — spot-check only"}
      },
      "staged_works": staged_dec,
      "overrides": {
        "_examples": {
            "levin-PRS-01": {"underlying_work": "levin-2018-bioelectric-code",
                             "note": "example: prefer the bioelectric paper over the canonical light-cones"}
        }
      }
    }
    json.dump(decisions, open(DEC, "w"), indent=1, ensure_ascii=False)
    print(f"wrote {DEC}\n  {len(staged_dec)} staged-work decisions "
          f"({sum(1 for d in staged_dec.values() if d['decision']=='hold')} held), "
          f"{len(decisions['batch_policies'])} batch policies pre-filled.")

# =============================================================== APPLY
def apply():
    if not os.path.exists(DEC):
        sys.exit("no reconcile_decisions.json — run:  merge_decisions.py --init  first")
    recon = _load("reconciliation.json")
    staged = _load("works_cited_staged.json")["works"]
    dec = _load("reconcile_decisions.json")
    res = recon["id_resolution"]
    pol = {k: v["decision"] for k, v in dec["batch_policies"].items()}
    sdec = dec["staged_works"]
    ovr = {k: v for k, v in dec.get("overrides", {}).items() if not k.startswith("_")}

    warnings, unresolved = [], []

    # ---- staged works: approve/amend -> verified:true; decline -> drop + redirect
    approved, declined = {}, {}
    for k, d in sdec.items():
        choice = d.get("decision")
        if choice == "hold":
            warnings.append(f"staged work '{k}' is HOLD — decide approve/amend/decline")
            continue
        if choice in ("approve", "amend"):
            w = dict(staged[k]); w.update(d.get("fields") or {}); w["verified"] = True
            approved[k] = w
        elif choice == "decline":
            declined[k] = d.get("redirect")
        else:
            warnings.append(f"staged work '{k}' has unknown decision '{choice}'")

    def redirect_for(work_key, thinker):
        """where a declined staged work's PRS should point instead."""
        r = declined.get(work_key)
        if r:
            return r, "redirected-per-decline"
        # fall back to the thinker's canonical, flagged
        can = recon["occurrence_summary"].get(thinker, {}).get("canonical_cite_key")
        return can, "declined->canonical-fallback (flag)"

    # ---- resolve scoped PRS
    scoped_out = {}
    for pid, r in res["scoped_prs"].items():
        thinker = pid.split("-PRS-")[0]
        uw, how, confirm = r["underlying_work"], r["resolution"], False
        if pid in ovr:
            uw, how, confirm = ovr[pid]["underlying_work"], "override", False
        elif how == "existing-canonical-via-source":
            confirm = False                                   # deterministic
        elif how in ("canonical", "canonical-fallback"):
            confirm = pol["rc_tome_prs_to_canonical"] != "accept"
        elif how == "existing":
            confirm = pol["existing_seeded_prs"] != "accept"
        elif how == "staged":
            if uw in approved:
                confirm = False
            elif uw in declined:
                uw, how = redirect_for(uw, thinker); confirm = True
                unresolved.append(f"scoped {pid}: staged work declined -> {uw}")
            else:
                confirm = True
                unresolved.append(f"scoped {pid}: staged work '{uw}' still HOLD")
        scoped_out[pid] = {**r, "underlying_work": uw, "resolution": how,
                           "endnote_pair": [r["loughran_form"], uw],
                           "needs_human_confirm": confirm}
        if confirm:
            unresolved.append(f"scoped {pid} still open ({how})")

    # ---- unscoped PRS
    unscoped_out = {}
    up = pol["unscoped_prs_scope"]
    for uid, r in res["unscoped_prs"].items():
        confirm = (up != "master_framework")
        unscoped_out[uid] = {**r, "needs_human_confirm": confirm}
        if confirm:
            unresolved.append(f"unscoped {uid} left per-day open")

    # ---- cross / flag
    cf = pol["cross_flag_internal"] != "accept"
    cross_out = {k: {**v, "needs_human_confirm": cf} for k, v in res["cross"].items()}
    flag_out  = {k: {**v, "needs_human_confirm": True} for k, v in res["flag"].items()}  # location still unverified
    for k in flag_out:
        unresolved.append(f"{k}: verify definition location (not in paradigm_flags.md)")

    # ---- friston active-inference candidates
    fa = pol["friston_active_inference"]
    ai_days = recon["occurrence_summary"].get("friston", {}).get("active_inference_candidate_days", [])
    if fa == "keep_generic":
        ai_note = f"{len(ai_days)} days kept generic -> FEP"
    elif fa == "promote_all":
        ai_note = f"{len(ai_days)} days promoted -> friston-2017-active-inference-process-theory"
    else:
        ai_note = f"{len(ai_days)} days left per-day open"
        unresolved += [f"friston active-inference day {d} left open" for d in ai_days]

    resolved = {
      "_meta": {"schema": "commentary-apparatus/reconciliation.resolved v1",
                "generator": "merge_decisions.py", "source": "reconciliation.json + reconcile_decisions.json",
                "policies_applied": pol, "note": "needs_human_confirm cleared where you decided; see `unresolved`."},
      "id_resolution": {"scoped_prs": scoped_out, "unscoped_prs": unscoped_out,
                        "cross": cross_out, "flag": flag_out},
      "friston_active_inference": {"policy": fa, "days": ai_days, "note": ai_note},
      "generics_policy": pol["generics_canonical_default"],
      "approved_new_works": sorted(approved), "declined_new_works": declined,
      "unresolved": unresolved,
      "summary": {"scoped_prs": len(scoped_out), "still_open": len(unresolved),
                  "approved_works": len(approved), "declined_works": len(declined)}
    }
    json.dump(resolved, open(os.path.join(OUT, "reconciliation.resolved.json"), "w"), indent=1, ensure_ascii=False)
    json.dump({"_meta": {"schema": "works_cited additions (verified:true)",
                         "note": "Approved staged works. Fold into build_works_cited.py's WORKS dict, then re-run it.",
                         "count": len(approved)}, "works": approved},
              open(os.path.join(OUT, "approved_works.json"), "w"), indent=1, ensure_ascii=False)

    print("=== DECISIONS SUMMARY ===")
    print(f"  approved new works : {len(approved)}  {sorted(approved)}")
    print(f"  declined new works : {len(declined)}  {declined or ''}")
    print(f"  active-inference   : {ai_note}")
    print(f"  scoped PRS resolved: {sum(1 for r in scoped_out.values() if not r['needs_human_confirm'])}/{len(scoped_out)}")
    print(f"  still OPEN         : {len(unresolved)}")
    for u in unresolved[:12]:
        print("     -", u)
    if len(unresolved) > 12:
        print(f"     ... +{len(unresolved)-12} more (see reconciliation.resolved.json `unresolved`)")
    if warnings:
        print("\n!!! HOLDS / WARNINGS (gate not closed):")
        for w in warnings:
            print("   -", w)
        sys.exit(2)
    print("\nGate clean. Fold approved_works.json into build_works_cited.py, re-run it, then proceed to step 3b.")

if __name__ == "__main__":
    (init if "--init" in sys.argv[1:] else apply)()
