SEARCH-AGAINST-PRESUMPTION-402:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-402
  Original statement: "That a dirty working tree can be reliably hand-partitioned each time by vigilance, with no structural staging guard"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-402
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: per-commit vigilance presumed a reliable substitute for a structural guard
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Reason 1990, "Human Error"; safety hierarchy of controls. - Attention-dependent controls have an irreducible slip/lapse rate and rank below engineering controls; "reliable by vigilance" is a contradiction in the human-factors sense.
    2. "Correct by construction" / poka-yoke (mistake-proofing). - The robust fix removes the error possibility structurally (the WIP cannot be staged), rather than asking the operator not to make it.
    3. Git worktree/sparse-checkout/branch isolation. - Concrete structural guards exist; not using them is a choice to rely on attention.

  Strength of challenge: Strong

  Summary: This presumption is the load-bearing-but-unstated belief beneath ASSUMPTION-370, and it is the weaker link. Human-error research and the hierarchy of controls are unambiguous: a process that depends on getting manual partitioning right every single time, across an unbounded number of commits, with 39 unrelated WIP files always present, will eventually fail. Calling that "reliable" mistakes possible-when-careful for reliable-in-repetition. The standing exposure persists between commits regardless of any single careful act; only a structural guard (isolation/poka-yoke) removes it.

  Specific risks: Eventual accidental commit of agent-WIP files; the exposure is continuous, not per-event; corrupted/polluted history.

  Mitigations available: Worktree/branch isolation so WIP is absent from the commit surface; sparse-checkout; pre-commit hook asserting the allowed fileset; commit from a clean checkout.

  STEELMAN:
    Item: PRESUMPTION-402
    Strongest counterargument: "Reliable by vigilance" is an oxymoron under human-factors evidence: the safe state requires never slipping once over an unbounded series, while the unsafe state is one keystroke away and continuously available - so the system is one lapse from failure by design, and only structural isolation changes that.
    What would need to be true for C2A2 to be safe: The 39 WIP files are not present in the tree commits are made from, OR a mechanical guard blocks out-of-scope staging.
    How to test: Audit accidental-inclusion incidents across commits; any nonzero rate over time confirms the structural guard is needed.

  Search scope: Human error; poka-yoke; git isolation. Comprehensive.

  Recommendation: CHALLENGED
