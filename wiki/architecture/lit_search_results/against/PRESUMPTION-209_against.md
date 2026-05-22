SEARCH-AGAINST-PRESUMPTION-209:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-209
  Original statement: "A single agent's directory scan is authoritative — no reconciliation layer across counting agents."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-209
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — counts taken from one agent's directory scan treated as ground truth, with no reconciliation across counting agents.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Gilbert, S. & Lynch, N. (2002). "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services" (CAP). — A single node's view is not authoritative under concurrency/partition; consistency requires coordination.
    2. Lamport, L. (1998). "The Part-Time Parliament" (Paxos). — Agreement on a value across processes requires consensus, not one process's reading.
    3. DeCandia, G. et al. (2007). "Dynamo" (SOSP). — Read-repair / quorum reconciliation exists precisely because divergent replica reads occur; one read is not ground truth.
    4. Split-brain literature (distributed-systems). — Two agents producing different counts (the observed Levin/Friston discrepancy) is the classic split-brain symptom that demands reconciliation.

  Strength of challenge: Strong

  Summary: The challenge is strong and directly instantiated: distributed-systems theory (CAP, Paxos, Dynamo) is unanimous that a single reader's snapshot is not authoritative when multiple agents observe shared, changing state. The observed Levin/Friston count discrepancies (OPEN-052, MONITOR-194/195) are textbook split-brain symptoms. Without a reconciliation layer (write-receipts / manifest-as-truth / quorum), the system will keep oscillating between disagreeing scans. This extends PRESUMPTION-196/204.

  Specific risks: Conservation-gate throttles and Pattern Detector inputs driven by an arbitrary, possibly-wrong scan; ground-truth oscillation; the count discrepancies already observed.

  Mitigations available: Introduce a reconciliation layer: write-receipt manifest as the source of truth; quorum/agreement across counting agents; alarm on inter-agent disagreement rather than trusting one scan.

  Recommendation: CHALLENGED (REVISE)

  STEELMAN:
    Item: PRESUMPTION-209
    Strongest counterargument: When multiple agents observe shared mutable state, no single agent's scan is authoritative — this is the foundational result behind CAP, consensus, and read-repair. The Levin/Friston discrepancies are split-brain in miniature; trusting one scan guarantees the system will act on the wrong count some fraction of the time.
    What would need to be true for C2A2 to be safe: Safe once a reconciliation layer (write-receipt manifest / quorum) is the source of truth and single scans are treated as proposals, not facts.
    How to test: Run two counting agents on the same snapshot; if they disagree (as observed), the no-reconciliation presumption is falsified.
