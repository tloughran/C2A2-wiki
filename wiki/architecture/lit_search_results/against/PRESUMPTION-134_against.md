SEARCH-AGAINST-PRESUMPTION-134:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-134
  Original statement: "PRESUMPTION-121 + PRESUMPTION-125 alternation presumes independent failure surfaces — but both rely on shared infrastructure substrate (Chrome MCP + claude.ai login state)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-134
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD substrate-decomposition concern
      15b: Searched for counter-evidence on cluster-identifier independence at infrastructure layer
    Current status: CHALLENGED (Strong)

  Sources:
    1. Vesely (1981) "Fault Tree Handbook" — common-cause failure analysis is foundational reliability engineering; treating shared-substrate failures as independent is unambiguously incorrect.
    2. Allspaw / Cook "How Complex Systems Fail" (2000) — naming-the-cluster substitutes for understanding-the-cluster; substrate-decomposition is canonical first step.
    3. Toyota Production System (Ohno 1988) Five Whys — terminating root-cause analysis at symptom-cluster (rather than substrate) is canonical anti-pattern.
    4. NIST SP 800-160 Vol. 1 (2018) "Systems Security Engineering" — shared-substrate failure mode analysis is required for cyber-physical-system reliability.
    5. C2A2-internal: ASSUMPTION-108 + ASSUMPTION-109 (this cycle) both depend on independence assumption that PRESUMPTION-134 challenges.

  Strength of challenge: Strong

  Summary: The challenge is strong. The independent-failure-surface assumption is contradicted across reliability-engineering (Vesely), complex-systems (Allspaw-Cook), root-cause-analysis (Toyota Five Whys), and systems-security (NIST SP 800-160) literatures. The PRESUMPTION-134 surfacing identifies an architectural gap that directly undermines ASSUMPTION-108 and ASSUMPTION-109's basis for treating the two failure modes as warranting separate DECISIONs. Substrate-decomposition is the canonical prerequisite and has not been performed.

  Specific risks: (a) Standalone DECISIONs canonized on cluster-identifier rather than substrate; (b) common-cause failure invisible to the mitigation design; (c) ADR sprawl from cluster-identifier proliferation; (d) week-carrying-capacity (PRESUMPTION-136) inflated by treating one substrate-failure as two.

  Mitigations available: (a) Substrate-decomposition before any standalone-DECISION canonization; (b) shared-substrate identification (Chrome MCP, claude.ai login state) explicit in DECISION text; (c) common-cause failure mode included in mitigation design; (d) combined-DECISION if substrate is shared.

  Recommendation: CHALLENGED (Strong)

  STEELMAN:
    Item: PRESUMPTION-134
    Strongest counterargument: Treating two failure clusters with observable shared substrate as having independent failure surfaces is unambiguously contradicted by canonical reliability engineering (Vesely fault-tree), complex-systems analysis (Allspaw-Cook), and root-cause analysis (Toyota Five Whys). The PRESUMPTION-121 (Chrome MCP diagnostic) and PRESUMPTION-125 (cowork-to-chat sync) clusters both involve Chrome MCP + claude.ai login state — observable shared substrate. The alternation between cluster identifiers in successive cycles is the textbook signature of common-cause failure being mis-classified as two independent surfaces. ASSUMPTION-108 and ASSUMPTION-109 inherit this misclassification; both are at risk of canonizing on cluster-name rather than substrate.
    What would need to be true for C2A2 to be safe: (a) Substrate-decomposition performed; (b) shared infrastructure explicitly named; (c) combined-DECISION considered.
    How to test: Audit shared-infrastructure between PRESUMPTION-121 and PRESUMPTION-125 incidents; check whether subsequent recurrence in either cluster reveals shared-substrate root cause.
