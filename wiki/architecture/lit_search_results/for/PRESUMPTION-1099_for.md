SEARCH-FOR-PRESUMPTION-1099:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1099
  Original statement: Monitoring a system split across execution environments needs a shared run record; per-environment health checks give false negatives.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Beyer, Jones, Petoff, Murphy (eds.), 2016. Site Reliability Engineering, ch. 6 "Monitoring Distributed Systems". https://sre.google/sre-book/monitoring-distributed-systems/ — black-box vs white-box monitoring; a single vantage or aggregate misses problems. [fetched]
    2. Chandra & Toueg, 1996. Unreliable Failure Detectors for Reliable Distributed Systems. J. ACM. — a failure detector in an asynchronous system can only suspect failure and can be wrong; single-observer liveness inference yields false suspicions/negatives. [search-snippet, bibliographic record only]
    3. Prometheus docs (Alerting practices); GitLab runbooks "Prometheus Dead Man's Snitch". — external heartbeat/dead-man's-switch because a monitor can fail silently. [search-snippet]

  Strength of support: Moderate

  Summary: Black-box/end-to-end monitoring and failure-detector theory support that a per-component view is unreliable and an independent shared signal is needed. Dead-man's-switch practice supports that absence of signal must itself be observed. No source directly states that a shared run record across cloud and local schedulers is required; the claim is a reasonable extrapolation.

  Caveats: Sources address services/processes, not scheduled agent tasks across execution environments. "Shared run record" is an inference, not a published prescription.

  Search scope: preliminary search — broader search recommended (web-only; practitioner and vendor sources dominate; no peer-reviewed primary studies located for the specific claim; fetched pages were passed through a summarizing model, so wording is paraphrase).

  Recommendation: PARTIALLY-SUPPORTED
