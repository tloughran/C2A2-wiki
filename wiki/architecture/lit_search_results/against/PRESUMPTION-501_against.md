SEARCH-AGAINST-PRESUMPTION-501:
  Date searched: 2026-07-20
  Original item: PRESUMPTION-501
  Original statement: [inferred] A measurement disagreement is presumed to be a measurement problem to be de-inflated rather than a contradiction to be reconciled. Two same-day censuses of one vault produced four differing numbers and two differing corrections; two further ID-maximum disagreements appeared the same day.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-501
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by cross-reading the two 2026-07-19 sewing transcripts and the cowork→chat summary against live registry maxima
      15b: Searched for challenging literature (data reconciliation practice, definitional vs error divergence, reference-standard designation)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Monte Carlo, "The Comprehensive Guide To Data Reconciliation" (retrieved 2026-07-20). Mismatches between systems "often stem from definitional differences rather than actual errors" — attribution windows, processing delays, differing definitions — and the guidance is explicit that "not all differences represent actual errors requiring correction."
    2. Tricentis, "What is data reconciliation? A practical guide" and Precisely, "Data Reconciliation Definition" (retrieved 2026-07-20). Reconciliation begins by aligning aggregation level and selecting common columns; financial data in different systems is routinely aggregated at different levels, and comparing counts before aligning definitions produces spurious discrepancies by construction.
    3. dqools, "How to Reconcile Data with Table Comparison Checks" (retrieved 2026-07-20). Record-count comparison is characterised as the shallowest reconciliation check, catching missing or extra records but unable to distinguish definitional from substantive divergence without schema alignment. Bears directly: the four numbers in question are record counts.
    4. This vault's own ASSUMPTION-474, filed the same day, which attributes roughly +80 of a +225 delta to a resolver definitional change. That is the pipeline's own evidence that in at least one of the same-day cases, de-inflation was the correct call — the disagreement genuinely *was* a measurement artefact.

  Strength of challenge: Moderate

  Summary: The presumption is well surfaced and the pattern it names is real: four numbers, two corrections, no designated authority, and a default reflex to de-inflate. But the item's implied correction — that these should be treated as contradictions to reconcile rather than measurement problems to de-inflate — runs against reconciliation practice, which holds the opposite as the base case. In production data systems, count divergence between two readers of the same store is *usually* definitional, arising from inclusion boundaries, aggregation level, and timing, and the standard first move is to align definitions rather than to escalate the divergence as a substantive conflict. The magnitudes in this case are consistent with that profile: inclusion-boundary sized, not corruption sized. And the pipeline supplied its own decisive counterexample the same day — ASSUMPTION-474 attributes ~80 of a ~225 delta to a resolver definitional change, which means that for that case the de-inflating instinct was correct and treating it as a contradiction would have consumed effort to reach the same conclusion. This does not vindicate the reflex; a reflex that happens to be right is still unexamined. But it does challenge the item's directional recommendation.

  Specific risks: Adopting a general rule that count disagreements are contradictions creates work proportional to the number of readers times the number of artifacts, in a pipeline already identified as unable to drain. It also risks the opposite pathology: if every definitional difference is escalated, genuine corruption is buried in a stream of resolved-as-definitional reports, which is the alert-fatigue mechanism this vault has already documented. The item's own proposed remedy (OPEN-124, a counting authority per artifact) has a further known cost: this vault's PRESUMPTION-494 search found single-source-of-truth designation characterised as a coupling anti-pattern that does not prevent a differently-scoped reader from computing a shadow count, so it hides divergence rather than removing it.

  Mitigations available: Circulate counts with their definitions attached — scope, inclusion rule, timestamp, resolver version — which the reconciliation literature identifies as the actual fix and which is cheaper than designating authorities. Reserve reconciliation-as-contradiction for divergences that survive definition alignment; those are the substantive ones and are rare. Where an authority is designated, publish its inclusion rule so that a differently-scoped question is answered by re-deriving from the rule rather than by a shadow count.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-501
  Strongest counterargument: The item spots a reflex and infers that the reflex is wrong, when the reflex is what the field recommends. Data-reconciliation practice treats definitional divergence — different inclusion windows, different aggregation levels, different processing timing — as the default explanation for two systems disagreeing about a count, states plainly that not all differences are errors requiring correction, and prescribes definition alignment before escalation. Record-count comparison is described as the shallowest available check precisely because it cannot separate the two cases on its own, and record counts are exactly what disagreed here. The magnitudes fit the definitional profile rather than the corruption profile. Most tellingly, the same pipeline on the same day filed ASSUMPTION-474, which attributes about eighty of a two-hundred-and-twenty-five item delta to a resolver definition change — that is the system's own demonstration that at least one of these disagreements really was a measurement artefact and that de-inflating it was correct. So the presumption's real defect is not its direction but its automaticity: the system reaches the right answer without checking, which means it will reach the same answer when the answer is wrong and nothing in the process will notice. The correct reframing is not "treat disagreements as contradictions" but "attach the definition to every count so that the definitional case resolves itself and only the residual reaches a human."
  What would need to be true for C2A2 to be safe: The divergences would have to be large relative to plausible inclusion-boundary effects, and would have to survive alignment of scope and timestamp. Neither has been checked for any of the four numbers.
  How to test: For each of the four disagreeing numbers, record the reader, the inclusion rule, the timestamp, and the resolver version, then re-derive all four under one rule over one frozen snapshot. Whatever divergence remains after that is the substantive component, and its size decides the item: if it is zero across all four, the de-inflating reflex was correct four times out of four and the presumption's recommendation is refuted; if any residual is non-trivial, the item is vindicated for that case specifically. Run this before implementing OPEN-124, since a counting authority designated over unaligned definitions inherits the problem.

  Search scope: Preliminary — two targeted searches plus in-vault cross-reference. The inter-rater-reliability-where-raters-are-instruments sub-target was not retrieved and remains open.
