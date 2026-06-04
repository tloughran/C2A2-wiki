SEARCH-FOR-ASSUMPTION-267:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-267
  Original statement: Raising the Sociogram MAX_NODES cap from 2000 to 20000 is correct crash-proofing — the old 2000 cap would truncate the 2529-node graph, and 20000 is a safe ceiling current/near-term data will not reach while keeping the render stable.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-267
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the cap change (2000→20000) made so the 2529-node graph renders without truncation.
      15a: Searched headroom / safety-margin sizing for resource caps and force-directed render limits.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SRE headroom/capacity-planning guidance (sreschool.com headroom guide; oneuptime headroom planning). — A healthy system keeps a deliberate margin (commonly cited 15–30%) above current load; setting a ceiling comfortably above the present 2529 nodes is consistent with headroom-sizing practice.
    2. Capacity-vs-load distinction (octocore "Capacity vs Load"). — Endorses separating the present load from the configured limit; raising the cap so it does not bind on the real dataset is the correct direction for the immediate truncation defect.
    3. Crash-proofing rationale (validated_premises crash-proofing lineage; the original 2000 cap was itself a guard). — Removing a cap that truncates real data restores correctness of the primary artifact; a cap that silently drops nodes is worse than a higher cap for a graph that must show all triplets.

  Strength of support: Moderate

  Summary: The directional claim is well supported: keeping the node ceiling above current load (with headroom) is standard capacity practice, and the old 2000 cap was actively wrong because it would truncate a 2529-node graph the tool must display in full. Raising it fixes a real, observed defect. What the literature does NOT establish is the specific value 20000 as a "safe" ceiling — headroom guidance says the safe operating limit must be found by testing, not asserted (see PRESUMPTION-299 / 15b). Support is strong for "raise above 2529 with margin," weaker for "20000 is verified safe."

  Caveats: 20000 is a ~10x jump validated only at the 2529-node point; the ceiling between ~2.5k and 20k is uncharacterized, so the upper end is an assumed, not tested, safe limit. The cap also guards a real failure mode (render crash), so an untested-too-high ceiling can re-admit the crash it was meant to prevent.

  Recommendation: PARTIALLY-SUPPORTED
