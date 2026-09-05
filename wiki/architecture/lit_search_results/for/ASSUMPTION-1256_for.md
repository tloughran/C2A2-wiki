SEARCH-FOR-ASSUMPTION-1256:
  Date searched: 2026-09-05
  Original item: ASSUMPTION-1256
  Original statement: "The sandbox output needs Tom's eyes, not more agent passes. ... The question they
    answer — what is actually in the sandbox, and does the outline hold — can only be closed by reading it."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1256
    Item type: ASSUMPTION (stated — quoted from a derived digest)
    Transform at each step:
      14a: Extracted verbatim from 2026-09-04_cowork_summary.md "What's Next" §1. Paired with PRESUMPTION-910.
      15a: Searched for supporting literature (2026-09-05). NOTE ON AUTHORSHIP: this search was run by the
        15c orchestrating context after the delegated 15a subagent was interrupted twice before writing;
        it was run and written BEFORE any 15b search for this item was begun in the same context.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Madaan et al. 2023, "Self-Refine: Iterative Refinement with Self-Feedback," arXiv:2303.17651
       [VERIFIED: title and arXiv ID; author list from memory of the paper, NOT re-verified in results] —
       The founding self-refinement paper's own curves show the largest gains in the first 1–2 rounds with
       marginal improvement decreasing thereafter; secondary summaries report saturation after ~3 loops.
       Supports the "not more agent passes" half: further passes are on the flat part of the curve.
    2. "Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning," arXiv:2608.05643
       [VERIFIED: title/ID; authors NOT verified] and "Revision or Re-Solving? Decomposing Second-Pass Gains
       in Multi-LLM Pipelines," arXiv:2604.01029 [VERIFIED: title/ID; authors NOT verified] — Both state
       the now-standard finding that intrinsic self-correction without a reliable external feedback channel
       is often ineffective and can degrade output; revision is reliable only when the feedback source is
       dependable. An expert read IS the dependable external channel the literature says is required.
    3. Huang et al. 2023/2024, "Large Language Models Cannot Self-Correct Reasoning Yet" [NOT verified in
       this search — cited from the summaries above, which report the oracle-feedback contrast: ~0.2%
       self-refine gain vs. ~4.8% with oracle feedback for GPT-3.5]. Same direction as (2).
    4. SmartBear / Cisco code-review study (2,500 reviews, 3.2M LOC, ~10 months) [VERIFIED: reported at
       smartbear.com "Best Practices for Peer Code Review"; primary Cohen 2006 report NOT retrieved] —
       Human review yields 70–90% defect discovery at 200–400 LOC per 60–90 min. Supports that a human read
       has high yield PER UNIT REVIEWED. (The same study's size limits are the strongest caveat; see below.)
    5. Kili / Maxim practitioner syntheses of LLM-as-judge vs human-in-the-loop 2025 [VERIFIED: pages
       located; not peer-reviewed] — report expert–LLM-judge agreement of only ~60–70% in specialist
       domains, which is the precondition for "Tom's eyes" adding information an agent pass cannot.
    6. "Knowledge graph validation by integrating LLMs and human-in-the-loop," Information Processing &
       Management 2025, S030645732500086X [VERIFIED: title/journal/ID; authors NOT verified] — HITL
       validation stages are reported as critical for precision and interpretability of LLM-derived
       constructs; iterative refinement with domain expertise improves classification reliability.

  Strength of support: Moderate

  Summary: The literature supports the assumption's contrast rather than its conclusion. It is well
  established that iterated LLM self-review saturates after two to three passes and that self-correction
  without a dependable external feedback source is unreliable or harmful; an expert human read is the
  canonical dependable source, and specialist-domain studies put LLM-judge/expert agreement low enough
  (~60–70%) that the human read carries information the passes do not. What the literature does NOT
  support is the implicit claim that a single human read of a 16,102-line document can "close" the
  question: the best-measured human-review data show detection dropping sharply above ~400 lines per
  sitting and after 60–90 minutes. The assumption is right that the marginal agent pass is worth little;
  it is unsupported that the marginal human read of THIS size is worth much without structuring.

  Caveats: (a) The SmartBear numbers cut both ways — 16,102 lines at 300–400 LOC/hour is 40–50 review
  hours, and the same source says detection collapses past 500 LOC/hour and past 90 minutes; the
  assumption as stated ignores this. (b) Self-refinement results are for generation tasks, not for
  document-structure auditing; transfer is by analogy. (c) No source addresses the specific case of an
  author reviewing his own reorganised material, where recognition memory should help but ownership
  bias may hurt (not searched — 15b's angle). (d) Search scope: preliminary — ~4 queries; did not cover
  the technical-editing or systematic-review-screening literatures on single-reviewer recall.

  Recommendation: PARTIALLY-SUPPORTED
