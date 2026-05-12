SEARCH-AGAINST-PRESUMPTION-040:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-040
  Original statement: "Structural verification of a .plugin archive is an adequate proxy for end-to-end operational readiness"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-040
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — structural-only verification treated as sufficient
      15b: Searched for challenging literature
    Current status: STRONGLY CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Myers, Sandler & Badgett (2011) "The Art of Software Testing": structural (syntactic / static) testing and behavioral (integration / smoke) testing address non-overlapping failure classes. Each is necessary; neither is sufficient alone.
    2. Humble & Farley (2010) "Continuous Delivery": definition-of-done for release requires validation in a production-like environment.
    3. Plugin/extension publishing practice (VS Code, JetBrains, Sketch docs): smoke test (install → trigger → observe) is the minimum bar.
    4. "Installed but never fires" failure-mode literature in IDE extensions (Eclipse community reports; IntelliJ plugin issue trackers): this is a recurring, well-documented failure class that structural verification cannot catch.

  Strength of challenge: Strong

  Summary: The literature's position is explicit: structural verification is necessary but not sufficient. Integration / behavioral / smoke testing is the documented minimum for operational readiness. The "installed but never fires" failure mode is one of the most common failure classes in plugin systems — and it is invisible to structural verification by definition. Treating structural verification as adequate ignores a known, named failure class.

  Specific risks: The plugin passes structural verification, installs correctly, and fails to fire at the intended trigger moments — a silent, self-invisible failure; discovery requires the next actual resume attempt, which may be the Saturday weekend test.

  Mitigations available:
    - End-to-end smoke test: install in a fresh environment; send a trigger phrase; observe activation
    - Automated plugin smoke-test as part of pre-release gate
    - Observable per-activation log so non-activation is visible, not silent

  Recommendation: STRONGLY CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-040
    Strongest counterargument: The single most common plugin failure mode — "installed but never fires" — is invisible to structural verification. The literature and community practice both identify end-to-end smoke test as the minimum bar. Treating structural verification as adequate is a known category error: it's testing the artifact, not the behavior.
    What would need to be true for C2A2 to be safe: A smoke test is executed on a fresh install before reliance; activation is observable; an observable signal exists for failed activation.
    How to test: Install in a fresh environment; issue each trigger phrase; observe whether the resume-session flow activates; check logs.
