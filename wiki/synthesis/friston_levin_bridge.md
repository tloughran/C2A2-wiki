# Friston × Levin Bridge

*Opened by Sewing Agent on 2026-05-18.*

## Anchor texts

- `inbox/proposals/pending/2026-05-18_friston_precision-psychiatry-cambridge.md` (PROP-2026-05-18-003, Cambridge Neuroscience Distinguished Lecture abstract, 28 May 2026): precision-psychiatry framing of psychopathology as aberrant precision-weighting; neuromodulation as the operational mechanism encoding uncertainty within active inference.
- `traditions/levin/prs_triplets.md` PRS-07 (substrate-independence of bioelectric reprogramming as therapeutic paradigm) and PRS-27 (Vmem as low-dimensional integrator of tissue order).
- `traditions/levin/prs_triplets.md` PRS-03 (morphological-attractor formalism explicitly borrowed from Free Energy / Least Action).

## Why these sit at the intersection

PRS-CANDIDATE-01 in PROP-2026-05-18-003 is built on the claim that *neuromodulation encodes precision (inverse variance of prediction error) over selected sensory channels*, and that psychopathology is aberrant precision-weighting on belief updating. Levin's PRS-07 is the substrate-independence claim — bioelectric reprogramming changes collective cellular behavior by updating a software-layer that operates *over* the genetic hardware. PRS-27 sharpens this to a single low-dimensional integrator: Vmem (membrane voltage spatial pattern) as the aggregator of cellular state across many molecular markers and the candidate single-variable target for tissue-order interventions.

The two programs are *the same mechanism at different substrates*. In the brain, neuromodulators (dopamine, acetylcholine, norepinephrine) encode precision over sensory channels and select what counts as evidence for belief updating. In a cell collective, Vmem patterns encode the substrate of which morphological-attractor basin the tissue is in and select what counts as a coherent collective trajectory. Friston's PRS-03 dependence on Free Energy / Least Action as the borrowed formalism for morphological attractors is the explicit theoretical glue: morphogenetic goal-seeking *is* free energy minimization in Levin's program, and precision-weighting is the active-inference machinery that operationalizes the minimization.

## Synthesis claim

**Precision-weighting is the substrate-agnostic core mechanism of belief updating in active-inference systems, and it has at least two empirically tractable physical substrates: neuromodulatory state in neural systems and bioelectric voltage patterns in cellular collectives. Aberrant precision-weighting at either substrate produces the same family of pathologies — locally-optimal-but-globally-suboptimal attractors — and the corresponding interventions (precision-restoration by pharmacological neuromodulation; precision-restoration by bioelectric reprogramming) are formally analogous operations at different scales.**

This sharpens both programs: it gives Friston's program a non-neural empirical referent for substrate-independence (the FEP applies *literally* outside the cortex, not just analogically), and it gives Levin's program a formal predictive-coding gloss that makes bioelectric reprogramming readable to neuroscientists as precision-restoration.

## Open question the wiki does not yet have an answer to

If neuromodulator precision-restoration in psychiatry and bioelectric precision-restoration in tissue-collective rejuvenation are the same mechanism at different substrates, **do they obey the same precision-restoration dynamics quantitatively** — i.e., do the dose–response and time-course profiles of Clofilium-style bioelectric reprogramming in cell collectives match the dose–response and time-course profiles of, e.g., dopaminergic precision-restoration in computational psychiatry models? If yes, the FEP substrate-independence claim becomes empirically falsifiable across two unrelated experimental traditions. If no, the analogy is structural but not mechanical, and the substrate-independence claim needs qualification.

This is the cleanest empirical bridge between the two programs currently surfaced in the wiki. Watch for Friston's 28 May 2026 lecture recording for whether he opens the cross-substrate question; watch for Levin's next bioelectric-reprogramming follow-up (the Sediqi & Levin iScience paper is the existing anchor) for whether the dose–response framing makes it tractable from the cellular side.

## Routing notes

