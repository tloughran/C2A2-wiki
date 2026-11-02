---
proposal_id: PROP-2026-11-02-003
thinker: Karl Friston
tradition_key: friston
source_type: interview
source_title: "The Brain in the Dark: A Conversation with Professor Karl Friston on Perception, Free Will and Whether Machines Can Be Conscious"
source_url: https://thoughteconomics.com/karl-friston/
source_date: 2026-10-19
searched_on: 2026-11-02
status: pending
---

## Summary
A long-form print interview (Vikas Shah, Thought Economics, 2026-10-19; ~27 min read) in which Friston covers inside-out perception, free will, consciousness, psychopathology, machine consciousness, curiosity, and selfhood. Most of the perception material is familiar, but four points are sharper than in sources already in the vault: (1) the decisive difference between people and large language models is not substrate alone but **uncertainty quantification** — LLMs carry no explicit representation of the precision of their beliefs, so they "do not know what they do not know," cannot be curious, and lack "true agency"; (2) consciousness requires a generative model in which you are modelled as the author of your own sensations, with a deeper, metacognitive layer giving "a minimal kind of selfhood"; (3) the self is a "fragile hypothesis," and individuation into self, objects and other agents is learned (causal discovery / structure learning — "a real frontier problem"); (4) the next big question is the "federated, intersubjective aspect of self-organisation," which he names as key to intelligence and consciousness, citing Levin.

I read the full interview text on the page. It is an edited print conversation, so quotations are as published.

## Why This Matters for This Tradition
It gives a plain-language, quotable statement of the active-inference criterion for agency (optimise a functional of beliefs, not a value function of states) and turns it into a concrete diagnostic for AI. It also restates mortal computation (Hinton's term) while saying he is "not personally committed to one side or the other" — a useful hedge to record next to the stronger mortality claims captured from the BBS Seth exchange (PROP-2026-10-26).

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Large language models produce human-like output; what, if anything, separates them from agents that infer?
  Resource: The active-inference requirement that beliefs carry an explicit, physically represented precision (credence / inverse uncertainty), so that expected information gain can be computed.
  Solution: Draw the line at uncertainty quantification: a system that only maps inputs to outputs via a value function of states cannot know what it does not know, so it cannot be curious or select uncertainty-resolving actions; agency requires optimising a functional of beliefs (variational free energy, the ELBO). Installing curiosity — systems that ask *you* questions — is the prerequisite for anything near AGI.
  Confidence: High (as a statement of Friston's position; the empirical claim about LLMs is contestable)
  Evidence: "If you do not have that, and large language models do not have that, then you do not know what you do not know. You cannot do belief updating. All you can do is produce outputs for any given input. So there is no true agency underneath."

PRS-CANDIDATE-02:
  Problem: What extra structure turns unconscious inference into something deserving the name consciousness or selfhood?
  Resource: Deep (hierarchical) generative models in which the agent models itself as the cause of its own sensations, plus a metacognitive layer that recognises that "this thing performing planning as inference is me," in context.
  Solution: Treat self-authorship of sensation as a prerequisite for consciousness and metacognitive depth as the source of minimal selfhood; read psychopathology as false inference (type I errors → hallucination/delusion; type II → neglect, dissociation).
  Confidence: Medium
  Evidence: "You are authoring your own sensations. To know that, to model it and to have it as part of your generative model is, I think, a prerequisite for consciousness." Type I/II mapping stated explicitly.

PRS-CANDIDATE-03:
  Problem: How does an agent come to carve the world into things, selves and other agents at all?
  Resource: Structure learning and causal discovery under the FEP; Markov blankets as the formal device for separating inside from outside "at many, many different scales"; developmental example (the infant learning that mother moves by herself, then hypothesising "perhaps I am a thing").
  Solution: Selfhood is an inferred, fragile hypothesis (depersonalisation and psychedelics show it can dissolve), and objecthood/selfhood/otherhood are coarse-grainings we learn — "our attempt to tell stories of a simple sort about how we best explain our universe."
  Confidence: Medium
  Evidence: "That conviction is quite a unique gift and quite a fragile gift, and it can go away... you don't know anything. It's all inference, including that you are you and that you exist." "How do we actually carve nature at its joints into things?... a real frontier problem, certainly in my world."

## Cross-Tradition Signals
- **Levin (explicit):** Friston names "the federated, intersubjective aspect of self-organisation" — systems in a world "which contains other things like them" — as key to intelligence and consciousness, citing ongoing Zoom work with Levin on the origin of life. Not a non-neural-substrate result, but it marks the Levin–Friston collaboration as his stated frontier. Also a clean disagreement with Levin's 2026-10-17 talk: Levin wants a protocol that puts you in another system's first-person state; Friston says of other minds, "we will never know," only infer with more or less confidence.
- **Social systems / C2A2:** federated, intersubjective self-organisation is the FEP framing closest to C2A2's interacting traditions; and "curiosity = expected information gain" is a candidate formal criterion for what C2A2 agents should do when meeting another tradition.
- **Physics (Carroll / Arkani-Hamed):** weak. Path of least action and thermodynamic efficiency (the von Neumann memory wall) are invoked, but no new formal FEP–physics link.
- **Hoffman / Kastrup:** "perception from the inside out," a "Platonic" view of perception, and "the universe is everything... no way of knowing" bear on Hoffman's interface theory and Kastrup's idealism, though Friston also insists a self/non-self distinction must be "metaphysically present."
- **Wolfram:** natural selection as "Bayesian model selection at a very slow timescale," and scale-invariant nesting of inference/learning/selection timescales, connect to multi-scale computational views.
- **Hawkins:** the proposed "12-second" test of whether an LLM has a metric sense of time touches Hawkins' emphasis on temporal sequence in cortical models.
