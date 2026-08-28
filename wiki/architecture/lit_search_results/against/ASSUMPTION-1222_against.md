SEARCH-AGAINST-ASSUMPTION-1222:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1222
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: Sampling rather than exhaustive inspection is appropriate for a class of items at a
    human-in-the-loop approval gate; and a rule described as "standing" is in force although its adoption is
    unrecorded.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1222
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from `review/archive/2026-08-27_decisions.md`.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on failures of risk-based/acceptance sampling and
    escaped defects, plus one query (shared with PRESUMPTION-887) on undocumented standing rules. Reached:
    AQL practitioner material (QIMA, HQTS, Quality Magazine), Michel Baudin's blog on acceptance sampling at
    low PPM, Springer's ACCEPTANCE SAMPLING reference entry, AlisQI. NOT COVERED: Deming's *Out of the
    Crisis* in primary form — his kp rule is the strongest formal argument against sampling and I have it
    only second-hand; and ISA 530 audit sampling, the closest analogue. All SNIPPET-ONLY. Confidence:
    MODERATE.

  Challenging evidence found: Yes

  Sources:
    1. Michel Baudin, "Acceptance Sampling In The Age Of Low PPM Defectives" (2017) [SNIPPET-ONLY]
       https://michelbaudin.com/2017/07/31/acceptance-sampling-in-the-age-of-low-ppm-defectives/ —
       Records that acceptance sampling has been criticised by W. E. Deming and is not part of the Lean
       approach to quality. The relevance is direct: sampling is defensible at high defect rates and becomes
       indefensible as defects become rare and severe.
    2. HQTS / QIMA AQL material [SNIPPET-ONLY] https://www.hqts.com/aql-calculator/ ,
       https://www.qima.com/aql-acceptable-quality-limit — The arithmetic point: at an RQL of 0.01% the plan
       demands thousands of samples. Detecting rare defects by sampling requires sample sizes that make the
       exemption pointless.
    3. Springer, "ACCEPTANCE SAMPLING" reference entry [SNIPPET-ONLY]
       https://link.springer.com/rwe/10.1007/1-4020-0612-8_8 ; AlisQI, "Acceptance Sampling: Calculated Risk
       or Clear Advantage?" [SNIPPET-ONLY] — Consumer's risk is structural: even where defects exist, the
       sample may miss them, and the whole lot is then accepted on that inference. "AQL is a risk management
       tool, but only if the numbers are calibrated to your actual risk tolerance."
    4. Innolect / Secoda shadow-rules material [SNIPPET-ONLY; shared corpus with PRESUMPTION-887] —
       On the secondary limb: unwritten rules exert outsized influence and operate without formal
       accountability. A rule described as "standing" whose adoption is unrecorded is, in this vocabulary,
       a shadow rule, and the literature treats shadow rules as an exposure rather than as an economy.

  Strength of challenge: Moderate-Strong

  Summary: The challenge is not that sampling is wrong but that this instance has none of what makes it
    right. Every source that endorses sampling conditions it on a calibrated risk tolerance, a known or
    assumed defect rate, and a bounded cost of an escaped defect; the sources that criticise it (Deming, and
    the low-PPM argument) do so precisely where the defect rate is low and the consequence high, which is
    the regime of a curation gate whose escaped defects are wrong claims entering a durable record. The
    secondary limb is challenged from a different direction entirely: a standing rule with no recorded
    adoption is a shadow rule, and shadow rules are exactly what nobody can test, revise or retire.

  Specific risks: (a) The exempted class absorbs an unknown escape rate that nobody will ever measure,
    because the exemption removes the only instrument that would have measured it. (b) The exemption is
    self-perpetuating: with no adoption record there is no date, no author and no rationale to revisit, so
    it cannot expire. (c) The estate acquires a second precedent for governing by undocumented convention —
    ASSUMPTION-1223 and ASSUMPTION-1232 being the others named the same day.

  Mitigations available: Yes, and cheap. Record the rule's adoption (date, author, rationale, expiry).
    State the defect rate the exemption assumes. Sample the exempted class at a low rate rather than at
    zero, which converts an untestable exemption into a measurement.

  STEELMAN:
    Item: ASSUMPTION-1222
    Strongest counterargument: A review gate with a single intermittently-available human server does not
      have the capacity for exhaustive inspection, and the honest choice is not between sampling and
      exhaustive review but between sampling and *nothing*, since an unreviewable queue delivers zero
      review. Under that framing the exemption is not a weakening of the gate; it is what keeps the gate
      functioning at all, and demanding a calibrated defect rate before permitting it imposes a measurement
      cost on the very party who has no capacity.
    What would need to be true for C2A2 to be safe: the exempted class would have to be genuinely
      low-consequence, and the exemption would have to carry an expiry and a residual sampling rate so that
      the escape rate becomes observable rather than assumed.
    How to test: apply full review to a random 1-in-N of the exempted class for one month and count
      defects. If the count is zero, the exemption is earned and now has a record; if it is not, the
      exemption's cost is measured rather than argued.

  Recommendation: CHALLENGED