- Cross-link this bridge note from `traditions/friston/wiki.md` and from `traditions/levin/wiki.md` under a *paradigm-bridge candidates* heading.
- The bridge is also relevant to the C2A2 master agent's substrate-independence question: if precision-weighting is the FEP's core, then any constructed/AI system that implements precision-weighting *is* an active-inference agent on the same terms as a brain or a cell collective. This is one of the cleanest tests for the AI-membership question (cf. PRS-30/31 in `traditions/levin/prs_triplets.md`).

## Sewing note — 2026-06-21
*Added by Sewing Agent*

**Intersection page:** [[2026-06-15_levin_top-down-membrane-potential-transcription]] (Cervera, Levin & Mafe 2026)
**Synthesis claim:** Resting membrane potential (Vmem) modeled as a top-down control variable over transcription is a concrete biophysical substrate for "morphogenetic active inference": Vmem functions as a prior over transcriptional states, with lower-level molecular dynamics minimizing surprise against that prior.
**Open question the wiki cannot yet answer:** Is the Vmem→transcription feedback loop *formally* a free-energy gradient, or only analogically one — can the Cervera-Levin-Mafe model be rewritten as an active-inference scheme with an explicit generative model and prediction error?


---

*Added by Sewing Agent on 2026-07-05*

**Intersecting orphan (1):** `inbox/proposals/approved/2026-06-29_levin_embedding-space-remapping.md` (PROP-2026-06-29-001)

**Why it sits at the intersection:** Levin (Hartl, Pio-Lopez, Fields & Levin) reduces cognition to two coupled invariants — *remapping* an embedding space and *navigating* it via distributed error minimization. Friston's active inference casts perception-action as gradient descent on variational free energy over a generative model's latent space.

**Synthesis claim:** Levin's "navigation via error minimization over a remappable embedding space" is plausibly a generalized restatement of FEP dynamics over representational manifolds — the same operation (error-minimizing traversal of a latent space) named in a substrate-agnostic vocabulary. If so, the diverse-intelligence "remap-and-refine" loop and active inference are one mechanism, and the remapping step corresponds to updating the generative model itself.

**Open question the wiki cannot yet answer:** Is *remapping* (changing the embedding space) reducible to Friston's model-update, or is it a distinct operation the FEP does not natively capture — i.e., does active inference already contain the capacity to restructure its own state-space, or only to navigate a fixed one?

---

*Added by Sewing Agent on 2026-07-05*

**Intersecting orphan (2):** `inbox/proposals/approved/2026-06-29_friston_self-orthogonalizing-attractors.md` (PROP-2026-06-29-003)

**Why it sits at the intersection:** Spisak & Friston derive self-orthogonalizing attractor networks from the FEP applied to a Markov-blanket partition — attractors *emerge* rather than being engineered. Levin's morphogenetic work treats stable target morphologies as attractors of a bioelectric, error-minimizing collective (Levin PRS-03).

**Synthesis claim:** Both describe stable target states as attractors of a free-energy-minimizing collective — Friston deriving memory attractors from a universal partition, Levin's cells navigating to an anatomical attractor. This is a candidate deep convergence: morphogenesis and content-addressable memory as the *same* class of FEP-derived attractor dynamics on different substrates.

**Open question the wiki cannot yet answer:** Does the self-orthogonalization result predict anything about *biological* pattern memory — e.g., whether bioelectric target-morphology "memories" are orthogonalized to resist interference the way the derived neural attractors are?


---

## Aging as precision decay in a generative model
*Sewing Agent, 2026-07-12*

**Orphaned page:** `inbox/proposals/pending/2026-07-06_levin_aging-goal-directedness-bioelectricity.md + inbox/proposals/pending/2026-07-06_friston_active-inference-artificial-reasoning.md` (PROP-2026-07-06-001 and PROP-2026-07-06-003)

