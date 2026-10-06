SEARCH-AGAINST-ASSUMPTION-1598:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1598
  Original statement: "A measure returning a *uniform* verdict across a whole population is
    usually broken rather than revealing, and a lone anomaly in an otherwise clean sweep deserves
    one direct read before write-up."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1598
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a generalised rule an agent derived from three of its own false positives.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Frontiers in Digital Health (2022), "Computational approaches to alleviate alarm fatigue
       in intensive care medicine" and PMC3752621, empiric alarm PPV study — note that 72-99%
       of monitoring alarms are false/non-actionable BUT the true-positive fraction is still a
       genuine, uniform-looking signal when a population shares a real underlying condition
       (e.g., an entire cohort with the same comorbidity triggers the same alarm for a true
       reason). This challenges limb 1: uniformity is consistent with, and expected from, a
       real population-wide effect, not only with a broken measure. The claim's "usually" is an
       unsupported frequency claim the sources do not establish either way.
    2. Sensor-fault literature (arXiv 1507.04540, "Learning to classify with possible sensor
       failures"; PMC11990947, variational-autoencoder sensor-failure detection) treats
       "uniform/degenerate output" as one hypothesis to be tested against genuine systematic
       effect, using independent instrumentation — it does not treat uniformity as
       presumptively diagnostic of failure. This is a domain precedent against defaulting to
       "broken" on uniformity alone.
    3. arXiv 2408.13667, "Outlier Detection Bias Busted: Understanding Sources of Algorithmic
       Bias through Data-centric Factors," and the cherry-picking/confirmation-bias literature
       (Gains.af summary; arXiv 1804.02969 on cognitive bias in rule-based ML interpretation) —
       challenges limb 2. Manually pulling and re-reading the single anomaly in an otherwise
       uniform sweep is a textbook setup for confirmation bias: the analyst approaches that one
       case already primed to find (or explain away) an exception, and single-case manual
       overrides are a known source of inconsistent, non-reproducible QC decisions.

  Strength of challenge: Moderate

  Summary: Limb 1 ("uniform verdict is usually broken") is not supported or refuted by direct
  base-rate literature on this exact scenario; the closest analogues (ICU alarms, sensor fault
  detection) treat uniform signal as ambiguous — sometimes a real shared effect, sometimes a
  fault — and explicitly warn against defaulting to either interpretation without independent
  corroboration. That already weakens the unqualified "usually broken." Limb 2 ("a lone anomaly
  deserves one direct read") is weaker still: the anomaly-detection and cognitive-bias
  literature treats hand-picking a single deviating case for manual review as a canonical bias
  trap, not a neutral QC good practice, especially when the reviewer already suspects the
  measure and is looking to confirm that suspicion.

  Specific risks: If C2A2 encodes "uniform = probably broken" as a heuristic, it will systematically
  discount true positive findings that happen to affect an entire batch (e.g., a real regression
  that breaks every instance of a task class), reclassifying real signal as measurement noise.
  If it also encodes "manually re-check the lone anomaly," it introduces a bias-prone manual
  override path exactly where confirmation bias is most likely to operate — reviewers checking
  the one different case only when it disagrees with their prior.

  Mitigations available: Require an independent corroborating signal (a second measure, ground
  truth spot-check across the uniform population, not just the anomaly) before concluding
  "broken." When reviewing the lone anomaly, review it under the same protocol as would be
  applied if it were the majority case, to avoid asymmetric scrutiny.

  Search scope: Preliminary — 3 searches (alarm fatigue base rates, sensor-fault degenerate
  output, anomaly-detection/cherry-picking bias). Did not find literature addressing this exact
  QC scenario (population-level measurement verdict uniformity) directly; relied on adjacent
  domains (clinical alarms, sensor fault detection, ML anomaly review bias).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1598
  Strongest counterargument: Both limbs encode an asymmetric prior — trust the crowd, distrust
  the singleton — that the literature does not support as a general rule. Uniform output is
  ambiguous between "shared real effect" and "instrument failure," and choosing "usually broken"
  without a base rate is an unjustified frequency claim. Meanwhile, singling out the one
  disagreeing case for manual re-examination is precisely the setup cognitive-bias research
  identifies as prone to confirmation bias, since the reviewer already knows it's the outlier
  before looking.
  What would need to be true for C2A2 to be safe: The task-class population would need to have
  a known, low base rate of genuine population-wide effects (so "broken" really is the more
  common explanation for uniformity in this specific domain), and the "one direct read" of the
  anomaly would need to be a blinded or protocol-matched check rather than a motivated
  re-examination.
  How to test: Empirically track, over many QC cycles, how often a uniform verdict turned out to
  be a real effect vs. a broken measure in this specific pipeline, and whether anomaly-only
  manual reviews changed write-up conclusions more often in the direction the reviewer already
  suspected (a red flag for confirmation bias) versus symmetrically in both directions.
