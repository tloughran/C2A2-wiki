# PRESUMPTION-793 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-793

**Date searched:** 2026-08-14

**Original item:** PRESUMPTION-793

**Original statement:** That a series being complete is the same thing as a project being finished. The producing task declared completion at 307 against a spec of 308 and recommended its own retirement on a day when four defect classes in its corpus were open and growing.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from a producing task declaring completion at 307/308 and recommending its own retirement while four defect classes in its corpus were open and growing, that the system presumes series-completeness equals project-completeness. Residual claim: retiring the producer leaves the corpus with open defect classes and no scheduled owner. Risk graded Medium.
  - 15b: Searched for literature challenging the inference — the base rate of premature versus over-extended project termination, whether producer retirement is the right lever for corpus maintenance, and whether the maintenance-tail result applies to fixed-spec generated artefacts.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note.** 14b's claim-to-test is worded as the defective belief. The AGAINST direction therefore challenges 14b's *residual* claim — that the producer's self-retirement recommendation is a mistake because the corpus has open defects. The proposition I am challenging is: **"a producer with open defect classes in its output should not retire."** I am not challenging the observation that project-completion and product-lifecycle are different things; that distinction is uncontroversial and I found no literature against it.

### Challenging evidence found: Yes (partial)

### Sources

1. **Staw, B. M., 1976. "Knee-deep in the Big Muddy: A study of escalating commitment to a chosen course of action." *Organizational Behavior and Human Performance*.** [canonical, not re-verified this run — attribution confirmed via secondary sources this run] — Founding study of escalation of commitment. The documented organisational bias runs *opposite* to 14b's worry: decision-makers systematically over-continue failing or completed courses of action rather than terminating them prematurely.
2. **Keil, M. et al. "Escalation of Commitment in MIS Projects: A Meta-Analysis."** [abstract/listing only, verified this run via ResearchGate listing; author list not fully confirmed] — Meta-analytic evidence that escalation of commitment is a recurrent and measurable pattern specifically in information-systems projects. The prior probability that a self-retiring producer is making the *rarer* error is therefore low.
3. **Practitioner/portfolio-governance literature on "zombie projects"** (Forbes Australia; PMI, "Early termination of failing projects"; PMI, "The psychology of project termination") [verified this run as web sources; PMI items are practitioner-conference papers, not peer-reviewed empirical studies] — The recurring finding is a *decision gap*: governance forums are effective at approving and launching initiatives and rarely have processes that enforce shutdown, so portfolios bloat with work nobody can end. A task that proposes its own retirement is executing the scarce behaviour, not the common failure.
4. **Beyer, B., Jones, C., Petoff, J., Murphy, N. R. (eds.), 2016. *Site Reliability Engineering*, Ch. "Evolving SRE Engagement Model" (Production Readiness Review).** [verified this run via sre.google/sre-book] — Establishes the standard structural answer: ownership of a running artefact is transferred through an explicit, evidence-based gate (the PRR) covering observability, automation, safety and *named ownership*, with a training/documentation handover. The remedy for an unowned corpus is a handover gate, not the indefinite survival of the producer.
5. **Humble, J., Molesky, J., O'Reilly, B., 2015. *Lean Enterprise*.** [snippet only, verified this run via a reader's public note; primary text not re-read] — Same pattern in the build/run separation: the product team owns the service at launch, and operations takes over day-to-day running only after a *handover readiness review*. Build-completion and run-ownership are deliberately decoupled, and the decoupling is the control.
6. **Lehman, M. M., 1974–1996. Laws of software evolution (Continuing Change; Declining Quality); and the S-type / E-type / P-type program taxonomy.** [canonical, not re-verified; taxonomy and law statements confirmed this run via Wikipedia and secondary summaries] — This is the source most often used to support the maintenance-tail claim, but it carries the boundary condition that matters here: Continuing Change and Declining Quality are asserted for **E-type** systems — those embedded in and continuously adapting to a real-world domain. A corpus generated once against a fixed 308-item specification is closer to **S-type** (specified) in the respect that governs the law. The maintenance tail is not automatic; it depends on whether the corpus's environment moves.
7. **"An Empirical Study of Lehman's Law on Software Quality Evolution."** [title and venue listing verified this run via IU ScholarWorks; contents not read] — Cited only to record that empirical confirmation of the laws is mixed in open-source settings, per the search summary. Treat as a pointer, not as evidence.
8. **Maintenance-cost benchmarks (15–20% of annual development cost, rising to 40–90% for large/complex systems).** [practitioner/vendor sources only — scnsoft, adevs, ltsgroup, progressiverobot; verified as retrieved this run but **not** citable as evidence. Flagged because these figures circulate widely and should not be treated as established.] — Noted here to warn the reconciliation step off them.

### Strength of challenge: Moderate

### Summary

