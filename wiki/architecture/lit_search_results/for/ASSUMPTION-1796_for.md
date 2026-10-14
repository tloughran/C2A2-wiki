SEARCH-FOR-ASSUMPTION-1796:
  Date searched: 2026-10-14
  Original item: ASSUMPTION-1796
  Original statement: [stated] Lit pipeline hypothesis over the 10-12 intake: "five of the six items share one weakness: each proposed fix replaces a failed proxy with another proxy that nobody checks against reality." Question tested: does replacing one monitoring proxy with another, without a ground-truth audit, reduce error or move it somewhere else? Supportive direction: literature showing that swapping one proxy for another without a ground-truth audit moves error rather than reducing it.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1796
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-10-13 transcripts (final 4 messages per session, read via subagents) and, where marked, from wiki artifacts.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fleming TR, DeMets DL, 1996. "Surrogate end points in clinical trials: are we being misled?" Annals of Internal Medicine 125:605-613. [Access level: snippet/secondary excerpts only, not full text.] This is the canonical statement that a correlate does not make a surrogate. A surrogate is valid only if the intervention's effect on it predicts the effect on the true outcome. Without trial-level validation against the clinical endpoint, a surrogate can mislead in either direction: it can show harm as benefit (the HRT/cholesterol example, reported in secondary sources) or miss real benefit (chronic granulomatous disease). This is direct support for the claim that an unvalidated proxy carries error that only a ground-truth audit can reveal.
    2. Surrogate endpoints in oncology review, 2017 (PMC5520356 / PubMed 28728605; author list not verified here). [Access level: search snippet.] Reports that surrogate validation against hard endpoints is rarely attempted, that the association is often unknown or weak, and that when validation is done it often finds the surrogate poor. This is empirical precedent that proxies stay in use without audit.
    3. Manheim D, Garrabrant S, 2018/2019. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585. [Access level: abstract/snippet. The search confirmed only the "regressional" category; extremal, causal and adversarial are from general knowledge and not re-verified here.] This is the theoretical basis: selecting on an imperfect proxy also selects on noise, and optimization pressure widens the gap between proxy and goal. It predicts that a new proxy under the same optimization pressure picks up its own divergence.
    4. Campbell DT, 1976 (often dated 1979). "Assessing the Impact of Planned Social Change." [Access level: secondary (Wikipedia and other summaries).] Campbell's law says the more a quantitative indicator is used for decisions, the more it is corrupted and the more it distorts the process it monitors. The police example (crime-clearance rates leading to non-recording of complaints) shows error moving out of the measured quantity into what goes unrecorded.
    5. Bevan G, Hood C, 2006. "What's measured is what matters: targets and gaming in the English public health care system." Public Administration 84(3):517-538. [Access level: abstract/snippet.] Shows that governance by targets rests on "synecdoche" (a part standing for the whole) and documents gaming. This is analogous support that performance moves to what is measured while unmeasured quality can decline.
    6. [Authors not verified; often attributed to John YJ et al.], 2023/2024. "Dead rats, dopamine, performance metrics, and peacock tails: Proxy failure is an inherent risk in goal-oriented systems." Behavioral and Brain Sciences 47. [Access level: snippet; author attribution UNVERIFIED.] Proposes that whenever a regulator selects or rewards on a proxy, pressure pushes the proxy away from the goal, across neuroscience, economics and ecology. This generalizes the mechanism beyond the clinical and policy domains.

  Strength of support: Moderate

  Summary: Strong, well-established literature (Fleming & DeMets; the surrogate-validation tradition; Goodhart and Campbell; Bevan & Hood) supports the core mechanism. A proxy that is not validated against the true outcome carries hidden error, and putting pressure on a proxy moves effort and distortion into whatever is not measured. It follows that replacing one unvalidated proxy with another, without auditing either against ground truth, gives no assurance that error falls. What changes is which unmeasured part of the system absorbs it. However, I found no study that directly compares "proxy A replaced by proxy B, neither audited" with "proxy replaced and audited". The specific "relocates rather than reduces" claim is an inference from these sources, not a measured finding.

  Caveats: (a) Domain transfer. The evidence is from clinical trials and public-sector targets, while C2A2's "proxies" are monitoring and health-check signals in an agent pipeline. (b) Some surrogates do validate well (e.g., blood pressure for stroke, per the general literature; not searched here), so a replacement proxy can be better. The literature says the improvement is unknowable without an audit, not that it is impossible. (c) Goodhart and Campbell effects scale with optimization pressure, and it is unclear how much pressure C2A2 agents put on their monitoring proxies. (d) Several sources were read only at snippet level, and the BBS author list is unverified.

  Search scope: 5 web searches (surrogate-endpoint validation; Goodhart variants; Campbell's law; targets/gaming; BBS proxy failure), 0 page fetches. Preliminary search; broader search recommended (e.g., measurement-validity and "metric substitution" literature in ML evaluation and SRE).

  Recommendation: PARTIALLY-SUPPORTED
