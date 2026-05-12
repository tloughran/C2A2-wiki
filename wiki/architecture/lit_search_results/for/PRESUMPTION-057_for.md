SEARCH-FOR-PRESUMPTION-057:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-057
  Original statement: "The 49 RC Wiki files are stable enough (no churn-rate audit performed)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-057
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absence of any churn-rate audit in caching-architecture deliverables
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Wiki edit-frequency literature (Halfaker et al. 2013 "The rise and decline of an open collaboration system"; general wiki-activity research 2010-2020): reference-page edit frequency on mature wikis is typically low — provides INDIRECT base-rate support that "reference material tends to be slow-changing."
    2. C2A2 internal evidence: the RC Wiki has been described as reference material (thinker profiles, concept nodes, tradition summaries) — content type that typologically expects low churn.

  Strength of support: Weak

  Summary: Reference material typologically exhibits low edit frequency, which provides a weak base-rate argument that "slow-changing" is plausible as a descriptor. However, this is a TYPOLOGICAL argument, not a MEASUREMENT of the specific 49 files. The presumption under examination is not "reference material is slow-changing in general" but "THESE 49 files are stable enough, without having measured." No literature supports "presume without measuring" as a valid practice in caching architecture — indeed, caching-layer design guides uniformly recommend characterizing input churn BEFORE sizing the cache.

  Caveats: (a) A typological argument is not a measurement; (b) Tom's wiki has a different usage pattern than public wikis — active research pushes could produce bursty edits; (c) the test is cheap (git log frequency count) — absence of the audit is itself a methodological gap; (d) cache-invalidation rate sensitivity is nonlinear — a 10% churn increase can be fine; a crossing of a threshold (e.g., >1 edit per session) produces near-total cache invalidation.

  Recommendation: NO-SUPPORT-FOUND (no literature supports the unmeasured "stable enough" claim; weak base-rate argument from typology does not substitute for measurement)
