SEARCH-AGAINST-PRESUMPTION-409:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-409
  Original statement: "That a deterministic harvest preserves the meaning of each card's signals - 158/158 coverage measures presence, not semantic fidelity"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-409
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: coverage presumed to imply preserved meaning of signals
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Coverage-vs-correctness distinction. - A 158/158 completeness gate measures that an output exists per input; it is logically independent of whether the output's MEANING is correct, so it cannot establish semantic fidelity.
    2. Silent mis-parse failure mode in rule-based extraction. - Deterministic harvesters can map a field to the wrong value on edge layouts while still emitting a value (full coverage), so meaning can be lost with zero coverage signal.
    3. Validation-beyond-completeness / sample-audit methodology. - Fidelity claims require a precision audit on labelled samples; completeness gates are necessary-not-sufficient.

  Strength of challenge: Moderate

  Summary: The presumption that the harvest "preserves meaning" is challenged precisely because the only evidence offered (158/158) measures presence, not correctness. Deterministic extraction can be complete and semantically wrong simultaneously, and nothing in a coverage metric would reveal it. The literature is clear that fidelity must be measured separately via a sample/precision audit; without one, meaning-preservation is asserted, not demonstrated.

  Specific risks: Wrong-but-present signals treated as faithful; cross-tradition analysis built on mis-mapped fields; a completeness gate that cannot fail on meaning gives false confidence (shared vulnerability with ASSUMPTION-380).

  Mitigations available: Random-sample precision audit against hand labels; field-level validators / range checks; drift canaries; report audited fidelity, not just coverage.

  STEELMAN:
    Item: PRESUMPTION-409
    Strongest counterargument: Completeness and correctness are orthogonal; a harvester that emits one value per card is 158/158 by construction whether or not any value is right, so "preserves meaning" is an unverified leap from a metric that cannot detect meaning errors.
    What would need to be true for C2A2 to be safe: A precision audit on a labelled sample shows extracted signals match intended meaning, and drift canaries guard against silent layout changes.
    How to test: Hand-label a random subset and compute field-level precision; deliberately feed a drifted layout and confirm the gate still reads 158/158 (demonstrating blindness to meaning).

  Search scope: Coverage vs correctness; silent mis-parse; sample-audit. Comprehensive.

  Recommendation: CHALLENGED
