SEARCH-AGAINST-ASSUMPTION-224:

  Date searched: 2026-05-25
  Original item: ASSUMPTION-224
  Original statement: "The connectivity/orphan metric should exclude `architecture/lit_search_results/` (machine-generated, unrouted) so the orphan count tracks real routing progress."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-224
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction of stated assumption
      15b: Searched for challenging literature (cycle 0)
    Current status: SEARCHED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart, C. (1975); Strathern, M. (1997). "When a measure becomes a target, it ceases to be a good measure." — Adjusting the scope of a metric in the direction that improves the metric is a textbook Goodhart manoeuvre.
    2. Campbell, D. T. (1979). "Assessing the impact of planned social change" (Campbell's Law). — The more a quantitative indicator is used for decision-making, the more it is subject to corruption pressures.
    3. Manheim, D. & Garrabrant, S. (2018). "Categorizing Variants of Goodhart's Law." arXiv:1803.04585. — Formalizes regressive/extremal/causal/adversarial Goodhart; metric re-scoping to track a target is a causal/adversarial-adjacent variant. (Surrogation: Choi, Hecht & Tayler, 2012.)

  Strength of challenge: Moderate-Strong

  Summary: The challenge is that changing what the orphan metric counts, in the direction that reduces the orphan count, is structurally a Goodhart/surrogation move: the metric is being adjusted to better "track routing progress" — i.e., to read better — rather than the underlying integration being improved. Even if the exclusion is defensible on hygiene grounds, doing it because the excluded folder is dragging the number down is exactly the corruption pattern Goodhart and Campbell describe, and it presumes (PRESUMPTION-246) that backlink density measures integration at all.

  Specific risks: The connectivity metric becomes self-serving (it improves by redefinition, not by integration), eroding its value as an honest health signal and masking real integration debt.

  Mitigations available: Pre-register the exclusion rule and its rationale independently of the current metric value; report both the included and excluded counts; periodically validate backlink density against an independent integration check so the proxy itself stays honest.

  STEELMAN:
    Item: ASSUMPTION-224
    Strongest counterargument: Any metric whose denominator is edited by the same party it evaluates, in the direction that flatters that party, is no longer a measurement but a presentation choice; the hygiene justification is true but insufficient, because the *reason* for acting now is that the number looks bad, which is the precise trigger condition of Goodhart's Law.
    What would need to be true for C2A2 to be safe: The exclusion rule is fixed in advance on construct grounds (non-linkable machine output), is applied symmetrically, and both counts are reported so the redefinition is transparent.
    How to test: Check whether the exclusion was specified before or after observing its effect on the count; transparent pre-specification distinguishes hygiene from Goodhart.

  Recommendation: PARTIALLY-CHALLENGED
