SEARCH-FOR-ASSUMPTION-1624:
  Date searched: 2026-09-23
  Original item: ASSUMPTION-1624
  Original statement: Two same-model agents with separate contexts but identical tools and claim wording
    produce searches independent enough to count as FOR and AGAINST evidence.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1624
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the fix claim; verified the reported writes; flagged the tension with PREMISE-004
        to 14b.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I., 2024. "Improving Factuality and
       Reasoning in Language Models through Multiagent Debate." ICML 2024 (arXiv 2305.14325). — Multiple
       instances of the same model, with identical prompts, propose a diverse range of answers and
       improve factuality through debate. Supports the idea that same-model instances with separate
       contexts are not fully redundant.
    2. Wang, X. et al., 2023. "Self-Consistency Improves Chain of Thought Reasoning in Language Models."
       ICLR 2023 (arXiv 2203.11171). — Independent samples from one model on one prompt yield diverse
       reasoning paths whose majority vote substantially beats single-sample accuracy (e.g. GSM8K
       +17.9%). Shows sampling alone produces partially independent outputs.
    3. Kim, E. et al., 2025. "Correlated Errors in Large Language Models." ICML 2025 (PMLR v267;
       arXiv 2506.07962). — Only indirect support: even across >350 models, error agreement (~60% when
       both err) is high but not total, so some independent signal remains. Principally this source
       cuts the other way (same-provider/same-architecture raises correlation).

  Strength of support: Weak

  Summary: The literature supports a weak form of the assumption: separately sampled instances of one
    model do produce non-identical outputs, and aggregating them adds measurable value (self-consistency,
    multiagent debate). However, these gains are measured on accuracy of convergent answers, not on
    whether directed FOR vs AGAINST searches constitute independent evidence. No source found shows that
    same-model agents with identical tools and claim wording are independent enough to be counted as
    separate evidential lines in an adversarial-collaboration sense. Support is for "partially
    independent," not "independent enough."

  Caveats: Supportive results come from tasks with a single correct answer and temperature sampling;
    directional search (support vs refute) introduces a task-framing difference that may add diversity
    (favourable) but shared retrieval tools and shared query wording likely return overlapping source
    pools (unfavourable). The same searches surfaced several sources reporting strong error correlation
    in homogeneous ensembles; those are 15b's lane and are noted here only so the partial rating is
    not read as stronger than it is.

  Search scope: Preliminary — three searches (correlated LLM errors; multiagent debate same model;
    self-consistency sampling). No literature found on independence of adversarially-framed searches by
    same-model agents specifically.

  NOVELTY-FLAG:
    Item: ASSUMPTION-1624
    Searched: LLM ensemble diversity, self-consistency, multiagent debate, correlated errors
    Finding: No existing literature directly tests whether direction-assigned (FOR/AGAINST) same-model
      search agents yield independent evidence
    Implication: C2A2's 15a/15b split could itself be an empirical test case (measure source overlap)
    Recommended status: NOVEL (for the specific configuration only)

  Excluded results: GitHub issue "AkihikoWatanabe/paper_notes #2145" (repo mirror of the Kim et al.
    paper; primary venue used instead).

  Recommendation: PARTIALLY-SUPPORTED
