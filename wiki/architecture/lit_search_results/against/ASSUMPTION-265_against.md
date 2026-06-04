SEARCH-AGAINST-ASSUMPTION-265:
  Date searched: 2026-06-02
  Original item: ASSUMPTION-265
  Original statement: The daily-run git phase must verify version-control health each run rather than infer it from no-error — a stale `.git/index.lock` from a crashed process can silently block all staging with no surfaced error (here: 2026-05-29 → 2026-06-02).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-265
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from a realized 4-day silent git-staging outage.
      15b: Searched for when pre-flight checks are over-engineering and when no-error is a sufficient success signal.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. YAGNI / KISS (PRESUMPTION-288 FOR lineage). — Adding a verification step to every git op in a low-frequency personal pipeline can be disproportionate; for most runs `git` exit codes ARE a reliable success signal.
    2. Exit-code reliability in the common case (Unix tooling convention). — git generally fails loudly (non-zero exit) on most errors; the stale-lock silent case is a specific edge, not the norm, so "verify every run" may over-correct from one incident.
    3. Cost-of-instrumentation / alert-fatigue (PagerDuty/Splunk lineage). — A health check that fires on benign states adds noise; the check must be precise or it trades one failure mode for another.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is real but weak. git exit codes are a reliable success signal in the common case, and per-run verification could be over-engineering for a low-frequency personal pipeline — IF the incident were a one-off. It was not: a stale `index.lock` silently disabled staging for ~4 days with a clean-looking tree, which is exactly the class of silent failure exit codes do not catch. The over-engineering objection is outweighed by a realized, multi-day, silent, high-consequence failure on the version-control spine.

  Specific risks: Skipping verification leaves the system blind to any future silent VC failure (lock, partial write, detached HEAD) for days; over-instrumenting adds noise. The targeted check (detect stale lock / confirm staging took effect) is cheap and precise enough to avoid the noise objection.

  Mitigations available: Scope the check narrowly — detect a stale `index.lock` and confirm the post-stage index reflects intended changes (read-after-write) — rather than a broad, noisy VC audit.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-265
    Strongest counterargument: For a low-frequency personal pipeline, git exit codes are a sound success signal and per-run VC verification is YAGNI; building checks off a single 4-day incident risks over-correcting and adding noise that causes its own failures (alert fatigue, false positives on benign states).
    What would need to be true for C2A2 to be safe: Either silent VC failures are genuinely rare AND independently caught soon after, OR the verification is narrow and precise (stale-lock detection + read-after-write confirm) so it adds negligible noise.
    How to test: Audit historical runs for other silent VC failures; if the stale-lock event is the only one in a long window, a narrow targeted check (not a broad audit) is the proportionate response.
