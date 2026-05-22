SEARCH-AGAINST-ASSUMPTION-204:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-204
  Original statement: "Coil altitude should encode discovery-time (~2026), not idea-age ("axis follows model")."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-204
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: design decision that a coil's vertical altitude encodes discovery-time, not the age of the underlying ideas.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Bitemporal modeling (Snodgrass). — Encoding only one time discards the other; if users care about idea-age, discovery-time misleads.
    2. Munzner, T. (2014). "Visualization Analysis and Design." — Encoding choices should follow the user task; a single fixed axis is rarely uniquely correct (PRESUMPTION-225).
    3. Presentism risk: discovery-time altitude can make recent rediscoveries look "newer/higher" than older foundational ideas, distorting lineage.

  Strength of challenge: Weak-Moderate

  Summary: The main challenge is underdetermination: no single time axis is uniquely right (Munzner; bitemporal theory), and discovery-time can introduce a presentist distortion of intellectual lineage. The challenge is weak-moderate because discovery-time is a reasonable default, not an error.

  Specific risks: Users may misread altitude as idea-age; lineage relationships get visually inverted.

  Mitigations available: Offer an axis toggle (discovery-time vs idea-age) or dual encoding; label the axis explicitly.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-204
    Strongest counterargument: 'Axis follows model' smuggles in a uniqueness claim the data model does not license; both discovery-time and idea-age are model-consistent, so fixing one without a toggle is an unjustified commitment that can mislead about lineage.
    What would need to be true for C2A2 to be safe: The axis is labeled and ideally toggleable.
    How to test: User comprehension test — do viewers correctly infer discovery vs idea chronology under each encoding?
