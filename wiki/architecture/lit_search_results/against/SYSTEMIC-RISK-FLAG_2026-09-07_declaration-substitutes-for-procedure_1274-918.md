SYSTEMIC-RISK-FLAG:
  Date: 2026-09-07
  Filed by: delegated 15b subagent (AGAINST direction only; did not read any FOR file or
    lit_search_returns.md)
  Affected items: ASSUMPTION-1274, PRESUMPTION-918 (secondary: PRESUMPTION-921 — see note)
  Common vulnerability: A written annotation is treated as equivalent to the verification step it
    names. In ASSUMPTION-1274 the annotation is "evidence gate noted" standing in for a full-text check;
    in PRESUMPTION-918 it is "independence compromised" standing in for an independent search. In both,
    the system records that a check is owed and then proceeds as if the record were the check. The
    literature attacks this from two sides: (i) annotations of this kind (caveats, disclosures) do not
    propagate — one downstream retelling loses ~90% of caveats (Sumner et al. 2014), and citation
    networks select against qualified versions of claims (Greenberg 2009); (ii) annotations of this kind
    are systematically under-discounted by readers and license the writer to lean further (Cain,
    Loewenstein & Moore 2005), and the writer cannot estimate the size of what the annotation is
    supposed to cover (Wilson & Brekke 1994; Pronin, Lin & Ross 2002). The net effect is that C2A2's
    provenance chain accumulates entries that look like controls and function as exemptions.
  Literature basis:
    - Cain, D.M., Loewenstein, G. & Moore, D.A., 2005. "The Dirt on Coming Clean." J. Legal Studies
      34(1):1–25. [VERIFIED: UCP landing page and abstract]
    - Wilson, T.D. & Brekke, N., 1994. "Mental Contamination and Mental Correction." Psychol. Bull.
      116(1):117–142. [VERIFIED: listings and abstract]
    - Pronin, E., Lin, D.Y. & Ross, L., 2002. "The Bias Blind Spot." PSPB 28(3):369–381. [VERIFIED: Sage
      landing page and abstract]
    - Greenberg, S.A., 2009. "How citation distortions create unfounded authority." BMJ 339:b2680.
      [VERIFIED: James Lind Library record]
    - Sumner, P., et al., 2014. BMJ 349:g7015 (caveats present in ~10% of press releases/news).
      [VERIFIED: listings; figure from search snippet]
    - Pitkin, R.M., et al., 1999. JAMA 281:1110–1111 (instructing authors to fix abstracts did not work —
      the 1998 RCT cited therein). [VERIFIED: full text read]
    - Huang, J., et al., 2024. "Large Language Models Cannot Self-Correct Reasoning Yet." ICLR 2024.
      [VERIFIED: arXiv PDF]
  Risk level: High
  Note on PRESUMPTION-921: Included as secondary because it exhibits the same shape at the design level
    rather than the run level — the label "tradition" is attached to an author corpus and downstream
    stages consume the label as if the community it names were present. It shares the mechanism
    (label consumed as object) but not the literature basis, so it is not counted in the primary set.
  Related prior flag: SYSTEMIC-RISK-FLAG_2026-09-06_evaluator-separation_1263-914.md (filed on the
    separation breach that PRESUMPTION-918 was inferred from). This flag is about the remedy applied to
    that breach, and generalises it: declaring the breach is the same move as noting the gate.
  Recommendation: Treat every "noted"/"declared" status in the provenance chain as a pending action
    with an owner and a blocking effect, never as a completed control. Concretely: (1) ABSTRACT-ONLY and
    INDEPENDENCE-COMPROMISED become machine-readable tags that downstream agents must propagate verbatim
    and that block promotion/reconciliation until cleared by a procedure (full-text check; fresh-context
    re-run and diff); (2) the clearing procedure is performed by a context other than the one that
    raised the tag; (3) 15d audits aged tags. The literature's consistent finding is that the fix for
    this class of problem is procedural and external, not declarative and internal; a system that
    accepts declarations in lieu of procedure will, per Cain et al., tend to produce more of the thing
    declared, not less.
