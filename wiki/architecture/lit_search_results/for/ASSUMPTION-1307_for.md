SEARCH-FOR-ASSUMPTION-1307:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1307
  Original statement: "**Four of the 36 cards approved a pointer, not a reading** (FINDING-089) — each
    said so itself and asked to be caught... **A batch APPROVE can't distinguish 'read and agreed' from
    'not read separately.'**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1307
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. Six of thirty-six cards in the largest ingest in the network's
        history are of uncertain warrant on the run's own account, and all thirty-six were ingested,
        flagging rather than holding. The relation to ASSUMPTION-1295 (ingest licensed by ID alignment
        rather than approval) is not drawn by the run.
      15a: Searched for supporting literature; found strong and directly transferable support in data
        protection law (granularity requirement), research ethics (specificity of consent), and the
        code-review size literature.
    Current status: SUPPORTED

  Register pre-check: Three ACTIVE premises bear closely.
    - PREMISE-172: "A PASS MARK IS A VERDICT ABOUT A (READER, FRAME, SCOPE) READING — NOT A PROPERTY OF
      THE FILE... a mark carries no information about what was NOT examined." This is very nearly the
      assumption already, stated at the level of individual review; ASSUMPTION-1307 extends it to the
      aggregated case and that extension is the new content.
    - PREMISE-121: review-queue acceptance is a function of workload and cumulative exposure rather than
      item merit; override/acceptance rates run 49-96% and acceptance falls as volume rises.
    - PREMISE-103: absence of primary text is a kind-difference in evidence, not a degree-difference, and
      no confidence label over metadata-only material is well-founded. This directly governs the four
      "pointer, not a reading" cards and arguably already denies their ingest.
    Adjacent: PREMISE-050 (small scoped batches), PREMISE-090 (attended HITL pass for quality-sensitive
    backlogs), PREMISE-201 (a gate's precision has an abandonment band). Searched anyway per OPEN-192.

  Supporting evidence found: Yes

  Sources:
    1. Regulation (EU) 2016/679 (GDPR), Art. 4(11) and Recital 32; UK ICO guidance "What is valid
       consent?" — SECONDARY (statutory text and ICO guidance retrieved via search results, not fetched
       in full) — Consent must be "specific"; Recital 32 states that consent is presumed NOT freely given
       where it does not allow separate consent to be given to different processing operations despite
       that being appropriate. Bundling distinct items under one affirmative act is treated in law as
       *invalidating* the consent, not merely as weakening it. This is the strongest available support
       and it is a legal-institutional rather than empirical source.
    2. 45 CFR 46 (Common Rule) and the "broad consent" provisions; NIH/NCBI "Understanding Broad Consent."
       — SECONDARY — Research ethics permits aggregated authorisation only under an explicitly enumerated
       and narrowly bounded exception (storage/maintenance/secondary research use of identifiable data),
       and even then requires disclosure of the categories covered. The existence of a named, bounded
       exception is itself evidence of the background rule: aggregated authorisation does not by default
       carry item-level warrant.
    3. 21 CFR 56.109(a) / IRB review outcomes. — SECONDARY — An IRB has three outcomes available
       (approve, require modifications, disapprove), and the standard informed-consent requirements apply
       regardless of whether review was expedited or convened. Supports the narrower point that a
       lower-cost review *procedure* does not lower the substantive warrant required per item.
    4. SmartBear / Cisco Systems code review case study, 2,500 reviews / 3.2M LOC. — SECONDARY (primary
       PDF returned an empty body on fetch) — Defect-detection density falls sharply above ~200-400 LOC
       per review and above ~450 LOC/hour review rate. The measured mechanism — per-item attention
       degrades as the reviewed aggregate grows — is exactly what "a batch APPROVE can't distinguish"
       asserts, and supplies the empirical rather than normative support.
    5. ALMA Proposal Handling Team, 2022, arXiv:2204.05390, Figure 15. — VERIFIED (fetched; caption read
       directly) — Reviewers assigned 5+ proposal sets wrote significantly shorter comments to the PI
       than those assigned 4 or fewer. Independent, non-software evidence that per-item engagement falls
       with aggregate load.
    6. Rubber-stamping / bundled-authorisation literature in corporate and legislative governance
       (omnibus bills, board consent agendas). — UNVERIFIED — I was unable to retrieve a specific
       empirical study measuring item-level scrutiny under consent-agenda procedures. The concept is
       widely discussed but I found no quantitative source I could read, and I record it as unverified
       rather than drop it or let it carry weight.

  Strength of support: Strong

  Summary: The claim is that an aggregated authorisation cannot carry item-level warrant, and the
    supporting case comes from two independent directions that converge. Normatively, the two bodies of
    law that have most carefully thought about aggregated consent — EU data protection and US research
    ethics — both hold that specificity is constitutive of valid consent, with bundling either
    invalidating it (GDPR Recital 32) or permitted only under a narrow enumerated exception (broad
    consent). Empirically, the review-size literature shows that per-item scrutiny measurably degrades as
    the reviewed aggregate grows, in two unrelated domains (code review at Cisco, grant review at ALMA).
    The assumption's specific epistemic form — that a batch APPROVE is *indistinguishable* between "read
    and agreed" and "not read separately" — is stronger than either body of evidence establishes on its
    own, but it follows straightforwardly from PREMISE-172 (a mark carries no information about what was
    not examined) applied to an aggregate act.

  Caveats:
    - Consent and approval are not the same speech act. GDPR and the Common Rule govern authorisation
      *by the affected party over their own interests*; a review approval is a competence judgement by a
      third party. The specificity principle transfers by analogy, not by entailment, and someone could
      reasonably argue that a delegated reviewer is entitled to approve in aggregate on a sampling basis
      in a way a data subject is not. This is the strongest available objection and it is not answered by
      anything I retrieved.
    - The indistinguishability claim is about the *record*, not about what happened. A batch APPROVE is
      perfectly compatible with every item having been read. What the literature supports is that the
      record cannot evidence it — which is the useful form of the claim and the one that should be
      minted.
    - Four of the six cards are governed by PREMISE-103 independently of anything about batching: a
      paywalled recording and an institutional listing with no source text are metadata-only material,
      and the register already holds that no confidence label over such material is well-founded. The
      batching question is not what disposes of those four.
    - The rubber-stamping empirical limb is UNVERIFIED and carries no weight in this rating. The rating
      rests on 1-5.
    - Highest-stakes note, recorded because it follows from the finding: if the claim holds, it applies
      retrospectively to every prior batch APPROVE in the estate's approval record, not only to this one.
      That is PREMISE-118's retrospective-impact obligation and it is not discharged by this search.

  Search scope: comprehensive search — GDPR consent granularity and bundling (Art. 4(11), Recital 32, ICO
    guidance), IRB review types and expedited-review consent standards, broad consent under the revised
    Common Rule, rubber-stamping in review boards and consent agendas, code-review batch size and defect
    detection, peer-review assignment load effects.

  Recommendation: SUPPORTED — resting on the GDPR/Common Rule specificity limb plus the Cisco and ALMA
    per-item-degradation limb. The indistinguishability claim should be minted in its record-level form
    ("the record cannot evidence item-level reading"), not in the behavioural form.
