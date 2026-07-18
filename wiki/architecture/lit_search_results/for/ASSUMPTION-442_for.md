SEARCH-FOR-ASSUMPTION-442:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-442
  Original statement: "Form-check-only PRS-id QC (wiki unmounted) is an acceptable degraded mode provided a deferred spot-check compensates."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-442
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [Risknowlogy, "Graceful Degradation — Degraded Mode in Safety Systems." — Safety engineering explicitly endorses predefined degraded modes: when resources are unavailable, the system keeps its most important functions running in a deliberate, designed, auditable reduced state rather than halting. Supports the principle that a reduced-depth QC pass beats no QC pass.]
    2. [SRE School, "Comprehensive Tutorial on Graceful Degradation in Site Reliability Engineering" (2026). — SRE doctrine: degraded modes are legitimate when priorities, triggers, and behaviours are designed up front and verified, so the degraded state is deliberate and auditable, not accidental. Conditional support: acceptability hinges on the degraded state being explicit and tracked.]
    3. [Dev3lop, "Resilient Pipeline Design with Graceful Degradation." — Data-pipeline analogue: degraded modes defer non-critical operations and reconcile them later via compensating actions (deferred writes, compensating transactions). Direct precedent for the "deferred spot-check compensates" structure — provided the compensating action reliably executes.]
  Strength of support: Moderate
  Summary: Graceful-degradation doctrine across safety engineering, SRE, and pipeline design supports operating a reduced-depth verification mode when a dependency (the mounted wiki) is unavailable, and supports pairing it with a compensating action to restore full assurance afterward. The support is strictly conditional on three design properties the literature treats as constitutive: the degraded mode is predefined, its outputs are distinguishable from full-mode outputs (auditable), and the compensating action is enforced rather than aspirational. Where those hold, form-check-only QC with a deferred spot-check is a textbook pattern.
  Caveats: All three conditions are load-bearing. The same 07-11 session that produced this assumption also surfaced PRESUMPTION-471 (degraded pairs share the same last_qc_at stamp as full pairs), which negates the auditability condition as currently implemented. Support applies to the pattern, not necessarily to the present implementation.
  Recommendation: PARTIALLY-SUPPORTED
