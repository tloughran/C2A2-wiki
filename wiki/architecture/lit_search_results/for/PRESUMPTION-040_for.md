SEARCH-FOR-PRESUMPTION-040:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-040
  Original statement: "Structural verification of a .plugin archive is an adequate proxy for end-to-end operational readiness"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-040
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — structural-only verification treated as sufficient
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Software testing literature (Myers, Sandler, Badgett 2011, "The Art of Software Testing"): structural/static verification and integration/behavioral testing address non-overlapping failure classes; structural is necessary but not sufficient.
    2. Plugin/extension test-strategy literature (VS Code, JetBrains, Sketch extension docs): end-to-end smoke test (install → trigger → observe output) is considered the minimum definition-of-done for plugin releases.
    3. Definition-of-done / continuous delivery literature (Humble & Farley 2010 "Continuous Delivery"): release readiness requires behavioral validation in a production-like environment.

  Strength of support: None

  Summary: The testing and release-engineering literature is consistent that structural verification is a necessary but not sufficient condition for release readiness. Plugin and extension publishing specifically call for an end-to-end smoke test ("install → trigger → fires correctly") as the minimum bar. No literature supports structural verification alone as an adequate proxy for operational readiness.

  Caveats: Structural verification is valuable as an early gate; the issue is treating it as the sole gate. The absence of literature support is clear.

  Recommendation: NO-SUPPORT-FOUND
