SEARCH-AGAINST-PRESUMPTION-1083:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1083
  Original statement: [inferred] Repetition is read as confirmation… Unchanged output is taken to
    mean an unchanged world, not a stale instrument. Which counters would change if their inputs
    froze? (Tested formulation: monitoring instruments that report unchanged values cannot, from
    their output alone, distinguish a stable system from frozen inputs.)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1083
    Item type: PRESUMPTION (unstated, surfaced by inference)
    Transform at each step:
      14b: Inferred from repeated identical scheduler figures, carried-forward nightly numbers, and stale_days 14 without WARN.
      15b: Searched for challenging literature (lane: stale-data detection; heartbeat/freshness; normalization of deviance)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Sharma, A.B., Golubchik, L., & Govindan, R. (2010). "Sensor faults: Detection methods and
       prevalence in real-world datasets." ACM Transactions on Sensor Networks 6(3). [Fetched: full
       text PDF from qed.usc.edu, partial read.] It defines CONSTANT faults ("reports a constant
       value for a large number of successive samples… uncorrelated to the underlying physical
       phenomena"). A seasonal time-series model working on the output series alone "can detect the
       onset of long duration NOISE and/or CONSTANT faults accurately; even in situations where all
       the sensor nodes suffer from faults simultaneously". Frozen output is detectable from the
       output when the true signal has expected variability. This directly contradicts "cannot,
       from output alone".
    2. Stuck-at / flat-line detection practice (arXiv:2409.17841 on spacecraft attitude sensors and
       others; seen in search results, not fetched). Rolling variance and derivative-to-zero tests
       flag frozen channels from the signal alone.
    3. Beyer, B. et al. (2016). Site Reliability Engineering, "Introduction". [Fetched.] It supports
       the underlying concern: "no one reads logs unless something else prompts them", and
       monitoring should not require humans to interpret it.
    4. Vaughan, D. (1996). The Challenger Launch Decision. [Seen via search-result summaries only.]
       Repeated anomalies without disaster were reclassified as normal. This CORROBORATES the social
       half of the presumption (repetition read as confirmation). It does not challenge it.

  Strength of challenge: Moderate

  Summary: As a strong epistemic claim ("cannot, from output alone"), the presumption is
  contradicted by the sensor-fault literature. When the true quantity is expected to vary (noise,
  seasonality, daily activity), exact repetition is itself the signature of a frozen input, and
  output-only tests detect it well. The claim holds only in a boundary case: the true quantity
  can legitimately stay flat, and the output has no timestamp, sequence number or noise component.
  Several estate counters look like the detectable case (an identical 87/3/5 split across days in
  an active scheduler is itself anomalous). If so, the problem is not that the instruments cannot
  tell; it is that nobody applies the test. The normalization-of-deviance literature supports that
  social diagnosis.

  Specific risks: Framing the problem as "instruments cannot tell" invites adding more instruments.
  The cheaper fix, a repetition or zero-variance check on existing outputs, gets skipped. Counters
  whose true values can legitimately be flat (for example, error counts at zero) remain truly
  ambiguous and need freshness metadata.

  Mitigations available: Add an "identical to previous N runs" flag to each reported metric. Emit
  input timestamps and row counts (freshness heartbeats) alongside every derived figure. For
  flat-by-design counters, add a canary input that should always change the output.

  Search scope: Preliminary: 4 searches plus 2 fetches.

  Excluded results: GitHub AseemPrasad/Air-Quality-Intelligence issue #44 (GitHub; its title echoes
  "stuck-value flatline"); Medium "Sensor faults" post; MATLAB Answers thread; data-freshness vendor
  pages (IBM Think, tacnode, anomalyarmor, datatrail, pipecode.ai, risingwave, Databricks blog,
  dev.to); psychsafety.com, Utah Avalanche Center and Wikibooks pages on normalization of deviance.
  Excluded as GitHub, vendor or secondary.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1083
  Strongest counterargument: Output-only detection of frozen inputs is a solved problem in
    sensor-network engineering whenever the true signal is expected to vary. Exact repetition is
    the fault signature. The estate's repeated figures are therefore not uninformative. They are
    positive evidence of staleness that went unread. Treating the instruments as incapable blames
    the instruments for what is a failure to apply a trivial test, and it points remediation at
    the wrong layer.
  What would need to be true for C2A2 to be safe (for the presumption to hold): The counters in
    question can legitimately be constant, and carry no timestamps or noise. Only then is external
    freshness metadata the only remedy.
  How to test: For each flagged counter, estimate its expected day-to-day variance from periods
    known to be live. Compute the probability of N identical readings under that variance. Where
    it is tiny, the output alone already distinguishes frozen from stable.
