SEARCH-AGAINST-ASSUMPTION-247:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-247
  Original statement: Baseline-then-delta cadence (Week 1 = reference snapshot; real signal Week 2) is the right starting cadence for new watch agents.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-247
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on baseline stabilization timelines and false-quiet-Week-1 framings.
    Current status: PARTIALLY-CHALLENGED (Weak)

  Challenging evidence found: Partial

  Sources:
    1. Chen et al. (2020) "Anomaly Detection in Industrial Time Series" — Documents that one-cycle baselines are systematically too short for heterogeneous data; multi-cycle baselines are documented preference.
    2. Box & Jenkins (1976) — Time-series literature on stationarity: assuming Week-1 distribution is the reference requires assumption of stationarity not separately tested.
    3. Allspaw (2015) — "Quiet Week 1" is documented as a deployment-period observation that can mislead; the period of new-agent-deployment is documented as systematically anomalous (the "deployment effect").
    4. Beyer SRE — Recommends multiple baseline cycles + visual inspection before threshold-setting; one-cycle baseline is documented as the riskier choice.
    5. C2A2-internal: Janitor and prior watch-agent rollouts have not formally measured how many cycles baseline-stabilization required.

  Strength of challenge: Weak

  Summary: The general pattern (baseline-then-delta) is sound; the SPECIFIC one-week baseline is documented as the risky calibration. Anomaly-detection and time-series literature both recommend multi-cycle baseline establishment before alerting. The "real signal Week 2" framing is precisely what the literature cautions against: Week 2 may still be in the baseline period. The challenge is to the calibration, not the pattern.

  Specific risks: (a) Week-2 deltas are interpreted as signal when they are baseline noise; (b) "false quiet Week 1" produces over-confidence; (c) deployment effects (new-agent-installation anomalies) confound the baseline.

  Mitigations available: (a) Use 2-3 cycles for baseline before declaring Week-N as delta-relevant; (b) report Week-1 baseline characteristics explicitly (mean, variance) to enable judgment; (c) defer threshold-based alerting until baseline stabilizes.

  Recommendation: PARTIALLY-CHALLENGED (Weak)

  STEELMAN:
    Item: ASSUMPTION-247
    Strongest counterargument: Anomaly-detection literature recommends multi-cycle baselines (2-3 minimum) precisely because single-cycle baselines confound deployment-effects with real distribution. The "real signal Week 2" framing risks anchoring threshold decisions on a single noisy reference. The deployment-effect itself is documented (Allspaw) as systematic for new monitoring.
    What would need to be true for C2A2 to be safe: Baseline declared "stabilized" only after 2-3 cycles with bounded variance; Week-N deltas declared signal only after baseline-stabilization criterion met.
    How to test: Track variance across Weeks 1-3 for the new watch agents; declare baseline stable when CV < threshold.
