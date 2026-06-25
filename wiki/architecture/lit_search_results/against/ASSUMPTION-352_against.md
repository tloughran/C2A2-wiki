SEARCH-AGAINST-ASSUMPTION-352:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-352
  Original statement: "Self-testing is non-vicious iff the falsifier is specified independently of the tested outcomes (register, then look)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-352
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; load-bearing for the whole falsifier; discharges REVISE-111
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Gassen 2023 (field experiment on preregistration). - Vague/non-exhaustive preregistrations leave substantial residual researcher degrees of freedom; register-then-look is necessary but far from sufficient.
    2. Bakker et al. 2020 / Claesen et al. 2021. - Many preregistrations are insufficiently specific and are deviated from undisclosed; the discipline often fails in practice.
    3. Auditor-independence principle: specifying a falsifier does not supply PERSONNEL independence; the same agent designing and grading retains discretion (ties PRESUMPTION-394).

  Strength of challenge: Moderate

  Summary: The 'iff' is too strong. Independent specification of the falsifier is necessary but the literature shows it is not sufficient: unless the falsifier is exhaustively and precisely specified (analysis path, thresholds, exclusions), residual degrees of freedom re-enter at scoring time, and self-administered tests retain personnel-independence problems regardless of specification. Pre-registration reduces viciousness; it does not, by itself, guarantee non-viciousness.

  Specific risks: A loosely specified falsifier could be treated as a guarantee of non-viciousness while still leaking degrees of freedom at execution, giving false confidence in the self-test.

  Mitigations available: Make falsifier specs exhaustive (pre-commit thresholds, exclusions, analysis path); add personnel/blind independence where possible; log all deviations.

  STEELMAN:
    Item: ASSUMPTION-352
    Strongest counterargument: Register-then-look removes ONE class of bias (outcome-dependent criterion choice) but not others (under-specified scoring, undisclosed deviations, self-grading), so 'non-vicious iff independent falsifier' overpromises; viciousness is reduced on a spectrum, not eliminated by a single condition.
    What would need to be true for C2A2 to be safe: The falsifier is specified exhaustively enough that no scoring discretion remains, and deviations are logged and visible.
    How to test: Have a third party attempt to 'game' the registered falsifier; if they find latitude, the spec is insufficient.

  Search scope: Preregistration-specificity critiques; auditor independence. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
