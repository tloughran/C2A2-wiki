SEARCH-AGAINST-ASSUMPTION-1730:
  Date searched: 2026-10-02
  Original item: ASSUMPTION-1730
  Original statement: Supabase free-tier projects pause after 7 days of inactivity, and a daily `SELECT 1` prevents the pause.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1730
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the keep-warm task prompt (1c750b65).
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Supabase docs, "Project Pausing" [fetched] — criterion is 'low activity' with undefined threshold; no distinction between API and direct DB queries; no guidance on keep-alive pings; Pro projects cannot be paused.
    2. travisvn/supabase-pause-prevention https://github.com/travisvn/supabase-pause-prevention ; dev.to/travisv/stop-supabase-projects-from-being-paused-36nf ; runhooks.app/blog/preventing-supabase-free-tier-pausing [search-snippets, unverified] — community keep-alive practice.

  Strength of challenge: Weak

  Summary: The 7-day low-activity pause is confirmed, but the docs say 'low activity' with an undefined threshold, not 'any request'. That a synthetic SELECT 1 (especially over a direct connection) counts is an inference from community practice, not documented policy.

  STEELMAN: Supabase can tighten the activity heuristic at any time; a trivial SELECT 1, especially over a direct connection that may not register in API-level metrics, may not count, and one daily query sits at the minimal edge of 'a few requests per day'. A reliable guard needs monitoring (alert on paused state) or the Pro plan.

  Caveats: No community claim verified; docs imply both API and DB activity count.

  Search scope: preliminary search — broader search recommended (1 docs fetch, 2 searches); web-only; independent of 15a — 15a results were not read by the 15b searcher.

  Recommendation: PARTIALLY-CHALLENGED
