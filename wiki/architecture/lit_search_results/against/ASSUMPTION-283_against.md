SEARCH-AGAINST-ASSUMPTION-283:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-283
  Original statement: Automating regeneration on a schedule is the right fix for "PRS triplets accumulate but the published connectome never changes."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-283
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated fix for a stale published artifact.
      15b: Searched for evidence that scheduling is the WRONG or insufficient fix for staleness.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Silent-cron-failure / unmonitored-job literature ("cron is where jobs go to die quietly"; SRE monitoring guidance, Google SRE Book ch. on monitoring). — A scheduled job that fails silently reproduces exactly the staleness it was meant to cure, and is HARDER to notice than a remembered manual chore because no human is in the loop. Scheduling without failure-alerting can worsen the problem.
    2. Dev/prod-parity failure (the actual 2026-06-07 incident; couples PRESUMPTION-317). — The scheduled context could not push, so "schedule it" did not in fact fix publishing; the fix presumed a capability the runtime lacked. Direct boundary condition.
    3. Push-vs-pull / event-driven freshness critiques (incremental/CDC vs batch refresh). — A fixed schedule is the crudest freshness mechanism: it is either too frequent (wasteful regen of an unchanged artifact) or too infrequent (stale between runs); event/threshold-triggered regeneration dominates fixed cadence for append-driven sources.

  Strength of challenge: Moderate

  Summary: Scheduling is challenged not as wrong-in-kind but as necessary-not-sufficient and crude. Three conditions break it: a silently failing job re-creates the staleness invisibly; the scheduled environment may lack the capability to publish at all (the realized incident); and fixed cadence is a blunt instrument versus event-triggered regeneration for an append-only source. "The RIGHT fix" overclaims; "a necessary part of the fix, with monitoring and capability parity" is defensible.

  Specific risks: A green-looking schedule masks a dead pipeline (false sense of freshness); regeneration runs but cannot publish (the incident); or the artifact regenerates too rarely to matter. Any of these returns the system to "the published connectome never changes," now with a dashboard that says it should.

  Mitigations available: Add dead-man's-switch / failure alerting on the job; verify publish capability in the scheduled context BEFORE relying on it (PRESUMPTION-317/318); prefer event/threshold-triggered regeneration (or at least log a no-op vs real-change diff each run); keep a visible "last successfully published" timestamp.

  STEELMAN:
    Item: ASSUMPTION-283
    Strongest counterargument: "Just schedule it" treats a systems problem (a derived artifact must stay in sync with an append-only source, in an environment able to publish, with failures surfaced) as a calendar problem. The most dangerous outcome is not that scheduling fails but that it appears to succeed: a cron entry exists, everyone assumes freshness, and the artifact silently stops updating the first time the job errors or the environment can't push — which is precisely what already happened.
    What would need to be true for C2A2 to be safe: The scheduled job runs in a context with verified publish capability, fails loudly (alert on miss/error), and emits a per-run change/no-op signal so staleness is observable, not assumed.
    How to test: Kill the credential/push path in staging and confirm the schedule SURFACES the failure rather than swallowing it; inject an append and confirm the next run publishes a visible diff.

  Recommendation: PARTIALLY-CHALLENGED
