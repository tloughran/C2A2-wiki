# ASSUMPTION-968 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-968

**Date searched:** 2026-08-12

**Original item:** ASSUMPTION-968

**Original statement:** That centralized coordination yields +80% on parallelizable work and -70% on sequential work, and that C2A2's 14 → 15a/b → 15c → 15d pipeline is sequential.

### PROVENANCE

- **Origin:** 14a
- **Chain:** [14a → 15b]
- **Item type:** ASSUMPTION (stated)
- **Transform at each step:**
  - 14a: Extracted as a stated quantitative claim imported from the Google/MIT agent-scaling study, together with a classification of C2A2's own pipeline as sequential.
  - 15b: Searched for the primary source and for challenges to both the figures and the classification.
- **Current status:** CHALLENGED

**What is being challenged:** both conjuncts. The figures are quoted as point estimates when the source reports a range and the point values attach to specific benchmarks; and the study's "sequential" category denotes sequential *reasoning within a task*, not a staged pipeline of heterogeneous roles with centralised verification — which is what C2A2 has.

### Challenging evidence found: Yes

### Sources

1. **"Towards a Science of Scaling Agent Systems." arXiv:2512.08296 (MIT Media Lab with Google; see also research.google/blog, "Towards a science of scaling agent systems: When and why agent systems work," and the MIT Media Lab project page).** — The primary source. Confirms the study exists and reports: +80.8/80.9% for centralised coordination on parallelizable tasks (financial reasoning), and degradation of **39–70%** across multi-agent architectures on sequential reasoning tasks, with −70.0% attaching specifically to *sequential planning* (PlanCraft). Also reports the predictive model achieving ~87% accuracy on held-out configurations. The assumption quotes the extreme of the degradation range as if it were the central estimate.
2. **Same source — configuration count discrepancy.** — Google's research blog and secondary coverage describe **180** configurations across five architecture types and three model families; other summaries of the paper describe **260** configurations across **six** benchmarks (four named: Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench) — [the 260/six figure is unverified, from a secondary summary]. The assumption's "180-configuration study" may be citing the blog-post framing rather than the paper's final experimental scope; either way the citation is unstable and should be pinned to the arXiv version.
3. **Same source — the error-amplification finding.** — Independent multi-agent systems amplified errors 17.2× relative to single-agent baselines, while **centralised** coordination contained amplification to 4.4×, and "architectures without centralized verification tend to propagate errors more than those with centralized coordination." This is the study's own result and it *favours* C2A2's orchestrated topology, cutting against the inference the assumption draws.
4. **Same source — boundary conditions.** — Reported qualifiers include diminishing returns once the single-agent baseline is already strong, and multi-agent overhead on *tool-heavy* tasks. Both are scope conditions on the +80% figure that the assumption does not carry, and the second is directly relevant: C2A2's stages are tool-heavy (file reads, web search), which is the regime the paper flags as adverse.
5. **Decentralised-vs-centralised differential: decentralised coordination excelled on dynamic web navigation (+9.2% vs +0.2%).** — Establishes that the optimal topology is task-property-dependent within the same study, so a single pair of figures cannot be applied to a heterogeneous pipeline as a whole.

### Strength of challenge: Strong

### Summary

The primary source is real and largely as described, and that is what makes the challenge sharp rather than speculative. Three problems. First, the −70% figure is the worst case of a 39–70% band and is attached to sequential *planning* on PlanCraft; quoting it as the sequential-work coefficient overstates the expected effect by up to a factor of nearly two. Second, the construct does not transfer: the study's sequential category concerns decomposing a single chain of dependent reasoning across agents, whereas C2A2's 14 → 15a/b → 15c → 15d structure is a staged pipeline of *heterogeneous roles* with distinct outputs and a coordinating orchestrator — closer to the paper's centralised-coordination arm than to its sequential-reasoning benchmark. Third, and most damaging to the inference, the paper's own headline safety result is that centralised coordination *reduces* error amplification from 17.2× to 4.4× and that architectures lacking centralised verification propagate errors more; applied to C2A2 this supports the current topology rather than indicting it. There is also a live citation problem: the configuration count differs between the Google blog framing (180) and paper summaries (260 across six benchmarks), so the assumption's own reference should be pinned to arXiv:2512.08296 before any figure is relied on. Separately, the study's caution about tool-heavy tasks incurring multi-agent overhead is the one finding that does plausibly transfer to C2A2 and it is the one the assumption omits.

