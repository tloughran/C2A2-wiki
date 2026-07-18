SEARCH-AGAINST-PRESUMPTION-469:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-469
  Original statement: "Task-file drift is benign because each run's agent will re-derive the repair — noted fixes in run outputs reach no future run and no file owner."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-469
    Item type: PRESUMPTION (unstated — surfaced by inference, QUEUED-EMPIRICAL)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Fowler, M. "SnowflakeServer" and Morris, K. "ImmutableServer" (martinfowler.com bliki); Thoughtworks, "Moving to the Phoenix Server Pattern." — Canonical statement that ad-hoc, unpersisted fixes produce configuration drift that compounds: each unrecorded repair widens the gap between the artifact's assumed and actual state until repairs themselves become unreliable. "If you have to log in to fix something, you've already lost the battle against drift."]
    2. [Beyer, B., et al., 2016. "Site Reliability Engineering," Ch. 5 "Eliminating Toil," Google/O'Reilly. — Repeated manual remediation is toil: it scales linearly with runs, yields no enduring improvement, and is explicitly identified as a failure of engineering discipline; the recommended response is to persist the fix, not re-derive it.]
    3. [Google SRE Workbook, "Postmortem Culture" (sre.google/workbook/postmortem-culture) and industry postmortem-completion data (e.g., Ozcay, 2025, "Your Incident Postmortem Process Is Probably Making Your Team Worse," Stackademic). — Documented pattern: findings that don't convert into owned, tracked action items don't get done (fewer than 40% of postmortem action items completed within 90 days; repeat-incident rates of 35-50%). "Noted in run outputs, reaching no owner" is the same anti-pattern with a 0% conversion rate by construction.]
    4. [DigitalOcean, "Configuration Drift: Phoenix Server vs Snowflake Server"; O'Reilly, "An Introduction to Immutable Infrastructure." — Drift's cost curve is nonlinear: divergence accumulates silently until a repair fails or interacts destructively, at which point recovery requires archaeology rather than routine maintenance.]
  Strength of challenge: Strong
  Summary: The presumption survives only while three fragile conditions hold: every future agent re-derives the same fix, the drift stays small enough to be re-derivable, and re-derivation is cheap. The configuration-drift literature says all three decay: unpersisted fixes compound, and each run starts from a worse baseline. The SRE toil framework classifies per-run re-derivation as pure toil — O(n) cost with zero enduring value — and LLM-agent re-derivation adds a failure mode the classic literature didn't have: nondeterminism. Different runs may derive *different* repairs, so the task file's effective semantics vary run to run. The postmortem literature supplies the organizational half of the challenge: even when fixes are noted, notes without an owner and a tracked queue demonstrably do not become changes (sub-40% completion even for tracked items; these aren't tracked at all). "Benign" here means "invisible until compounded."
  Specific risks: Repair cost grows each run until an agent fails to re-derive and the task silently degrades or fails; divergent re-derivations make runs non-reproducible and debugging archaeology-grade; fix knowledge is written into run outputs that no process reads — institutional memory exists but is unreachable; a future task-file edit interacts with unrecorded assumptions and breaks tasks that "always worked."
  Mitigations available: A drift-harvest step: a scheduled agent greps run outputs for noted fixes and opens owned repair items against the task file (closing the loop that currently dead-ends); treat task files as immutable-infrastructure artifacts — repairs only via the file, never in-run; add a "task-file version/hash" line to run outputs so drift becomes measurable; assign each task file an owning agent whose job includes merging noted fixes.
  STEELMAN:
    Strongest counterargument: For capable LLM agents, re-derivation may genuinely be cheap and robust — the agent reads the current reality each run, so it is never fooled by stale documentation, and self-healing-per-run arguably *out-performs* persisted fixes that themselves go stale (the persisted fix is a cache, and caches invalidate). In a rapidly evolving pipeline, freezing today's repair into the task file may encode today's workaround as tomorrow's bug; ephemeral re-derivation is the phoenix pattern applied to procedure rather than infrastructure.
    What would need to be true for C2A2 to be safe: Re-derivation success rate is empirically ~100% across model updates and context variations; the same repair (semantically) is derived each run; per-run repair cost is a small fraction of run budget and not growing; and no fix requires cross-run state (e.g., "delete the corrupted row once") that re-derivation would repeat destructively.
    How to test: Instrument three runs: log whether a repair was needed, what it was, and time/tokens spent. Compare repairs across runs for semantic identity and check the trend of repair count over 30 days — flat and identical supports the steelman; growing or divergent confirms compounding drift.
  Recommendation: CHALLENGED