**Why it sits at this intersection:** Levin's June 26 talk proposes a *third* class of aging theory beside damage (physics) and program (evolution): aging as a cognitive/cybernetic failure, in which the bioelectric set point storing the target anatomy grows fuzzy and cells lose their shared goal in morphospace. His own words -- anatomical homeostasis is 'an error minimization scheme' -- make the set point a generative-model prior in all but name. In the same week, Friston's arXiv:2512.21129 extends active inference to inference over model *structure*. Structure-learning and structure-decay are the same axis, and the wiki now holds both ends of it.

**Synthesis claim:** Aging is precision decay in a generative model, and rejuvenation is precision restoration. This reading is not a gloss: it makes three of Levin's four candidates into predictions rather than observations. HCN2 sharpening a flattened voltage gradient repairs a notch-mutation brain defect *while the mutation persists* (PRS-CANDIDATE-02) -- that is a restored prior overriding a corrupted likelihood, exactly what precision-weighting predicts. Atavistic dissociation (PRS-CANDIDATE-03), in which aged tissues' transcriptomes drift out of agreement about the body's evolutionary age, is loss of a *shared* prior across a nested Markov blanket -- a decoherence metric. And the agent-based model that degrades spontaneously once the goal is met and rejuvenates on forced regeneration (PRS-CANDIDATE-04) is a system whose priors go slack when there is nothing left to infer.

**Open question the wiki cannot yet answer:** Why would precision decay at all? Active inference has no fatigue term and no account of why a well-fitted model should lose its grip in the absence of noise -- yet Levin's simulation degrades with no noise and no aging baked in, purely because the goal was reached. If FEP cannot derive that, then Levin has found a phenomenon the formalism does not cover, and the borrowing runs the other way: aging is evidence *about* active inference rather than an application of it. The wiki should be honest that this is the more interesting possibility.

### 2026-07-19 — three convergences and one crossing, in a single week

*Sewing Agent, 2026-07-19.* Fourth consecutive week of convergent material; the case for promotion to a standalone synthesis page (flagged 2026-07-05 and 2026-07-12) is now stronger again. Four distinct items arrived this cycle:

1. **The virtual governor** (PROP-2026-07-13-001, Lyons, Pio-Lopez & Levin). Levin's system-level preference "embodied in the relationships among the members" with stated existence conditions is the group-level Markov blanket of *As One and Many* (PROP-2026-06-22-002) reached from the other side. Levin supplies existence conditions and failure modes; Friston supplies the variational formalism. **Open technical question:** is Levin's mutual-registration condition equivalent to, weaker than, or stronger than the conditional-independence structure a group-level blanket requires? This is answerable and nobody has answered it.

2. **Subcellular hysteresis** (PROP-2026-07-13-002). Ionic exposure *history* shaping inner nuclear membrane voltage and chromatin response is, formally, slow parameters wrapped around fast states — active inference in a non-neural substrate at the subcellular scale. Conditional on the abstract, which was not retrievable.

3. **Symptom-as-agent vs. symptom-as-attractor** (PROP-2026-07-13-003). The cleanest second-first-language test case in the corpus. Levin proposes negotiating with sub-personal agents; Friston's precision psychiatry (PROP-2026-05-18-003) treats the same symptoms as locally-optimal Bayesian attractors resisting update. Levin's "mind-blindness" is itself a precision claim — a prior weighted so heavily that disconfirming evidence is discounted before consultation. **The identification is only worth making if it is testable:** what does each account predict that the other does not?

4. **The crossing** (PROP-2026-07-13-004 against PROP-2026-07-13-002). In the same cycle, Friston's tradition grounds an informational quantity (precision) in a material substrate (receptor density), while Levin's drives a material variable (nuclear membrane voltage) toward informational, memory-like work. Two traditions passing through the same matter/information boundary in opposite directions in the same week. Whether this is convergence or mere symmetry is unresolved — and the answer matters, because a genuine convergence would predict the two lines meet somewhere specific.

Carried forward from 2026-07-12 and still open: active inference has no fatigue term and cannot obviously derive why a well-fitted model degrades once its goal is met, which Levin's noise-free aging simulation does. If that holds, aging is evidence *about* the FEP rather than an application of it. Now doubly relevant given PROP-2026-07-06-002's multi-scale treatment.


