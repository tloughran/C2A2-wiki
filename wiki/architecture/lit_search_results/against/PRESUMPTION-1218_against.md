SEARCH-AGAINST-PRESUMPTION-1218:
  Date searched: 2026-11-06
  Original item: PRESUMPTION-1218
  Original statement: Health ledger presumed to allow a writer to withhold a true observation to keep the last-line-wins aggregate correct.
  Search scope: PRELIMINARY. 1 targeted web search for challenging evidence (legitimate suppression, last-writer-wins acceptability), plus the alarm-management hits treated independently. 0 fetches; title-only. The 15a file was not read before this one.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1218
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the design of a last-line-wins health ledger
      15b: Searched for challenging literature (preliminary; title-only)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Partial
  Challenges:
    1. Boundary condition - suppression is sometimes the correct act. Titles such as "Proper alarm suppression reduces nuisance alarms" (esmagazine.com; achrnews.com) and the AIChE 2022 paper on rationalization and suppression for situational awareness suggest that suppressing a true but non-actionable signal improves operator effectiveness. Unread.
    2. Last-writer-wins is an accepted design. LWW registers are a standard conflict-resolution choice where the latest value is the intended meaning; a health file whose last line is the current state is that design. Title-level only (OPC UA Part 9 alarm state pages list shelving/suppression as defined states).
    3. Scale/domain mismatch. Plant alarm systems have many operators, thousands of alarms and enforced authorization; a one-owner personal ledger with a human reader differs, so neither the hazard nor the remedy transfers cleanly.
  STEELMAN: The strongest form of the challenge is that the presumption describes ordinary practice. ISA-18.2 and OPC UA both define suppression and shelving as legitimate states; what they require is that the act is authorized, time-limited and recorded. If the ledger's writer can note the withheld observation in a separate line or file, the aggregate stays correct and the record stays whole, and the defect is only an unlogged withholding, not the ability to withhold.
  Strength of challenge: Weak. Nothing read refutes the hazard; the challenge narrows it to unlogged withholding.
  SYSTEMIC-RISK: not flagged. Shares the unlogged-dismissal theme with PRESUMPTION-1207 (MONITOR-701); related, not independent evidence.
  Caveats: Title-only; no source opened.
  Recommendation: PARTIALLY-CHALLENGED
