SEARCH-AGAINST-PRESUMPTION-415:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-415
  Original statement: "[inferred] That directory path + file size reliably indicate a page's content type and synthesis value (folder taxonomy treated as ground truth; no misfiled/mis-sized content)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-415
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: folder path + size treated as ground truth for content type/value
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Folder-taxonomy decay in growing repositories. - Well-organized folder structures "rarely work for long" as a repository grows; location drifts from content, so path is not a reliable ground-truth signal.
    2. Metadata-incompleteness mislabeling. - Metadata-based classification "risks mislabeling when metadata is incomplete or incorrect"; treating taxonomy as ground truth ignores this documented failure mode.
    3. File size as a weak content signal. - Size does not encode content TYPE or synthesis VALUE; a terse high-value seed and a terse stub are indistinguishable by size, so the size axis is especially unreliable.

  Strength of challenge: Moderate-Strong

  Summary: The presumption that path + size reliably indicate content type and synthesis value is directly challenged: folder taxonomies decay as repositories grow, metadata is known to mislabel when incomplete, and file size is a poor proxy for either content type or value. The "no misfiled/mis-sized content" assumption is precisely what the literature flags as unsafe at scale. This presumption is the unstated twin of ASSUMPTION-387 and inherits its accuracy problem, but in stronger form because it asserts RELIABILITY as ground truth.

  Specific risks: Systematic misclassification of misfiled/mis-sized pages; high-value pages discarded because they are short or sit in a "low-value" folder; errors invisible because taxonomy is trusted as truth.

  Mitigations available: Treat path/size as priors, not ground truth; sample-audit against content; flag and content-check pages whose size/location conflict with expectations.

  STEELMAN:
    Item: PRESUMPTION-415
    Strongest counterargument: Folder location and file size are convenient but decay-prone, low-fidelity signals; treating them as ground truth for content type AND synthesis value bakes in every historical misfiling and discards short-but-important pages, with no mechanism to notice the errors because the taxonomy is assumed correct.
    What would need to be true for C2A2 to be safe: The vault's taxonomy is actively maintained and a sampled audit confirms low misfile/mis-size rates.
    How to test: Sample pages whose folder/size implies one class and hand-check content for class agreement.

  Search scope: Taxonomy decay; metadata mislabeling; size-as-proxy. Adequate.

  Recommendation: CHALLENGED
