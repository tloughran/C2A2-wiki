SEARCH-AGAINST-PRESUMPTION-429:
  Date searched: 2026-07-01
  Original item: PRESUMPTION-429
  Original statement: "[inferred] That deferring the token/metabolism view is cost-free because the connectome 'already confirms' — presumes the two views are redundant, not complementary."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-429
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the metabolism-view deferral
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. N-version / independent-verification literature (NASA common-mode-failure material, IEEE N-version studies) — the value of a second check is its INDEPENDENCE; two checks over different substrates catch faults a single check shares. Collapsing them assumes correlated coverage that must be demonstrated, not presumed.
    2. Common-mode-failure analysis — treating independent signals as redundant discards exactly the cross-check that detects a fault in the first signal's own substrate.
    3. C2A2-internal: the connectome reads git+vault; the metabolism/token view reads the OpenStory DB (the very DB that was CORRUPT this session). The metabolism view is the independent signal on the DB's health — precisely not redundant with a git/vault-based connectome.

  Strength of challenge: Moderate

  Summary: The two views read different substrates (git+vault vs the OpenStory DB), so they are complementary independent signals, not redundant. Deferring the metabolism view is therefore not cost-free: it removes the only view that would have surfaced the DB-side health that the connectome cannot see (and the DB was in fact corrupt). "Already confirms" assumes correlated coverage that the substrate difference denies.

  Specific risks: DB-side ingestion/metabolism faults go unobserved because the only independent view of them was deferred; a corrupt-DB condition is missed until it surfaces elsewhere.

  Mitigations available: Restore the metabolism view (post DB-recovery, A-400) as an independent cross-check; do not treat one substrate's confirmation as coverage of another (echoes PREMISE-089 per-source freshness independence).

  STEELMAN:
    Item: PRESUMPTION-429
    Strongest counterargument: If the token/metabolism view is DERIVED from the same git/vault events as the connectome (just a different rendering), then it IS redundant and deferral is cheap — the substrate-difference claim collapses and the presumption is right.
    What would need to be true for C2A2 to be safe: Confirm the metabolism view's data source; if it reads the OpenStory DB independently, it is complementary and must not be deferred as "cost-free."
    How to test: Trace the metabolism view's inputs; if any input is the DB (not git/vault), the redundancy claim fails.

  SYSTEMIC-RISK: relates to the verification-completeness cluster (single-check over-trust) and to PREMISE-089 (per-source independence).

  Recommendation: CHALLENGED (Moderate — different substrates make the views complementary; deferral loses an independent DB-health signal)
