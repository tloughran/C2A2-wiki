SEARCH-FOR-PRESUMPTION-490:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-490
  Original statement: [inferred] Scripts that run correctly when invoked by a human on the Mac are presumed to behave identically when invoked headless by the scheduler in the sandbox (HOME, filesystem reach, credentials, lock state) — falsified twice today (metabolism `~/`, c282 index.lock).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-490
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from two same-day context-dependence failures
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Mattrickard, "Environment Parity"; Box Blog, "Dev and prod parity"; KodeKloud, "Dev/Prod Parity" (12-Factor). — The 12-Factor "dev/prod parity" factor exists precisely because the same code behaves differently across contexts that differ in environment; the literature treats context-identity as something to ENGINEER, not presume.
    2. Bazel, "Hermeticity"; DevSecOpsSchool, "Reproducible Builds." — Hermetic execution is defined as insulation from external mutable state (HOME, host tools, filesystem); non-hermetic execution is documented to produce runner-specific, context-specific breakage — exactly HOME/reach/lock divergence.
    3. Cronitor, "Crontab environment variables." — Scheduler contexts supply a distinct minimal environment; corroborates that headless/scheduled invocation is not identity-equivalent to interactive invocation.

  Strength of support: Strong

  Summary: The presumption's NEGATION is what the literature endorses: identical behavior across execution contexts must be secured by hermeticity/parity engineering, and its absence reliably yields context-specific failures (environment, filesystem reach, credentials, lock state). The two same-day falsifications (metabolism `~/`, c282 index.lock) are canonical non-hermetic failures. Thus 15a strongly SUPPORTS the (14b-surfaced) claim that the presumption is unsafe — i.e., the literature supports that "runs on the Mac ⇒ runs headless in sandbox" is an unwarranted assumption.

  Caveats: Direction note — here "support" means support for the presumption being a genuine, literature-recognized blind spot (parity is not free). The remedy space (hermetic wrappers, explicit env, context audits) is well developed, so the risk is addressable.

  Recommendation: SUPPORTED
