SEARCH-FOR-PRESUMPTION-1097:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1097
  Original statement: Static task prompts remain valid without scheduled review.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1097
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 7+ scheduled tasks.
      15a: Searched for supporting literature (scheduled run 2026-09-30; depth: web search + selective fetch; sources marked 'search-result level' were not read in full)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (conditional analogue only)

  Sources:
    1. Lehman, M. M., 1980. "Programs, Life Cycles, and Laws of Software Evolution." Proc. IEEE 68(9):1060-1076 (as summarized in Wikipedia, "Lehman's laws of software evolution"). — S-programs written against an exact, fixed specification "are mostly static and shouldn't evolve much"; the laws of continuing change and declining quality apply only to E-type programs embedded in a changing environment. This is the only framework found under which a static artefact stays valid without review. (fetched: Wikipedia summary; primary paper not read)
    2. No source was found supporting the claim for artefacts that reference environmental state (paths, dates, counts, scheduler state, commands). Searches on documentation decay, software rot and runbook staleness found only literature describing drift.

  Strength of support: Weak

  Summary: The only supportive grounding is Lehman's S-type category. An artefact defined entirely by a fixed specification, with no reference to a changing environment, need not change. Task prompts that contain only stable intent (goals, format rules, invariants) could plausibly fit that category. The prompts in this item instead embed environmental facts such as dates, file paths, completion counts and command flags, which puts them in Lehman's E-type category, where the literature predicts they will decay. So the claim is supported only for the stable-intent part of a prompt.

  Caveats: Drawing an analogy from programs to natural-language task prompts is an inference. Supportive literature is sparse because the premise is an unexamined default, not a stated position. Preliminary search.

  Recommendation: NO-SUPPORT-FOUND
