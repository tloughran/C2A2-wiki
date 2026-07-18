SEARCH-AGAINST-ASSUMPTION-466:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-466
  Original statement: The metabolism regen script presumes `~/` resolves to the Mac home; in scheduled sandbox context it resolves to the sandbox home, so it cannot reach the live OpenStory db (exit 1). (Compounded by the OpenStory writer freeze: db unwritten since 07-05.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-466
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Cronitor, "Crontab environment variables." — Cron DOES set HOME (from /etc/passwd) for the executing user; `~/` therefore resolves to a valid home under the scheduler, not to nothing. So the failure is not "`~/` is unset" but "the resolved home is the wrong filesystem" — a mount-REACH problem more than a tilde-resolution bug.
    2. Baeldung, "Load Environment Variables in a Cron Job." — The remedy space (BASH_ENV, explicit absolute paths, exported HOME) means `~/` dependence is easily corrected; if exit 1 persists after that, the cause lies elsewhere (mount reach or the writer freeze).

  Strength of challenge: Weak-Moderate

  Summary: The challenge is narrow: the item's own parenthetical concedes the OpenStory writer freeze (db unwritten since 07-05), which means correcting `~/` would still not yield fresh data — so `~/` is at most the proximate exit-1 trigger, not the operative reason the metabolism view is stale. Further, the scheduler does set HOME, so the precise defect is that the sandbox HOME cannot REACH the Mac-resident db (a mount-scoping issue), which a simple `~/`→absolute-path fix may not resolve if the mount doesn't expose the db at all.

  Specific risks: A pure path-resolution fix (`~/`→absolute) could be shipped, exit-1 could disappear, and the metabolism view could still be stale because the db itself is frozen — a false "fixed."

  Mitigations available: Fix path portability AND verify (a) the mount exposes the live db path and (b) the OpenStory writer is unfrozen; only then does the view refresh. Bind the "refreshed" claim to db mtime (ties to P-491).

  STEELMAN:
    Strongest counterargument: The exit-1 is real and path-driven, but curing it would only convert a loud failure into a silent staleness, because the db is frozen. The assumption correctly names a bug but mislocates the operative cause of the stale metabolism view.
    What would need to be true for the assumption to be the whole story: The OpenStory db must actually be live and reachable once `~/` is corrected — i.e., the writer freeze must not exist.
    How to test: After making the path absolute, check the metabolism db's last-write timestamp; if still 07-05, the freeze (not `~/`) is the operative cause.

  Recommendation: PARTIALLY-CHALLENGED
