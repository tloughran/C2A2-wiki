SEARCH-FOR-PRESUMPTION-547:
  Date searched: 2026-07-26
  Original item: PRESUMPTION-547
  Original statement: [inferred] Falling back to the 07-24 summary when the morning sync fails is presumed an adequate substitute, but "most recent successful summary" decays each dark day; after 6 consecutive dark runs the fallback presumes yesterday ≈ today while the last genuine Chat context recedes — staleness treated as freshness.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-547
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a multi-day-old fallback presented as adequate current context
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Bounded-staleness / stale-if-error discipline (Fastly stale-while-revalidate & stale-if-error docs; application-level caching study, Mertz & Nunes). — The accepted pattern serves last-known-good ONLY within a bounded window and with an explicit freshness/TTL limit; "the key is setting appropriate time limits on how long stale data can be served before it must be discarded." An UNBOUNDED fallback that re-serves a 6-day-old summary violates the very discipline that makes stale-serving safe. Supports the presumption that a decaying fallback without a staleness bound is a defect, not a feature.
    2. Cache-invalidation / staleness literature (daily.dev, "Cache Invalidation vs Expiration"; Tacnode, "Stale Data: freshness SLAs"). — Staleness is defined relative to an expiry; serving expired data AS IF current is the canonical staleness bug. Directly supports "staleness treated as freshness": re-emitting the last successful summary without annotating its age conflates not-yet-replaced with still-valid.
    3. Stale-context risk for automated decisions (Tacnode; graceful-degradation-for-AI literature). — "For AI and automated decisions, stale context is especially dangerous because models act confidently on outdated inputs." An agent consuming a 6-day-old summary as today's context is exactly this hazard: confident action on decayed input, with the error growing each dark day.

  Strength of support: Strong

  Summary: Strongly supported. The resilience literature endorses last-known-good fallback, but ONLY as BOUNDED staleness with an explicit age limit and (ideally) a staleness annotation; the defect here is that the fallback is unbounded and unlabeled, so a 6-day-old summary is consumed as current. Cache theory names this the core staleness bug — serving expired data as fresh — and the automated-decision literature flags stale context as especially dangerous because downstream agents act confidently on it. The monotonic decay ("each dark day the gap grows") means the adequacy of the substitute is not constant, contradicting the presumption that yesterday ≈ today. The remedy the literature prescribes is a freshness SLA: cap the fallback age and surface the age so consumers can discount it.

  Caveats: Bounded stale fallback IS a legitimate, valuable pattern (see 15b) — the support is for bounding and labeling it, not for failing hard on the first dark day.

  Recommendation: SUPPORTED
