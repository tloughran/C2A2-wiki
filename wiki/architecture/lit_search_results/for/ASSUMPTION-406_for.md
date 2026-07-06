SEARCH-FOR-ASSUMPTION-406:
  Date searched: 2026-07-03
  Original item: ASSUMPTION-406
  Original statement: "The honest unit of replication is the conversation (k=5), so conversation-clustered CIs are the correct inferential unit."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-406
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-02 Inter-Tradition Dialogue Study (unit-of-analysis choice)
      15a: Searched for supporting literature
    Current status: SUPPORTED (for the unit-of-analysis principle)

  Supporting evidence found: Yes

  Sources:
    1. Hurlbert, 1984. "Pseudoreplication and the design of ecological field experiments." Ecol Monogr. — Canonical statement that treating sub-observations within a replicate as independent replicates inflates evidence; the honest replicate is the independently randomized unit (here, the conversation), not the turn/utterance.
    2. Galbraith, Daniel & Vissel, 2010; Aarts et al., 2014 (Nat Neurosci). — Nested/clustered data must be analyzed at the cluster level or with mixed models; ignoring clustering produces anticonservative inference. Confirms the conversation as the correct inferential unit.
    3. Cameron & Miller, 2015. "A Practitioner's Guide to Cluster-Robust Inference." J Human Resources. — Standard errors must account for within-cluster correlation; the cluster is the unit at which independence can be assumed.

  Strength of support: Strong (for choosing the conversation as the replication/clustering unit)

  Summary: The methodological literature strongly supports the first, load-bearing half of the assumption: when observations are nested within conversations, the conversation is the honest unit of replication and inference should be clustered at that level rather than treating within-conversation observations as independent. This is the standard remedy for pseudoreplication and is uncontested as a principle.

  Caveats: The support is for the *unit choice*, not for the reliability of the *interval estimator* at k=5. Cluster-robust CIs are asymptotic in the number of clusters; with only 5 clusters the "correct unit" is right but standard clustered CIs are unreliable (see 15b — small-cluster corrections such as wild-cluster bootstrap or randomization inference are required, and even these strain at k=5).

  Recommendation: SUPPORTED (unit-of-analysis principle); conditional on small-cluster CI correction
