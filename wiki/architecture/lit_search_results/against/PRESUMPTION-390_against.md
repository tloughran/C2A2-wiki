SEARCH-AGAINST-PRESUMPTION-390:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-390
  Original statement: "That corpus-slice/analytic-axis variation produces genuinely different 'reference frames' (Thousand-Brains transfer condition assumed, not shown)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-390
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the neuroscience reference-frame metaphor is assumed to transfer without checking decorrelation
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Metaphor-transfer caution (domain-transfer literature). - A neuroscience construct (cortical reference frames) does not transfer to multi-agent LLMs without validating the transfer condition; analogy is not mechanism.
    2. Correlated-error LLM ensembles ('Nine Judges...', arXiv 2025). - Input/prompt variation often fails to decorrelate model errors; nominal frame-diversity != effective diversity.
    3. Prompt-sensitivity studies. - LLM outputs vary with prompts, but the variation is frequently superficial (style) rather than error-decorrelating.

  Strength of challenge: Strong

  Summary: Strongly challenged: the presumption assumes that varying corpus slices/analytic axes yields genuinely independent 'reference frames' that decorrelate errors, borrowing the Thousand-Brains framing. But (a) the neuroscience-to-multi-agent transfer condition is asserted, not demonstrated, and (b) the empirical LLM literature shows input variation often does NOT decorrelate errors - output may differ in surface form while shared errors persist. If axes fail to decorrelate, the 'reference-frame ensemble' is the redundancy trap (ties 347/386).

  Specific risks: The pathway's core claim to robustness/diversity could be vacuous: 'different frames' that share errors give correlated columns dressed as diverse ones, inflating false confidence.

  Mitigations available: Empirically measure inter-column error correlation per axis; require demonstrated decorrelation before treating axes as independent frames; do not rely on the neuroscience analogy as evidence.

  STEELMAN:
    Item: PRESUMPTION-390
    Strongest counterargument: Calling corpus-slice variation 'different reference frames' is an analogy, not a demonstrated mechanism; unless the axes are shown to decorrelate errors, the design is correlated redundancy with a neuroscientific label, and the Thousand-Brains transfer is doing unearned work.
    What would need to be true for C2A2 to be safe: Different axes produce measurably decorrelated errors (low pairwise error correlation) on the target task.
    How to test: Compute per-axis pairwise error correlation on a labeled benchmark; if not materially below same-seed baselines, the transfer condition fails.

  Search scope: Metaphor transfer; input-variation decorrelation. Comprehensive.

  Recommendation: CHALLENGED

SEARCH-AGAINST-PRESUMPTION-390 (RE-TRIGGER cycle 1):
  Date searched: 2026-07-08
  Original item: PRESUMPTION-390
  PROVENANCE:
    Chain: [... -> 15c -> 15d -> 15b] (cycle 1, 2026-07-08)
    Transform: 15d weekly re-trigger 2026-07-05; 15b refreshed disconfirmatory search
    Current status: NO-CHALLENGE-FOUND (direct) / PARTIALLY-CHALLENGED (by extension)
  New sources since last cycle: No direct critique (TBP corpus arXiv 2507.04494 describes frames but no correlated-redundancy objection published)
  Strength of challenge: Weak-to-Moderate
  Summary: The theoretical challenge stands on first principles but lacks targeted literature: TBP 'reference frame' requires genuinely different sensorimotor/informational bases; three overlapping readings of one corpus may be correlated redundancy. No external source tests this transfer condition.
  STEELMAN: Calling three analyses of the same corpus 'different reference frames' borrows TBP prestige without meeting its transfer bar; they may just be correlated re-reads.
  Recommendation: NO-CHALLENGE-FOUND (direct) / PARTIALLY-CHALLENGED (by extension) / Keep as live but under-evidenced challenge; burden is internal — measure inter-slice correlation/independence to earn the label. Do not rely on external literature to settle it.
