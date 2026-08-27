---
proposal_id: PROP-2026-08-12-030
prop_id: PROP-2026-08-12-030
thinker: Sean Carroll
tradition_key: carroll
source_type: podcast
source_title: "363 | Chandra Sripada on How LLMs and Humans are Cognitive Cousins"
source_url: https://preposterousuniverse.com/podcast/2026/08/10/363-chandra-sripada-on-how-llms-and-humans-are-cognitive-cousins/
source_date: 2026-08-10
searched_on: 2026-08-12
status: pending
---

## Summary
Mindscape 363 puts Carroll opposite Chandra Sripada — a philosopher and psychiatrist at Michigan who directs the Weinberg Institute for Cognitive Science — on whether large language models think the way humans do, or have found an "alien" route to human-sounding output. Sripada argues for the second-order position he calls "cognitive cousin": next-word prediction at internet scale is such a powerful training signal that LLMs converge on the same core processing principles as the human mind-brain, and the right evidence is not behavioural tallying but whether LLMs reproduce specific, mechanism-understood effects from decades of cognitive science. He runs through several that they do reproduce: center-embedding and garden-path parsing costs from psycholinguistics; the full serial-position signature in list memory (primacy, recency, lost-in-the-middle, contiguity, forward temporal asymmetry); and the disjunctive-versus-conjunctive asymmetry in visual search, in vision-language models.

The episode is notable as a **Carroll-primary** source because Carroll uses his own opening monologue to record a credence shift against his prior public position. He states that he had been "on the side of being impressed" by anomaly evidence such as the strawberry-R counting failure, treating it as good evidence that LLMs are not thinking as humans do, and says this conversation "shifted my credences in important ways." He also gives his reason for having discounted industry testimony: AI leaders are experts in computer science, "but not experts in intelligence and cognitive science."

## Why This Matters for This Tradition
Carroll's poetic naturalism holds that higher-level vocabularies (agency, thought, self) are real when they are the useful emergent description of an underlying substrate, and he has applied that test to human minds for years; this episode is the first captured source where he applies the same emergence test to artificial cognition and publicly revises a stated credence on the result. It also gives the tradition a concrete, falsifiable criterion for "same kind of thinking" — reproduction of mechanism-understood cognitive-science effects rather than input-output indistinguishability — which is a sharper instrument than the Turing test framing Carroll opens with.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The Turing test settles only input-output indistinguishability, so it cannot decide whether an LLM has rediscovered human cognitive mechanisms or found a different route to human-sounding output. Behavioural anomaly-counting (the strawberry-R case) does not settle it either, in the other direction.
  Resource: The "cognitive cousin" criterion — test the system against specific effects from cognitive science whose *underlying mechanism* is already understood, rather than tabulating surface similarities and dissimilarities.
  Solution: Replace the behavioural test with a mechanism-matched one: an LLM counts as a cognitive cousin to the degree it reproduces effects whose human explanation is known, so that a shared effect licenses an inference to a shared mechanism.
  Confidence: High
  Evidence: Sripada, verbatim: "counting and tabulating at the level of behavioral outputs is probably not gonna get us very far. We need to look mechanistically, and we need to think about which are the mechanisms that we actually care about that are core processing principles for the human mind-brain." Carroll frames the two options explicitly at 0:15:48 — rediscovered mechanisms versus "a wholly new way of sounding human ... an alien kind of intelligence."

PRS-CANDIDATE-02:
  Problem: If LLMs are human-like, is that convergence a designed-in resemblance, or does it fall out of something more basic?
  Resource: Prediction as, in Sripada's phrase, "the mother of all training signals" — the claim that dual-process structure and other cognitive principles previously thought innately specified or evolutionarily contingent are instead *downstream of* prediction, in humans as well as in machines.
  Solution: A common-cause account of the convergence: both systems are prediction machines, so similar representations, procedural techniques, and modes of inferential organization emerge in both without either copying the other.
  Confidence: High
  Evidence: Sripada at 0:18:15: "a lot of cognitive principles that we thought were innately specified or due to some sort of contingent evolutionary trajectory, they actually are emergent ... they are downstream of prediction ... at the level of basic core cognitive principles, the LLMs and humans, they identify similar representations, similar procedural techniques."

