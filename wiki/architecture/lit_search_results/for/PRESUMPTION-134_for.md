SEARCH-FOR-PRESUMPTION-134:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-134
  Original statement: "PRESUMPTION-121 + PRESUMPTION-125 alternation presumes independent failure surfaces — but both rely on shared infrastructure substrate (Chrome MCP + claude.ai login state)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-134
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD substrate-decomposition observation across two alternating cluster identifiers
      15a: Searched for cluster-naming-vs-substrate-decomposition literature in root-cause-analysis
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. (None found supporting independent-failure-surface assumption when shared substrate is observable.)
    2. Allspaw / Cook "How Complex Systems Fail" (2000) — failures sharing substrate are NOT independent regardless of cluster identifier; the substrate-decomposition rule is canonical.
    3. Five Whys / Toyota root-cause-analysis literature — terminating root-cause analysis at symptom-cluster (not substrate) is canonical anti-pattern.
    4. Reliability engineering (Vesely 1981 "Fault Tree Handbook") — common-cause failure analysis is foundational; treating common-cause failures as independent inflates apparent reliability and corrupts mitigation design.
    5. C2A2-internal: PRESUMPTION-121 (Chrome MCP diagnostic) and PRESUMPTION-125 (cowork-to-chat sync) share Chrome MCP + claude.ai login state — observable shared substrate.

  Strength of support: None

  Summary: No literature supports treating two clusters that share an observable infrastructure substrate as having independent failure surfaces. The substrate-decomposition rule (Allspaw-Cook, Five Whys, common-cause-failure analysis in reliability engineering) is canonical and unambiguous. The presumption inverts the canonical rule and is therefore an documented anti-pattern. This is high-severity because it undermines the architectural basis for treating ASSUMPTION-108 / ASSUMPTION-109 as separate DECISIONs.

  Caveats: If the Chrome-MCP-substrate and the claude.ai-login-state are themselves orthogonal failure dimensions, then PRESUMPTION-121 and PRESUMPTION-125 could share infrastructure but differ on which dimension fails — requiring per-cluster mode-of-failure analysis before splitting/lumping decision.

  Recommendation: NO-SUPPORT-FOUND — independent-failure-surface assumption is contradicted by common-cause-failure analysis literature; substrate-decomposition is the required prerequisite for split-vs-lump decision
