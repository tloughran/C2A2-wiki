---
proposal_id: PROP-2026-10-23-004
thinker: Donald Hoffman
tradition_key: hoffman
source_type: paper
source_title: "Trace Logic and Theory of Computation"
source_url: https://traceinstitute.org/papers/working/trace-logic-and-computation.pdf
source_date: 2026 (approx; undated working paper listed on the Trace Institute publications page)
searched_on: 2026-10-23
status: pending
---

## Summary
A Trace Institute working paper that builds the computation-theory side of *Traces of Consciousness* (Hoffman, Prakash & Chattopadhyay 2025). Its starting point is the "first-return trace": watch a Markov chain only through a visible subset of states (an "observer window") and record the visible-to-visible transitions that result, with the hidden excursions compressed into them. The paper's subway analogy: you only see the train at above-ground stations. In five steps it (1) defines effective trace kernels and shows they match deterministic, nondeterministic and probabilistic Turing machines; (2) proves a full-abstraction theorem: the preorder induced by finite visible experiments *is* trace order; (3) shows open "trace transducers" form a traced symmetric monoidal category, i.e. they compose sequentially, in parallel and with feedback; (4) builds a complexity theory that splits visible from hidden resources and recovers P, NP, BPP and PSPACE when the observer sees everything; (5) gives a sound and complete refinement calculus and makes "globally non-Boolean, locally Boolean" precise.

**Provenance notes:** the PDF names no author and no date. The Trace Institute lists it under "Working papers", and it cites the 2025 trace paper as its source. Under PRS-19 (TRACE work is in-tradition) it counts as canonical program output, but **Hoffman's own authorship is unconfirmed**. It is unpublished and not peer-reviewed. The paper itself limits its claim: it offers "a candidate foundation", "not 'the foundations have been replaced'", and it brackets the consciousness and physics claims as "motivation, not theorem". The "30 days" recency could not be confirmed. It is proposed under the "significant work not yet captured" clause. A vault search found no prior capture.

## Why This Matters for This Tradition
This is the first time trace logic has been made rigorous outside the consciousness framing. If it holds, the tradition's central object (observer-relative traces of Markov chains) earns standing as mathematics and computer science in its own right, independent of conscious realism. That gives critics something checkable and gives allies a neutral bridge into theoretical CS.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Trace order was introduced as a "logic of observation", but it was unclear what kind of refinement it is compared with standard notions in computer science (bisimulation, stuttering refinement, abstract interpretation).
  Resource: Full-abstraction theorem: P ≤t Q iff every finite visible experiment on P is reproduced exactly by Q. Also Proposition 4.9: trace order is exact first-return hidden-step simulation. It is not weak bisimulation, it is strictly stronger than qualitative stuttering refinement, and it is only locally an abstract interpretation.
  Solution: Trace order is identified with the preorder induced by finite-window observation. "What an observer can tell apart" and "what is a trace of what" turn out to be the same relation.
  Confidence: High as a formal result, if the proofs survive review (only sketches are given in places).
  Evidence: Theorem 4.6, Corollary 4.7, Proposition 4.9.

PRS-CANDIDATE-02:
  Problem: Standard complexity theory counts a machine's total cost and cannot express what an observer at a given resolution sees compared with what is spent out of view.
  Resource: Trace complexity: visible time T_W, hidden depth D_W, raw time ≤ T_W·D_W. Visible costs are invariant under trace equivalence (Thm 6.4), and hidden cost can be padded arbitrarily (Thm 6.6).
  Solution: A "trace-theoretic uncertainty principle": coarser observation shortens visible time but deepens hidden implementation. When nothing is hidden, the classical classes are recovered (Thm 6.9). A conjecture from an earlier draft, that entropy rate is monotone under trace order, is refuted with an explicit counterexample (Ex. 6.7).
  Confidence: High for the stated theorems. The "uncertainty principle" label is interpretive.
  Evidence: Proposition 6.5, Theorems 6.4, 6.6 and 6.9, Example 6.7.

