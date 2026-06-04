SEARCH-FOR-ASSUMPTION-247:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-247
  Original statement: Baseline-then-delta cadence (Week 1 = reference snapshot; real signal Week 2) is the right starting cadence for new watch agents.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-247
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 watch-agent rollout planning.
      15a: Searched for supporting literature on baseline-stabilization in monitoring rollouts.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Beyer et al. (2016) "SRE" — Baseline-establishment before alerting is canonical SRE practice; Week-1-as-baseline is documented as standard for new monitoring instrumentation.
    2. Burns et al. (2019) "Kubernetes Up & Running" — Observability rollouts standardly establish baseline period before threshold-based alerting; matches the watch-agent pattern.
    3. NIST SP 800-92 "Guide to Computer Security Log Management" — Baseline-then-delta is the documented pattern for anomaly detection rollouts.
    4. Chen et al. (2020) "Anomaly Detection in Industrial Time Series" — Establishing reference distribution before declaring deltas significant is methodologically standard.
    5. C2A2-internal: prior watch-agent rollouts have used similar baseline-first cadence without recorded issue.

  Strength of support: Moderate

  Summary: Baseline-then-delta is canonical practice across SRE, observability, anomaly-detection, and time-series-monitoring literature. The specific Week-1/Week-2 cadence is defensible for weekly-cycle agents. Literature supports the general shape; the specific choice of one-week baseline is a calibration parameter that should be revisited if baseline does not stabilize.

  Caveats: (a) Literature notes baseline may take multiple cycles to stabilize for highly heterogeneous data; (b) one-week baseline assumes weekly cycle captures meaningful variance — not separately validated for these agents; (c) "false-quiet-Week-1" framing risk noted in 15b target.

  Recommendation: SUPPORTED (Moderate)
