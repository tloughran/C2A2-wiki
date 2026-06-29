SEARCH-FOR-ASSUMPTION-380:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-380
  Original statement: "A deterministic rule-based harvest recovers the cross-tradition signal dataset with no model passes (158/158 coverage)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-380
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: deterministic harvest claimed to fully recover signals, 158/158, no model passes
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Wrapper-based / rule-based information extraction literature (Kushmerick et al. on wrapper induction). - Over regular, templated, semi-structured sources, deterministic pattern extraction achieves very high precision and recall and is fully reproducible.
    2. "Use code, not the model, when code can answer" engineering principle (deterministic transforms over deterministic structure). - Aligns with Rule-5: for structured input a parser is more reliable, cheaper, and auditable than an ML pass.
    3. Regex/grammar-based parsing of structured records. - When the source format is stable, deterministic parsing attains effectively complete coverage.

  Strength of support: Moderate

  Summary: For genuinely templated/semi-structured source cards, a deterministic harvest can achieve complete extraction coverage, and doing so without a model pass is the recommended, reproducible, auditable choice. The 158/158 figure is credible as a COVERAGE (extraction-success) result on regular input. Support is moderate and conditional on the source being regular; it speaks to completeness, not to semantic correctness (see caveats and PRESUMPTION-409).

  Caveats: Support is for COVERAGE/completeness, not semantic FIDELITY. Rule-based extraction is brittle to format drift; 158/158 measures presence, not correctness. A sample audit of meaning is required to claim fidelity.

  Search scope: Rule-based vs ML IE; wrapper induction; deterministic parsing. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
