SEARCH-AGAINST-ASSUMPTION-1684:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1684
  Original statement: After one full review, later structural (mechanical) checks are enough to keep a text's pass status.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1684
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa QC 8c58d8ca.
      15b: Searched for challenging literature (scheduled run 2026-09-29; sources marked 'search-result level' were not read in full)
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No
  Strength: Weak

  Sources:
    1. Same query family returned no primary evidence either way. Background expectation (unverified): audit standards (e.g. ISA 330) require substantive procedures where control reliance is unproven, and mechanical checks are known not to detect semantic drift — this overlaps PRESUMPTION-1088 in the same batch.

  STEELMAN: mechanical checks detect only what the checklist encodes; if text passes structure while its meaning changes (edits, stale citations), pass status silently persists. The assumption is safe only where change between reviews is itself mechanically detectable.

  SYSTEMIC-RISK: see run note in for_lit_search.md (2026-09-29).

---
SUPPLEMENT — second 15b pass, same date (concurrent-writer collision; appended, nothing above
removed). A separate 15b process wrote the block above while this pass was in progress and
overwrote this pass's file. This pass did NOT read lit_search_results/for/.
DISCREPANCY FOR RECONCILER: the block above reports NO-CHALLENGE-FOUND/Weak. This pass found
primary-source challenging evidence and reports CHALLENGED/Moderate.

SEARCH-AGAINST-ASSUMPTION-1684 (supplement):
  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1684
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa QC 8c58d8ca.
      15b: Searched for challenging literature (lane: audit re-review intervals; checklist vs holistic review efficacy)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Urbach, D. R., et al. (2014). "Introduction of Surgical Safety Checklists in Ontario, Canada."
       NEJM 370:1029-1038 (NEJMsa1308261). [Not fetched (PubMed reCAPTCHA); figures confirmed via
       search results.] Mandatory checklist adoption across 101 hospitals: no significant change
       in mortality (OR 0.91, 95% CI 0.80-1.03) or complications (OR 0.97). Procedural compliance
       did not track the substantive outcome.
    2. Shojania, K. G., Sampson, M., Ansari, M. T., et al. (2007). "How Quickly Do Systematic Reviews
       Go Out of Date? A Survival Analysis." Annals of Internal Medicine 147(4):224-233. [Not
       fetched (PubMed blocked); findings via search results.] 23% of high-quality reviews were
       out of date within 2 years, 15% within 1 year, and 7% already at publication. A
       substantive pass decays, and nothing in the text's structure signals it.
    3. Wright, A. (1988). "The impact of prior working papers on auditor evidential planning
       judgments." Accounting, Organizations and Society 13(6):595-605. [Fetched: abstract.] When
       the client's environment changed, auditors given prior working papers were about as
       adaptive as the other groups but less efficient. The effect is modest.

  Strength of challenge: Moderate (upper end; no study specific to structural checks on
    interpretive prose)

  Summary: Checklist or mechanical compliance is a weak proxy for the substantive property it
  tracks. A substantive pass also decays over time without the text changing. Structural checks
  catch neither semantic edits nor evidence drift. The literature points to re-review triggered by
  edits and elapsed time, not to a single review followed by structural maintenance.

  Specific risks: Summa texts edited after their full review keep a PASS while carrying new semantic
    errors, and passes are never refreshed when sources or wiki consensus change.

  Mitigations available: Invalidate the pass (or downgrade it to "structurally maintained") above a
    content-diff threshold. Set a maximum age for semantic passes. Sample passed texts for blind
    full re-review and track the overturn rate.

  Search scope: Preliminary: 3 searches, 3 fetch attempts (1 success).
  Excluded results: secure.com, qualys.com, compassmsp.com, ciso.inc, elevateconsult.com, jettbt.com,
    privacychecker.pro, nhimg.org (vendor/SEO compliance blogs echoing the lane; "73% of incidents
    outside audit windows" statistic is unsourced and was not used).

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1684
  Strongest counterargument: A structural check certifies form, not meaning. The one thing a full
    review certifies, that the interpretation is correct, is what later edits and later evidence
    break without tripping any structural rule. Mandatory checklists at population scale produced
    compliance and no outcome change. Untouched syntheses go stale within 1-2 years for about a
    quarter of cases.
  What would need to be true for C2A2 to be safe: Texts are frozen after full review, passes carry
    a date and scope, and sampled re-review shows a low overturn rate.
  How to test: Blind full re-review of a random sample of structurally-maintained passes; the
    overturn rate estimates what the regime misses.
