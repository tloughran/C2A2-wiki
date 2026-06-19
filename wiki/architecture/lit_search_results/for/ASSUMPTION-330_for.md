SEARCH-FOR-ASSUMPTION-330:
  Date searched: 2026-06-19
  Original item: ASSUMPTION-330
  Original statement: "regen_sociogram.sh is the only supported regen path (hardcodes --summa, guards Summa-less builds); direct generate_visualization.py is forbidden."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-330
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the canonical-build-wrapper decision
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Paved road" / "golden path" platform-engineering practice (Netflix, Spotify, Google) — a single supported, opinionated wrapper that bakes in correct defaults reduces operator misconfiguration; teams are steered to the wrapper and away from raw entry points.
    2. Build-automation convention (Make targets, wrapper scripts, task runners) — encapsulating the correct invocation (required flags, guards) in one canonical command is standard; it prevents the "forgot the flag" class of errors.
    3. Configuration-as-code / sane-defaults guidance — embedding required configuration in a checked-in wrapper makes the safe path the easy path and the unsafe path require deliberate effort.

  Strength of support: Moderate-Strong

  Summary: A single canonical build wrapper that hardcodes required flags (--summa) and guards a known-bad configuration (Summa-less builds) is well-supported by the "paved road"/golden-path pattern and ordinary build-automation practice: centralizing the correct invocation prevents operator misconfiguration and makes the safe path the default. Support is strong for HAVING a canonical wrapper with guards.

  Caveats: Support is for the wrapper existing and being the recommended path. "direct generate_visualization.py is forbidden" is only as strong as its enforcement: if the underlying entry point remains runnable and "forbidden" only by convention/docs, the guarantee is bypassable and can drift from the wrapper. Strongest form: the guard lives in the entry point itself (refuse Summa-less builds) so even direct invocation is safe — convention-only forbiddance is the weaker version (cf. the convention-guard cluster, PRESUMPTION-366).

  Search scope: golden-path/paved-road tooling; canonical build wrappers; forbidding direct entry-point invocation; config-as-code guards. Comprehensive.

  Recommendation: SUPPORTED
