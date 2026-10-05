SEARCH-AGAINST-PRESUMPTION-1111:
  Date searched: 2026-10-04
  Original item: PRESUMPTION-1111
  Original statement (presumption under test): A chat's title is a reliable enough signal of whether it carries designer input to serve as the sole inclusion filter.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1111
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (lane: selection bias from metadata-based filtering; precision/recall of title vs content classification in document triage).
      15b: Searched for challenging literature; found title-vs-full-text evidence (mixed) and documentation that chat titles are generated from the first exchange only; strength: Moderate
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Galke, L., Mai, F., Schelten, A., Brunsch, D. & Scherp, A., 2017. "Using Titles vs. Full-text as Source for Automated Semantic Document Annotation." K-CAP 2017; arXiv:1705.05311 [search-result] — MIXED. On three of four datasets, title-only classification reached over 90% of full-text quality. Full text still did better, and the gap varied by dataset. Titles carry most of the topical signal for *published* documents whose authors chose the titles to describe them. That condition does not hold for chat titles (see 2).
    2. Chat auto-titling documentation: Hasura PromptQL "Chat titles"; Treasure AI Studio "Auto-Titled Conversations"; Supra Labs "SupraTitle"; OpenWebUI title-generator model card [search-result, practitioner/vendor] — Chat titles are typically generated automatically by a small or main LLM from the *first message or first exchange*, then left unchanged. By construction the title cannot reflect input that arrives later in the chat, so designer input given mid-conversation is invisible to a title filter.
    3. Older IR work comparing title-only and full-text indexing (NIST IRLib / ISR-11 reports; OHSU "A comparison of techniques for classification and ad hoc retrieval" (Hersh et al.)) [search-result] — Full-text indexing generally beats title-only indexing for category assignment; one evaluation reported rank-1 correct category of 20-41% with full text, rising to 37-59% when combined. Titles alone lose recall.
    4. Heckman, J., 1979. "Sample Selection Bias as a Specification Error." Econometrica 47(1) [background-knowledge] — When inclusion depends on a variable correlated with the outcome of interest, estimates from the selected sample are biased. A title filter selects chats whose *opening* signals design talk, which over-represents design-first chats and under-represents chats where design input comes up incidentally.
    5. eDiscovery/TAR literature (e.g. Grossman & Cormack 2011, Richmond J. Law & Technology, "Technology-Assisted Review in E-Discovery Can Be More Effective and More Efficient Than Exhaustive Manual Review") [background-knowledge] — Professional document triage validates filters by measuring recall against a sample of the excluded set. Metadata-only culling with no recall estimate is not treated as defensible. (A targeted search for subject-line-only eDiscovery recall returned off-topic results; this point rests on background knowledge.)

  Strength of challenge: Moderate

  Summary: The evidence is mixed on titles in general: for curated documents, titles carry most of the topical signal (Galke et al. 2017). Three conditions weaken that for this presumption. (a) Chat titles are machine-generated from the first exchange and frozen, so they systematically miss content introduced later. (b) "Contains designer input" is a property of who spoke and what they said, not of the topic, so topical title signal is a weak proxy for it. (c) Using the title as the *sole* filter with no recall check leaves an unmeasured false-negative rate, and the misses are biased rather than random. The presumption is not refuted as a precision heuristic. It is challenged as a sole, unvalidated inclusion gate.

  STEELMAN:
    Item: PRESUMPTION-1111
    Strongest counterargument: A chat title is a one-shot, auto-generated summary of how a chat *started*, not of what it *contains*. Designer input often shows up as an aside, a correction or a late redirection inside a chat titled for some other task, and those are exactly the moments a title filter cannot see. Because the filter is the only gate, nothing downstream can recover what it drops, and the corpus built from it will look complete while systematically under-representing incidental design decisions. Even the most favourable title-vs-full-text study still finds a recall loss, and it studied author-chosen titles.
    What would need to be true for C2A2 to be safe: Designer input is concentrated in chats whose opening topic is design (testable), or titles are regenerated or edited to reflect the whole chat, or the title filter is paired with a cheap content check (e.g., keyword or speaker scan) on the excluded set.
    How to test: Draw a random sample (e.g., 50) of chats the title filter *excluded*, read or content-scan them for designer input, and estimate the false-negative rate (recall). Repeat on the included set for precision.

  Specific risks: Designer decisions made in "off-topic" chats never enter the wiki; downstream agents (14a/14b) reason over a biased corpus; coverage looks complete because no excluded item is ever inspected.

  Mitigations available: Recall sampling of the excluded set; two-stage triage (title for priority, content scan for inclusion); speaker/role-based detection where transcripts mark the designer.

  Caveats: Galke et al. is genuine evidence that titles can be strong classifiers. If the observed false-negative rate turns out to be small, the presumption may be acceptable as a cost-saving heuristic. The challenge rests partly on the mechanism of chat auto-titling (vendor/practitioner documentation) rather than on a direct empirical study of chat-title recall, which was not found.

  Search scope: preliminary search (3 searches, 0 fetches); no direct study of chat-title recall located — broader search recommended; independent of 15a.

  Recommendation: PARTIALLY-CHALLENGED
