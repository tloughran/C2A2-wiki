SEARCH-FOR-PRESUMPTION-211:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-211
  Original statement: "File-on-disk == durably persisted — commit responsibility is unowned."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-211
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — writes treated as durable once on disk; no agent owns the commit/push step that actually persists them.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: Partial

  Sources:
    1. OS write semantics (caching). — There is a trivial sense in which a written file persists across a process exit; but this provides no support for the durability claim in a version-controlled, multi-agent, synced context.

  Strength of support: Weak

  Summary: There is essentially no support for equating on-disk with durably persisted in this system's context. A file in the working tree that is never committed/pushed is ephemeral: it can be overwritten by a regenerating agent, lost on sandbox teardown, or excluded by a path-scoped commit. The supportive direction finds nothing of substance; the only true reading (file survives a process exit) is irrelevant to the durability the system needs.

  Caveats: No meaningful support; the trivial OS-level persistence does not address commit/push durability or multi-agent overwrite.

  Recommendation: NO-SUPPORT-FOUND
