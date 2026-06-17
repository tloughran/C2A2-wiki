SEARCH-FOR-ASSUMPTION-322:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-322
  Original statement: "PRS-triplet production = first git appearance of each (tradition, PRS-NN) in traditions/*/prs_triplets.md."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-322
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the operational definition dating PRS production to first git appearance
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (partial)

  Sources:
    1. Mining-software-repositories (MSR) practice — using a file's/entity's first commit as its creation date is the standard, reproducible operationalization in repository-mining and software-evolution studies; git's first-appearance timestamp is the conventional "introduction" event for an artifact. Supports first-git-appearance as an accepted, well-defined production proxy.
    2. Scientometrics creation-dating — bibliometrics routinely dates a contribution to its first recorded appearance (deposit/publication date). Dating an artifact to first appearance in the authoritative store is an established and defensible convention.
    3. Lehman's laws of software evolution (Lehman & Belady) — software entities have identifiable introduction events in version history; counting introductions is a recognized way to characterize the growth of a system over time. Grounds "first appearance = a production event."

  Strength of support: Moderate

  Summary: First-git-appearance is an accepted, reproducible operationalization for dating the creation of a versioned artifact, used routinely in MSR and software-evolution work and analogous to first-appearance dating in scientometrics. As a deterministic, auditable rule it satisfies the basic requirements of a production metric: it is well-defined, replayable from the repository, and pinned to a single authoritative store (traditions/*/prs_triplets.md). The support is for "first appearance is A defensible production event," not for "first appearance is THE only meaningful event" (that stronger claim is the province of PRESUMPTION-355).

  Caveats: Support holds only where the authoritative store is the locus of creation. Pre-VCS work, content authored elsewhere and pasted in a single commit, and triplets created-then-renamed all date to the moment of git capture, not conceptual creation (couples PRESUMPTION-359 on completeness, ASSUMPTION-323 on verification). The convention is sound; its fidelity depends on the workflow actually routing creation through git.

  Search scope: MSR first-commit dating; scientometric first-appearance dating; software-evolution introduction events. Comprehensive at the conceptual level.

  Recommendation: PARTIALLY-SUPPORTED
