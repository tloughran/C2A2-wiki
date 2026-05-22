SEARCH-FOR-ASSUMPTION-191:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-191
  Original statement: "regen_sociogram.sh refuses Summa-less builds; .gitignore *.bak* blocks backup commits."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-191
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: build guard (refuse Summa-less builds) and .gitignore *.bak* added as point guards.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Saltzer, J. & Schroeder, M. (1975). "The Protection of Information in Computer Systems." — Fail-safe defaults: deny/refuse on a missing precondition rather than proceed into a degraded state.
    2. Humble, J. & Farley, D. (2010). "Continuous Delivery." — Build-time invariants / guard checks that fail the build on a violated precondition are a core deployment-safety pattern.
    3. gitignore(5) documentation. — Pattern-based exclusion (*.bak*) is the standard mechanism for keeping derivative/backup artifacts out of version control.

  Strength of support: Strong

  Summary: Both guards are textbook fail-closed practice: refusing a Summa-less build is a fail-safe default (refuse rather than emit a degraded sociogram), and a .gitignore pattern is the canonical way to block backup-file commits. The mechanisms are correct and the practice is well supported. These are exactly the kind of cheap, local invariants that prevent a known degraded state.

  Caveats: Support is for the guards as good local practice; it does not certify they address the systemic question raised by PRESUMPTION-216 (point-guards vs root-cause ownership).

  Recommendation: SUPPORTED
