SEARCH-AGAINST-PRESUMPTION-377:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-377
  Original statement: "That inbound-backlink count is the right proxy for graph health at all (connectivity measured, synthesis quality never)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-377
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the audit measured connectivity throughout and never measured synthesis quality
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Vanity-metrics / Goodhart's Law (Amplitude/Cutler; arXiv 1809.07841 academic-metric over-optimization). - A count that 'rises without proving causal value creation' is the definition of a vanity metric; backlink count can climb while synthesis value does not. 'When a measure becomes a target it ceases to be a good measure.'
    2. Connectivity != quality (GraphRAG, arXiv 2507.03226). - 'A few well-chosen triples beat many loosely related sentences' - link COUNT is explicitly the wrong target; quality of connection is what matters.
    3. Construct validity. - Using a structural proxy (backlinks) for a substantive construct (synthesis quality) with no validation is a construct-validity failure.

  Strength of challenge: Strong

  Summary: This is a strong, direct challenge. Backlink/orphan count is a structural connectivity measure; the presumption treats it as THE proxy for graph health, where 'health' implicitly includes synthesis quality - a quantity the audit never measured. That is a textbook vanity-metric / Goodhart substitution: the count can rise (e.g., via an index node, 344/381) while synthesis value is flat or worse. The GraphRAG literature explicitly says link quality, not count, drives synthesis. Optimizing the count risks optimizing the wrong target.

  Specific risks: The whole audit's notion of 'graph health' could be tracking a vanity metric; effort optimizes backlink count while the synthesis quality the project exists to produce is never measured and possibly declines.

  Mitigations available: Pair connectivity with a synthesis-quality measure (e.g., validated cross-tradition syntheses produced per unit graph change); treat backlink count as one input, never the target.

  STEELMAN:
    Strongest counterargument: Connectivity count is a legitimate CHEAP STRUCTURAL indicator and a fine early-warning signal for orphans; it becomes a vanity metric only when treated as the definition of health or as an optimization target.
    What would need to be true for C2A2 to be safe: At least one independent synthesis-quality metric must sit alongside it, and neither may be gamed by the index-node move.
    How to test: Does backlink count correlate with measured synthesis quality across vault states? If not, it is not a health proxy.

  Search scope: vanity metrics; Goodhart; construct validity. Comprehensive.

  Recommendation: CHALLENGED
