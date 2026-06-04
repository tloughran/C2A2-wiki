SEARCH-AGAINST-ASSUMPTION-256:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-256
  Original statement: Sociogram interaction model locked (Tom: 'leave the current model'): search/focus: is a transient highlight-in-place lens; checkboxes are hard filters; the two do not sync.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-256
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched mode-error / dual-control confusion literature.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Norman (1983), 'Design rules based on analyses of human error' — when two controls affect the same observable (here, visibility) without a shared model, mode errors and confusion rise.
    2. Kahneman & Tversky (1984) framing / binary-choice literature — locking by preference between two clean options without a usability test subordinates a possible third 'reframe/unify' design (couples PRESUMPTION-284).
    3. Nielsen heuristics (visibility of system status, consistency) — non-syncing controls that both change what is visible can violate the user's expectation that visibility has one cause.

  Strength of challenge: Moderate

  Summary: Even though the separation is a valid pattern, two controls that both alter visibility without agreement is a recognized source of mode confusion. The model was locked by preference, not by a usability test, so the residual risk is empirical, not conceptual.

  Specific risks: Users may expect focus and checkbox filters to agree; silent divergence could read as a bug; subordinated third 'unify' option never evaluated.

  Mitigations available: Add a clear visual distinction (lens vs filter), a 'clear lens' affordance, and a lightweight usability check.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-256
    Strongest counterargument: The pattern is valid, but validity of a pattern is not validity of *this* instantiation; only a usability test can show the non-syncing dual controls don't confuse real users.
    What would need to be true for C2A2 to be safe: A small usability check shows users correctly model focus-as-lens and checkbox-as-filter without mistaking divergence for a fault.
    How to test: 5-user think-aloud test on the locked model.
