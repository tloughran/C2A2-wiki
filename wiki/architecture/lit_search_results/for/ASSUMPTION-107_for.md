SEARCH-FOR-ASSUMPTION-107:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-107
  Original statement: "92% PRESUMPTION REVISE rate is highest single-cycle REVISE rate to date — record-density disposition signal exceeding yesterday's 75% prior peak"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-107
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD cycle-superlative observation
      15a: Searched for record-density disposition signals and metric-design superlative-claim audit literature
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Shewhart (1931) / Wheeler (2000) "Understanding Variation" — single-cycle records are interpretable only when normalized; raw rate cycle-over-cycle without batch-composition control is non-comparable.
    2. Newport & Drucker on attention-to-records — observing-the-record is operationally valid; treating-the-record-as-significant requires effect-size and reference-class.
    3. SRE post-mortem literature (Beyer 2016) — "record" framings are warranted as operator-attention signals but require accompanying disclosure of batch context (denominator, composition, prior-distribution).
    4. C2A2-internal: yesterday's "75% prior peak" comparison is per-item-rate not per-cycle aggregate; comparability is conditional on identical batch composition (unverified).
    5. Goodhart (1975) — record-tracking as the metric of interest is canonical Goodhart precondition.

  Strength of support: Weak-Moderate

  Summary: The observation that 92% > 75% is arithmetically valid; the "record" framing is operationally warranted as an attention-signal. The interpretive claim that this is a meaningful disposition signal requires batch-composition normalization that has not been disclosed. Literature supports record-observation as legitimate when paired with normalization disclosure; without normalization, the record framing is a Goodhart precondition. The signal is real (REVISE rate did increase); the calibration of significance is the gap.

  Caveats: (a) Batch composition differs between cycles (different items, different complexity) — direct rate comparison is non-rigorous; (b) "Highest single-cycle REVISE rate" is N=many-but-small (cycle counts in the tens) — record-by-chance probability is non-negligible; (c) Record-tracking as the metric of interest invites optimization-against-record (Goodhart); (d) PRESUMPTION-129 is the paired second-layer recurrence that REVISE'd "superlative-without-normalization" yesterday — same anti-pattern recurring.

  Recommendation: PARTIALLY-SUPPORTED (Weak-Moderate) — record-observation is canonical; significance-claim requires normalization disclosure that PRESUMPTION-129 captures as paired REVISE
