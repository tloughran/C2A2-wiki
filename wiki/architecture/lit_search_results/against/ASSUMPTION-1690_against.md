SEARCH-AGAINST-ASSUMPTION-1690:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1690
  Original statement: Supabase free-tier projects pause after ~7 days of inactivity (the C2A2 DB could pause ~10-01; keep-warm last ran 09-24).
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1690
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from ecosystem report eab829c8.
      15b: Searched for challenging literature (scheduled run 2026-09-29; sources marked 'search-result level' were not read in full)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Strength: Weak

  Sources:
    1. Same Supabase page: threshold is phrased as 'low activity', not zero activity, and the doc does not define 'low' numerically — so 'inactivity ~7 days' is an approximation and the exact trigger is vendor-controlled.
    2. Prior in-house 15b (revision_flags.md ~line 5601): free-tier policies change without notice and a synthetic query may not count as activity — not re-verified this run. SERP also showed third-party posts (simplebackups.com 'Supabase Free Tier Paused and Lost Data') of data-loss cases; not read in full, so the loss claim is unverified.

  STEELMAN: 'roughly 7 days' is safe only if the keep-warm ping is counted as activity and the policy is unchanged. If keep-warm last ran 09-24, the 7-day mark lands ~10-01, so the ~10-01 pause estimate is a lower-bound risk date, not a certainty; the correct action is to verify keep-warm ran, not to trust the estimate.

  SYSTEMIC-RISK: see run note in for_lit_search.md (2026-09-29).

---
SUPPLEMENT — second 15b pass, same date (concurrent-writer collision; appended, nothing above
removed). This pass did NOT read lit_search_results/for/. It agrees with the block above on
PARTIALLY-CHALLENGED and rates the strength Moderate rather than Weak, because the primary docs
give a specific safe-activity level that one weekly ping does not meet.

SEARCH-AGAINST-ASSUMPTION-1690 (supplement):
  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1690
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from ecosystem report eab829c8.
      15b: Searched for challenging literature (lane: vendor documentation, time-sensitive)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Supabase Docs, "Project Pausing" (supabase.com/docs/guides/platform/free-project-pausing).
       [FETCH FAILED for this pass: the tool returned "already fetched" with no content visible.
       Wording from search-result extracts of this page.] Free projects showing "low activity over
       a 7-day period" are paused. Inactive means not receiving "sufficient user database activity
       over the past week". "Typically a few user requests to the database each day over the
       previous week" prevents pausing.
    2. Supabase Docs, "Billing FAQ" (modified 2026-09-28). [Fetched: full.] Paid plans: "no project
       pausing". A separate pause route exists: the Fair Use Policy can pause projects for orgs
       that keep exceeding Free Plan quota, and overdue invoices also trigger pausing.
    3. Supabase Docs, Troubleshooting, "How To Restore a Project Paused for More Than 1 Year" (edited
       9/28/2026). [Fetched: full.] Studio restore is available for up to 1 year after pausing.
       After that, recovery is manual from backups. The 90-day figure in third-party posts is
       outdated.
    4. Supabase Docs, Troubleshooting, "Pausing Pro-Projects". [Fetched.] Pro projects cannot be paused.

  Strength of challenge: Moderate (on timing and definition; the headline "free projects pause
    after about a week of low activity" is SUPPORTED by the primary source)

  Summary: The criterion is a rolling, undisclosed "sufficient activity" level, with "a few
  requests each day" named as typical. It is not a 7-days-since-last-request countdown. A single
  keep-warm on 09-24 may already count as insufficient, so ~10-01 is a best-case date, not a
  deadline. Quota and billing are extra pause triggers. Severity is lower than older guidance
  suggests, since restore is available for 1 year.

  Specific risks: The DB may pause before 10-01 or may already be paused. Writes to a paused DB fail,
    silently if failures are not surfaced.

  Mitigations available: Run keep-warm daily with real queries on a user table. Check project status
    directly (read-only) instead of inferring it from dates. Alert on pause. Use the paid tier if
    the DB is load-bearing.

  Search scope: 2 searches, 4 fetch attempts (3 succeeded). Time-sensitive: the docs changed
    2026-09-28.
  Excluded results: simplebackups.com, itpathsolutions.com, aiagencyplus.com, adhdecode.com,
    tellmewhendown.com, vibeanswers.com, medium.com, dev.to (SEO/vendor; several claim "any
    request counts", which conflicts with the primary docs); github.com/travisvn/supabase-pause-prevention
    (tool repo); supabase GitHub issue #37453 (user issue).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1690
  Strongest counterargument: The 7-day figure is not a countdown timer. Supabase judges
    "sufficient" weekly activity against an undisclosed threshold and names "a few requests each
    day" as safe. A lone ping on 09-24 is the pattern most likely to be judged insufficient, so the
    DB may pause before 10-01. Quota and billing triggers sit outside the model entirely.
  What would need to be true for C2A2 to be safe: Keep-warm runs at least daily with real DB
    queries, or status is directly confirmed ACTIVE before the estimated date.
  How to test: Query project status now (read-only). Confirm keep-warm ran on at least 5 of the
    last 7 days.
