SEARCH-FOR-PRESUMPTION-890:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-890
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High) [FIX FIRST candidate]
  Original statement: [inferred] That job liveness is an adequate proxy for artifact production, and that a
    monitor which has declared its own read failure may still report green.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-890
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a green report read against the directory listings it describes; the missing
        2026-08-26 run is the demonstrated instance.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND (the literature states the contrary rule explicitly)

  Search scope: WebSearch, 2026-08-28, two dedicated queries — liveness vs black-box/end-to-end monitoring,
    and dead-man's-switch detection of absent output. Same corpus as ASSUMPTION-1230_for.md; the two items
    are the stated and unstated forms of one claim and were searched together, which is recorded here rather
    than presented as independent corroboration. NOT COVERED: Google SRE (Beyer et al.) in primary form; the
    runtime-verification literature on safety vs liveness properties. All sources SNIPPET-ONLY.
    Search confidence: HIGH.

  Supporting evidence found: No

  Sources:
    1. Dylan Dumont, "Health Checks That Actually Work: Liveness vs Readiness vs Startup Probes"
       [SNIPPET-ONLY] https://dev.to/dylan_dumont_266378d98367/health-checks-that-actually-work-liveness-vs-readiness-vs-startup-probes-545e —
       A liveness check answers only whether the process is alive and able to serve, and should not check
       dependencies or business logic. Liveness is defined so as to exclude what the presumption reads it
       as proving.
    2. Crontap, "Dead man's switch, explained for developers"; Kriss-V, `deadmancheck`; Datashelter,
       "Backup Monitoring: Solving the Dead Man's Switch Problem" [all SNIPPET-ONLY] —
       Three independent statements of the rule the presumption violates: for unattended scheduled work the
       most dangerous failure produces no output at all; the first sign of failure is silence; therefore
       absence of the expected signal must itself be treated as failure, and the ping should assert on the
       produced artifact rather than on completion. `deadmancheck`'s tagline — "alerts when jobs run but do
       nothing" — is the exact failure class of the missing 2026-08-26 outputs.
    3. Web-alert, "Black-Box vs White-Box Monitoring" [SNIPPET-ONLY]
       https://web-alert.io/blog/black-box-vs-white-box-monitoring-difference —
       "Each is blind exactly where the other sees clearly" — a single scheduler-reading instrument cannot
       cover the artifact question, by construction.
    4. Anon. (2026), "Vitality assurance in microservice architectures," Frontiers in Computer Science,
       doi:10.3389/fcomp.2026.1811944 [SNIPPET-ONLY; authors unverified] — Separates service-local health
       checks from synthetic end-to-end transactions as distinct instruments.

  Strength of support: None for the presumption; Strong for its negation

  Summary: Nothing supports treating liveness as a proxy for output, and the practice literature states the
    contrary rule in terms close enough to be quotable: silence is the characteristic failure of unattended
    scheduled work, so the absence of an artifact must be a first-class alarm rather than the default
    condition of the system. The second limb — a monitor reporting green while declaring its own read
    failure — found no defence anywhere; the closest treatment is the dead-man's rule that an unreadable or
    missing signal counts as failure, which makes a self-declared-blind instrument's green verdict a
    category error rather than an optimistic one. The estate has the demonstrated instance already: the
    2026-08-26 pipeline produced no `changelog/` or `metrics/` outputs and was not flagged.

  Caveats: Practitioner corpus, snippet-level, normative rather than measured; no study quantifies how often
    liveness-only monitoring misses production failures. Shares its evidence base with ASSUMPTION-1230.

  Recommendation: NO-SUPPORT-FOUND
