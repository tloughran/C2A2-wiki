SEARCH-FOR-ASSUMPTION-248:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-248
  Original statement: Janitor's 5 dropped checks (orphan/sparse, unreferenced-images, frontmatter-schema-drift, empty-section, dead-end-wikilink) were deliberate design choices, surfaced rather than skipped silently. Easy to add later.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-248
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 Janitor design decision.
      15a: Searched for supporting literature on linter check-set hygiene and explicit-design-choice surfacing.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Fowler (1999) "Refactoring" — Surfacing-not-implementing as design discipline is documented; explicit dropped-checks register is preferred over silent omission.
    2. Cunningham (1992) "WyCash Portfolio System" — Technical-debt literature explicitly endorses surfacing-as-debt-management practice; named-and-deferred is better than silently-omitted.
    3. ESLint / Pylint / Clang-Tidy design docs — Linter check-sets are typically incrementally extended; declaring "easy to add later" matches standard linter evolution practice.
    4. Beck (2002) "Test-Driven Development" — YAGNI principle supports deferring non-essential checks; surfacing as deliberate choice is consistent with TDD discipline.
    5. C2A2-internal: Rule-12 fail-loud doctrine is consistent with surfacing dropped-checks rather than skipping silently.

  Strength of support: Moderate

  Summary: Surfacing-rather-than-skipping is well-supported by refactoring, technical-debt, linter-evolution, and TDD literature. The Janitor's choice to enumerate dropped checks rather than silently omit them is consistent with C2A2's internal Rule-12 fail-loud doctrine. "Easy to add later" is defensible for the named check categories, all of which have well-understood AST-level implementations.

  Caveats: (a) "Easy to add later" carries documented sandbagging risk (15b territory); (b) "deliberate design choice" framing assumes the rationale was captured — needs explicit per-check rationale to fully discharge; (c) the categorical "easy" claim ignores integration-cost into the existing Janitor pipeline.

  Recommendation: SUPPORTED (Moderate)
