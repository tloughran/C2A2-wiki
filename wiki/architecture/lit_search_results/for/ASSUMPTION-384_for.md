SEARCH-FOR-ASSUMPTION-384:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-384
  Original statement: "The 2,337 orphan count is an artifact of excluding shared-reference edges + counting structural/inbox pages that shouldn't carry backlinks - not a real knowledge-graph deficit."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-384
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: orphan metric framed as edge-type + page-population artifact rather than deficit
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Network-analysis methodology (no single agreed connectivity metric; edge-weight/edge-type choice is decisive). - Connectivity results, including isolate/orphan counts, are sensitive to which edge type is admitted; excluding a whole edge class (shared references) demonstrably changes the orphan tally, supporting the "artifact" framing.
    2. Wikipedia/wiki network-analysis practice (HITS/PageRank on link graphs). - Structural and namespace pages are routinely treated differently from content pages in link analysis, supporting the claim that counting structural/inbox pages as expected-backlink nodes inflates an orphan metric.

  Strength of support: Moderate

  Summary: The dependence of an orphan count on edge-type inclusion and on which pages are deemed "should-have-backlinks" is well established in network analysis: isolate counts are a function of the chosen edge set and node population, not an objective fact. This supports the claim that excluding shared-reference edges and counting structural/inbox pages mechanically inflates the orphan number. Literature supports the mechanism; it cannot certify that ALL 2,337 are spurious - some may be genuine content orphans.

  Caveats: "Artifact" is a partial truth: edge-type choice inflates the count, but the same literature warns that a recomputation may still leave a real residual of content orphans. Supports "overstated," not "non-existent."

  Search scope: Connectivity metric sensitivity; namespace/structural-page handling; isolate definition. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
