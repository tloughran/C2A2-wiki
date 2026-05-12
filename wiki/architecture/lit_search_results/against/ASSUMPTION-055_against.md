SEARCH-AGAINST-ASSUMPTION-055:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-055
  Original statement: "git commit/push not possible from sandbox — the git repo path is outside the mounted sandbox filesystem."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-055
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run 2026-04-21 Phase 6
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Container runtime mount-propagation literature (Docker docs 2022-2025; OCI runtime spec): mount topology can be updated dynamically (shared, slave, private propagation) and bind-mounts can change at runtime. A static "repo path is outside the mount set" claim risks over-interpretation: the path may be unreachable today and reachable tomorrow depending on sandbox configuration.
    2. Confounding-failure literature (Nygard 2007 "Release It!"; postmortem patterns): diagnostic claims that attribute a failure to a single cause often miss compound causes. The 2026-04-16 `.git/index.lock` issue and the 2026-04-21 mount-topology issue may be symptoms of a shared upstream problem (sandbox-repo integration design) rather than two independent failures.
    3. Git alternatives / host-side commit patterns: literature on CI/CD and agent pipelines (GitHub Actions, CircleCI design patterns) shows that committing from inside the sandbox is itself an architectural choice — many mature systems deliberately perform git operations host-side via a scheduler primitive, not inside the agent sandbox. Framing the failure as "sandbox cannot reach repo" implicitly endorses "sandbox should reach repo" without challenge.
    4. Pre-flight invariant literature (SRE practice; Beyer et al. 2016 "Site Reliability Engineering"): diagnostic assumptions made without an invariant-check protocol have high false-diagnosis rates. Without a pre-flight mount-topology probe, the "repo is outside the mount set" claim is today's snapshot, not a run-over-run invariant.

  Strength of challenge: Moderate

  Summary: The diagnosis is technically correct for today's observation but it implicitly smuggles two further claims: (a) the topology is a stable condition, not a transient one; (b) committing-from-sandbox is the correct architectural stance. Both are contestable. The sandbox-repo integration choice itself is a design decision that has alternatives (host-side commit primitive) that the assumption does not consider. Without a pre-flight reachability probe, today's reading is a point-observation and cannot be treated as a persistent invariant.

  Specific risks: (a) If the topology is actually variable, fixing today's mount without an invariant-check leaves the silent-failure mode fully intact; (b) if the right architectural fix is host-side commit rather than extend-the-mount, then extending the mount treats the symptom and not the cause; (c) compounds with PRESUMPTION-061 (mount-topology stability presumed): both items need to be resolved jointly, not separately.

  Mitigations available: (a) Add a pre-flight reachability probe at scheduled-task start; (b) restructure Phase 6 to run host-side via a scheduler primitive (candidate OPEN-035); (c) pair the remediation with PRESUMPTION-061 mount-topology audit; (d) treat the 2026-04-16 `.git/index.lock` and today's mount-topology failure as potentially-compound symptoms of a shared upstream integration problem.

  Recommendation: PARTIALLY-CHALLENGED (diagnosis is technically sound; architectural framing smuggles contestable assumptions; remediation should pair with PRESUMPTION-061 and candidate OPEN-035)

  STEELMAN:
    Item: ASSUMPTION-055
    Strongest counterargument: The diagnostic claim is correct for today's snapshot but does not establish that the fix should be "extend the mount." Mature CI/CD and agent pipelines (GitHub Actions, CircleCI, many Airflow patterns) deliberately keep git operations host-side via a scheduler primitive precisely because sandboxes are ephemeral and mount topology can drift. Framing "sandbox cannot reach repo" as the problem implicitly commits to the architectural stance that it should — an unexamined design choice. The right remediation may be to move Phase 6 host-side (OPEN-035) rather than to expand the sandbox mount set.
    What would need to be true for C2A2 to be safe: Either (a) mount topology is genuinely stable and invariantly includes the repo path (which PRESUMPTION-061 challenges); or (b) git operations are restructured to run host-side where sandbox topology is irrelevant.
    How to test: Instrument a pre-flight mount-topology check across 30 days of scheduled-task runs; measure mount-set drift rate. If drift > 0, the invariant claim is empirically broken and host-side restructuring is preferred.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-04-21
    Affected items: ASSUMPTION-055 (this), PRESUMPTION-061 (mount topology stable), CACHING-ARCHITECTURE cluster (sandbox-repo integration), DECISION-018 (rescue commit)
    Common vulnerability: Sandbox-repo integration design has not been audited as an architectural choice; today's failure exposes the absence of both a reachability-invariant and a host-side fallback path.
    Literature basis: Docker/OCI mount-propagation; SRE pre-flight patterns; CI/CD host-side commit patterns
    Risk level: High (blocks Phase 6 on 2026-04-21; compounds with `.git/index.lock` from 2026-04-16; gates caching-architecture rollout 2026-04-27)
    Recommendation: Pair ASSUMPTION-055 remediation with PRESUMPTION-061 audit; introduce OPEN-035 host-side-restructure candidate; add pre-flight reachability probe as standard invariant for all scheduled tasks reaching host artifacts.
