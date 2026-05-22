SEARCH-FOR-ASSUMPTION-132:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-132
  Original statement: "Toolkit / content separation (Pathway 18) is non-optional; '18 → 25 arc collapses if 18 fails'; framework / content seam must be clean enough to swap content without touching code"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-132
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 18 toolkit-extraction commitment
      15a: Searched for toolkit-from-demonstration extraction patterns in FLOSS frameworks
    Current status: SUPPORTED (Strong)

  Sources:
    1. Hunt & Thomas (1999) "The Pragmatic Programmer" — DRY and orthogonality principles: framework/content separation is canonical software engineering.
    2. Fowler (2003) "Patterns of Enterprise Application Architecture" — separation of concerns between framework and application content is foundational.
    3. Django, Rails, Drupal, Pelican case studies — successful FLOSS frameworks all maintain strict framework/content seams; content is data, framework is code.
    4. Reenskaug (1979) MVC and successors — model/view/controller separation enables content swap without code changes; canonical 40+ year pattern.
    5. Parnas (1972) "On the Criteria to Be Used in Decomposing Systems into Modules" — information hiding requires clean seams; this is the canonical formulation.
    6. Apache Wicket, Hugo (static-site generator) — explicit toolkit-from-demonstration extractions that successfully maintained the seam.

  Strength of support: Strong

  Summary: Framework/content separation is one of the most well-established principles in software engineering, with 50+ years of canonical literature (Parnas, MVC, DRY). FLOSS frameworks that maintain this seam (Django, Rails, Hugo) succeed at content-swap-without-code-touch; those that fail (early Drupal, pre-Symfony PHP frameworks) require code-level forks per deployment. The "non-optional" framing is supported by both theory (information hiding) and practice (FLOSS framework success patterns). The 18 → 25 arc dependency is sound: if Pathway 18 doesn't establish the seam, Pathways 19-22 (federation/institutional/departmental/individual deployment) require per-deployment code modification.

  Caveats: (a) "Clean enough to swap content without touching code" is a strong claim — most frameworks support content-swap with template/config changes but require some code adaptation for novel use cases; (b) The seam is rarely perfectly clean — boundary cases (e.g., "is this validation logic content or code?") require ongoing curation; (c) Toolkit-from-demonstration extraction is harder than designing toolkit-first (Mythical Man-Month "second-system effect").

  Recommendation: SUPPORTED (Strong) — framework/content separation is canonical; load-bearing for portability arc
