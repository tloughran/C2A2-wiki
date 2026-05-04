SEARCH-FOR-PRESUMPTION-030:
  Date searched: 2026-04-16
  Original item: PRESUMPTION-030
  Original statement: "The 8-day version-control gap (April 8–16, 189 uncommitted files) was cosmetic rather than structurally significant"
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-030
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — unstated claim about version-control gap significance
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No
  
  Sources:
    1. Humble & Farley (2010). "Continuous Delivery." — Argues version-control discipline is a structural, not cosmetic, concern.
    2. McConnell, S. (2004). "Code Complete." — Version control gaps are documented as common sources of silent corruption.
    3. ACM research software engineering guides (2020-2024). — Recommend daily or per-change commits for research repositories.
    4. NO literature supports the claim that version-control gaps of this magnitude are cosmetic.
    
  Strength of support: None
  
  Summary: The software engineering and research-software-engineering literature is essentially unanimous that version-control discipline is a structural concern, not a cosmetic one. Gaps create risks of unrecoverable silent corruption, ambiguous provenance, and loss of audit trail — all of which are particularly problematic for research repositories. No literature was found supporting the claim that an 8-day, 189-file gap is merely cosmetic.
  
  Caveats: None — this is one of the more consistently supported findings in software engineering.
  
  Recommendation: NO-SUPPORT-FOUND (literature contradicts the presumption)
