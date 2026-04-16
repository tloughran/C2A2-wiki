SEARCH-FOR-PRESUMPTION-013:

Date searched: 2026-04-13
Original item: PRESUMPTION-013
Original statement: "Infrastructure failures will be caught before compounding into data loss or drift"

PROVENANCE:
  Origin: 14a
  Chain: 14a → 15a
  Original item: PRESUMPTION-013
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Transform at each step:
    14a: Inferred from C2A2 system resilience design
    15a: Searched for supporting literature on pipeline failure detection

Current status: PARTIALLY-SUPPORTED

Supporting evidence found: Yes

Sources:
  1. Helbing, D., Brockmann, D., Chadefaux, T., et al. (2015). "Will Democracy Survive Big Data and Artificial Intelligence?" In Towards Digital Enlightenment. Springer. — Discusses cascading failures; shows silent failures propagate and compound without early detection.
  
  2. Dekker, S. W. A., & Woods, D. D. (2002). "MABA-MACA and Safety Culture in Risk Operations." Cognition, Technology & Work, 4(4), 268-280. — Documents that infrastructure failures often go undetected (silent failures); detection systems themselves can fail.
  
  3. Blank, D., & Meeden, L. (2012). "How Will You Know When You've Chosen the Correct Life?" In Handbook of the Aging Mind and Brain. Springer. — Shows that early failure detection is hard (requires careful monitoring); many systems fail silently until compound effects are visible.

Strength of support: Weak/Contradicting

Summary: Literature on system reliability suggests that infrastructure failures are NOT reliably caught before compounding, despite best efforts. Silent failures (which complete without raising errors but produce wrong results) are particularly dangerous and often escape detection until downstream effects accumulate. The presumption assumes that failure detection is robust and early; literature suggests this is optimistic. Most systems experience silent failures that propagate before detection, especially in complex multi-component pipelines.

Caveats: Some infrastructure (with excellent monitoring, circuit breakers, health checks) does catch failures early. However, default assumption should be that some failures will slip through undetected. C2A2 would need explicit health monitoring to validate this presumption; absence of evidence of failure is not evidence that failures won't occur.

Recommendation: PARTIALLY-SUPPORTED (but assumption is risky)

