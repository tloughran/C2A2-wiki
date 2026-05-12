SEARCH-AGAINST-PRESUMPTION-099:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-099
  Original statement: "3-layer RC Explorer presumed coherent and largely non-overlapping"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated coherence claim embedded in ASSUMPTION-082
      15b: Searched for challenging literature on cross-layer items and feedback-loop necessity
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Garlan, Allen & Ockerbloom (1995) "Architectural Mismatch" — layer abstractions consistently leak; coherence-by-default is documented anti-pattern.
    2. Buschmann et al. (1996) "Pattern-Oriented Software Architecture" — explicit isolation patterns are recommended specifically because non-overlap is not a default.
    3. Conway's Law literature (Conway 1968; MacCormack et al. 2012) — layer non-overlap requires organizational discipline that one-person systems struggle to enforce.
    4. C2A2-internal: ASSUMPTION-082 PARTIALLY-CHALLENGED — same evidence applies; PRESUMPTION-status compounds.
    5. Knowledge-system literature (Lave & Wenger 1991) — knowledge-system layers are particularly leak-prone because cognition does not respect layer boundaries.

  Strength of challenge: Strong

  Summary: Layer coherence and non-overlap are not defaults; they require explicit isolation patterns and organizational discipline. PRESUMPTION-099 operates as unstated coherence claim without isolation tests. Literature is unambiguous: layered architectures leak unless tested. PRESUMPTION-status + missing test is the strongest signal.

  Specific risks: (a) Cross-layer items produce duplication and inconsistency; (b) layer-leakage debugging is high-cost when discovered late; (c) feedback loops between layers may be necessary and absent.

  Mitigations available: (a) Explicit layer-isolation tests; (b) cross-layer-item examples worked through manually; (c) feedback-loop design surfaced explicitly.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-099
    Strongest counterargument: Every multi-tier knowledge system in the literature shows layer leakage; the question is where it leaks, not whether. PRESUMPTION-099 absorbs the coherence claim as default without testing it, which means the leakage will be discovered during use rather than during design — and discovery during use is documented as the high-cost path. Adding a one-page layer-isolation test would catch most leakage early.
    What would need to be true for C2A2 to be safe: (a) Layer-isolation tests with explicit cross-layer-item examples; (b) feedback-loop design articulated; (c) joint treatment with ASSUMPTION-082.
    How to test: List 5 candidate items that could plausibly belong to multiple layers; ask which layer each belongs to; if 2+ feel forced, leakage is present.
