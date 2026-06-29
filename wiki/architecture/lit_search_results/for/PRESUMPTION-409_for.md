SEARCH-FOR-PRESUMPTION-409:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-409
  Original statement: "That a deterministic harvest preserves the meaning of each card's signals - 158/158 coverage measures presence, not semantic fidelity"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-409
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: coverage presumed to imply semantic fidelity of harvested signals
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Wrapper-based extraction over templated sources. - Where the source is highly regular, presence and correct meaning are tightly coupled, so for templated cards a complete deterministic harvest may also be largely faithful.
    2. Deterministic-parsing reproducibility. - A deterministic transform yields the same mapping every run, so fidelity, if validated once on a sample, is stable thereafter.

  Strength of support: Weak

  Summary: The claim that a deterministic harvest "preserves meaning" has weak, conditional support: on genuinely templated input, extraction success correlates strongly with semantic correctness, and determinism makes any validated fidelity stable across runs. But this support is contingent on regular input and on at least one fidelity audit; it does not follow from the 158/158 coverage figure itself, which measures presence (see 15b). The presumption's own caveat - coverage != fidelity - is the better-supported reading.

  Caveats: Support requires a sample audit confirming meaning; coverage alone cannot establish fidelity. Format drift breaks the presence-fidelity coupling.

  Search scope: Extraction precision/recall; coverage vs correctness; sample-audit methodology. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
