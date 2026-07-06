SEARCH-AGAINST-ASSUMPTION-406:
  Date searched: 2026-07-03
  Original item: ASSUMPTION-406
  Original statement: "The honest unit of replication is the conversation (k=5), so conversation-clustered CIs are the correct inferential unit."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-406
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-02 Inter-Tradition Dialogue Study (unit-of-analysis choice)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. MacKinnon & Webb, 2018, "The wild bootstrap for few (treated) clusters," Econometrics J. — With few clusters, cluster-robust t-tests can severely over-reject; naïve clustered CIs are unreliable exactly in the k-small regime.
    2. Cameron, Gelbach & Miller, 2008. — Cluster-robust inference is justified asymptotically in the *number of clusters*; small cluster counts break the approximation.
    3. Canay, Romano & Shaikh; Webb (subcluster wild bootstrap). — Even the recommended small-cluster fixes (wild-cluster bootstrap, randomization inference) can over- or under-reject when the number of clusters is very small, and require similar cluster sizes to behave.
    4. Practical rule-of-thumb literature (~≥30–50 clusters for standard CRVE). — k=5 is far below any threshold at which conventional clustered standard errors are trustworthy.

  Strength of challenge: Moderate-Strong

  Summary: The challenge is not to the *unit* (the conversation is the right unit) but to the second clause: "so conversation-clustered CIs are the correct inferential unit" is misleading at k=5. Cluster-robust CIs are an asymptotic-in-clusters device; with five clusters they can badly misstate uncertainty (typically anticonservative), and even purpose-built few-cluster corrections strain at this count. The honest statement is that the *unit* is right but standard clustered CIs are not automatically valid there.

  Specific risks: Reporting conversation-clustered CIs at k=5 as "correct" invites overconfident intervals; the +0.086 effect (A-404) and the robust/directional/null sort (P-439) could be reported with intervals that are too narrow, overstating stability.

  Mitigations available: Use randomization/permutation inference or wild-cluster bootstrap with small-sample corrections; report the fragility explicitly; treat k=5 intervals as indicative, and pre-commit to a higher-k replication before any "banked" claim.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Strongest counterargument: Choosing the conversation as the clustering unit is unambiguously correct and strictly better than pseudoreplicating on turns; given that constraint, clustered inference is the *right family* of method. The problem is purely the small k, which the study already flags. So the assumption is 90% right and the residual is a known, bounded caveat, not a refutation.
    What would need to be true for C2A2 to be safe: Small-cluster-valid procedures are used; intervals are labeled fragile; no result is treated as confirmed on k=5 alone.
    How to test: Compare naïve clustered CIs vs wild-cluster-bootstrap/RI intervals on the same data; if they diverge materially, the naïve "correct CI" claim is falsified in practice.
