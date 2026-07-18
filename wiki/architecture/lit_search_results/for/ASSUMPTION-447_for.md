SEARCH-FOR-ASSUMPTION-447:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-447
  Original statement: "Bridge/synthesis notes are near-orphans by nature (link out, rarely linked in); 42 of 45 at <=2 backlinks is expected steady state, not connectivity failure."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15a
    Original item: ASSUMPTION-447
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-12 connectivity census
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. [Barabasi, A.-L. & Albert, R. (1999). "Emergence of scaling in random networks." Science 286(5439):509-512. — Preferential attachment yields a stationary power-law degree distribution in which the modal node has very low indegree by structural necessity. Low indegree is an equilibrium property, not a defect.]
    2. [Broder, A. et al. (2000). "Graph structure in the web." Computer Networks 33:309-320. — Web indegree follows ~1/i^2.1; the bow-tie's IN and TENDRIL regions consist of large populations of pages that link out to the core and are never linked in. This is exactly the topological position the claim assigns to bridge notes.]
    3. [Zlatic, V., Bozicevic, M., Stefancic, H. & Domazet, M. (2006). "Wikipedias: Collaborative web-based encyclopedias as complex networks." Phys. Rev. E 74:016115. — Across language editions in- and out-degree are both heavy-tailed but with DIFFERENT exponents: indegree and outdegree are decoupled, so a note can be outbound-rich and inbound-poor without anomaly.]
    4. [Kleinberg, J. (1999). "Authoritative sources in a hyperlinked environment." JACM 46(5):604-632. — Formalises HUBS (high outdegree, pointing at good authorities) as a distinct and valuable role from AUTHORITIES (high indegree). A synthesis note is a hub in precisely Kleinberg's sense, and hubs are not defined by being pointed at.]
    5. [PKM/Zettelkasten practitioner literature on Maps of Content and structure notes (LYT; Obsidian and Zettelkasten community). — NOTE: folk practice only. NO peer-reviewed source was found empirically characterising synthesis/index notes as outbound-heavy. This gap is reported, not papered over.]
  Strength of support: Moderate
  Summary: The structural half of the claim is well supported. In any preferential-attachment-like link graph, most nodes carry near-zero indegree; indegree and outdegree are separate, decoupled distributions; and the hub role is recognised in link analysis as functionally valuable independent of indegree. "42 of 45 at <=2 backlinks" is therefore entirely consistent with a healthy heavy-tailed graph and requires no pathology to explain. What the literature does NOT supply is the specific empirical premise that SYNTHESIS notes are the low-indegree ones in a PKM vault: that is asserted from practitioner convention, not measured. The claim is topologically plausible and empirically untested in this vault.
  Caveats: The support covers "low indegree is expected"; it does not reach the normative second clause, "therefore not a connectivity failure." Structural expectedness and functional harmlessness are different claims, and only the first is supported here.
  Recommendation: PARTIALLY-SUPPORTED
