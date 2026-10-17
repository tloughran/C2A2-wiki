SEARCH-FOR-PRESUMPTION-1100 (RE-TRIGGER — 15d, MONITOR-635, cycle 1; Medium):
  Date searched: 2026-10-17
  Original item: PRESUMPTION-1100
  Original statement: [inferred] Status records that conflate attempt outcome with system state produce
    misleading health signals.
  Owed (per 15d block): case or literature on attempt-vs-state conflation producing misleading status (e.g.,
    Kubernetes conditions vs events, desired/observed state, alert design).
  Cycle: 1 (RE-TRIGGER by 15d; processed 2026-10-17)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-1100
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 2026-09-30 sessions.
      15a (cycle 0, 2026-10-01): PARTIALLY-SUPPORTED (Weak-Moderate). Fowler 2005 event narrative [fetched];
        SRE book ch. 6 [fetched]; Overeem et al. 2021 [snippet]. Support by analogy only.
      15b (cycle 0): independent; not read by this agent.
      15c: -> MONITOR-635 (Medium)
      15d: re-triggered without evaluating evidence; owed = case/literature on the conflation itself.
      15a (cycle 1, 2026-10-17): 2 web searches; 1 fetch (arXiv 2509.14347: abstract and selected body
        passages read; ~100 KB page, not read end to end).
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: (a) Kubernetes status/conditions conventions (spec vs status, observedGeneration);
    (b) CI job "success" status vs actual outcome (silent failures; status badges).

  Supporting evidence found: Partial — one empirical study plus established design conventions.

  Sources:
    1. Aïdasso, H., Bordeleau, F. & Tizghadam, A., 2025. "On the Illusion of Success: An Empirical Study of
       Build Reruns and Silent Failures in Industrial CI." arXiv:2509.14347v1. [abstract read in full + selected
       body passages; preprint — peer-review status not verified]
       Findings:
       - 142,387 jobs, 81 industrial projects (TELUS); replication on 8 open-source projects (198,146 jobs)
         and 92 public silent-failure issues.
       - 11% of SUCCESSFUL jobs are rerun; these are 51% of all no-code-change reruns (more than reruns of
         failed jobs, 44%); >35% occur after 24 hours; they consume ~48% of all rerun server time.
       - A job can "signal a success after its execution (exit code 0 and green check mark), but in reality
         fails—at least partially—to carry out its intended tasks"; example: a GitLab Runner cache upload
         failure with no error in the logs.
       - Silent failures are "difficult (if not impossible) to identify ... only based on logs".
       Relevance: direct empirical evidence that an attempt-outcome signal (job exit status) is a misleading
       proxy for the state it is meant to establish (artifact built, cache uploaded, deployment correct), and
       that the misleading signal has measurable cost. This is the owed "case" for the conflation.
    2. Kubernetes conventions: KEP-1623 "Standardize Conditions" (kubernetes.dev); Gateway API
       "Troubleshooting and Status" docs; OpenShift API reference. [snippet]
       - spec = desired state; status = most recently OBSERVED state.
       - Conditions answer continuous state questions (Ready, Progressing, Degraded), "not log every event or
         reconcile step"; lastTransitionTime changes only when the value changes.
       - observedGeneration on each condition lets a reader detect that a status describes an older spec
         (staleness test).
       - Events are best-effort and may expire; they are not the authoritative state record [background
         knowledge — UNVERIFIED this cycle; Kubernetes api-conventions.md not fetched].
       Relevance: a major production system deliberately separates attempt/event records from state
       conditions and carries a staleness marker — design-level support that conflation is a known hazard.
    3. CI status-badge reports: GitHub Community threads ("Failing badge status for passing runs"; "Status
       badge stuck on passing"); CircleCI Discuss ("Badge is green even if some builds in the workflow
       failed"). [snippet]
       - A badge went red because the most recent ATTEMPT was cancelled, though the code was healthy.
       - GitHub staff: "Passing" generally means the check executed successfully.
       - CircleCI: badge shows only the last completed workflow.
       Relevance: practitioner cases where a last-attempt signal was read as system state, misleading in
       both directions (false red and false green).

  Strength of support: Moderate. Up from Weak-Moderate in cycle 0, because source 1 is an empirical study of
    the failure mode itself rather than an analogy.

  Summary: An industrial CI study finds that "success" status, meaning the attempt exited 0, often does not
    reflect whether the intended state was achieved. Developers rerun 11% of successful jobs, often days
    later, and these reruns consume about half of rerun compute. Kubernetes encodes the opposite discipline:
    observed state is kept in conditions separate from events, with an observedGeneration staleness marker.
    Badge cases show last-attempt status misleading in both directions. Together these support the
    presumption that conflating attempt outcome with system state yields misleading health signals.

  Owed condition: LARGELY met. Empirical case found (source 1); Kubernetes desired/observed and
    conditions-vs-events design found (source 2, snippet level). Not found: a study quantifying misleading
    signals in a monitoring dashboard specifically (as opposed to CI).

  Caveats:
    - Source 1 infers silent failure from reruns of successful jobs. Some reruns may have other causes, such
      as flakiness checks or redeploys, so 11% is an upper-bound proxy.
    - Source 1 is a preprint; peer-review status not checked.
    - Kubernetes sources were read at snippet level; the authoritative api-conventions.md was not read.
    - CI is not the same as C2A2's scheduled agent runs; transfer is by close analogy (both are scheduled
      job runs with exit-status records).

  Recommendation: PARTIALLY-SUPPORTED (Moderate). Close to SUPPORTED, pending a primary read of the
    Kubernetes conventions.
