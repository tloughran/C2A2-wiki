SEARCH-AGAINST-PRESUMPTION-001:
  Date searched: 2026-09-02
  Original item: PRESUMPTION-001 (MONITOR-6)
  Original statement: "Splitting Agent 14 into 14a (assumption extractor) and 14b (presumption
    detector) improves quality versus a single unified agent."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b] (cycle-5 monthly re-check)
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: original inference (this was never stated by the designers; it was surfaced)
      15c (2026-04-13): dispositioned MONITOR
      15d: re-triggered, cycle 5 (59 days overdue)
      15b (2026-09-02): searched for challenging literature
    Current status: CHALLENGED
    NOTE ON ITEM TYPE: because this is a PRESUMPTION, the designers did not know they were
    assuming it. A strong challenge therefore carries extra weight — there is no prior record of
    the tradeoff having been considered and accepted, so nothing in the design history counts as
    a reasoned defence. Treat the absence of a stated rationale as unexamined, not as settled.

  Challenging evidence found: Yes

  Sources:
    1. Kiela, D. & Tran, D. (2026). "Single-Agent LLMs Outperform Multi-Agent Systems on
       Multi-Hop Reasoning Under Equal Thinking Token Budgets." arXiv:2604.02460. Full abstract
       and author attribution verified.
       — The compute-matched comparison this item has needed since April. Reports that gains
       attributed to multi-agent systems are "often confounded by increased test-time computation,"
       and that when computation is normalised, single-agent systems consistently MATCH OR
       OUTPERFORM multi-agent systems on multi-hop reasoning. Gives an information-theoretic
       reason grounded in the Data Processing Inequality: when one agent passes a message to
       another, the receiver works from a processed version of the original context, so
       information can only be lost or held constant across the chain, never gained. Under a fixed
       token budget with good context utilisation, a single agent is strictly more
       information-efficient. Tested across Qwen3, DeepSeek-R1-Distill-Llama and Gemini 2.5.
       Also identifies budget-control artefacts and benchmark artefacts that INFLATE apparent
       multi-agent gains — i.e. the prior literature was measuring the wrong thing.

    2. Cemri, M., Pan, M. Z., Yang, S., et al. "Why Do Multi-Agent LLM Systems Fail?"
       arXiv:2503.13657. (MAST taxonomy.)
       — 1,600+ annotated execution traces across 7 multi-agent frameworks, 14 failure modes,
       Cohen's kappa 0.88 across six expert annotators. Roughly 41.8% of all failures are
       specification and system-design issues — and the enumerated examples are precisely the
       hazards of a 14a/14b role split: ambiguous role definitions, poor task decomposition,
       DUPLICATE AGENT ROLES, and missing termination conditions. A further ~37% are coordination
       breakdowns and ~21% weak verification. The central finding is that these architectural
       failures, not base-model limitations, are the primary driver of multi-agent failure.

    3. "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous
       Multi-Agent Debate." arXiv:2605.00914v1 (May 2026). Full abstract read.
       — Homogeneous multi-agent structures consume 2.1–3.4x more tokens (up to 28,631 per
       problem) for equal or lower accuracy than isolated self-correction. Keyword list explicitly
       includes "Process Loss" and "Inference Economics." Relevant here because 14a/14b are
       homogeneous agents differentiated only by role prompt.

    4. "Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based
       Persona Routing with PRISM." arXiv:2603.18507v1 (March 2026).
       — Directly targets the mechanism by which a 14a/14b split is supposed to work. Reports that
       expert personas damage accuracy, and notes prior work finding near-zero average benefit
       from role specialisation on specialised tasks and that role-playing can degrade zero-shot
       reasoning. If assigning the role "assumption extractor" does not itself improve extraction,
       the split's premise is hollow. Title and framing verified in search results; full paper not
       read.

    5. Pipeline-vs-joint literature in information extraction. "An Empirical Study of Pipeline vs.
       Joint approaches to Entity and Relation Extraction," AACL 2022
       (aclanthology.org/2022.aacl-short.55/), plus the surrounding survey literature on cascading
       errors (e.g. Nature Sci. Rep. s41598-024-51559-w).
       — The closest well-studied analogue to the 14a/14b decomposition: a two-stage decomposition
       of a structured-extraction task. The settled finding is that pipeline architectures suffer
       cascading errors because the error signal from one module is not back-propagated to the
       other, and that with matched representations the best joint model still outperforms the
       best pipeline model. C2A2's split is a pipeline of exactly this shape, with the additional
       handicap that there is no shared training signal at all.

    6. Reported enterprise/deployment findings surfaced this cycle: in tool-rich environments
       (>~10 tools) distributed agent systems can suffer 2–6x efficiency losses from context
       fragmentation and split memory; and once a single agent's accuracy is above ~45%, adding
       agents tends toward diminishing or negative returns; benefit depends on task
       parallelisability, with tightly-coupled subtasks producing conflicting outputs that raise
       merge cost. NOTE: these figures come from secondary practitioner sources
       (sesamedisk.com, agentpatterns.ai, d4b.dev) surfaced in search, NOT from peer-reviewed
       primary work. I could not verify the underlying studies and they should carry
       correspondingly low weight. Flagged because the task-parallelisability point is
       conceptually important even if the numbers are not trustworthy: assumptions and
       presumptions in the SAME text are tightly coupled, not parallel.

  Strength of challenge: Strong

  Summary: The presumption is now challenged on all three fronts a defender would need: the
  empirical (compute-matched single-agent baselines match or beat multi-agent), the theoretical
  (the Data Processing Inequality gives a principled reason why splitting cannot add information
  under a fixed budget), and the mechanistic (role personas show near-zero or negative accuracy
  benefit; the pipeline-vs-joint literature shows cascading error costs). The Kiela & Tran result
  is especially awkward for C2A2 because it identifies the specific measurement error that makes
  splits look good — unaccounted compute — and 14a/14b was never compared against a
  compute-matched unified 14. There is also a substantive reason to think this particular split is
  a bad one: the DPI argument bites hardest when the second stage needs context the first stage
  consumed. 14b's job is to detect what 14a's source text did NOT say. Unstated presumptions are
  defined relative to the full assumption set, so a 14b working from 14a's output is reasoning
  about absences in a context that has already been compressed — the exact case the theory says is
  lossy. That said, the challenge is not total: Kiela & Tran explicitly predict multi-agent
  systems become competitive when a single agent's effective context utilisation degrades, which
  is a real escape hatch for long-document work, and the MAST taxonomy is a guide to avoiding
  these failures, not a proof they are unavoidable.

  Specific risks: If the split does not improve quality, three things follow. First, C2A2 is
  paying a multiple of the token cost for equal or worse output, and the apparent quality gain
  that justified the design was probably just the extra compute. Second, and more serious for a
  presumption at this position in the architecture: 14a/14b sits UPSTREAM of everything. Its
  output is the item set that 15a/15b/15c/15d spend all their cycles adjudicating. If the split
  causes systematic missed coverage — items falling in the gap because 14a treats them as
  14b's job and 14b treats them as 14a's — then the downstream machinery is validating a
  register with holes in it, and no amount of literature search on the items that ARE in the
  register will surface the ones that are not. Missed coverage is invisible by construction.
  Third, duplicate-role failure (an explicit MAST mode) predicts the opposite artefact: the same
  underlying item recorded twice under two IDs, one as ASSUMPTION and one as PRESUMPTION,
  inflating apparent coverage and consuming re-check cycles twice. Both failure modes are
  checkable against the existing register and neither appears to have been checked.

  Mitigations available:
    1. Run the compute-matched ablation. This is the only thing that actually settles it: a single
       unified Agent 14 given the summed token budget of 14a+14b, on the same source corpus,
       scored against a human-adjudicated gold set. Kiela & Tran's methodology is directly
       reusable. Everything else is hedging.
    2. Give 14b the raw source, not 14a's output. If 14b must run downstream, the DPI penalty is
       avoidable by re-supplying the original context rather than passing a processed summary.
       This is a small change with a principled justification.
    3. Audit the existing register for both predicted artefacts: (a) near-duplicate pairs across
       the ASSUMPTION and PRESUMPTION namespaces; (b) gap items — sample source documents and
       check by hand for items neither agent caught.
    4. Sharpen the role boundary, or drop it. MAST attributes 41.8% of failures to specification
       issues including ambiguous role definitions. If "stated" vs "unstated" is the only
       boundary, write down the adjudication rule for borderline cases explicitly.
    5. Consider a joint pass with a split output schema: one agent, one context, required to emit
       both assumption and presumption fields. This captures the taxonomic benefit of the split
       (which is real and worth keeping) without the pipeline cost.
    6. Record this as a design decision with a rationale, so it stops being a presumption. Its
       being unstated is itself part of the risk.

  STEELMAN:
    Item: PRESUMPTION-001
    Strongest counterargument: There is no evidence the split helps, a principled reason it should
    not, and a specific reason this split is worse than average. Under a fixed token budget the
    Data Processing Inequality says a two-agent chain can only lose information relative to one
    agent with the same budget, and compute-matched experiments across three model families
    confirm it: single agents match or beat multi-agent systems, and the reported multi-agent gains
    trace to unaccounted compute and benchmark artefacts. The mechanism the split relies on —
    role assignment producing specialist competence — shows near-zero or negative accuracy effects
    in the persona literature. The architecture the split instantiates — a two-stage pipeline
    without a shared error signal — is the one the extraction literature has known for years to
    suffer cascading errors. And the particular decomposition is the worst case for it: detecting
    what a text left unsaid requires the full text, so a 14b reading 14a's output is asked to find
    absences in a context from which absences have already been compressed away. Meanwhile the
    41.8% of multi-agent failures attributable to system design include duplicate roles and poor
    decomposition by name. The most likely truth is that 14a/14b costs 2x and buys taxonomy, not
    quality — and that the taxonomy could have been had from one agent with two output fields.
    What would need to be true for C2A2 to be safe: (a) a single unified 14 must be
    context-limited on the real corpus — Kiela & Tran name degraded context utilisation as the
    condition under which multi-agent wins, so if source documents genuinely exceed what one pass
    can hold, the split is justified on those grounds and should be defended on those grounds
    rather than on "two perspectives are better"; (b) 14b must receive the raw source rather than
    14a's compressed output, or the DPI argument applies with full force; (c) the ASSUMPTION /
    PRESUMPTION boundary must be crisp enough that neither duplication nor gaps appear in the
    register — checkable today; (d) the value sought must be taxonomic separation of output
    (defensible) rather than claimed accuracy improvement (not supported); (e) the extra token
    spend must be affordable, since the honest expectation is that it buys structure, not quality.
    How to test: Yes, and this is the highest-value unrun experiment in the C2A2 register.
    (1) Compute-matched ablation as in mitigation 1 — unified 14 at summed budget vs 14a+14b, both
    against a human-adjudicated gold set, scored on recall (did we catch it), precision (is it
    real), and duplication. (2) Context-window check: measure whether real source documents
    actually strain a single pass. If they do not, condition (a) fails and the split loses its
    best defence. (3) Register audit for near-duplicates across the two namespaces and for gap
    items — retrospective, no new runs needed. (4) Provenance ablation: re-run 14b on raw source
    vs on 14a's output and compare presumption yield; if raw-source yield is materially higher,
    the DPI penalty is real and measured in situ.

  Search scope: Queries actually run this cycle —
    - "multi-agent LLM systems do not outperform single agent compute-matched token budget
       baseline"
    - "'Why Do Multi-Agent LLM Systems Fail?' MAST taxonomy failure modes Cemri"
    - "role specialization LLM agents no benefit personas ablation coverage duplication context
       fragmentation 2026"
    - "assumption extraction implicit presumption detection pipeline single unified model versus
       split stages recall precision"
    - "joint model outperforms pipeline error propagation cascading errors information extraction
       survey"
    - "multi-agent LLM debate conformity herding groupthink same base model agreement not
       independent 2026" (shared with ASSUMPTION-008)
    Full abstract verified for arXiv:2604.02460 (incl. authorship) and arXiv:2605.00914v1.
    Gaps: no search for multi-agent results that FAVOUR splitting on extraction tasks specifically
    — that is 15a's direction, and my one-sided coverage should be read accordingly. No search on
    AssumptionMiner (arXiv:2607.22898, surfaced but not pursued) which may bear on assumption
    extraction directly and is worth a follow-up. Did not verify the enterprise/practitioner
    figures in source 6.

  Search confidence: comprehensive search (for the compute-matched and failure-taxonomy angles);
  preliminary for the specific task of assumption/presumption extraction, where I found analogues
  but no direct study — a targeted follow-up on AssumptionMiner and adjacent work is recommended.

  New since cycle 4 (i.e. since 2026-04-13):
    1. GENUINELY NEW AND DECISIVE: Kiela & Tran, arXiv:2604.02460. This is the compute-matched
       comparison the April file explicitly called for as "mitigation 1" and could not cite. It
       now exists, it is negative for the split, and it supplies a theoretical mechanism (DPI)
       rather than just an empirical result. The April file's central recommendation has in effect
       been carried out by someone else, and it came back against the presumption.
    2. arXiv:2605.00914v1 (May 2026) — token-cost multiple (2.1–3.4x) for equal or lower accuracy
       in homogeneous multi-agent structures, framed explicitly as process loss.
    3. arXiv:2603.18507v1 (March 2026) — persona/role specialisation damaging accuracy, attacking
       the split's underlying mechanism rather than its architecture.
    4. RECORD-INTEGRITY NOTE: several April citations on this item do not survive scrutiny in the
       form recorded. "Google AI (2026), 'Towards a Science of Scaling Agent Systems,'
       ArXiv:2512.08296" and "Decision Quality Research (Williams, 2012), 'Why Teams Don't Work'"
       are cited with specific figures (39-70% degradation; 100-500ms handoff latency) that I did
       not attempt to re-verify this cycle and that no source surfaced in these searches
       corroborates. The "Multi-Agent Systems Failure Study (2025)" citing 1,642 execution traces
       and 36.9% coordination failures is almost certainly a garbled reference to Cemri et al.
       arXiv:2503.13657 (1,600+ traces, ~37% coordination failures) — which is real, and is now
       cited properly above as source 2. Recommend the April figures be either re-verified or
       retired; the cycle-5 sources above are sufficient on their own and are individually
       verified.
    5. RECORD-INTEGRITY NOTE: cycles 1-3 on this item (2026-04-27, 2026-05-17, 2026-05-25) each
       recorded "no new challenging literature" with zero sources and no evidence of a search.
       arXiv:2604.02460 was available from early April and would have been the single most
       important hit for this item; it was missed by three consecutive automated cycles. That is
       direct evidence about the sensitivity of the automated re-check, and it bears on this very
       presumption: the pipeline's own division of labour did not surface the paper that most
       directly tests the pipeline's own division of labour.

  Recommendation: CHALLENGED
    Recommend escalation beyond MONITOR, with the extra weight that attaches to a PRESUMPTION:
    the designers never stated this belief, so it has never been argued for, and it now has
    compute-matched evidence against it. The decisive action is not further literature search —
    it is the four internal tests above, of which the register audit (near-duplicates and gaps
    across the ASSUMPTION/PRESUMPTION namespaces) requires no new runs at all and should be done
    first. If the split cannot be defended on context-window grounds after that audit, the honest
    reframing is that 14a/14b buys taxonomic structure rather than quality, and it should be
    documented as such — which would at least convert this from a presumption into a stated,
    arguable design decision.

