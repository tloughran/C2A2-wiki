---
proposal_id: PROP-2026-08-16-025
thinker: Nima Arkani-Hamed
tradition_key: arkanihamed
source_type: paper
source_title: "Surface Water Wave Scattering and the Hydrotope"
source_url: https://arxiv.org/abs/2606.28280
source_date: 2026-06-26
searched_on: 2026-08-16
status: pending
---

> RETRIEVAL NOTE. Authorship and date were verified directly against the arXiv abstract page
> metadata (`citation_author` list: Arkani-Hamed, Calisto, Ussembayev, Zhao, Zhou;
> `citation_date` 2026/06/26; "Submitted on 26 Jun 2026"), and cross-checked against the
> INSPIRE-HEP author record for Arkani-Hamed (recid 3174135), which lists this as his most
> recent paper before the already-captured flavor paper of 2026-07-29. **What was read is the
> abstract, the comments field, and the metadata — not the body of the paper.** Claims below
> that go beyond the abstract are marked accordingly. Comments field reports: 7 pages, 3
> figures, plus Supplemental Material and a GitHub repository (repository not inspected).

## Summary
Arkani-Hamed and four collaborators apply the machinery of high-energy scattering-amplitude
theory to a completely classical, non-relativistic system: gravity waves on the surface of deep
water. Restricting to one horizontal dimension and to what they call the "two-negative-wavenumber
sector," they obtain a closed-form expression for the tree-level scattering amplitude of any
number *n* of waves. Up to a kinematic prefactor, that amplitude is the **volume of a polytope** —
specifically a box sliced by a hyperplane, which they name the **hydrotope**. The polytope's job,
in their words, "is simply to organize the sign patterns of the 'chambers'" — the distinct regions
into which the two-minus kinematic space divides. The result resolves a long-standing puzzle from
Y. V. Lvov's 1997 computation of five-wave amplitudes, and unifies and extends that computation to
all multiplicities. The abstract also states plainly that the general formula "was discovered by
Claude Opus 4.6 working under our guidance," starting from the authors' own one-term expression
valid in the simplest kinematic chamber.

## Why This Matters for This Tradition
The tradition's central conjecture is that scattering amplitudes are shadows of a positive
geometry that is logically prior to spacetime and quantum mechanics; the standing objection is
that this could be an accident of a few highly symmetric quantum field theories. A polytope-volume
formula for **classical water waves** — a system with no supersymmetry, no relativity, no quantum
mechanics, and a messy real-world dispersion relation — is the first evidence captured in this
wiki that the amplitude-as-volume pattern reaches outside fundamental physics entirely. Separately,
this is the first source in the tradition in which an AI system is named as the agent that found
the result, which bears directly on the wiki's own questions about machine participation in
inquiry.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Is the "amplitude = volume of a positive geometry" pattern a special feature of
    supersymmetric or otherwise fine-tuned quantum field theories, or a general property of
    scattering processes as such?
  Resource: The *hydrotope* — a box in the relevant kinematic space cut by a single hyperplane —
    whose volume, up to a kinematic prefactor, equals the n-wave tree amplitude for deep-water
    surface gravity waves in one horizontal dimension, in the two-negative-wavenumber sector.
  Solution: A positive-geometry representation is exhibited for a classical, non-relativistic,
    non-quantum system, extending the program's core claim well outside the class of theories
    where it was developed.
  Confidence: High
  Evidence: Abstract, verbatim: "Up to a kinematic prefactor, the amplitude is the volume of a
    classic polytope -- a box sliced by a hyperplane, which we dub the hydrotope."

PRS-CANDIDATE-02:
  Problem: Y. V. Lvov's 1997 five-wave amplitude computation produced an expression whose
    structure nobody had been able to explain or generalize to higher wave number.
  Resource: A chamber decomposition of the two-minus kinematic space, with the hydrotope's facet
    structure encoding which sign pattern holds in each chamber, yielding a single closed formula
    valid for all n.
  Solution: The 1997 puzzle is resolved: the five-wave result is recovered as one case of a
    general all-multiplicity formula, and the apparent complexity is relocated into chamber
    combinatorics rather than the dynamics.
  Confidence: High
  Evidence: Abstract, verbatim: "Our results resolve the puzzle raised by Y.V. Lvov's 1997
    computation of the five-wave amplitudes, unifying and extending it to all multiplicities."

PRS-CANDIDATE-03:
  Problem: Can a large language model do the generalizing step in front-line theoretical physics —
    moving from a special-case expression to the general law — rather than only assisting with
    algebra or literature?
  Resource: A human-set-up problem (the one-term expression in the simplest chamber) handed to
    Claude Opus 4.6 under the authors' guidance, with the model tasked to find the general formula.
  Solution: The authors credit the model with the discovery of the general n-wave formula, which
    they then organize geometrically as the hydrotope. This is a documented instance of
    AI-as-discoverer inside a named research program, not a claim about AI in the abstract.
  Confidence: Medium
  Evidence: Abstract, verbatim: "The general formula was discovered by Claude Opus 4.6 working
    under our guidance, beginning with our earlier discovery of a one-term expression valid in
    the 'simplest' kinematic chamber." Confidence is Medium rather than High only because the
    division of labor between the human framing and the model's contribution is described in one
    sentence of the abstract and is not verifiable from the material read here; the body of the
    paper and the GitHub repository may qualify it.

## Cross-Tradition Signals
- **Wolfram.** Wolfram's ruliology holds that simple rules generate structure discoverable only by
  running them, and his recent "Towards a Theory of Bugs" work leans on exhaustive search over rule
  space. The hydrotope is the mirror case: an exhaustively-messy classical system turning out to
  have a compact combinatorial skeleton after all. The two programs disagree about how often
  irreducibility can be circumvented, and this paper is a data point on Arkani-Hamed's side of that
  disagreement — worth pairing with Wolfram's computational-irreducibility claims rather than
  reading either alone.
- **Carroll.** Poetic naturalism's core move is that higher-level descriptions can be exactly as
  real as lower-level ones when they are the right way to carve the system. A polytope volume
  governing water waves is a case where the *useful* description is not the one nearer the
  fundamental level — the fluid equations — but a geometric one with no obvious ontological
  standing. Carroll's emergence criteria have not been tested against a case of this shape.
- **Hoffman.** Hoffman's decorated-permutation and amplituhedron borrowings assume the positive
  geometry sits *beneath* spacetime, as evidence that spacetime is an interface artifact. If the
  same geometry organizes water waves — which are unambiguously *in* spacetime — that inference
  weakens, or at least needs a further premise. This is a signal that cuts against a live
  cross-tradition bridge and should be recorded as such, not smoothed over.
