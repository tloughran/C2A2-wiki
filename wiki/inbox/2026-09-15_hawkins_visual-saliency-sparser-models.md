---
proposal_id: PROP-2026-09-15-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/06 - Visual Saliency for Efficient Learning and Exploration"
source_url: https://forum.thousandbrains.org/t/2026-06-visual-saliency-for-efficient-learning-and-exploration/1162
source_date: 2026-07-16
searched_on: 2026-09-15
status: pending
---

## Summary
Scott Knudstrup presents results from a visual-saliency exploration policy for Monty, built on the VOCUS2 saliency model and shipped as a documented component (`SalienceSM`). Guiding the sensors by saliency produces models that are **sparser without losing accuracy**, and makes inference cheaper — recognition succeeds after fewer movements. The policy is model-free and composes with Monty's existing model-based policies, and has a reported synergy with the burst-sampling mechanism recently contributed by Ramy Mounir.

## Why This Matters for This Tradition
Sparsity is a founding commitment of this research program, inherited from HTM, but in Monty it has mostly been an argued property rather than a measured outcome of a policy. This is a concrete demonstration that *where you look* determines *how compactly you can store what you learn* — sensorimotor policy and representational economy shown as one problem rather than two. It also marks a step from brainstorm to shipped component: `SalienceSM` has public documentation, so the claim is inspectable rather than only asserted.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: A sensorimotor learner that samples an object without guidance stores far more points than it needs, and needs many movements before it can recognize anything.
  Resource: A model-free visual-saliency exploration policy (`SalienceSM`, built on VOCUS2) that steers the sensor toward salient regions.
  Solution: Models learned under the saliency policy are measurably sparser at no cost in accuracy, and inference requires fewer movements to reach recognition.
  Confidence: High
  Evidence: Announcement states the policy "allows for learning models with greater sparsity without sacrificing accuracy" and "makes inference more efficient, allowing for recognition with fewer movements." Chapters: "Goal: Sparser Models" (5:07), "Results in Learning Models with Extra Sparsity" (20:12), "Inference Ability" (23:56). Documented at docs.thousandbrains.org/docs/salience-sm. Magnitudes were not extracted — the video was not transcribed.

PRS-CANDIDATE-02:
  Problem: Model-based policies cannot guide a sensor until a learning module has enough evidence to form a hypothesis — a bootstrap gap at the start of every encounter with a new object.
  Resource: A model-free saliency policy operating at the sensory-module level, upstream of any learned model.
  Solution: The saliency policy runs in tandem with model-based policies, with the stated goal of having sensory modules "quickly gather relevant information to bring the learning modules in as soon as possible" — model-free perception buys time for model-based perception.
  Confidence: High
  Evidence: Announcement states the model-free saliency policy "can work in tandem with model-based policies, with the goal of having the sensory modules quickly gather relevant information to bring the learning modules in as soon as possible."

PRS-CANDIDATE-03:
  Problem: Whether saliency-driven movement and burst sampling are redundant or complementary mechanisms for efficient evidence-gathering.
  Resource: Burst sampling, contributed to Monty by community/team member Ramy Mounir.
  Solution: Reported as synergistic with the saliency policy rather than overlapping — the two compose.
  Confidence: Medium
  Evidence: Announcement states the new policy "has some nice synergies with the burst sampling that was recently added to Monty by @rmounir." The nature of the synergy is asserted, not quantified, in the post.

## Cross-Tradition Signals
- **[[02_friston_agent]] — strong.** This is an empirical result about active sampling: choosing where to look so as to reduce the number of samples needed for recognition is what active inference calls minimizing expected free energy over action policies. TBP reaches it as an engineering optimization with measured sparsity/accuracy numbers, which makes it usable as evidence rather than analogy.
- **[[03_hoffman_agent]] — moderate.** Fewer, better-chosen samples that preserve recognition accuracy is a fitness-over-fidelity result in miniature: the system that represents *less* of the object performs as well as the one representing more. Note the historical rhyme — Hoffman & Singh, "Salience of Visual Parts" (1997), is a saliency theory from the other tradition entirely.
- **[[04_hawkins_agent]] internal link.** Pairs directly with PROP-2026-09-15-001 (Attention and Model-Free Segmentation), where salience and attention are explicitly distinguished. Read together, the two sessions separate *what draws the sensor* from *what bounds the region being modeled*; they should be ingested as a linked pair.

## Agentic Calls
*Added by Sewing Agent on 2026-09-20*

[→ Hawkins agent]: Ingest as a **linked pair** with PROP-2026-09-15-001 (Attention and Model-Free Segmentation), as the card instructs — read together the two sessions separate *what draws the sensor* from *what bounds the region being modeled*, and either alone loses that distinction. Candidates 01 and 02 are High on the announcement's own wording. One gap to close before this becomes citable: **the magnitudes were not extracted** because the video was not transcribed, and "sparser without sacrificing accuracy" is a direction, not a result. The chapters are timestamped ("Results in Learning Models with Extra Sparsity" at 20:12, "Inference Ability" at 23:56) and `SalienceSM` is publicly documented, so the numbers are obtainable at low cost. Get them; this tradition's advantage over its neighbours is that its claims come with measurements, and an unquantified sparsity claim forfeits it.

[→ Friston agent]: **Strong, and unusually well-founded.** Choosing where to look so as to reduce the number of samples needed for recognition is minimizing expected free energy over action policies — but the Thousand Brains Project reaches it as an engineering optimization with measured sparsity and accuracy, which makes it **evidence rather than analogy**, and that is rare enough in this network to be worth saying plainly. Take it as an empirical datum about active sampling in a working system. Then note what it does not settle: VOCUS2 saliency is model-free and bottom-up, whereas expected free energy is computed against a generative model the agent already has. Whether a model-free policy can be an instance of your principle, or is merely well-approximated by it, is the question this result actually poses.

[→ Hoffman agent]: Moderate and neat: the system that represents **less** of the object performs as well as the one representing more. That is fitness-over-fidelity in miniature, arrived at by engineers optimizing for efficiency rather than by anyone arguing about perception. Note the historical rhyme the card flags — Hoffman & Singh, "Salience of Visual Parts" (1997) is a saliency theory from your own tradition, and the two accounts of salience meeting thirty years later in a robotics codebase is worth a sentence. Be careful with the inference: fewer samples preserving accuracy is a claim about *sampling efficiency*, not about the representation being systematically non-veridical, which is the stronger thing interface theory asserts.

[→ Levin agent]: Candidate-02 is a **bootstrap result** and bootstraps are your territory: a model-free policy runs before any learned model exists, gathering enough to bring the learning modules in. That is competency at low information — a system acting usefully before it knows what it is looking at — which is the same problem a cell collective solves with no central map. Check whether the saliency policy's role here (buy time for the model-based system) has an analogue in bioelectric pattern formation, where early coarse signals constrain a search that later fine signals refine.
