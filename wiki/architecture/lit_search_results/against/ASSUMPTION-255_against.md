SEARCH-AGAINST-ASSUMPTION-255:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-255
  Original statement: v1.6 (bare-guess parser, logic-validated 16/16) is held -- not pushed, not regenerated -- because its isolate/link share the opacity mechanism of the confirmed fade bug; shipping now would ship a non-working fade.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-255
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched all-or-nothing-increment cost vs feature-flag/partial release.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Flagsmith / DevCycle / ConfigCat (decoupling deployment from release) — the established practice is to deploy the validated parser with the fade behind a flag or disabled, rather than hold the whole increment.
    2. Hodgson/Fowler, 'Feature Toggles' — kill-switch / partial-release patterns exist precisely so a coupled defect does not block unrelated validated work.
    3. Continuous-delivery literature — large held increments accumulate merge/regen risk; small, flag-gated releases reduce it.

  Strength of challenge: Moderate-Strong

  Summary: A large body of release-engineering practice holds that deployment should be decoupled from release: the validated parser could ship with the fade disabled or flagged rather than holding all of v1.6. The all-or-nothing hold is the very pattern feature-flagging was designed to avoid (couples PRESUMPTION-279).

  Specific risks: Held increment grows stale; validated work is withheld from users for a defect that could be flagged off; regen cost compounds.

  Mitigations available: Ship the validated parser with the fade behind a flag or set to a no-op; release the fade fix when confirmed.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-255
    Strongest counterargument: 'Ship nothing with a broken fade' is only forced if the fade cannot be cleanly disabled; feature-flag practice shows it almost always can, so the hold reflects an unconsidered alternative, not a necessity.
    What would need to be true for C2A2 to be safe: The fade can be disabled/flagged without destabilizing the validated parser path.
    How to test: Spike: gate the fade behind a flag, regen, confirm the parser path works with fade off.
