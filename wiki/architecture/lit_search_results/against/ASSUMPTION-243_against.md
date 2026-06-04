SEARCH-AGAINST-ASSUMPTION-243:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-243
  Original statement: The Sociogram-tab AI search wired in today via shared `wiki/lib/c2a2-search.js` delegation is the per-tab adapter pattern broker-v4 (DECISION-049 candidate) was designed to enable; today's working integration is the first demonstrated instance.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-243
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on adapter-pattern overhead and "first demonstrated instance" claims.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Partial

  Sources:
    1. Hunt & Thomas (1999) "The Pragmatic Programmer" — Premature-abstraction is documented as a category of waste; thin adapters can fall into this if per-surface divergence is small.
    2. Brown (2015) "Tradeoffs in Software Architecture" — Adapter-pattern overhead is documented to outweigh benefit when N=1; the "first instance" framing IS the period of highest overhead-to-benefit ratio.
    3. Bass et al. (2021) — Documents that "shared module" claims at N=1 carry no architectural-proof weight; the design only proves itself at N=2+ when actual divergence is observable.
    4. Conway (1968) — Adapter patterns that don't reflect real organizational/system divergence tend to ossify into accidental complexity.
    5. C2A2-internal: 2 other tabs (Wiki, ParaThink) have not yet adopted; the design's value is conditional on subsequent adoption.

  Strength of challenge: Weak-Moderate

  Summary: The adapter pattern is sound, but the "first demonstrated instance" framing is precisely the period when the literature warns the architecture cannot yet justify its overhead. Brown and Bass both note that a shared-module pattern's value is proved only across multiple consumers; at N=1, the alternative (direct implementation) is documented as equally viable and cheaper. The challenge is not to the pattern's eventual value, but to the present claim.

  Specific risks: (a) N=1 abstraction may ossify before real divergence is observed; (b) other tabs may not adopt, leaving the shared module as overhead without payoff; (c) "first demonstrated instance" framing implicitly claims architectural validation that the literature does not grant at N=1.

  Mitigations available: (a) Track adoption count and migration cost across remaining tabs; (b) define a sunset criterion (e.g., if N=2 not reached within 60 days, reconsider); (c) measure per-surface divergence; if low, collapse to single implementation.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-243
    Strongest counterargument: At N=1, no shared-module architecture has proven its value. The literature on premature-abstraction (Hunt & Thomas; Brown; Bass) is robust: thin adapters without N=2+ adoption are documented overhead. Today's "first demonstrated instance" is a category-error if intended as architectural validation — at most it demonstrates the integration works, not that the broker pattern outperforms direct implementation. The claim risks anchoring future tab integrations to a pattern that has not yet earned its overhead.
    What would need to be true for C2A2 to be safe: At least 2 tabs adopt the broker pattern within the next 30-60 days, with measured per-surface divergence ≥ threshold to justify the abstraction.
    How to test: Track adoption count; measure migration cost for next tab; compare against estimate-of-direct-implementation cost.
