#!/usr/bin/env python3
"""Render Reconcile review.md from reconciliation.json + works_cited_staged.json."""
import json, os
OUT = os.environ.get("OUT_DIR", "/tmp/reconcile_out")
r = json.load(open(os.path.join(OUT, "reconciliation.json")))
staged = json.load(open(os.path.join(OUT, "works_cited_staged.json")))["works"]
res = r["id_resolution"]; st = r["stats"]

L = []
w = L.append
w("---")
w("title: Reconcile Review — Summa Commentary Apparatus (foundation §7 step 3)")
w("updated: 2026-07-17")
w("status: DERIVED from reconciliation.json + works_cited_staged.json — do not hand-edit; re-run reconcile_reference_master.py")
w("relates_to: \"[[Referencing and linking foundation]]\", \"reconciliation.json\", \"works_cited_staged.json\"")
w("---\n")
w("# Reconcile Review — human-confirm queue\n")
w("Step 3 (reconcile) ran non-destructively over the confirmed 46-work bibliography and the "
  "307-day harvest. Nothing in `works_cited.json` or `reference_master.json` was changed. This "
  "page is the queue of judgment calls for your confirmation; the machine overlay is "
  "`reconciliation.json`; proposed new works are `works_cited_staged.json`.\n")
w("## At a glance\n")
w(f"- **{st['occurrences_total']}** body occurrences reconciled — **{st['specific_kept']}** kept as harvested specifics, "
  f"**{st['generic_canonical_default_flagged']}** generic → thinker-canonical default (flagged, never pinned; foundation §4).")
w(f"- **{st['auto_promotions']}** auto-promotions (bounded policy: the only title-candidate present is the denylisted concept-label *active inference*).")
w(f"- Ids resolved to a wiki node + endnote target: **{st['scoped_prs_ids']}** scoped PRS, "
  f"**{st['unscoped_prs_ids']}** unscoped PRS, **{st['cross_ids']}** CROSS, **{st['flag_ids']}** FLAG.")
w(f"- **{st['staged_new_works']}** proposed new works (all `verified:false`) — your confirmation gates each.\n")
w("Every PRS endnote cites **two** things (foundation §4): Loughran's PRS-form re-description "
  f"(`{r['id_resolution']['scoped_prs'][list(res['scoped_prs'])[0]]['loughran_form']}`) **+** the underlying thinker work below. "
  "CROSS/FLAG ids are internal (foundation §5, stripped at export) and never become a body citation.\n")

# ---------- 1. staged works ----------
w("## 1. Proposed new works — confirm & set `verified:true` (highest priority)\n")
w("These underlying works are cited by PRS ids but were not among your confirmed 46. Each is staged "
  "`verified:false` in `works_cited_staged.json`. Confirm the detail, flip `verified`, then merge.\n")
w("| cite_key | work | type | year | note / decision needed |")
w("| --- | --- | --- | --- | --- |")
for k, v in staged.items():
    au = ", ".join(v["authors"])
    cont = f" — *{v['container']}*" if v.get("container") else ""
    w(f"| `{k}` | {au}, \"{v['title']}\"{cont} | {v['work_type']} | {v['year']} | {v['note']} |")
w("")

# ---------- 2. scoped PRS ----------
w("## 2. Scoped PRS-id resolutions (48)\n")
by = {}
for pid, rec in res["scoped_prs"].items():
    by.setdefault(rec["resolution"], []).append((pid, rec))
labels = {"existing-canonical-via-source":"Deterministic (from works_cited source field) — no action",
          "canonical":"RC-Tome re-description → thinker canonical work — **confirm**",
          "canonical-fallback":"Canonical fallback — **confirm**",
          "existing":"Maps to an already-seeded non-canonical work — **confirm**",
          "staged":"→ a proposed NEW staged work (see §1) — **confirm**"}