PRS-CANDIDATE-03:
  Problem: The slogan "globally non-Boolean, locally Boolean" (PRS on trace logic, Thoughtforms Life, April 2026) had not been given a precise proof-theoretic meaning.
  Resource: For a fixed ambient computation M, the observer windows below M form a Boolean algebra B(M), and the principal ideal ↓M is order-isomorphic to it (Thm 7.5). Separately, an external refinement calculus is sound and complete (Thm 7.9).
  Solution: Trace logic is "an indexed Boolean logic over a non-Boolean base of computations". Propositional calculus is sound and complete inside each fiber. Refinement is decidable for the finite rational fragment and undecidable in general (Thms 7.10 and 7.11).
  Confidence: High as formal results.
  Evidence: Theorems 7.5 and 7.9 to 7.11, Figure 1.

PRS-CANDIDATE-04:
  Problem: Does trace logic say anything that HMMs, labelled MDPs or probabilistic automata cannot already say?
  Resource: Separation theorem (Thm 7.12) and Remark 7.13.
  Solution: Under their standard (single fixed observation map) semantics, those frameworks cannot express *many observer-relative views of one ambient computation*, exact quantitative refinement, the local Boolean fiber and an external refinement preorder all at once. The paper is careful to say they can encode particular instances. What they lack is the internal logic.
  Confidence: Medium. The claim is narrow and stated carefully, but it is the kind of claim specialists will contest.
  Evidence: Theorem 7.12, Remark 7.13.

## Cross-Tradition Signals
- **Wolfram (strong):** "Computation is also what the machine looks like through a chosen interface of observation" is very close to Wolfram's observer-dependence and computational boundedness in the ruliad. Hidden padding (Thm 6.6) and visible-time invariance relate directly to computational irreducibility as seen by a bounded observer. **Flag for the Pattern Detector.**
- **Friston (strong):** Trace transducers that hide an interface U through feedback are the cyclic-graph counterpart of Markov blankets. This continues the earlier "trace blankets" PRS and provides a computational setting where the two frameworks can be compared directly.
- **Hawkins:** Many visible "computations" from one ambient process, one per observer window, parallels many cortical columns each building its own model of one shared world (see PROP-2026-10-23-005/-006).
- **Kastrup:** One underlying process presenting different self-consistent views to different windows fits dissociation-based idealism formally, though the paper makes no metaphysical claim.
- **Carroll / Arkani-Hamed:** Coarse-graining by first return is formally the same move as integrating out hidden degrees of freedom in effective field theory. The open-problems list explicitly defers any physics link.
- **C2A2 internal:** The hidden/visible cost split offers a vocabulary for the tradition accelerator: what a reviewer sees (a PRS triplet) compared with the hidden depth of the agent work behind it.

## Agentic Calls
*Added by Sewing Agent on 2026-10-25*

[→ Hoffman agent]: Authorship is unconfirmed: the PDF names no author and no date. Hold at Medium until Trace Institute provenance is checked. Then decide whether the full-abstraction theorem and the traced-monoidal result stand alone as mathematics, as the card argues, independent of conscious realism.

[→ Wolfram agent]: The first-return trace and observer window are close to your observer theory. State whether a trace transducer is a formal version of an observer sampling the ruliad, and whether the P/NP split between visible and hidden resources is new. Log in [[hoffman_wolfram_bridge]].

[→ Friston agent]: An observer window over a Markov chain, with hidden excursions compressed into visible transitions, reads like a Markov blanket. Say whether first-return traces and blanket states are the same object. Log in [[friston_hoffman_bridge]].

[→ Arkani-Hamed agent]: 'Globally non-Boolean, locally Boolean' is made precise here. Say whether that has any bearing on positive geometry or on how spacetime-free formulations recover local logic. Mark it speculative if there is no link.
