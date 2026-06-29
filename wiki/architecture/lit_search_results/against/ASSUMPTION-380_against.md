SEARCH-AGAINST-ASSUMPTION-380:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-380
  Original statement: "A deterministic rule-based harvest recovers the cross-tradition signal dataset with no model passes (158/158 coverage)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-380
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: deterministic harvest claimed to fully recover the dataset (158/158, no model)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Coverage-vs-correctness / completeness-gate literature. - 158/158 is a COVERAGE metric (every card produced an extraction); it does not measure whether the extracted values are SEMANTICALLY correct. A gate that can only ever read 100% (one output per input) cannot fail on meaning. (See PRESUMPTION-409.)
    2. Brittleness of rule-based extraction. - Deterministic wrappers silently mis-parse on format drift, edge layouts, or unanticipated variants, producing confidently wrong fields while still "covering" the card.
    3. Precision/recall distinction in IE. - High recall (coverage) with unmeasured precision is a known failure mode; reporting only coverage hides extraction errors.

  Strength of challenge: Moderate

  Summary: The challenge is not to deterministic harvesting per se but to what 158/158 proves. Coverage counts that an output was produced for every input; it is structurally incapable of detecting a wrong-but-present value, so it cannot certify the dataset was "recovered" in meaning. Rule-based parsers are brittle to drift and can mis-map fields silently. Without a precision/fidelity audit, the 158/158 claim overstates what was verified.

  Specific risks: Silently mis-parsed signals enter the dataset; a completeness gate that can only read 100% gives false confidence; downstream cross-tradition analysis built on wrong fields.

  Mitigations available: Add a sample audit measuring precision/semantic fidelity on a random subset; add format-drift canaries; report coverage AND audited-accuracy, never coverage alone.

  STEELMAN:
    Item: ASSUMPTION-380
    Strongest counterargument: 158/158 is a metric that cannot fail by construction - one output per card guarantees 100% coverage regardless of correctness - so it certifies presence, not recovery; the dataset could be fully "covered" and substantially wrong.
    What would need to be true for C2A2 to be safe: A sample audit shows extracted values are semantically faithful, and drift canaries catch layout changes that would silently corrupt parsing.
    How to test: Hand-label a random sample of cards and measure field-level precision against the deterministic harvest.

  Search scope: Coverage vs correctness; wrapper brittleness; precision/recall. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
