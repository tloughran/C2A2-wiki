SEARCH-AGAINST-ASSUMPTION-330:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-330
  Original statement: "regen_sociogram.sh is the only supported regen path (hardcodes --summa, guards Summa-less builds); direct generate_visualization.py is forbidden."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-330
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the canonical-build-wrapper decision
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. "Paved road that isn't enforced is bypassable" (platform engineering) — a golden path only helps those who take it; if the raw entry point (generate_visualization.py) is still runnable and "forbidden" only by convention, the guarantee is one habit-lapse away from being violated, especially by new contributors or agents.
    2. Wrapper/underlying-tool drift — a wrapper that hardcodes flags can fall out of sync with the underlying script's evolving interface; the wrapper guarantees correctness only as long as someone maintains the coupling. Convention-level "only path" claims decay.
    3. Guard-by-convention vs guard-by-code — the strongest version puts the Summa-less guard in generate_visualization.py itself; a wrapper-only guard leaves the unsafe path reachable, which is the recurring weakness across this cohort (cf. PRESUMPTION-366).

  Strength of challenge: Weak-Moderate

  Summary: The wrapper is good practice, but "the ONLY supported path / direct invocation is FORBIDDEN" is enforced by convention, not code: the raw entry point remains runnable, the forbiddance is a social rule, and the wrapper can drift from the underlying script. The guarantee holds only while everyone obeys and someone maintains the coupling — which is exactly the failure mode golden-path literature warns about.

  Specific risks: A contributor or agent runs generate_visualization.py directly without --summa, producing a Summa-less build that the wrapper would have blocked; or the wrapper's hardcoded flags silently lag the script's real interface.

  Mitigations available: Move the guard into the entry point (generate_visualization.py refuses/ warns on Summa-less builds regardless of caller); add a CI/regen assertion that the produced artifact contains Summa nodes; keep the wrapper but make safety a property of the program, not of the documentation.

  STEELMAN:
    Strongest counterargument: Centralizing the correct invocation in one wrapper is precisely how you prevent operator misconfiguration; demanding that every entry point also self-guard is defense-in-depth gold-plating for a single-maintainer repo where the convention is cheap and effective right now.
    What would need to be true for C2A2 to be safe: The Summa-less failure mode is caught by code (entry point or post-build assertion), so taking the "forbidden" path cannot silently ship a bad artifact.
    How to test: Invoke generate_visualization.py directly without --summa; if it produces a publishable artifact with no guard tripping, the "forbidden path" is unenforced.

  Search scope: paved-road enforcement gaps; wrapper/underlying drift; guard-by-convention vs guard-by-code. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
