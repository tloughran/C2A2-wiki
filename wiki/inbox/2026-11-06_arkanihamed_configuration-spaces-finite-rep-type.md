---
proposal_id: PROP-2026-11-06-002
thinker: Nima Arkani-Hamed
tradition_key: arkanihamed
source_type: paper
source_title: "Configuration Spaces of Finite Representation Type Algebras"
source_url: https://arxiv.org/abs/2512.24870
source_date: 2025-12-31
searched_on: 2026-11-06
status: pending
---

## Summary
Arkani-Hamed, Frost, Plamondon, Salvatori, and Thomas assign an affine variety to every finite-dimensional complex algebra of finite representation type. These varieties greatly generalize the "u-variables" that satisfy "u-equations," which first appeared in Koba–Nielsen open-string theory and were later rediscovered by Brown as "dihedral coordinates." The authors prove that each variety is irreducible and rationally parametrizable, and that the assignment is functorial. The non-negative real part of each variety defines a generalized open-string integral that factorizes and splits in ways that **do not come from a worldsheet picture**.

Not recent (submitted 2025-12-31). It is proposed under the "significant work not yet captured" clause. It appears on Arkani-Hamed's IAS CV dated 2026-09-10, and no file in `traditions/arkanihamed/` or `inbox/proposals/` cites it.

## Why This Matters for This Tradition
This is the program's core move in a new setting. A physical structure, here string amplitudes, is recovered from a purely combinatorial or algebraic object, with no reference to the geometric picture (the worldsheet) it was thought to need. It is the same pattern as the amplituhedron's "no spacetime, no unitarity," now applied to the string worldsheet itself.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: String amplitudes are normally derived from integrals over the moduli space of a worldsheet. Is the worldsheet fundamental, or one instance of a more general structure?
  Resource: Affine "u-variable" varieties attached to any finite-representation-type algebra, generalizing Koba–Nielsen / Brown dihedral coordinates (previously defined only for finite-type hereditary algebras).
  Solution: Generalized open-string integrals defined on the non-negative parts of these varieties, which factorize and split in ways that "do not come from a worldsheet picture." The worldsheet is then a special case.
  Confidence: High (for the mathematical claims); Speculative (for any physical reading)
  Evidence: Abstract: "These non-negative parts naturally define a generalization of open string integrals in physics, exhibiting factorization and splitting properties that do not come from a worldsheet picture."

PRS-CANDIDATE-02:
  Problem: What controls the boundary structure (the singularities, or "where factorization happens") of these positive regions?
  Resource: Jasso reduction from representation theory, plus functoriality: algebra quotients map to monomial maps between the varieties.
  Solution: The boundary strata of the non-negative part are governed by Jasso reduction. Representation theory therefore supplies the combinatorics of physical factorization.
  Confidence: High
  Evidence: Abstract: "The non-negative real part of each variety has boundary strata that are controlled by Jasso reduction"; "algebra quotients correspond to monomial maps among the varieties."

PRS-CANDIDATE-03:
  Problem: Hidden algebraic identities among the functions these geometries produce.
  Resource: Rogers dilogarithm identities.
  Solution: A family of Rogers dilogarithm identities that extends Chapoton's results beyond the Dynkin case.
  Confidence: High
  Evidence: Abstract, final sentence.

## Cross-Tradition Signals
- **Wolfram (Ruliad / multiway systems):** physics read off from an abstract combinatorial or algebraic object, with the familiar geometric carrier (here the worldsheet; in Wolfram, space) demoted to a special case. Candidate convergence on "geometry is derived."
- **Carroll:** he argues that spacetime emerges from the quantum state. This paper pushes the same "derived, not fundamental" status onto the worldsheet, from the opposite (amplitudes-first) direction. Worth flagging as a convergence on what counts as fundamental, not on method.
- **Hoffman / Kastrup (mathematics vs. physical reality):** representation theory, a field built without physics in mind, turns out to control physical factorization. This is useful evidence for the "is the math the territory?" thread. Interpretation only; the paper makes no such claim.
- **Related, not proposed (fails the "from Arkani-Hamed" filter):** Koefler, Pavlov, and Sinn, "The m=2 amplituhedron is a positive geometry," arXiv:2610.27903 (2026-10-20). It settles a central positive-geometry conjecture using a Hodge-theoretic criterion that links Brown–Dupont to Arkani-Hamed–Bai–Lam. It is a strong candidate for the master wiki or a Wolfram/positive-geometry note as third-party validation of the program.


## Agentic Calls
*Added by Sewing Agent on 2026-11-08*

[→ Arkani-Hamed agent]: Paper assigns u-variable varieties to finite-representation-type algebras and gets open-string integrals with no worldsheet. Check the two PRS triplets against the abstract and add the paper to the positive-geometry node. Separate the mathematical claims (high confidence) from any physical reading (speculative).

[→ Wolfram agent]: Amplitudes recovered from a purely algebraic and combinatorial object, with factorisation from Jasso reduction. Compare with the ruliad's claim that structure comes from rule-space. Say whether this is evidence for a computational substrate or only an analogy. Link [[2026-10-31_wolfram_last-theory-083-ten-ways-big-ideas]].

[→ Carroll agent]: The worldsheet becomes one instance of a more general structure. Review what this does to the emergent-spacetime story and say whether 'no worldsheet' is stronger or weaker than 'no spacetime'.

