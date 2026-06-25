SEARCH-FOR-ASSUMPTION-337:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-337
  Original statement: "The proposal-review queue is review-bound, not search-bound — the binding constraint since 06-16 is human review throughput, not literature discovery"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-337
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-22 session as an actionable workflow-design claim
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Goldratt, Theory of Constraints (ASQ; leanproduction.com). — Every system has a binding constraint; identify it by where WIP piles up. A five-deep review queue with nothing decided since 06-16 is the signature of a review-stage bottleneck.
    2. Little's Law (ASQ; 6sigma.us). — WIP = throughput x cycle time; a growing queue with flat throughput localizes the constraint at the review stage.
    3. Kanban queuing-theory guidance (kanbantool). — WIP accumulation marks the constraint; supports "review-bound" diagnosis.

  Strength of support: Moderate

  Summary: Theory of Constraints and Little's Law jointly support the diagnosis: the constraint is wherever WIP accumulates, and a review queue five deep with no decisions since 06-16 places the binding constraint at human review, not at literature discovery. The flat decision-throughput against accumulating intake is exactly the empirical signature TOC uses to localize a bottleneck. Support is solid for the diagnosis and for the implied "subordinate other stages" prescription.

  Caveats: TOC also warns that constraint identification must be evidence-based, not assumed; the diagnosis holds as long as intake genuinely outpaces review (which the 06-16->06-22 backlog shows).

  Search scope: theory of constraints; Little's law; kanban/WIP. Comprehensive.

  Recommendation: SUPPORTED
