SEARCH-AGAINST-ASSUMPTION-442:
  Date searched: 2026-07-12
  Original item: ASSUMPTION-442
  Original statement: "Form-check-only PRS-id QC (wiki unmounted) is an acceptable degraded mode provided a deferred spot-check compensates."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-442
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-11 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Vaughan, D., 1996. "The Challenger Launch Decision" — via Wikipedia/Grokipedia "Normalization of deviance" and legal/organizational reviews. — The canonical mechanism: deviations accepted because they produce no immediate bad outcome become the operating baseline. A degraded QC mode that keeps passing (because its reduced checks can't see the defects) is self-normalizing by construction.]
    2. [Enticott, J. et al., 2022. "A qualitative systematic review on the application of the normalization of deviance phenomenon within high-risk industries." Journal of Safety Research 83:119-131. — Across high-risk industries, procedural shortcuts repeated for production benefit become invisible as deviations; the enabling conditions are exactly those here: no immediate loss signal, production pressure, and no forcing function to restore full mode.]
    3. [Banja, J., 2010. "The normalization of deviance in healthcare delivery." Business Horizons 53(2). — Deferred compensating actions are the weak link: compensation that depends on somebody remembering later reliably decays; the system's own postmortem-completion data (<40% of tracked action items completed in 90 days, cited in DISPOSITION-453) is the local base rate for "deferred spot-check compensates."]
  Strength of challenge: Strong
  Summary: The graceful-degradation pattern is fine; this instance is missing every safeguard the pattern requires. The degraded mode's outputs are indistinguishable from full-mode outputs (P-471: same last_qc_at stamp), so nothing marks the debt; the compensating spot-check is deferred with no owner or trigger, in a system whose measured action-item completion is under 40%; and real id-drift was confirmed the same morning, meaning the degraded mode is already passing defective pairs. Under normalization-of-deviance dynamics, "acceptable degraded mode" without a restoration forcing-function is the documented first step of permanent quality erosion.
  Specific risks: Form-check-only passes accumulate in the same namespace as full passes; id-drift spreads silently; when eventually discovered, there is no record of which pairs got which depth — the entire QC history becomes suspect (pairs with P-471).
  Mitigations available: Namespace the stamp (qc_mode field); make the deferred spot-check a queued task with a date and owner rather than an intention; bound the degraded mode (max N runs before forced full pass).

  STEELMAN:
    Item: ASSUMPTION-442
    Strongest counterargument: "Acceptable provided a deferred spot-check compensates" assumes the compensation executes, but the system's own measured follow-through rate makes non-execution the base-rate outcome. A degraded mode whose debt is unmarked (uniform stamp) and whose compensation is unenforced is not a degraded mode in the safety-engineering sense — it is normalization of deviance with a plan to feel bad about it later. The same-morning id-drift confirmation removes any doubt that the reduced checks have real misses.
    What would need to be true for C2A2 to be safe: Degraded passes are distinguishable in metadata; the spot-check is scheduled, owned, and blocking on some downstream milestone; the degraded mode has a bounded lifetime.
    How to test: Run the Days-239/240 spot-check on a mounted run and measure id-drift incidence among form-check-only pairs; simultaneously audit whether any past deferred compensating check in this system was actually executed.
  Recommendation: CHALLENGED
