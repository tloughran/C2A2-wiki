SEARCH-AGAINST-PRESUMPTION-318:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-318
  Original statement: [inferred] Building the auto-push task before probing whether the sandbox could push presumed capabilities instead of checking them (violates Rules 1/8).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-318
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated build-then-discover ordering.
      15b: Searched for evidence that building before probing capabilities is a costly, recognized anti-pattern.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Walking-skeleton / spike / "prove the riskiest path first" (Cockburn; Freeman & Pryce, GOOS). — The discipline is explicit: when an end-to-end capability is uncertain, build the THINNEST end-to-end slice first to retire the risk; building the full feature before proving the path is the named anti-pattern.
    2. Fail-fast / shift-left and pre-mortem practice (Klein, "Performing a Project Premortem," HBR 2007). — Cheapest place to discover a missing capability is before you build on it; the cost of discovery rises monotonically the later it happens (shift-left). Build-then-discover maximizes that cost.
    3. Tom's own Rules 1 (Think Before Coding) and 8 (Read Before You Write). — The presumption is a direct violation of the project's own stated method: state assumptions, check rather than guess, read exports/callers before writing.

  Strength of challenge: Moderate-Strong

  Summary: There is broad, convergent evidence that building a capability-dependent artifact before confirming the capability is a recognized, costly anti-pattern (walking-skeleton, fail-fast, shift-left, pre-mortem), and it directly violates the project's own Rules 1 and 8. The cost is not just rework; it is rework discovered at the worst time (unattended run). This is a clean process-discipline lesson.

  Specific risks: Wasted build effort on an automation that cannot run; false confidence that the task is "done" until the scheduled run reveals the missing capability; reinforcement of a build-first habit that will recur on the next capability-dependent task. Tightly coupled to PRESUMPTION-317 (it is the procedural cause of that environment-mismatch).

  Mitigations available: Adopt capability-probe-first as a standing pre-step for any automation that depends on an environment capability (write a 3-line probe before the task); treat "can the target context actually do X?" as a Rule-1 assumption to verify, not guess; add a dry-run mode that exercises the path without side effects.

  STEELMAN:
    Item: PRESUMPTION-318
    Strongest counterargument: The ordering error is the root cause that the environment-mismatch (317) merely expresses: had a one-line "can I push from here?" probe run first, the entire auto-push task would not have been built against a capability the sandbox lacks. Every relevant discipline — walking skeleton, fail-fast, shift-left, pre-mortem — and the project's own Rules 1 and 8 say probe the uncertain capability before building on it. Building first converted a five-second check into a built-and-failed task.
    What would need to be true for C2A2 to be safe: Capability-dependent automation is preceded by an explicit capability probe (or dry run) in the target context, made a non-skippable step.
    How to test: Adopt the probe-first rule and check on the next capability-dependent task whether the probe catches the gap before any build occurs.

  Recommendation: CHALLENGED
