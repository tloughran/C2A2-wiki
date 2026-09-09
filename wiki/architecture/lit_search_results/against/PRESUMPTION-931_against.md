SEARCH-AGAINST-PRESUMPTION-931:
  Date searched: 2026-09-09
  Original item: PRESUMPTION-931
  Original statement: [inferred] Scheduler liveness is estate health — if the jobs fired, the system is
    working, and the freshness of what they produced is a separate and lesser question.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-931
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from two same-morning reports that disagree because they ask different questions,
        neither of which states which question it is asking — the 08:00 `Morning project status`
        ("all of today's jobs fired on schedule … Nothing is broken") read against the 09:45Z scheduler
        health check's five freshness FAILs on the same estate.
      15b: Searched for challenging literature (2026-09-09), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item.
    Current status: NO-CHALLENGE-FOUND on the core claim; a real but narrower challenge found on the
      cost of the remedy.

  Challenging evidence found: Partial — and not where the intake expected it.

  I searched specifically for the claim the intake asked me to find: that liveness/exit-status checks
  are adequate proxies for output health in scheduled batch estates. **I could not find it.** Not in
  peer-reviewed work, not in practitioner literature, not even in the vendor marketing that would have
  the strongest commercial reason to say something reassuring about existing monitoring. What I found
  instead was the opposite claim stated as background assumption by sources with no stake in it — that
  a job can succeed and produce nothing. The genuine challenge that does exist is narrower and worth
  taking seriously: adding freshness alerting has a measurable, documented cost in alert volume, and
  monitoring literatures in two domains have watched that cost eat the benefit.

  Sources:
    1. HHS Office of Inspector General, 2012. "Hospital Incident Reporting Systems Do Not Capture Most
       Patient Harm." Report OEI-06-09-00091, issued 2012-01-05.
       [VERIFIED: the OIG report page was retrieved and read this run; figures and the quoted
       characterisation are from that page. The 1.9 MB full PDF was not opened.] — Cited here for the
       structural point rather than the domain: the systems in question were *live* — "All of the
       hospitals we reviewed had incident reporting systems designed to capture events; hospital
       administrators we interviewed indicated that they rely heavily on the systems to identify
       problems" — and they captured 14% of the harm. Liveness of the reporting channel was not just an
       imperfect proxy for its output; it was uncorrelated with it, and the reliance on liveness was
       what made the gap invisible. This does not challenge PRESUMPTION-931; it is the cleanest
       measured instance of the presumption failing, and I record it in the AGAINST file because
       honesty requires reporting what the search returned.
    2. Clinical-decision-support and ICU alarm literature: "Appropriateness of Overridden Alerts in
       Computerized Physician Order Entry: Systematic Review" (PMC7400042); "Effects of workload, work
       complexity, and repeated alerts on alert fatigue in a clinical decision support system"
       (PMC5387195); ICU alarm reviews reporting false-alarm rates.
       [NOT-verified — all figures from search-result summaries; no full text retrieved this run.] —
       Reported: 72–99% of clinical alarms are false; only 5–13% of ICU alarms are actionable;
       CDS override rates range 46.2%–96.2% across systems. This is the real challenge, and it is a
       challenge to the *remedy*, not to the presumption: a monitoring channel whose alerts are mostly
       non-actionable does not merely fail to add detection, it degrades the channels around it by
       training the operator to dismiss. Five freshness FAILs on one morning in a one-person estate is
       already at the volume where this matters.
    3. Practitioner survey reported April 2026 (businesswire release; underlying study not identified).
       [NOT-verified — press-release summary only; I could not identify the underlying study, its
       sample, or its methodology, and I am not treating the numbers as reliable.] — Reported: 57% of
       on-call teams say fewer than 30% of alerts are actionable; 83% of engineers ignore or dismiss
       alerts at least occasionally; 44% had an outage traced to a suppressed or ignored alert. Noted
       with the caveat that the same release reports 78% had an incident where *no alert fired at all*
       — i.e. the source cuts both ways and, if anything, cuts harder against the presumption than for
       it.
    4. Data-observability practitioner literature (Monte Carlo, Validio, Atlan, Litmus, Conduktor,
       Sifflet, Databricks).
       [NOT-verified — vendor grey literature, read as search summaries only. Weak as evidence; cited
       for what it concedes rather than what it claims.] — Two things are consistent across vendors who
       sell freshness monitoring and vendors who sell pipeline monitoring alike. First, the concession
       that runs against the presumption: monitoring pipeline jobs alone is not enough, because a job
       can run successfully and produce no new data. Second, the concession that runs against the
       remedy: aggressive freshness SLOs set before a pipeline can meet them "create alert fatigue and
       erode trust in the monitoring system," and false positives train teams to ignore alerts. The
       recommended false-positive target is under 10% and the recommended alert-to-incident conversion
       above 20% — thresholds that exist because unmanaged freshness alerting routinely misses them.
    5. Searches that returned nothing on point, recorded as negative results: an evaluation study
       comparing the yield of freshness checks against job-success monitoring; any study finding
       staleness monitoring low-yield in practice; any defence of exit-status monitoring as sufficient.
       Two separate queries; nothing returned. This is a genuine literature gap and should be recorded
       as one rather than as reassurance in either direction.

  Strength of challenge: Weak

  Summary: The AGAINST direction largely failed on this item, and I want that stated plainly rather
  than padded. I searched for evidence that liveness is an adequate proxy for output health and found
  none; the nearest thing to a defence of exit-status monitoring in the sources I saw was silence. The
  one substantive challenge available is displaced from the presumption onto its remedy: the alarm and
  alert-fatigue literatures document, with hard numbers in the clinical case, that a monitoring channel
  with a low actionable fraction imposes real costs — desensitisation, override, and eventually the
  dismissal of true positives. Five freshness FAILs arriving on one morning against a "nothing is
  broken" summary is precisely the configuration that produces those costs, because the operator's
  cheapest resolution of the contradiction is to stop reading one of the two channels. So the honest
  finding is: the presumption itself stands unchallenged and looks false, but the naive fix — turn on
  freshness alerting everywhere — has a documented failure mode of its own, and the design question is
  not whether to measure freshness but how to make freshness alerts actionable enough that they are
  still being read in three months.

  Specific risks: These are risks of the *remedy*, since I found no support for the presumption. (a)
  Alert-fatigue capture: if freshness checks fire five times on a quiet morning, the operator learns
  within weeks that freshness FAILs are ambient, and the channel is dead while still appearing live —
  which reproduces the presumption's error one level up, with a monitoring system that is itself
  green-because-running. (b) Threshold arbitrariness: a freshness SLO set without knowledge of a
  pipeline's real cadence generates structural false positives; the vendor literature's own remedy is
  to start conservative and tighten, which means the first months of freshness data will be dominated
  by threshold error rather than by staleness. (c) Two green channels asking different questions is
  worse than one, unless each states its question — the 08:00/09:45Z contradiction is not an accident
  of implementation but the expected result of two monitors with unstated scopes, and adding a third
  monitor without stating scopes makes it worse. (d) Residual risk on the FOR side that I am not
  positioned to assess: the OIG finding suggests the detection gap between "the mechanism ran" and
  "the mechanism worked" can be very large indeed, and nothing I found bounds it.

  Mitigations available: (i) Require every health report to state its own question in its first line
  ("jobs fired: yes/no" vs "outputs fresh: yes/no"). This costs one line and would have prevented the
  09-08 contradiction entirely. (ii) Set freshness thresholds from observed cadence rather than from
  intent, and record the false-positive rate of each freshness check for its first month before it is
  allowed to page. (iii) Track the alert-to-action ratio for the freshness channel explicitly; the
  clinical literature's lesson is that a channel below roughly 20% actionable is not a monitor, it is
  noise with a timestamp. (iv) Prefer one merged report with two labelled sections over two reports
  that can disagree silently. (v) Note that (i)–(iv) are prescriptions with no owner and therefore
  fall under PRESUMPTION-935 unless one is assigned.

  Search scope: Preliminary, and explicitly incomplete in the direction I was asked to search — 4
  queries, 1 retrieval. Two of the four queries were aimed directly at the requested challenge and
  returned nothing. Literatures touched: healthcare incident-reporting coverage, clinical alarm and
  alert fatigue, SRE/on-call alerting practice (grey), data-observability practice (vendor grey). Not
  covered: process-safety alarm philosophy (EEMUA 191 / ISA 18.2) at primary-source level, which is the
  most likely place to find a rigorous treatment of alarm-rate limits and would strengthen the
  mitigation section; academic work on monitor precision in production data pipelines (searched,
  nothing on point); any study measuring the incremental detection yield of freshness SLOs over
  exit-status monitoring, which appears not to exist. A broader search is recommended, but on present
  evidence I expect it to strengthen rather than weaken the case against the presumption.

  Recommendation: NO-CHALLENGE-FOUND (on the presumption itself); the challenge that exists applies to
    the remedy and is Weak-to-Moderate. Recorded as NO-CHALLENGE-FOUND per the charter's requirement to
    distinguish "searched and found nothing" from "not enough searched" — this was searched, twice,
    directly, and nothing was found.

