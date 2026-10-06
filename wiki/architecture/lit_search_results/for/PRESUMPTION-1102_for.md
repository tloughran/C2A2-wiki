SEARCH-FOR-PRESUMPTION-1102:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1102
  Original statement: Polling schedules sized for active work should back off when the work completes (adaptive scheduling).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Brooker, 2015. "Exponential Backoff and Jitter". AWS Architecture Blog. https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ — backoff+jitter cut wasted calls by more than half in simulation (retry contention, not idle polling). [fetched]
    2. AWS Well-Architected REL05-BP03 "Control and limit retry calls". — bound and back off repeated calls. [search-snippet]
    3. Beyer et al., 2016. SRE book ch. 6 — rote repetitive pages as signal-to-noise red flag. [fetched]
    4. InfoQ, 2024. Alert fatigue at Cloudflare. https://www.infoq.com/news/2024/06/alert-fatigue-cloudflare — noise-reduction experience. [search-snippet]

  Strength of support: Weak-Moderate

  Summary: Backoff is well established for retries/contention and noise reduction is well documented. No source found specifically on adaptive polling that slows once work completes, or on the cost of idle scheduled runs. Claim follows from general principles; only indirectly evidenced.

  Caveats: Retry backoff addresses failures and contention, not polling of a finished workload. Idle-run cost in LLM-agent scheduling is not covered.

  Search scope: preliminary search — broader search recommended (web-only; practitioner and vendor sources dominate; no peer-reviewed primary studies located for the specific claim; fetched pages were passed through a summarizing model, so wording is paraphrase).

  Recommendation: PARTIALLY-SUPPORTED
