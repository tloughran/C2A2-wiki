SEARCH-AGAINST-ASSUMPTION-123:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-123
  Original statement: "Whiteboard plots (Pathway 05) ephemeral by default + Pin-this promotion + per-plot export (PNG/SVG/HTML/CSV/PDF)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-123
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 05 whiteboard design
      15b: Searched for counter-evidence on ephemeral-default for derivative-realization use cases
    Current status: CHALLENGED

  Sources:
    1. Bruce et al. (2004) and Capra & Pérez-Quiñones (2005) re-finding research — users routinely fail to recognize derivative value in real time; ephemeral-default produces lost-work events.
    2. Thaler & Sunstein (2008) "Nudge" — default direction has normative weight; choosing ephemeral over persistent is itself a substantive design claim.
    3. Jupyter cell-output persistence research (2020-2024) — auto-save / auto-persist with auto-cleanup is the canonical compromise; pure ephemeral is recognized as risky.
    4. Discoverability research on "pin" affordances — discoverability failure is well-documented; users miss the pin button precisely when value is most evident.
    5. PRESUMPTION-156 paired — inverse-default not audited.

  Strength of challenge: Moderate

  Summary: Pure ephemeral-default puts the burden of value-recognition on the user in real time, but the re-finding literature shows users routinely fail at this. The canonical compromise is auto-persist + auto-cleanup, not pure-ephemeral. Pin-this discoverability is itself a known UX failure mode. The export option helps but only if the user pinned-or-exported in time. Moderate challenge.

  Specific risks: (a) Lost-work events on session-end; (b) Pin discoverability failure; (c) Real-time value-recognition is hard; (d) "By default" sets normative weight.

  Mitigations available: (a) Auto-persist with auto-cleanup; (b) Higher-visibility pin affordance; (c) Last-N-plots automatic recovery; (d) Configurable default per user mode.

  Recommendation: CHALLENGED (Moderate) — ephemeral-default has known failure mode; auto-persist with auto-cleanup is the canonical compromise

  STEELMAN:
    Item: ASSUMPTION-123
    Strongest counterargument: Ephemeral-default requires users to recognize value in real time, but the canonical re-finding research shows this is exactly what users fail at. The "Pin-this" affordance optimizes the wrong axis: it assumes the user notices value, when the literature shows they often don't. Auto-persist with auto-cleanup (e.g., last-N-plots auto-saved, cleaned after M days unless pinned) gives the same clutter management with better failure characteristics.
    What would need to be true for C2A2 to be safe: (a) Pin-this discoverability validated; (b) Auto-recovery for last-N plots; (c) Default reversibility per user mode.
    How to test: Usability test with derivative-recognition scenarios; measure pin-rate vs. retrospective-want-rate.
