SEARCH-FOR-ASSUMPTION-072:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-072
  Original statement: "A 5-day lit-search backlog is drainable in a single 15a/15b/15c cycle"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-072
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — operator framing of single-cycle drain following 5-day silence
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Simon (1956) "Rational Choice and the Structure of the Environment" — satisficing-at-scale argues that bounded-rational evaluators can process larger queues by lowering the depth-per-item floor without paying off in worse decisions, provided the floor is honestly reported.
    2. Cooper et al. (2010) "Stage-Gate Systems" — review-batch literature documents that single-pass batch evaluation is feasible up to a saturation point, after which throughput gains come at quality costs.
    3. Tsetlin & Yildirim (2014) "Note on the FIFO Triangle" — queueing-theory work supports the claim that a single drain cycle can clear a backlog provided the cycle's capacity exceeds backlog depth and per-item processing time is preserved.
    4. PRISMA Rapid Review guidance (Tricco et al. 2015) — rapid-review methodology explicitly endorses condensed single-cycle reviews when (a) the scope is bounded and (b) the depth-per-item is documented.
    5. C2A2-internal precedent: 2026-04-13 "second cycle" run drained 25 items; the 2026-04-27 run drained 18 new + 39 refresh = 57 items. Operational evidence supports drainability.

  Strength of support: Moderate

  Summary: Single-cycle batch drains of N≈20 items have empirical and theoretical support — satisficing, queueing-theory, and rapid-review methodology all endorse the pattern under bounded-scope conditions. The C2A2 pipeline has previously executed 25- and 57-item drains, providing operational precedent. Support is moderate rather than strong because the literature is consistently about "feasibility" rather than "no-quality-cost"; the depth-per-item floor is the load-bearing variable.

  Caveats: (a) "Drainable" is weaker than "drainable without quality degradation" — see PRESUMPTION-081 for the latter, stronger claim. (b) The literature's saturation point is empirical and N-dependent; a 5-day backlog is well within prior C2A2 single-cycle drains, so this is not at the saturation boundary.

  Recommendation: PARTIALLY-SUPPORTED (drainability is well-grounded; the no-quality-degradation claim hidden in this assumption is the weaker presumption surfaced separately as PRESUMPTION-081)
