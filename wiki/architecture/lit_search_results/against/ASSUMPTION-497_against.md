SEARCH-AGAINST-ASSUMPTION-497:
  Date searched: 2026-08-29
  Original item: ASSUMPTION-497
  Original statement: Two proposals vanished with no recorded disposition; likeliest reading is deliberate withholding, but incidental loss cannot be excluded from the artifacts alone.

  SCOPE NOTE (load-bearing, applies to every item in this run):
    Two limbs. (1) The internal-empirical claim about this repository's file state: NOT-SEARCHED,
    literature cannot adjudicate it. (2) The generalizable question named by the item's own
    "Search targets" line: searched here. The item is NOT retagged [MISROUTED-INTERNAL-EMPIRICAL];
    REVISE-408's authorisation request to Tom stands untouched.

  INDEPENDENCE CAVEAT: 15a and 15b ran in the same process this run — a stronger coupling than the
    read-channel coupling the standing 15a/15b correlation discount was written for. Where this
    search agrees with 15a, that agreement is worth LESS than usual and 15c discounts it.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-497
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. PagerDuty, "The Blameless Postmortem." — attaching an individual's character to their actions, assuming negligence or intent behind an error, is the named failure of non-blameless analysis. The item's 'likeliest reading is deliberate withholding' is an intent attribution made from an evidence gap.
    2. Attribution-bias findings summarised in the postmortem literature: people are more likely to attribute NEGATIVE outcomes to another's intentions than neutral or positive ones. The prior favouring 'withholding' over 'loss' is a known bias, not a Bayesian update.
    3. Augment Code, 2026. "How to Write an Incident Postmortem." — 'causality may exist, but evidence often does not'; real incidents usually have multiple contributing conditions, each necessary and only jointly sufficient, and five-whys style linear reasoning forces a simplistic single explanation onto them.

  Strength of challenge: Moderate

  Summary: The item's hedge is correct and its ranking is not. Nothing challenges the claim that the two hypotheses are indistinguishable from the artifacts; the challenge lands on 'likeliest reading is deliberate withholding'. Attribution research says a negative outcome plus an evidence gap reliably produces an intent attribution, and postmortem practice treats that specific inference as the thing to suppress. The coincidence cited in support (the two match the two the sewing run flagged) is real evidence, but with n=2 out of 36 the coincidence is weak — and the bulk-move mechanism is independently documented as high-loss, so the alternative has its own positive prior rather than being a courtesy.

  Specific risks: If withholding is assumed and the cause was loss, the bulk-move defect stays unfixed and recurs on the next bulk operation, while a human is quietly recorded as having made a decision they did not make. Both errors are durable and neither is self-correcting.

  Mitigations available: Drop the ranking and keep the disjunction. Add omission detection so the next occurrence IS decidable: a pre-move manifest, so absence becomes a detectable anomaly rather than an interpretive question.

STEELMAN:
  Item: ASSUMPTION-497
  Strongest counterargument: Strongest counterargument: the item is doing forensics on its own logs while having no independent expectation set, and in that situation the ranking of hypotheses is determined by whatever is psychologically available rather than by evidence. The postmortem literature's whole point is that this is where analysis reliably goes wrong. The honest output is 'undecidable, and here is the manifest that makes the next one decidable' — the ranking adds nothing but a false sense of resolution and quietly assigns intent to a person.
  What would need to be true for C2A2 to be safe: Safe if the ranking is dropped and treated as a disjunction, and if a pre-move manifest is added before the next bulk state transition.
  How to test: Reconcile queue-at-review (36) against decision archive (34) by ID; separately, check whether any pre-move record of the 36 exists. If none does, the withholding-vs-loss question is formally undecidable and should be recorded as such.

  Recommendation: PARTIALLY-CHALLENGED
