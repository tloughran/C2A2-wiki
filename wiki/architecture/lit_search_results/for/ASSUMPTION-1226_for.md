SEARCH-FOR-ASSUMPTION-1226:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1226
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: A gate set built on ids, glosses, grades and length signals cannot detect
    argument-layer inversions (semantic reversal) in doctrinal or technical prose; detection methods for
    such reversal exist elsewhere.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1226
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the Summa QC sweep; n=1 generalisation flagged in status.
      15a: Searched for supporting literature
    Current status: SUPPORTED (limb a) / PARTIALLY-SUPPORTED (limb b)

  Search scope: WebSearch, 2026-08-28, one dedicated query on the limits of static checking for semantic
    defects and on NLI for meaning reversal. Literature reached: a 2026 industrial experience report on
    LLM-based static verification of code against natural-language requirements (arXiv:2605.17926); a 2026
    paper on dataset defects in Lean theorem-proving benchmarks (arXiv:2606.29493); survey material on
    Natural Language Inference; a Springer NPL survey on multilingual NLI. NOT COVERED and material:
    (i) the software-defect-taxonomy literature proper (ODC / IEEE 1044), which the queue entry asked for
    by name; (ii) argument-mining and stance-detection work, which is the nearest match for "argument-layer
    inversion"; (iii) anything on doctrinal or theological prose specifically. All sources SNIPPET-ONLY.
    Search confidence: HIGH on limb (a), MODERATE on limb (b).

  Supporting evidence found: Yes (limb a) / Partial (limb b)

  Sources:
    1. Anon., "LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial
       Experience Report" (arXiv:2605.17926) [SNIPPET-ONLY; authors unverified] —
       Two directly on-point findings: automated checking that does not separate enforceable logic from
       ambiguous or contradictory statements "can create false confidence"; and important defects arise
       from mismatched triggers, partial enforcement and incorrect execution paths rather than from missing
       keywords or local syntactic violations, so useful analysis must reason about *intended behaviour*
       rather than textual resemblance. This is limb (a) in its general form.
    2. Anon., "Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem
       Proving" (arXiv:2606.29493) [SNIPPET-ONLY; authors unverified] —
       States the division explicitly: static checkers are cheap and deterministic but cannot assess whether
       a formalisation captures intent; LLMs can reason about semantics but require human verification.
       This is the cleanest statement of limb (a) found, and it is stated in a field (formal mathematics)
       where the static checker is far stronger than anything in the C2A2 gate set.
    3. Emergent Mind, "Natural Language Inference (NLI)" topic survey [SNIPPET-ONLY]
       https://www.emergentmind.com/topics/natural-language-inference-nli ; and Springer, Neural Processing
       Letters, "A Study of the State of the Art Approaches and Datasets for Multilingual Natural Language
       Inference" (2024), doi:10.1007/s11063-024-11673-2 [SNIPPET-ONLY] —
       Documents NLI reformulation with label verbalisation outperforming baselines for requirements
       defect detection and conflict analysis, i.e. a real method for limb (b); and simultaneously reports
       that models generalise poorly off-domain and are sensitive to subtle perturbation and superficial
       lexical change.

  Strength of support: Strong (limb a) / Weak-Moderate (limb b)

  Summary: The first limb of the assumption is supported at textbook strength and from a field where the
    static apparatus is much stronger than C2A2's: a checker over identifiers, structure and surface form
    is definitionally unable to decide whether the content means what it was meant to mean. Two independent
    2026 sources state this in almost the assumption's own terms, and one adds the sharper point that a
    structural gate which appears to check can manufacture false confidence — worse than no gate. The
    second limb is only weakly supported: semantic methods (NLI reformulation, LLM verification) exist and
    are reported to work on requirements-engineering defect detection, but every source that reports them
    working also reports domain-transfer failure and lexical brittleness.

  Caveats: Both primary sources are 2026 arXiv preprints with unverified author lists, read at snippet
    level; neither concerns doctrinal prose. The n=1 basis of the original observation is untouched by
    this search — the literature supports the mechanism, not the frequency.

  Recommendation: SUPPORTED (limb a); PARTIALLY-SUPPORTED (limb b)
