SEARCH-AGAINST-PRESUMPTION-268:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-268
  Original statement: [inferred] Deploying two new weekly watch agents today addresses system-identified meta-problems rather than adding meta-layers to a human-bandwidth-constrained system; the net-value test for new-agent deployment is not separately defined.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-268
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated net-value gap.
      15b: Searched for challenging literature on canary-too-many anti-pattern and observation-as-distraction.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Bainbridge (1983) "Ironies of Automation" — Each added observation-layer adds its own monitoring requirement; the cumulative human-bandwidth burden grows non-linearly.
    2. Beyer SRE — "Toil" literature explicitly notes that monitoring-layer additions are net-negative when they add operational overhead exceeding time-to-detect reduction.
    3. Hong et al. (2024) "MetaGPT" — Documents that meta-agent layers fail when monitored-vs-monitor count ratio drops below threshold; canary-too-many is the named anti-pattern.
    4. Park et al. (2023) — Reflection-agent literature is conditional on agent-system having capacity to act on the reflections; without that capacity, the reflections are overhead.
    5. C2A2-internal: human-bandwidth constraint is well-documented (FLAG-I cluster); adding watch agents without explicit bandwidth accounting carries documented risk.

  Strength of challenge: Moderate

  Summary: Multi-agent / observability literature is robust on the canary-too-many anti-pattern. Bainbridge / Beyer SRE / Hong / Park all document that observation-layers have a documented break-even point beyond which they are net-negative. The presumption (deployment is net-positive) is not separately tested. The C2A2-specific concern is acute: the human-bandwidth constraint is already documented as the FLAG-I bottleneck; adding observation-layers in front of that bottleneck is exactly the documented anti-pattern shape.

  Specific risks: (a) Watch-agent outputs accumulate without action capacity; (b) human-bandwidth bottleneck worsens, not improves; (c) the watch agents become the next FLAG-I documentation route; (d) "addressing meta-problems" framing masks the bandwidth-trade question.

  Mitigations available: (a) Define net-value test BEFORE deployment (e.g., time-to-detect reduction > N hours per week); (b) sunset criterion (e.g., 4 cycles without actionable output → reconsider); (c) explicit human-bandwidth budget accounting; (d) cap total watch-agent count.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-268
    Strongest counterargument: The canary-too-many anti-pattern is well-documented across observability literature. Adding observation-layers ON TOP of an already-named human-bandwidth bottleneck (FLAG-I) is exactly the documented failure shape. "Net-value test not separately defined" is the precise gap — the literature requires explicit value-vs-overhead accounting before adding observation-layers, especially in capacity-constrained systems.
    What would need to be true for C2A2 to be safe: Net-value test defined ex ante; sunset criterion; human-bandwidth budget tracked; cap on total watch-agent count.
    How to test: Track watch-agent output → action conversion rate; flag if < threshold.
