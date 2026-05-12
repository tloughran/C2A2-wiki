SEARCH-AGAINST-PRESUMPTION-114:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-114
  Original statement: "Master-narrative-gap cause attribution presumed most-likely the daemon link-count = 1 bug over alternative failure modes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-114
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 cause-attribution: most-recently-discussed bug class assumed most-likely cause
      15b: Searched for counter-evidence on alternative-explanations enumeration
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Tversky & Kahneman (1974) — availability heuristic ("most-recently-discussed = most-likely") is documented attribution bias; counter-evidence is empirical.
    2. Pearl (2009) "Causality" — most-likely-cause attribution requires probabilistic-comparison across enumerated alternatives.
    3. Zeller (2009) "Why Programs Fail" — first-cause-hypothesis must be testable; preferring recency-tagged hypothesis without elimination is documented anti-pattern.
    4. Allspaw (2012) "Blameless Postmortems" — proximate-cause attribution requires alternative-cause enumeration; recency-priority is documented as availability bias.
    5. C2A2-internal: ASSUMPTION-092 (regression hypothesis, PARTIALLY-SUPPORTED with explicit alternative-cause enumeration caveat) — the presumption is exactly the gap that ASSUMPTION-092's caveat flags.

  Strength of challenge: Strong

  Summary: Recency-priority cause attribution is documented availability bias. Causal-inference, judgment-under-uncertainty, debugging, and SRE-postmortem literatures uniformly require alternative-cause enumeration before "most-likely" framing. The presumption short-circuits the very enumeration step that ASSUMPTION-092's PARTIALLY-SUPPORTED disposition flagged.

  Specific risks: (a) Misattribution leads to mis-fix; (b) actual cause goes undiagnosed; (c) compounds with ASSUMPTION-092 — both items together short-circuit alternative-cause enumeration.

  Mitigations available: (a) Alternative-cause enumeration before attribution commitment; (b) diagnostic probe to distinguish causes; (c) reframe as "working hypothesis" rather than "most-likely cause".

  Recommendation: CHALLENGED — recency-priority cause attribution is documented availability bias.

  STEELMAN:
    Item: PRESUMPTION-114
    Strongest counterargument: "Most-recently-discussed = most-likely-cause" is the canonical availability-bias trap. Causal inference, debugging, SRE postmortem literatures uniformly require alternative-cause enumeration. The presumption short-circuits exactly the step that ASSUMPTION-092's PARTIALLY-SUPPORTED disposition explicitly flagged.
    What would need to be true for C2A2 to be safe: (a) alternative-cause enumeration; (b) diagnostic probe; (c) hypothesis-not-attribution framing.
    How to test: List 3 alternative causes for the master-narrative gap; check log evidence for each; if evidence rules out alternatives, attribution is supported; if not, presumption is empirically refuted.
