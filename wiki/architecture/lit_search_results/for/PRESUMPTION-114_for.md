SEARCH-FOR-PRESUMPTION-114:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-114
  Original statement: "Master-narrative-gap cause attribution presumed most-likely the daemon link-count = 1 bug over alternative failure modes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-114
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 cause-attribution: most-recently-discussed bug class assumed to be most-likely cause without enumeration
      15a: Searched for supporting literature on causal-attribution heuristics and recency bias
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Pearl (2009) "Causality" — most-likely-cause attribution requires probabilistic-comparison across enumerated alternatives; recency-of-discussion is not a literature-supported attribution criterion.
    2. Tversky & Kahneman (1974) "Judgment under Uncertainty" — availability heuristic (most-recently-discussed = most-likely-cause) is documented attribution bias.
    3. Software-debugging literature (Zeller 2009 "Why Programs Fail") — first-cause-hypothesis must be testable; preferring recency-tagged hypothesis without elimination of alternatives is documented anti-pattern.
    4. SRE postmortem practice (Allspaw 2012) — proximate-cause attribution requires alternative-cause enumeration and elimination, not recency-priority.
    5. C2A2-internal: ASSUMPTION-092 (regression hypothesis as working assumption) — companion ASSUMPTION already PARTIALLY-SUPPORTED with explicit caveat on alternative-cause enumeration; the presumption inherits that gap.

  Strength of support: None — recency-priority cause attribution is documented availability bias.

  Summary: Supportive literature for "most-recently-discussed bug class is most-likely cause" does not exist. Causal-inference, judgment-under-uncertainty, debugging, and SRE-postmortem literatures uniformly require alternative-cause enumeration and probabilistic comparison; recency-priority is documented as availability bias. The presumption short-circuits the elimination step that ASSUMPTION-092's PARTIALLY-SUPPORTED disposition flagged as the standard guard.

  Caveats: (a) The presumption may be operationally correct in this specific case (the daemon bug may in fact be the cause), but as a default attribution method it is unsupported; (b) supportive literature treats recency as a starting hypothesis, not as endpoint attribution; (c) NO-SUPPORT here is uniformly active recommendation against the pattern.

  Recommendation: NO-SUPPORT-FOUND — recency-priority cause attribution is documented bias; alternative-cause enumeration is canonical