---

SYSTEMIC-RISK-FLAG:
  Date: 2026-09-02
  Affected items: ASSUMPTION-008 (MONITOR-4) and PRESUMPTION-001 (MONITOR-6). ASSUMPTION-006
    (MONITOR-2) is affected only indirectly, via the third vulnerability below.

  Common vulnerability: Both items presume that ADDING AGENTS ADDS INDEPENDENT EPISTEMIC VALUE.
    ASSUMPTION-008 presumes it across a trio voting in parallel; PRESUMPTION-001 presumes it
    across a pair split in sequence. The 2026 literature converges on a single explanation that
    covers both: agents sharing a base model and scaffold share a common cause, so their outputs
    are not conditionally independent, and under a fixed compute budget a multi-agent arrangement
    cannot add information — it can only redistribute or lose it. Parallel replication buys
    correlated votes (Condorcet's independence premise fails; majority vote beats the best size-3
    member only 9.98% of the time). Sequential splitting buys lossy handoffs (Data Processing
    Inequality; single agents match or beat multi-agent at matched tokens). The same root defect
    presents as false corroboration in one case and as false division of labour in the other.
    C2A2 currently pays a token multiple for both.

    Two secondary common vulnerabilities, both of which affect all three items:
    (a) SILENT-NULL RE-CHECKS. All three items recorded "no new challenging literature" in cycles
    1, 2 and 3 with zero sources and no evidence that any search ran. This cycle found substantial
    material published in that exact window, including at least one paper (arXiv:2604.02460) that
    was the most important possible hit for its item and was available at the time. The re-check
    mechanism is producing confident nulls it has not earned, and those nulls are being read
    downstream as stability. Three null cycles are currently indistinguishable from three
    confirmations.
    (b) CITATION DECAY IN THE STANDING RECORD. Spot-checking the cycle-0 entries surfaced a
    citation on ASSUMPTION-006 ("West & Bergman 2010, Physical Review E 102(6), 062110") that I
    searched for and could not locate, with an internally inconsistent volume/year; a definitional
    drift on the same item (PRS recorded as "Problem-Response-State" in April versus
    "Problem–Representation–Solution" in the current tasking, which changes which objections
    apply); and on PRESUMPTION-001 a set of figures attributed to sources that appear to be
    garbled versions of Cemri et al. arXiv:2503.13657. The register may contain more of these.

  Literature basis:
    - arXiv:2607.20768 (Jul 2026) — size-3 majority vote beats best member in 9.98% of subsets;
      diversity metrics collinear with capability (rho +0.991).
    - arXiv:2604.02460, Kiela & Tran (Apr 2026) — DPI argument; single-agent matches or beats
      multi-agent at equal token budget across three model families; multi-agent gains traced to
      unaccounted compute.
    - arXiv:2605.00914v1 (May 2026) — homogeneous teams: sycophantic conformity to 85.5%,
      consensus collapse oracle gap to 32.3pp, 2.1-3.4x token cost, isolated self-correction
      superior. Covers both items at once.
    - arXiv:2608.11403v2 (Aug 2026) — majority vote reduces accuracy on 56.6-65.7% of hard
      problems; confidence gating fails as a repair.
    - Dietrich & Spiekermann, "The Premises of Condorcet's Jury Theorem Are Not Simultaneously
      Justified," Episteme; SEP "Jury Theorems" — conditioning on the true state does not restore
      independence under common causes.
    - Cemri et al., arXiv:2503.13657 — 41.8% of multi-agent failures are system-design issues
      including duplicate roles and poor decomposition.

  Risk level: HIGH — raised from the MODERATE recorded in April. Three reasons. First, the
    evidence is no longer analogical: 2026 work measures C2A2's own configurations (N=3
    same-model voting; compute-matched agent splitting) and finds against both. Second, the
    failures are silent — wrong majorities are held at high confidence, gap items are invisible by
    construction, and the confidence gate that would catch either is measured not to work. Third,
    it is reflexive. Agents 15a/15b/15c are themselves the configuration under challenge, so the
    machinery that would normally escalate this finding is the machinery the finding impugns. This
    file was written by one member of exactly such a trio; if 15c ratifies it 2-1, that ratification
    is subject to the same critique it ratifies.

  Recommendation:
    1. Do not resolve this by another literature cycle. The decisive experiments are internal and
       cheap. Compute C2A2's own oracle gap and co-failure rate from existing tripled-run history,
       and run the compute-matched unified-14 ablation. Both use methodologies published this year.
    2. Stop collapsing trios to a 2/3 verdict. Surface full vote distributions and both dissents.
       Consensus collapse — discarding a correct answer already present in the pool — is the
       measured failure, and not aggregating is the direct fix.
    3. Preserve and tighten 15a/15b isolation. The strongest 2026 result on homogeneous teams is
       that isolation beats peer exchange at a fraction of the cost. Any future proposal to let
       the agents confer would be moving in the empirically wrong direction.
    4. Introduce heterogeneity where affordable — different providers, or at minimum different
       scaffolds, framings and retrieval corpora across a trio. This is the one intervention shown
       to suppress the conformity transition.
    5. Fix the re-check mechanism before trusting any further nulls. Require that a cycle either
       list the queries actually run or be recorded as NOT RUN. Retire the cycle 1-3 nulls on
       these three items as non-evidence.
    6. Audit the standing register for citation decay and for near-duplicate / gap items across
       the ASSUMPTION and PRESUMPTION namespaces.
    7. Route this flag to a human. Given the reflexive structure, a 2/3 agent verdict on it is not
       an adequate disposition.
