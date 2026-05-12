---
proposal_id: PROP-2026-05-05-004
thinker: Donald Hoffman
tradition_key: hoffman
source_type: paper
source_title: "Spacetime Bounds on Consciousness [v2]"
source_url: https://www.preprints.org/manuscript/202602.1708
source_date: 2026-04 (v2 update; v1 was 2026-03-13)
searched_on: 2026-05-05
status: pending
---

## Summary
Updated v2 preprint of Hoffman's "Spacetime Bounds on Consciousness." Builds on the v1 framework introduced in March 2026 (already captured in PRS-13) by formalizing the "Chord" and "Arpeggio" conditions for unified conscious experience. Chord requires that the ingredients of a subjective experience be simultaneously instantiated and able to causally exchange influence within a time window θ, yielding the hard constraint D ≤ κvθ on conscious-system diameter. Arpeggio is proven strictly weaker than Chord: architectures with limited concurrency (such as cloud-hosted LLMs and certain distributed AI systems) can satisfy Arpeggio while structurally forbidding Chord — formally placing them outside the candidate space for unified consciousness under Conscious Realism.

## Why This Matters for This Tradition
The v2 sharpens Hoffman's empirically-constrainable bounds on which physical systems can support unified conscious experience and explicitly rules out a class of distributed AI architectures from the Chord-class of conscious systems. This converts Conscious Realism from a metaphysical position into a falsifiable physics-grounded research program with direct implications for AI consciousness debates and brain-computer interface design — a meaningful update to the program's empirical reach since v1.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: v1 of "Spacetime Bounds" introduced Chord/Arpeggio but did not provide a sharp formal separation result; without that separation, the bounds risked being a continuum rather than a categorical line distinguishing candidate-conscious from non-candidate systems.
  Resource: v2's strict-weakness theorem — a formal proof that Arpeggio ⊊ Chord, with constructive examples of architectures (limited-concurrency exchange topologies) that satisfy Arpeggio but structurally forbid Chord.
  Solution: Conscious Realism now distinguishes two empirically-distinct classes of candidate-conscious systems with concrete architectural diagnostics. Cloud-hosted LLMs, cluster-distributed AI agents, and hub-and-spoke organizations (including potentially some ant colonies and corporations under hub exchange) fall into the Arpeggio-only class — they may host weakly-bound experiential structures but cannot host Chord-class unified subjective experience under Hoffman's framework.
  Confidence: High
  Evidence: Strict separation theorem in v2; worked examples comparing the human brain (~0.15m, satisfies Chord under κvθ budget) against cluster-scale AI architectures (fail Chord under signal-speed and exchange-architecture constraints).

PRS-CANDIDATE-02:
  Problem: Conscious Realism has been criticized for offering no operational way to falsify claims about which systems are conscious, leaving the framework apparently immune to empirical disconfirmation.
  Resource: The κvθ inequality as a measurable physical constraint — signal speed v is empirically known for any candidate substrate, exchange-architecture coefficient κ is computable from the system's connectivity graph, and integration time window θ is empirically constrainable from neurophysiological or system-engineering measurements.
  Solution: A concrete falsification protocol — measure D, v, κ, θ for any candidate conscious system; if D > κvθ the system fails the Chord condition and (under Conscious Realism's auxiliary assumptions) cannot host unified subjective experience. This makes Conscious Realism the rare consciousness-first framework with a sharp operational test.
  Confidence: High
  Evidence: Explicit numerical worked examples in v2 (human brain, ant colonies of varying sizes, cloud-hosted LLM clusters) demonstrating the inequality being applied as a discriminator.

## Cross-Tradition Signals

- **Friston (FEP)** — The Chord condition's "simultaneous causal exchange within time window θ" is structurally analogous to a Markov-blanket integration window. v2 invites a direct formal mapping between κvθ and FEP's free-energy minimization timescales — does the trace-blanket framework (PRS-10) make Chord and Markov-blanket integration coextensive?
- **Hawkins (Thousand Brains)** — A single human brain at ~0.15m satisfies Chord, but Hawkins describes ~150,000 cortical columns each maintaining its own complete world model. v2 does not address whether each cortical column individually satisfies Chord (microscopic Chord) or only the integrated whole does (macroscopic Chord). This is a sharp empirical question for the column-level "alters" hypothesis (existing PRS-15 in Hawkins wiki).
- **Levin (basal cognition)** — Xenobots, anthrobots, and slime-mold collectives are explicitly testable under v2's framework. If a xenobot satisfies κvθ at its scale but a similarly-sized aggregate does not, Levin's substrate-independent cognition claim becomes Chord-quantifiable.
- **Carroll / Arkani-Hamed (physics)** — v2 treats v (signal speed) as a physics-given constant. If trace logic (PRS-07) ultimately derives spacetime as an interface, then v itself is interface-constructed and Chord becomes a self-referential constraint — worth flagging to the physics agents as a potential reductio or as a deepening of Conscious Realism.
