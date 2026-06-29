SEARCH-FOR-ASSUMPTION-382:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-382
  Original statement: "A JS-set ?v=Date.now() cache-bust on a lazy iframe satisfies the asset-freshness requirement"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-382
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: ?v=Date.now() query-string cache-bust used to guarantee a fresh iframe asset
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. HTTP caching / cache-busting practice (MDN, web-performance guides). - Appending a unique query string makes the browser treat the URL as a new resource and bypass its HTTP cache; a per-load Date.now() guarantees uniqueness, so it does force a refetch.
    2. Front-end asset-versioning literature. - Query-string versioning is a long-standing, widely deployed technique for defeating stale cached assets on load.

  Strength of support: Moderate

  Summary: As a mechanism for forcing the browser to refetch on load, ?v=Date.now() works: a unique query string reliably bypasses the browser HTTP cache for that request. For the narrow goal of "always load a fresh copy when the iframe is (re)created," the technique is sound and commonly used. Support is moderate and bounded by known pitfalls about intermediary caches and the timing of when the busted URL is actually applied (see caveats and 15b).

  Caveats: Per-load timestamp busting defeats caching entirely (always refetch); some intermediary/CDN configs ignore query strings; for a LAZY iframe the bust applies when src is set, not on later staleness; content-hash fingerprinting is the more correct freshness mechanism. Kin to the ASSUMPTION-366 cache-delivery family.

  Search scope: HTTP cache invalidation; query-string busting; asset versioning. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
