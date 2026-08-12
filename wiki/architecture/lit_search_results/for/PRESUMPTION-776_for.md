SEARCH-FOR-PRESUMPTION-776:
  Date searched: 2026-08-12
  Original item: PRESUMPTION-776
  Original statement: [inferred] That an unwritable git is a deferral rather than a data-loss exposure — 191 uncommitted paths in ephemeral compute, and the yield metric reads git as ground truth.

  Claim as tested here (polarity note): two propositions are bundled. (P1) Uncommitted work held in ephemeral compute is an active data-loss exposure, not a scheduling deferral. (P2) A yield metric that reads git as ground truth, while the producers of the measured work cannot write git, is measuring durability rather than production. Both are the CORRECTIVE converse of the presumption; support below counts against it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-776
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a count (191 uncommitted paths), a substrate fact (ephemeral compute), and a measurement-system fact (the yield metric's ground truth is git). Risk graded Critical. The three facts are high-confidence; the presumption attributed — that this is read as deferral — is an inference from the absence of escalation.
      15a: Searched for supporting literature on both corrective propositions
    Current status: PARTIALLY-SUPPORTED (P1 well supported; P2 supported only by analogy from audit and measurement theory)

  Supporting evidence found: Yes for P1; Partial for P2

  Sources (P1 — ephemeral compute as durability boundary):
    1. Ephemeral storage semantics, converging practitioner and vendor documentation (MongoDB, "What is Ephemeral Storage in Kubernetes?"; ITU Online; simplyblock, "Persistent Storage"; appsecuritystandards.org, "Ephemeral Workloads"). — The definitional point, stated without qualification: "everything on ephemeral storage can disappear during a stop, reboot, instance replacement, cluster upgrade, autoscaling event, or host maintenance window," and "the value is speed and convenience; the tradeoff is that you do not get durability." Best practice as stated: "place only scratch files, caches, or rebuildable artefacts on the temporary volume." 191 uncommitted paths of generated wiki content are not rebuildable artefacts. [unverified — from search snippets; vendor/standards-body documentation, authoritative as practice]
    2. Northflank, 2026. "Ephemeral execution environments for AI agents in 2026." — Directly addresses C2A2's system class and states the required architecture: "the execution environment can be ephemeral, but agent memory, working data, and execution history are written to external storage (volumes, object storage, or a database) that persists independently of the environment." This is the closest thing found to a design rule for the exact configuration at issue. [unverified — from search snippet; vendor blog]
    3. US Patent 12,367,105, "Reducing potential data-loss scenarios when using ephemeral storage as backing storage for journaling by a virtual storage system." — Independent commercial recognition that journaling to ephemeral storage is a data-loss scenario requiring engineered mitigation (flush to persistent storage on imminent-shutdown signal). A patent is weak evidence of efficacy but decent evidence that the risk is regarded as real and non-trivial by practitioners who invested in solving it. [unverified — from search snippet]
    4. Single point of failure, standard reliability concept. — "Whenever you have the entire history of the project in a single place, you risk losing everything." Uncommitted work in a single ephemeral container is unreplicated by construction; git's distributed-replica property, which is the usual reason to trust git, is exactly the property that uncommitted paths do not have. [canonical concept; the git-specific framings surfaced this session are grey literature and unverified]

  Sources (P2 — producers who cannot write the measured store):
    5. Audit evidence hierarchy, ISA 500 / standard audit doctrine (as summarised in the practitioner material surfaced this session). — The relevant principle inverted: audit doctrine ranks evidence by independence from the party being measured. Here the *measurement* is independent of the producer in the wrong direction — the yield metric can only see work that crossed a boundary the producer cannot cross. The metric is therefore not measuring the producer's output; it is measuring the conjunction of output and a commit event outside the producer's control. [unverified — from search snippets; the underlying independence principle is canonical]
    6. Little's Law (Little, J.D.C., 1961, Operations Research 9(3)) and standard WIP accounting. — Theoretical grounding for reading the 191 paths correctly: they are work-in-progress. A throughput metric that counts only completions while WIP grows unboundedly reports a stable or falling rate during precisely the period when the system is accumulating the most unrealised work. The metric is not merely incomplete, it is anti-correlated with the risk. [canonical; cited from domain knowledge]

  Strength of support: Strong for P1; Weak-to-Moderate for P2

  Summary: P1 is settled by definition and by uniform practitioner guidance: ephemeral storage offers no durability, only rebuildable artefacts belong there, and agent working data belongs in external persistent storage. On that reading 191 uncommitted paths in ephemeral compute is not a deferral in any sense the literature recognises — it is unreplicated work-in-progress one host event away from loss, and the fact that the substrate is git makes it worse rather than better, because git's usual durability argument rests on replication that uncommitted paths do not enjoy. P2 is a subtler claim and I found no literature addressing it directly. The nearest support is structural: audit doctrine's independence principle and basic WIP accounting both imply that a completion-counting metric whose completion event lies outside the producer's control measures the boundary, not the production — and will under-report exactly when WIP is accumulating fastest. That is an argument, not a finding.

  Caveats: (a) All P1 sources are vendor or standards-body documentation rather than peer-reviewed measurement; none quantifies loss probability per unit time for a given substrate, so the *magnitude* of the exposure is not established here, only its existence. (b) P1's force depends on a fact this search cannot check: whether the ephemeral compute in question has any snapshot, volume-mount or sync path that partially mitigates. If a mounted persistent volume holds the same paths, the exposure is much smaller than 14b's framing implies. (c) P2 is supported only by analogy, and the analogy has a weak point: a yield metric that reads git may be *intentionally* measuring durable yield, in which case it is correct and the defect is that nothing else measures undurable production. The literature cannot adjudicate which was intended. (d) Publication bias favours P1 strongly — persistence vendors write most of this material.

  Search scope: Comprehensive on ephemeral-storage durability semantics. Moderate on agent-specific persistence architecture (one directly relevant 2026 vendor source). Preliminary and, I judge, exhausted on P2 — see the novelty flag below.

  NOVELTY-FLAG:
    Item: PRESUMPTION-776 (second half only, P2)
    Searched: measurement systems whose producers cannot write the measured store; construct validity of throughput metrics under a durability boundary; audit independence applied to self-measuring pipelines; WIP-versus-throughput reporting under unbounded queue growth
    Finding: No existing literature addresses this specific claim. There is abundant work on ephemeral-storage durability (P1) and abundant work on metric gaming and construct validity in general, but I found nothing on the specific structure where a pipeline's yield metric reads a store the pipeline's own producers lack write access to — so that the metric silently reports on the commit channel rather than on production, and degrades precisely when work-in-progress accumulates.
    Implication: potential original contribution — a named failure mode ("the metric measures the boundary, not the work") for autonomous pipelines whose measurement substrate sits outside their write scope. This is a general defect of self-measuring agent systems and is worth stating as such, not just fixing locally.
    Recommended status: NOVEL (for P2; P1 remains SUPPORTED)

  Recommendation: PARTIALLY-SUPPORTED (P1 SUPPORTED — the exposure is real and the practice guidance is unambiguous; P2 NO-SUPPORT-FOUND with a novelty flag raised)
