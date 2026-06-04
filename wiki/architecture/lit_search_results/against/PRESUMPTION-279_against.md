SEARCH-AGAINST-PRESUMPTION-279:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-279
  Original statement: [inferred] Holding all of v1.6 presumes 'ship nothing with a broken fade' dominates shipping the validated parser with the fade disabled/flagged; partial release was not considered.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-279
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched feature-flag / decoupled partial-release practice.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Flagsmith / DevCycle / ConfigCat — decoupling deployment from release via flags is the standard way to ship validated work while a coupled defect stays off.
    2. Hodgson/Fowler 'Feature Toggles' — kill-switch/partial-release patterns exist precisely to avoid blocking validated increments on one defect.
    3. Continuous-delivery literature — held increments accumulate integration/regen risk; partial release reduces it.

  Strength of challenge: Moderate

  Summary: A whole body of release practice says deploy the validated parser with the fade flagged/disabled rather than hold everything; the presumption that holding dominates was never weighed against this. The unconsidered partial-release option is standard and cheap.

  Specific risks: Validated work withheld unnecessarily; held increment goes stale; regen cost compounds.

  Mitigations available: Gate the fade behind a flag and ship the parser; release the fade fix when confirmed.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-279
    Strongest counterargument: Holding 'dominates' only if no clean flag boundary exists; feature-flag practice shows one almost always does, so the dominance was assumed, not shown.
    What would need to be true for C2A2 to be safe: A clean flag boundary isolates the fade from the validated parser path.
    How to test: Spike a flagged build; confirm parser path works with fade off.
