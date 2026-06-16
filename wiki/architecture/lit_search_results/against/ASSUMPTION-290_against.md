SEARCH-AGAINST-ASSUMPTION-290:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-290
  Original statement: The capture gap should be solved with an external symlink session-bridge, not an OpenStory fork, to stay on upstream.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-290
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated design assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. Spolsky, J., 2002. "The Law of Leaky Abstractions." joelonsoftware.com. — An adapter that papers over a gap inherits the leakiness of what it wraps; symlink bridges depend on filesystem layout, an interface with no contract at all.
    2. Winters/Manshreck/Wright, 2020. "Software Engineering at Google" (Hyrum's Law). — A bridge that depends on OpenStory's unstated on-disk session layout is a de facto fork of the *interface*: it breaks on upstream changes exactly like a fork, but without the fork's ability to control or even detect the change.
    3. Glazkov, D., 2023. "Stages of project forking." glazkov.com. — Notes that the shim/"soft fork" stage is rarely a stable resting place: accommodation of both your needs and upstream's thinking accumulates until a decision (real fork or upstreaming) is forced; the adapter is often a deferral, not a solution.
    4. Nick Desaulniers, 2023. "Forking is not free; the hidden costs." — Supports the claim's anti-fork direction (rebase cost proportional to divergence), but identifies the actually-recommended third option the assumption skips: upstream the change (a capture-path PR to OpenStory), which dominates both fork and shim.
  Strength of challenge: Weak
  Summary: The mainstream literature largely *supports* avoiding forks (fork drift, rebase debt), so the core direction of the assumption is well grounded. The genuine challenge is narrower: (a) a symlink bridge couples to an even less stable interface (undocumented file layout) than a fork would, and breaks silently rather than at merge time — fork breakage is at least loud and localized to pulls; (b) the framing is a false binary — the option the forking literature actually recommends (contribute the capture fix upstream) is absent; (c) "soft fork harmony" via external adapters is documented as an unstable equilibrium when upstream moves quickly.
  Specific risks: Upstream changes session file layout or naming and the bridge silently stops capturing — recreating the very capture gap it was built to close, but now invisibly; debugging cost lands at data-analysis time, far from the cause.
  Mitigations available: Add a canary check (expected session count vs bridged count) that alerts on silent bridge failure; propose the capture path upstream as a PR; document the bridged layout assumption so an upstream pull triggers re-verification.
  STEELMAN:
    Strongest counterargument: For a single-user local deployment, the bridge is ~zero-divergence and trivially disposable; a fork of an actively developed project is a permanent tax. Filesystem layouts of session stores change rarely, and the bridge can be re-pointed in minutes, whereas un-forking takes weeks. Reversibility strongly favors the bridge.
    What would need to be true for C2A2 to be safe: Bridge failure is detectable (loud, not silent); upstream session layout is stable across the versions actually pulled; an upstreaming path remains open if the bridge churns.
    How to test: After each upstream OpenStory pull, diff bridged-session count against directly-enumerated session count; any shortfall = bridge rot.
  Search scope: 1 search — "when to fork instead of adapter shim upstream divergence maintenance hidden costs". Plus established literature (Hyrum's Law, leaky abstractions).
  Recommendation: PARTIALLY-CHALLENGED
