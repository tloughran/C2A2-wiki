SEARCH-AGAINST-PRESUMPTION-350:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-350
  Original statement: "[inferred] Git commit timestamps are faithful clocks for knowledge-production events."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-350
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated timing premise beneath ASSUMPTION-319
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Committer-vs-author date + history rewriting ("Teaching MSR," Palomba/Verdecchia 2025; "Does the Tool Matter?" arXiv:2501.15114). — Two timestamps exist and rebase/squash/amend mutate the commit date; tools binning on one vs the other yield shifted series. The "clock" is ambiguous and editable, not a single faithful reading.
    2. Committed ≠ completed / authored ("The Sound of Silence," arXiv:2009.01694; quick-remedy commits, PMC8553712). — Work can be completed long before it is committed (or committed via secret/integration channels, or in batches), so the commit instant is a record of a VERSION-CONTROL action, not of the knowledge-production event. The gap between doing the work and recording it is unbounded for a curated ledger.
    3. Invalid/outlier timestamps (commit-frequency and timestamp studies). — A small but nonzero fraction of timestamps are simply wrong (future-dated, pre-VCS-era), so individual commit times are not unconditionally trustworthy even if aggregates are.

  Strength of challenge: Moderate (Strong on the literal "faithful clock" reading)

  Summary: The literal presumption — commit timestamps are FAITHFUL clocks for knowledge-production — is strongly challenged: timestamps record a version-control action, are ambiguous (committer vs author), are editable (history rewriting), and decouple from the actual work via batching/backfill. They are good enough for aggregate daily rhythm (the weak reading, which 15a supports) but not faithful for individual-event production timing. As a PRESUMPTION, the unexamined "faithful clock" framing overstates what the data can bear.

  Specific risks: Any per-event timing built on commit timestamps (when was THIS triplet completed?) can be off by the commit-lag; batched/backfilled ledger edits collapse many events onto one timestamp; the committer/author choice silently shifts events across day boundaries — distorting the Metabolism timeline's fine structure.

  Mitigations available: Scope claims to aggregate daily resolution only; prefer author-date and state the choice; for events where timing matters, record an explicit completion timestamp in the artifact rather than inferring from commit metadata; detect and down-weight batch/backfill commits.

  STEELMAN:
    Strongest counterargument: For aggregate working-rhythm at day/week resolution, commit timestamps ARE empirically faithful (work-rhythm studies recover lunch-hour and weekend structure; invalid timestamps are <0.1%). If the Metabolism view only ever makes coarse aggregate claims and the user commits roughly when they work, the "faithful clock" reading is true within its operating range.
    What would need to be true for C2A2 to be safe: Claims must stay at aggregate daily resolution; commit-soon-after-work must hold; a consistent date semantics must be fixed; batch/backfill must be rare or flagged.
    How to test: Compare commit-date series against any independent completion record for the same artifacts; systematic lead/lag or batch spikes quantify the unfaithfulness.

  Search scope: Committer/author semantics, history rewriting, committed-vs-completed gap, invalid timestamps. Comprehensive. (Couples ASSUMPTION-319; member of the Metabolism-proxy SYSTEMIC-RISK cluster.)

  Recommendation: PARTIALLY-CHALLENGED
