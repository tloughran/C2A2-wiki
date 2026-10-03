SEARCH-AGAINST-ASSUMPTION-1733:
  Date searched: 2026-10-03
  Original item: ASSUMPTION-1733
  Original statement: A bare `SELECT 1` over the API counts as activity for Supabase's free-tier inactivity pause.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1733
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 322480f4 and 0dda1a36.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Supabase docs, "Project Pausing" (page modified 2026-10-02), https://supabase.com/docs/guides/platform/free-project-pausing [fetched] — Criterion is "sufficient user database activity over the past week"; "projects with too few user queries ... are the clearest candidates for pausing"; "While you may be actively using the project, it's possible that usage is not enough to exclude it"; "Typically a few user requests to the database each day ... is enough". Remedy given: "Generate a sufficient amount of activity by making API calls". No threshold, no statement on whether trivial/synthetic queries count, no definition of "user" query. Only guaranteed prevention: Pro plan.
    2. simplebackups.com/blog/supabase-free-tier-paused; runhooks.app/blog/preventing-supabase-free-tier-pausing [search-result, unverified] — Community claims that "any request counts" and "one request a day is enough". These are third-party assertions, not policy, and conflict in strength with the docs' "a few requests each day".
    3. [background-knowledge] Supabase's REST API (PostgREST) does not expose raw SQL; a "SELECT 1 over the API" must go through an RPC function, the Management API SQL endpoint, or a direct Postgres connection. The Management API / dashboard SQL path may run as a privileged/service role and could plausibly be excluded from "user database activity". Unverified — no source found either way.

  Strength of challenge: Weak-to-Moderate

  Summary: The docs do not contradict the claim outright, but they qualify it in three ways that matter: (a) the criterion is "user" database activity/"user queries", a phrase that leaves room to exclude synthetic or system-role traffic; (b) the threshold is "sufficient", explicitly warning that genuine usage may not be enough; (c) the documented norm is "a few user requests each day", so a single daily SELECT 1 sits at or below the stated typical floor. Community sources asserting "any request counts" are unverified and not authoritative. Whether a bare SELECT 1 counts is therefore undocumented; the claim rests on practice, not policy.

  STEELMAN:
    Item: ASSUMPTION-1733
    Strongest counterargument: Supabase defines inactivity by "user database activity" against an unpublished, changeable threshold and states that real usage can still be insufficient. A single trivial query, possibly routed through a management or service-role path rather than a user role, is precisely the kind of activity a provider would discount if it wanted to stop keep-alive gaming of free resources. The docs give "a few user requests each day" as the typical floor, so one SELECT 1 per day is below the documented norm. Because the warning email arrives about one week before the pause, a silent failure of the ping is recoverable only if someone reads that email.
    What would need to be true for C2A2 to be safe: The ping goes through a path that registers as user activity (e.g., PostgREST/RPC with the anon or authenticated key), runs several times per day, and a monitor checks the project's actual status (not just the ping's success).
    How to test: Log the ping's role/path; check the project's status via the Management API daily; check the owner inbox for pause-warning emails; ideally run a sacrificial free project with only SELECT 1 pings for >14 days.

  Specific risks: Keep-warm task reports success while the project still accrues "inactive" status and pauses; downstream jobs fail silently.

  Mitigations available: Multiple daily pings via the user-facing API; status-based monitoring; Pro plan.

  Caveats: No evidence found that SELECT 1 is excluded; the challenge is from definitional ambiguity in the docs, not a documented failure. The background-knowledge point about routes is unverified.

  Search scope: preliminary search (1 search, 1 fetch); web only; independent of 15a — 15a results were not read.

  Recommendation: PARTIALLY-CHALLENGED
