SEARCH-FOR-PRESUMPTION-871:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-871
  Queue ref: LIT-QUEUE-2026-08-24-008
  Original statement: "Contradictions between independent agents' reports will be surfaced without a dedicated reconciliation mechanism."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-871
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from three same-day incompatible reports of one artifact's freshness, none referring to another
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-25. Queries covered (a) ensemble/cross-model disagreement as an
    uncertainty or correctness signal in LLM agent systems; (b) multi-agent debate and error
    detection, including judge-free and heterogeneous-agent variants; (c) blackboard and
    shared-memory multi-agent architectures, specifically whether divergence in a shared workspace
    becomes visible to any reader without a central coordinator; (d) the non-AI analogue —
    triangulation across independent sources, double data entry, and audit discrepancy detection.
    Venues: arXiv (HTML and PDF), ScienceDirect, OpenReview, Emergent Mind topic pages,
    methodology guides, USPTO. Date range: no restriction; supportive hits cluster 2025–2026.
    Titles of the two primary arXiv sources were verified by direct fetch; author lists were not
    captured and are marked unverified.
    Assessment: **preliminary — broader search recommended.** Gaps: the web-search budget was
    exhausted before I could search the distributed-systems limb (version vectors, read repair,
    CRDT conflict detection) or the organisational/HRO literature on cross-checking. Author
    attributions for the 2026 arXiv preprints could not be confirmed.

  Supporting evidence found: Partial

  Sources:
    1. "Cross-Model Disagreement as a Label-Free Correctness Signal." arXiv:2603.25450 (v2).
       https://arxiv.org/html/2603.25450 [authors unverified]
       — Title verified by direct fetch; paper develops cross-model perplexity and cross-model
       entropy as measures that identify incorrect outputs *without labels*. Supports the core
       supportive proposition: the fact of divergence between independently produced outputs is
       itself information-bearing and readable off the outputs, rather than requiring a separate
       adjudicating authority to establish. FULL-TEXT (retrieved; read in part).
    2. "When Agents Disagree With Themselves: Behavioral Consistency as an Uncertainty Signal for
       LLM Agents." arXiv:2602.11619 (v2). https://arxiv.org/html/2602.11619v2 [authors unverified]
       — Title verified by direct fetch. Frames each independent agent run as an implicit ensemble
       member and treats cross-run disagreement as a model-agnostic uncertainty signal that is
       black-box and "requires no calibration set, no log-probs, and no prompting strategy." This
       is the strongest single piece of support: it asserts that the disagreement signal is
       obtainable from repeated independent execution alone, with no added apparatus.
       FULL-TEXT (retrieved; read in part).
    3. "DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent
       Ensembles." arXiv:2603.20975. https://arxiv.org/html/2603.20975 [authors unverified]
       — Argues that inter-agent disagreement has rich internal structure (shared evidence, point
       of divergence, minority argument strength, representational clustering) that is highly
       informative about whether the majority is correct. Supports the claim that contradictions
       carry a strong, extractable signature in independently produced reports. SNIPPET-ONLY.
    4. "Consensus is Strategically Insufficient: Reasoning-Trace Disagreement as a
       Knowledge-Representation Signal." arXiv:2606.04223. https://arxiv.org/pdf/2606.04223
       [authors unverified]
       — Argues that multi-agent systems are typically designed to *suppress* disagreement and
       that this is a mistake, since disagreement may be a stable property of the case. Supports
       the view that raw, unreconciled disagreement is a legitimate and readable output state
       rather than a defect that must be resolved before it can be seen. SNIPPET-ONLY.
    5. "Towards Scalable Oversight with Collaborative Multi-Agent Debate in Error Detection" /
       "When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?"
       arXiv:2510.20963 (v2). https://arxiv.org/html/2510.20963v2 [authors unverified]
       — Reports that heterogeneous agents (different providers) fail less often simultaneously
       and that error-reduction rates rise with heterogeneity. Supports the underlying premise
       that independence between reporters is what makes contradictions informative and
       detectable. SNIPPET-ONLY.
    6. "LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science."
       arXiv:2510.01285 (also OpenReview egTQgf89Lm). https://arxiv.org/html/2510.01285v1
       [authors unverified]
       — Blackboard architecture: agents interact indirectly through a shared structured workspace
       rather than by direct messaging, and the approach is described as eliminating the need for
       a rigid central coordinator. Supports the specific supportive mechanism relevant here —
       that when independent reports are posted to a common surface, divergence among them is
       visible to any agent that reads the surface. SNIPPET-ONLY.
    7. "Understanding Shared Memory In Multi-Agent Systems." JumpCloud IT Index (undated).
       https://jumpcloud.com/it-index/understanding-shared-memory-in-multi-agent-systems
       — Practitioner statement that state updates in shared multi-agent memory are visible across
       the system, so inconsistencies in shared state are observable by any agent reading it.
       SNIPPET-ONLY.
    8. "What Is Triangulation In Qualitative Research?" SimplyPsychology (undated), and
       "Triangulation in Research: Definition, Types, Examples, and Steps." researchmethod.net.
       https://www.simplypsychology.org/what-is-triangulation-in-qualitative-research.html
       — The methodological tradition in which comparing independently obtained accounts is
       expected to reveal conflicting information, and in which discovered inconsistency is
       treated as substantively informative rather than as a failure. Supports the general
       principle in the human-research analogue. SNIPPET-ONLY.
    9. "ContraGen: A Multi-Agent Generation Framework for Enterprise Contradictions Detection."
       arXiv:2510.03418 (v1). https://arxiv.org/html/2510.03418v1 [authors unverified]
       — Evidence that contradictions in accumulated enterprise text are detectable from the text
       itself, including contradictions arising from evolving/superseded statements.
       SNIPPET-ONLY.

  Strength of support: Weak

  Summary: There is a substantial and growing 2025–2026 literature holding that disagreement
    between independently produced agent outputs is a real, extractable and informative signal.
    The most directly supportive result is that cross-run behavioural disagreement functions as a
    model-agnostic uncertainty signal obtainable in black-box fashion from repeated independent
    execution alone — no calibration set, no log-probabilities, no special prompting — which is
    close to the presumption's claim that no dedicated apparatus is required. Cross-model
    disagreement is likewise reported to be a label-free correctness signal, and structured
    analyses of inter-agent disagreement find that its internal structure is highly diagnostic.
    A second, architectural strand supports the claim by a different route: blackboard and
    shared-memory designs, in which agents post to a common workspace, are described as making
    inconsistent state visible to any reader and as removing the need for a rigid central
    coordinator. The triangulation tradition in qualitative research provides the human analogue —
    comparing independent accounts is expected to expose conflict, and the conflict is treated as
    a finding.

  Caveats: The support is real but does not reach the presumption's strongest reading. Every
    supportive source describes a *deliberate comparison* — an ensemble is run, cross-run variance
    is computed, disagreement structure is analysed, a blackboard is read. None establishes that
    contradictions surface *spontaneously*, i.e. to a reader who is not already looking for them
    and who encounters the reports at different times or in different places. The blackboard
    result depends on the reports actually landing on a shared surface with a common key; three
    reports about one artifact that "none refer to another" satisfy the independence precondition
    but not necessarily the co-location precondition. The double-data-entry analogue, which is the
    most established human-process instance, in fact runs an explicit reconciliation step (e.g.
    SAS PROC COMPARE) and so supports detectability rather than mechanism-free detectability. The
    2026 arXiv sources are preprints whose author lists I could not verify and whose results are
    not independently replicated. Finally, the disagreement-as-signal literature concerns
    disagreement about *answers to a posed question*; transferring it to disagreement about
    *observed state of an artifact* (freshness) is a domain transfer that no source I found makes.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that disagreement among independently produced agent reports is a
    genuine, extractable, informative signal; (ii) that it can be read from black-box outputs
    without a trained arbiter, calibration set, or judge model; (iii) that shared-workspace
    architectures make divergent postings visible to any reader without a central coordinator.
    Unaddressed sub-claim: **that contradictions will be surfaced with no comparison step at all
    — that is, that a mutually incompatible set of same-day state reports becomes visible to a
    downstream reader who is not deliberately collating them and who may encounter the reports
    asynchronously.** All supportive literature located presupposes that some agent or process
    actually places the independent reports side by side. Whether that collation counts as the
    "dedicated reconciliation mechanism" the presumption denies is the precise point on which no
    source speaks.
