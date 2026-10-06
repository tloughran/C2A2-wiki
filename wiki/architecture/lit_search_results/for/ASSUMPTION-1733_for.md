SEARCH-FOR-ASSUMPTION-1733:
  Date searched: 2026-10-03
  Original item: ASSUMPTION-1733
  Original statement: A bare `SELECT 1` sent over the API counts as activity for Supabase's free-tier inactivity pause.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1733
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 322480f4 and 0dda1a36.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Supabase docs, "Project Pausing" (markdown version). https://supabase.com/docs/guides/platform/free-project-pausing.md [fetched] — A project counts as inactive if it "does not receive sufficient user database activity over the past week"; "Typically a few user requests to the database each day over the previous week is enough"; after a warning email, the pause can be prevented by "making API calls to your project or sending requests via your connected application." The page does not define "user database activity", does not mention SELECT 1, and gives no threshold.
    2. travisvn, "supabase-pause-prevention" (GitHub) and DEV Community post "Stop Supabase projects from being paused". https://github.com/travisvn/supabase-pause-prevention ; https://dev.to/travisv/stop-supabase-projects-from-being-paused-36nf [search-result] — Community keep-alive tool that runs scheduled database queries. Practitioners report it works. Not official.
    3. runhooks.app, "Preventing Supabase Free Tier Pausing". https://runhooks.app/blog/preventing-supabase-free-tier-pausing/ [search-result] — Vendor blog says the 7-day window is tracked against database activity, and that a scheduled request "as simple as a SELECT 1" or a weekly ping is enough. Third-party claim with a commercial interest; not verified.
    4. OpenSourcePatents, "Supabase_Keepalive" (GitHub), and a gitconnected Medium article on a GitHub Actions fix [search-result] — More community keep-alive patterns of the same kind.

  Strength of support: Weak-to-Moderate

  Summary: The official docs say that user requests to the database, and API calls, are the activity that prevents pausing. A SELECT 1 sent through an API path that reaches Postgres as a user query plausibly fits that description. Several community tools rely on trivial scheduled queries and report that they work, which is anecdotal precedent. No official source says whether a constant query with no table access, sent as a single daily request, counts as "sufficient". The docs say activity must be "sufficient", "a few requests each day" is the documented baseline, and usage "may not be enough" even when the project is in use.

  Caveats: (a) "User database activity" is undefined. Supabase may filter out health-check-like or internal traffic, and the docs say nothing about how SELECT 1 is classified. (b) The route matters. A REST/PostgREST call, an RPC, and a direct pooler connection may be counted differently. A bare SELECT 1 cannot be issued through PostgREST without an RPC function. (c) A single daily call is below the documented "a few requests each day". (d) Community claims are survivorship-biased: users whose projects paused anyway rarely publish. (e) Docs can change, and the page wording differs from the version recorded in ASSUMPTION-1730.

  Search scope: preliminary search (1 search, 1 fetch); web-only; official docs plus community or vendor pages. No Supabase support threads or GitHub discussions were fetched.

  Recommendation: PARTIALLY-SUPPORTED
