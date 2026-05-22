SEARCH-AGAINST-ASSUMPTION-127:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-127
  Original statement: "Wiki agent daily run 2026-05-13 network delta +7 PRS / +8 CROSS / +7 findings; 3 new HIGH escalations; network state 213 PRS / 86 cross / 33 findings"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-127
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from daily run output
      15b: Searched for counter-evidence on 3-HIGH-in-one-day as criterion-drift indicator
    Current status: CHALLENGED

  Sources:
    1. Shewhart (1931) / Wheeler (2000) statistical process control — 3 HIGH in a day is meaningful only against a baseline distribution; without baseline, it is data without inference.
    2. Goodhart (1975) — escalation rate as a measure that has become a target invites criterion drift.
    3. Classifier-drift literature (Webb et al. 2016 "Characterizing concept drift") — sudden shifts in classifier output rates are textbook indicators of criterion drift.
    4. C2A2-internal SELF-MEASUREMENT Goodhart cluster (PRESUMPTION-160 paired) — this is a recurring pattern.
    5. Operations metrics literature: monotone-good metrics (Allspaw 2012) — "more findings = better detection" is a recognized failure mode.

  Strength of challenge: Moderate

  Summary: The factual counts are not challenged, but the interpretive framing ("3 HIGH = normal output") lacks the baseline normalization that statistical process control would require. Criterion drift is the canonical concern when classifier output rates shift suddenly. The SELF-MEASUREMENT Goodhart cluster is the structural concern — single-instance treatment of 3-HIGH as content density underdetermines whether the system's criteria are stable. Moderate challenge.

  Specific risks: (a) Criterion drift undetected; (b) Goodhart cluster recurrence; (c) Monotone-good metric interpretation; (d) No baseline.

  Mitigations available: (a) Build per-day baseline; (b) Statistical process control on HIGH escalation rate; (c) Spot-check FINDING-025/029/030 for criterion stability; (d) Sample HIGH escalations from prior weeks for comparison.

  Recommendation: CHALLENGED (Moderate) — counts are recorded but interpretation lacks baseline; criterion drift is the load-bearing concern

  STEELMAN:
    Item: ASSUMPTION-127
    Strongest counterargument: Recording the counts is fine, but the implicit "3 HIGH = normal" interpretation lacks the baseline that statistical process control would require. Sudden shifts in classifier output rates are the textbook signal of criterion drift; without baseline comparison, the system cannot distinguish content-density-up from criterion-loosened. The SELF-MEASUREMENT Goodhart cluster (recurring) is the structural concern: when escalation rate becomes a tracked metric, it tends to drift. The conservative move is to build a per-day baseline, flag deviations explicitly, and require a periodic criterion-stability audit on the HIGH escalation set.
    What would need to be true for C2A2 to be safe: (a) Per-day baseline established; (b) Control-limits set; (c) Criterion-stability audit cadence.
    How to test: Build baseline from historical daily runs; compute control limits; check whether 3-in-a-day is within or beyond.
