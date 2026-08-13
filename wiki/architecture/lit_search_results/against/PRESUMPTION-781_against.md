# PRESUMPTION-781 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-781

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-781

**Original statement:** That entering something in a register constrains what is done next — PREMISE-107 and PREMISE-110 each prescribed the exact remedy the pipeline reinvented weeks later, and the minting agents do not read the register.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from two premises that prescribed remedies the pipeline independently re-derived weeks later while the minting agents never read the register, that the system presumes a written record has downstream force; residual and sharper claim is that a record with no specified reader has none, and that this is the default rather than a failure mode. Risk graded Critical.
  - 15b: Searched for literature challenging the inference — evidence that written protocols measurably change action, transactive memory research, and the costs of mandating consultation.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated or mis-scoped — specifically, that the claim "a written record has no downstream force by default" is contradicted by the best-evidenced case of a written record changing behaviour, and that the mechanism the counterexample reveals narrows the presumption rather than refuting it.

### Challenging evidence found: Yes

### Sources

1. **Haynes, A.B. et al., 2009. "A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population." *New England Journal of Medicine* 360:491–499.** — The strongest available counterexample. A 19-item written artefact, deployed across eight hospitals on four continents, was followed by 30-day mortality falling from 1.5% to 0.8% and any-complication rate from 11% to 7%. A written record demonstrably constrained what was done next, in a domain with high autonomy, high expertise and strong resistance to procedural imposition. This is a direct empirical challenge to the presumption stated generally.
2. **WHO *Guidelines for Safe Surgery* (2009) and subsequent national implementations (e.g. the Scottish programme; Madagascar countrywide evaluation, PMC5798831).** — Replication at national scale, which addresses the scale-failure objection: the effect is not confined to the original eight sites. Cited to establish that the mechanism transfers.
3. **Wegner, D., 1987 (transactive memory); Lewis, K., 2003, *Journal of Applied Psychology* / 2004, *Management Science* (TMS measurement and performance); and subsequent TMS–performance studies including trauma-team work in *Organization Science* (2024).** — Establishes the actual mechanism: what makes distributed knowledge usable is not the record but the *directory* — meta-knowledge of who knows what, plus credibility and coordination. Teams with stronger transactive memory systems show measurably better performance (e.g. shorter ICU and hospital stays for trauma patients). This challenges the presumption's framing: the missing ingredient is a directory and a retrieval trigger, not the record's force per se.
4. **Ancker, J.S. et al., 2017. "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system." *BMC Medical Informatics and Decision Making* 17:36.** — Bears on the implied remedy. Reminder acceptance fell about 30% per additional reminder per encounter and 10% per five-percentage-point increase in repeated reminders. Systematic reviews of computerised order entry report override rates of 49–96%. Mandating that minting agents read a growing register is, structurally, this intervention, and the literature predicts consultation rates will fall as the register grows.
5. **Google Cloud Architecture Center, "Architecture decision records overview," and related ADR guidance.** — Practitioner guidance is explicit that records must be scoped and lightweight or they accumulate unread; "start small… which helps prevent documentation fatigue." Cited as the design-side statement of the same constraint.

### Strength of challenge: Moderate

### Summary

The presumption as written — that a register does not constrain subsequent action, and that this is the default — is contradicted by the single best-evidenced case in the literature. The WHO surgical safety checklist is a written register of required steps, deployed into a high-autonomy expert domain that had every cultural reason to ignore it, and its introduction was followed by roughly a one-third reduction in death and major complications, replicated at national scale. Written artefacts can and do constrain action. But the counterexample also shows *why*, and the mechanism narrows the presumption rather than dissolving it: the checklist is bound to three specific time-bound trigger points (before induction, before incision, before the patient leaves), each with a named reader and a moment of forced consultation. It is not consulted because it exists; it is consulted because the workflow stops until it is. The transactive-memory literature makes the same point structurally — distributed knowledge becomes usable through a directory and a retrieval process, not through storage. So 14b's residual claim, that a record with no specified reader has no downstream force, is largely *supported* by the mechanism of the counterexample even as the general claim is refuted by its outcome. What is genuinely challenged is the word "default" and the Critical grading: the default is not inertness, it is inertness-absent-a-trigger, and triggers are cheap to install. Against the remedy, the alert-fatigue evidence is sharp: a general instruction to read the register will decay with register size, and will produce a false record of consultation.

