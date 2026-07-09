SEARCH-AGAINST-PRESUMPTION-449:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-449
  Original statement: "[inferred] The set of possible repo writers is fully enumerable from the local process table."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-449
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the lock-deletion decision (justified by inspecting local processes) that the writer set was presumed enumerable via the local process table
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. anthropics/claude-code Issue #47241, "macOS: session-snapshot hook fossilises iCloud FileProvider corruption when repo is under ~/Documents." — Directly documents a hidden writer on macOS: with iCloud "Desktop & Documents Folders" sync enabled, fileproviderd silently reverts filesystem operations seconds after they complete; the repo appears consistent to the operating process while a system daemon rewrites it. Highly relevant because the C2A2 vault lives under ~/Documents.
    2. Chandra, A., "A Side Effect of Storing a Git Repository in iCloud Drive." — Documented case of the iCloud sync daemon seizing .git/index.lock within seconds of git init and propagating intermediate file states; the writer is a system service most users would not identify as a "repo writer" in a process check.
    3. "Why iCloud Fails: The Category Mistake of Cloud Synchronization" (arXiv 2602.19433, 2026). — Analyzes cloud-sync daemons as concurrent writers with non-transactional semantics; silent filename swapping and state reconciliation occur after local operations report success, defeating any point-in-time process-table check.
    4. Mahmoud, S. et al., "Dealing with observability in interaction-based Offline Runtime Verification of Distributed Systems" (arXiv 2212.09324). — Formalizes that in distributed systems some subsystems cannot be instrumented/observed; correctness judgments must account for unobservable actors rather than assume complete enumeration.
    5. Emergent Mind, "Partial Process Observability" (survey). — Partial observability is the default condition of real systems; sound decision procedures maintain belief states over unobserved actors instead of assuming the observed set is complete.
    6. Practitioner corpus on git corruption via NFS/CIFS/Dropbox/OneDrive (dev.to, josh.fail). — Multiple sync services are "notorious" for corrupting repos; none of these writers appear as git processes in a local process table.

  Strength of challenge: Strong

  Summary: The presumption fails on both theory and documented practice. Theoretically, partial observability is the standard condition of distributed systems: the writer set for a repo includes remote pushers to the shared remote, cron/scheduled jobs on other hosts, and — critically — local system daemons whose activity does not present as a git process. Practically, the strongest evidence is exactly on point for C2A2's configuration: the vault sits under ~/Documents on macOS, where iCloud's fileproviderd is a documented hidden writer that seizes index.lock, reverts completed operations, and propagates intermediate states — including a Claude Code issue describing corruption of repos under ~/Documents. A local process-table check at time T also suffers the TOCTOU problem: even a correctly enumerated writer set is stale the moment it is used (see PRESUMPTION-448). The process table answers "what git processes are running here now," which is a strictly narrower question than "who can write to this repo."

  Specific risks: A lock or file conflict attributed to "no live writer, safe to delete" when a sync daemon or remote actor holds effective write interest; iCloud/FileProvider silently reverting or swapping files in the vault after agents believe writes succeeded, corrupting both the artifact and the evidence chain; non-fast-forward rejections misdiagnosed because the conflicting writer (remote scheduled agent, another machine) was never in the local candidate set; recurrence of the lock-deletion-under-uncertainty incident with worse luck.

  Mitigations available: Verify whether iCloud Desktop & Documents sync is enabled and, if so, relocate the repo outside ~/Documents (the documented standard remedy) or exclude it via .nosync; treat the writer set as open — decide lock staleness by lock age plus recorded owner metadata, not by process-table absence; enumerate known writer categories explicitly in the architecture doc (attended session, scheduled agents, remote pushers, sync daemons, editors with git integration) and add detection for each; use the remote as the serialization point (branch-per-writer, protected main) so hidden local writers cannot silently win races.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-449
  Strongest counterargument: The local process table is an answer to the wrong question. It enumerates currently running local git processes, but the repo's effective writer set includes actors that are temporally hidden (a scheduled agent that will start in ten seconds), spatially hidden (a push from another host to the shared remote), and categorically hidden (macOS fileproviderd, which is a system daemon, not a git process, yet documentedly seizes git locks and reverts completed writes for repos under ~/Documents — where this vault lives). Since the lock-deletion decision in the incident was justified by local-process inspection, the decision procedure was unsound even if its outcome was lucky; distributed-systems literature holds that under partial observability, safe procedures must be robust to unenumerated actors, not conditioned on their absence.
  What would need to be true for C2A2 to be safe: iCloud/Documents sync verifiably disabled for the vault path (or repo relocated); all coordination decisions (lock staleness, push conflicts) made by mechanisms robust to unknown writers (age/ownership metadata, remote-side serialization) rather than by local enumeration.
  How to test: Check `defaults read` / System Settings for Desktop & Documents iCloud sync and for fileproviderd activity on the vault path (log stream --predicate on the repo directory during a write burst); create a canary file in the repo and watch for unexplained modification; enumerate writers in the architecture doc and have a red-team agent list writers not on it.
