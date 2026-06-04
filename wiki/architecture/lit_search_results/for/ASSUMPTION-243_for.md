SEARCH-FOR-ASSUMPTION-243:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-243
  Original statement: The Sociogram-tab AI search wired in today via shared `wiki/lib/c2a2-search.js` delegation is the per-tab adapter pattern broker-v4 (DECISION-049 candidate) was designed to enable; today's working integration is the first demonstrated instance.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-243
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 demo-path architecture event (Sociogram-tab AI search wiring).
      15a: Searched for supporting literature on per-tab adapter patterns and shared-module + thin-consumer architectures.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Gamma et al. (1994) "Design Patterns" — Adapter pattern is canonical for accommodating heterogeneous consumers behind a uniform interface; thin-consumer + shared-broker is documented as a stable design.
    2. Fowler (2002) "Patterns of Enterprise Application Architecture" — Service Layer + Gateway pattern supports a single broker behind multiple surface adapters; matches the c2a2-search.js delegation shape.
    3. Martin (2017) "Clean Architecture" — Dependency-inversion principle supports per-tab adapters depending on shared abstraction (broker-v4) rather than the reverse.
    4. C2A2-internal: DECISION-049 candidate explicitly anticipated this shape; today's Sociogram wiring is the first instance moving from candidate to demonstrated.
    5. Microservices literature (Newman 2021 "Building Microservices") — broker-with-adapters is documented as scalable across multiple consumer surfaces with low per-surface marginal cost.

  Strength of support: Moderate (architectural pattern is industry-standard; "first demonstrated instance" claim is internally verifiable but not externally citable).

  Summary: The per-tab adapter + shared-broker pattern is a well-established design pattern with strong precedent across Gamma, Fowler, Martin, and microservices practice. Broker-v4's design as a shared module with thin per-tab consumers maps cleanly onto Gateway / Adapter / Service-Layer patterns. The internal claim that today's Sociogram integration is the "first demonstrated instance" of DECISION-049's intent is consistent with the registry's candidate-tracking history.

  Caveats: (a) "First demonstrated instance" is a C2A2-internal historical claim, not validated by external literature; (b) the pattern's success at N=1 demonstrated instance does not prove cross-surface stability — literature notes adapter-overhead grows when per-surface divergence is small; (c) DECISION-049 is still a candidate (not numbered), which is itself the subject of ASSUMPTION-251 / PRESUMPTION-271.

  Recommendation: SUPPORTED (Moderate)
