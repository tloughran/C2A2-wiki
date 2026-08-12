# PRESUMPTION-769 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-769

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-769

**Original statement:** That a document's own account of its provenance is evidence about the document — three false provenance claims found in one day.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from three same-day false provenance claims that self-reported provenance is being treated as evidence; risk graded High.
  - 15b: Searched for challenging literature on provenance models that treat provenance as assertion, and on professional evidence hierarchies that grade rather than exclude self-generated evidence.
- **Current status:** CHALLENGED

**What is being challenged:** the binary. The presumption's implied conclusion is that self-reported provenance is *not* evidence. Both the provenance-standards literature and the auditing standards treat asserted, entity-generated evidence as *lower-reliability* evidence requiring corroboration — not as non-evidence.

### Challenging evidence found: Yes

### Sources

1. **W3C PROV family of specifications (PROV-DM, PROV-O, PROV-N), W3C; described in "The W3C PROV family of specifications for modelling provenance metadata," *IEEE TKDE* — [journal attribution unverified; the specifications themselves and their assertional semantics are verified].** — PROV-DM defines provenance explicitly as "a record of assertions" about the activities and entities that produced an artefact. The international standard for provenance is built on asserted provenance, and deliberately leaves verification semantics to the consuming domain. This directly challenges the claim that asserted provenance is not evidence: the standard's whole purpose is to make such assertions interoperable and usable.
2. **ISA 500, *Audit Evidence*, IAASB (International Standard on Auditing 500).** — Establishes a graded reliability hierarchy: external sources are generally more reliable than internal, auditor-generated more reliable than entity-generated, documentary more reliable than oral, originals more reliable than copies. Entity-generated evidence is explicitly *used*, subject to the auditor evaluating its accuracy and completeness and corroborating across sources. The profession whose entire method is scepticism about self-report does not exclude self-report; it discounts and corroborates it.
3. **ISA 500 on inconsistency: where evidence from one source conflicts with another, the auditor performs additional procedures to resolve the inconsistency.** — This is the operative pattern for the three false claims: their discovery is itself the corroboration mechanism working, and it yields a base rate, which is usable calibration information rather than grounds for discarding the class.
4. **Decision-provenance and agent-claim-verification literature (arXiv:1804.05741, "Decision Provenance: Harnessing data flow for accountable systems"; arXiv:2605.20312, "Pramana: A Protocol-Layer Treatment of Claim Verification in Autonomous Agent Networks") — [second citation unverified beyond title/ID from search snippet].** — Both frame the problem as layering verification *onto* asserted claims rather than replacing assertion with unforgeable metadata, consistent with a discount-and-corroborate posture.

### Strength of challenge: Moderate

### Summary

The finding is sound and the inference is too strong. The international provenance standard treats provenance as assertion by design, and the auditing standards — the most developed professional apparatus for reasoning about self-interested self-report — grade evidence by reliability rather than admitting or excluding it. On that framework, a document's own account of its provenance is low-reliability internal evidence: usable, requiring corroboration, and carrying a discount that should be stated. Three false claims discovered in one day is a data point about the size of that discount, and is precisely the outcome ISA 500 anticipates when it requires additional procedures upon inconsistency; it is evidence that corroboration is working, not that the evidence class is void. The presumption's practical force survives in a narrower form: C2A2 currently applies no visible discount and has no corroboration requirement, so self-reported provenance is being consumed at face value. That is a real gap. But the remedy the literature supports is a stated reliability grade plus a corroboration rule, not the removal of asserted provenance from the evidence base — which, given that unforgeable provenance is unavailable for most of these artefacts, would leave nothing.

### Specific risks

If the strong reading is adopted, C2A2 discards the only provenance information it has for a large body of documents and gains nothing, since no unforgeable substitute exists for them; the practical outcome is provenance nihilism, where nothing is traceable because nothing is trusted. If the finding is dismissed, false provenance claims continue to propagate at an unmeasured rate, and because provenance claims are load-bearing for the chain-of-custody the whole register depends on, a false claim contaminates every downstream item that cited it. The three known cases give a floor, not an estimate, on that rate.

### Mitigations available

(a) Attach a reliability grade to every provenance claim, following the ISA 500 hierarchy: self-asserted, corroborated-by-one-independent-source, or machine-attested. (b) Require corroboration for provenance claims that gate irreversible action, and only those — this bounds the cost. (c) Where machine attestation is cheap (filesystem timestamps, session ids, content hashes), prefer it and mark the claim as attested; this converts a subset of claims to the high-reliability tier at low cost. (d) Measure the base rate: sample provenance claims and verify, so the discount is empirical rather than notional.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-769

**Strongest counterargument:** An auditor would find the presumption's conclusion both too strong and self-defeating. The profession that exists specifically to evaluate self-interested self-report does not exclude entity-generated evidence; ISA 500 grades it as less reliable and requires corroboration and resolution of inconsistencies, and that graded posture is what makes assurance possible at all. The W3C's provenance standard makes the same choice at the technical level: provenance *is* a record of assertions, with trust deliberately layered on top, because unforgeable provenance is unavailable for most real artefacts. If C2A2 adopts the rule that a document's own account of its provenance is not evidence, it does not become more rigorous — it loses the only provenance signal most of its corpus has, and the chain-of-custody the register depends on becomes unreconstructable rather than merely discounted. The three false claims are, on this reading, the corroboration process functioning as designed and producing a measurable base rate, which is more valuable than the categorical exclusion the presumption implies.

**What would need to be true for C2A2 to be safe:** Every provenance claim must carry an explicit reliability tier, corroboration must be mandatory for the subset of claims that gate irreversible action, and the base rate of false claims must be sampled and published so the discount applied is empirical. Under those conditions asserted provenance is safe to use and the presumption's hazard is bounded.

**How to test:** Draw a random sample of provenance claims across the corpus and attempt independent verification of each (filesystem metadata, session records, content hashes). The resulting false-claim rate is the discount. Then check whether any *gating* decision in the register rests on an unverified claim — that intersection is the actual exposure, and it may be much smaller or much larger than three.

---

## Search scope

Moderate. Query families executed: W3C PROV assertional semantics; audit evidence hierarchy under ISA 500; decision provenance in autonomous systems. Not searched: the tamper-evident logging and transparency-log literature (Merkle-based audit trails), which would sharpen the machine-attestation mitigation. Broader search recommended for the mitigation design, not for the direction of the challenge.
