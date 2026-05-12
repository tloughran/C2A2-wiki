SEARCH-FOR-ASSUMPTION-055:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-055
  Original statement: "git commit/push not possible from sandbox — the git repo path is outside the mounted sandbox filesystem."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-055
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run 2026-04-21 Phase 6 — explicit statement that sandbox mount topology excludes the repo path
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Docker/OCI runtime spec (2022-2025) and container mount semantics: sandbox filesystem views are explicitly scoped by bind-mounts configured at container creation. Paths outside declared mounts are by specification not visible inside the sandbox.
    2. Anthropic MCP sandbox documentation (2024-2025) and Claude Code sandbox references: sandboxed tool execution runs in a filesystem namespace with a finite mount set; host paths not explicitly mounted are not accessible.
    3. Kubernetes pod spec / gVisor documentation: sandboxed runtimes enforce mount-time declared topology; runtime-side discovery of "unreachable host path" is a standard failure mode, not an exotic one.
    4. Git operational literature (Scott Chacon, "Pro Git" 2014; git-scm documentation): git operations require filesystem access to the `.git` directory and working tree; without that access, commit/push cannot proceed regardless of the presence of valid changes.

  Strength of support: Strong

  Summary: The diagnostic claim — that Phase 6's git operation fails because the repo path is outside the sandbox mount set — is directly supported by the standard semantics of containerized/sandboxed runtimes. Mount topology is authoritatively declared at sandbox creation time; paths outside the declared mounts are structurally unreachable, not merely permission-denied. This is the expected behavior under Docker/OCI/gVisor/MCP sandbox specifications. Git's own design requires filesystem access to the working tree, so an unreachable path produces exactly the observed failure mode.

  Caveats: The assumption diagnoses the failure mode correctly but does not prescribe a remedy. Supporting literature identifies at least three standard mitigations (extend mount set at sandbox creation; move git operation host-side via a scheduler primitive; introduce a reachability pre-flight check) but does not rank them. The CACHING-ARCHITECTURE rollout gate and the `.git/index.lock` 2026-04-16 issue are independent concerns the sandbox-mount topology claim does not address.

  Recommendation: SUPPORTED (strong technical support; diagnostic claim is correct by standard sandbox-runtime specifications; remedy selection is out-of-scope for this claim)
