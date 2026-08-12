SEARCH-FOR-ASSUMPTION-017:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-017
  Original statement: "AI synthesis is complementary to human validation; AI does first-pass synthesis, humans validate."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 5)
    Original item: ASSUMPTION-017
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from morning walk chat summary 2026-04-14
      15a (cycle 1, 2026-04-14): initial supporting search — human-AI evidence synthesis, Nature Human Behaviour meta-analysis on human-AI combinations, complementarity framework; SUPPORTED, Strong
      15d: re-triggered for cycle 5 monitoring
      15a (cycle 5, 2026-08-11): re-searched for supporting literature; checked for new sources since April 2026
    Current status: SUPPORTED

  Search scope: LLM-assisted systematic review screening and triage (2025-2026); prospective/deployed validations against Cochrane reference standards; human-LLM collaboration in evidence synthesis; scoping reviews of LLM readiness for review conduct. Comprehensive — this is the best-evidenced item in the cycle-5 cohort.

  Supporting evidence found: Yes

  Sources:
    1. medRxiv 2026.06.02.26354724, 2026. "Audited large language model triage for systematic review screening in national clinical guideline production: validation and prospective deployment." — NEW and the strongest source in this file. Ten LLMs across five model families benchmarked on 419 Cochrane reviews / 26,892 records; selected ensemble achieved 98.0% mean review-level sensitivity. Prospective deployment at Sweden's National Board of Health and Welfare screened 74,679 records and cut estimated first-pass screening effort from 415 to 34 person-days. This is precisely the "AI first pass, human validation" division of labour, validated *and then actually deployed* in a national guideline body.
    2. medRxiv 2025.11.08.25339805. "Computational Review of Technology-Assisted Medical Evidence Synthesis through Human-LLM Collaboration: A Case Study of Cochrane." — NEW. Frames human-LLM collaboration (not substitution) as the operative model for evidence synthesis and evaluates it against Cochrane's dual-independent-screener standard.
    3. medRxiv 2025.11.03.25339455. "Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access." — NEW. Near-perfect sensitivity across 16 Cochrane reviews; notable because it demonstrates the pattern works without privileged API tooling.
    4. arXiv 2603.22327, 2026. "Evaluating AI-based Scientific Knowledge Synthesis with Epidemiological Systematic Reviews." — NEW. Extends evaluation from screening to synthesis proper, the step ASSUMPTION-017 actually claims.
    5. ScienceDirect (J. Clinical Epidemiology) S0895435625000794. "Large language models for conducting systematic reviews: on the rise, but not yet ready for use — a scoping review." — NEW. Supports the assumption in its precise form: LLMs are "not yet at the capability threshold to replace expert judgment," and their "clearest short-term role is to accelerate human-led review at points where missed evidence is most costly." This is an endorsement of complementarity, not of autonomy.
    6. Nature Human Behaviour, 2024. "When combinations of humans and AI are useful: a systematic review and meta-analysis." — Carried forward from cycle 1; establishes that human-AI combinations outperform AI alone in content-creation-type tasks but require deliberate design.

  Strength of support: Strong

  NEW SINCE LAST CYCLE: Yes — sources 1-5 are all new to this file since April 2026, and four of them are 2026-dated. What they add: the April evidence base was largely framework-level and retrospective; the 2026 evidence base includes a *prospectively deployed* national-scale system with quantified sensitivity (98.0%) and quantified human effort reduction (415 → 34 person-days), plus an independent scoping review that states the complementarity position explicitly. This is the largest genuine movement of any item in the cycle-5 cohort.

  Evidence trajectory (supporting): growing

  Summary: Support for ASSUMPTION-017 has strengthened materially since April 2026. The assumption's exact structure — AI performs the first pass, humans validate — is now the documented operating model of a national clinical guideline producer, with peer-reviewable sensitivity figures and effort savings. The 2025-2026 scoping review independently arrives at the same position from the sceptical direction: LLMs are not ready to replace expert judgment, so the defensible use is human-led review accelerated by AI triage. Both the optimistic and the cautious strands of the 2026 literature converge on complementarity. Support is now Strong on a firmer empirical footing than in April.

  Caveats: (a) The deployment evidence is concentrated in biomedical systematic review, where inclusion criteria are pre-specified and the ground truth (Cochrane adjudication) is unusually well defined; C2A2's synthesis task has no comparable reference standard. (b) "Audited" is doing work in source 1 — the reported performance depends on a human audit layer that C2A2 does not obviously have an analogue for. (c) The 98% sensitivity figure is review-level mean; per-review variance and the cost of the residual 2% are not addressed. (d) Automation bias remains the standing risk: the assumption holds only if human validation is genuinely active rather than nominal, and none of the sources measures validator engagement in C2A2's regime. (e) Several key sources are preprints (medRxiv/arXiv) and not yet peer reviewed.

  Recommendation: SUPPORTED
