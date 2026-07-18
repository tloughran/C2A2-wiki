SEARCH-FOR-PRESUMPTION-455:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-455
  Original statement: "Per-task independent failure diagnosis (no shared incident state) is an acceptable way to handle infrastructure failures that span agents."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-455
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from cohort listing (2026-07-07 EOD)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Avizienis, 1985. "The N-Version Approach to Fault-Tolerant Software." IEEE Trans. Software Engineering. — Analogous support only: independent, diverse redundant analyses avoid common-mode error; multiple independent diagnoses of the same failure can catch what a single shared diagnosis misses.
    2. Valdes & Skinner, 2001. "Probabilistic Alert Correlation." RAID 2001. — Foundational alert-correlation work; notably, its premise is that independent per-sensor alerts are the natural starting state and correlation is a layer added on top — i.e., independent detection is the accepted substrate, shared state the enhancement.
    3. SRE School, 2026. "What is Alert Deduplication?" sreschool.com. — Documents that real-time deduplication has a latency/completeness trade-off; short-lived independent handling before correlation kicks in is an acknowledged operating mode, not a defect.

  Strength of support: Weak

  Summary: Direct support is thin. The strongest case assemblable from the literature is (a) diversity-redundancy arguments: independent diagnoses avoid anchoring on one incident narrative and can surface aspects a merged record suppresses; and (b) the observation that correlation architectures treat independent per-monitor detection as the baseline layer, with dedup/correlation as an added optimization whose absence degrades efficiency rather than correctness. However, the dominant thrust of incident-management practice (single incident record, alert dedup, Microsoft Defender-style correlation) treats uncoordinated parallel diagnosis of one underlying failure as waste and a source of diagnostic drift, which is the opposite of the presumption. The presumption is defensible as a temporary or low-frequency operating mode, not as steady-state design.

  Caveats: Support weakens as (a) cross-agent infrastructure failures become frequent (repeated duplicated diagnosis cost compounds); (b) diagnoses diverge and produce inconsistent remediation; (c) no post-hoc reconciliation step exists to harvest the diversity benefit — independent diagnosis without later merge gives the cost of N-version without its payoff.

  Search scope confidence: Preliminary; searched incident-management and fault-tolerance framings.

  Recommendation: PARTIALLY-SUPPORTED
