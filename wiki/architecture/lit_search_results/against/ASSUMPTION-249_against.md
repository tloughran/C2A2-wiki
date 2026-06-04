SEARCH-AGAINST-ASSUMPTION-249:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-249
  Original statement: ISME is now ~5.5 weeks out; demo-path-shaped work is the prioritization tiebreaker.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-249
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on demo-path heuristic biases and ISME-deadline negotiability.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Partial

  Sources:
    1. Brooks (1975) — Documents that demo-driven prioritization systematically de-prioritizes load-bearing infrastructure; the dimensional bias is documented.
    2. DeMarco & Lister (1987) "Peopleware" — Demo-orientation produces visible-progress bias; non-visible work (infrastructure, testing, refactoring) is under-resourced.
    3. Goldratt (1984) — While ToC supports deadline-orientation, it explicitly warns against optimizing-for-the-visible at the expense of the actual bottleneck.
    4. Heath & Heath (2013) "Decisive" — Documented bias: "what's available to demo" anchors decisions even when other work is higher-value.
    5. C2A2-internal: REVISE-056, REVISE-057, REVISE-058 (PRS-extraction backlog, ingest-state gap, route-rate-fact) are all non-demo load-bearing items that the demo-path tiebreaker can systematically defer.

  Strength of challenge: Weak-Moderate

  Summary: Demo-path tiebreaking IS supported (15a) for true tiebreakers, but the LITERATURE on demo-driven bias is robust. Brooks, DeMarco & Lister, Goldratt, and decision-science all document that "demo-path-shaped" framing systematically obscures non-visible load-bearing work. The current C2A2 backlog (FLAG-I cluster: PRS-extraction, ingest, route-rate) is precisely the non-demo work that demo-tiebreaking can defer. The challenge is not to deadline-orientation but to demo-path AS the tiebreaker.

  Specific risks: (a) Non-demo FLAG-I cluster work (REVISE-056..058) systematically deferred; (b) post-ISME the deferred load-bearing work emerges as compounded debt; (c) demo-path tiebreaker becomes the cover for the binary-framing pattern (PRESUMPTION-267); (d) ISME deliverables ship but on top of un-remediated foundations.

  Mitigations available: (a) Use demo-path AS one tiebreaker among several (load-bearing weight, FLAG-I exposure, etc.); (b) reserve N% of pre-ISME capacity for non-demo load-bearing work; (c) explicit accounting for what demo-tiebreaking is deferring.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-249
    Strongest counterargument: Demo-driven prioritization literature (Brooks, DeMarco & Lister, Goldratt) consistently documents that "what's demo-able" anchors decisions even when non-demo work is the actual bottleneck. C2A2's own active FLAG-I cluster (REVISE-056/057/058) is the direct internal example of non-demo work that demo-tiebreaking can defer. The 5.5-week window may ship a presentation atop unremediated foundations.
    What would need to be true for C2A2 to be safe: Demo-path is one of multiple tiebreakers; non-demo load-bearing work gets reserved capacity; explicit "what's being deferred" log per prioritization decision.
    How to test: Track FLAG-I cluster items deferred to post-ISME; audit at ISME-end for compounded-debt emergence.
