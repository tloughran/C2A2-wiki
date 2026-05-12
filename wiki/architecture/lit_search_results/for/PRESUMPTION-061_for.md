SEARCH-FOR-PRESUMPTION-061:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-061
  Original statement: "Sandbox filesystem mount topology is presumed stable across scheduled-task runs."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-061
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from wiki daily run 2026-04-21 mount-topology gap as newly-surfaced failure
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Container orchestration best-practices (Kubernetes docs 2022-2025; Docker Compose documentation): mount declarations in well-configured container setups are designed to be stable across container restarts when configured with explicit volume mounts. Stability is achievable under deliberate configuration.
    2. Reproducibility literature (Peng 2011 "Reproducible Research in Computational Science"): stable infrastructure is a prerequisite for reproducibility. The presumption is consistent with reproducibility norms.

  Strength of support: Weak

  Summary: The presumption (mount topology stable across runs) is not directly supported by literature — it is an invisible operational assumption. The closest supportive literature addresses what stability SHOULD look like under deliberate configuration, but this is a normative claim about desired state, not an empirical claim about the C2A2 sandbox topology's actual stability. No literature endorses treating sandbox mount topology as invariant without a verification check. In fact, the supportive literature cited here IS conditional on deliberate configuration, which today's Phase 6 failure suggests was not in place. Literature on stability is most consistent with "stability if configured, verified with a probe" — not with "presumed stable without check."

  Caveats: (a) The presumption was invisible until it failed; supportive literature cannot ground a claim that has not been audited; (b) all supportive literature conditions stability on explicit configuration + verification; the presumption as stated has neither.

  Recommendation: NO-SUPPORT-FOUND (no literature supports treating mount topology as invariant without a verification mechanism; conditional support exists for "stable-if-configured-and-checked," which differs from the presumption as stated)
