# PRESUMPTION-775 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-775

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-775

**Original statement:** That surfacing a defect is sufficient because a later reader will act on it — the seventh recurrence of a retracted trap and the third pass of a known-truncated file, same day.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from a seventh recurrence and a third repeat pass on the same day that the system relies on a later reader acting on surfaced defects; risk graded High.
  - 15b: Searched for challenging literature on defect-backlog decay, deliberate triage, and the empirical determinants of whether reported findings get acted on.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** the norm that a surfaced defect ought to be acted on. Empirically, most reported defects are never fixed and much of that is deliberate, rational triage. The challenge does not extend to the retracted-trap half, where the literature offers no such excuse.

### Challenging evidence found: Partial

### Sources

1. **Guo, P.J. et al., 2010. "Characterizing and Predicting Which Bugs Get Fixed." ICSE 2010 (Microsoft Research).** — Establishes empirically that fix probability is a function of reporter, component, and process factors rather than of defect validity, and that reassignment history materially changes outcomes. Challenges the presumption's premise that a surfaced defect has a default expectation of being acted on: the base rate is governed by process, not by the finding's merit.
2. **"Understanding the triaging and fixing processes of long lived bugs." *Information and Software Technology*, 2015 (S0950584915000531).** — Across seven open-source projects, a considerable population of long-lived bugs persists in every system, delayed for reasons including long assignment times and unrecognised importance, with roughly 40% of long-lived bugs requiring only small fixes. Reported figures include ~20% of all bugs in the studied repository still open, and 68.9% of Mozilla bug reports classified as open — [percentages unverified — from search snippet]. Establishes that reported-not-fixed is the normal steady state, not a pathology of this system.
3. **Sadowski, C. et al., 2015. "Tricorder: Building a Program Analysis Ecosystem." ICSE 2015 (Google).** — The operative finding for remedy design: developer trust collapses above roughly a 10% false-positive rate, and the intervention that works is surfacing findings *at the point of change* with suggested fixes co-located, not increasing the volume or urgency of reports. Challenges the presumption's implicit remedy (make readers act) and substitutes a different one (change where and when the finding appears).
4. **"Mitigating False Positive Static Analysis Warnings: Progress, Challenges, and Opportunities." *IEEE TSE*, 2023 (doi:10.1109/TSE.2023.3329667).** — Documents alert fatigue as the mechanism by which high report volume reduces action, and notes that "a false positive report is any report that they did not want to see" from the user's perspective — i.e., non-action is often a considered judgement rather than neglect.
5. **Bug-triage practice taxonomy — "Defects to Fix Now / Defects to Fix Later / Defects We'll Never Fix" — [unverified — practitioner source from search snippet].** — The third category is standard and legitimate; its existence is a direct challenge to treating any recurrence count as automatically indicting.

### Strength of challenge: Moderate

### Summary

The item bundles two findings with different standing under the literature. On the general claim — that surfacing is treated as sufficient — the empirical record challenges the presumption's baseline: most reported defects are never fixed, a large fraction of open items are deliberately deprioritised, and the software-engineering response has not been to demand that readers act but to change *where* findings appear so that acting is cheap at the moment of relevance. Under that framing, seven recurrences of a surfaced defect can be a correct triage outcome, and the useful remedy is placement, not exhortation. On the retracted-trap half, the challenge does not hold. A retraction is not a low-priority defect report; it is a withdrawal of a conclusion, and continued consumption of retracted material is a correctness propagation failure rather than a triage decision — the retraction-citation literature already cited in the register's 2026-08-04 systemic flag (Hsiao & Schneider, 2021) establishes that withdrawals do not propagate to marks already issued. Likewise a known-truncated file passed a third time is not deprioritisation; it is a wasted run producing a conclusion from incomplete input, which has a cost the triage frame does not cover. So the presumption is over-general but not wrong where it matters most.

### Specific risks

If the general framing is adopted, C2A2 may adopt an act-on-every-finding policy, which the alert-fatigue literature predicts will raise volume, lower trust, and reduce the action rate on the findings that matter — the opposite of the intent. If the challenge is over-applied and both halves are dismissed as triage, then retracted conclusions continue to be consumed and truncated files continue to be processed, both of which produce silently wrong outputs rather than merely deferred fixes.

### Mitigations available

(a) Split the classes explicitly: RETRACTION and INPUT-INVALID are not defect reports and must be enforced as blocking preconditions at the point of consumption, not surfaced for a later reader. This is the Tricorder placement lesson applied to the half of the item that needs it. (b) For genuine defect reports, adopt point-of-change surfacing with a false-positive budget, and accept a nonzero never-fixed population as normal. (c) Maintain a retraction and known-bad-input registry that consuming code checks automatically, so recurrence is structurally impossible rather than dependent on memory. (d) Track recurrence counts per finding and escalate on recurrence rather than on age — recurrence is the signal the triage literature agrees is not explainable as deprioritisation.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-775

**Strongest counterargument:** The empirical software-engineering record says the presumption's baseline expectation is unrealistic and its implied remedy counterproductive. Most reported defects are never fixed — the studied populations show large standing open fractions — and this is substantially deliberate: triage exists, "defects we'll never fix" is a legitimate category, and from the user's perspective a finding they did not want to see is a false positive regardless of its technical validity. The intervention that has actually worked at scale is Google's: hold the false-positive rate under about 10% and move the finding to the point of change with a co-located fix, because trust and placement determine action, not urgency. Demanding that later readers act on surfaced defects raises volume and erodes the trust that makes action possible. Where the presumption survives is narrower and stronger than it states: a retraction and a known-truncated input are not defect reports at all, and treating them as items in a queue that a reader may reasonably deprioritise is a category error — those must be blocking preconditions enforced by machine at the moment of consumption, which removes the dependence on a later reader entirely.

**What would need to be true for C2A2 to be safe:** Retractions and known-bad inputs must be machine-enforced preconditions checked at consumption time, with no reliance on reader memory. Ordinary defect findings must be surfaced at the point of change under a false-positive budget, with a nonzero never-fixed population accepted and recurrence — not age — used as the escalation trigger.

**How to test:** Instrument a retraction registry and a known-bad-input registry and make one consuming path check them; then attempt to re-consume the retracted trap and the truncated file. If the path blocks, the structural fix works and the general triage challenge can be accepted for the remainder. Separately, measure the action rate on surfaced findings as a function of where they were surfaced; if point-of-change findings are acted on materially more often than register-only findings, the placement remedy is validated and the exhortation remedy can be dropped.

---

## Search scope

Moderate. Query families executed: bug-fix prediction and long-lived-bug triage; static-analysis false positives and alert fatigue. Not searched: the shift-handover and institutional-memory literature (clinical handoff protocols) named in the item's search strategy, which is the most direct analogue for agent-to-agent memory transfer and should be added. Broader search recommended.
