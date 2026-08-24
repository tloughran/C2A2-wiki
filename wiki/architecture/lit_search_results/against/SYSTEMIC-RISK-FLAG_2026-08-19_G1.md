SYSTEMIC-RISK-FLAG:
  Date: 2026-08-19
  Filed by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-837, PRESUMPTION-841, ASSUMPTION-1152, ASSUMPTION-1149
  Common vulnerability: **Identity and absence are both inferred from position rather than asserted by content.**

  Statement: Four items in this cohort reduce to one architectural pattern. A file's authorship is inferred from its path (837). A record's non-existence is inferred from its absence in a register that cannot distinguish "checked and empty" from "never checked" (841). A run's own output is inferred from the presence of something at the location it wrote to (1152). And the queue's contents are inferred from what one regex happens to match, so items in an unmatched format are invisible rather than merely unread (1149). In every case the system reads a *location* and concludes something about *provenance* or *coverage*. Nothing anywhere carries a content-level claim about who produced it, when, or over what input set.

  Literature basis:
    - TOCTOU / CWE-367 [established-work]: "A pathname is not a stable reference to a specific file object." Four decades of privilege escalations in sudo, at, crontab, tmpwatch; still live — filelock CVE-2025-68146, advisories GHSA-qmgc-5h2g-mvrw and GHSA-w853-jp5j-5j7f; carried into agents by arXiv:2603.00476.
    - Content-addressable storage [established-work]: an entire storage paradigm exists because location does not identify content.
    - "On Build Hermeticity in Bazel-based Build Systems" (IEEE Software 2025): 0 of 70 projects built on the toolchain designed to remove filesystem-state dependence actually achieve it. [authors not verified]
    - Rubin MCAR/MAR/MNAR [established-work]; informative-MNAR in EHR (J Biomed Inform 2023, S1532046423000278): absence of a measurement encodes a decision and must be explicitly represented.
    - "Systematic review search strategies are poorly described and not reproducible" (medRxiv 2023.05.11.23289873): 95% of reviews do not report a reproducible search — the measured failure rate of leaving coverage to prose.
    - Log-parsing evaluation literature (arXiv:2308.09003 and the large-scale evaluation, ResearchGate 383974909): refined-metric template accuracy averages ~0.2; a regex-defined view of a heterogeneous corpus is not a census.

  Risk level: **Critical**

  Why it is systemic rather than four bugs: The failures share a signature — each produces a *passing* result. A stale artifact read as fresh yields a clean verdict; an unsearched item with no recorded null looks searched; an unmatched queue record looks absent; a path that resolves looks authoritative. No failure-detector in the system is looking for a pass. This means the observed instances (three traps, four hand-written qualifiers, thirteen hidden items) are a sample from an uncounted population, and the sampling mechanism is biased toward zero.

  Recommendation:
    1. Adopt one content-level provenance convention across all four surfaces: every artefact and every register entry carries producer identity, timestamp, and a description of the input set examined. This is a single change that closes all four items.
    2. Require positive evidence for negative results. A "clean" verdict, a null search result, and an empty queue must each be accompanied by evidence the check ran (counts examined, run ID). Silence must never be readable as a result.
    3. Enumerate the attack surface before estimating the risk. Count every point where the system reads a conventionally-named artefact or infers absence from a register. Until that count exists, the three/four/thirteen figures are floors, not measurements.
    4. Note the interaction with ASSUMPTION-1153: tightening detectors to reduce false positives increases exactly this class of failure, which is Type II. The two cohorts pull in opposite directions and no loss function has been stated for either.
