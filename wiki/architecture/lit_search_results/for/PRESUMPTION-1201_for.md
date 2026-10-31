SEARCH-FOR-PRESUMPTION-1201:
  Date searched: 2026-10-31
  Original item: PRESUMPTION-1201
  Original statement: "[inferred] Second firings now present themselves as verification ('I checked its work and changed none of it'; 'I checked it against the chat, found it accurate'). This presumes a second run of the sa[me process counts as independent verification]" (truncated in source)
  Claim tested (literature): N-version programming and independent-verifier literature (e.g., Knight & Leveson 1986 on correlated failures); whether re-running the same process counts as independent verification; LLM self-consistency vs self-verification limits.
  Reading used for the FOR direction: "Support" = literature showing a re-run of the same process is NOT independent verification (correlated failures, self-verification limits), which supports the concern that the presumption is unsound. Literature supporting the presumption itself (that same-process re-runs verify) was not found in this pass.
  Search scope: PRELIMINARY. 2 web searches, 0 fetches. Searched: Knight-Leveson independence in multiversion programming; LLM self-correction / self-verification limits. Not reached: self-consistency (Wang et al. 2022) literature, LLM-as-judge self-preference bias, human-factors work on same-reviewer re-checking, any literature SUPPORTING same-process re-run as verification. All sources are search-result titles/URLs only; no page content was read.
  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1201
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from 2026-10-30 local pass second-firing notes (second runs described as verification)
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — SUPPORTED
  Supporting evidence found: Yes
  Sources:
    1. Knight & Leveson, 1986. An Experimental Evaluation of the Assumption of Independence in Multi-Version Programming. Hits: https://www.kth.se/social/files/564df871f2765419e306178d/KnightLeveson.pdf ; https://ntrs.nasa.gov/api/citations/19870002808/downloads/19870002808.pdf ; https://libraopen.lib.virginia.edu/public_view/jd472w463 [snippet only: titles/URLs] — the paper's title directly addresses the independence assumption; that independently written versions fail coincidentally more than independence predicts is [from memory, unverified]. Same-process re-runs would be expected to be at least as correlated.
    2. Huang et al., 2023/ICLR 2024. Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/pdf/2310.01798 [snippet only: title] — title states LLMs cannot self-correct reasoning without external feedback; relevance is to self-review passes.
    3. Stechly, Valmeekam, Kambhampati, 2024/ICLR 2025. On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks. https://arxiv.org/pdf/2402.08115 [snippet only: title] — title directly addresses limits of LLM self-verification; authorship [from memory, unverified].
    4. Vaughan, 2026. N-Version Programming with Coding Agents (Knight–Leveson replication for Codex CLI). https://codex.danielvaughan.com/2026/06/20/n-version-programming-coding-agents-codex-cli-diversity-majority-voting-multi-model-resilience/ [snippet only: title; blog, non-peer-reviewed] — applies the independence concern to LLM agents.
    5. https://tianpan.co/blog/2026/05/10/spec-code-tests-single-author-lost-test-independence [snippet only: title; blog] — title suggests same-author tests lose independence; same logic.
  Strength of support: Moderate
  Summary: Established literature (Knight & Leveson; LLM self-correction/self-verification papers) is on its face consistent with the concern that a second run of the same process does not supply independent verification. The Knight-Leveson result concerns separately developed versions, so same-process re-runs are a weaker case still. LLM self-verification papers support doubt about self-checks lacking external grounding. However, the 'checked against the chat' case has an external reference (the chat), which may partly mitigate; the literature suggests grounding matters.
  Caveats: Snippet-only; no content verified. Specific findings above are from titles plus memory where marked. The wiki's second firing may differ from LLM self-verification (it compares against a source). No literature found supporting the presumption.
  Recommendation: SUPPORTED
