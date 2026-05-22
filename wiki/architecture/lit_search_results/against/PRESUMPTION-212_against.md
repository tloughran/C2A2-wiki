SEARCH-AGAINST-PRESUMPTION-212:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-212
  Original statement: "The documented number == the true number — registers presumed consistent and current."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-212
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — documented counts (CLAUDE.md, PRS registers) trusted as current and consistent with the artifacts they describe.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Parnas, D. (1994). "Software Aging." — Documentation drifts from reality absent active reconciliation; documented != true is the default, not the exception.
    2. Redman, T. (2001). "Data Quality." — Registers diverge from ground truth continuously; trusting documented figures without validation is a primary data-quality failure.
    3. Observed instances: ASSUMPTION-192 (CLAUDE.md viz stats stale) and ASSUMPTION-193 (231-vs-225 PRS divergence). — Same-cycle, in-system confirmations that documented != true here and now.

  Strength of challenge: Strong

  Summary: The challenge is strong and already realized this very cycle: ASSUMPTION-192 (stale viz stats) and ASSUMPTION-193 (231-vs-225 divergence) are direct instances of documented != true. Software-aging and data-quality literature treat documented==true as a property that decays without active reconciliation. Presuming registers are consistent and current is the meta-pattern behind both of today's measurement-integrity defects. Sits in SYSTEMIC-RISK-FLAG A.

  Specific risks: Decisions made on stale registers (e.g., the payload-diet deferral on stale stats); Pattern Detector fed divergent counts; compounding measurement-integrity errors.

  Mitigations available: Auto-derive documented figures from artifacts (couples PREMISE-040); add register-vs-artifact reconciliation checks in CI; alarm on divergence; treat documented numbers as claims to verify.

  Recommendation: CHALLENGED (REVISE)

  STEELMAN:
    Item: PRESUMPTION-212
    Strongest counterargument: Documented==true is a property that decays the moment the artifact changes and the doc does not; this cycle already produced two instances (stale viz stats, 231-vs-225). Presuming registers are current is the meta-error generating the day's measurement-integrity defects.
    What would need to be true for C2A2 to be safe: Safe once documented figures are auto-derived from artifacts and reconciled in CI, so equality is enforced rather than presumed.
    How to test: Diff every documented count against an artifact-derived recount; any nonzero diff (already present) falsifies the presumption.
