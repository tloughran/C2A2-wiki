SEARCH-AGAINST-PRESUMPTION-542:
  Date searched: 2026-07-25
  Original item: PRESUMPTION-542
  Original statement: [inferred] A 15d monthly re-check returning "ACTIVE, no change" is presumed genuine re-validation, but a staleness-triggered re-stamp may certify only "not-yet-expired," not "re-tested against current state."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a time-triggered re-check read as re-confirmation
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. ISO recertification design. — Cuts both ways: a properly designed periodic re-check (the Year-3 recertification audit) DOES re-exercise the assertion against current state. So "time-triggered re-check = mere re-stamp" is not necessary; it is a property of a BADLY designed re-check. If 15d re-computes the underlying figure, the presumption does not apply.
    2. Condition-based vs calendar-based maintenance literature. — Calendar-triggered checks are criticized for exactly this, but the fix (and common practice) is to attach a substantive test to the trigger, not to abandon periodic review. The trigger and the test are separable; a calendar trigger can gate a real test.
    3. Monitoring/observability practice. — A scheduled health check that re-runs the probe is genuine re-validation; the anti-pattern is only the check that returns cached status. Whether 15d caches or re-probes is an empirical, fixable implementation detail.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is narrow but real: the presumption is only true if 15d's monthly re-check fails to re-compute the underlying measurement. A staleness trigger is not inherently recency-theatre — it can gate a substantive re-test. The presumption should therefore be scoped to "IF the re-check only advances the date," which is an implementation question answerable by inspection, not a standing defect.

  Specific risks: Over-reading could discredit periodic review generally, when the actual fix is cheap (make the re-check re-probe).

  Mitigations available: Require every 15d re-check to re-run at least one underlying measurement and record the recomputed value, not just a new date — converting a re-stamp into a re-test.

  STEELMAN:
    Item: PRESUMPTION-542
    Strongest counterargument: Recency and re-confirmation are genuinely distinct (the support side is strong), BUT the remedy is to instrument the re-check, not to distrust all periodic review; a calendar trigger gating a real re-probe is fully valid re-validation.
    What would need to be true for C2A2 to be safe: 15d re-computes the governing measurement on each re-check and logs the recomputed value.
    How to test: inspect 15d's monthly re-check code/log — does "ACTIVE, no change" carry a freshly recomputed figure or only an updated date?

  Recommendation: PARTIALLY-CHALLENGED
