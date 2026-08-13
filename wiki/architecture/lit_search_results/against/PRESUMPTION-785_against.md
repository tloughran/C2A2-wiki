# PRESUMPTION-785 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-785

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-785

**Original statement:** That the absence of an identifiable attended session means no attended work occurred beyond what the vault records. *(REFLEXIVE — the item concerns the record from which the item itself was inferred.)*

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference; flagged REFLEXIVE)
- **Transform at each step:**
  - 14b: Inferred that the system treats the absence of a file-system trace of an attended session as evidence that no attended work occurred, and that a file-system trace is a systematically biased sample of intellectual work — biased against exactly the activity the project most wants to record; risk graded Medium.
  - 15b: Searched for literature challenging the inference — the evidential status of absent evidence, the two-sided noise profile of trace-derived provenance, and the boundary conditions of the invisible-work literature.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated or mis-scoped. Here the challenge is that absence of trace *is* evidence — graded, not null — and that trace-derived records are noisy in both directions rather than only under-counting.

### Challenging evidence found: Yes

### Sources

1. **Sober, E., 2009. "Absence of evidence and evidence of absence: evidential transitivity in connection with fossils, fishing, fine-tuning, and firing squads." *Philosophical Studies*.** — The formal treatment. Under the law of likelihood, absence of evidence *is* evidence of absence to some degree whenever the evidence would have been more probable had the hypothesis been true. This directly challenges the presumption's implicit framing: the inference from "no attended session found" to "probably no attended session" is not a fallacy, it is a likelihood judgement whose strength depends on detection probability. The correct correction is to state the detection probability, not to withdraw the inference.
2. **Strevens, M., 2009. "Objective Evidence and Absence: Comment on Sober." *Philosophical Studies* (strevens.org).** — A published commentary refining when absent-evidence reasoning is objectively licensed. Cited to show the framework is live and contested in its details, not to overturn Sober.
3. **"When does absence of evidence constitute evidence of absence?" (eScholarship qt9k15n0b0) and "More on the question 'When does absence of evidence constitute evidence of absence?' How Bayesian confirmation theory can logically support the answer," *Forensic Science International* (S0379073819302397).** — Applied treatments giving the operational criterion: absence is strongly informative where a thorough search would very probably have detected the thing, and weakly informative where it would not. This converts the item's binary worry into a measurable parameter.
4. **"From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces," 2026. arXiv:2603.07609.** — Reports that raw logs from creative work systems are "extremely noisy," with a single creative move generating dozens of system events including re-routing, cleanup routines and redundant metadata updates. This is a two-sided challenge to the presumption: trace-derived activity records do not only *miss* intellectual work, they also *inflate* it, so the direction of bias is not established by the fact that traces are proxies. (Note the direct link to PRESUMPTION-786 — the sign of the error is the question.)
5. **Provenance-reconstruction literature on incompleteness (e.g. "Reconstructing Data Provenance from Log Files"; "Capturing end-to-end provenance for machine learning pipelines," *Information Systems*, 2024).** — Documents that scavenged provenance is partial, low-fidelity and requires post-processing, and that coverage is fragmented across pipeline stages. Cited as the boundary condition rather than as a refutation: incompleteness is a measurable coverage property with known remedies, not an in-principle bias.
6. **Star, S.L., Strauss, A., 1999. "Layers of Silence, Arenas of Voice: The Ecology of Visible and Invisible Work." *Computer Supported Cooperative Work* 8(1–2):9–30.** — The canonical source *for* the item's position, cited here for its boundary conditions. Its central claim is that no work is inherently visible or invisible; visibility is a negotiated relation constituted by a selection of indicators. That framing challenges the item's phrasing — there is no fact of the matter about work that "occurred beyond what the vault records" independent of the indicator set — and its empirical setting is human organisational labour with political stakes about recognition and pay, which is not obviously the vault's situation.

### Strength of challenge: Moderate

### Summary

