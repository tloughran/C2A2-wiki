SEARCH-FOR-ASSUMPTION-1690:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1690
  Original statement: Supabase free-tier projects pause after ~7 days of inactivity (the C2A2 DB could pause ~10-01; keep-warm last ran 09-24).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1690
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from ecosystem report eab829c8.
      15a: Searched for supporting literature (scheduled run 2026-09-29; depth: web search + selective fetch; sources marked 'search-result level' were not read in full)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Strength: Strong

  Sources:
    1. Supabase Docs, 'Project Pausing' (fetched 2026-09-29). https://supabase.com/docs/guides/platform/free-project-pausing — free projects pause on 'low activity over a 7-day period'; 'a few user requests to the database each day over the previous week' suffices to avoid pausing; dashboard visits, API calls and app requests count; a warning email is sent roughly one week before pausing; paused projects are restorable from the dashboard for up to 1 year; paid-plan projects are exempt.

  Notes: Primary vendor documentation, fetched today. Consistent with prior ASSUMPTION-434 (7 idle days; daily SELECT 1 resets the clock) which is already in the monitor queue.
