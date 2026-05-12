SEARCH-AGAINST-ASSUMPTION-082:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-082
  Original statement: "3-layer RC Explorer architecture (L1/L2/L3) with 5 explicit integration steps; Community Explorer = Tool #1, AI Heartbeat = Tool #2 (urgent)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-082
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 RC-Explorer architecture proposal
      15b: Searched for challenging literature on layer-coherence failures and cross-layer leakage
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Software-architecture literature on layered-architecture critiques (Garlan, Allen & Ockerbloom 1995 "Architectural Mismatch") — layered architectures consistently leak; the assumption that layers are coherent is documented as a frequent source of integration failure.
    2. Conway's Law (Conway 1968; MacCormack et al. 2012) — system layering mirrors team structure; one-person systems frequently produce layer abstractions that dissolve under multi-person use.
    3. Knowledge-management literature (Lave & Wenger 1991 "Situated Learning") — knowledge-system layers are particularly leak-prone because human cognition does not respect layer boundaries.
    4. Tool-prioritization critique (Reinertsen 2009) — labeling Tool #1 / Tool #2 / urgent without explicit cost-of-delay analysis is a documented heuristic anti-pattern; ranking should be derived, not asserted.
    5. C2A2-internal: PRESUMPTION-099 (3-layer presumed coherent and non-overlapping) — the unstated coherence claim is itself flagged.

  Strength of challenge: Moderate

  Summary: Layered architectures are well-supported in general but consistently leak in practice. The 3-layer RC Explorer skeleton inherits this leakage risk. The Tool #1 / Tool #2 / urgent ranking is asserted without cost-of-delay derivation, which the literature consistently warns against. The architectural skeleton is canonical; the specific layer-isolation and tool-ranking claims are weaker.

  Specific risks: (a) Cross-layer leakage producing duplication and inconsistency; (b) Tool #1 / Tool #2 ordering may not survive contact with implementation realities; (c) PRESUMPTION-099 is the operational form of this concern and is queued for separate disposition.

  Mitigations available: (a) Add explicit layer-isolation tests; (b) derive tool-prioritization from cost-of-delay rather than asserting it; (c) treat the architectural skeleton as a hypothesis, not a fixed plan; (d) revisit ordering after Tool #1 implementation reveals real costs.

  Recommendation: PARTIALLY-CHALLENGED (skeleton is canonical; coherence and ranking inherit weaker support and warrant explicit treatment)

  STEELMAN:
    Item: ASSUMPTION-082
    Strongest counterargument: Layered architectures are easy to draw and hard to enforce. Every deployed multi-layer knowledge system in the literature shows layer leakage; the question is not whether RC Explorer's layers will leak but where. Asserting Tool #1 / Tool #2 / urgent without cost-of-delay derivation locks in a prioritization that may be inverted by what implementation reveals. Architecture diagrams are hypotheses; treating them as plans before implementation feedback is a documented anti-pattern.
    What would need to be true for C2A2 to be safe: (a) Layer boundaries explicitly tested with cross-layer-item examples; (b) tool prioritization derived from cost-of-delay rather than asserted; (c) the 5 integration steps treated as testable rather than fixed.
    How to test: List 5 candidate items that could plausibly belong to multiple layers; ask the architecture which layer each belongs to; if the answers feel forced, the layer abstraction is leaking and needs revision.
