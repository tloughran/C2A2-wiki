# ASSUMPTION-966 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-966

**Date searched:** 2026-08-12

**Original item:** ASSUMPTION-966

**Original statement:** That ASSUMPTION-017 (humans validate everything) and ASSUMPTION-023 (33 agents) are arithmetically incompatible, not merely in tension.

### PROVENANCE

- **Origin:** 14a
- **Chain:** [14a → 15b]
- **Item type:** ASSUMPTION (stated)
- **Transform at each step:**
  - 14a: Extracted as a stated claim that two registered assumptions stand in arithmetic, not merely rhetorical, conflict.
  - 15b: Searched for challenging literature on human-review throughput, learning-to-defer and selective prediction, and assurance-by-sampling as an interpretation of "validate everything."
- **Current status:** CHALLENGED

**What is being challenged:** the arithmetic claim itself, by challenging the review model it presupposes. The incompatibility follows only if "humans validate everything" means one human inspecting each artefact serially. Both the machine-learning deferral literature and professional assurance practice reject that as the operative meaning of validation.

### Challenging evidence found: Yes

### Sources

1. **"No Need for Learning to Defer? A Training Free Deferral Framework to Multiple Experts through Conformal Prediction." arXiv:2509.12573.** — Reports reducing required expert labels per expert by up to 91.3% while maintaining predictive accuracy. Establishes that human review load is not a fixed multiple of production volume; it is a tunable quantity set by the deferral policy. Directly challenges the arithmetic, which treats review cost per artefact as a constant.
2. **"Learning to Defer in Congested Systems: The AI-Human Interplay." arXiv:2402.12237.** — Formalises the exact question at issue — how to scale automation under a fixed human capacity constraint — by combining learning-to-defer with queueing delays and soft capacity limits. The existence of a solved formalism for "more automation than humans can review" contradicts the framing that the two assumptions cannot coexist.
3. **"Learning When to Defer to Humans for Short Answer Grading." AIED / Springer (doi:10.1007/978-3-031-36272-9_34).** — Empirical instance: a selective-prediction policy reached expert human performance on 3,381 unlabelled items from 1,322 labelled ones, a reported ~25% reduction in human effort at expert accuracy. Demonstrates that population-level validation quality can be preserved while per-item human contact is reduced.
4. **Selective-prediction literature generally (Emergent Mind, "Selective Prediction in AI"; "Minimizing Human Intervention in Online Classification," arXiv:2510.23557) — [first source is a secondary summary; unverified].** — Establishes abstention-and-defer as a standard architecture in which the human sees only the high-risk residual.
5. **ISA 500, *Audit Evidence*, IAASB, and audit-sampling practice.** — In the profession whose product is assurance over populations too large to inspect item by item, "validate everything" is delivered by sampling with a stated confidence level plus tests of controls, not by exhaustive inspection. This is the strongest available challenge to the assumption's implicit reading of ASSUMPTION-017: exhaustive per-item human review has never been the meaning of validation at scale in any assurance discipline.

### Strength of challenge: Moderate

### Summary

The arithmetic is only as good as its model of review, and the challenge attacks the model. Under the reading that every artefact receives individual human inspection, ASSUMPTION-966 is trivially right — 33 agents producing continuously will exceed any human's throughput, and no literature disputes that. But both the machine-learning deferral literature and professional assurance practice reject that reading as the operative meaning of validation. Deferral and selective-prediction frameworks explicitly decouple human load from production volume, with reported reductions in required expert contact of 25% to 91.3% at preserved accuracy, and there is a formal treatment of exactly the congested case where automation outpaces human capacity. Independently, the auditing profession has always delivered assurance over populations it cannot inspect exhaustively, by sampling plus controls testing, with a stated confidence level substituting for exhaustiveness. On either route, the two assumptions are compatible under a defensible reading of validation, which means the conflict is a definitional one requiring ASSUMPTION-017 to be made precise — not an arithmetic impossibility. That is a materially different finding with a different remedy: rewrite ASSUMPTION-017 to state its review model, rather than choose between the two assumptions.

### Specific risks

If the arithmetic framing is accepted, C2A2 faces a false forced choice — cap the agent count or abandon human validation — and may reduce agent count for a reason that better validation design would dissolve. If the challenge is accepted carelessly, the opposite risk: a sampling or deferral regime adopted without stating its confidence level or its risk-stratification criteria, which delivers the *appearance* of validation coverage while high-risk artefacts flow through unreviewed. That failure mode is the one the deferral literature guards against with calibrated abstention, and it maps directly onto PRESUMPTION-768 in this batch — an unfalsified review process that never surfaces anything.

### Mitigations available

(a) Restate ASSUMPTION-017 with its review model explicit: exhaustive per-item, risk-stratified, or sampled-with-confidence-level. This is the load-bearing action and it costs nothing but a decision. (b) If sampled or stratified, define the strata by irreversibility and external visibility, and mandate exhaustive review only for the top stratum — the standard assurance pattern. (c) Instrument human review capacity empirically (artefacts reviewed per hour, by class) so the arithmetic can be redone against real throughput rather than assumed throughput. (d) Calibrate the deferral criterion and audit it: sample the auto-approved population periodically to estimate the escape rate, which is the negative control this regime needs.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** ASSUMPTION-966

**Strongest counterargument:** The claim of arithmetic incompatibility smuggles in a premise it does not defend, namely that validation means one human looking at every artefact. No mature assurance discipline works that way: auditors have delivered opinions on populations they cannot exhaustively inspect for a century, by sampling to a stated confidence level and testing controls, and the machine-learning literature has formalised the same move for automated pipelines — selective prediction and learning-to-defer route only the high-risk residual to humans, with published reductions in expert contact of up to roughly 90% at preserved accuracy, and there is an explicit formal treatment of the congested regime where automation outpaces human capacity. Under any of those readings, 33 agents and human validation coexist without contradiction. So ASSUMPTION-966 is best understood not as an arithmetic result but as a demand that ASSUMPTION-017 be made precise, and the demand is well-founded while the arithmetic conclusion is not. Acting on the arithmetic reading risks the specific bad outcome of capping agent count — the one variable that is expensive to change — instead of specifying the review model, which is free to change.

**What would need to be true for C2A2 to be safe:** ASSUMPTION-017 must state its review model explicitly. If it is risk-stratified or sampled, the strata or the confidence level must be published, the deferral criterion must be calibrated, and the auto-approved population must be periodically spot-audited so the escape rate is known rather than assumed. Given that, the two assumptions are compatible and the arithmetic objection dissolves.

**How to test:** Two measurements. First, establish actual human review throughput by class of artefact over a week — this is the denominator the arithmetic needs and currently lacks. Second, classify one week's agent output by irreversibility and external visibility; the size of the top stratum is the true exhaustive-review load. If that stratum is within measured human throughput, the assumptions are compatible in fact and not merely in principle. If it is not, ASSUMPTION-966 is corroborated — but corroborated against a stratified model, which is a much stronger and more useful result than the unstratified arithmetic.

---

## Search scope

Moderate. Query families executed: learning to defer and selective prediction under capacity constraints; audit evidence and sampling. Not searched: span-of-control and supervisory-ratio literature from organisational research, and queueing-theoretic models of approval gates, both named in the item's search strategy; these would bear on the throughput denominator. Broader search recommended before the arithmetic is redone.