### Specific risks

If the assumption is acted on as stated, C2A2 may collapse or serialise a pipeline whose staged structure the source study would actually endorse, discarding the centralised-verification property the same study credits with a ~4× reduction in error amplification. The concrete harm is replacing a topology with contained error propagation with one the paper measures at 17.2× amplification, in pursuit of a −70% penalty that the paper does not predict for this task class. If the assumption is dismissed entirely, the genuinely transferable caution — multi-agent overhead on tool-heavy work, and diminishing returns when the single-agent baseline is already strong — goes unheeded.

### Mitigations available

(a) Pin the citation to arXiv:2512.08296 and re-extract the figures with their benchmarks and ranges attached; the assumption should read "39–70% on sequential *reasoning* (PlanCraft: −70.0%)" not "−70% on sequential work." (b) Apply the paper's own predictive model rather than its headline coefficients: it reports ~87% accuracy from measurable task properties (tool count, decomposability), so C2A2 can classify each stage instead of classifying the pipeline. (c) Classify per stage: 15a/15b are parallelizable by construction (two independent searchers on the same items) and 15c/15d are aggregation and reconciliation, which is the centralised-coordination pattern — the pipeline is probably a mixture, not a sequence. (d) Treat the tool-heaviness caution as the actionable finding and measure per-stage tool counts.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** ASSUMPTION-968

**Strongest counterargument:** The assumption imports two numbers and a classification from a real study, and all three fail on inspection. The −70% is the floor of a 39–70% band measured on sequential *planning* in PlanCraft, not a general coefficient for sequential work; the +80% is measured on financial-reasoning decomposition and is qualified in the paper by diminishing returns against strong single-agent baselines and by overhead on tool-heavy tasks, both of which describe C2A2's stages. Most importantly the classification is wrong in a way that inverts the conclusion: the study's sequential arm is about splitting one dependent reasoning chain across agents, while C2A2 runs heterogeneous roles with distinct products through an orchestrator, which is the study's centralised-coordination arm — the very arm the paper credits with cutting error amplification from 17.2× to 4.4× and with the presence of centralised verification that limits propagation. Acting on the assumption as written would therefore mean dismantling the property the cited evidence says to keep. And because the assumption's own citation is unstable — 180 configurations per the Google blog versus 260 across six benchmarks per paper summaries — the register is currently carrying a quantitative claim whose source scope it has not pinned down.

**What would need to be true for C2A2 to be safe:** The figures must be re-cited from arXiv:2512.08296 with benchmarks and ranges intact; the pipeline must be classified per stage using the paper's own measurable task properties (tool count, decomposability) rather than labelled sequential as a whole; and any topology change must preserve centralised verification, which the source identifies as the mechanism containing error amplification.

**How to test:** Run the paper's own classifier logic on each C2A2 stage: count tools per stage and score decomposability. The prediction is that 15a/15b score as parallelizable (they are, by construction, two independent agents on an identical item list) and that 15c/15d score as centralised aggregation. If so, the sequential classification is falsified directly. Then, empirically: run one item batch through the current staged topology and through a single-agent-does-everything alternative, and compare error rates and coverage. The paper's error-amplification result predicts the staged version wins; that is a testable and cheap discriminating experiment.

---

## Search scope

Moderate-to-good on the primary source — the study was located, its identifiers verified, and its figures, benchmarks, and boundary conditions extracted from the abstract, the Google Research blog, and secondary summaries. Not done: reading the full paper text, which is required to resolve the 180-versus-260 configuration discrepancy and to confirm the operational definition of "sequential" that the challenge turns on. No replications of the study were found; given a December 2025 arXiv date, independent replication may not yet exist, so the +80/−70 figures rest on a single study regardless of how they are quoted. Full-text review strongly recommended before this item is reconciled.
