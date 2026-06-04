SEARCH-FOR-PRESUMPTION-297:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-297
  Original statement: [inferred] Cross-repo correctness is held by human memory + a handoff doc, not by tooling: the shipped/pushed Day-190 viz (wiki repo) depends on edits left UNCOMMITTED in the separate Summa 2026 repo, with no interlock binding the two.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-297
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated dependency — a pushed artifact relies on uncommitted edits in a second repo with no binding interlock.
      15a: Searched cross-repo / cross-artifact consistency and silent desync of dependent artifacts.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Artifact-synchronization research (Concordia DAS Lab, "Keeping Software Artifacts Synchronized with ArtifactSync"). — When a change in one place requires a matching change elsewhere and they are not committed together, inconsistencies appear: stale docs, broken builds, failing tests. Direct analogue of a viz depending on uncommitted edits in a second repo.
    2. Cross-project build-artifact dependency limitations (GitLab issue #14311). — Tooling for binding build artifacts across repositories is a recognized gap; cross-project dependencies are not transactional by default, so dependent artifacts can silently desync.
    3. Multi-artifact consistency verification (ACM Koli Calling 2025, "LLM-Based Multi-Artifact Consistency Verification"). — Treats cross-artifact consistency as a problem requiring explicit verification precisely because manual checks and CI "still leave gaps"; supports the claim that human memory + a handoff doc is a weak interlock.

  Strength of support: Strong

  Summary: The presumed vulnerability is well-grounded: cross-repository/cross-artifact dependencies have no transactional guarantee, and the literature documents exactly this silent-desync failure (a dependent artifact left inconsistent because its counterpart was not committed in lockstep). Relying on human memory plus a handoff note is recognized as a gap-prone interlock. The condition is real and the risk is named in the software-engineering literature — strong support that this is a genuine, not hypothetical, exposure. This sits in the same "absence/desync goes unverified" family as the run's other items.

  Caveats: Severity scales with frequency and number of contributors; for a single-author, low-frequency personal workflow a handoff note may be a tolerable interlock (see 15b). Support establishes the risk exists, not that it has already caused harm here.

  Recommendation: SUPPORTED
