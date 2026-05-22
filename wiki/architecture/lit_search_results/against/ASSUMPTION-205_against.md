SEARCH-AGAINST-ASSUMPTION-205:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-205
  Original statement: "Cross-tradition convergence is analogical not verbatim — only 3 literal shared-resource hubs (max 2 traditions each)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-205
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: claim that convergence across traditions is analogical/structural rather than literal, evidenced by only 3 literal shared-resource hubs.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Christen (2012) "Data Matching" (entity resolution). — Literal string-match counts are method-dependent; "only 3 literal hubs" may be a normalization artifact (PRESUMPTION-228), so the cited evidence is weak.
    2. Boyd & Crawford (2012) on measurement framing. — A count is shaped by what you choose to match; the artifact risk challenges using the count as evidence.
    3. (Weak) Some convergence IS literal (shared formal results, e.g., a theorem cited across fields), so "analogical not verbatim" is not exhaustive.

  Strength of challenge: Weak-Moderate

  Summary: There is no credible literature against the core principle (convergence is mainly analogical) — that is well established. The challenge is narrower and real: the specific evidence offered (3 literal hubs) is measurement-dependent and should not be load-bearing (PRESUMPTION-228). Also, 'analogical not verbatim' slightly overstates — some convergence is literal (shared formal results).

  Specific risks: If DECISION-040 relies on the literal-hub count rather than the principle, it rests on an artifact.

  Mitigations available: Ground the principle on analogy theory, not the count; run entity-resolution sensitivity analysis (PRESUMPTION-228) before the count informs DECISION-040.

  Recommendation: PARTIALLY-CHALLENGED (measurement only)

  STEELMAN:
    Item: ASSUMPTION-205
    Strongest counterargument: The principle is fine, but the sentence fuses a robust theoretical claim with a fragile empirical one ('only 3 literal hubs'); a critic should refuse the fused claim and demand the count be treated as artifact-prone until entity resolution is run.
    What would need to be true for C2A2 to be safe: The validated premise is scoped to the analogical principle and the count is quarantined to PRESUMPTION-228.
    How to test: Vary naming/normalization and re-count hubs; if unstable, the count is method-dependent.
