SEARCH-AGAINST-ASSUMPTION-1230:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1230
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High) [CHALLENGED-in-house: 2026-08-27]
  Original statement: A health check that reads the scheduler establishes that the scheduled work happened;
    a green verdict may be issued by an instrument that has declared its own read failure.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1230
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim, then falsified in part by listing `changelog/` and `metrics/` — no 2026-08-26
        outputs exist.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on the limits of synthetic/output-based
    monitoring — chosen deliberately, because the easy challenge (liveness is not correctness) is one the
    for direction already establishes, and the useful challenge is against the *remedy*. Reached: Splunk,
    "Assert Like You Mean It: How To Validate Outcomes in Synthetic Tests"; USENIX ;login: on synthetic
    monitoring and E2E testing; dotcom-monitor and UptimeRobot practitioner material; Microsoft's
    Code-With engineering playbook. NOT COVERED: incident post-mortem corpora that would quantify how often
    synthetic checks miss real outages. All SNIPPET-ONLY. Confidence: MODERATE.

  Challenging evidence found: Yes — against the remedy; none found defending the assumption itself

  Sources:
    1. Splunk, "Assert Like You Mean It: How To Validate Outcomes in Synthetic Tests" [SNIPPET-ONLY]
       https://www.splunk.com/en_us/blog/observability/synthetic-test-assertions.html —
       The operative warning: without assertions you are left with surface-level checks — "did the page load
       or not" — and "a test can pass even when functionality is broken." An artifact-existence check that
       does not assert on content is the same class of instrument as the scheduler check it replaces.
    2. USENIX ;login:, "Synthetic Monitoring & End-to-End Testing: Two Sides of the Same Coin"
       [SNIPPET-ONLY] https://www.usenix.org/publications/loginonline/synthetic-monitoring-e2e-testing-two-sides-same-coin —
       Treats synthetic monitoring and E2E testing as the same discipline with the same blind spots, rather
       than as a stronger instrument.
    3. dotcom-monitor / UptimeRobot practitioner guides [SNIPPET-ONLY] — Multi-step flows fail in ways basic
       uptime checks miss; a page can load while a submit breaks. The analogue: a `changelog/` file can exist
       while its content is empty, stale or an error transcript.

  Strength of challenge: Moderate — and it does not rescue the assumption

  Summary: Nothing was found that defends reading a scheduler as evidence of output; the assumption as
    stated has no support in either direction and is additionally falsified in-house. What the against
    direction contributes is a constraint on the fix. Moving the monitor from scheduler state to artifact
    existence buys less than it appears to: the monitoring literature's repeated finding is that a check
    without assertions on content passes while the thing it monitors is broken, and an existence check is a
    check without assertions. The estate would move from one green-when-wrong instrument to another, with
    the added risk that the second one looks rigorous.

  Specific risks: (a) An artifact-existence monitor declares green on a zero-byte or error-transcript
    output. (b) The second limb — a monitor reporting green while declaring its own read failure — has no
    defence in any literature reached and is a plain defect; fixing only the first limb leaves it standing.
    (c) The 2026-08-26 miss went unreported for a full day, so the estate's current detection latency for
    total pipeline failure is at least 24 hours and is not itself monitored.

  Mitigations available: Assert on content, not existence: the check should read the artifact and confirm a
    property it could not have by accident (a date stamp inside the file matching the run date, a non-zero
    item count). Make an unreadable source produce UNKNOWN rather than green — a monitor that cannot see
    must not vote. Add a dead-man's window so absence alarms without anyone asking.

  STEELMAN:
    Item: ASSUMPTION-1230
    Strongest counterargument: A scheduler-reading check is not claiming to prove output; it is a cheap
      first-tier signal, and demanding that every monitor assert on content is how monitoring systems become
      expensive, brittle and eventually unmaintained — at which point the estate has no monitor at all. The
      failure on 2026-08-26 was a failure to have a second tier, not a failure of the first.
    What would need to be true for C2A2 to be safe: the tiering would have to be explicit, so that a green
      first-tier signal is reported as "scheduler ran," never as "pipeline healthy," and the absence of a
      second tier is visible rather than implied.
    How to test: read the monitor's own output text. If it says "healthy" or "green" rather than "scheduler
      reachable, outputs unverified," the tiering is not explicit and the steelman does not apply.

  Recommendation: CHALLENGED