The distinction 14b draws is correct and I found nothing against it: a project life cycle closes at handover while a product life cycle continues, and generated corpora do accumulate defects. But the residual claim attaches that distinction to the wrong lever. The literature's base rate is emphatic that organisations fail by over-continuing rather than by terminating, and the specific governance pathology named in the portfolio literature — the "decision gap" where nobody can end a piece of work — describes a fleet that keeps a producer scheduled past its output more accurately than it describes one that retires it. The established remedy for the real hazard 14b identifies is not producer survival but an explicit ownership-transfer gate: the SRE production readiness review and the Lean Enterprise handover readiness review both exist precisely to make "who owns this now" an answered question at the moment of build-completion. On the maintenance-tail premise itself there is a further boundary condition: Lehman's Continuing Change and Declining Quality laws are stated for E-type systems that track a moving domain, and a corpus generated once against a fixed 308-item spec does not obviously qualify. Two things in the original observation survive the challenge untouched and should not be conflated with the retirement question: 307 against a spec of 308 is an *incompleteness*, not a completion, and four open-and-growing defect classes are a live finding regardless of who owns them.

### Specific risks

If 14b's residual claim is adopted at strength, the fleet acquires a standing rule that no producer may retire while its output has open defects — which, given that every corpus has open defects at all times, is a rule that no producer can ever satisfy. That is the zombie-project mechanism installed as policy: schedule slots consumed indefinitely by tasks whose productive work is done, and the review budget 14b's sibling items (787) already show is being spent re-deriving fixed lists gets larger. The failure is not hypothetical for this fleet — 787 records seven runs in one day concluding their assigned work was exhausted.

If the challenge is over-weighted and the producer retires with nothing else changed, the hazard 14b names is real and specific: four defect classes with no scheduled owner, and no run whose contract obliges it to notice their growth. The literature is unambiguous that this is what a handover gate is for, and equally unambiguous that handover without a *named* successor owner is the modal failure.

### Mitigations available

(a) Replace the implied rule ("do not retire") with a gate ("do not retire without a named successor owner and a scheduled read"), which is the PRR/handover-readiness pattern and costs one artefact. (b) Separate the two findings the item currently fuses: the 307/308 shortfall is a specification-conformance defect and belongs in the defect register; the retirement recommendation is a portfolio decision and belongs to whoever holds the schedule. (c) Ask the E-type/S-type question explicitly of this corpus — does anything upstream of it move? If the answer is no, the maintenance tail is a defect-repair backlog with a known finite size, not an open-ended obligation, and it can be sized. (d) Record, at retirement, the four open defect classes as an inherited liability on the successor rather than as a reason to block retirement.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-793

**Strongest counterargument:** The single best-established finding about project termination is that organisations do it too late, not too early — escalation of commitment has half a century of evidence behind it and a meta-analysis in the MIS setting specifically — and the corresponding governance finding is that portfolios accumulate work nobody is empowered to stop. Against that base rate, a producing task that recommends its own retirement on completing its series is displaying the behaviour the literature says is scarce and valuable, and treating it as a symptom is exactly backwards. The real problem 14b has found is an *ownership vacancy*, and software engineering solved ownership vacancies decades ago with an explicit transfer gate: SRE's production readiness review and Lean Enterprise's handover readiness review both make build-completion and run-ownership two separate, separately-gated events. Neither requires the builder to stay. Meanwhile the premise doing the heavy lifting — that a finished corpus necessarily has a maintenance tail — imports Lehman's laws past their stated boundary: Continuing Change and Declining Quality are claims about E-type systems embedded in a moving domain, and a corpus generated once against a fixed 308-item spec may simply not be one. If the fleet adopts "no retirement while defects are open," it has written a rule no producer can ever satisfy, and it will discover in a month that it is paying schedule slots to tasks that re-derive an empty queue — which is the failure another item in this same intake batch is already reporting.

**What would need to be true for C2A2 to be safe:** A retirement must be gated on a named successor owner with a scheduled read of the corpus's defect classes, and that gate must be a real artefact rather than a sentence in a completion report. Given that, retirement is safe and correct. Additionally, the corpus's E-type/S-type character must be assessed once: if upstream content moves, the maintenance obligation is continuing and must be resourced; if it does not, the obligation is a bounded repair backlog. Absent the named successor, 14b's hazard is live — but the deficiency is a missing handover, not a mistaken retirement.

**How to test:** Two cheap tests. First, historical: count how many tasks in this fleet have ever been retired versus how many are currently scheduled and producing no new output. If the second number greatly exceeds the first, the fleet's error direction is over-continuation and the item's worry is misdirected. Second, prospective: retire the producer, and at 14 and 30 days measure whether the four defect classes have (i) grown, (ii) been picked up by any run, and (iii) appeared in any report a human would read. If none of the three, the handover gate is what was missing, and that is directly fixable. A third test settles the maintenance-tail premise: check whether any of the four open defect classes arises from *upstream drift* rather than from generation errors. Upstream drift means E-type and a genuine tail; generation errors mean a finite repair list.

---

## Search scope

**Preliminary-to-moderate.** Query families executed this run: software maintenance cost after feature-complete; definition-of-done versus product lifecycle; SRE production readiness and build/run handover; escalation of commitment and zombie projects; Lehman's laws and defect accumulation in unmaintained software.

**Not searched:** the empirical literature on orphaned/abandoned open-source projects and their measured defect trajectories (this is the most likely place to find evidence *for* 14b and it was not reached); the software-sustainment literature in defence/aerospace acquisition, which has quantitative post-delivery cost models; capture-recapture or growth-curve estimation for "defect classes open and growing." The maintenance-cost figures returned were vendor marketing and are explicitly not being offered as evidence. A broader search is recommended before this item's status is settled, and it would most likely *strengthen* 14b on the maintenance-tail axis while leaving the retirement-lever challenge intact.
