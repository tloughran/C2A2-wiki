# PRESUMPTION-777 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-777

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-777

**Original statement:** That this pipeline's inputs are auditable; transcripts return no tool outputs, so every unmarked figure is an agent's self-report. *(REFLEXIVE — the item is about the pipeline that produced it.)*

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference; flagged REFLEXIVE)
- **Transform at each step:**
  - 14b: Inferred, of its own detection pipeline, that because transcripts carry no tool outputs, every quantitative figure in the register that is not otherwise marked is an unverified agent self-report; risk graded High.
  - 15b: Searched for challenging literature on self-report validity, chain-of-thought faithfulness and its critics, and audit-evidence standards for entity-generated information.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** the inference from "self-reported" to "unauditable." The figures in question are counts over a durable artefact store and are therefore re-derivable ex post; and the faithfulness literature the worry draws on concerns *reasoning* traces, a different epistemic object from a count.

### Challenging evidence found: Partial

### Sources

1. **ISA 500, *Audit Evidence*, IAASB.** — Where information produced by the entity is used as audit evidence, the auditor is required to evaluate its accuracy and completeness — the standard contemplates precisely this situation and provides a procedure rather than a disqualification. Self-generated evidence obtained by the *auditor's own* procedures sits at the top of the reliability hierarchy, which is significant here: a figure the register re-derives itself from the artefact store is high-reliability evidence, not self-report.
2. **Lanham, T. et al., 2023. "Measuring Faithfulness in Chain-of-Thought Reasoning." arXiv:2307.13702.** — Establishes faithfulness as a measurable property via interventions (truncation, paraphrase, injected error) on the reasoning trace. Cited here for scope: the object of study is the causal role of a *reasoning narrative* in producing an answer, not the accuracy of a factual count, and the paper's method shows that the measurement instrument shapes the conclusion drawn.
3. **"the case for CoT unfaithfulness is overstated," LessWrong — [unverified — author not identified in search results; non-peer-reviewed].** — A live counter-position holding that the unfaithfulness results are narrower than commonly cited. Included honestly as evidence that the literature the presumption implicitly relies on is contested, not settled.
4. **Turpin et al., 2023 (unfaithful CoT under biasing features) — [title unverified; described in search snippet only].** — Described as demonstrating unfaithfulness in *adversarially constructed* settings where biasing prompt features change the answer without changing the stated reasoning. The adversarial construction is the boundary condition: it does not license a general inference that unmarked figures are unreliable in a non-adversarial reporting task.
5. **"Doing What They Say, Not What They Reason: Locating the Faithfulness Gap in LLM Agents." arXiv:2606.00476.** — Localises the faithfulness gap rather than treating it as global, consistent with a bounded rather than blanket discount on agent self-report.

### Strength of challenge: Moderate

### Summary

The reflexive observation is accurate and important: transcripts carry no tool outputs, so a figure like "191 uncommitted paths" or "12 of 12" arrives in the register with no attached evidence. What the literature challenges is the step from there to unauditability. First, the relevant standard — ISA 500 — treats entity-generated information as usable subject to the consumer testing its accuracy and completeness, and rates evidence the consumer generates by its own procedures as the most reliable class; because almost every figure in this register is a count over a durable artefact store, the auditing route is open and cheap, which means the inputs are auditable in the sense that matters even though the transcript does not audit them. Second, the faithfulness literature the worry leans on is about reasoning narratives under adversarial or biasing conditions, and there is a live position that even those results are over-read; a count is a different object from a rationalisation, and the failure modes differ (miscount, stale count, and scope error rather than post-hoc justification). The presumption's real content, stated precisely, is that the register currently carries no *marks* distinguishing re-derived figures from reported ones — a provenance-annotation gap, not an evidential impossibility.

### Specific risks

If the strong reading is adopted, every quantitative claim in the register becomes suspect and the register loses its usefulness as a record while gaining nothing, because no alternative source of these figures exists inside the transcript channel. If the finding is dismissed, unmarked figures continue to accumulate and the specific realistic failure is a stale or mis-scoped count propagating into a severity grade — for instance a path count taken at one moment and cited as current days later, or a denominator drawn from a different population than the numerator. That failure is silent and is the concrete hazard worth guarding.

### Mitigations available

(a) Mark every figure with its derivation class: RE-DERIVED (recomputed from the artefact store at a stated time), REPORTED (agent self-report, unverified), or ATTESTED (accompanied by a tool output). This is a one-token change and it closes the presumption's actual gap. (b) For any figure that gates a severity grade, require re-derivation before the grade is applied; this bounds the cost to the small gating subset. (c) Spot-audit: sample REPORTED figures and recompute them, publishing the discrepancy rate so the discount applied is empirical. (d) Where the harness permits, persist tool outputs to the durable store rather than relying on the transcript, converting REPORTED figures to ATTESTED at source.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-777

**Strongest counterargument:** The presumption conflates "not accompanied by evidence" with "not auditable," and those are different claims. Nearly every figure at issue is a count over a store that still exists on disk; ISA 500's posture is that entity-generated information is usable when the consumer tests its accuracy, and that evidence the consumer generates through its own procedures is the most reliable class available — which means the register can convert almost any REPORTED figure to a high-reliability one by recomputing it, at trivial cost. The faithfulness literature does not close this gap either: Lanham's and Turpin's results concern whether a *reasoning narrative* causally produced an answer, largely under adversarial or biasing constructions, and there is a serious position that even those findings are over-read. A count is not a rationalisation; its failure modes are staleness and scope error, both of which re-derivation detects directly. Read at full strength the presumption implies that a register whose figures are self-reported is worthless, which would be a counsel of despair; read precisely it says the register lacks a derivation-class mark, which is a small and immediately fixable defect and one whose fix also happens to close the gating-decision risk.

**What would need to be true for C2A2 to be safe:** Every figure must carry a derivation-class mark, and every figure that gates a severity grade must be re-derived from the durable store at the time of grading. Under those two conditions the absence of tool outputs in the transcript is a logging limitation rather than an audit failure.

**How to test:** Sample twenty unmarked figures from recent register entries and recompute each from the artefact store. The discrepancy rate is the empirical answer to the presumption, and it is obtainable today. Pay particular attention to two failure classes the count framing predicts and the self-report framing does not: figures that were correct when written and are now stale, and figures whose numerator and denominator were drawn from different populations. If the discrepancy rate is low and the errors are staleness rather than fabrication, the challenge holds and the fix is annotation plus re-derivation at gating time.

---

## Search scope

Preliminary-to-moderate, and note the reflexive constraint: this search was itself conducted through a channel that returns snippets rather than verified sources, so several citations here are marked unverified for exactly the reason the item describes. Query families executed: CoT faithfulness and its critics; audit-evidence standards. Not searched: the survey-methodology literature on self-report validity and social desirability, and the agent-observability/tracing literature named in the item's search strategy. Broader search recommended.
