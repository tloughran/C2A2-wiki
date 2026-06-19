SEARCH-FOR-ASSUMPTION-328:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-328
  Original statement: "Single-source-of-truth bios — read the pop-up summary from the same wiki.md the agents maintain, so 'no second copy to drift'."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-328
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the data-architecture decision — derive the user-facing bio from the canonical wiki.md rather than a duplicated copy
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hunt & Thomas, 1999, "The Pragmatic Programmer" — the DRY principle ("every piece of knowledge must have a single, unambiguous, authoritative representation within a system"). Directly supports deriving the bio from one canonical source rather than copying.
    2. Single-Source-of-Truth (SSOT) data-architecture practice — duplicated state is the standard cause of divergence/drift; canonical-source-plus-derived-views is the recommended pattern (data-warehousing, master-data management, configuration management).
    3. Database normalization (Codd) — eliminating redundant copies removes update anomalies; the same logic applies to documentation: one authored copy, many rendered views, no sync step to forget.

  Strength of support: Strong

  Summary: Reading the pop-up from the canonical wiki.md is a textbook application of DRY / single-source-of-truth: duplicated content is the recognized root cause of drift, and the standard remedy is one authoritative representation with derived (read-only) views. The decision removes an entire class of sync bugs because there is no second copy to update. Support is strong and conventional for the ARCHITECTURE choice (one source, derived view).

  Caveats: SSOT does not eliminate coupling — it relocates it. The view now depends on the wiki.md's structure/parse-contract (heading names, the `**Summary**` block format), so a refactor of the agents' working doc can silently break the derived view. Support is for "one source, no copy," not for "the source is automatically fit to serve as a user-facing bio" (that adequacy question is PRESUMPTION-361/363). SSOT's payoff is also conditioned on the source actually being maintained (PRESUMPTION-365).

  Search scope: DRY / SSOT / master-data-management; duplicated-state drift; canonical-source-with-derived-views. Comprehensive.

  Recommendation: SUPPORTED
