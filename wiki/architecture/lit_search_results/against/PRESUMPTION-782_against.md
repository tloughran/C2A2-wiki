# PRESUMPTION-782 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-782

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-782

**Original statement:** That an upstream key is a record rather than a claim — a wrong `summa_ref` made thirteen files' frontmatter, commentary and every static check mutually consistent and jointly wrong.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from a single wrong `summa_ref` propagating into thirteen files' frontmatter and commentary such that every nominally independent static check agreed, that the system presumes an upstream key is a record rather than an unverified claim, and that agreement among derived artefacts constitutes corroboration; risk graded High.
  - 15b: Searched for literature challenging the inference — the common-cause-failure and design-diversity literature, and the architectural case for a single authoritative key.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated, boundary-limited, or its remedy harmful. Here the core claim survives — the relevant literature largely agrees with it — but the *remedy* it implies (redundant or diverse derivation of upstream keys) has a documented ceiling and a documented backfire mode.

### Challenging evidence found: Partial

### Sources

1. **Knight, J.C., Leveson, N.G., 1986. "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming." *IEEE Transactions on Software Engineering* SE-12(1).** — Twenty-seven independently written versions of one specification, one million tests: coincident failures occurred substantially more often than an independence model predicts. Cited here *against the remedy*: independent re-derivation does not deliver independent failure. If the system's response to a shared upstream key is "derive it twice, independently," the canonical experiment says the two derivations will still fail together more often than the arithmetic suggests.
2. **Littlewood, B., Miller, D., 1989. "Conceptual Modelling of Coincident Failures in Multiversion Software." *IEEE Transactions on Software Engineering* 15(12):1596–1614.** — Provides the formal model and the constructive result: *forced* diversity (deliberately different methodologies, not merely different authors) can reduce correlated failure below the naive-independence baseline in some regimes. This is the boundary condition on the challenge — diversity is a design lever with an achievable but bounded payoff, not a free property of "using more than one check."
3. **Knight, J.C., Leveson, N.G. "A Reply to the Criticisms of the Knight & Leveson Experiment" (sunnyday.mit.edu/critics.pdf).** — The experiment has a critical literature; the reply documents and rebuts it. Cited for honesty about the strength of the underlying result.
4. **"N-Version Programming with Coding Agents," 2026. arXiv:2606.20158 (ASSERT-KTH; replication artefact at github.com/ASSERT-KTH/Knight-Leveson-Redux).** — Direct transfer of the Knight–Leveson design to AI coding agents: across 48 admitted implementations, 429 coincident-failure cases against 115.36 predicted by the independence model. Highly relevant here because C2A2's "nominally independent checks" are agent-authored, and this is the closest available evidence about whether the 1986 result transfers to that population. It does — which strengthens 14b's claim about common-cause failure and simultaneously weakens any remedy based on agent-authored redundancy.
5. **Normalisation / single-source-of-truth practice (standard database design literature; consolidated practitioner sources 2024–2026).** — The architectural counterpoint: storing a value once is what *prevents* update anomalies, and redundancy is known to produce divergence proportional to the number of duplicated occurrences. The recommended pattern is not to duplicate the authoritative value but to keep the canonical version upstream and reconcile derived copies against it during load. This challenges an over-broad reading of the item: the fault is not that `summa_ref` is a single upstream key, it is that the key was never validated against an external referent at ingest.

### Strength of challenge: Moderate

### Summary

Most of what the literature says here agrees with 14b, and that should be said first: common-cause failure among nominally independent checks is the best-documented result in this area, agreement among derived artefacts is not corroboration, and the 2026 replication indicates the effect survives transfer from human to agent authorship at roughly the same magnitude. The challenge is therefore not to the diagnosis but to two things around it. First, scope: the presumption's framing invites the conclusion that single upstream keys are the error, when the design literature says the opposite — a single authoritative value is what prevents divergence, and the alternative (redundant independently maintained keys) trades a correlated-error failure for an inconsistency failure that is more frequent and harder to detect. The fault is located at the ingest boundary, where a claim becomes a record without ever meeting an external referent, not in the downstream architecture. Second, remedy: if the response is to re-derive keys with additional agent-run checks, Knight–Leveson and its 2026 agent replication predict that the added checks will fail together with the originals far more often than an independence model implies, producing exactly the false confidence the item warns against, one layer out. Littlewood and Miller give the constructive escape — diversity must be *forced* and methodological, not merely multiple — and that is a sharper design instruction than "add checks."

