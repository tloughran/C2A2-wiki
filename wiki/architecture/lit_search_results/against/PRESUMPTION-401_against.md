SEARCH-AGAINST-PRESUMPTION-401:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-401
  Original statement: "That header uniformity (one brand gold across all tools) is an improvement - presumes consistency > per-tool wayfinding cues"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-401
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: visual uniformity presumed strictly better than per-tool differentiation
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Wayfinding / "you-are-here" orientation literature (information architecture). - Distinct visual cues per location help users know WHERE they are; uniform chrome can remove an orientation signal in a multi-view system.
    2. Nielsen "recognition rather than recall" + minimal-difference critiques. - Over-uniform UIs can make distinct sections indistinguishable, raising recall load (which tool am I in?).

  Strength of challenge: Weak

  Summary: Consistency is genuinely good (15a), but the presumption's STRICT ranking - consistency strictly beats per-tool wayfinding - is not supported. Wayfinding research shows differentiated cues aid orientation; a single brand-gold header across all tools can erase the "which tool am I in?" signal, trading a small recognition aid for uniformity. This is a real but minor tension on a reversible aesthetic choice; the right answer is usually "consistent shell + a small per-tool wayfinding cue," not a strict either/or.

  Specific risks: Mild user disorientation in a multi-tool suite; momentary "which view is this?" friction.

  Mitigations available: Keep the consistent header but retain one differentiator (per-tool title/icon/accent); user-test orientation if the suite grows.

  STEELMAN:
    Item: PRESUMPTION-401
    Strongest counterargument: Consistency and wayfinding are not a strict ordering; maximizing uniformity can suppress orientation cues, so "uniformity is an improvement" is true only up to the point where it erases useful differentiation.
    What would need to be true for C2A2 to be safe: A per-tool wayfinding cue survives inside the unified header.
    How to test: Ask users mid-task to name the current tool with chrome only; high error => differentiation needed.

  Search scope: Wayfinding; consistency heuristics. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
