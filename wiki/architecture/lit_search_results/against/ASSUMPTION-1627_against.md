SEARCH-AGAINST-ASSUMPTION-1627:
  Date searched: 2026-09-23
  Original item: ASSUMPTION-1627
  Original statement: Search results that echo a query's idiosyncratic phrasing are
    disproportionately synthetic, adversarial or self-citing.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1627
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the candidate the pipeline addressed to 14a/14b.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Reflexivity note: This assumption underlies the CITATION HYGIENE rule that 15b was given for
  this run ("exclude results that echo the claim's idiosyncratic phrasing"). This search
  therefore tests a filter this file itself applied.

  Challenging evidence found: Partial

  Sources:
    1. [unverified — from background knowledge; not confirmed by a primary-source search this
       run] Thakur, N. et al. (2021). "BEIR: A Heterogeneous Benchmark for Zero-shot
       Evaluation of Information Retrieval Models." NeurIPS Datasets & Benchmarks. BM25, which
       ranks purely on lexical overlap, is a strong zero-shot baseline, and many dense
       retrievers fail to beat it out of domain. Lexical echo of rare, distinctive query terms
       is a main signal of genuine relevance, not of contamination. (The search did confirm,
       through secondary sources only, the general point that BM25 is strongest on queries with
       rare, distinctive terms such as names, codes and technical terms.)
    2. Sadasivan, V.S., Kumar, A., Balasubramanian, S., Wang, W., & Feizi, S. (2023/2024).
       "Can AI-Generated Text be Reliably Detected?" arXiv:2303.11156 (OpenReview). Gives
       empirical and theoretical evidence that AI-text detectors are unreliable and are broken
       by light paraphrasing. The optimal detector's advantage shrinks toward chance as models
       improve. A surface-feature heuristic such as "echoes the phrasing" is weaker than the
       detectors studied, and a paraphrasing adversary evades it trivially.
    3. Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). "GPT detectors are biased
       against non-native English writers." Patterns (Cell Press). Surface-linguistic
       heuristics for "synthetic" text flagged over half of genuine non-native essays as AI.
       By analogy, surface-form filters risk systematic false positives on legitimate sources.
    4. Zou, W., Geng, R., Wang, B., & Jia, J. (2025). "PoisonedRAG: Knowledge Corruption
       Attacks to Retrieval-Augmented Generation of Large Language Models." USENIX Security
       2025 (arXiv:2402.07867). Five injected texts per target question achieve about 90%
       attack success in a corpus of millions. This is two-edged. It CORROBORATES that
       adversarial texts are built to match the target query. [unverified — from background
       knowledge] The white-box variant optimizes for embedding similarity rather than lexical
       echo, so an echo filter would miss those adversarial documents.
    5. Bevendorff, J., Wiegmann, M., Potthast, M., & Stein, B. (2024). "Is Google Getting
       Worse? A Longitudinal Investigation of SEO Spam in Search Engines." ECIR 2024. Heavily
       SEO-optimized affiliate content dominates product-review results beyond its share of
       the web. This CORROBORATES a link between query-optimization and low-quality content,
       but only within one commercial genre. The authors did not test phrasing-echo as a
       marker.

  Strength of challenge: Moderate

  Summary: No source directly tests the claim that phrasing-echo signals synthetic content;
  there appears to be no literature on that exact question. The adjacent literature cuts both
  ways. Against the claim: lexical overlap is the foundation of relevance ranking, so genuine
  primary sources (especially the original paper whose phrasing a claim borrowed) will echo a
  query. Surface-form heuristics for detecting synthetic or adversarial text perform poorly and
  are biased (Sadasivan; Liang). Adversaries can optimize for semantic rather than lexical
  similarity. For the claim: SEO spam and RAG-poisoning texts are built to match target
  queries. The best-supported reading is that echo is a weak, base-rate-dependent signal. It
  may be informative when the query phrasing is truly idiosyncratic (coined by the pipeline
  itself and unlikely to appear in independent literature). It is not reliable as a general
  rule, and it produces false positives whenever the claim's phrasing came from a real source.

  Specific risks: (a) False exclusion. The citation-hygiene filter may drop the most relevant
  genuine source, the one the claim was paraphrased from, and this falls hardest on precise
  technical claims. (b) False security. Adversarial or synthetic content that paraphrases or
  optimizes semantically passes the filter, so the filter's presence overstates how clean the
  source list is. (c) Both 15a and 15b apply the same filter, so its errors are correlated
  across the FOR/AGAINST split (see SYSTEMIC-RISK-FLAG_2026-09-23_same-model-independence).

  Mitigations available: Make echo a trigger for verification rather than exclusion. Check
  that the source resolves to a real venue with real authors, and check its date against the
  date the claim was coined. Treat phrasing coined inside the pipeline differently from
  phrasing that may be borrowed from literature. Log excluded items so a later reviewer can
  audit false exclusions.

  Search scope: Preliminary — 5 searches (SEO-spam longitudinal study; AI-text detection
  reliability; lexical-overlap relevance; RAG poisoning; detector bias). No primary study of
  "phrasing echo" as a contamination marker was found. The BEIR claim is from background
  knowledge and was confirmed only through secondary sources.

  Excluded results: Medium post on hybrid BM25 retrieval; searchatlas, digitalapplied,
  ranjankumar.in and mbrenndoerfer.com blog posts; GitHub "semantic-search-reranking" repo; a
  "themoonlight.io" literature-review page on PoisonedRAG (AI-generated review aggregator).
  These were excluded as unattributable or secondary, not for phrasing echo; no results
  echoed this claim's phrasing.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1627
  Strongest counterargument: Lexical overlap is what relevance looks like, so the echo filter
    selects against relevance. For any claim whose wording was borrowed, even unconsciously,
    from a real paper, that paper is the result most likely to echo it and so the most likely
    to be excluded. Meanwhile, the adversarial content the filter targets can evade it with a
    single paraphrase pass, and state-of-the-art detectors cannot reliably tell such text from
    human text. The filter's expected effect is to lower recall of genuine sources while
    barely lowering precision against capable adversaries.
  What would need to be true for C2A2 to be safe: The phrasing being filtered is truly coined
    within the pipeline, so an independent real source is unlikely to contain it. Echo leads
    to a verification step, not an automatic exclusion. The main defense against synthetic
    sources is verifying venue and author, not matching surface form.
  How to test: Take past excluded results and check each by hand for a real venue and author.
  The share that turn out genuine is the filter's false-positive rate. Separately, seed a
  paraphrased synthetic page and check whether the filter catches it, which measures the
  false-negative rate.
