SEARCH-AGAINST-PRESUMPTION-156:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-156
  Original statement: "Ephemeral-by-default + Pin-this presumes users will notice valuable plots in real time and remember to pin"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-156
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-123 default-direction without inverse audit
      15b: Searched for counter-evidence on real-time-recognition assumption for derivative-realization
    Current status: NO-CHALLENGE-FOUND

  Sources:
    1. Re-finding literature (Bruce et al. 2004; Capra & Pérez-Quiñones 2005) — real-time recognition routinely fails.
    2. For purely exploratory use, ephemeral-default may be appropriate — partial defense for narrow use case.
    3. Auto-persist-with-cleanup is the canonical compromise.

  Strength of challenge: Weak

  Summary: The presumption is well-founded. The narrow defense (pure-exploratory ephemeral) does not cover the derivative-recognition case, which is the load-bearing concern.

  Specific risks: None substantial.

  Mitigations available: Auto-persist with auto-cleanup; configurable per user mode.

  Recommendation: NO-CHALLENGE-FOUND — presumption inference is sound

  STEELMAN:
    Item: PRESUMPTION-156
    Strongest counterargument: For purely exploratory whiteboard sessions, ephemeral-default is appropriate; user habit teaches them to pin valuable plots.
    What would need to be true for C2A2 to be safe: Use mode characterized; if derivative-recognition is significant, default-direction reconsidered.
    How to test: Track pin-rate vs. retrospective-want rate.
