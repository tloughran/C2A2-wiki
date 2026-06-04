SEARCH-FOR-PRESUMPTION-268:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-268
  Original statement: [inferred] Deploying two new weekly watch agents today addresses system-identified meta-problems rather than adding meta-layers to a human-bandwidth-constrained system; the net-value test for new-agent deployment is not separately defined.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-268
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated net-value gap on new-agent deployment.
      15a: Searched for supporting literature on canary-deployment-as-self-observation in agentic systems.
    Current status: PARTIALLY-SUPPORTED (Weak-Moderate)

  Supporting evidence found: Partial

  Sources:
    1. Hong et al. (2024) "MetaGPT" — Meta-agent layers for monitoring agent-system behavior are documented as effective when the monitored layer is well-scoped.
    2. Park et al. (2023) "Generative Agents" — Reflection / observation agents are documented as adding net value when their outputs feed back into the system's decision-making.
    3. Shao et al. (2024) — Self-observation patterns in multi-agent systems are supported when they are bounded and goal-conditional.
    4. Beyer SRE — Observability layers are documented as net-positive when they reduce time-to-detect more than they add operational overhead.
    5. C2A2-internal: prior watch-agent additions (Janitor, etc.) produced net-positive outcomes in observable cases.

  Strength of support: Weak-Moderate

  Summary: Multi-agent / observability literature supports meta-agents-as-net-positive UNDER specific conditions (well-scoped, bounded, feeds back into decision-making, reduces time-to-detect). The presumption here is that today's two new agents meet those conditions; the literature provides no specific support for that — only general support for the pattern when the conditions are met.

  Caveats: (a) The literature explicitly notes the symmetric failure mode (canary-too-many; observation-as-distraction); (b) human-bandwidth-constrained framing is the load-bearing element — literature on this is limited and inconclusive; (c) "net-value test not separately defined" is the gap the presumption names — literature confirms such a test SHOULD exist.

  Recommendation: PARTIALLY-SUPPORTED (Weak-Moderate)
