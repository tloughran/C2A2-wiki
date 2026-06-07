SEARCH-FOR-ASSUMPTION-273:
  Date searched: 2026-06-06
  Original item: ASSUMPTION-273
  Original statement: Sociogram LOCKED search semantics (highlight lens, never filter; checkboxes filter, search highlights, never sync — 2026-05-29) transfer correctly and should be inherited exactly by the 156-node Community Explorer graph.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-273
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated design commitment to inherit the sociogram's search-highlights/checkbox-filters lock into Community Explorer.
      15a: Searched HCI literature on search-as-highlight vs search-as-filter and on overview+detail / focus+context interaction.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Cockburn, Karlson & Bederson, 2008. "A Review of Overview+Detail, Zooming, and Focus+Context Interfaces." ACM Computing Surveys 41(1). — Establishes that preserving context while directing attention to a focus is a distinct, well-validated interaction goal; highlighting a focus within retained context (rather than removing non-matches) keeps the analyst oriented. Direct theoretical grounding for "highlight, never filter."
    2. Heer & Shneiderman, 2012. "Interactive Dynamics for Visual Analysis." Communications of the ACM / Queue. — Names cue-based techniques (highlight matches, deemphasize non-matches) as a first-class category distinct from filtering; supports treating search as a highlight lens layered over a stable view.
    3. Munzner, 2014. "Visualization Analysis and Design" (highlight vs filter idioms). — Distinguishes the "highlight" idiom (change appearance, keep all marks) from the "filter" idiom (remove marks); supports keeping search and checkbox-filter as separate, non-synced channels because they serve different manipulate-the-view intents.

  Strength of support: Moderate-Strong

  Summary: The HCI literature strongly supports the underlying principle of the locked semantics: highlighting search matches inside a retained context is a recognized, validated idiom that preserves orientation, and it is categorically distinct from filtering. Keeping search (highlight) and checkbox (filter) as separate, non-synchronized channels is consistent with treating them as different view-manipulation intents. This grounds the design choice itself. What the literature does NOT establish is the stronger clause — that the lock should be inherited "exactly" at a ~10x smaller scale — which is the scale-transfer bet carried by the inferred twin PRESUMPTION-307.

  Caveats: Support is for the highlight-preserves-context principle in general, where the dominant task is exploration/structure-reading. The literature's endorsement weakens when the dominant task is targeted retrieval (find a specific named node), where filtering can outperform highlight — exactly the "156 unlabeled dots need name lookup" framing CE states. So "the semantics are good" is supported; "inherit exactly, regardless of scale/task" is not.

  Recommendation: SUPPORTED
