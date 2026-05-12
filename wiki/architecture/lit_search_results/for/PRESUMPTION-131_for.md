SEARCH-FOR-PRESUMPTION-131:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-131
  Original statement: "Sewing agent's 'agent judgment call' to exclude architecture-root tracking files as routing targets defensible without user review — autonomous-agent boundary-setting authority presumed"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-131
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 sewing-agent autonomous exclusion decision without policy review
      15a: Searched for autonomous-agent boundary-setting authority literature
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Russell & Norvig (2020) "AIMA" 4th ed. — bounded autonomy for sub-task scope decisions is canonically endorsed for narrow agents; broader scope decisions require human-in-the-loop.
    2. Amodei et al. (2016) "Concrete Problems in AI Safety" — distributional shift and scalable oversight literature: routine sub-task decisions can be agent-autonomous when reversibility is high.
    3. Software-engineering ".gitignore" / "exclude-from-index" conventions — exclusion of architecture-meta files is canonical practice in code repositories; convention-based exclusions warrant lower review threshold.
    4. C2A2-internal: routing-target exclusion is reversible (single-line config change); blast-radius is low.
    5. ASSUMPTION-110 (this cycle) is the paired stated-claim that depends on this exclusion decision being defensible.

  Strength of support: Moderate

  Summary: Bounded autonomy for narrow, reversible sub-task decisions is supported in AI-safety (Amodei) and AI-architecture (Russell-Norvig) literatures. Exclusion of architecture-meta files from routing targets is convention-aligned with software-engineering ".gitignore" / index-exclusion practice. The "agent judgment call" framing is acceptable for narrow scope provided reversibility is preserved and the exclusion is documented. The C2A2 case meets reversibility and documentation criteria.

  Caveats: (a) Convention-alignment is not a substitute for policy specification — boundary-setting authority should be explicitly bounded; (b) Aggregating multiple agent-judgment-calls creates a policy by accretion rather than by deliberation; (c) PRESUMPTION-130 (this cycle) is the related concern about agent-defined definitions; both touch the same policy-vs-judgment gap.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — bounded autonomy for narrow reversible decisions is canonical; explicit boundary specification is the load-bearing follow-up
