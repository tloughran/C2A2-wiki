SEARCH-AGAINST-ASSUMPTION-107:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-107
  Original statement: "92% PRESUMPTION REVISE rate is highest single-cycle REVISE rate to date — record-density disposition signal exceeding yesterday's 75% prior peak"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-107
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD record-density observation
      15b: Searched for counter-evidence on REVISE-rate-as-record without batch normalization
    Current status: CHALLENGED

  Sources:
    1. Wheeler (2000) "Understanding Variation" — unnormalized cycle-over-cycle rate comparison is documented anti-pattern; SPC explicitly requires normalization disclosure for "record" framings.
    2. Bornmann & Mutz (2015) "Growth Rates of Modern Science" — bibliometric superlative-claims without batch-normalization are documented artifact-generators rather than signals.
    3. Goodhart (1975); Strathern (1997) — record-tracking as the metric of interest is canonical Goodhart precondition.
    4. Kahneman (2011) — extremity-attraction bias: cycle-records receive disproportionate attention even when within ordinary variance.
    5. C2A2-internal: PRESUMPTION-116 (REVISE 2026-05-10) was the upstream cluster-density superlative-without-normalization REVISE; PRESUMPTION-129 (this cycle) is the second-layer recurrence — ASSUMPTION-107 is the paired stated-claim asserting the same superlative.

  Strength of challenge: Strong

  Summary: The challenge is strong. The 92% > 75% comparison is unnormalized for batch composition and is therefore non-rigorous by SPC, bibliometric, and Goodhart literatures. PRESUMPTION-116 was REVISE'd for the same anti-pattern yesterday; PRESUMPTION-129 (this cycle) extends to second-layer recurrence. ASSUMPTION-107 is the explicit-statement counterpart — naming the record without acknowledging the normalization-gap. The challenge is well-supported across multiple converging literatures.

  Specific risks: (a) Record-framing reifies an unnormalized comparison as a finding; (b) Goodhart vulnerability — system may optimize REVISE-rate to reproduce the record; (c) cluster-recurrence (PRESUMPTION-116, PRESUMPTION-129, ASSUMPTION-107) constitutes documented anti-pattern not converging across three layers; (d) downstream consumers may treat the rate as comparable to prior cycles when it is not.

  Mitigations available: (a) Per-item normalization (REVISE rate per item-complexity); (b) batch-composition disclosure (denominator, composition, prior distribution); (c) baseline reference distribution; (d) demote "record" framing to "observed value" without superlative.

  Recommendation: CHALLENGED (Strong) — same anti-pattern as PRESUMPTION-116/PRESUMPTION-129; the stated-claim form makes the framing harder to overlook than the implicit form

  STEELMAN:
    Item: ASSUMPTION-107
    Strongest counterargument: The numerical comparison is arithmetically valid but is unnormalized across heterogeneous batches and therefore non-rigorous. Cycle 2026-05-09 and 2026-05-10 differ in batch composition (different items, different complexity, different topic-mix). Raw rate comparison ignores these differences and treats the higher rate as a "record". By SPC and bibliometric discipline, this comparison cannot bear the "record" framing. Three converging cluster instances (PRESUMPTION-116, PRESUMPTION-129, ASSUMPTION-107) within a 48-hour window indicate the anti-pattern is not converging.
    What would need to be true for C2A2 to be safe: (a) Per-item-complexity normalization; (b) batch-composition disclosure; (c) baseline reference distribution; (d) demote "record" framing.
    How to test: Audit subsequent cycle-rate framings for normalization disclosure; track whether "record" framing recurs without normalization (4th-layer recurrence would trigger ASSUMPTION-098 three-recurrence threshold for this specific anti-pattern).
