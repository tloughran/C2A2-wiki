SEARCH-AGAINST-PRESUMPTION-061:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-061
  Original statement: "Sandbox filesystem mount topology is presumed stable across scheduled-task runs."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-061
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absence of pre-flight mount-topology checks across 2026-04 scheduled-task briefs
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Container runtime mutation literature (Docker mount propagation docs; OCI runtime spec sections on bind-mounts): mount topology CAN change across container lifecycles. Bind-mount propagation modes, overlay mount changes, and host-side volume reconfigurations are all documented variation sources. The literature treats mount topology as variable-under-many-conditions, not invariant.
    2. Ephemeral-infrastructure literature (Hightower et al. 2017 "Kubernetes Up & Running"; Netflix Chaos Engineering 2014+): modern cloud infrastructure assumes ephemeral configuration; persistence requires explicit state management. Presuming stability without verification is the 12-Factor App anti-pattern.
    3. Invariant-check failure literature (Beyer 2016 SRE; Nygard 2007): operational failures where a "presumed stable" dependency turned out to be variable are the canonical class of silent-failure incidents. Literature strongly endorses pre-flight invariant checks for any dependency outside the task's direct control.
    4. C2A2 empirical evidence: today's Phase 6 failure IS the counterexample. The topology that was presumed stable was not — or the mounted set never included the repo path in the first place and no prior run verified it. Either way, the presumption is empirically broken.
    5. "Infrastructure as code" literature (Morris 2016; Terraform/Pulumi docs): even explicitly-configured infrastructure drifts when configuration management is not in place. The presumption of stability without explicit configuration + verification is inconsistent with modern practice.
    6. SRE silent-failure literature (Google SRE book Ch. 6 "Monitoring"; internal C2A2 PRESUMPTION-013 precedent — infrastructure silent failures already documented): silent-failure modes are the dominant category of operational incidents. The presumption creates one.

  Strength of challenge: Strong

  Summary: The presumption is directly challenged by container-runtime documentation (mount topology can change), ephemeral-infrastructure norms (stability requires explicit state management), and empirical evidence (today's Phase 6 failure IS the counterexample). Literature strongly endorses pre-flight invariant checks for dependencies outside a task's direct control. The silent-failure category this presumption enables is the dominant category of operational incidents. The 12-Factor App and Infrastructure-as-Code literatures are unambiguous on this point: stability requires explicit configuration + verification, not presumption.

  Specific risks: (a) Every scheduled task reaching through the sandbox to a host-side artifact carries this presumption; today's failure cost Phase 6 but tomorrow's could cost caching-architecture rollout (2026-04-27) or specialist-slot writes; (b) the silent-failure mode is symmetric across all such tasks — a single infrastructure change could take out multiple pipelines simultaneously; (c) compounds with ASSUMPTION-055 (sandbox-unreachable-repo diagnosis) as a paired architectural concern.

  Mitigations available: (a) Add a pre-flight mount-topology check at the start of every scheduled task reaching host-side artifacts (cheap, standard SRE pattern); (b) treat mount topology as a first-class infrastructure contract declared and verified at task start; (c) restructure Phase 6 and similar tasks to run host-side where mount topology is irrelevant (candidate OPEN-035); (d) pair remediation with ASSUMPTION-055 — they are two sides of the same integration problem.

  Recommendation: CHALLENGED (strong; container-runtime docs, 12-Factor norms, and empirical evidence all contradict the presumption; silent-failure category is dominant operational incident class; cheap standard mitigation available)

  STEELMAN:
    Item: PRESUMPTION-061
    Strongest counterargument: The presumption sits in the invisible category of "infrastructure-as-given" — the kind of assumption designers don't write down because it feels like plumbing. But every modern infrastructure practice (12-Factor, Infrastructure-as-Code, Chaos Engineering, SRE) explicitly rejects this stance. Ephemeral infrastructure requires explicit state management; stability without verification is the anti-pattern that produced today's Phase 6 failure. The failure mode is symmetric — any task reaching host-side carries the same presumption, so a single infrastructure change could simultaneously fail multiple pipelines. The mitigation (pre-flight mount-topology check) is cheap, standard, and maps directly to documented practice.
    What would need to be true for C2A2 to be safe: Pre-flight mount-topology probe as standard invariant for all scheduled tasks reaching host-side artifacts; or restructure host-side-reaching tasks to run host-side via scheduler primitive.
    How to test: Instrument mount-topology probe at scheduled-task start across 30 days; measure drift rate. If drift > 0, the presumption is empirically broken and pre-flight verification is mandatory. If drift = 0 across 30 days, the presumption is defensible only for the observed configuration window — still not generalizable.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-04-21
    Affected items: PRESUMPTION-061 (this), ASSUMPTION-055 (sandbox-unreachable-repo), CACHING-ARCHITECTURE cluster (2026-04-27 rollout), DECISION-018 (rescue commit)
    Common vulnerability: Sandbox-to-host integration has no invariant-check protocol; silent-failure mode is symmetric across all tasks reaching host-side artifacts.
    Literature basis: Container runtime mount-propagation; 12-Factor App; Chaos Engineering; SRE silent-failure; Infrastructure-as-Code.
    Risk level: High (BLOCKS Phase 6 on 2026-04-21; gates caching rollout on 2026-04-27; symmetric risk across all host-side-reaching tasks)
    Recommendation: Pair remediation with ASSUMPTION-055; introduce pre-flight mount-topology probe as standard scheduled-task invariant; consider OPEN-035 host-side-restructure for Phase 6.
