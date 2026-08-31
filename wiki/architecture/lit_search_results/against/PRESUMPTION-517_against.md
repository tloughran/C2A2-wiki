SEARCH-AGAINST-PRESUMPTION-517:
  Date searched: 2026-08-29
  Original item: PRESUMPTION-517
  Original statement: [inferred] Recovery source and corrupted instrument are the same artifact.

  SCOPE NOTE (load-bearing, applies to every item in this run):
    Two limbs. (1) The internal-empirical claim about this repository's file state: NOT-SEARCHED,
    literature cannot adjudicate it. (2) The generalizable question named by the item's own
    "Search targets" line: searched here. The item is NOT retagged [MISROUTED-INTERNAL-EMPIRICAL];
    REVISE-408's authorisation request to Tom stands untouched.

  INDEPENDENCE CAVEAT: 15a and 15b ran in the same process this run — a stronger coupling than the
    read-channel coupling the standing 15a/15b correlation discount was written for. Where this
    search agrees with 15a, that agreement is worth LESS than usual and 15c discounts it.
  EVIDENCE GRADE: snippet-level search results only. Zero full-text reads, zero abstract-level reads.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-517
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: original extraction/inference (2026-07-21 cohort)
      15b: Searched for challenging literature on the generalizable limb only (2026-08-29); internal-empirical limb NOT-SEARCHED
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Gasti & Marcon / 'RecuperaBit: Forensic File System Reconstruction Given Partially Corrupted Metadata.' — reconstructs directory structures from partially damaged metadata successfully in all tested cases, often outperforming commercial tools. Partial corruption does not imply unusability.
    2. Forensic practice on DMDE and comparable tools: file systems are frequently rebuilt even where metadata is partially damaged, with manual repair available where automatic detection misses incongruences.
    3. Requirements-engineering artifact-recovery literature (arXiv 2304.04670; 2406.01055): where artifacts are unavailable, documented pragmatic reconstruction with the unavailability and its reasons recorded is established, accepted practice rather than a failure.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is bounded and does not touch the core. Nothing found disputes that a compromised artifact cannot INDEPENDENTLY CONFIRM itself. What the literature adds is that partial corruption is routinely survivable: reconstruction from a partly damaged source is standard forensic work, and where no independent source exists, documented reconstruction with the limitation recorded is accepted practice rather than something to refuse. The decisive question the presumption does not ask is whether the corruption and the needed data are in the SAME dimension — here the position-ID defect corrupts card-to-button BINDING, while the recoverable content (which proposals existed, and their live URLs) may sit in an unaffected dimension. If so the review page is a usable but unconfirmed source, which is a different verdict from unusable.

  Specific risks: Over-reading the presumption leads to discarding the only surviving evidence about the two lost proposals on a purity argument, making an arguably recoverable loss permanent. Under-reading it leads to recording reconstructed dispositions as if confirmed.

  Mitigations available: Both are avoided by the same move: reconstruct from the review page, verify against the live URLs directly (bypassing the card mapping, as the item's own in-house test proposes), and label the result RECONSTRUCTED-UNCONFIRMED wherever the second source is silent.

STEELMAN:
  Item: PRESUMPTION-517
  Strongest counterargument: Strongest counterargument: the presumption proves too much. On its logic, no artifact touched by any defect may inform any recovery — which would forbid most of digital forensics, a field whose normal condition is reasoning from damaged sources. The discipline's answer is not to refuse the source but to bound the claim: use it, name the corruption, and mark what remains unconfirmed. C2A2's own PREMISE-096 already says this correctly ('or independent is nominal only') — it forbids self-CERTIFICATION, not self-derived evidence.
  What would need to be true for C2A2 to be safe: Safe if reconstruction proceeds but outputs are labelled RECONSTRUCTED-UNCONFIRMED unless corroborated by the live URLs read independently of the card mapping.
  How to test: Establish whether the position-ID defect affects proposal CONTENT rendering or only card-to-button binding. If only binding, the content dimension is uncorrupted and the page is a usable source.

  Recommendation: PARTIALLY-CHALLENGED
