SEARCH-AGAINST-PRESUMPTION-1097:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1097
  Original statement: Static task prompts remain valid without scheduled review.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1097
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 7+ scheduled tasks.
      15b: Searched for challenging literature (scheduled run 2026-09-30; depth: web search + selective fetch)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Patsakis, C., Argyropoulos, V., & Alepis, E. (2026). "Configuration, Not Conscience: A
       Large-Scale Empirical Study of LLM System Prompts." arXiv:2609.31575 (cs.CR, 25 Sep 2026).
       [Fetched: abstract, intro, section 4.5 excerpt.] In a corpus of 407 system prompts from 62
       vendors, prompts behave like configuration files and "carry measurable maintenance debt". The
       paper counts "rot-risk markers" (dates, version strings, model IDs, URLs, paths) and notes
       that "a prompt with over a dozen perishable references has many places to age silently". It
       recommends versioning, regression tests, and linting for stale references. C2A2's stale
       items (a 2026-08-05 "known state", a "Day 308" target, wrong paths, a stale CLI flag) are
       exactly these marker types.
    2. Wen, F., Nagy, C., Bavota, G., & Lanza, M. (2019). "A Large-Scale Empirical Study on
       Code-Comment Inconsistencies." ICPC 2019. [Search-result level.] The study mined 1.3 billion
       AST-level changes across 1,500 systems. Natural-language descriptions of code routinely fall
       out of sync when the code changes (deprecation, refactoring).
    3. Tan, W. S., Wagner, M., & Treude, C. (2023). "Detecting outdated code element references in
       software repository documentation." Empirical Software Engineering. [Search-result level;
       author names from background recall.] Of over 3,000 GitHub projects, most contained at least
       one outdated code-element reference at some point in their history. Developers are often
       unaware that a change made the documentation obsolete.
    4. Background knowledge, not fetched this run. Parnas, D. L. (1994). "Software Aging." ICSE '94.
       Software ages even when unchanged because its environment changes around it ("lack of
       movement"). Prompt-drift practitioner sources (Comet, Agenta; search-result level) make the
       same point for LLM prompts under silent model updates.

  Strength of challenge: Strong

  Summary: Empirical software engineering consistently finds that natural-language artifacts
    describing a changing system go stale unless something forces them to update (Wen et al.; Tan
    et al.). Parnas's "software aging" says this happens even when nothing touches the artifact,
    because its environment moves. The first large-scale study of LLM system prompts (Patsakis et
    al. 2026) now shows the same for prompts: they are configuration, carry perishable references,
    and rot silently. C2A2's task prompts embed dates, day counts, paths and CLI flags, the
    highest-rot categories. No evidence was found that such prompts stay valid without review.

  Specific risks: Each run rediscovers and works around the same staleness in its own way, so per-run
    workarounds diverge (ASSUMPTION-1706). The cost recurs daily. A wrong-root task file may write
    to the wrong location, or silently skip work, before a run notices. Because agents may not edit
    system files, no feedback loop exists: staleness is observed but never fixed.

  Mitigations available: Run a scheduled prompt-lint pass that extracts dates, paths, commands and
    counts from each task prompt and checks them against the live environment. Have runs write a
    structured "prompt drift" note to one queue for Tom to review in batches. Record a last-reviewed
    date on each task prompt, with an expiry.

  Search scope: Preliminary: 3 searches, 1 fetch.
  Excluded results: software-aging studies on memory leaks (OpenStack, Android, GPU serving),
    off-lane (runtime aging, not specification staleness); vendor blog on prompt incidents
    (Deepchecks).

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1097
  Strongest counterargument: A task prompt is a specification of an environment written at one moment,
    and the environment keeps moving: paths, scheduler state, completed backlogs, tool flags,
    model versions. Decades of work on documentation and code drift, and now a direct study of LLM
    system prompts, show that such specifications go stale by default and that the people who
    change the environment rarely notice. C2A2 adds an aggravating factor: the agents that detect
    the staleness are forbidden from fixing it. That turns a one-time repair into a permanent daily
    tax, and each run pays it slightly differently.
  What would need to be true for C2A2 to be safe: Prompts contain no perishable references, or a
    scheduled review or lint catches them within a few days of going stale.
  How to test: Count perishable references in each task prompt and, for each one, check whether it
    is still true today. Track the stale fraction over time with no review, and with a weekly lint.
