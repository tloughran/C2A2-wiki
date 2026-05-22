SEARCH-AGAINST-PRESUMPTION-228:
  Date searched: 2026-05-21
  Original item: PRESUMPTION-228
  Original statement: "The "3 literal hubs" finding reflects the territory, not the resource-naming/normalization method (measurement-artifact risk)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-228
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred: the '3 literal shared-resource hubs' finding is treated as reflecting the territory, not the resource-naming/normalization method used to count them.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Furnas et al. (1987) "The vocabulary problem." — Independent authors name the same resource differently; literal matching massively undercounts and is naming-dependent.
    2. Christen (2012) "Data Matching" (entity resolution). — String-match counts are artifacts of normalization choices; without entity resolution, counts are unreliable.
    3. Knowledge-graph entity normalization/synonymy literature. — Overlap counts are highly sensitive to canonicalization; "3 hubs" is plausibly a normalization artifact.
    4. In-system: joins the prior measurement-integrity findings (PRESUMPTION-212, lit-pipeline FLAG A) where counts diverged from ground truth.

  Strength of challenge: Strong

  Summary: The challenge is strong: literal string-match hub counts are well known to be naming/normalization artifacts (vocabulary problem; entity resolution), so 'only 3 literal hubs' likely reflects the matching method rather than the territory. This directly threatens the evidence basis for ASSUMPTION-205 and feeds DECISION-040; it belongs to the measurement-integrity cluster (FLAG A).

  Specific risks: DECISION-040 ('convergence is analogical') could be firmed on an artifactual count; the true number of literal hubs could be higher or lower under different normalization.

  Mitigations available: Run entity resolution / normalization; do a sensitivity analysis varying naming/canonicalization and report the count's stability; do not let the raw count inform DECISION-040 until stabilized.

  Recommendation: CHALLENGED (strong)

  STEELMAN:
    Item: PRESUMPTION-228
    Strongest counterargument: '3 literal hubs' is exactly the kind of number the vocabulary problem and entity-resolution literature warn against trusting — the count is a function of how resources are named and normalized, not of the territory, so without a sensitivity analysis it cannot support DECISION-040 and may be an artifact like the prior count discrepancies (FLAG A).
    What would need to be true for C2A2 to be safe: The count is shown stable across reasonable normalization schemes (or entity resolution is applied).
    How to test: Re-count hubs under >=3 normalization schemes; instability proves method-dependence.
