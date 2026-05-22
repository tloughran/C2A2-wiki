SEARCH-AGAINST-PRESUMPTION-179:
  Date searched: 2026-05-15
  Original item: PRESUMPTION-179
  Original statement: "Reference-instance retention (Carpathi Wiki stays live) presumes dual-maintenance burden is sustainable; reference-instance bit-rot risk in FLOSS frameworks unaudited"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-179
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as inference
      15b: Searched for counter-evidence on reference-instance bit-rot trajectories
    Current status: NO-CHALLENGE-FOUND (Weak)

  Sources:
    1. Counter-pattern: when reference instance is the maintainer's operational instance (e.g., Django was originally Lawrence Journal-World's CMS), bit-rot is less because attention is already there.
    2. Counter-pattern: well-tooled FLOSS frameworks (Rails Showcase 2010+) maintain reference instances with automated tests; bit-rot is preventable.
    3. The literature supports the presumption in general; mitigations are documented.

  Strength of challenge: Weak

  Summary: The literature largely supports the presumption. Counter-patterns suggest mitigation is possible (operational-instance overlap, automated testing). Weak challenge: the inference stands; mitigation tooling is the load-bearing concern.

  Specific risks: (a) Reference-instance bit-rot; (b) Framework moves on, Carpathi falls behind; (c) Cluster: PRESUMPTION-173 cognitive-bandwidth.

  Mitigations available: (a) Automated tests of framework against Carpathi instance; (b) Periodic re-instantiation; (c) CI/CD pipeline that exercises both.

  Recommendation: NO-CHALLENGE-FOUND (Weak) — inference well-grounded; mitigation tooling is load-bearing

  STEELMAN:
    Item: PRESUMPTION-179
    Strongest counterargument: Carpathi is Tom's operational instance, so the dual-maintenance has natural attention. Counter: even with attention, framework-vs-reference divergence requires explicit tooling (automated tests, CI). The presumption is correct that the audit is missing.
    What would need to be true for C2A2 to be safe: (a) Automated tests; (b) CI/CD pipeline; (c) Periodic re-instantiation.
    How to test: Build automated test suite against Carpathi instance; measure framework-reference divergence over time.
