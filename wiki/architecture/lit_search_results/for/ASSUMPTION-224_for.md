SEARCH-FOR-ASSUMPTION-224:

  Date searched: 2026-05-25
  Original item: ASSUMPTION-224
  Original statement: "The connectivity/orphan metric should exclude `architecture/lit_search_results/` (machine-generated, unrouted) so the orphan count tracks real routing progress."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-224
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: original extraction of stated assumption
      15a: Searched for supporting literature (cycle 0)
    Current status: SEARCHED

  Supporting evidence found: Partial

  Sources:
    1. Measurement-construction methodology (DeVellis, "Scale Development," 2016). — Excluding items that cannot, by construction, exhibit the measured property is legitimate scope definition, not gaming, provided the exclusion rule is principled and pre-specified.
    2. Knowledge-graph / documentation-health literature on connectivity metrics. — Backlink/connectivity density is an established (if coarse) signal of how integrated a node is into a corpus.
    3. Signal-vs-noise practice in instrumentation. — Removing a systematically non-linkable, machine-generated subtree reduces a known noise source so the remaining count better reflects the routing process it is meant to track.

  Strength of support: Moderate

  Summary: There is a legitimate measurement-hygiene case: lit_search_results/ is machine-generated and never intended to be wiki-linked, so its files are structural non-participants in the backlink graph. Excluding a category that cannot exhibit the property being measured is defensible scope definition, and connectivity density is a recognized integration proxy in the documentation-health literature.

  Caveats: The hygiene case holds only if the exclusion is principled and fixed in advance, not tuned to make the metric look better. It does not address the deeper question (twin PRESUMPTION-246) of whether backlink density is a valid integration proxy at all.

  Recommendation: PARTIALLY-SUPPORTED
