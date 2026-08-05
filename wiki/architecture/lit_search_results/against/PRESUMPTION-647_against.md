SEARCH-AGAINST-PRESUMPTION-647:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-647
  Original statement: That a guard's tolerance can be validly calibrated from the
    single incident that motivated it — thresholds of +20 skips and 25% node change
    derived from one observation of a 2 -> 1164 jump.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-647
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 introduction of a guard whose thresholds
        trace to a single observed 2 -> 1164 skip jump
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. EEMUA 191 (4th edition), "Alarm Systems: A Guide to Design, Management and
       Procurement." Engineering Equipment and Materials Users Association. — The
       reference standard for alarm rationalisation; specifies steady-state alarm
       rates (order of one alarm per ten minutes per operator) and requires each
       alarm to be justified against process-wide analysis, explicitly not against
       the incident that prompted it. Rates above roughly six to twelve per hour are
       documented to degrade response quality.
    2. Cvach, M., 2012. "Monitor Alarm Fatigue: An Integrative Review." Biomedical
       Instrumentation & Technology, 46(4), 268. — Synthesises evidence that
       thresholds set for maximum sensitivity produce nonactionable alarm volumes
       that clinicians then silence or ignore, converting a well-intentioned guard
       into a net safety decrement.
    3. Jämsä, J. et al., 2021. "Clinical alarms and alarm fatigue in a University
       Hospital Emergency Department — A retrospective data analysis." Acta
       Anaesthesiologica Scandinavica. — Empirical alarm-burden data showing
       nonactionable alarm proportions of the order of 70%+ under default and
       incident-derived thresholds.
    4. (2011). "An Evidence-Based Approach to Reduce Nuisance Alarms and Alarm
       Fatigue." Biomedical Instrumentation & Technology, 45(s1), 46. — Documents
       that effective threshold change requires distributional evidence (e.g., the
       Johns Hopkins SpO2 90% -> 88% change cutting alarms 63%), i.e. thresholds
       must be fitted to the observed population of values, not to one event.
    5. (2019). "LSTM-Based Anomaly Detection: Detection Rules from Extreme Value
       Theory." arXiv:1909.06041. — Methodological counter: correct threshold
       setting for rare events estimates the tail distribution (generalized Pareto)
       to achieve a specified false-alarm rate; a single realised extreme provides
       essentially no information about the tail's shape or scale.
    6. (2025). "Beyond Static Thresholds: Adaptive RRC Signaling Storm Detection with
       Extreme Value Theory." arXiv:2511.01391. — Shows static thresholds derived
       from historical incidents underperform tail-estimated adaptive thresholds and
       are structurally prone to both misses and floods as the base distribution drifts.
    7. Sunstein, C.R. & Zeckhauser, R., 2011. "Overreaction to Fearsome Risks."
       Environmental and Resource Economics. — The behavioural mechanism: a single
       vivid event is over-weighted via the availability heuristic, producing
       defences shaped like the last incident rather than like the risk distribution.

  Strength of challenge: Strong

  Summary: Two literatures converge and both go against the presumption. The
    statistical one says a threshold intended to control false-alarm rate is a
    property of the tail of a distribution and cannot be estimated from n=1; extreme
    value theory exists precisely because one realised extreme is uninformative about
    the probability of the next one. The human-factors one says the practical failure
    mode of a threshold set too tight is not a false sense of security but alarm
    fatigue: operators acknowledge without investigating, or disable the guard, and
    the guard's real-world sensitivity collapses to something worse than no guard at
    all because it also consumes attention. The availability-heuristic literature
    explains why an incident-derived threshold feels rigorous while being arbitrary.
    Nothing in the searched literature supports single-incident calibration as sound
    practice; the standards documents (EEMUA 191) explicitly prescribe the opposite.

  Specific risks: If the thresholds are wrong in the tight direction, the guard fires
    on ordinary variation, and the predictable organisational response is to raise the
    threshold ad hoc, add `|| true`, or stop reading the output — at which point C2A2
    carries the cost of the guard and none of the protection, and believes itself
    protected. If they are wrong in the loose direction, a smaller-but-real corruption
    (say, 2 -> 21 skips, or a 20% node change) passes unremarked, and the guard's
    existence actively licenses the false conclusion that nothing anomalous happened.
    Because the thresholds were never derived from the distribution of normal day-to-day
    variation, C2A2 does not currently know which of these two failure modes it is in.

  Mitigations available: (1) Backfit before trusting: replay the guard against the
    historical series of skip counts and node counts and record how many times it
    would have fired. If the implied firing rate exceeds roughly one per month, the
    threshold is too tight for a system with a single human reviewer. (2) Replace the
    absolute constant with a distributional rule — e.g. fire above the 99th percentile
    of the trailing 90-day change distribution, recomputed weekly. (3) Log near-misses:
    record every run's skip delta and node-change percentage regardless of firing, so
    that after 90 days the threshold can be set from data rather than from memory.
    (4) Track the guard's own disposition history — how often it fired, and how often
    the firing was overridden. Override rate is the direct empirical measure of alarm
    fatigue and should be a monitored quantity. (5) Separate "alarm" from "alert":
    a logged anomaly that does not demand action costs nothing; only escalate the tail.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-647
    Strongest counterargument: A guard with an imperfectly calibrated threshold
      strictly dominates no guard at all when the cost of a false positive is a
      cheap human glance and the cost of a false negative is a corrupted persistent
      artifact. The alarm-fatigue literature describes environments with hundreds of
      alarms per shift and a fixed-attention operator; a guard that fires perhaps
      twice a year in a single-user system is nowhere near that regime, so the
      fatigue argument does not transfer. Moreover, incident-derived thresholds are
      normal practice in SRE precisely because the observed incident is the only
      ground truth available at the moment the guard is written, and waiting for a
      distribution means being unprotected for the duration of the wait.
    What would need to be true for C2A2 to be safe: (a) The guard's realised firing
      rate is low enough that every firing is actually investigated — measured, not
      assumed. (b) The threshold is loose enough to sit above ordinary variation but
      tight enough to catch corruptions materially smaller than the one observed;
      this requires knowing the ordinary variation. (c) The guard's output is
      logged even when it does not fire, so that the calibration can be revisited
      from data rather than from a second incident. (d) No path exists to bypass or
      mute the guard without that bypass itself being recorded.
    How to test: Recompute skip counts and node-count deltas for every stored run in
      the vault's history and plot the distribution. Read off where +20 and 25% sit.
      If either falls inside the ordinary range, the guard is miscalibrated tight; if
      both sit far beyond every observed value except the one incident, it is
      miscalibrated loose. This is a single pass over existing data and needs no new
      instrumentation.

  Search scope: Adequate. Concepts searched: alarm threshold setting from single
    incidents; alert/alarm fatigue and disable rates; EEMUA 191 alarm management;
    extreme value theory for false-alarm-rate control; adaptive vs static thresholds;
    availability heuristic and policy overreaction to rare events.
