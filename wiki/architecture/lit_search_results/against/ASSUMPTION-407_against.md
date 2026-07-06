SEARCH-AGAINST-ASSUMPTION-407:
  Date searched: 2026-07-03
  Original item: ASSUMPTION-407
  Original statement: "Preregistration-before-run should be enforced as a machine gate (Appendix G Stage 2 invariant)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-407
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-02 Inter-Tradition Dialogue Study (preregistration enforcement invariant)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Adherence studies (Claesen et al., 2021, "Comparing dream to reality," PMC8548785; Psychological Science adherence review). — Undisclosed deviations from preregistered plans are frequent (majority of studies deviate without disclosure). Enforcing prereg-before-run does nothing to stop deviation at the analysis/reporting stage, where the leakage actually happens.
    2. Szollosi et al., 2020, "Is preregistration worthwhile?"; Devezer et al. — Preregistration does not by itself improve inference and can create a false sense of rigor; strong theory matters more than procedural gates.
    3. "Are Preregistration and Registered Reports Vulnerable to Hacking?" (PMC7757516). — Registered/gated plans can still be gamed; a machine gate that checks existence/timing cannot detect a strategically vague or hacked plan.
    4. Survey on preregistration workflow (Royal Society Open Science, rsos.211997). — Mixed evidence on reducing p-hacking/HARKing; benefits are real but partial and workload-heavy; hard gating can incentivize minimal/uninformative preregistrations that satisfy the gate without constraining behavior.

  Strength of challenge: Moderate

  Summary: The challenge is to the sufficiency and framing of "enforce as a machine gate." Empirically, enforcement of the *timing* invariant does not secure the *goal* (constrained researcher degrees of freedom): undisclosed analysis-stage deviations are the norm, gates can be satisfied by vague plans, and preregistration's effect on p-hacking/HARKing is mixed. A gate that guarantees ordering can produce false assurance that the study is confirmatory when the binding constraint (honest adherence) is unenforced.

  Specific risks: The Stage-2 invariant could certify runs as "preregistered" while the actual analyses drift; the gate becomes a compliance ritual that launders exploratory analysis as confirmatory.

  Mitigations available: Pair the gate with adherence auditing (diff the executed analysis against the frozen plan and fail loud on undisclosed deviation); require specificity checks on the plan, not just its existence; label deviations transparently rather than blocking them.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Strongest counterargument: A machine gate enforces the one part of preregistration that is objectively checkable — the plan existed and was frozen before the run — and thereby removes the most common and most deniable abuse (retroactive "pre"registration). It doesn't claim to enforce honesty; it removes an excuse. Given automation, this cheap invariant strictly dominates voluntary norms.
    What would need to be true for C2A2 to be safe: The gate is understood as necessary-not-sufficient; an adherence diff and specificity check are added; "gated" is not conflated with "confirmatory."
    How to test: Compare frozen plan vs executed pipeline for each run; count undisclosed deviations that passed the gate. A nonzero count falsifies "the gate secures confirmatory status."
