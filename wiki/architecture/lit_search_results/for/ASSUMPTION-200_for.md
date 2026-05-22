SEARCH-FOR-ASSUMPTION-200:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-200
  Original statement: "Four Sunday-cron tasks fired Monday catch-up instead of Sunday; re-check next Sunday."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-200
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: four Sunday-scheduled cron tasks fired Monday as catch-up rather than on Sunday; flagged to re-check next Sunday.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. anacron(8) / systemd.timer Persistent= semantics. — Missed scheduled jobs firing late as catch-up on next wake is documented, intended behavior for persistent timers; a Monday catch-up of Sunday jobs is consistent with this.
    2. Quartz Scheduler misfire-handling docs. — Schedulers define explicit misfire policies (fire-now catch-up vs skip); late catch-up firing is a standard, expected outcome, not necessarily a bug.
    3. Google SRE (2016), cron chapter. — Distinguishing missed-fire catch-up from genuine scheduling failure requires observing the next scheduled occurrence — exactly the premise's "re-check next Sunday".

  Strength of support: Strong

  Summary: The premise is well supported: late catch-up firing of missed scheduled jobs is documented behavior (anacron Persistent timers, scheduler misfire policies), so a Monday catch-up of Sunday tasks is plausibly benign. The premise's own remedy — re-check next Sunday to see whether it fires on time — is precisely the right diagnostic per SRE practice. Strong support for both the explanation and the verification plan.

  Caveats: Support is for 'catch-up is a known benign-or-bug-ambiguous behavior; verify on next occurrence'; it cannot pre-confirm which case this is.

  Recommendation: SUPPORTED (explanation plausible; verification plan correct)
