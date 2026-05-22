SEARCH-AGAINST-PRESUMPTION-225:
  Date searched: 2026-05-21
  Original item: PRESUMPTION-225
  Original statement: ""Axis follows model" presumes a unique axis semantic where several (publication/narrative/connectome time) may be defensible."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-225
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred: 'axis follows model' presumes the data model fixes a unique axis semantic, where several time semantics (publication/narrative/connectome) are defensible.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bertin (1967) "Semiology of Graphics"; Munzner (2014). — Encodings are underdetermined by data; many valid mappings exist for the same model.
    2. Mackinlay (1986) APT. — Multiple expressive/effective encodings are typically available; the system ranks, it does not uniquely fix.
    3. Bitemporal/temporal-network theory. — Several legitimate time semantics (publication, narrative, discovery/connectome time) coexist; none is uniquely "the" axis.

  Strength of challenge: Moderate

  Summary: Moderate challenge: the visualization literature is clear that a data model underdetermines its encoding (Bertin, Munzner, Mackinlay) and temporal theory recognizes multiple legitimate time axes. 'Axis follows model' overstates — several axes are defensible, so the design should expose a choice rather than assert uniqueness.

  Specific risks: Asserting a unique axis hides a design decision and may mismatch the user's task.

  Mitigations available: Offer an axis toggle / multiple-coordinated-views; document the chosen semantic; treat as DECISION-039/OPEN-057.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-225
    Strongest counterargument: 'Axis follows model' is a uniqueness claim the visualization literature flatly denies — Bertin, Mackinlay, and Munzner all show encodings are underdetermined by the data model — so the axis is a design choice masquerading as a derivation, and at least three time semantics are defensible.
    What would need to be true for C2A2 to be safe: The axis is presented as a labeled, switchable choice.
    How to test: Enumerate defensible axes; if more than one is task-appropriate, uniqueness is false (already the case).
