SEARCH-AGAINST-ASSUMPTION-1246:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1246
  Original statement: The specific two-mention threshold for promoting an item is appropriate. (The
    parent principle is already dispositioned; only the numeric threshold is untested.)
  Generalizable limb searched: Is there literature bearing on the calibration or arbitrariness of
    small-integer confirmation thresholds (n=2) for promoting an observation to a tracked item?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Weak — deliberately under-searched. Priority Low, residue only: Pass 1 only,
    2 queries, no Pass 2, per tasking. Query 1 (threshold calibration / ROC) returned almost entirely
    clinical-assay and data-mining material with no transferable result. Query 2 (qualitative
    saturation) returned the closest available analogue but is analogical rather than on-point. No
    literature was found that addresses a two-mention promotion threshold in a review or
    self-audit pipeline. The finding below is a partial and indirect challenge, and the residue is
    carried, not resolved.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1246
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Isolated the numeric threshold as the untested residue after the parent principle was
           dispositioned.
      15b: Searched for challenging literature (2026-08-31) — Pass 1 only, Low priority
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Guest, G., Namey, E. & Chen, M. 2020. "A simple method to assess and report thematic
       saturation in qualitative research." *PLOS ONE*. (Snippet-level.)
       — The closest usable analogue found. It treats the confirmation threshold as an explicit,
       reportable *parameter pair* — a base size plus a run length — rather than as a self-evident
       number, and demonstrates that the number of additional units needed to confirm that nothing
       new is arriving is derived from the data, not assumed. The snippet reports a worked case at
       run length 2 requiring eleven interviews plus two more to confirm no new information. This
       challenges 1246 not by showing that two is wrong but by showing that a threshold of this kind
       is a tunable parameter that carries a justification burden the pipeline has not discharged.
    2. Naeem, M., Ozuem, W., Howell, K. & Ranfagni, S. 2024. "Demystification and Actualisation of
       Data Saturation in Qualitative Research Through Thematic Analysis." *International Journal of
       Qualitative Methods* (SAGE). Also a review reported in the same search finding that 42% of
       studies used saturation without defining it and only about 40% documented their assessment.
       — Supports the general point that rule-of-thumb confirmation thresholds are routinely adopted
       and reported without stated criteria, and that this is treated in the methods literature as a
       reporting failure rather than as acceptable practice.
    3. Threshold-calibration literature generally (ROC / precision-recall tradeoffs; family-wise error
       rate vs false discovery rate control), encountered in query 1.
       — Recorded as *not* transferable. This literature calibrates thresholds against a labelled
       ground truth and a stated loss function. C2A2 has neither for item promotion, so the framework
       cannot be applied and offers no verdict on n=2. Noted so that a later cycle does not repeat
       the query expecting a result.

  Strength of challenge: Weak

  Summary: No literature was found that speaks directly to a two-mention promotion threshold, and
  none was found showing that n=2 is wrong. The one transferable finding is procedural: in the nearest
  analogous methodological literature, confirmation thresholds of this form are treated as parameters
  to be derived and reported, not as constants to be assumed, and undocumented rule-of-thumb cutoffs
  are treated as a known reporting weakness. That challenges the word "appropriate" — which asserts
  calibration — while leaving the number itself untouched. Substantively, n=2 remains unevaluated: the
  false-positive cost (promoting noise that happened to recur once) and the false-negative cost
  (dropping a real signal mentioned only once) have not been estimated in either direction, and
  without a loss function the standard threshold-calibration machinery cannot be brought to bear. Per
  tasking this item was searched at Low priority with two queries and no deepening pass; the residue
  is carried forward, not resolved.

  Specific risks: If two is too low, the promoted set fills with coincidental recurrence and the
  pipeline's attention is diluted — a cost that is invisible because promoted noise looks the same as
  promoted signal. If two is too high, single-mention items that matter are silently discarded, and
  that loss leaves no trace at all in the record, so it can never be discovered from the pipeline's
  own outputs. The asymmetry is the real hazard: only one of the two error types is even in principle
  observable downstream, which biases any future recalibration toward the visible error.

  Mitigations available: Log rejected single-mention items rather than discarding them, so the
  false-negative rate becomes estimable at all. Periodically sample promoted two-mention items and
  ask retrospectively whether promotion was warranted. Follow the saturation literature's minimum
  standard and simply *state* the threshold and the reasoning behind it wherever it is applied, which
  costs nothing and converts an unexamined constant into an auditable parameter.

  STEELMAN:
    Strongest counterargument: Two is not offered as a calibrated optimum but as a cheap
    single-occurrence filter — its whole job is to exclude one-off noise, and any n>=2 does that. Where
    the cost of a false positive is a small amount of review attention and the cost of a false
    negative is a missed item that will very likely recur and be caught next cycle, precise
    calibration is not worth its own cost, and demanding it is exactly the kind of gold-plating the
    pipeline should resist. The absence of literature on this threshold may simply reflect that
    nobody considers it a question worth studying.
    What would need to be true for C2A2 to be safe: that genuinely important items recur — i.e. that
    a single-mention miss is recoverable on a later pass rather than permanently lost — and that the
    review cost of a false positive stays small.
    How to test: Retain rejected single-mention items for three cycles and measure how many
    subsequently reach two mentions. A high recurrence rate vindicates n=2 as a safe filter and closes
    the residue. A low rate means single-mention misses are permanent and the threshold needs
    lowering or supplementing with a severity override.

  Recommendation: PARTIALLY-CHALLENGED
