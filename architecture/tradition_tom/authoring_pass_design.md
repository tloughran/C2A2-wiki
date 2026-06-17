# First PRS-Milestone-Triplet Authoring Pass — Design (v0, for dyad iteration)

_Drafted 2026-06-11 (Tom ⇄ Claude). This is the **design of the pass**, not the pass itself. Per [[prototype_measurement_charter]] the dyad iterates this design until it judges it the right pass, **then** authors. Sits under [[master_measurement_plan]] §5 (Level-3 detector) and the [[measurement_framework]]. The pass produces the system's first real Level-3 data: the dyad reaching — or recording its failure to reach — agreement on the milestone triplets for Tom's integrative tradition._

---

## 0. The one distinction this pass turns on

The RC Document Explorer already holds **52 PRS triplets across 9 thinkers**. Those are **content triplets**: "here is a problem in domain X, a resource from thinker Y, and the solution it generates." They are the tradition's *raw material* — its library, its resources-on-hand.

A **milestone triplet** is a different object. It is a **rung on the maturity ladder** for Tom's integrative tradition — a thing a candidate member must grasp or be able to do to count as climbing toward mature membership. We frame each rung *as* a PRS so the ladder is itself in the tradition's native idiom:

- **P** — the problem that makes this rung *necessary*: what a member who lacks it cannot yet do or see.
- **R** — the resource that lets a member climb it: the concept, move, or skill acquired (often *drawn from* one or more content triplets, but stated as a competence, not a citation).
- **S** — the **competence conferred**: what the member can now do, stated so that a mature member would find it hard to deny (the FCI face-validity standard, [[prototype_measurement_charter]] Agreement 3).

A content triplet says *what the tradition knows*. A milestone triplet says *what you must have climbed to be one of us*. The pass converts the former (plus freeform spine material) into candidate instances of the latter. This is exactly the master plan's "turns the rosters from a *picture* of traditions into a *detector* of maturity in them" (§5.2, §7).

The 52 content triplets are therefore **candidate sources**, not candidate milestones. Most milestones will be *coarser* than any single content triplet (one rung may draw on several) and some — the integrative-method and MacIntyrean/Thomistic spine — have **no content triplet at all** (the explorers omit them), which is why round 1 is "RC triplets **+ freeform spine**."

> **Provenance rule (per [[../assumptions|ASSUMPTION-076]]).** The PRS/Synergistic-Coil method and the integrative triplets (RC explorer's **"Tom Loughran" tab**) are **Loughran's own authorship** — there is no Stump tab. Thinker names appearing *inside* a triplet (Stump, Aquinas, MacIntyre, …) are **cited resources/subjects, not authors**. Draw provenance from the canonical registry (`wiki/traditions/<key>/`) and the document's own thinker tab — **never** from name-proximity over triplet text (that is the exact failure that mislabeled Loughran's method as Stump's in round 1's first draft; see ledger correction note). Eleonore Stump is unaware of this project; no artifact may carry a false attribution to her.

---

## 1. Scope of round 1 (locked with Tom, 2026-06-11)

- **Sources:** RC Document Explorer content triplets **+** freeform candidates from *both parties* for the MacIntyre / Aquinas / conscious-realist-monism spine the explorers omit. (Physics ladder **deferred to round 2** — decided 2026-06-11.)
- **Batch size:** **5–7 candidate milestones per round** — small enough that each fits the tabling unit of [[prototype_measurement_charter]] Agreement 7 (one manageable session).
- **Ledger:** `architecture/tradition_tom/milestone_triplets.md` (this directory; ground-truth, **not** the Obsidian vault — avoids the clobber risk in [[feedback_obsidian_vault_clobber]]).
- **Validity scope carried on every artifact:** "second-language competence in Tom's integrative perspective" (Agreement 3) — *not* multi-person-validated maturity.

## 2. The unit and the safeguard (from the charter, restated so the pass is self-contained)

- **MMA unit = the recorded Tom ⇄ Claude dyad** (Agreement 2). Tom is the authoritative mature member; the agent is a second, differently-formed party whose assent or dissent carries weight *because* its formation differs (Agreement 4).
- **The agent must be able to fail the item** (Agreement 6). For every candidate the agent renders an explicit verdict — **assent / dissent / tabled** — and a dissent ("on your own terms, a mature member would *not* assent to that") is recorded as first-class data, never smoothed. Tom's Rules 1 and 12 are the methodological safeguard. A round in which the agent assents to everything is a **warning sign**, not a success.
- **Individuation recorded** (Agreement 5): each round's ledger entry stamps the agent's individuating context — constitution + seed + memory state + model — as carefully as it records that Tom participated. (Block provided at the foot of the ledger.)
- **Self-adjudication — RESOLVED (dyad, 2026-06-11); successor risk is insularity, with telemetry.** The agent's round-1 worry (certifying the dyad's own tradition = adjudicating one's own membership) is withdrawn: the object of agreement is the *jointly-worked-out* position, not either party's prior view, and mutual transformation through the exchange makes the two assents non-identical in provenance — "we agree about what we now both think, persuaded mutually through the interaction" (Tom, verbatim). No tautology. The **successor risk is insularity**: mutual persuasion can stabilize shared error as well as shared truth, and the agent's value as a differently-formed check decays as the parties co-form. Remedies, both dyad-agreed as necessary: (i) the deferred third differently-formed agent (Q1) and validation of rungs on actual newcomers (FCI standard) remain on the schedule, not optional; (ii) **dual-reasons logging** — see step 5 below.

