SEARCH-AGAINST-PRESUMPTION-728:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-728
  Original statement: That repair is metric-neutral; anchoring moved one file out of the tolerance band it is judged against (1.154 -> 1.401) and another 0.94 -> 1.042, with 21 unexplained length deviations standing and no field distinguishing drifted from repaired-into-deviation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-728
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two same-day measurements of the same coupling
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart's Law literature (survey via ModelThinkers, Grokipedia, and "Goodhart's Law in Reinforcement Learning," arXiv 2310.09144). Establishes that a metric is only informative "under the distribution of behaviors observed when the metric was not being optimized" — once an intervention (repair) targets the underlying artifact, the correlation between the metric and the quality it proxies for is no longer guaranteed to hold. This is the general theoretical case against "repair is metric-neutral."
    2. Regressional Goodhart / regression-to-the-mean literature [unverified — from search snippet, general statistics consensus]. Notes that extreme "before" values partly reflect noise; remediation targeted at extreme values will show mean-reversion in the "after" measurement that is statistically indistinguishable from genuine repair, contaminating any metric used to judge repair quality.
    3. Before-after study methodology literature (PMC3753332, STROBE-related; interrupted time series vs. before-after analysis). Documents that before-after designs "ignore underlying secular trends and may overestimate the impact of interventions," and that confounding from concurrent process changes is a known, well-studied threat to validity in exactly this kind of same-day paired measurement.

  Strength of challenge: Strong

  Summary: The theoretical case against "repair is metric-neutral" is well established across both the AI-alignment Goodhart's Law literature and classical before-after study methodology: an intervention that touches the artifact being measured routinely shifts the metric independent of whether it improved the underlying quality, and paired same-day before/after measurements cannot distinguish genuine correction from metric artifact, regression to the mean, or newly-introduced deviation. PRESUMPTION-728's own data (values crossing tolerance bands post-anchoring, 21 unexplained deviations) is consistent with exactly this predicted contamination.

  Specific risks: If repair actions are assumed metric-neutral, drift caused by the repair process itself gets silently absorbed into "unexplained deviations" or attributed to the original defect rather than the fix — masking whether the anchoring/repair pipeline is itself a defect source. Over many repair cycles this could compound, degrading the register's ability to distinguish signal from intervention noise.

  Mitigations available: Yes — standard confound-control techniques apply: (1) add a field tagging each deviation as "pre-existing drift" vs. "introduced by repair," recoverable via diffing pre-repair and post-repair artifact states; (2) use control/held-out files not subject to repair in the same window to separate secular trend from intervention effect; (3) report repair effects with a paired design that includes a no-intervention comparison group, as recommended in before-after study methodology critiques.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-728
  Strongest counterargument: Any process that both (a) modifies an artifact and (b) is judged by a metric computed on that same artifact is structurally vulnerable to Goodhart-style contamination and before-after confounding — this is not domain-specific to C2A2, it is a general property of intervention-and-remeasurement designs, documented across statistics and ML-safety literature. The fact that two files in this batch moved outside their tolerance bands on the same day repair activity occurred is the textbook signature researchers are warned to check for, not a coincidence to wave away.
  What would need to be true for C2A2 to be safe: The repair mechanism would need to operate on a strictly disjoint set of properties from what the tolerance-band metric measures (e.g., repair only touches formatting, metric only measures semantic content) — and this disjointness would need to be verified, not assumed. Absent that, the register needs a mechanism to separate repair-induced from pre-existing deviation.
  How to test: For the two files that crossed tolerance bands, diff the pre-anchoring and post-anchoring artifact states directly. If the repair's edits are causally sufficient to explain the metric shift (e.g., edits touch exactly the measured dimension), that confirms contamination; if the shift persists in content untouched by repair, that points to independent drift instead.

Search scope: preliminary search — a follow-up search specifically into "software repair introduces regressions" / APR (automated program repair) literature is recommended, as it directly studies this failure mode in a closer domain analogue.