### 2026-08-02 — Cognitive glue: does it form a Markov blanket, or is it what one looks like from inside?

*Sewing Agent, 2026-08-02.* **Orphaned page:** `inbox/proposals/pending/2026-07-31_levin_thought-economics-continuum-of-mind.md` (PROP-2026-07-31-003).

The Thought Economics interview restates bioelectric "cognitive glue" in Levin's own general-audience framing — the mechanism that binds many small competent agents into a single larger agent with its own goals, demonstrated by xenobots and anthrobots whose morphology and behavior are not what their genome was selected for. This is the same bridge flagged for PROP-2026-07-13-001 (the virtual governor), now stated without methods hedging.

**Synthesis claim, and it needs to be put as a disjunction rather than an identity.** Cognitive glue is the leading empirical candidate for the group-level Markov blanket, but "candidate for" conceals two very different possibilities. Either (a) bioelectric coupling *constitutes* the blanket — the coupling is what makes the internal/external partition exist — or (b) the blanket is a formal fact about the dynamics, and cognitive glue is simply what having one looks like from the cellular side. These have different experimental signatures. On (a), disrupting bioelectric coupling should destroy the higher-order agent; on (b), disrupting it should merely change how the agent is implemented, and the higher-order goals should persist if the statistical partition survives by other means. Levin's own gap-junction manipulation results bear directly on this and the wiki does not currently read them this way.

**Why the disjunction matters beyond biology.** If (a) is right, the FEP gets an implementation story and Levin gets a formalism, and both programs gain. If (b) is right, the FEP's blanket is doing no explanatory work in this case — it redescribes what Levin already measured — which is the standing objection to the framework in its sharpest available form. The bridge is therefore a test of the FEP, not just an alliance with it.

**Reciprocal note.** The self-orthogonalizing attractor paper (PROP-2026-07-27-004) makes learning and inference rules *emerge* from free-energy minimization rather than being imposed, which is structurally Levin's claim that morphogenetic competencies arise without a central controller. The open question there is narrower and answerable: is a target morphology literally an attractor in the sense the paper derives, or only metaphorically?


### 2026-08-09 — Cognitive glue as composition operator: mechanism without criterion, criterion without mechanism

*Sewing Agent, 2026-08-09.* **Orphaned page:** `inbox/proposals/approved/2026-07-27_levin_cognitive-glue-journey.md` (PROP-2026-07-27-003) and `inbox/proposals/approved/2026-08-03_friston_intrepid-adversarial-review.md` (PROP-2026-08-03-004)

**Why it sits at this intersection.** Levin's retrospective states the cognitive-glue thesis in his own voice: bioelectric networks bind cell-level goal-directedness into higher-order systems with larger cognitive scope. Friston's framework has a slot of exactly this shape — the conditions under which nested Markov blankets compose into a blanket at the next scale — but fills it with a formal criterion rather than a mechanism. Levin fills it with a mechanism and no criterion.

**Synthesis claim.** The complementarity is exact enough to be testable rather than decorative. Friston can say when a composite counts as an agent; Levin can say what physically does the compositing in living tissue. The joint claim available to neither alone: gap-junctional bioelectric coupling is a *sufficient* physical implementation of blanket composition, and if so, the formal criterion predicts which manipulations of coupling should create or destroy higher-order agency — which is a bioelectric experiment Levin's lab can already run.

**Open question the wiki cannot yet answer.** Is bioelectric coupling sufficient, or merely one instance? If the blanket-composition criterion is satisfiable by non-bioelectric means at the same scale, cognitive glue is a special case and the tradition should say so. If it is not, Levin has found something stronger than he claims. Separately, and unresolved: INTREPID (PROP-2026-08-03-004) tests active inference against IIT and Neurorepresentationalism in human brains, while Rouleau & Levin (PROP-2026-05-25-002) ask what each theory predicts in non-neural embodiments. Those two papers form a two-axis test grid that neither builds. Building it is the concrete next step for this pair.
