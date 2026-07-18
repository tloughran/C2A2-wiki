SEARCH-AGAINST-PRESUMPTION-461:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-461
  Original statement: "A single specialist agent can reliably assign the 'paradigm-shift candidate' label at intake, one pass, no adjudication or second opinion."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-461
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, HIGH, from 2026-07-08 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Gartlehner, G., et al., 2020. "Single-reviewer abstract screening missed 13 percent of relevant studies: a crowd-based, randomized controlled trial." Journal of Clinical Epidemiology 121. — RCT: single-reviewer screening achieved 86.6% sensitivity (missed 13% of relevant studies) vs 97.5% for dual screening — a ~4x reduction in misses from adding a second screener.
    2. Waffenschmidt, S., et al., 2019. "Single screening versus conventional double screening for study selection in systematic reviews: a methodological systematic review." BMC Medical Research Methodology 19:132. — Across evaluations, single screening missed a median 5% of relevant studies with a range up to 58%; experience mattered greatly (experienced median 3%, inexperienced 13%). Conclusion: single screening does not meet the methodological standard for decisions that depend on not missing rare relevant items.
    3. "Characteristics and recovery methods of studies falsely excluded during literature screening — a systematic review." 2022. PMC9644550. — False exclusions at intake are systematically hard to recover: items screened out generally leave the workflow permanently unless a dedicated recovery mechanism exists — the miss is final, which is the worst case for a rare-category label.

  Strength of challenge: Strong

  Summary: The best empirical evidence on single- vs dual-judge intake screening is unambiguous: one screener misses a material fraction of relevant items (5-13% typical, far worse at the tail), and a second independent judgment recovers most of that loss. The paradigm-shift-candidate task is a HARDER version of the studied task on every axis that drives miss rates: the category is low base-rate (misses are concentrated in rare positives), the construct is fuzzy and judgment-laden (vs relatively crisp PICO inclusion criteria), and there is no adjudication step to catch drift. A single agent also exhibits the automated analogue of rater drift — prompt/context sensitivity and model-version changes shift the effective decision boundary over time with no second rater to expose it. And per the false-exclusion literature, intake misses are structurally unrecoverable: a source not labeled at intake never re-enters consideration (compounded by PRESUMPTION-460's capture-finality). One-pass single-judge labeling of a rare, consequential category is the configuration the screening literature specifically warns against.

  Specific risks: Genuine paradigm-shift candidates — by definition the highest-value, lowest-frequency items in the pipeline — are silently missed at a double-digit percentage rate, with no recovery path; label meaning drifts across model/prompt versions so the candidate set is temporally inconsistent; because misses are invisible (no ground truth arrives to contradict them), confidence in the single-pass design grows precisely while it fails.

  Mitigations available: Dual screening on this label only (a second agent with an independent prompt/framing; cheap because the label is rare and the second pass can run on intake batches); adjudication of disagreements by a third pass or human; asymmetric threshold — bias the single screener toward over-labeling and let a second stage prune (sensitivity-first, the standard rapid-review hedge); periodic audit: re-screen a random sample of NOT-labeled intake items to estimate the miss rate directly.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: The single-vs-dual literature studies humans, whose errors are attention-driven and uncorrelated; a single LLM agent applies uniform attention to every item and never fatigues, so its misses are systematic rather than random — and a second copy of a similar agent would share those systematic blind spots, delivering far less than the human dual-screening gain. Waffenschmidt's own finding that experienced single reviewers miss only ~3% supports a well-specified specialist agent as an acceptable rapid-review-grade screen, and the label is advisory (candidate flagging for later human attention), not a terminal gate.
    What would need to be true for C2A2 to be safe: The label must genuinely be advisory with a downstream human look at candidates AND some path by which unflagged items get reconsidered (otherwise it is a terminal gate in practice); the agent's decision boundary must be stable across model/prompt versions; correlated-blind-spot risk must be addressed by making any second pass use a genuinely different framing, not a clone.
    How to test: Construct a small ground-truth set (items the human owner judges to be clear paradigm-shift candidates, mixed with distractors) and measure the single agent's sensitivity; then measure the marginal recall of a differently-prompted second agent. The delta directly prices what "no second opinion" costs.