for how in ["existing-canonical-via-source","existing","staged","canonical","canonical-fallback"]:
    items = by.get(how)
    if not items: continue
    w(f"### {labels.get(how, how)}  ({len(items)})\n")
    w("| PRS id | → underlying work | days | note |")
    w("| --- | --- | --- | --- |")
    for pid, rec in sorted(items):
        w(f"| `{pid}` | `{rec['underlying_work']}` | {len(rec['days'])} | {rec['note']} |")
    w("")

# ---------- 3. unscoped PRS ----------
w("## 3. Unscoped PRS-ids (10) — provisional, confirm scope\n")
w("Appear in bodies with no adjacent surname; provisionally the C2A2/RC master framework (→ Loughran PRS-form). "
  "Could be a thinker's PRS the harvester failed to scope — confirm per occurrence.\n")
w("| id | occurrences | provisional target | node |")
w("| --- | --- | --- | --- |")
for uid, rec in sorted(res["unscoped_prs"].items()):
    w(f"| `{uid}` | {rec['n_occurrences']} | `{rec['underlying_work']}` | {rec['wiki_node']} |")
w("")

# ---------- 4. CROSS/FLAG ----------
w("## 4. CROSS / FLAG ids — internal bridges (34) — stripped at export\n")
w("Not citable body works. Listed so the build step maps them to the involved programs' canonical works "
  "and so QC can verify none leak into print (foundation §5).\n")
w("| CROSS id | programs | → canonical works if cited | occ |")
w("| --- | --- | --- | --- |")
for uid, rec in sorted(res["cross"].items()):
    works = ", ".join(f"`{x}`" for x in rec["underlying_canonical_works"])
    w(f"| `{uid}` | {rec['programs']} | {works} | {rec['n_occurrences']} |")
w("")
for uid, rec in sorted(res["flag"].items()):
    w(f"- `{uid}` ({rec['n_occurrences']} occ) — {rec['note']}")
w("")

# ---------- 5. promotion candidates ----------
w("## 5. Generic→specific promotion candidates (bounded)\n")
w("No occurrence was auto-promoted. The only title-candidate in the harvest is the denylisted concept-label "
  "*active inference* (→ `friston-2017-active-inference-process-theory`). These Friston days matched it; confirm "
  "which genuinely cite the 2017 process-theory paper versus staying generic → FEP:\n")
ai = res["scoped_prs"]  # placeholder
fr = r["occurrence_summary"].get("friston", {})
days = fr.get("active_inference_candidate_days", [])
w(f"- **friston**, {len(days)} days: {', '.join('d'+str(d) for d in days)}\n")

# ---------- 6. generic default per thinker ----------
w("## 6. Generic surname-only mentions → canonical default (flagged, foundation §4)\n")
w("Kept resolved to each thinker's canonical work, flagged for confirmation — never silently pinned. "
  "Per-thinker counts (specific kept / generic-default flagged):\n")
w("| thinker | canonical | specific kept | generic→canonical (flagged) |")
w("| --- | --- | --- | --- |")
for t, s in sorted(r["occurrence_summary"].items(), key=lambda kv:-kv[1]["n_generic_canonical_default"]):
    if s["n_specific"] or s["n_generic_canonical_default"]:
        w(f"| {t} | `{s['canonical_cite_key']}` | {s['n_specific']} | {s['n_generic_canonical_default']} |")
w("")
w("---")
w(f"*Self-check: {'PASS — ' if not r['self_check_errors'] else 'FAIL — '}"
  f"{st['occurrences_total']} occurrences accounted for; "
  f"{st['scoped_prs_ids']+st['unscoped_prs_ids']+st['cross_ids']+st['flag_ids']} distinct ids resolved to a node.*")

open(os.path.join(OUT, "Reconcile review.md"), "w").write("\n".join(L))
print("wrote Reconcile review.md ("+str(len("\n".join(L)))+" bytes)")
print("errors:", r["self_check_errors"] or "none")
