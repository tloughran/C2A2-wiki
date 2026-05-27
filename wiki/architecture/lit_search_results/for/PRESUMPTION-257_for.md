SEARCH-FOR-PRESUMPTION-257:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-257
  Original statement: The 2026-05-25 Rule-12 gap surfaced today (registries advanced ASSUMPTIONs 225-229 / PRESUMPTIONs 248-253 but no 2026-05-25_changes.md or 2026-05-25_snapshot.md was written) is direct evidence the 14a/14b artifact-write step can fail silently while the registries-advance step succeeds — a Rule-12 fail-loud violation embedded in the pipeline that exists to detect Rule-12 violations.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-257
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — self-referential pipeline-integrity failure.
      15a: Searched for supporting literature on write-vs-commit atomicity and audit-trail invariants.
    Current status: SUPPORTED (Strong)

  Sources:
    1. Gray & Reuter (1992) "Transaction Processing" — ACID atomicity is canonical: partial-success states (one write succeeds, paired write does not) are recognized as the central failure mode requiring 2PC or compensation.
    2. Nygard (2007) "Release It!" — "silent partial failure" is identified as one of the most dangerous distributed-system failure patterns.
    3. ISO 27001 / SOC2 audit-trail requirements — atomicity of audit-write + state-change is foundational; failing to write the audit while changing state is a recognized non-conformance.
    4. C2A2-internal: PRESUMPTION-241/247 (introspection-illusion family) and the broader Rule-12 fail-loud principle align — this is consistent with established C2A2 self-flags.

  Strength of support: Strong

  Summary: The presumption identifies a textbook silent-partial-failure pattern. Transaction-processing literature, distributed-systems anti-patterns, and audit-trail standards converge: write-paired operations must be atomic, and partial-success states are the dangerous case. The Rule-12 fail-loud principle is the project's own version of this norm. Self-referential nature (pipeline-that-detects-violations-violates-them) is itself a documented meta-monitoring failure mode.

  Caveats: (a) Support is for the *vulnerability claim*; the specific incident may have a benign explanation (e.g., manual workflow gap rather than automation bug) — diagnosis is still owed; (b) "embedded in the pipeline" presumes the same automated step writes both, which should be verified.

  Recommendation: SUPPORTED (Strong; vulnerability claim is well-supported)
