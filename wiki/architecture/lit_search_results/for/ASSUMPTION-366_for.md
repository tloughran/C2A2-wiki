SEARCH-FOR-ASSUMPTION-366:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-366
  Original statement: "That the residual 'click does nothing / lens link invisible' symptom is a cache-delivery problem (stale app.js in iframe), not logic, because the on-disk headless tests pass"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-366
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: live symptom attributed to stale-asset caching (iframe app.js) rather than logic
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Browser/iframe HTTP caching (RFC 7234; cache-busting/versioned-asset practice). - Stale cached scripts are a well-documented cause of "fixed in source, broken in the live page" symptoms; iframes commonly serve cached sub-resources.
    2. Karlton's adage ("two hard things in CS: cache invalidation and naming things") and the cache-busting literature. - Cache-invalidation failures are a recognized, high-frequency class of "works locally / stale live" defects, consistent with the observed symptom.

  Strength of support: Moderate

  Summary: The cache-delivery hypothesis is a priori plausible and matches a very common failure mode: a corrected on-disk asset that the running iframe still serves from cache, producing dead clicks / missing UI while the source is correct. Cache-busting (versioned URLs) is the standard, cheap test. Support is for the PLAUSIBILITY of the cache hypothesis, not for the INFERENCE used to reach it ("headless tests pass, therefore logic is fine"), which 15b challenges.

  Caveats: Plausibility != confirmation. The diagnosis is empirically falsifiable in one step (force a versioned reload). The supporting evidence does not license excluding a logic bug until that test is run.

  Search scope: HTTP/iframe caching; cache invalidation. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