STEELMAN:
  Item: PRESUMPTION-931
  Strongest counterargument: The best available case for the presumption is not that liveness measures
  health — nobody argues that — but that freshness monitoring is not free and, in a small estate, may
  cost more than it returns. Monitoring literatures with actual measurements are uniformly grim about
  low-precision channels: 72–99% of clinical alarms are false, only 5–13% of ICU alarms are actionable,
  and override rates in decision support run as high as 96%. The consequence is not neutral. A channel
  that fires often and means little does not sit inertly beside the good channels; it teaches the
  operator to discount alerts as a class, and the documented endpoint is a true positive being
  dismissed. An estate with one human reader, five freshness FAILs before ten in the morning, and a
  cheerful summary saying nothing is broken is exactly the setup where that learning happens fast. On
  this reading the 08:00 report's behaviour is not a naive conflation but a defensible triage: report
  the signal that is nearly always actionable (a job that did not fire is unambiguously wrong) and
  leave the signal that is usually threshold noise to a specialist check that a human consults
  deliberately. The presumption, stated charitably, is a claim about alert economics rather than about
  system health — and the alert-economics literature is on its side even though the system-health
  literature is not.
  What would need to be true for C2A2 to be safe: The freshness checks would have to have a low enough
  false-positive rate that they are worth reading — say, thresholds derived from each pipeline's
  observed cadence rather than from intent — and the two reports would have to state their scopes so
  that a disagreement between them is legible as two answers to two questions rather than as one
  channel being wrong. Additionally the presumption would need the staleness failures it ignores to be
  either rare or independently detected downstream. On 09-08 there were five of them on one morning and
  no evidence of downstream detection, so that condition visibly does not hold.
  How to test: Directly measurable from the estate's own logs, and it settles both the presumption and
  the alert-economics defence at once. Over the next 30 days record, for every scheduled job: whether
  it fired, its exit status, and the mtime/content-hash delta of its declared outputs. Then build the
  2×2 — fired-and-fresh, fired-and-stale, didn't-fire-and-stale, didn't-fire-and-fresh. The
  fired-and-stale cell is the detection gap that liveness monitoring structurally cannot see, and its
  size is the entire question; if it is empty, the presumption is vindicated for this estate and the
  freshness checks can be relaxed. Simultaneously, count how many of the freshness FAILs raised in
  those 30 days led to any action. If the fired-and-stale cell is large and the action rate is high,
  the presumption is false and the remedy is cheap. If the cell is large and the action rate is near
  zero, the presumption is false but the remedy as currently configured is already dead — which is the
  outcome the alarm literature would predict and the one worth catching early.
