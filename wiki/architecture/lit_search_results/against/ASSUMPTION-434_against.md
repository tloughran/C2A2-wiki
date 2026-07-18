SEARCH-AGAINST-ASSUMPTION-434:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-434
  Original statement: "Supabase free-tier projects pause after 7 idle days and a daily SELECT 1 resets the inactivity clock."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-434
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. [Supabase, current docs. "Project Pausing" (supabase.com/docs/guides/platform/free-project-pausing). — Official wording is hedged: a Free-plan project is considered inactive if it lacks "sufficient user database activity over the past week," with "typically a few user requests to the database each day" being enough. The policy is stated in terms of sufficiency judged by Supabase, not a deterministic "any single daily query resets a 7-day clock."]
    2. [Supabase GitHub Discussions, #38442. "Clarification on what 'inactivity' means." — The existence of an open clarification thread shows the activity definition is ambiguous even to users; community answers disagree on whether dashboard visits, REST API calls, or direct Postgres connections all count equally.]
    3. [travisvn, GitHub. "supabase-pause-prevention." — Community keep-alive tooling exists precisely because naive approaches fail; maintainers note the workaround depends entirely on the cron host staying online and on the query actually reaching the project through a counted path (REST API), i.e., a raw `SELECT 1` over a direct connection may not be the counted form of activity.]
    4. [SimpleBackups blog. "Supabase Free Tier Paused and Lost Data: What Happened." — Documents real cases of free-tier projects pausing despite users believing they had activity, and downstream data-restore complications; the pause threshold "can change as Supabase updates its policies."]
    5. [Natt, 2024. "Prevent Supabase free tier pauses using a cron job." — Even advocates of the SELECT-ping approach concede failure modes: cron host downtime, and requests that do not register as database activity (e.g., hitting a static page) do not reset the timer.]

  Strength of challenge: Moderate

  Summary: No source flatly contradicts the 7-day pause figure — it matches current Supabase documentation — but the second half of the claim is on shakier ground. Supabase's own policy language is probabilistic ("may pause," "sufficient user database activity," "typically a few requests each day"), not a hard clock reset by a single daily query. Community discussion threads exist specifically because the definition of counted activity is ambiguous (REST API vs direct SQL vs dashboard), and there are documented reports of projects pausing despite keep-alive attempts, usually because the ping did not traverse a counted path or the ping host itself failed. Finally, multiple sources note the threshold and policy have changed before and may change again, so the assumption has a shelf life.

  Specific risks: If the daily SELECT 1 travels a path Supabase does not count (e.g., a direct Postgres connection rather than the REST API), or if the policy changes, the project pauses silently; on free tier, a paused project's database is unreachable and restore is manual, so C2A2's DB-backed features fail exactly when nobody is watching.

  Mitigations available: Route the keep-alive through the REST API (PostgREST endpoint) which is unambiguously counted; verify outcome rather than intent — check project status via the Supabase management API or a reachability probe, and alert on pause-warning emails; keep an exported backup so a pause is an inconvenience, not data loss; re-verify the policy quarterly.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Strongest counterargument: The claim encodes a folk model ("7-day clock, one query resets it") of what is actually a discretionary, vaguely specified platform policy ("may pause projects exhibiting low activity"). Vendors change free-tier economics without notice, the counted-activity definition is undocumented at the granularity the claim requires, and there are field reports of keep-alive pings failing to prevent pauses. Treating a hedged vendor policy as a deterministic mechanism is the error.
    What would need to be true for C2A2 to be safe: The daily query must traverse a counted path (REST API), the 7-day/low-activity policy must remain stable, and the machine issuing the ping must itself be reliable — all three, continuously.
    How to test: Confirm the ping goes via the REST endpoint; monitor for Supabase's pre-pause warning email; optionally sacrifice a scratch free-tier project (ping it only via direct SQL for 8+ days) to empirically determine whether raw SQL counts.
