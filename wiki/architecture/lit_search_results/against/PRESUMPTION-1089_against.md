SEARCH-AGAINST-PRESUMPTION-1089:
  Date searched: 2026-09-29
  Original item: PRESUMPTION-1089
  Original statement: Deferring to prior reviewers' dispositions is reliable when the prior record can contain errors.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1089
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from deference to earlier runs on Day 76 while the log held an error.
      15b: Searched for challenging literature (scheduled run 2026-09-29; sources marked 'search-result level' were not read in full)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Strength: Moderate

  Sources:
    1. Anchoring and adjustment effects on audit judgments: experimental evidence from Switzerland (ScienceDirect S0967542621000369; https://www.sciencedirect.com/org/science/article/abs/pii/S0967542621000369) — auditors' judgments anchor on earlier/prior figures. SERP-level; not read in full.
    2. Wolters Kluwer 'The psychology of internal audit: navigating bias, behavior and decision-making' and IIA 'Building a Better Auditor: Beating Behavioral Biases' (2024) — practitioner sources naming anchoring and prior-review deference as audit risks. PMC11098414 on debiasing anchoring from past performance in supplier evaluation. Tversky & Kahneman 1974 (already cited in validated_premises ~line 418).

  STEELMAN: deferring to prior reviewers is efficient and often correct, since re-deriving everything is costly and most prior dispositions are right; the risk concentrates where the record is known to contain an error. The presumption is unsafe unconditionally, safe if deference carries a spot-check on a sample of prior items.

  SYSTEMIC-RISK: see run note in for_lit_search.md (2026-09-29).

---
SUPPLEMENT — second 15b pass, same date (concurrent-writer collision; appended, nothing above
removed). This pass did NOT read lit_search_results/for/. It independently agrees: CHALLENGED,
Moderate. It adds fetched primary sources and one boundary-condition source that partly supports
the presumption.

SEARCH-AGAINST-PRESUMPTION-1089 (supplement):
  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1089
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from deference to earlier runs on Day 76 while the log held an error.
      15b: Searched for challenging literature (lane: anchoring / path dependence in sequential review; error propagation in audit trails)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Teplitskiy, M., et al. (2019/2020). "Social Influence among Experts: Field Experimental
       Evidence from Peer Review." (AEA 2020 preliminary paper.) [Not fetched; figures from search
       results citing it.] Medical-school faculty reviewers were shown randomly high or low
       "other reviewer" scores. 47% updated, and all but one of about 185 updates moved toward the
       external score. The shown scores were random, not informative. Experts deferred to a
       prior record whether or not it was right.
    2. Wright, A. (1988). "The impact of prior working papers on auditor evidential planning
       judgments." Accounting, Organizations and Society 13(6):595-605. [Fetched: abstract.] The
       abstract describes anchoring on prior working papers as a "significant concern". Auditors
       given prior papers were less efficient, and a summarized prior-year "scenario" did better.
       The adaptiveness difference was small, so this is moderate evidence.
    3. Stelmakh, I., Rastogi, C., Shah, N. B., Singh, A., & Daumé III, H. (2020/2023). "A Large Scale
       Randomized Controlled Trial on Herding in Peer-Review Discussions." arXiv:2011.15083 (PLOS
       ONE 2023). [Fetched: abstract/intro.] This source partly supports the presumption as a
       boundary condition. The ICML 2020 RCT found no herding on the discussion initiator's opinion
       when reviewers had formed independent opinions before seeing others'. Deference is less
       harmful when an independent assessment comes first.
    4. Jamshidi, S., Dakhel, A. M., Nafi, K. W., & Khomh, F. (2026). "Hallucination Cascade:
       Analyzing Error Propagation in Multi-Agent LLM Systems." arXiv:2606.07937. [Fetched:
       abstract.] The picture is mixed. Sequential agent refinement lowered the hallucination
       score, but factual accuracy declined slightly at each step (0.789 to 0.769). The setup is
       revision chains, not deference to a record known to contain errors, so it neither confirms
       nor refutes the presumption.

  Strength of challenge: Moderate

  Summary: Experts shown a prior assessment move toward it even when it is random (Teplitskiy). Audit
  research treats anchoring on prior workpapers as a known hazard (Wright; SALY practice
  literature). The key boundary condition is Stelmakh et al.: herding disappears when each reviewer
  forms an independent view before seeing the prior disposition. The presumption therefore fails
  in the specific form 14b identified, where a later run adopts the earlier disposition without an
  independent pass, and fails worst when the record is known to contain errors, as on Day 76. It
  may hold if an independent assessment comes first.

  Specific risks: One erroneous disposition gets re-ratified by every later run and gains apparent
  consensus weight each time. Combined with structural-only QC (PRESUMPTION-1088), errors are then
  neither caught nor re-examined.

  Mitigations available: Blind-first protocol: form a view before reading the prior disposition,
    then compare. Mark prior entries with a "verified-by" chain and skip deference for entries
    whose chain contains a known error. Re-derive a random sample of deferred items.

  Search scope: Preliminary: 3 searches, 3 fetches.
  Excluded results: cpahalltalk.com, yellowbook-cpe.com (practitioner blogs; the SALY framing was
    used only as context, not cited); zartis.com, latenteval.ai (vendor blogs echoing the lane);
    arXiv:2608.14588 "Hallucination Snowball" (surfaced; not fetched; not cited).

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1089
  Strongest counterargument: When experts are shown a prior assessment, they move toward it even
    if it is random. A sequential system that defers to its own log therefore turns one early
    error into a lasting consensus. The field-experimental evidence shows the deference happens
    whether or not the prior is correct, and on Day 76 the prior was known to hold an error. The
    one condition under which herding vanished (independent opinion formed first) is the one the
    Day 76 deference did not meet.
  What would need to be true for C2A2 to be safe: Each run forms an independent disposition before
    consulting prior ones, and entries downstream of a known error are excluded from deference.
  How to test: Seed an erroneous prior disposition into the log for a test item and measure how
    often subsequent runs adopt it, under deference-first and blind-first protocols.
