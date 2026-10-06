SEARCH-FOR-ASSUMPTION-1598:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1598
  Original statement: "A measure returning a uniform verdict across a whole population is usually
    broken rather than revealing, and a lone anomaly in an otherwise clean sweep deserves one direct
    read before write-up."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1598
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a generalised rule an agent derived from three of its own false positives.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Output quality-control literature for automated classifiers (general ML-QC pattern; see e.g.
       arxiv survey material on "from out-of-distribution detection to quality control," and patent-
       literature descriptions of classifier QC pipelines that flag predictions failing to match an
       expected output distribution). — Supports limb 1: a classifier/measure whose output distribution
       collapses to a single verdict across a whole population is a recognized failure signature that
       QC systems are explicitly built to catch, distinct from a genuine uniform population result.
    2. Statistical process control tradition (Shewhart/Deming control-chart reasoning, general
       knowledge) [unverified — from background knowledge, not confirmed by this search]: a process
       exhibiting zero natural variation is itself treated as anomalous and prompts investigation of
       the measurement system, not celebration of a "clean" result. Directly analogous to limb 1 but
       not independently confirmed by a retrieved source this session.
    3. Base-rate neglect literature — "On the generality and cognitive basis of base-rate neglect"
       (bioRxiv preprint / ScienceDirect companion, 2021-2022) and general anomaly-detection literature
       on analyst follow-up of flagged outliers (e.g. discussion of analysts and single anomalous
       points in outlier-detection surveys). — Bears on limb 2 (single anomaly deserving a direct read)
       but cuts in a more qualified direction than the claim: the base-rate literature is a caution
       against over-weighting rare/salient signals relative to their prior probability, not an
       endorsement of always investigating them. It supports that lone anomalies need deliberate
       handling, but not that a "direct read" is always warranted.

  Strength of support: Moderate for limb 1 (uniform verdict → suspect measure); Weak for limb 2 (lone
    anomaly → deserves a direct read).

  Summary: Limb 1 — "a uniform verdict across a whole population is usually broken rather than
    revealing" — has solid grounding: both classifier-QC practice and the general statistical-process-
    control heuristic (absence of variation is itself a red flag) treat degenerate, invariant output as
    a signal to check the measurement instrument, not the population. Limb 2 — "a lone anomaly deserves
    a direct read" — is only weakly supported; base-rate neglect research actually warns against
    over-trusting a single deviant signal without weighing its prior probability, which is in tension
    with (though not a flat contradiction of) "deserves one direct read." The two limbs diverge in
    support strength, so the combined claim is graded partially supported.

  Caveats: No source directly addresses "false positives an agent derived about its own measurement
    tooling," so all support is analogical (classifier QC, industrial SPC, human cognitive bias
    literature). The base-rate literature could equally be read as counter-evidence for limb 2 (an
    argument 15b should weigh) rather than support — flagged here for balance since it surfaced in a
    supportive-direction search.

  Search scope: Preliminary — three searches covering classifier degeneracy detection, base-rate
    neglect, and general anomaly-detection analyst practice. Statistical-process-control claim not
    independently re-confirmed by search this session (background knowledge only).

  Recommendation: PARTIALLY-SUPPORTED
