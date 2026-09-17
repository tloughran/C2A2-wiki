SEARCH-FOR-ASSUMPTION-508 — CYCLE 1 (15d re-trigger). The cycle-0 file ASSUMPTION-508_for.md (2026-08-30) is
preserved untouched; this file re-establishes the support at abstract/full-text level and adds new sources.

SEARCH-FOR-ASSUMPTION-508:
  Date searched: 2026-09-17
  Original item: ASSUMPTION-508
  Original statement: "McGilchrist-002 entered at Speculative because only title/venue were available; flagged
    transcript-verify-before-ingest — fail loud, not fabricate." Searched on the GENERALIZABLE limb only:
    provenance-gated confidence scoring; abstention under missing source rather than fabrication; a labelled
    gap as a first-class output. The internal-empirical limb (whether the transcript exists) is NOT-SEARCHED.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a]
    Original item: ASSUMPTION-508
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-22 specialist run.
      15a (cycle 0): SUPPORTED, Strong — four arXiv sources, all snippet-level, zero abstract/full-text reads.
      15b (cycle 0): not independently searched (NO-CHALLENGE-FOUND by default).
      15c: MONITOR-575, HIGH for procedural reasons — "would very likely mint on a proper pairing."
      15d: Re-triggered 2026-09-13 as cycle 1.
      15a (cycle 1): Read two key sources at full-text level (CiteCheck; Jülich's assertibility constraint),
        one new source at abstract level (HLE-Verified), one supporting source at full text (arXiv:2604.18880);
        fresh search for abstention / selective prediction / epistemic-status labelling since 2026-08-30.
    Current status: SUPPORTED (now at source level)

  Search scope: web_fetch of arXiv:2605.27700 (HTML full text), arXiv:2603.03971 (HTML full text, §§4.3–4.4
    and reason-class list read; abstract via search), arXiv:2602.13964 (PDF), arXiv:2604.18880 (HTML full
    text, shared with the ASSUMPTION-1211 cycle-1 search). WebSearch queries: CiteCheck; assertibility
    constraint / provenance gap; LLM abstention, selective prediction, provenance-gated confidence, refuse
    rather than fabricate; knowledge-base ingest epistemic-status / confidence labels / unverified source.
    Confidence: **comprehensive on the two named key sources; moderate on the fresh search** (abstention
    literature is large; snippet-level beyond the sources listed). Not re-read: cycle-0 sources
    arXiv:2603.14170 and arXiv:2605.08583, which remain snippet-level.

  Supporting evidence found: Yes — direct, and now read at source.

  Sources:
    1. Jülich, M. 2026. "No Certificate, No Categorical Speech Act: A Brouwerian Assertibility Constraint for
       Public Reason." arXiv:2603.03971. [FULL TEXT, §§4.3–4.4 read at source; abstract via search]
       CORRECTION to cycle 0: the paper does not use the phrase "world-grounded vs pipeline-grounded gaps";
       that was a paraphrase. What it does say is stronger and more exact. Three-status interface semantics
       {Asserted, Denied, Undetermined}; statuses "mark entitlement to categorical speech rather than truth
       values." A/D require "a publicly inspectable and contestable certificate of entitlement; otherwise
       [the system] must return Undetermined." The certificate token carries a provenance field; "If any
       mandatory field is withheld or cannot be verified ... the only licensed interface output is U,
       accompanied by a reason class identifying which element of the certificate boundary failed." Mandatory
       reason classes include **U-SCOPE: "scope, identity, provenance, or eligibility conditions fail or cannot
       be verified"** and U-EVIDENCE ("eligible public sources exist, but do not yet warrant"). Explicitly
       "a contract-relative semantic obligation, not a tunable statistical reject option based on
       confidence" — i.e. provenance-gated, not confidence-gated. "U is not a failure state but a
       deliberative safeguard by design"; the trace must state "what would have to change for an Asserted
       ... status to become licensed." Every limb of the item — gate on provenance, withhold rather than
       assert, label the gap and its cause, say what would close it — is present in terms.
    2. Zhai, W., Wang, Z. et al. (Alibaba / Qwen Team) 2026. "HLE-Verified: A Systematic Verification and
       Structured Revision of Humanity's Last Exam." arXiv:2602.13964. [ABSTRACT + construction section at
       source — NEW this cycle] Of 2,500 items, 668 verified, others repaired, and "the remaining 689 items
       are released as a documented uncertain set with explicit uncertainty sources and required expertise
       tags." "Rather than discarding them, we retain these items as an explicit epistemic category,
       reflecting cases where validity cannot be established with sufficient confidence." Each uncertain item
       carries "an uncertainty source label" and "a required expertise tag indicating the type of specialist
       input needed for resolution." This is the labelled gap as a first-class output with a resolution
       pointer attached — the closest published analogue to "Speculative + transcript-verify-before-ingest."
    3. CiteCheck, arXiv:2605.27700. [FULL TEXT read at source] Verifies "whether a citation corresponds to a
       real scholarly work and whether its metadata is faithful to that work" — existence and fidelity are
       separate checks. Three severity labels: Exact / Minor ("the intended paper still exists, but one or
       more bibliographic fields are corrupted") / Major (no matching work). Retrieval is "candidate
       generation rather than final verification." Supports the item's premise that a record known only by
       title and venue is not thereby licensed for content claims: a citation can be Minor-corrupt with its
       title intact. Caveat: its Minor class is synthetic (GPT-4o-mini corruptions, §4.2); it is a detector
       benchmark, not a study of ingest policy.
    4. Chen, Y. et al. 2026. "Where Fake Citations Are Made." arXiv:2604.18880. [FULL TEXT at source] From
       parametric memory alone, author fields are correct under 14% of the time at N=15 across 9 models.
       Establishes the base rate that makes a fabrication-free default worth having: content recalled
       without a source is unreliable at the field level, so "only title/venue available" is a state that
       should block, not license, further content.
    5. Cycle-0 sources retained at snippet level: arXiv:2603.14170 (closed-world citation policy — cite only
       ids in the session evidence table, else abstain); arXiv:2605.08583 ("Source or It Didn't Happen" —
       abstention complementary to citation enforcement). Not re-read.
    6. Snippet-level, fresh: "Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction"
       (arXiv:2605.25133 — "the selector is not a thresholded probability but the outcome of structured
       verification dialogue"); "I-CALM: Incentivizing Confidence-Aware Abstention" (arXiv:2604.03904);
       "Uncertainty-Aware Abstention ... with Provable Alignment Guarantees" (arXiv:2607.04430); "Trust, but
       Don't Verify: Epistemic Blind Spots in LLM Source Evaluation" (arXiv:2606.05403). Confirm the
       abstention literature is active; not read at source.
    7. Cross-item, at source: ISO 15489-1:2016 §5.2.2.2 (read for PRESUMPTION-1019) — a reliable record is
       created "by individuals who have direct knowledge of the facts, or by systems routinely used to conduct
       the transaction." A title/venue-only entry lacks the direct-knowledge condition; marking it Speculative
       is the records-management posture, not only the LLM-safety one.

  Strength of support: **Strong**, and now at abstract-or-better level for four of the load-bearing sources.

  Summary: The discipline the item describes — score confidence by provenance, withhold content when the
    source is missing, and emit the gap as a labelled object with its cause and the action that would close
    it — is stated in terms by Jülich's output contract (1): U-SCOPE is precisely "provenance ... cannot be
    verified," U is mandatory and carries a reason class, and the gate is contractual rather than a
    confidence threshold. HLE-Verified (2) shows the same discipline applied at scale to a curated knowledge
    artefact: 689 items kept as "an explicit epistemic category" with an uncertainty-source label and a
    required-expertise tag, rather than silently repaired or dropped. CiteCheck (3) supplies the existence-
    versus-fidelity distinction that makes "title and venue only" an insufficient state, and Chen et al. (4)
    supply the base rate that makes fabrication the default alternative. The support is no longer snippet-
    level and no longer rests on a single generation-time setting: (1) is an interface contract, (2) is
    benchmark curation, (3)–(4) are generation-time detection and measurement.

  Caveats: Sources 1–4 are 2026 arXiv preprints; (1) is a philosophical framework paper without empirical
    evaluation; (2) concerns exam items, not bibliographic ingest. Setting transfer remains: none of the
    sources is about a personal knowledge base ingesting a talk transcript. The cycle-0 gloss of (1) was a
    paraphrase presented as the paper's terms; corrected above. The pairing remains incomplete until 15b
    searches this item independently, which is MONITOR-575's stated condition and is outside this file.

  Recommendation: **SUPPORTED** (Strong; source-level).

  NOVELTY-FLAG: NOT RAISED. The generalizable limb is a documented, named practice in at least three settings.

  Independence attestation: Read — agents/15a_lit_search_for_agent.md; architecture/provenance_protocol.md;
    lit_search_results/for/ASSUMPTION-508_for.md (cycle 0); monitor_queue.md lines 22385–22405 (MONITOR-575
    only; the sed window also displayed the first lines of MONITOR-576, which were not used). NOT read — any
    against/ file dated 2026-09-17, lit_search_returns.md, revision_flags.md, validated_premises.md, any
    other monitor_queue.md entry.
