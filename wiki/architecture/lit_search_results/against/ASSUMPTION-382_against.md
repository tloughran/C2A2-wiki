SEARCH-AGAINST-ASSUMPTION-382:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-382
  Original statement: "A JS-set ?v=Date.now() cache-bust on a lazy iframe satisfies the asset-freshness requirement"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-382
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: ?v=Date.now() on a lazy iframe claimed to satisfy asset freshness
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cache-busting pitfalls (query-string vs content-hash). - Timestamp query strings defeat caching wholesale (every load refetches) and, more importantly, freshness is keyed to WHEN the URL is built, not to whether the asset CHANGED; content-hash fingerprinting is the correct freshness primitive.
    2. Intermediary/CDN/proxy caching behavior. - Some proxies and older CDN configs ignore or normalize query strings, so a ?v= bust is not guaranteed to reach origin; Service Worker caches can also serve a stale asset regardless of query string.
    3. Lazy-iframe load timing. - For a lazy iframe the busted URL is fixed at src-assignment; if the iframe is not re-created, later changes to the underlying asset are not picked up - the bust addresses first-load, not ongoing staleness.

  Strength of challenge: Moderate

  Summary: For the narrow case "force a refetch when the iframe is created" the technique works, but as a general "satisfies asset-freshness requirement" claim it is over-stated. Timestamp busting is freshness-by-time-of-load, not freshness-by-content-change; it can be subverted by proxies/Service Workers that ignore query strings, and for a lazy iframe it only governs the first load. The correct primitive is content-hash fingerprinting plus proper cache-control headers.

  Specific risks: Stale asset served via Service Worker / query-string-ignoring proxy; lazy iframe never refreshed after first load; unbounded refetching (no caching) as a performance cost.

  Mitigations available: Use content-hash fingerprinting + immutable cache-control for changed assets; verify intermediary caches honor the query string; if ongoing freshness is required, re-create/reload the iframe on a real change signal, not on a static timestamp.

  STEELMAN:
    Item: ASSUMPTION-382
    Strongest counterargument: ?v=Date.now() conflates "fetched recently" with "is the current version"; it busts on clock, not on content, can be ignored by intermediaries/Service Workers, and on a lazy iframe only fires once - so it can report freshness it does not actually guarantee.
    What would need to be true for C2A2 to be safe: Either the asset rarely changes after first load, or freshness is keyed to content (hash) and the iframe reloads on a real change signal, with intermediary caches confirmed to honor the bust.
    How to test: Change the asset behind a loaded lazy iframe and confirm whether the page actually serves the new version; test behind a proxy/Service Worker.

  Search scope: HTTP cache invalidation; query-string vs fingerprinting; SW/proxy caching; iframe load timing. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
