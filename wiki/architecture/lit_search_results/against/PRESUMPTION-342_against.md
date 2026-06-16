SEARCH-AGAINST-PRESUMPTION-342:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-342
  Original statement: "Vault retrieval recovers the relevant prior thought (unwritten material treated as nonexistent)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-342
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Polanyi, M. (1966). The Tacit Dimension. Doubleday. — The foundational statement: "we can know more than we can tell." All knowledge has tacit roots that resist full externalisation. Knowledge management systems that treat written records as exhaustive capture of knowledge systematically exclude the class of things that are known but cannot be adequately articulated.
    2. OJAKM (2015). "A discussion focusing on Polanyi's Tacit Knowing." Vol. 3(2), pp.100-113. — Reviews Polanyi's theory and its implications for knowledge management, noting that many KM projects premised on externalising tacit knowledge fail to meet objectives because the original theory holds that full externalisation is impossible in principle, not just in practice.
    3. Nickerson, R.S. (1998). "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises." Review of General Psychology. — Documents the streetlight effect (also known as the Einstellung effect or observational selection bias): searchers retrieve what they were looking for rather than what is most relevant, particularly when query formulation is based on prior beliefs. Retrieval systems amplify pre-existing framings rather than correcting them.
    4. Forte, T. (2022). Building a Second Brain. Atria Books. — Acknowledges the core limitation of PKM systems directly: "If you can't find it, it doesn't exist." The book's own framing concedes that retrieval failure is endemic to PKM; the system design addresses only the case where the user knows what they are looking for, not the case where the relevant prior thought was never recorded or its relevance is not yet recognised.
    5. Nonaka, I. (1994). "A Dynamic Theory of Organizational Knowledge Creation." Organization Science. — Distinguishes explicit (codifiable, transferable) from tacit (embodied, contextual) knowledge; shows that knowledge management systems that attempt to operate purely on explicit knowledge suffer systematic loss of context, nuance, and embeddedness that cannot be reconstructed from the record.
    6. arXiv:2603.23530 (2025). "Did You Forget What I Asked? Prospective Memory Failures in Large Language Models." — Demonstrates that LLMs themselves exhibit prospective memory failures — failing to retrieve and act on deferred intentions even when the relevant content is nominally in context — directly relevant to an AI agent whose operational memory is vault retrieval.

  Strength of challenge: Strong

  Summary: The presumption that vault retrieval recovers the relevant prior thought is challenged from two independent directions. First, a Polanyian epistemological argument holds that the class of tacit knowledge — things known but not fully articulable — is systematically excluded from any written vault by design; this is not a retrieval failure but a capture failure, and treating unwritten material as nonexistent does not make the unwritten knowledge disappear, it merely removes it from the system's reach. Second, a retrieval-quality argument holds that even for material that was written, query-based retrieval is subject to the streetlight effect — finding what you were looking for rather than what is most relevant — and to the "unknown unknowns" problem, where the relevant prior thought is not retrieved because the current query does not match its terms. PKM practitioners acknowledge this explicitly; the "if you can't find it, it doesn't exist" design philosophy is a pragmatic concession, not an epistemological claim.

  Specific risks: The vault will act as a confirmation amplifier: agents retrieve material consistent with current framing and miss material that would challenge it. Genuinely novel or anomalous thoughts that were never written down — including the human member's tacit intuitions and the AI's implicit model states — are permanently excluded. Over time, the system's reasoning will converge on what the vault contains rather than on the full space of relevant considerations, producing a narrowing rather than a broadening of intellectual scope.

  Mitigations available: Treat vault retrieval as a starting point rather than a complete search; build in explicit prompts for "what might be relevant that is NOT in the vault?"; maintain a separate log of things-not-yet-written (parking lot notes, voice memos, or structured "tacit capture" exercises); periodically audit retrieval by having an independent agent search the same vault with different query framings and comparing results.

  STEELMAN:
    Strongest counterargument: The principle that unwritten material is treated as nonexistent is not an error but a design choice that enforces discipline: it prevents the system from being paralysed by the unknowable and provides a tractable operational boundary. All knowledge management systems must draw a boundary between what is in scope and what is not; the vault boundary is explicit and consistent. The alternative — treating unwritten knowledge as potentially relevant — introduces an uncontrolled and unverifiable variable that could justify any conclusion.
    What would need to be true for C2A2 to be safe: The vault boundary would need to be explicitly acknowledged as a methodological choice with known limitations, not as a claim about completeness. The system's outputs would need to be hedged by "contingent on vault contents as of [date]" rather than presented as conclusions about the full knowledge space.
    How to test: Select a topic covered in the vault and have the human member articulate their tacit understanding of it verbally (or through free-association); compare that articulation against vault content. A systematic divergence identifies the tacit-explicit gap. Separately, test retrieval recall by planting a known document and querying for it with different formulations; recall failure rate identifies retrieval blindspots.

  Search scope: Searched Polanyi tacit knowledge literature, knowledge management externalization critiques, streetlight/observational selection bias, PKM second brain limitations, and LLM prospective memory failures. Comprehensive for primary challenge directions; additional search on "knowledge base retrieval recall precision in PKM tools" recommended for empirical data.

  Recommendation: CHALLENGED