PRS-CANDIDATE-03:
  Problem: What specific empirical findings would count as evidence for mechanism-sharing, as opposed to anecdote?
  Resource: Three families of pre-registered-by-history cognitive effects, documented in humans decades before LLMs existed: (a) psycholinguistic parsing costs — center-embedding degradation ("A man that a woman that a child knows loves ran"), garden-path sentences ("The horse raced past the barn fell"), similarity-based interference; (b) serial-list memory — primacy, recency, lost-in-the-middle, contiguity, forward temporal asymmetry; (c) visual search — pop-out in disjunctive search versus serial, set-size-proportional search time in conjunctive search.
  Solution: All three families reproduce in LLMs (visual search in vision-language models), and because the human mechanisms behind them are independently known — incremental parsing that commits early and must backtrack; compositional coding versus feature binding — the shared effects support shared mechanisms rather than coincidence.
  Confidence: High
  Evidence: Sripada enumerates each effect and states "LLMs exhibit all these effects," then: "The fact that you're seeing these non-obvious patterns of similarities in LLMs and people, especially where we know some of the mechanisms that happened in these effects in cognitive science, they point to similar mechanisms being operative in the LLMs and people."

PRS-CANDIDATE-04:
  Problem: Anomalies such as an LLM's inability to count the letter R in "strawberry" have been treated (by Carroll among others) as strong disconfirming evidence for human-like cognition.
  Resource: A sensory-primitive account of the anomaly: tokens are the model's sensory interface, so sub-token structure is not normally available to it — letter-level manipulation was never a candidate "core processing principle" to begin with.
  Solution: Reclassify such anomalies as expected consequences of a different sensory channel rather than as evidence against mechanism-sharing, and restrict the evidential weight of behavioural anomalies to principles that cognitive science independently regards as core.
  Confidence: Medium
  Evidence: Sripada: "their contact with the 'world' is exclusively textual via these tokens, which essentially serve as kind of sensory primitives ... there's a very natural explanation for why they can't count the number of Rs in strawberry." Marked Medium rather than High because the account is offered as an explanation and not tested against a control in the episode.

PRS-CANDIDATE-05:
  Problem: Where does Carroll himself now stand, given that he had publicly used the anomaly evidence to argue LLMs are not thinking as humans do?
  Resource: Carroll's own stated Bayesian discipline, applied to himself on the record, plus his separation of cognition from consciousness ("Cognition is easier to understand than consciousness").
  Solution: Carroll revises his credence toward the cognitive-cousin position while explicitly bounding what that does and does not license — not consciousness, not moral agency, but a step in that direction that should be established first.
  Confidence: High
  Evidence: Carroll, monologue: "this is one of those podcasts that has shifted my credences in important ways ... one should always be a good Bayesian." And, bounding it: "It's not the same as saying that LLMs are conscious or responsible moral agents or anything like that, but this is something we should establish in that direction."

## Cross-Tradition Signals

- **Carroll × Hawkins.** Sripada's claim that prediction is the generative principle from which higher cognitive structure emerges is the same architectural bet as the Thousand Brains framework's prediction-driven cortical model, arrived at from cognitive psychology rather than neuroanatomy. The two programs now offer independent routes to "prediction is the core operation," which is a candidate convergence rather than a shared citation.
- **Carroll × Friston.** Prediction as "the mother of all training signals" is adjacent to, but weaker than, the free-energy formulation: Sripada makes prediction the *training objective* whose byproducts are cognitive principles; Friston makes prediction-error minimization the *normative principle* itself. Worth flagging as a productive tension over whether prediction is explanans or explanandum.
- **Carroll × McGilchrist.** Directly opposed valence on the same evidence. McGilchrist's program treats machine cognition as structurally left-hemispheric and therefore categorically unlike the whole human mind; the cognitive-cousin thesis argues from empirical psycholinguistics and memory effects that the resemblance runs deeper than supposed. This is a live disagreement the wiki can now state with sources on both sides.
- **Carroll × Wolfram.** Wolfram's captured position (PROP-2026-08-01-001) identifies the observer by a computational signature — crushing large input down to a single slow thread of decision. Sripada's serial-list-memory and conjunctive-search findings are empirical evidence about exactly that bottleneck, in both humans and LLMs. Possible bridge: the "cognitive cousin" claim as an empirical test of whether an LLM occupies a comparable observer position in rulial space.
- **Carroll × Levin.** Both bear on substrate-independence of cognitive principles; Levin's case is made across biological substrates, this one across biological and artificial. The shared claim is that the principle survives the substrate change; the traditions differ on what the principle is.
