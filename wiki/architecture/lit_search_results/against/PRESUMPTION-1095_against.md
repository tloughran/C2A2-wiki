SEARCH-AGAINST-PRESUMPTION-1095:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1095
  Original statement: Unwritten, model-default omission of sensitive content from a research archive is compatible with archival fidelity.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1095
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from fef2bbcb.
      15b: Searched for challenging literature (scheduled run 2026-09-30; depth: web search + selective fetch)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Schwartz, J. M., & Cook, T. (2002). "Archives, Records, and Power: The Making of Modern
       Memory." Archival Science 2(1-2):1-19. [Search-result level, plus background knowledge of the
       paper.] This is foundational archival theory. Appraisal and selection are acts of power that
       shape memory, "a tiny fraction of all those records created are appraised, selected, and
       memorialized". The authors argue selection must be made visible and accountable, not
       presented as neutral. An unwritten, unreviewed selection rule is the case they warn about.
    2. Carter, R. G. S. (2006). "Of Things Said and Unsaid: Power, Archival Silences, and Power in
       Silence." Archivaria 61:215-233. [Search-result level.] This paper develops the concept of
       archival silences: systematic absences produced by the archive's own selection, which later
       users read as absences in the historical record.
    3. Khorramrouz, A., & Levy, S. (2025). "Characterizing Selective Refusal Bias in Large Language
       Models." arXiv:2510.27087. [Fetched: abstract.] LLM safety guardrails "can inadvertently
       introduce or reflect new biases". Refusal behavior is uneven across topics and groups. Model
       defaults are therefore not neutral filters, and their omissions are patterned.
    4. "What Large Language Models Do Not Talk About: An Empirical Study of Moderation and
       Censorship Practices" (Springer LNCS chapter, 2025; authors not verified in this run). Also
       "What Stays and What Goes: Auditing the Impact of LLM Summarization on News Partisanship"
       (CHI 2026 Extended Abstracts). [Both search-result level.] These describe "soft censorship"
       (selective omission or downplaying) and treat summarization as selecting perspectives, where
       omission is itself a bias.

  Strength of challenge: Strong

  Summary: Archival theory directly contradicts the presumption. Selection that is undocumented and
    unreviewed is the mechanism behind archival silences (Schwartz & Cook; Carter). Such silences
    are later read as gaps in the thinker's own record rather than in the archive. The LLM
    literature adds that model-default omissions are patterned, not random (Khorramrouz & Levy;
    soft-censorship studies). The resulting silence is therefore systematic, concentrated on
    death, suicide, mental health and grief. Omitting sensitive material can be legitimate, and
    archives routinely restrict access. What the literature rejects is an omission policy that
    nobody wrote, disclosed or reviewed.

  Specific risks: The McGilchrist and Wolfram records get systematically thinner where those thinkers
    discuss death, possession and bereavement, which are central to their positions on the soul
    and meaning. Downstream agents (PRS, pattern detector 13, 15a/15b) then find less evidence on
    those themes and may conclude the thinkers say little about them. Because the omission is
    reported only in a closing message, nobody can later tell a thinker's silence from the
    archive's.

  Mitigations available: Write an explicit sensitive-content policy (include, include with content
    note, restrict, or exclude with a placeholder). When content is omitted, leave a stub marker
    ("[omitted: sensitive, topic X, source Y]") so the gap is visible. Log each omission for human
    review. Archival practice distinguishes restricting access from destroying or omitting records,
    and a restricted but indexed record keeps fidelity (background knowledge of standard archival
    practice).

  Search scope: Preliminary: 2 searches, 1 fetch.
  Excluded results: university library LibGuides on archival silences (teaching aids), used as
    corroboration only; arXiv 2606.29251 (financial-summary fidelity), off-lane.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1095
  Strongest counterargument: The core of archival ethics is that selection is never neutral and must
    therefore be explicit and accountable. An archive whose coverage is shaped by the safety
    defaults of the model doing the writing has a selection policy that is invisible, varies with
    the model version, and is patterned in ways the LLM-bias literature has documented. The
    silences it creates fall on the topics (death, mental illness, the soul) where two of the
    tracked thinkers do some of their most distinctive work. Later readers will not see an editorial
    choice. They will see a thinker who seemingly never addressed those topics.
  What would need to be true for C2A2 to be safe: Every omission leaves a visible marker, the policy
    is written and reviewed, and the omitted material stays reachable in the source layer.
  How to test: Compare PRS triplet density on death, grief and mental-health passages with density
    on other passages from the same source sessions (McGilchrist, Wolfram). A significant
    shortfall confirms a patterned silence.
