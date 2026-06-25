SEARCH-AGAINST-PRESUMPTION-372:
  Date searched: 2026-06-23
  Original item: PRESUMPTION-372
  Original statement: "[inferred] That adding two well-chosen proposals is progress, even into a queue the same session calls review-bound and five deep with nothing decided since 06-16 (intake-as-progress)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-372
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated intake-as-progress premise in tension with ASSUMPTION-337
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goldratt TOC + Little's Law (ASQ; 6sigma.us). — Adding work at a non-binding stage upstream of a saturated constraint does not raise throughput; it raises WIP and cycle time. Classic anti-pattern.
    2. Kanban/WIP-limit literature (kanbantool). — WIP limits exist precisely to stop intake-as-progress; unbounded intake at a bottleneck degrades flow.
    3. C2A2-internal: corollary of ASSUMPTION-337 (review-bound, INCORPORATE PREMISE-070). — If the queue is review-bound, more intake is by definition not progress.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged by the same TOC/Little's-Law logic that supports its twin ASSUMPTION-337: when review is the binding constraint, adding proposals increases WIP and aging, not throughput. WIP-limit practice was invented to stop exactly this. Because 337 is INCORPORATEd as review-bound, intake-as-progress is its direct corollary error.

  Specific risks: Felt productivity from intake masks a stalling pipeline; proposals age and decay in value while the real constraint (review) goes unaddressed.

  Mitigations available: Impose a WIP limit on intake; subordinate intake to review throughput; measure progress as decisions made, not proposals added.

  STEELMAN:
    Strongest counterargument: Two exceptionally on-mission proposals (the Levin<->Friston bridge) are not generic WIP; capturing a rare high-value insight when it appears is progress even if review is slow, because the insight might not recur.
    What would need to be true for C2A2 to be safe: The value of capture must exceed the aging/decay cost in a review-bound queue; this holds only for genuinely rare, perishable insights, not as a general intake policy.
    How to test: Compare realized value of captured-but-unreviewed proposals against their decay rate; if decay dominates, intake-as-progress is false.

  Search scope: TOC/Little's law; WIP limits; option-value boundary. Comprehensive.

  Recommendation: CHALLENGED
