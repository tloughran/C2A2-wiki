SEARCH-FOR-PRESUMPTION-1210:
  Date searched: 2026-11-04
  Original item: PRESUMPTION-1210
  Original statement: Duplicate copies of a task are presumed temporally separable: the second copy is called harmless because it 'waits and only checks', which holds only if it can tell when the first copy has finished.
  Claim tested (literature lane): primary sources on at-most-once execution for cron/scheduler duplicates (leases, fencing tokens, idempotent writes) versus wait-and-check heuristics. The in-house limb (second-copy start times vs first-copy completion, 10-26..11-03) is NOT 15a/15b scope and was not run.
  Reading used for the FOR direction: the presumption is a real, documented hazard. Wait-and-check without an atomic, durable launch record cannot establish that the first copy is finished or gone, so the literature supports treating it as an unsafe presumption.
  Search scope: PRELIMINARY. 4 web searches, 2 fetches (SRE book ch. 24, Lorin Hochstein's FizzBee post, both read as fetch summaries). Other hits are title-only. Not reached: Kleppmann's essay text, Gray & Cheriton 1989 on leases, any LLM-agent scheduler source.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a
    Original item: PRESUMPTION-1210
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the claim that a second task copy is harmless because it 'waits and only checks'
      15a: Searched for supporting literature (preliminary; 4 searches, 2 fetches)
    Current status: PARTIALLY-SUPPORTED
  Supporting evidence found: Partial
  Sources:
    1. Beyer, B., Jones, C., Petoff, J., Murphy, N.R. (eds.), 2016, Site Reliability Engineering, ch. 24 "Distributed Periodic Scheduling with Cron." https://sre.google/sre-book/distributed-periodic-scheduling/ [fetched; summary read] - Google's cron does not rely on copies noticing each other: one leader launches, and the start and end of each launch are written synchronously to a quorum, with launches identified by scheduled time so a successor can tell whether a launch happened. The need for that machinery is the case against wait-and-check.
    2. Hochstein, L., 2025, "Locks, leases, fencing tokens, FizzBee," surfingcomplexity.blog https://surfingcomplexity.blog/2025/03/03/locks-leases-fencing-tokens-fizzbee/ [fetched; summary read; secondary, cites Kleppmann] - a process can believe it still holds an expired lease while another takes it, and both enter the critical section. A copy that waits for the first to finish can be wrong in the same way if the first has merely paused.
    3. Kleppmann, M., "How to do distributed locking" [not retrieved; known via source 2 and title-only hits such as alivedise BEE-19028 Fencing Tokens https://alivedise.github.io/backend-engineering-essentials/distributed-systems/fencing-tokens] - fencing tokens are proposed so a stale holder cannot act on the shared resource.
    4. dev.to "Designing Distributed Cron: At-Most-Once Execution" https://dev.to/sashaonion/designing-distributed-cron-at-most-once-execution-4hlj ; velobot-wiki "The Exactly-Once Illusion" https://velobot-wiki.pages.dev/article/software/distributed-cron-scheduler-correctness-idempotency-playbook/ [title only; practitioner] - practitioner material treating duplicate scheduler launches as a standard correctness concern.
  Strength of support: Moderate for the general claim that wait-and-check is not a safe substitute for a durable launch record (one read primary book chapter plus one read secondary); Weak for any LLM-agent scheduler claim (nothing found).
  Summary: The literature does not treat "the second copy waits and checks" as a guarantee. The SRE chapter builds quorum-recorded launches keyed by scheduled time precisely so a successor never has to infer completion, and the lease literature shows an apparent holder may act after it appears gone. The presumption is therefore supported as a presumption: it holds only if completion is recorded atomically and the checker reads that record.
  Caveats: Both read sources are summaries. None concerns LLM-agent or file-lock schedulers on a single machine, where pause and clock hazards differ from cloud clusters. NOVELTY: not flagged for the general pattern; the LLM-agent case is unaddressed.
  Recommendation: PARTIALLY-SUPPORTED
