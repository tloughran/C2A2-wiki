SEARCH-AGAINST-PRESUMPTION-270:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-270
  Original statement: [inferred] The swarm-contract mirror pattern (root architecture/ + wiki/architecture/) is a stable ground-truth pattern; drift risk is not separately defended.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-270
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated stability claim.
      15b: Searched for challenging literature on silent-drift failure modes.
    Current status: CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Kleppmann (2017) — Replication / mirror literature is unambiguous: copy-mirror drifts without detection; the design assumption of stability without drift-defense is documented as the failure precondition.
    2. Nygard (2018) — Operational documentation explicitly recommends symlink when both must agree; copy is documented as drift-prone.
    3. Conway (1968) — Dual-write conventions drift in directions of organizational/agent activity; the default is divergence.
    4. Bass et al. (2021) — Single-source-of-truth (SSOT) is documented as preferred; mirror-without-detection is named anti-pattern.
    5. C2A2-internal: assumption does not name a drift-detection mechanism — the precise gap the literature warns about.

  Strength of challenge: Moderate

  Summary: The challenge is direct: every relevant literature source documents that copy-mirror requires drift-detection to be stable. The assumption-of-stability without drift-defense is exactly the failure precondition Kleppmann / Nygard / Conway / Bass all name. Symlink is the canonical remediation when both locations must always agree; it's a near-zero-cost change.

  Specific risks: (a) Silent drift between root and wiki/architecture; (b) downstream agents read inconsistent state; (c) "ground truth" claim becomes false without detection; (d) the drift itself becomes another silent-failure mode (compounds REVISE-059 / REVISE-064).

  Mitigations available: (a) Replace copy-mirror with symlink (near-zero cost, instant remediation); (b) add file-hash equality check to Janitor (1-line check); (c) on drift detection, fail-loud per Rule-12.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-270
    Strongest counterargument: Mirror conventions are unambiguously documented as drift-prone without detection. Symlink is the literature-canonical remediation when both locations must always agree. The absence of drift-defense is precisely the failure precondition. The "stability" presumption is exactly what the literature warns against assuming for copy-mirror.
    What would need to be true for C2A2 to be safe: Either (a) symlink (eliminates drift entirely), or (b) automated drift-detection check (file-hash equality on each Janitor cycle).
    How to test: Run hash-equality check on root + wiki/architecture/swarm-contract.md once per cycle.