### Specific risks

If the presumption drives a redundancy remedy, the concrete risk is a system with more checks, higher cost, and a correlated-failure profile barely better than before, plus a stronger and now unwarranted belief in its own verification. If it drives distrust of single-source-of-truth architecture, the risk is duplicated keys drifting apart, which is the failure mode the normalisation literature exists to prevent. If it is dismissed, the original hazard stands and is severe: any single wrong upstream value silently makes an entire derived population self-consistent and wrong, and no amount of internal cross-checking can detect it, because every check is downstream of the fault.

### Mitigations available

(a) Validate at ingest against an external referent — the one place a claim can become a record. For `summa_ref` this means checking the key against the source corpus once, at the boundary, rather than checking derived files against each other thirteen times. (b) Mark keys by provenance class: EXTERNALLY-VERIFIED versus ASSERTED, so that downstream agreement is interpreted against the right prior. (c) Where redundancy is used, force methodological diversity per Littlewood and Miller — a check that reads the source corpus directly is diverse from one that reads frontmatter; two checks that both read frontmatter are not, regardless of who wrote them. (d) Treat agreement among derived artefacts as evidence about *propagation integrity* (no transcription errors downstream) and explicitly not as evidence about the key's correctness — which is a real, if narrow, thing the agreement does establish.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-782

**Strongest counterargument:** The diagnosis is right and the architectural inference drawn from it is wrong. Nothing in this incident indicts having one authoritative `summa_ref`; having one is what stops thirteen files from carrying thirteen slightly different values, which is the more common and more insidious failure. What the incident indicts is a boundary with no validation on it: a value entered the system as a claim and was thereafter treated as a record, and no check anywhere in the pipeline ever compared it to anything outside the pipeline. That is a one-place defect with a one-place fix, and locating it in the general relationship between keys and derived artefacts makes it look structural and expensive when it is neither. The remedy the item's framing suggests is also actively dangerous. Knight and Leveson showed in 1986 that independently developed versions fail together far more than independence predicts, the result has withstood a critical literature, and a 2026 replication using coding agents found 429 coincident failures where the independence model predicted 115 — meaning that adding agent-authored cross-checks to catch this class of fault will buy far less than it appears to. Littlewood and Miller's constructive result is the only escape and it is specific: diversity has to be forced and methodological. "More checks" is not a remedy; "one check that reads a different source" is.

**What would need to be true for C2A2 to be safe:** Every key that a derived population depends on must be validated once against a referent outside that population, at ingest, and must carry a mark saying whether it was. Given that, the single-source architecture is a strength rather than an exposure, and downstream agreement can be read for what it is — propagation integrity — without being mistaken for corroboration.

**How to test:** Enumerate the upstream keys on which more than three derived artefacts depend. For each, determine whether any check anywhere in the pipeline compares it to something outside the derived population. The count of keys for which the answer is no is the exposure, and it is measurable today. A second, sharper test: deliberately corrupt one such key in a scratch copy and run the full static check suite. The number of checks that pass is the empirical measure of how much of the system's verification is downstream of a single claim — and the Knight–Leveson result predicts that number will be uncomfortably close to all of them.

---

## Search scope

Moderate. Query families executed: N-version programming and the independence assumption, including its critical literature and a 2026 agent-based replication; conceptual modelling of coincident failure and forced diversity; normalisation versus denormalisation and single-source-of-truth trade-offs. The last family returned mostly practitioner material and is marked as such. Not searched: the fault-tree and common-cause-failure literature from reliability engineering proper (beta-factor models, IEC 61508 treatment of CCF), which is the formal home of this problem and would likely sharpen both the diagnosis and the mitigation set. Broader search recommended.
