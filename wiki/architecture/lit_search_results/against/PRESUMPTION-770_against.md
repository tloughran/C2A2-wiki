# PRESUMPTION-770 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-770

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-770

**Original statement:** That a mark written mid-run carries the authority of a completed run — twelve pass-marks and two task advances left by a session that died before narrating.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from a crashed session's surviving artefacts that the system has no concept of an uncommitted mark; risk graded Critical.
  - 15b: Searched for challenging literature on transactional integrity, the critique of distributed atomicity, and the idempotence/attestation trade-off.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** not that partial writes survived a crash, but the framing that the fix is stronger *attestation* (a mark that certifies run completion). The distributed-systems literature is largely hostile to that direction and favours re-derivability instead.

### Challenging evidence found: Partial

### Sources

1. **Helland, P., 2007. "Life Beyond Distributed Transactions: An Apostate's Opinion." CIDR 2007 (reprinted *Communications of the ACM*, doi:10.1145/3009826).** — The foundational argument that two-phase commit and distributed atomicity degrade availability and scalability to the point of being the wrong default in loosely-coupled systems, and that the correct discipline is at-least-once delivery plus application-level idempotence. This directly challenges the remedy implied by PRESUMPTION-770: making marks atomic with run completion imports the coordination cost the field has spent two decades escaping.
2. **Idempotent-pipeline engineering literature (Airbyte, "Idempotency in Data Pipelines"; Prefect, "The Importance of Idempotent Data Pipelines for Resilience"; systemoverflow.com, "Failure Modes and Edge Cases in Idempotent Pipelines") — [unverified — practitioner sources from search snippets].** — The consensus recovery pattern is checkpoint-and-resume with idempotency keys and partition overwrite, explicitly designed so that a partially-completed run leaves a *safe* rather than an *authoritative* state, and re-running is cheaper than certifying. Challenges the presumption's premise that a surviving mark must be authority-bearing: under this pattern its authority is irrelevant because it will be recomputed.
3. **"AI Agent Workflow Checkpointing and Resumability," Zylos Research, 2026-03-04 — [unverified — from search snippet].** — Applies the same conclusion to agent workflows: resumability from a mid-run checkpoint is the design target, and the cost of exact-once semantics across heterogeneous sinks is normally judged not worth paying.
4. **Crash-consistency work on partial writes in intermittent computation (arXiv:2006.11479, "Compiler Directed Speculative Intermittent Computation").** — Even in a domain where power loss mid-write is the *expected* case, the accepted answer is speculative execution plus rollback rather than an atomic commit barrier — i.e., tolerate the partial state and re-derive, rather than prevent it.

### Strength of challenge: Moderate

### Summary

The literature agrees that a mid-run mark surviving a crash is a real hazard, and disagrees about what follows. The dominant position since Helland is that in loosely-coupled, multi-writer systems the attempt to make a mark atomic with run completion — the two-phase-commit direction — trades availability for a guarantee that is expensive, brittle, and frequently unattainable across heterogeneous stores. The recommended alternative is to make marks *cheap to re-derive* and to make re-running idempotent, so that the question "does this mark carry the authority of a completed run?" never needs answering: the mark is provisional by construction and the next run overwrites it. On that reading PRESUMPTION-770 is correctly identifying a symptom but pointing at the wrong lever. The residual force of the presumption is the *task advance* rather than the pass-mark: advancing a task pointer is a side effect on a shared queue that a re-run may not be able to reverse, and the idempotence literature is explicit that non-idempotent side effects are the genuinely hard case. So the twelve pass-marks are challenged; the two task advances are not.

### Specific risks

If the presumption is accepted with an attestation remedy, C2A2 acquires a commit barrier at the end of every run — a single point at which any failure discards all work, which the ephemeral-compute exposure noted elsewhere in this batch makes actively dangerous. If the challenge is accepted but the split between marks and advances is missed, the non-idempotent task advances remain unprotected and the queue can drift forward past work that was never done, which is the harder half of the finding.

### Mitigations available

Split the two artefact classes. For pass-marks: make verification re-derivable and mark provisional-until-narrated with a timestamp and a session id, so a crashed session's marks are visibly stale rather than silently authoritative — this is the checkpoint pattern and costs one field. For task advances: make the advance idempotent by keying it to the run id (an advance replayed by the same run id is a no-op; an advance from a run that never narrated is reversible), which is the idempotency-key pattern Helland prescribes. Avoid the two-phase-commit direction entirely.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-770

**Strongest counterargument:** A distributed-systems engineer would grant the observation and reject the framing. Asking whether a mid-run mark "carries the authority of a completed run" presupposes that authority is the property worth engineering, and the field's settled answer since Helland's apostate's opinion is that it is not: in any system where writers can die and stores are heterogeneous, atomicity across the run boundary is either unavailable or purchased at a price in availability that exceeds the value of the guarantee. The right property is re-derivability. A pass-mark that any subsequent run can recompute in seconds has no authority to misuse; a system that instead installs a completion barrier has converted twelve recoverable stale marks into a class of failure where a late crash destroys an entire run's output. The presumption's severity grading is also questionable for the twelve marks — stale-but-recomputable is a low-cost state — and understated for the two task advances, which are the genuinely non-idempotent side effects and the only part of the finding the literature will not talk you out of.

**What would need to be true for C2A2 to be safe:** Pass-marks must be cheaply recomputable and must carry a session id and timestamp so staleness is visible; task advances must be keyed to a run id such that replay is a no-op and an advance from a non-narrated run is reversible. Under both conditions the crashed session leaves a recoverable state and the presumption's hazard does not materialise.

**How to test:** Deliberately kill a run after it has written marks and advanced a task, then start a fresh run and observe whether (a) the stale marks are detected as stale or silently trusted, and (b) the task pointer double-advances, stays, or reverts. This is a one-hour fault-injection exercise and it settles both halves of the item — and note that it also constitutes the positive control that PRESUMPTION-768 says does not exist anywhere.

---

## Search scope

Moderate. Three query families executed (distributed-transaction critique; idempotent-pipeline practice; crash consistency under partial writes). Not searched: write-ahead-logging and ARIES recovery primary literature, and the workflow-engine literature (Temporal/Cadence-style durable execution), which is the closest engineering analogue and would likely strengthen the challenge. Broader search recommended.
