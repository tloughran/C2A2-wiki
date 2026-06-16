SEARCH-FOR-PRESUMPTION-336:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-336
  Original statement: Captured file-write telemetry is representative of agent activity; cluster emptiness is a data fact rather than a possible capture artifact.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-336
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced unstated presumption by inference from telemetry-cluster interpretation (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Gupta, S. et al., 2019. "Trustworthy Experimentation Under Telemetry Loss." arXiv:1903.12470 (Microsoft, CIKM). — Establishes that telemetry-based measurement can be made valid, but only after explicitly quantifying and correcting for loss/coverage gaps — conditional support for relying on captured telemetry.
    2. Hoffmann, M. & co-authors (NBER w32401, 2024). "The Streetlight Effect in Data-Driven Exploration." — Formalizes how analysis concentrated on well-instrumented regions yields systematically biased conclusions; defines the validity conditions the presumption would need to meet.
    3. "Evidence of absence," standard treatment (e.g., Sober, E.; summarized Wikipedia entry with detection-power framing). — Absence of observations is evidence of absence only in proportion to detection power: a calibrated instrument with known coverage licenses the "data fact" reading.
  Strength of support: Weak
  Summary: Direct support for the presumption as stated is thin. The strongest favorable reading from the literature: log/telemetry-based measurement is a mainstream, accepted observational method, and absence-of-evidence inferences are legitimate when detection power is high — so if file-write capture is known to cover all agent output channels, cluster emptiness genuinely is a data fact. The Microsoft telemetry-loss work shows such validity is achievable in practice and gives the method (quantify capture rate, correct or bound the bias). However, every supporting source makes the inference conditional on demonstrated instrumentation coverage, which is precisely what is presumed rather than checked here. No source supports treating representativeness as a default.
  Caveats: Support is conditional: it transfers only after a coverage audit (do all agent sessions/write paths emit telemetry? are there silent capture failures?). The streetlight-effect literature warns that empty clusters are the canonical place where capture artifacts masquerade as facts. A cheap discriminating test (inject known activity into the empty cluster's channel and confirm capture) would convert this presumption into a checked fact.
  Search scope: 2 WebSearch passes within one query session ("log telemetry instrumentation coverage bias measurement validity absence of evidence streetlight effect behavioral analytics" + streetlight-effect refinement).
  Recommendation: PARTIALLY-SUPPORTED
