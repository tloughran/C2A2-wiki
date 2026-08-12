# PRESUMPTION-748 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-748

**Date searched:** 2026-08-10

**Original item:** PRESUMPTION-748

**Original statement:** The control arm does not exist and cannot be allocated; every agent has run with cross-tradition input since the first bridge note.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Original item:** PRESUMPTION-748
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred by asking, of a correctly-routed design decision, what asset the decision would allocate. There is none.
  - 15b: Searched for challenging literature on contamination, retrospective/synthetic controls, and falsifiability without an unexposed cohort.
- **Current status:** PARTIALLY-CHALLENGED

### Challenging evidence found: Partial

### Sources

1. **NIH Research Methods Resources, "Stepped Wedge Group-Randomized Trials"; Hemming & Taljaard, "Reflection on modern methods: when is a stepped-wedge cluster randomized trial a good study design choice?" *IJE* 49(3), 2020.** — Stepped-wedge designs are the closest methodological analogue to C2A2's situation: every unit is eventually exposed, so there is no permanently unexposed cohort. The literature explicitly flags within-cluster contamination (control-condition sites adopting the intervention early or intervention sites lapsing back) as a known, hard-to-eliminate bias in exactly this design family — this is a direct structural parallel to "every agent has run with cross-tradition input."
2. **[unverified — from search snippet] Overview of synthetic control methods (Abadie-style), including limitations discussion.** — Synthetic/retrospective controls require a "donor pool" of comparable untreated units whose pre-treatment trajectory resembles the treated unit and remains stable afterward (the "convex hull" and stability assumptions). If no untreated donor units exist at all — as PRESUMPTION-748 states — synthetic control cannot be constructed either; it is not a rescue for a genuinely absent control.
3. **General falsifiability literature (Popper-derived summaries) — [unverified — from search snippet].** — A claim is falsifiable only if it names, in advance, an outcome that would count against it. If the only cohort that could produce that counter-outcome (the unexposed arm) is structurally unobtainable, the prediction is falsifiable in principle but untestable in practice — precisely the gap PRESUMPTION-748 identifies as a risk.

### Strength of challenge: Moderate

### Summary

The literature on stepped-wedge trials strongly supports the presumption's core worry: designs where every unit is eventually exposed reliably suffer contamination and lose their comparative power, and methodologists treat this as a known, only partially mitigable limitation (transition periods, fixed-effects estimators with within-period comparisons) rather than a solved problem. Synthetic-control methods are sometimes proposed as a workaround, but they require an actual donor pool of untreated comparators; C2A2 has none, so this mitigation path is foreclosed, not just weakened. This corroborates rather than contradicts the presumption itself, but it also surfaces a boundary condition C2A2 hasn't addressed: even the standard methodological patches (transition windows, retrospective synthetic controls) assume *some* residual untreated data, which C2A2's own record shows does not exist.

### Specific risks for C2A2

If the presumption is accepted uncritically, C2A2 may report ASSUMPTION-909-style predictions as "tested and falsifiable" when in fact no design-available data could ever falsify them — producing false confidence in a headline claim (reduced overconfidence via cross-tradition exposure) that cannot be disconfirmed with current assets.

### Mitigations available

Stepped-wedge methodology suggests two partial mitigations: (a) treat early-vs-late-adopting agents as a rough proxy for a dose-response gradient rather than a true control, and (b) retrospectively reconstruct pre-bridge-note outputs (if logged) as a quasi-baseline, acknowledging this is a weaker, historically-confounded comparison, not a true control.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-748

**Strongest counterargument:** Methodologists who study stepped-wedge and synthetic-control designs would say the presumption understates the problem rather than overstates it: even the standard partial fixes (transition periods, donor pools, fixed-effects-within-period estimators) require some residual untreated data or comparable units, and C2A2's own account states no such asset exists at all ("66 agentic calls issued today alone across 14 traditions"). This means C2A2 is not merely missing a control — it lacks the minimal structural precondition (a donor pool, a pre-treatment window, or a transition period) that lets any known contamination-tolerant design produce a defensible causal estimate. The honest conclusion from the literature is that the ASSUMPTION-909 prediction is currently unfalsifiable in any rigorous sense, not just "harder to test."

**What would need to be true for C2A2 to be safe:** A logged pre-bridge-note baseline of agent outputs must exist and be usable as a genuine (if imperfect) pre-treatment period, and the system must be willing to report the resulting estimate as quasi-experimental with explicitly bounded confidence rather than as a clean falsification test.

**How to test:** Audit historical logs for any agent runs that predate "the first bridge note" cross-tradition input; if found, use them as a stepped-wedge-style pre-period baseline and report calibration/overclaiming metrics with explicit contamination caveats, rather than treating the comparison as a true RCT-style control.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-08-10

**Affected items:** PRESUMPTION-748, ASSUMPTION-909

**Common vulnerability:** Both depend on the availability of an unexposed/uncontaminated comparison condition that the system's own provenance record shows does not exist. ASSUMPTION-909 is explicitly blocked on PRESUMPTION-748 in the queue, confirming this is a single shared failure point, not two independent risks.

**Literature basis:** Stepped-wedge contamination literature (NIH SWGRT resource; Hemming & Taljaard 2020); synthetic control donor-pool/stability-assumption limitations.

**Risk level:** High

**Recommendation:** Do not report ASSUMPTION-909's prediction as tested until either a genuine pre-exposure baseline is located or the claim is explicitly reframed as untestable-in-practice rather than falsifiable.
