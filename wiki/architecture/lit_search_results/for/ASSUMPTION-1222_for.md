SEARCH-FOR-ASSUMPTION-1222:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1222
  Queue ref: for_lit_search.md — "Queued 2026-08-27 (Agents 14a + 14b, self-awareness intake)" (Priority Medium)
  Original statement: Sampling rather than exhaustive inspection is appropriate for a class of items at a
    human-in-the-loop approval gate; and a rule described as "standing" is in force although its adoption
    is unrecorded.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1222
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from `review/archive/2026-08-27_decisions.md`.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-28, one dedicated query on acceptance sampling vs 100% inspection and
    the conditions that justify sampling. Literature reached: quality-engineering practitioner and CQE
    body-of-knowledge material (acceptance sampling, AQL, consumer's/producer's risk), plus facility-
    management guidance on hybrid inspection regimes. NOT COVERED, and material: (i) the audit-sampling
    literature (ISA 530 / AICPA), which is the closest analogue to an approval gate over documents rather
    than parts; (ii) risk-based inspection standards (API 580) in primary form; (iii) anything at all on
    the secondary limb — rules described as "standing" whose adoption is unrecorded — which was searched
    only from the against direction's shadow-policy angle and is therefore NOT supported here.
    All sources below are SNIPPET-ONLY (WebFetch not attempted this run). Search confidence: MODERATE on
    the primary limb, NONE on the secondary limb.

  Supporting evidence found: Partial

  Sources:
    1. CQE Academy, "Acceptance Sampling" (CQE Body of Knowledge, Product/Process Control), [SNIPPET-ONLY]
       https://cqeacademy.com/cqe-body-of-knowledge/product-process-control/acceptance-sampling/ —
       States the standard justification set: sampling is appropriate where testing is destructive, where
       100% inspection cost is prohibitive, where lot volume is large, and where supplier history supports
       a sanity-check posture. Directly supports the general form of the assumption.
    2. Five Star, "When to Use 100% Inspection vs. Sampling Inspection for Quality Control" [SNIPPET-ONLY]
       https://www.five-star.com.hk/post/100-inspection-vs-sampling-inspection —
       Gives the complementary rule: 100% inspection where a single defect is catastrophic and where
       defect cost is high relative to inspection cost. This is the discriminating condition the
       assumption does not state.
    3. FSM.How, "Quality Control in Stores: 100% vs. Sampling Inspection" [SNIPPET-ONLY]
       https://fsm.how/materials-management/quality-control-stores-sampling-inspection/ —
       Documents the hybrid regime as normal practice: criticality-based split, 100% on critical classes,
       sampling on routine classes. Supports exempting *a class* rather than exempting by convenience.

  Strength of support: Moderate

  Summary: The general proposition — that a defined class of items can correctly be exempted from
    individual review — is well established and uncontroversial in quality engineering. The literature is
    equally explicit that the exemption is earned rather than assumed: it rests on a stated defect rate, a
    stated cost of an escaped defect, and a stated risk tolerance, and the standard practice is a hybrid
    in which criticality decides which class gets which treatment. What the literature supports is the
    *form* of ASSUMPTION-1222, not this instance of it, because no defect-rate or cost basis for the C2A2
    exemption was located in the search or named in the queue entry. The secondary limb — the standing-
    but-unratified rule — found no supporting literature from this direction at all.

  Caveats: The sources are practitioner and body-of-knowledge material, not primary research, and none of
    them concerns document review or approval of generated text; the transfer from manufactured lots to a
    curation gate is assumed, not demonstrated. The whole supportive case is conditional on a calibration
    step this estate has not been shown to have performed.

  Recommendation: PARTIALLY-SUPPORTED
