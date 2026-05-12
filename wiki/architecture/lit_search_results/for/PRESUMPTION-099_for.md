SEARCH-FOR-PRESUMPTION-099:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-099
  Original statement: "3-layer RC Explorer presumed coherent and largely non-overlapping"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated coherence claim embedded in ASSUMPTION-082 — layer non-overlap presumed without test
      15a: Searched for supporting literature on layer-decomposition robustness in multi-tier knowledge systems
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Software architecture (Bass, Clements & Kazman 2012) — layered decompositions are common but layer abstractions are routinely noted to leak; coherence is not a default.
    2. Buschmann et al. (1996) "Pattern-Oriented Software Architecture" — explicit layer-isolation patterns are recommended specifically because non-overlap is not a default.
    3. Conway's Law (Conway 1968; MacCormack et al. 2012) — system structure mirrors team/communication structure; non-overlap depends on organizational discipline.
    4. C2A2-internal: ASSUMPTION-082 partial-support — supports the layered skeleton; non-overlap is the additional unsupported extension.

  Strength of support: Weak

  Summary: Literature supports layered decompositions in general but does not support coherence and non-overlap as defaults. Layer abstractions are well-known to leak; explicit isolation patterns are the canonical response. PRESUMPTION-099 is operating without those isolation patterns. The partial support inherits from ASSUMPTION-082 but the non-overlap claim is unsupported as a default.

  Caveats: (a) Coherence and non-overlap are achievable but require explicit testing; (b) presumption-status compounds with the missing-test concern; (c) cross-layer items and feedback loops are routinely found in deployed knowledge systems — non-overlap without test is a fragile default.

  Recommendation: PARTIALLY-SUPPORTED (layered skeleton inherits ASSUMPTION-082 support; non-overlap default is weakly supported and warrants explicit isolation tests)