### Specific risks

If the presumption is adopted at full strength, the natural conclusion — registers are useless — would license abandoning the premise register, which is the wrong lesson from a case whose actual reading is "bind the register to a trigger." If it is adopted via a blanket "read the register first" instruction, the predicted failure is override behaviour: agents will assert consultation without performing it, and the system will then have a documented control that certifies without examining, the fail-open pattern PREMISE-110 already names. If the finding is dismissed, the observed failure recurs: remedies already written down are independently re-derived weeks later at full cost, and the register grows as a monument rather than a control.

### Mitigations available

(a) Bind consultation to a trigger point rather than to an instruction — identify the specific moment in the minting workflow where a premise could change the output, and require a lookup *there*, on a scoped subset. This is the checklist mechanism and it is what made it work. (b) Build the directory, not just the store: index premises by the decision they bear on, so retrieval is targeted rather than a full-register read. This is the transactive-memory finding operationalised. (c) Keep the consulted subset small and stable, since acceptance falls with volume and with repetition; a five-item scoped check will outperform a hundred-item register read. (d) Instrument consultation — record which premises were retrieved at which trigger — so that the control's own effectiveness is measurable rather than presumed, which is the very failure this item describes.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-781

**Strongest counterargument:** The claim that written records do not constrain action is empirically false in the most demanding available test. Surgery is a domain of extreme expert autonomy, time pressure and hierarchy, and a nineteen-line written artefact cut thirty-day mortality nearly in half across eight hospitals on four continents, with the result replicating at national scale. If a register can do that there, "registers have no downstream force by default" cannot be right as stated. The interesting content of the counterexample is the mechanism: the checklist has three named moments at which work stops and the record is read aloud, and a named person responsible for reading it. That is a design property, not a property of writing things down, and it is inexpensive to replicate. The presumption's grading as Critical therefore over-reads a fixable binding problem as a structural impossibility. And the remedy it points toward — instruct the minting agents to consult the register — is the intervention the clinical-decision-support literature has measured most thoroughly and found to degrade predictably: override rates of 49–96%, with acceptance falling roughly 30% per additional prompt. A general instruction to read a growing register will produce compliance theatre, which is strictly worse than the current honest silence because it creates a record of a check that did not happen.

**What would need to be true for C2A2 to be safe:** Each register entry must name the workflow moment at which it applies and the agent that owns that moment, and the consulted subset at any trigger must stay small enough that consultation does not decay. Given those two properties, entering something in the register does constrain what is done next, and the presumption's worry lapses. Absent them, the worry stands — but as a binding defect, not as evidence that registers are inert.

**How to test:** Two measurements. First, retrospective: for each of PREMISE-107 and PREMISE-110, identify the exact point in the minting workflow at which consulting it would have prevented the re-derivation, and check whether the premise as written names that point. If it does not, the defect is binding, not force. Second, prospective and cheap: bind two or three premises to named trigger points, instrument retrieval, and measure the re-derivation rate for bound versus unbound premises over the next ten runs. That comparison distinguishes "registers are inert" from "unbound registers are inert" directly, and the second is the far more likely finding.

---

## Search scope

Moderate. Query families executed: checklist efficacy and its replications; transactive memory systems and team performance; alert and reminder fatigue and override rates; ADR guidance on documentation fatigue. Not searched: the lessons-learned-database failure literature named in the item's search strategy (Weber/Aha and successors), documentation read-write ratio studies, or the "reality check for checklists" critical literature that qualifies Haynes. That last omission matters and cuts *toward* 14b: there is a known critical literature arguing the checklist effect is smaller or context-dependent than the 2009 result, and a fuller search would need to weigh it. Broader search recommended.
