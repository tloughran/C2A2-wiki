SEARCH-FOR-ASSUMPTION-1230:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1230
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High) [CHALLENGED-in-house: 2026-08-27]
  Original statement: A health check that reads the scheduler establishes that the scheduled work happened;
    and a green verdict may be issued by an instrument that has declared its own read failure.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1230
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim, then falsified in part by listing `changelog/` and `metrics/` — no 2026-08-26
        outputs exist.
      15a: Searched for supporting literature
    Current status: SUPPORTED (for the distinction; the item's own claim is thereby refuted)

  Search scope: WebSearch, 2026-08-28, two dedicated queries — liveness vs black-box/end-to-end monitoring,
    and dead-man's-switch detection of missing outputs. Literature reached: Frontiers in Computer Science
    (2026) on health-box testing in microservice architectures; SRE practitioner material on black-box vs
    white-box monitoring; Kubernetes probe semantics; dead-man's-switch engineering write-ups including
    OneUptime and Datashelter. NOT COVERED: Google's SRE book in primary form, and the formal
    runtime-verification literature on liveness vs safety properties, which is the theoretically exact
    framing and was not reached. All sources SNIPPET-ONLY. Search confidence: HIGH.

  Supporting evidence found: Yes — for the *distinction*, which cuts against the item's claim

  Sources:
    1. Anon., "Vitality assurance in microservice architectures: introducing the health box testing
       methodology," Frontiers in Computer Science (2026), doi:10.3389/fcomp.2026.1811944 [SNIPPET-ONLY;
       authors unverified] — Distinguishes service-local liveness/readiness endpoints from synthetic
       monitoring (scripted end-to-end transactions) and from testing in production, treating them as
       different instruments answering different questions.
    2. Dylan Dumont, "Health Checks That Actually Work: Liveness vs Readiness vs Startup Probes," DEV
       Community [SNIPPET-ONLY] https://dev.to/dylan_dumont_266378d98367/health-checks-that-actually-work-liveness-vs-readiness-vs-startup-probes-545e —
       States the scope rule directly: a liveness check determines only whether the process is alive and
       able to serve, and "should not check external dependencies, database connectivity, or complex
       business logic." A scheduler-reading check is a liveness check by this definition.
    3. Kriss-V, `deadmancheck` — "Cron job monitoring that alerts when jobs run but do nothing"
       [SNIPPET-ONLY] https://github.com/Kriss-V/deadmancheck ; Crontap, "Dead man's switch, explained for
       developers" [SNIPPET-ONLY] https://crontap.com/blog/dead-man-switch-explained-for-developers ;
       Datashelter, "Backup Monitoring: Solving the Dead Man's Switch Problem" [SNIPPET-ONLY]
       https://datashelter.tech/blog/backup-monitoring-dead-mans-switch —
       Three independent statements of the operative point: for unattended jobs the most dangerous failure
       is the one that produces no output at all; "in many incidents, the first sign of failure is silence";
       and the design rule is that *absence of signal must itself be treated as failure*, with output
       assertions on the payload rather than a bare liveness ping.
    4. Web-alert / PulsAPI, "Black-Box vs White-Box Monitoring" [SNIPPET-ONLY]
       https://web-alert.io/blog/black-box-vs-white-box-monitoring-difference —
       "Each is blind exactly where the other sees clearly." Supports the claim that a single instrument
       reading the scheduler cannot cover the artifact-production question.

  Strength of support: Strong — but supporting the *negation* of the item as stated

  Summary: This is the unusual case where a thorough supportive search returns a strong result that runs
    against the item. The monitoring literature is unambiguous that liveness and correctness are distinct
    properties requiring distinct instruments, that a liveness probe is explicitly scoped to exclude
    business outcomes, and that for unattended scheduled work the characteristic failure is silence — which
    is why the dead-man's-switch pattern exists and why practitioners insist on output assertions rather
    than run-completion pings. No source was found that treats scheduler state as evidence of output. On the
    second limb — a green verdict issued by an instrument that has declared its own read failure — nothing
    supportive was found and nothing defends the practice; the nearest treatment is the dead-man's-switch
    rule that a missing or unreadable signal is a failure, not a pass. The in-house falsification recorded
    by 14a on 2026-08-27 (no 08-26 outputs in `changelog/` or `metrics/`) is consistent with the literature's
    prediction rather than an anomaly.

  Caveats: The corpus is practitioner engineering writing plus one 2026 journal article read at snippet
    level; none of it concerns agent pipelines specifically. Its unanimity is partly a function of the
    literature being normative guidance rather than measurement.

  Recommendation: SUPPORTED (for the distinction — which refutes the item's stated inference)
