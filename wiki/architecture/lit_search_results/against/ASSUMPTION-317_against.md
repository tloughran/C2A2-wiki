SEARCH-AGAINST-ASSUMPTION-317:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-317
  Original statement: "Marking a QC item resets its staleness clock, so a transcript-only pass is left unmarked to avoid masking the synthesis half's later Layer-4 review."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-317
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-14 automated-only run (QC marking behavior)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. TTL / cache-invalidation design (computing). "Time to live." — The challenge is structural: the premise treats the staleness clock as item-scoped, but cache design solves exactly this with FINER-GRAINED keys/TTLs. Leaving the whole item unmarked to protect one sub-component is a coarse workaround for a granularity problem; the literature's answer is per-sub-key freshness, not withholding the write. The chosen remedy fixes one masking at the cost of losing the record of the work that WAS done.
    2. Silent-failure / "no record == not done" hazard (observability practice; couples C2A2's own PRESUMPTION-294/322 family). — Leaving a completed transcript pass unmarked makes real work invisible: there is no durable trace that the pass happened, so the system now relies on memory or re-derivation. This is the trace-vs-substance / absence-as-evidence failure the project has repeatedly flagged — an unmarked-but-done item is indistinguishable from a not-done item to any later reader.
    3. Percentage-of-completion accounting (project accounting). — POC explicitly REJECTS binary done/not-done in favor of proportional recording precisely because both extremes mislead: booking partial as full over-reports, and booking nothing under-reports. The assumption avoids over-reporting only by adopting the equally-flawed under-reporting horn; POC says the correct move is to record the partial completion, not to suppress the mark.

  Strength of challenge: Moderate

  Summary: The challenge is not that the concern is wrong (masking coverage is a real hazard) but that the chosen remedy — leaving the item unmarked — trades a visible failure (over-reported coverage) for an invisible one (unrecorded work, memory-dependence, absence read as not-done). Cache design and percentage-of-completion accounting both prescribe finer-grained recording (per-sub-component freshness / proportional completion) rather than a binary mark/no-mark choice. The binary framing is the defect; the remedy inherits the project's recurring "absence ≠ evidence" vulnerability.

  Specific risks: A completed transcript-only pass left unmarked is later indistinguishable from work never done; the staleness/coverage accounting silently undercounts real coverage; if the synthesis-half review is delayed or dropped, the transcript pass is effectively lost. The masking the assumption fears is merely relocated from "looks done when partial" to "looks undone when partially done."

  Mitigations available: Replace the binary mark with a per-sub-component freshness record (transcript-pass timestamp AND synthesis-review timestamp tracked separately), so marking the transcript pass does NOT reset the synthesis-review clock and no work is left invisible. This is the granularity fix the TTL literature implies and directly resolves OPEN-082's marking-path remediation.

  STEELMAN:
    Strongest counterargument: Under the CURRENT single-clock implementation, the agent has only two moves — mark (resets the whole clock, masking the unreviewed synthesis half) or don't-mark (preserves the synthesis review's staleness signal). Given that constraint, leaving it unmarked is the lesser evil because a falsely-fresh item that hides unreviewed content is more dangerous than a falsely-stale item that merely invites re-checking. The assumption is locally rational given a tool limitation.
    What would need to be true for C2A2 to be safe: The freshness clock would need to be scoped per sub-component so the dilemma disappears; until then, the unmarked item must itself be tracked somewhere (a "done-but-unmarked" ledger) so the work is not invisible.
    How to test: Audit items processed under this rule over a month; count how many transcript-only passes were later re-done or lost because they carried no mark. Any nonzero rate confirms the invisibility cost.

  Search scope: TTL/cache-invalidation granularity, observability "absence ≠ evidence" hazard, percentage-of-completion accounting. Comprehensive for the analogues; the specific pattern is under-studied (matches 15a NOVELTY note).

  Recommendation: PARTIALLY-CHALLENGED
