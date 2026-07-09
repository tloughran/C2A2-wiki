SEARCH-FOR-ASSUMPTION-363:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-363
  Original statement: "That a Cowork-app-dependent 6-hour scheduled task is adequate cadence to keep the local Heartbeat fresh ('runs only while the Cowork app is open')"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-363
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: app-gated 6h scheduled refresh assumed adequate for Heartbeat freshness
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Cache/TTL freshness theory (HTTP caching, RFC 7234 max-age semantics). - Fixed-interval refresh is an accepted freshness model WHEN the staleness tolerance exceeds the interval; a 6h cadence is adequate for content that changes on a daily-or-slower timescale.
    2. Cron / periodic-poll scheduling norms (watchflow, "Why Cron Jobs Fail Silently"). - Periodic polling is the standard mechanism for keeping a derived view fresh; the cadence VALUE is a tunable, not a defect, when matched to the source change rate.

  Strength of support: Weak

  Summary: The literature supports periodic refresh as a freshness mechanism and gives no reason to reject a 6-hour cadence per se: cadence adequacy is a function of the underlying change rate and staleness tolerance, and for slow-changing Heartbeat content 6h is plausibly fine. However, support attaches only to the cadence NUMBER. It does not extend to the load-bearing clause "runs only while the Cowork app is open," which makes EXECUTION conditional on an external app being foregrounded - a property the freshness literature assumes away (it presumes the scheduler actually runs).

  Caveats: Support is conditional on the source changing slower than 6h AND the job actually executing. The app-gating condition is exactly where 15b concentrates.

  Search scope: TTL/freshness models; periodic-poll scheduling. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-FOR-ASSUMPTION-363 (RE-TRIGGER cycle 1):
  Date searched: 2026-07-08
  Original item: ASSUMPTION-363
  PROVENANCE:
    Chain: [... -> 15c -> 15d -> 15a] (cycle 1, 2026-07-08)
    Transform: 15d weekly re-trigger 2026-07-05; 15a refreshed supportive search
    Current status: SUPPORTED
  New sources since last cycle: Yes (HackerNoon polling tradeoffs; arXiv 2603.09738; Altss cadence glossary)
  Strength of support: Moderate
  Summary: Refresh-cadence literature reaffirms matching cadence to source change-rate ('slowest acceptable cadence'); a 6-hourly poll of a slowly-changing local vault sits comfortably within guidance. 'App-open/local-only' caveats are operational, not principle-violating. Trajectory stable.
  Recommendation: SUPPORTED / Hold Moderate; cadence value well-justified by change-rate matching.
