SEARCH-AGAINST-PRESUMPTION-358:
  Date searched: 2026-06-17
  Original item: PRESUMPTION-358
  Original statement: "[inferred] Making all 269 nodes individually resolvable increases fidelity (visual resolvability = informational fidelity)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-358
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated equation resolvability = fidelity
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Graphical perception (Cleveland & McGill 1984) — once nodes are individually placed, their POSITIONS are decoded as quantitative; resolving 269 nodes by an arbitrary fan injects positions that get read as structure, LOWERING fidelity (false signal) while raising legibility. Resolvability and fidelity are different axes.
    2. Overview-vs-detail / aggregation (Shneiderman; clutter research) — forcing all 269 to be individually resolvable can increase clutter and HARM the viewer's ability to read aggregate structure; "show every item" is not the same as "show the information," and can reduce it.
    3. Trace-vs-substance error (the project's own recurring failure mode) — equating a visible trace (every node rendered) with the substance (true informational content) is the same conflation flagged in prior dispositions; visibility of items != fidelity of meaning.

  Strength of challenge: Moderate-Strong

  Summary: The equation "resolvability = fidelity" is challenged on two axes. Perceptually (Cleveland & McGill), individually placing 269 nodes makes their incidental positions readable as structure, so resolvability can ADD spurious signal — negative fidelity. Informationally (overview/clutter research), "show every item" can bury aggregate structure and reduce what the viewer actually extracts. Resolving identity is a real but narrow legibility gain (15a); equating it with informational fidelity is the trace-vs-substance error.

  Specific risks: Viewers infer structure from the resolving layout (couples ASSUMPTION-327's fan); clutter from 269 individually-resolved nodes hides real pattern; the system mistakes "everything is visible" for "the picture is faithful."

  Mitigations available: Decouple the two goals — provide identity-resolution on demand (hover/zoom/detail) while the default view shows faithful aggregate structure; mark incidental positions as non-semantic; evaluate fidelity by what viewers correctly infer, not by whether every node is drawn.

  STEELMAN:
    Strongest counterargument: If individual nodes carry real identity that the viewer needs, then collapsing them loses information, and making each resolvable is the only way to show that information faithfully — so for an identity-bearing dataset resolvability genuinely does serve fidelity.
    What would need to be true for C2A2 to be safe: The per-node identity is actually needed at the default zoom AND the positions used to resolve them are either meaningful or clearly marked incidental, so resolving identity does not smuggle in false structure or clutter.
    How to test: Ask whether viewers need all 269 identities at once (vs on demand); test whether the resolved layout makes them infer non-existent structure or miss real aggregate pattern.

  Search scope: positional-encoding perception; overview-vs-detail/clutter; trace-vs-substance. Comprehensive. (Couples ASSUMPTION-327.)

  Recommendation: CHALLENGED
