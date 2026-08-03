SEARCH-FOR-PRESUMPTION-645:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-645
  Original statement: That an audit trail can be trusted to be complete in the successful
    direction — that a completed step implies a logged step.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-645
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a disclosed seven-week log gap and generalised to the registers
           that depend on log completeness (origin ASSUMPTION-670)
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. OWASP Top 10:2025 A09, Security Logging and Alerting Failures — auditable events
       are routinely "not logged or logged inconsistently"; the named canonical example
       is a system that records the success-path metric and drops the other side.
       Asymmetric logging is the default defect, not an edge case.
    2. "Application Logs Are Not Audit Logs" (dev.to/robertatkinson3570) — for audit
       purposes a single dropped event is a completeness failure; log forwarding to
       central stores drops silently under load.
    3. Time, Causality, and Observability Failures in Distributed AI Inference Systems,
       2026. arXiv:2604.21361 — silent failure produces no signal detectable by automated
       monitoring; agents keep returning plausible output while the record diverges.

  Strength of support: None

  Summary: No literature was found supporting the trustworthiness of append-last logging
  in the successful direction. The observability and security-logging literature treats
  log completeness as a property that must be independently verified and is routinely
  violated, with silent drops the expected failure mode under fail-fast shell semantics
  and under load. The asymmetry 14b identifies — that success-path gaps are harder to
  notice than failure-path gaps — is itself a documented pattern rather than a novel
  observation, which is bad news for the presumption: it means the failure is well
  characterised and C2A2 has no mitigation in place.

  Caveats: The security-logging literature is oriented to adversarial and
  high-throughput settings; a single-user vault writing a handful of lines per day faces
  far lower drop pressure, so base rates do not transfer. But the disclosed seven-week
  gap is direct in-house evidence that the failure has already occurred here at least
  once, which makes the base-rate objection moot. Every "Nth consecutive day" and
  autonomy-streak figure in the registers inherits this exposure.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Observability, audit-log completeness, silent failure,
  OWASP logging failures.
