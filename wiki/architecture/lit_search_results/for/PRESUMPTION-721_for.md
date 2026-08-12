SEARCH-FOR-PRESUMPTION-721:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-721
  Original statement: That a blocker named on one day is the same blocker the next; two ceilings declared hard on 08-06 (3.3 GB disk, 45-second wall) both cleared today by an unlogged TMPDIR change, with no representation in the system for "currently not biting" as distinct from "repaired".

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-721
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading today's two successes against 08-06's impossibility claims for the same operations
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. IBM, "What is Configuration Drift? Tools, Causes & Risks"; Octopus Deploy, "Configuration Drift: Causes, Examples, Risks, And Best Practices"; Coder, "What is configuration drift?" — [unverified — from search snippet] define configuration drift as gradual, often manual and undocumented deviation from a baseline environment state, explicitly note that "root causes of issues might stem from undocumented changes, complicating troubleshooting," and recommend GitOps-style change tracking (all changes require a logged, auditable pull request) specifically to prevent silent environment changes from invalidating prior diagnoses. This directly supports the structural claim that an unlogged TMPDIR change can silently alter whether a previously "hard" blocker still applies, and that the standard remediation is auditable change-tracking, not re-declaring the blocker resolved.
    2. Software defect life-cycle literature (Guru99, "Defect/Bug Life Cycle in Software Testing"; GeeksforGeeks, "Different Defect States available in Defect Life Cycle"; Qodo, "What is Latent Defect? Causes & Prevention") — [unverified — from search snippet] documents that mainstream defect-tracking practice already distinguishes several intermediate states beyond simple open/closed — including "Not Reproducible" (cannot currently be triggered by the documented steps) and "Reopened" (a previously closed defect resurfaces) — precisely the missing state PRESUMPTION-721 identifies ("currently not biting" vs. "repaired"). This shows established practice elsewhere already has a name and process for this distinction, supporting both the diagnosis and that a fix (a formal intermediate state) is a recognized, implementable pattern.
    3. Devzery, "Solving Heisenbugs: Tackling Elusive Parallel Bugs"; Ministry of Testing, "Heisenbugs: Handling software defects you can't reproduce" — [unverified — from search snippet] describes the general phenomenon of environment-sensitive failures that appear or disappear under small, often incidental environmental changes (e.g., added instrumentation, altered timing) without the underlying defect being fixed — "environment changes can occur spontaneously, and cause problems when system designers have failed to consider the possibility of their occurrence" — directly analogous to a TMPDIR change incidentally clearing disk/wall-time ceilings without the underlying capacity constraint being addressed.

  Strength of support: Moderate

  Summary: The literature gives solid, if analogical, support for both halves of the presumption: (a) that undocumented environment changes (configuration drift) commonly and silently alter whether a previously identified blocker still holds, and (b) that mainstream defect-tracking practice already has, and needs, an explicit intermediate state ("not currently reproducing" / "not currently biting") distinct from "resolved," precisely because conflating the two is a known and named failure pattern. The Heisenbug literature further supports the causal mechanism — that incidental environment changes can mask rather than fix an underlying constraint.

  Caveats: These bodies of literature (DevOps configuration-drift practice, software defect-tracking conventions, and Heisenbug/intermittent-failure research) are general software engineering literature, not specific to LLM agent pipelines, disk-quota or wall-clock resource ceilings, or C2A2's architecture. The mapping from "unreproducible bug" states to "hard resource ceiling that cleared incidentally" is a reasonable structural analogy but not a literal precedent — resource ceilings (disk, wall-time) are qualitatively different from logic-level intermittent defects, and none of the retrieved sources address resource-constraint tracking specifically. No source was found addressing multi-agent or LLM-pipeline-specific instances of this exact pattern.

  Recommendation: PARTIALLY-SUPPORTED
