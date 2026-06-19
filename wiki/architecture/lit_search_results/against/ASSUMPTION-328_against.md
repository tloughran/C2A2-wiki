SEARCH-AGAINST-ASSUMPTION-328:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-328
  Original statement: "Single-source-of-truth bios — read the pop-up summary from the same wiki.md the agents maintain, so 'no second copy to drift'."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-328
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the SSOT data-architecture decision
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. SSOT coupling critique (software architecture) — SSOT removes duplication but COUPLES consumers to the source's internal format. The user-facing view now depends on the agents' working-doc structure (heading names, `**Summary**` block syntax); an internal refactor silently breaks the derived view. Drift is replaced by a parse-contract dependency.
    2. "One source serving two masters" — when a single artifact must satisfy both an internal working purpose (agent maintenance) and an external presentation purpose (user bio), the two purposes can pull the format in incompatible directions; the single source becomes a constraint, not just a convenience.
    3. Robustness-vs-DRY tradeoff — eliminating the second copy also eliminates the buffer that would let the presentation layer be curated independently of the (possibly messier) working notes; tight coupling can reduce resilience.

  Strength of challenge: Weak-Moderate

  Summary: SSOT is sound, but the challenge is that it relocates rather than removes the failure mode: instead of two copies drifting, the derived view is now coupled to the source's parse contract, and the wiki.md must simultaneously serve agent-maintenance and user-presentation. A refactor of the working doc can break the pop-up with no second copy to warn anyone. "No copy to drift" is true; "no coupling to manage" is not.

  Specific risks: A future change to wiki.md structure breaks the pop-up extraction silently; the bio quality is hostage to whatever shape the agents' working notes take.

  Mitigations available: Define and test an explicit extraction contract (stable heading/marker for the Summary block); add a parse/fidelity check in regen so a structural change fails loudly rather than silently; keep the source authoritative but treat the extraction boundary as a tested interface.

  STEELMAN:
    Strongest counterargument: A second curated copy is exactly what rots — duplicated bios diverge the moment either side is edited, and no discipline reliably keeps two copies in sync; one authoritative source with a derived view is the only structurally drift-free option, and the parse-contract coupling is a small, testable surface compared with perpetual two-copy reconciliation.
    What would need to be true for C2A2 to be safe: The extraction boundary (which block, which markers) is explicit and verified by the regen pipeline, so a source refactor fails loudly.
    How to test: Refactor the wiki.md Summary block format and confirm regen/verify FAILS rather than silently emitting an empty or wrong pop-up.

  Search scope: SSOT coupling critiques; single-source-serving-two-purposes; DRY-vs-robustness tradeoffs. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
