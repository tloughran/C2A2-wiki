# ASSUMPTION-012 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-012

**Date searched:** 2026-04-13

**Original item:** ASSUMPTION-012

**Original statement:** "Human review is the primary throughput constraint"

### PROVENANCE

- **Origin:** 14a/14b (bottleneck identification)
- **Chain:** Constraint assumption → 15b (evaluation)
- **Item type:** ASSUMPTION (performance claim)
- **Current status:** CHALLENGED

### Challenging evidence found: YES

### Sources

1. **Asyncsquad Labs (2025). "Code Review is a Bottleneck in the AI Era: Rethinking Software Quality Gates."** — While code review *appears* to be the bottleneck, fixing it without improving automation reveals that the true bottleneck is often *test generation*, *compilation*, or *deployment*. Removing one bottleneck just reveals the next.

2. **DigitalOcean (2026). "13 AI Testing Tools to Streamline Your QA Process."** — Automated testing, LLM evaluation, and continuous monitoring can reduce human review burden significantly. Human review is not the only or primary constraint; evaluation automation can be equally important.

3. **Panther Platform (2025). "Identifying and Mitigating False Positive Alerts."** — Automated quality filters generate excessive false positives; human review must handle alert fatigue, making review more time-consuming, not faster. The constraint is not human review capacity, but automated filter quality.

4. **Galileo AI (2025). "How to Evaluate LLMs: Metrics + Best Practices."** — Modern LLM evaluation combines automated metrics (cost-effective) with human-in-the-loop sampling (cost-efficient). Human review for 100% throughput is inefficient; sampling-based approaches are superior.

5. **Understanding Data (2024). "The Human Bottleneck Is a Quality Mechanism."** — Human review isn't a bottleneck; it's a quality mechanism. Removing it degrades quality faster than it increases throughput. The real constraint is the *quality-throughput trade-off*, not just human capacity.

6. **SuperAnnotate (2025). "LLM Evaluation Guide."** — Effective evaluation combines automated scoring (fast, cheap), heuristic filtering (medium cost), and human validation (expensive, high-confidence). Human review is the third tier, not the primary constraint; tiers 1-2 matter more for throughput.

### Strength of challenge: MODERATE

### Summary

The assumption that human review is the primary throughput constraint assumes that removing human review would increase throughput. But evidence shows that: (1) removing human review without improving automated filtering increases error rates faster than throughput gains, (2) human review quality is the real bottleneck, not human capacity, (3) automated evaluation alternatives (LLM metrics, heuristic filters) can reduce human review burden without sacrificing quality. For C2A2, the primary constraint may not be human review of agent outputs, but agent output quality (which determines review burden) and automated evaluation (which can reduce review demand).

### Specific risks for C2A2

1. **Optimizing wrong constraint**: C2A2 might focus on speeding up human review while ignoring automated evaluation, which is more cost-effective.
2. **Quality degradation**: Reducing human review burden without improving agents' output quality will increase error rates, not throughput.
3. **Automation paradox**: Better automated filtering might increase human review demand (reviewing false positives) rather than reducing it.
4. **Cascade from prior steps**: If agents (14a, 14b) produce poor-quality outputs, human reviewers can't compensate; the constraint is agent quality, not review capacity.

### Mitigations available

1. **Automated evaluation first**: Improve agents' outputs and automated filtering before relying on human review speed.
2. **Tiered evaluation**: Use automated scoring (fast), heuristic filters (medium), human validation (expensive). Optimize tier 1-2 before optimizing tier 3.
3. **Quality metrics**: Track error rates and false positive rates; don't optimize for review speed at the expense of quality.
4. **Constraint identification**: Empirically measure where the throughput bottleneck actually is (agent quality, automation, or human review); don't assume.
5. **Sampling-based review**: Use statistical sampling for human review; validate a representative subset rather than reviewing everything.

### Recommendation: CHALLENGED

The assumption that human review is the primary throughput constraint is not well-supported. The real constraint is likely agent output quality and automated evaluation effectiveness. Optimizing human review speed without addressing these will not improve overall throughput.

---

## STEELMAN

**Item:** ASSUMPTION-012

**Strongest counterargument:**

Human review is not the primary throughput constraint; it's a quality mechanism. If agents produce poor-quality outputs, human review cannot compensate; the constraint is agent quality. If automated filters generate excessive false positives, human review burden increases, not decreases. Modern approaches use tiered evaluation: automated metrics (fast, cost-effective), heuristic filtering (medium cost), human validation (expensive, high-confidence). Optimizing human review speed alone doesn't improve overall throughput; you must optimize the entire evaluation pipeline. Understanding Data shows that human review bottlenecks are often symptoms of upstream problems (poor automation, low agent quality), not the root cause.

**What would need to be true for C2A2 to be safe:**

1. Human review would need to be the actual bottleneck (not agent quality or automation).
2. Removing human review would improve throughput without degrading quality (it wouldn't).
3. Automated evaluation couldn't reduce human review burden (it can).

**How to test:**

1. Measure C2A2's actual bottleneck: profile where time/tokens are consumed (agent reasoning, automation, human review, or other).
2. Simulate removing human review; measure quality degradation vs. throughput improvement.
3. Measure false positive rates from automated filters; assess whether they increase human review burden.
4. Compare tiered evaluation (automated + sampling) against full human review on cost-effectiveness.

---

## SYSTEMIC-RISK-FLAG

**Date:** 2026-04-13

**Affected items:** ASSUMPTION-012, ASSUMPTION-013

**Common vulnerability:** Both assume that downstream quality filters (human review, cross-tradition signals) are reliable proxies for agent output quality. Both overlook that quality depends on upstream agent performance.

**Literature basis:**

- Asyncsquad Labs (2025) - bottleneck cascade
- DigitalOcean (2026) - automation alternatives
- Understanding Data (2024) - quality-throughput trade-off
- SuperAnnotate (2025) - tiered evaluation

**Risk level:** MODERATE

**Recommendation:** Before optimizing human review, profile C2A2's actual bottleneck. If agent quality or automation are the constraints, address those first. Use tiered evaluation (automated + sampling) rather than full human review to increase cost-efficiency.
