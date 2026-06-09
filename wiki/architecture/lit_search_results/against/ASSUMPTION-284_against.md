SEARCH-AGAINST-ASSUMPTION-284:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-284
  Original statement: The right safety split is "approved data auto-publishes, generator/template code changes are gated for human visual review."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-284
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated safety policy.
      15b: Searched for evidence that the data/code split mis-locates the risk.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Sculley et al. 2015, "Hidden Technical Debt in ML Systems" (data dependencies, "CACE: Changing Anything Changes Everything," undeclared consumers). — Data changes are a leading cause of silent, hard-to-localize failure; treating data as the safe-to-auto-publish class inverts a well-documented risk ordering. Direct challenge.
    2. "Data downtime" / data-quality literature (bad data is detected late and is costly; data observability movement). — Code failures tend to be loud (exceptions, broken builds); data-quality regressions are quiet and propagate into every downstream view before anyone notices, which argues data needs MORE not less gating in some regimes.
    3. Garbage-in/garbage-out and provenance practice (couples ASSUMPTION-280/PREMISE-052). — For a system whose OUTPUT is evidence-about-traditions, a wrong-but-well-formed datum is more corrosive than a rendering bug, because it is published as fact.

  Strength of challenge: Moderate

  Summary: The split is half right and half inverted. Code = higher blast radius is fair, but "data is the safe class" ignores that data-quality regressions are the quietest, latest-detected, most-propagating failures and that a wrong datum is published as truth. The defensible claim is "code needs human visual review"; the indefensible add-on is "data needs none," which depends on PRESUMPTION-319 (data is deterministic/safe enough) — itself challenged.

  Specific risks: A schema-valid but wrong datum (mis-attributed edge, duplicated node, a bad CC-xxx id — see the manufactured-identity cluster, REVISE-091) auto-publishes into the connectome as fact, unreviewed, and propagates to every derived artifact. The very failure the gate was meant to prevent occurs on the unguarded side.

  Mitigations available: Replace "human review" on the data path with AUTOMATED data-quality gates (schema + invariants + diff-magnitude thresholds + anomaly alerts), not with nothing; cap auto-publish to bounded diffs and route large/anomalous data diffs to human review; treat the data gate as lighter-but-present, not absent.

  STEELMAN:
    Item: ASSUMPTION-284
    Strongest counterargument: The split conflates "lower blast radius" with "no risk." Code changes are gated because they can break everything at once — true — but the inference "therefore data is safe to auto-publish unreviewed" smuggles in that data cannot break everything, when in fact a single bad systemic datum (a manufactured id, a duplicated entity) silently corrupts every view that joins on it and is published as evidence. The loud/quiet asymmetry means the auto-published side is the one most likely to fail undetected.
    What would need to be true for C2A2 to be safe: The data path is not unreviewed but auto-CHECKED by sufficient automated invariants/anomaly gates, with bounded diff sizes and escalation of anomalies to a human.
    How to test: Inject a plausible-but-wrong datum upstream and measure whether the auto-publish path catches it; if it sails through to the published connectome, the split is unsafe as stated.

  Recommendation: PARTIALLY-CHALLENGED
