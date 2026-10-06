SEARCH-AGAINST-ASSUMPTION-1274:
  Date searched: 2026-09-07
  Original item: ASSUMPTION-1274
  Original statement: Abstract-level is enough for a proposal with an evidence gate noted.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1274
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-07 session transcripts ("C2a2 agent levin friston" / "Morning walk
        cowork handoff") where a proposal was built from abstract-level reading with an evidence gate noted.
      15b: Searched for challenging literature (2026-09-07) by a delegated 15b subagent (one subagent, all
        three items, AGAINST direction only; did not read any FOR file).
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Pitkin, R.M., Branagan, M.A. & Burmeister, L.F., 1999. "Accuracy of Data in Abstracts of Published
       Research Articles." JAMA 281(12):1110–1111. [VERIFIED: full text read via psychrights.org PDF mirror;
       journal, volume, pages, table and figures seen] — In six top general-medical journals (Annals, BMJ,
       JAMA, Lancet, NEJM, CMAJ), 18%–68% of abstracts contained data inconsistent with, or absent from,
       the article body. The authors' earlier RCT (Pitkin & Branagan 1998, JAMA 280:267) found that
       instructing authors to make abstracts accurate did not fix it. The abstract is not a reliable
       compression of the paper even at the highest editorial tier.
    2. Boutron, I., Dutton, S., Ravaud, P. & Altman, D.G., 2010. "Reporting and Interpretation of Randomized
       Controlled Trials With Statistically Nonsignificant Results for Primary Outcomes." JAMA
       303(20):2058–2064. [VERIFIED: PubMed abstract fetched; figures below are from it] — In 72 RCTs with
       null primary outcomes, spin was present in the abstract Results of 37.5% and abstract Conclusions of
       58.3%; 23.6% of abstract conclusions focused only on treatment effectiveness. Abstracts of null
       results are systematically written to read as positive.
    3. Boutron, I., et al., 2014. "Impact of Spin in the Abstracts of Articles Reporting Results of
       Randomized Controlled Trials in the Field of Cancer: The SPIIN Randomized Controlled Trial." Journal
       of Clinical Oncology 32(36). [VERIFIED: title/venue/PMID 25403215 via search; findings from search
       snippet; full text NOT retrieved] — Clinicians randomised to read spun abstracts rated the
       intervention as more beneficial than those reading de-spun versions of the same abstract. Abstract
       spin changes expert readers' conclusions, not just lay readers'.
    4. Greenberg, S.A., 2009. "How citation distortions create unfounded authority: analysis of a citation
       network." BMJ 339:b2680. [VERIFIED: James Lind Library record page fetched, confirming title, venue
       and free PDF; abstract figures from search snippet] — In a 242-paper network, citation bias,
       amplification (citing reviews rather than data) and invention converted a weakly supported claim into
       an "established fact"; papers that qualified or refuted the claim were cited less. Caveats placed
       upstream do not propagate; the un-caveated version is what gets cited.
    5. Sumner, P., et al., 2014. "The association between exaggeration in health related science news and
       academic press releases: retrospective observational study." BMJ 349:g7015; and Bratton, L., et al.,
       2019 replication (PMC6833989). [VERIFIED: titles/venues via search and PMC listing; the "caveats in
       ~10% of press releases and news" figure from search snippet; full text NOT retrieved] — When research
       is summarised one step downstream, caveats survive in roughly one summary in ten; exaggeration
       present in the summary is carried forward at high rates. A "noted gate" is a caveat, and caveats are
       the first thing compression drops.
    6. Thelwall, M., 2026. "Will AI be overconfident about academic research findings when reliant on
       abstracts?" arXiv:2605.27392. [VERIFIED: arXiv identifier, title and author via search; abstract
       summary from search snippet; PDF returned no machine-readable text] — An LLM (GPT-OSS 120B) rating
       claim strength separately in abstract, discussion and conclusion of full papers found claims
       stronger in abstracts than in discussions outside the social sciences/humanities; the author
       concludes that LLMs working from abstracts will be overconfident and pass that on. This is the exact
       C2A2 case: an LLM agent building a proposal from abstracts.
    7. Li, G., et al. (Sarmiento et al.), 2013. "Comparing data accuracy between structured abstracts and
       full-text journal articles: implications in their use for informing clinical decisions." (PMID
       23786759). [VERIFIED: title and PMID via search; 53% inaccuracy figure from search snippet; full text
       NOT retrieved] — 53% of structured abstracts in six widely read journals had data inaccuracies vs the
       full text; 40% contained numbers not found in the full text at all. Structured abstracts, the
       best-case format, do not remove the problem.

  Strength of challenge: Strong

  Summary: The empirical literature on abstracts is unusually consistent and unusually old: across two
  decades and multiple fields, a large minority to a majority of abstracts contain data that cannot be
  verified in the paper (Pitkin 1999; Li 2013), and abstracts of null results are written to read as
  positive in over half of cases (Boutron 2010). The spin is not cosmetic: it shifts the judgements of
  expert readers in a randomised trial (Boutron 2014). The second half of the assumption — that a noted
  evidence gate protects the proposal — is challenged by the downstream-propagation literature: caveats
  survive one step of summarisation about 10% of the time (Sumner 2014), and citation networks
  systematically strip qualifications while amplifying the bare claim (Greenberg 2009). Thelwall (2026)
  applies both halves directly to LLM readers of abstracts and predicts overconfidence. The assumption
  therefore rests on two things the literature says are false in the base case: that the abstract is a
  faithful compression, and that a caveat attached to a proposal travels with it.

  Specific risks: (a) A proposal built on an abstract inherits the abstract's spin; if the full paper's
  discussion is more hedged (Thelwall's finding), the proposal encodes a stronger claim than the source
  supports, and the "gate" is the only thing standing between that and the wiki. (b) The gate is a
  caveat in a note; when the proposal is cited, summarised, or transcribed by a later agent (14a, 13, 12,
  or a hand-off document), the caveat is the first thing dropped, leaving an un-gated claim with a
  provenance chain that looks clean. (c) The gate is never actually closed: "evidence gate noted" becomes
  a permanent status rather than a pending action, and the proposal is built on as if it had passed.
  (d) Levin/Friston-style claims are high-spin domains (theoretical-unification abstracts); the base rate
  of abstract–body mismatch is likely above the medical-journal figures, not below.

  Mitigations available: Treat the gate as a blocking state, not a note: a proposal derived from
  abstract-level reading carries a status tag (e.g. ABSTRACT-ONLY) that downstream agents are required to
  propagate verbatim and that blocks promotion to any wiki page until a full-text check has been logged.
  Where full text is unavailable, read at minimum the Discussion/Limitations section, which Thelwall's data
  identifies as the least inflated part. Record which specific claim in the proposal depends on the
  abstract, so the gate names a claim rather than a paper. Periodic audit (15d) of ABSTRACT-ONLY tags that
  have aged past a threshold without closure.

  Search scope: Preliminary — 9 queries. Covered: abstract–full-text discrepancy (medicine), spin in
  abstracts and its effect on readers, citation distortion, caveat survival under summarisation, and one
  direct LLM-on-abstracts study. Not covered: title/abstract screening sensitivity in systematic reviews
  (the requested search line was not run to completion; relevant but secondary), abstract accuracy in
  physics/biology preprints (the actual domain of Levin/Friston sources), and any study of whether a
  reader's own recorded caveat changes their later behaviour. Broader search recommended on the last
  point; the challenge as it stands is already strong on the first two.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1274
  Strongest counterargument: An abstract is not a summary of a paper; it is the paper's advertisement,
  written by interested authors, and roughly half of them cannot be reconciled with the paper they front.
  A proposal built on one therefore starts from the most inflated version of the claim available. Adding
  "evidence gate noted" does not fix this, because a gate is a caveat, and the evidence on caveats is that
  they do not travel: one downstream retelling loses nine in ten of them, and citation networks actively
  select against the qualified version. The system will thus end up holding the spun claim without the
  gate, with a provenance record that says the gate was noted. The assumption is really two assumptions
  (abstracts are faithful; caveats persist), and both are contradicted by the literature.
  What would need to be true for C2A2 to be safe: The gate must be a machine-enforced state that blocks
  promotion rather than a human-readable note; downstream agents must be unable to cite the proposal
  without carrying the tag; and the proposal's abstract-dependent claims must be enumerated so the gate
  attaches to claims, not to the document.
  How to test: Take the last 20 proposals in the wiki that were built from abstract-level reading with a
  noted gate. For each, (1) obtain the full text and check whether the Discussion/Limitations section is
  more hedged than the abstract on the claim used; (2) trace every downstream citation of the proposal and
  count how many carry the gate. If (1) exceeds ~30% and (2) is below ~50%, the assumption fails in
  C2A2's own data.
