SEARCH-FOR-ASSUMPTION-434:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-434
  Original statement: "Supabase free-tier projects pause after 7 idle days and a daily SELECT 1 resets the inactivity clock."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-434
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Supabase, 2026 (current as of search date). "Project Pausing." Official docs, supabase.com/docs/guides/platform/free-project-pausing. — Confirms: "Supabase pauses Free Plan projects that show low activity over a 7-day period." A project is inactive if it lacks "sufficient user database activity over the past week"; "typically a few user requests to the database each day over the previous week is enough to keep the project from being paused." Also documents a warning email ~1 week before pause and a 90-day restore window.
    2. travisvn, 2024–2026. "supabase-pause-prevention." GitHub repository. — Widely used community keep-alive project whose entire premise is that a scheduled trivial database query prevents free-tier pausing; documents the practice as effective in production use.
    3. Shadhujan, 2026. "How to Keep Supabase Free Tier Projects Active (2026 Guide)." Medium. — States the 7-day window is tracked against database activity (not dashboard visits or API pings that don't hit the DB), and that any database activity, including trivial inserts/selects to a ping table, resets the inactivity timer.
    4. Level Up Coding / gitconnected, 2025–2026. "Supabase Free Tier Will Pause Your App. Here's the GitHub Actions Fix." — Describes the standard GitHub Actions cron pattern issuing a scheduled query; reports that as long as the workflow runs within the 7-day window the pause timer never expires.

  Strength of support: Strong (7-day pause policy, DB activity as the criterion); Moderate (that one daily SELECT 1 is sufficient)

  Summary: Supabase's current official documentation directly confirms the first half of the claim: Free Plan projects with insufficient database activity over a 7-day window are paused, and activity is defined as user database queries. The second half — that a single daily SELECT 1 resets the clock — is strongly supported by widespread, working community practice (dedicated keep-alive repos and CI cron recipes), and is consistent with the docs' statement that "a few user requests to the database each day" typically suffices. A daily scheduled query comfortably exceeds the once-per-week minimum implied by the 7-day window, so the practice is over-provisioned relative to the policy.

  Caveats: The official docs use hedged language ("sufficient" activity, "typically a few requests each day"), and do not formally guarantee that exactly one trivial SELECT per day is always enough — Supabase reserves judgment on what counts as sufficient. The policy is a vendor policy, not a standard, and can change without notice (the docs themselves note pausing exists "to save server resources"); the claim's own framing acknowledges this via the queued keep-warm design. Community sources are practitioner reports, not vendor guarantees.

  Search scope confidence: comprehensive (official current docs fetched directly plus multiple independent 2025–2026 practitioner sources)

  Recommendation: PARTIALLY-SUPPORTED
