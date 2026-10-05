SEARCH-FOR-PRESUMPTION-1048:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1048
  Original statement: A monitoring agent sampling at a slower rate than its source publishes has a structurally invisible coverage window whose size is determined by the two cadences, and whose failure mode is a null report indistinguishable from a quiet period.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1048
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (cadence mismatch between monitoring agents and source publication; window found by accident when orchestrator read the source index directly)
      15a: Searched for supporting literature; found formal support (sampling theory) and applied analogues (crawler freshness, RSS polling, systematic-review decay); strength: Moderate
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Cho, J. & Garcia-Molina, H., 1999/2000. "Synchronizing a Database to Improve Freshness." Stanford tech report (Oct 1999); SIGMOD 2000. — Models source changes as Poisson events and derives freshness as a function of the ratio of change rate to sync rate (e.g., ~63% freshness when the two rates are equal under fixed-order sync; roughly 2x sync-to-change rate needed for ~80%). Poisson assumption checked on ~720,000 pages from 270 sites. Directly shows the coverage/freshness loss of a periodic poller is a closed-form function of the two cadences. (Fetched via kth.se copy; figures as reported by the fetch summary, not independently re-derived.)
    2. Liu, H., Ramasubramanian, V., Sirer, E.G., 2005. "Client Behavior and Feed Characteristics of RSS, a Publish-Subscribe System for Web Micronews." ACM IMC '05. — Measured heterogeneity of feed update rates (55% of feeds update hourly, 25% silent for days) against client polling (~58% of automated clients use the default hourly rate). Documents the real-world cadence-mismatch condition for pull-based monitoring of a publishing source; absence of push notification forces poll-based design. Does NOT itself quantify missed items.
    3. Shannon, C.E., 1949. "Communication in the Presence of Noise." Proc. IRE 37(1):10-21; Nyquist–Shannon sampling theorem (standard exposition checked: dsprelated.com/foundations/sampling.php). — Under the bandlimit assumption, sampling at less than 2·fmax makes higher frequencies alias to lower ones and the loss is irreversible; samples alone cannot distinguish the original from its alias. Supports the "structurally invisible" and "indistinguishable" parts in the formal half.
    4. Shojania, K.G. et al., 2007. "How Quickly Do Systematic Reviews Go Out of Date? A Survival Analysis." Annals of Internal Medicine 147(4):224-233. — 100 meta-analyses: median survival without substantive new evidence 5.5 years; 23% had a signal for updating within 2 years; 7% were already outdated at publication. Supports that update/search intervals longer than the evidence-arrival interval leave undetected change. (Details taken from a secondary summary, tripdatabase blog; PubMed page not retrievable; confirm against primary text.)

  Strength of support: Moderate

  Summary: The claim has two halves. The formal half (coverage loss is determined by the two cadences) is well supported: sampling theory shows irreversible, undetectable information loss below the Nyquist rate, and Cho and Garcia-Molina give an explicit rate-ratio formula for how much change a periodic poller misses. For a simple periodic publisher of period P sampled every T > P and observing only the latest state, the unseen fraction is 1 - P/T; this is my own elementary derivation, not a cited result. The applied half is supported by analogy: RSS measurement work documents poll-versus-publish mismatch, and systematic-review decay work shows search intervals exceeding evidence-arrival intervals miss material change. No source found directly addresses the third clause, that a null report is indistinguishable from a quiet period, in a monitoring-agent setting; it follows logically from the aliasing result but is not independently documented.

  Caveats:
    - Nyquist–Shannon assumes bandlimited continuous signals; the presumed corpus is discrete, event-based and (per 15b's likely direction) possibly persistently indexed. If items persist and are retrievable by index, a slow sampler loses latency, not items; the "invisible window" then applies only to non-persistent or expiring sources, or to polling the stream versus polling the index. Aliasing is an analogy here, not a direct application.
    - Cho and Garcia-Molina concern freshness of copies of changing pages (overwrites), not accumulation of append-only publications, so the missed-items measure differs.
    - Liu et al. is 2005 RSS data and does not measure missed items; Shojania is clinical-evidence decay, a loose analogue.
    - Items 2 and 4 verified only through summaries; item 1 through a mirrored PDF summary. Primary-text confirmation recommended before citing figures.
    - Publication bias: positive framing of polling-cost results is likely over-represented.
    - Scope: preliminary search (about 4 queries, 5 fetches); did not search news-alerting cadence design, systematic-review search-recall decay as a recall metric, or stream-vs-index polling literature in depth. Broader search recommended. Tradition wikis were not consulted (not available to this run).

  Recommendation: PARTIALLY-SUPPORTED

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1048
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Cho, J. & Garcia-Molina, H. (1999/2000). "Synchronizing a Database to Improve Freshness." SIGMOD 2000.
  Summary: Sampling theory and crawler-freshness models show that what a periodic poller misses is a closed-form function of the two cadences, and that sub-Nyquist loss is undetectable from the samples alone. The "null report indistinguishable from quiet period" clause and the append-only, persistently indexed corpus case are not directly documented; transfer from continuous-signal/overwrite models is by analogy.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1048_for.md

NOVELTY-FLAG:
  Item: PRESUMPTION-1048 (third clause only: null report indistinguishable from a quiet period)
  Searched: sampling theory, crawler freshness, RSS polling, systematic-review update decay (preliminary)
  Finding: No existing literature located that addresses this specific failure mode for monitoring agents as stated; formal ingredients exist but the combined claim was not found
  Implication: Possible original framing for agent-based literature monitoring (silent-failure signature of cadence mismatch); limited to the null-report clause, not the whole claim
  Recommended status: NOVEL (partial; pending broader search)

QUEUE SUMMARY: PRESUMPTION-1048 [SEARCHED-15a: 2026-10-05] PARTIALLY-SUPPORTED / Moderate; formal and analogous support found, null-report clause undocumented, persistence/indexing caveat open for 15b.
