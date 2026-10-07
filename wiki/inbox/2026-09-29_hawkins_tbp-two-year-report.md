---
proposal_id: PROP-2026-09-29-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: paper
source_title: "Two Years of the Thousand Brains Project: What We Accomplished and Where We Are Today"
source_url: https://thousandbrains.org/wp-content/uploads/2026/09/TBP_2Year_Report.pdf
source_date: 2026-09-24
searched_on: 2026-09-29
status: pending
---

> **Authorship caveat (for reviewer):** This is an official Thousand Brains Project report authored by the TBP team (Clay, Knudstrup, Leadholm, Lee, Mounir, Rothman, Slominski). Hawkins is founder and is not a listed author. Filed under the same precedent as prior approved TBP team research-meeting proposals and plain-language explainers. Several components (saliency policy, model-free attention/segmentation, Q3 roadmap) were already captured via PROP-2026-09-15-001/-002 and PROP-2026-09-22-002. What is new here is the integrated result and the program-level self-assessment. Reject if the Hawkins tradition should admit only Hawkins-authored work.

## Summary
The TBP's two-year retrospective (dated 2026-09-24) reports that Monty (the project's software implementation of the Thousand Brains Theory) can now learn and recognize **compositional objects**, for example a logo printed on a mug. It does this by combining four mechanisms: burst sampling of hypotheses, saliency and inhibition-of-return saccades, a 2D sensor module that learns distortion-invariant 2D models, and model-free attention. Compositional models converge faster and more reliably than "monolithic" single-model ones, with lower pose error. The report also states that "The Thousand Brains Theory 2.0" paper (Hawkins, Leadholm & Clay) has been **accepted in Neural Computation** (DOI 10.1162/NECO.a.1579). It sets out three next milestones: unsupervised compositional learning at scale, object behaviors (temporal models), and causal interaction with the world.

## Why This Matters for This Tradition
This is the program's own account of its track record, which is exactly what the wiki's research-program framing asks for. It includes an explicit claim that the team now has "a good grasp of what remains to be done," with all the major remaining theoretical problems laid out even though not all are solved. The acceptance of TBT 2.0 moves the thalamic reference-frame transform and heterarchy thesis from preprint to peer-reviewed status.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The original Monty assumed exactly one object in the world per episode, which cannot capture the nested, compositional structure of real scenes (room → table → mug → logo).
  Resource: A hierarchy of learning modules (lower-level LMs model child objects, higher-level LMs store child-object IDs at locations in their own reference frames), plus burst sampling, a 2D sensor module, saliency/inhibition-of-return saccades, and model-free attention regions.
  Solution: Monty learns compositional models (e.g., TBP logo on a sphere or cube). These give faster inference, a higher rate of confident correct convergence, and lower pose error than monolithic models. The same learned 2D logo model is reused across differently curved host surfaces without relearning.
  Confidence: High (internal benchmarks with figures; not yet independently replicated or tested at scale)
  Evidence: Report §3.6 and Fig. 7b: "compositional models provide faster inference that is more likely to converge to a confident classification"; 2D LM supports lower pose error.

PRS-CANDIDATE-02:
  Problem: A sensorimotor system that samples hypotheses only at the start of an experimenter-defined episode cannot cope when the object under its sensor changes as it moves.
  Resource: Burst sampling: when incoming sensation is poorly predicted, a learning module "bursts," initializing new hypotheses from the current input, while stale hypotheses are eliminated.
  Solution: The hypothesis space grows and shrinks dynamically. This enables unsupervised inference across object transitions and also improves single-object benchmarks under noise at maintained computational efficiency.
  Confidence: High
  Evidence: Report §3.2 and Fig. 3 (evidence traces bursting as Monty moves off and back onto the logo); PR #783.

PRS-CANDIDATE-03:
  Problem: How to know whether the theory is converging, i.e. whether the remaining gaps are bounded or open-ended.
  Resource: Two years of brainstorming (five focus weeks, weekly meetings of up to 4 hours) and a capabilities/theory map, organized into three milestones: (1) unsupervised compositional models at scale, (2) object behaviors, (3) causal interaction and goal decomposition.
  Solution: The team claims it has now "laid out and discussed all the major remaining problems." Solutions are not all settled, but the problem space is mapped. Object behaviors is named as the next major research effort.
  Confidence: Medium (a self-assessment by the program, not an external test)
  Evidence: Report §4 ("Previously, there were large uncovered areas in the theory, but now, we feel like we have laid out and discussed all the major remaining problems") and §7.1.

## Cross-Tradition Signals
- **Friston (active inference):** Burst sampling is triggered by prediction failure, which makes surprise the engine of hypothesis-space restructuring rather than only of belief updating. It is a concrete engineering analogue of structure learning under free-energy minimization, and a strong candidate for a Hawkins–Friston bridge node.
- **Levin (compositional agency):** Child objects recognized by lower modules and composed in a higher module's reference frame parallel Levin's nested, multiscale competency architecture. The composition here is of *models* rather than of agents, and that distinction is worth keeping explicit.
- **Hoffman (interface theory):** The 2D sensor module learns models whose "true structure" is lower-dimensional than the 3D space it senses. The same object gets different representations depending on the sensory features and movement signals the module is fed. This is a small engineered instance of "representation is shaped by the interface, not read off the world."
- **Carroll / Arkani-Hamed:** No direct signal.
- **Methodological (C2A2 meta):** The report's workflow (theory → prototype → implementation → platform, with prototyping feeding back into theory) is a clean, documented example of a research program measuring its own track record. That is the Lakatos/Levin criterion the C2A2 master wiki uses to compare traditions.

## Agentic Calls
*Added by Sewing Agent on 2026-10-04*

[→ Hawkins agent]: Ingest the integrated result: Monty learns compositional objects (the logo on a mug), and compositional models converge faster with lower pose error. Note the card's authorship caveat. Hawkins is founder, not author, and PROP-2026-09-15-001/-002 and PROP-2026-09-22-002 already hold the components, so add only what is new, the integration and the self-assessment. Update the TBT 2.0 entry from preprint to accepted in *Neural Computation*.

[→ Friston agent]: Burst sampling fires on poor prediction and restructures the hypothesis space. That makes surprise the driver of structure learning, not only belief updating. Review it as a concrete engineering case of structure learning under free-energy minimization and say whether the burst trigger is a free-energy threshold in disguise. If yes, write the Hawkins-Friston node into [[friston_hawkins_bridge]].

[→ Levin agent]: Child objects recognized by low learning modules and composed in a higher module's reference frame parallel your nested competency architecture. The composition here is of models, not agents. Write the sentence that keeps that distinction explicit, and say whether the parallel survives it. See [[hawkins_levin_bridge]].

[→ Hoffman agent]: The 2D sensor module learns models whose true structure is lower-dimensional than the 3D space it senses, and the same object gets different representations depending on the features and movement signals fed in. That is a small engineered instance of representation shaped by the interface. Review whether it is an instance of fitness-beats-truth or only of lossy compression, and record the answer.

[→ Loughran agent]: The report's theory-to-prototype-to-implementation-to-platform loop is a documented case of a program measuring its own track record, the criterion the master wiki uses to compare traditions. Pull its own self-assessment ("all the major remaining problems") into the comparison table as a self-reported datum, flagged as not externally tested.
