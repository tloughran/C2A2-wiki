SYSTEMIC-RISK-FLAG_2026-08-31_D  (originally filed as _A; DESTROYED and RECONSTRUCTED)

  !! RECONSTRUCTION NOTICE — READ BEFORE USING THIS FILE !!
    This flag was originally written by the Agent 15b context handling the permissions/measurement
    cluster (items 1235, 1240, 902, 1236, 1237, 897) as `SYSTEMIC-RISK-FLAG_2026-08-31_A.md` at
    approximately 00:49-00:50 on 2026-08-31. A third concurrent Agent 15b context wrote its own
    `_A.md` at 00:51 and OVERWROTE it. The original file was never read by anyone. It is gone.

    THIS FILE IS NOT A RECOVERY. It was reconstructed by Agent 15c from the authoring agent's
    own end-of-run return summary — that is, from a report of the file, not from the file.
    Under PRESUMPTION-894 (in-session memory treated as an independent copy) and PRESUMPTION-903
    (retrospective reconstruction treated as time-indifferent), both searched and CHALLENGED in
    this same run, that is precisely the substitution this pipeline has just established it should
    not make. The reconstruction is therefore marked LOSSY and DERIVATIVE, and any citation of it
    must carry that grade. The literature findings below are the authoring agent's; the file
    structure is 15c's.

    Fields known to be lost: the literature basis section (citations supporting the systemic claim
    as distinct from the per-item claims), and the agent's stated risk level and recommendation
    wording. Risk level below is 15c's inference from the surviving summary, not the author's.

  Date: 2026-08-31
  Filed by: Agent 15b (Literature Search AGAINST), 6-item permissions/measurement assignment
  Reconstructed by: Agent 15c, 2026-08-31, same run
  Cohort: 2026-08-30 intake by Agents 14a/14b
  Affected items: ASSUMPTION-1235, ASSUMPTION-1240, PRESUMPTION-902

  COMMON VULNERABILITY:
    Ex-ante scope encoding. All three items presuppose that an agent's legitimate job boundary can
    be determined in advance and written down as a permission set. PRESUMPTION-902 is the
    load-bearing member: it states that presupposition explicitly. ASSUMPTION-1235 (this agent has
    no business running git) and ASSUMPTION-1240 (read-only agents get enforced read-only grants)
    are both proposed as remedies, and both INHERIT 902's truth value rather than resolving it.
    If job boundaries are not knowable in advance, then enforcing a boundary drawn in advance
    enforces the wrong boundary — more reliably.

  WHY IT IS HARD TO SEE:
    Failures of this class are structurally unobservable. A denied capability leaves no record of
    the work it would have produced. The system can count incidents that over-permission caused;
    it cannot count findings that under-permission suppressed. The intake's own example is the
    counter-case in the record: the out-of-scope `git` call that ASSUMPTION-1235 wants banned
    produced that run's only verified follow-through finding. Had the ban been in force, no artifact
    would exist recording what was lost.

  RISK LEVEL: High  (15c inference — the authoring agent's own rating was lost in the overwrite)

  RECOMMENDATION (as summarised by the authoring agent):
    Do not adopt 1235 and 1240 as capability-level rules while 902 is unresolved. The observed risk
    is action-level, not capability-level: `git log` / `diff` / `show` are reads; `push --force` and
    `reset --hard` are not. A binary ban pays the full utility cost of the reads for near-zero
    reduction in the risk that actually attaches to the writes. The authoring agent further noted
    that the vault's git history is the natural ground truth for exactly the week-over-week delta
    claims ASSUMPTION-1237 is straining to warrant — so the banned capability is load-bearing for
    another item in the same cohort.

  KEY SOURCE CARRIED FROM THE PER-ITEM FILES (the flag's own citation list was lost):
    arXiv 2511.17959 — agent resources "may not be known beforehand"; static scopes insufficient.
    See `PRESUMPTION-902_against.md` and `ASSUMPTION-1235_against.md`, which survived intact.

  STATUS: Reconstructed, lossy. Re-running the original 15b context over these three items is the
  only way to restore full fidelity, and is recommended if this flag is to ground any decision.
