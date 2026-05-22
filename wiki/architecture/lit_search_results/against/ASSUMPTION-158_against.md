SEARCH-AGAINST-ASSUMPTION-158:
  Date searched: 2026-05-18
  Original item: ASSUMPTION-158
  Original statement: "Path 2 (DeepSeek-Flash via API + worker script reading job-folder queue) is the chosen architecture for adding a non-Claude LLM agent to the same vault."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-158
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/Surfaced from 2026-05-17 c2a2-self-awareness-daily run (resumed cycle)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. AWS Builders' Library 'Timeouts, retries and backoff with jitter' — file-folder queues lack the retry-budget, dead-letter-queue, and visibility-timeout primitives that production queue services provide; rolling your own is a documented anti-pattern under load.
    2. Microsoft Azure 'Retry Pattern' guidance — transient-fault handling is non-trivial; the chosen one-shot architecture (per ASSUMPTION-163) is incompatible with the most-cited retry-pattern advice.
    3. ByteByteGo 'A Guide to Retry Pattern in Distributed Systems' — flags failure-mode handling as the load-bearing concern in producer/consumer architectures; file-folder coordination defers this rather than solving it.

  Strength of challenge: Moderate

  Summary: The chosen-architecture claim is supportable at the topology level but vulnerable on operational-maturity grounds. Production queue services exist precisely because rolling-your-own queue surfaces predictable failure modes (lost messages, double-processing, ordering, visibility timeouts) that file-folder coordination cannot natively address. The 'Path 2 chosen' decision optimizes for inspection-and-simplicity over operational robustness — a tradeoff the literature considers defensible at small N but suboptimal at scale.

  Specific risks: (a) Folder-as-queue may silently lose messages if the worker crashes mid-processing without atomic move-on-pickup; (b) no visibility-timeout means concurrent workers could double-process; (c) operational issues that production queues solve (dead-letter, retry budgets) re-emerge as ad-hoc patches.

  Mitigations available: (a) Atomic-rename move-on-pickup; (b) hold to single-consumer until contention is empirically observed (PRESUMPTION-183 flags this); (c) periodic outbox/done reconciliation audit.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-158
    Strongest counterargument: The strongest case against: 'Chosen architecture' is premature; the more honest framing is 'first-acceptable architecture for N=1 producer and small message volumes.' Literature on integration patterns consistently warns that 'simple folder queue' is a starter pattern that breaks at the boundaries that any production system eventually meets. The Path-3 rating ('worth doing after Path 2 pays off') quietly acknowledges this.

