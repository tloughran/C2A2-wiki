SEARCH-AGAINST-ASSUMPTION-137:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-137
  Original statement: "Pathway 13 (Under-Development Visualizer) is architecturally distinct from Pathway 25 (Meta-Visualization of Pathways); different audiences and data substrates"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-137
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 25 architectural-distinctness commitment
      15b: Searched for counter-evidence on pathway-distinctness sustainability over user-population overlap
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Sources:
    1. Multi-tool sprawl studies (Berlin 2017 "Tools and Their Maintenance") — distinct tools for related domains accumulate maintenance debt; users often want unified views.
    2. Jira / GitHub Projects evolution — many development-tracking tools have absorbed architectural-overview features over time; user demand for unified views is strong.
    3. PRESUMPTION-174 paired — Pathway 25 self-loop blurs the audience distinction (the meta-viz visualizes itself, including its own development state).
    4. User-population overlap: in a small project (Carpathi Wiki), the user-population for Pathway 13 (dev team) and Pathway 25 (researcher) may be 100% overlapping — Tom is both.
    5. Maintenance cost: two distinct visualization tools double the maintenance burden — relevant given PRESUMPTION-179 dual-maintenance concerns.
    6. Conway's Law: architectural distinctness reflects organizational distinctness; in a single-developer project, the distinction is harder to maintain.

  Strength of challenge: Weak-to-Moderate

  Summary: Architectural-distinctness claim is sound under canonical visualization design but faces sustainability concerns in C2A2's specific context: small user-population, recursive Pathway 25 self-loop, and dual-maintenance burden. The distinction is correct at design-time but may collapse in practice when the dev-team-user and researcher-user are the same person, or when Pathway 25 visualizes itself (PRESUMPTION-174). Weak-to-Moderate challenge: not refuting the design intent, but flagging that the distinction may need re-evaluation after second-pass use.

  Specific risks: (a) Dual-maintenance burden; (b) User-population overlap (Tom is both audiences) may not justify two tools; (c) Pathway 25 self-loop blurs the audience distinction; (d) Feature creep — over time, tools tend to absorb each other's features.

  Mitigations available: (a) Shared visualization primitives (D3 force-layout, color palette) even if entry points are distinct; (b) Re-evaluate distinctness after 1-2 use cycles; (c) Pathway 25 explicit non-overlap with Pathway 13's substrate; (d) Accept that distinctness may be design-time-only and converge later.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate) — design-time distinction sound; sustainability under single-user / recursive-self-loop conditions is the concern

  STEELMAN:
    Item: ASSUMPTION-137
    Strongest counterargument: Audience/substrate-driven distinction is canonical visualization design, but the canonical principle assumes distinct user-populations. In C2A2, the user-population is largely Tom — both as dev-team-user (Pathway 13) and researcher-user (Pathway 25). The substrate distinction is real (development-state vs. pathway-as-object) but may be better expressed as two views in one tool rather than two architecturally distinct tools. The dual-maintenance burden is significant given PRESUMPTION-179 reference-instance sustainability concerns. The commitment is right in principle but may be wrong in implementation grain.
    What would need to be true for C2A2 to be safe: (a) User-population separation actually exists (current state: no); (b) Distinct tools share visualization primitives to amortize maintenance; (c) Pathway 25 self-loop scoped to not duplicate Pathway 13 substrate.
    How to test: After Pathway 13 and Pathway 25 are both prototyped, measure feature overlap and maintenance cost; consider merging if overlap > 60%.