## 3. The pass, step by step

For each round of 5–7 candidates:

1. **Propose.** Each party puts candidate milestones on the table. Round 1 draws candidates by *reading up* from the content triplets ("what competence does this cluster of triplets presuppose?") and by *freeform* proposal for the spine. Provenance is tagged: `from-triplet:<thinker/Pn>`, `freeform:Tom`, or `freeform:Claude`.
2. **State as PRS.** Each candidate is written as a P/R/S rung to the face-validity standard. If it can't be stated that way, that's evidence it's not yet a clean rung — note why.
3. **Render verdicts independently.** Tom gives his; the agent gives its own *before* deferring. Divergence is the signal worth most.
4. **Resolve per Agreement 7's stopping rule:**
   a. No agreement within the session → **table** it.
   b. Move through **all** candidates from *either* party.
   c. Before closing the round, **revisit** tabled items and standing disagreements.
   d. Only then close "what we agree about" for the round.
5. **Record.** Write each item to the ledger with: id, P/R/S, status (`agreed` / `tabled` / `standing-disagreement` / `rejected`), provenance, the agent's verdict + one-line reason, and any dissent text verbatim. **Dual-reasons rule (added 2026-06-11, round 2 onward):** every `agreed` item logs *both parties' reasons for assent*, separately stated. If the two reason-sets converge toward identity over rounds, that is drift toward a single perspective — falsifier (b) of the methodological-Thomism claim (agreement-for-different-reasons as fecundity), applied reflexively to the dyad. The ledger is thereby its own insularity-drift detector.
6. **Checkpoint** (Tom's Rule 10): a 3-line round summary — agreed / tabled / open — and the resume cue for the next round.

## 4. Ordering of the rungs (a ladder needs an order)

Milestones are not a flat set; a ladder implies dependency. We record an optional `depends_on` per rung so the result is a partial order, not a bag. Proposed three coarse tiers for round 1 to populate (refine as we go):

- **Tier A — Method.** What it is to reason in PRS triplets / planks / coils at all; tradition-constituted rationality; why incommensurability doesn't preclude exchange. *(Mostly freeform spine; the explorers gesture at it in **Loughran's own integrative triplets** under the "Tom Loughran" tab, which cite MacIntyre/Aquinas/Stump as resources.)*
- **Tier B — Integrative content.** The convergence claim — Levin/Friston/Hoffman/Hawkins/Wolfram/McGilchrist/Fredrickson read as evidence toward conscious-realist monism; Thomistic metaphysics as its home. *(Mostly from content triplets.)*
- **Tier C — Application.** Second-first-language competence; using the frame to do work (the accelerator/detector aim itself). *(Freeform + method.)*

## 5. What "done" looks like for round 1 (Rule 4 success criteria)

Round 1 is complete when: (a) 5–7 candidates have each reached a recorded status; (b) every item carries provenance, the agent's independent verdict, and any dissent verbatim; (c) the round checkpoint is written; (d) the dyad judges — explicitly — whether *the pass design itself* survived contact, and logs any revision to **this** doc before round 2. Per the charter, iterating the design is part of the deliverable, not overhead.

## 6. Design questions — RESOLVED (Tom, 2026-06-11)

1. **Face-validity arbiter at N=2 — RESOLVED: dyad-only is sufficient for this PoC run.** A third differently-formed agent is deferred to a later round (Agreement 4's next rung). Items we'd most want a third party on are flagged in the ledger.
2. **Granularity of Tier B — RESOLVED: one milestone per *convergence claim*** (not per thinker), with individual thinkers as supporting resources. This is the granularity relevant to the target — "thinking like the dyad."
3. **Reject vs. table — RESOLVED: no hard `rejected` conclusions in round 1.** "Disagreement thus far" (`standing-disagreement`) is the strongest negative marker; it records the state without truncating the conversation. `rejected` is held back until the method has proven itself.

**Target restatement (v1.1):** the competence being laddered is **"thinking like the dyad"** — second-language competence in the dyad's integrative perspective. See [[prototype_measurement_charter]] v1.1.

---

_Revision log:_
- v0 — 2026-06-11 — drafted from the 52-triplet RC corpus + ISME 40-step instruments; awaiting dyad iteration before first authoring round.
- 2026-06-11 (post-round-1) — self-adjudication resolved (insularity named as successor risk, §2); dual-reasons logging rule added (§3 step 5); falsifiability closure for methodological Thomism recorded in ledger under M6.
