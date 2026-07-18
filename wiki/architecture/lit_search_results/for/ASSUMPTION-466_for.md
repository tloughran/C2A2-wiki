SEARCH-FOR-ASSUMPTION-466:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-466
  Original statement: The metabolism regen script presumes `~/` resolves to the Mac home; in scheduled sandbox context it resolves to the sandbox home, so it cannot reach the live OpenStory db (exit 1). (Compounded by the OpenStory writer freeze: db unwritten since 07-05.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-466
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run (metabolism regen exit 1)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Cronitor, "Crontab environment variables." — Documents that scheduled (cron) jobs run in their own minimal environment; HOME is set from /etc/passwd for the executing user, which need not match the interactive user's home. Grounds the claim that `~/`/HOME resolves differently under the scheduler.
    2. Baeldung on Linux, "How to Load Environment Variables in a Cron Job." — Confirms cron executes in a non-interactive, non-login shell that does not source ~/.bashrc/.bash_profile, so environment (including path anchors) differs from an interactive Mac session.
    3. w3tutorials.net, "Where to Set Environment Variables for Crontab." — Reinforces that user-defined environment present interactively is absent under the scheduler unless explicitly re-established.

  Strength of support: Strong

  Summary: The literature strongly supports the core mechanism: a script that hard-codes `~/` or relies on an implicit HOME will resolve to a different location when invoked headless by a scheduler than when run interactively by the user, because the scheduled context supplies its own minimal environment. This is a textbook cron/scheduled-context pitfall, so the metabolism script reaching the sandbox home (and failing to find the Mac-resident OpenStory db, exit 1) is exactly the predicted behavior. The remedy in the literature — explicit, absolute, mount-aware paths rather than `~/` — is well established.

  Caveats: The compounding OpenStory writer-freeze (db unwritten since 07-05) is a SEPARATE fault; even with correct path resolution the db would be stale. Support is for path-resolution as the proximate exit-1 cause, not for the freeze.

  Recommendation: SUPPORTED
