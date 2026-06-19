---
proposal_id: PROP-2026-06-19-002
thinker: Nima Arkani-Hamed
tradition_key: arkanihamed
source_type: paper
source_title: "Surfaceology / curve-integral formalism (All Loop Scattering For All Multiplicity; Surfaceology for Colored Yukawa Theory)"
source_url: https://arxiv.org/abs/2311.09284
source_date: 2024 (program); coverage gap as of 2026-06-19
searched_on: 2026-06-19
status: pending
---

> NOTE (autonomous run, fail-loud): No *newly authored* Arkani-Hamed primary source appeared in the past-30-day window. The two June/April hits that surfaced — arXiv:2606.19054 (a doctoral dissertation on the Dual Amplituhedron problem) and arXiv:2604.01133 (Li & Rodina) — build on his program but are NOT by him, so they fail the "from the thinker" filter. This proposal instead invokes the filter's second clause — "a significant work not yet captured" — to close a real coverage gap: the **surfaceology / curve-integral** program is absent from the captured PRS list (which jumps amplituhedron → cosmohedron/positive-geometry). Flagging for Tom's judgment on whether to ingest a non-recent backfill.

## Summary
"Surfaceology" is Arkani-Hamed's curve-integral reformulation of scattering amplitudes for colored theories (with Carolina Figueiredo and collaborators). Amplitudes are written as integrals over combinatorial data attached to surfaces decorated by kinematics, with no Feynman diagrams and no spacetime locality as input. A striking structural result: in the curve-integral form, the dependence on particle number n and loop order L effectively *decouples* — all-loop, all-multiplicity amplitudes in Tr(φ³) can be assembled from simple L-loop "tadpole-like" curve integrals combined with the tree result. The framework extends to Yang-Mills and Yukawa-type theories via "scaffolding" and "splits."

## Why This Matters for This Tradition
Surfaceology is the most recent major instance of Arkani-Hamed's central thesis — that physics can be reformulated without spacetime scaffolding — and it is currently a hole in this tradition's wiki. It is methodologically distinct from the amplituhedron (curve integrals / u-variables on surfaces rather than a single positive polytope) and is the engine behind much of the 2024–2026 follow-on literature (hidden zeros, splits, cosmohedra), some of which IS already captured (PRS-08). Capturing the parent program makes the existing children coherent.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Standard amplitude computation builds in spacetime locality and unitarity through Feynman diagrams, and scales explosively with particle number and loop order.
  Resource: The curve-integral / "surfaceology" formalism — amplitudes as integrals over combinatorial surface data (u-variables) decorated by kinematics, with no diagrams.
  Solution: Colored-theory amplitudes are computed directly from surface combinatorics, with locality and unitarity emerging as outputs rather than inputs — a second, diagram-free route to the post-spacetime claim beyond the amplituhedron.
  Confidence: High
  Evidence: "scattering amplitudes for colored theories can be expressed as integrals over combinatorial objects simply constructed from surfaces decorated by kinematic data" (curve-integral formalism, arXiv:2311.09284 and follow-ons).

PRS-CANDIDATE-02:
  Problem: Can the dependence of amplitudes on particle number (n) and loop order (L) be disentangled, making all-loop / all-multiplicity scattering tractable?
  Resource: The observation that the curve integral decouples n and L, reducing higher-loop computation to L-loop "tadpole-like" curve integrals (one particle per color trace-factor).
  Solution: All-n, L-loop amplitudes are obtained by combining tadpole-like curve integrals with the tree-level result — an all-multiplicity, all-loop counting-problem reformulation.
  Confidence: High
  Evidence: "the dependence on the number of particles, n, and the loop order, L, is effectively decoupled… it suffices to study the curve integrals for L-loop tadpole-like amplitudes… formulas for the all n amplitudes at L loops can be found." (arXiv:2311.09284)

## Cross-Tradition Signals
- **Wolfram (Ruliad / hypergraphs):** Surfaceology recasts QFT as combinatorics on surfaces — two independent post-spacetime programs (Arkani-Hamed's curve integrals and Wolfram's rewriting graphs) reaching for the same target object from opposite directions. This is the CROSS-002 convergence the wiki already wants tested, now with a concrete combinatorial (not just polytopal) handle.
- **Hoffman (interface / non-spacetime fundament):** The decoupling of n and L, and the derivation of locality/unitarity as outputs, sharpen the claim that spacetime is an interface-level appearance rather than the substrate.
- **Carroll convergence (note today's pairing):** Today's Carroll proposal (PROP-2026-06-19-001) speculates on the *spacetime interpretation* of a finite-dimensional quantum state; surfaceology supplies the complementary direction — deriving amplitude structure with spacetime removed. Worth flagging to the master wiki as a same-day two-physicist resonance on spacetime non-fundamentality.