The item's worry is real but its logic is stronger than it needs to be and weaker than it claims. On the formal side, the inference it objects to is licensed: absence of evidence is evidence of absence in proportion to the probability that a search would have found the thing had it existed, so the vault's silence about attended sessions is genuinely informative, and how informative is a number that could be estimated rather than a fallacy to be flagged. On the empirical side, the assumption that trace-derived records are biased *against* intellectual work is asserted, not shown, and the nearest recent evidence points the other way as often as not: raw system traces are documented as noisy in the inflationary direction, with single conceptual moves generating dozens of low-level events, so a trace can over-represent activity as readily as under-represent it. The provenance literature confirms that scavenged records are incomplete, but treats incompleteness as a coverage property with known instrumentation remedies rather than as a structural bias. Finally, the invisible-work literature that most supports the item also undercuts its phrasing: Star and Strauss argue that visibility is constituted by the indicator set rather than being a property work has independently, which means "attended work occurred beyond what the vault records" is not a well-formed factual claim until the indicator set is specified. Their setting — contested recognition of human labour — also does not obviously transfer.

### Specific risks

If the presumption is adopted at full strength, the specific danger is unfalsifiability: any inconvenient absence can be attributed to invisible work, and the register acquires a general-purpose excuse that cannot be checked. Given the item is REFLEXIVE, that excuse would be available to the detection pipeline about its own outputs, which is the worst place for it. If it is dismissed, the risk 14b names stands: an activity metric derived from one channel gets read as a measure of the underlying activity — the exact defect PREMISE-140 already covers — and the project's record of its own most valued work is silently truncated.

### Mitigations available

(a) State the detection probability rather than the inference. "No attended session found; the vault would record such a session with probability p" makes the absence usable and the uncertainty explicit. Even a rough p converts the worry into information. (b) Name the metric by its channel, per PREMISE-140 — "no attended session in the file-system trace," never "no attended work." This closes most of the item at zero cost. (c) Establish the bias direction empirically rather than assuming it: take a period where attended work is independently known to have occurred and measure what the trace shows, in both directions. (d) Add a cheap out-of-band marker — a one-line session log written by the attendant — which converts a scavenged proxy into a direct record for the specific activity class that matters most.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-785

**Strongest counterargument:** The inference the item objects to is valid, and the objection substitutes an unfalsifiable posture for a measurable one. Under the law of likelihood, an absent observation confirms absence exactly to the degree that the observation would have been expected under presence; the vault's silence about attended sessions is therefore evidence, and the honest response is to estimate how good a detector the vault is, not to declare the inference unsafe. The item's stronger claim — that the trace is biased *against* the very work the project cares about — is an empirical assertion with no measurement behind it, and recent work on reconstructing workflows from raw traces reports the opposite failure at least as prominently: traces are extremely noisy and a single conceptual move can generate dozens of events, so trace-derived activity can be inflated as easily as suppressed. Even the invisible-work literature that seems to underwrite the item argues that visibility is constituted by the choice of indicators rather than being something work has in itself, which makes "work that occurred beyond what the vault records" ill-formed until the indicators are named — and its empirical setting is the contested recognition of human labour, a context with political stakes the vault does not obviously share. Adopted at full strength on a reflexive item, this presumption gives the detection pipeline a permanent, uncheckable explanation for anything missing from its own record.

**What would need to be true for C2A2 to be safe:** Every activity claim must be named by its channel, and any inference from absence must carry an explicit detection-probability estimate. Given those, the vault's silence is a legitimate, bounded piece of evidence and the presumption's hazard closes. If neither is present, the worry is live — but as a naming and calibration defect, which PREMISE-140 already covers, rather than as a structural bias.

**How to test:** Take a bounded window in which attended work is independently known to have happened, and score the trace against it: how many attended sessions leave a detectable signature, and how many trace signatures correspond to no attended work. Those two numbers give the detection probability and the false-signature rate, which is exactly the pair the item's argument needs and does not supply. The result also settles the direction of bias empirically — and it is worth noting in advance that the answer could go either way, which is itself the point.

---

## Search scope

Moderate. Query families executed: absence-of-evidence reasoning in Bayesian and forensic contexts, including a published commentary; provenance reconstruction from logs and its documented incompleteness; invisible work in CSCW; telemetry-derived activity metrics and their known distortions (Goodhart-type effects, gaming, poor construct validity). Not searched: the survivorship-bias literature proper, and the digital-humanities work on archival silence, both named in the item's search strategy. Reflexive caveat, as with PRESUMPTION-777: this search was conducted through a channel returning snippets rather than verified full texts, so two sources are cited with unconfirmed detail and marked. Broader search recommended.
