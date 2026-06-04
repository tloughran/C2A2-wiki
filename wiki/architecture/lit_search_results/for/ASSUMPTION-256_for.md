SEARCH-FOR-ASSUMPTION-256:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-256
  Original statement: Sociogram interaction model locked (Tom: 'leave the current model'): search/focus: is a transient highlight-in-place lens; checkboxes are hard filters; the two do not sync.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-256
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched transient-lens vs persistent-filter separation patterns in graph UIs.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Furnas (1986), 'Generalized Fisheye Views' — establishes the focus+context distinction: a transient lens and a persistent selection are legitimately separate interaction layers.
    2. Shneiderman (1996), 'The Eyes Have It' (visual information-seeking mantra) — overview/filter/details-on-demand treats filtering and highlighting as distinct operations.
    3. Heer & Shneiderman (2012), 'Interactive Dynamics for Visual Analysis' (CACM) — brushing/highlighting and filtering are catalogued as separate, complementary interaction idioms, supporting a non-syncing two-control design.
    4. Munzner, 'Visualization Analysis and Design' — highlight (reversible, transient) vs filter (stateful) are standard, intentionally distinct manipulations.

  Strength of support: Moderate-Strong

  Summary: The transient-lens-vs-persistent-filter separation is a well-established and intentional pattern in the visualization literature (Furnas, Shneiderman, Heer & Shneiderman, Munzner). Treating search/focus as reversible highlight-in-place and checkboxes as stateful hard filters maps directly onto the recognized highlight-vs-filter idiom, so the locked model is grounded in canonical HCI practice.

  Caveats: Literature endorses the separation as coherent; it does not certify that two visibility-affecting controls that do not sync are free of user confusion (see AGAINST).

  Recommendation: SUPPORTED
