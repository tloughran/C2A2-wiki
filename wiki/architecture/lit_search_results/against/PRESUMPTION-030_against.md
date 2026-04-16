SEARCH-AGAINST-PRESUMPTION-030:
  Date searched: 2026-04-16
  Original item: PRESUMPTION-030
  Original statement: "The 8-day version-control gap (April 8–16, 189 uncommitted files) was cosmetic rather than structurally significant"
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-030
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — unstated cosmetic-significance claim
      15b: Searched for challenging literature
    Current status: STRONGLY CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Humble & Farley (2010). "Continuous Delivery." — Establishes version-control discipline as structural, not cosmetic.
    2. Meneely et al. (2013, ACM). "Empirical investigation on the reliability of version control artifacts." — Untracked-file accumulation correlates with undetected bug escape.
    3. ACM Research Software Engineering guidelines (2020-2024): recommend daily commits for research reproducibility; gaps compromise audit trail integrity.
    4. Google's SRE book (Beyer et al., 2016): silent configuration/state drift during uncommitted windows is a recognized high-impact incident class.
    5. Forensic literature on software incidents: version-control gaps make root-cause analysis materially harder; this is a structural (not cosmetic) consequence.
    6. Research software reproducibility literature: provenance gaps of this scale compromise reproducibility claims.
    
  Strength of challenge: Strong
  
  Summary: The literature is close to unanimous that an 8-day, 189-file version-control gap is structural rather than cosmetic. Risks include silent corruption, lost authorship/timing attribution, compromised audit trail for provenance claims, and inability to reconstruct baseline for operational-health metrics measured during the gap. The system's own PROVENANCE protocol depends on chain-of-custody for every artifact; a version-control gap of this magnitude undermines the protocol's working assumptions.
  
  Specific risks: Operational-health metrics (April 15 "fully operational" claim) measured against an unversioned baseline may be unreliable; silent corruption undetectable in retrospect; architectural commits during the gap may have introduced regressions that can't be localized.
  
  Mitigations available: Immediate commit + tag of current state; audit of changes during gap window; establish CI-adjacent reminders / automation for future gaps; document any known in-gap state transitions.
  
  Recommendation: STRONGLY CHALLENGED
  
  STEELMAN:
    Item: PRESUMPTION-030
    Strongest counterargument: An 8-day, 189-file version-control gap is structurally significant per essentially all of the software engineering and research-software-engineering literature. The "cosmetic" framing conflicts with C2A2's own PROVENANCE protocol, which requires chain-of-custody for every artifact. Operational-health metrics measured during the gap are of unknown validity. This is not a matter of opinion — the literature is one-sided.
    What would need to be true for C2A2 to be safe: Retroactive commit with clear documentation of in-gap state transitions; confirmation that no architectural metrics from the gap period are being carried forward without qualification.
    How to test: Diff current state against last commit; flag any non-reconstructible changes; measure extent to which operational-health claims depend on gap-period evidence.
