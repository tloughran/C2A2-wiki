SEARCH-FOR-ASSUMPTION-332:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-332
  Original statement: "The ? feature is independent of Summa node counts, so the unexplained ~256-vs-379 gap doesn't block the push."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-332
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the ship-despite-known-orthogonal-defect decision
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Separation of concerns / modularity (Parnas 1972) — if two features are genuinely decoupled, a defect in one need not block release of the other; shipping with a known, isolated, orthogonal defect is normal release practice.
    2. Release management with known-issues lists — mature practice explicitly permits shipping with documented, scoped defects that don't touch the feature under release, provided the independence is established.

  Strength of support: Moderate (conditional on independence being verified)

  Summary: IF the ? (summary pop-up) feature and the Summa node-count discrepancy are truly independent, then standard separation-of-concerns and release practice support not letting the orthogonal defect block the push. The conditional is well-supported. The strength hinges entirely on whether the independence is established rather than assumed.

  Caveats: Both features render into the SAME generated artifact (wiki_narration.html), which is a coupling surface; "independent" is asserted, not demonstrated, and an unexplained count gap is precisely the kind of latent-coupling signal that separation-of-concerns warns you to verify before relying on it. Support is conditional: sound IF independence is confirmed and the gap explained (this verification is the AGAINST angle).

  Search scope: separation of concerns/modularity; shipping with known orthogonal defects; coupling via shared artifacts. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
