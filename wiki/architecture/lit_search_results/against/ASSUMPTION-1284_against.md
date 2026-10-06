SEARCH-AGAINST-ASSUMPTION-1284:
  Date searched: 2026-09-09
  Original item: ASSUMPTION-1284
  Original statement: "Two programs treating the same problem as open vs. closed is a strong bridge
    candidate."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1284
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted verbatim from an agent run report (`C2a2 agent hawkins hoffman`, 2026-09-08,
        cross-tradition signals block, Hawkins→Friston on goal decomposition and causality learning).
      15b: Searched for challenging literature (2026-09-09), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Gentner, D. & Toupin, C., 1986. "Systematicity and Surface Similarity in the Development of
       Analogy." Cognitive Science 10(3):277–300.
       [PARTIALLY verified — the paper PDF was retrieved from the Northwestern Gentner lab archive this
       run, but the scan's OCR is unusable for the body text; author list, title, journal and year
       confirmed independently against the Wiley listing (doi 10.1207/s15516709cog1003_2), PhilPapers
       and Semantic Scholar. The findings below are from search-result summaries, NOT from reading the
       paper — treat the numbers as unverified.] — The reported result is the one that matters here:
       transfer accuracy was driven mainly by *transparency* (surface similarity of the corresponding
       objects) and was worst in the **cross-mapped** condition, where similar-looking items played
       different structural roles. Surface resemblance is what drives retrieval; structural
       correspondence is what makes a mapping valid; the two come apart, and they come apart worst
       precisely when the surfaces match but the roles do not. That is the exact shape of a status
       mismatch between two programs.
    2. Wulff, D.U. & Mata, R., 2026. "Escaping the Jingle-Jangle Jungle: Increasing Conceptual Clarity
       in Psychology Using Large Language Models." Current Directions in Psychological Science,
       doi 10.1177/09637214251382083.
       [NOT-verified — the article page was fetched but exceeded the retrieval limit and was not read;
       title, authors, journal, year and DOI confirmed from the publisher listing. The figures below
       are from the search summary.] — Reported: the APA PsycTests database contains 38,000+ constructs
       and 43,000+ measures, most used only infrequently, and conceptual ambiguity is *worsening*.
       The jingle fallacy (same name, different things) and jangle fallacy (different names, same
       thing) are the two standing failure modes of cross-program comparison. A field that has 43,000
       measures for 38,000 constructs cannot be assumed to be using "open" and "closed" to pick out the
       same problem across two programs.
    3. Jingle–jangle fallacy literature more broadly, incl. Lawson & Robins (2021) and its extension
       (PMC12089215), and applications in L2 motivation research (Applied Linguistics 45(4), 2024).
       [NOT-verified — titles/venues seen in search listings only; none opened this run.] — Named to
       mark that this is an active, methodologically formalised literature with published evaluation
       guidelines, not an anecdote. Its whole existence is a standing demonstration that verbal status
       differences between research communities routinely fail to track substantive differences.
    4. Interdisciplinary-communication literature on "problematically ambiguous terms" — Sage,
       *Enhancing Communication & Collaboration in Interdisciplinary Research*, chapter "Conceptual
       Barriers to Interdisciplinary Communication: When Does Ambiguity Matter?"; and the
       boundary-object literature (Star & Griesemer lineage), incl. the Journal of Environmental Studies
       and Sciences work on boundary objects in interdisciplinary practice.
       [NOT-verified — from search snippets; no primary text opened this run.] — Reported findings:
       interdisciplinary projects are "frequently challenged by problematically ambiguous terms" where
       it is not clear which meaning is meant; and boundary objects fail specifically when one
       discipline imposes its own interpretation as mandatory. The literature's diagnosis is that
       apparent disagreements between fields are often disagreements about words, and that the
       expensive failure mode is treating a verbal difference as a substantive one.
    5. Frenkel, A. et al. / Popovic & Kuzmanović-style reviews of entropy misuse: "Researchers in an
       Entropy Wonderland: A Review of the Entropy Concept" (arXiv:1711.07326), and "Entropy and
       Information Theory: Uses and Misuses," Entropy 21(12):1170, 2019.
       [NOT-verified — from search snippets; neither opened this run. Author lists deliberately not
       stated because I could not confirm them.] — Reported: entropy is "used, misused and even abused"
       across disciplines, with contradictions and misconceptions arising from the same term carrying
       different content in different fields. This is the concrete, documented instance of what
       ASSUMPTION-1284 would classify as a bridge: two programs with different status assignments for
       "the entropy problem" — where the difference was largely a difference of definition.
    6. Laudan, L., 1977. *Progress and Its Problems: Towards a Theory of Scientific Growth.* University
       of California Press.
       [NOT-verified — no primary text opened; positions summarised from search results, including
       Bird's criticism that problem-solving as a progress criterion is "regressive".] — Relevance is
       structural rather than evidential: on Laudan's own account, whether a problem counts as *solved*
       is a judgement internal to a research tradition, made against that tradition's own standards of
       what counts as a solution. That makes "solved here, open there" the expected default between two
       traditions, not a signal. The signal-to-noise ratio of the heuristic is therefore unknown and
       plausibly low.

  Strength of challenge: Moderate

  Summary: I found no literature that supports treating a cross-program open/closed status mismatch as
  a *reliable* locator of conceptual gaps, and several literatures that predict it will be dominated by
  noise. The cognitive-science work on analogy is the sharpest: retrieval is driven by surface
  similarity while validity depends on structural correspondence, and the hardest case for human
  reasoners is exactly the cross-mapped one, where the surfaces line up and the roles do not. The
  psychometric literature supplies the base rate — tens of thousands of constructs and measures, with
  jingle and jangle fallacies formalised as standing hazards — meaning that two programs using the same
  problem-name is weak evidence that they are pointing at the same problem. The interdisciplinary-
  communication literature reports that ambiguous shared terms are a *primary* documented cause of
  collaboration failure. And on Laudan's account of problem-solving, "solved" is tradition-internal by
  definition, so a status difference is the null expectation between traditions rather than an anomaly.
  Note carefully what is and is not challenged: nothing I found says status mismatches *never* mark real
  gaps — the analogy literature is explicit that structural mappings can be found when the task supports
  it. What is challenged is the word **strong** in the assumption. The heuristic has no published base
  rate, and every adjacent literature predicts the false-positive rate is high.

  Specific risks: (a) Every CROSS-* item minted since roughly 08-17 rests on this heuristic, so a high
  false-positive rate is not a local error but a systematic contamination of the bridge corpus — the
  cost is paid in analyst attention on bridges that dissolve on inspection. (b) The failure is
  *biased*, not random: jingle fallacies will systematically manufacture bridges where two traditions
  use one word for two things (the C2A2 corpus is dense with exactly these — "inference",
  "representation", "model", "prediction", "free energy", "attention"), while jangle fallacies will
  systematically *hide* real bridges where two traditions use different words for the same thing. The
  heuristic therefore has both a false-positive and a false-negative mode, and the false-negative mode
  is invisible. (c) Documentation habits are a confound the heuristic cannot see: a program that
  maintains an explicit open-problems list (physics, mathematics, parts of ML) will register as "open"
  on any problem it has thought about, while a program with no such convention (contemplative
  traditions, clinical work, most of the humanities-adjacent wikis here) will register as neither open
  nor closed, or as closed by silence. The heuristic will preferentially fire between programs that
  differ in *genre*, not in substance. (d) If a bridge built on a status mismatch is later cited as
  though the mismatch itself were evidence for the bridge, the reasoning becomes circular and the error
  is unrecoverable downstream.

  Mitigations available: (i) Demote the heuristic from *evidence* to *search*: treat a status mismatch
  as a cheap way to generate candidates, and require an independent structural check before any
  candidate is recorded as a bridge. The analogy literature names the check — a role-level mapping, not
  a label-level match. (ii) Add an explicit jingle/jangle screen: before recording a bridge, state what
  each program means by the shared term and check that the two definitions pick out the same object.
  (iii) Record the *genre* of each program's problem-status convention (does it maintain an
  open-problems list at all?) so that mismatches attributable to documentation convention can be
  filtered. (iv) Measure the heuristic in-house — this is the only way to get the missing base rate;
  see the test below. Note that (i)–(iii) are declarative prescriptions and so fall under
  ASSUMPTION-1289's and PRESUMPTION-935's question: without a named owner and a threshold they will
  themselves be unmeasured controls.

  Search scope: Preliminary — 6 queries plus 3 document-retrieval attempts (1 succeeded but with
  unusable OCR, 1 exceeded the retrieval limit, 1 blocked). Literatures touched: cognitive science of
  analogy; psychometrics of construct proliferation; interdisciplinary communication / boundary
  objects; cross-disciplinary concept misuse (entropy/information); philosophy of scientific progress.
  Not covered at primary-source level: scientometric work on "open problem" declarations specifically
  (searched twice; nothing on point returned — this looks like a genuine literature gap), the
  sociology-of-expectations literature on research-agenda rhetoric, and any quantitative study of
  bridge-candidate precision. A broader search would strengthen source quality but I do not expect it
  to change the direction of the finding.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1284
  Strongest counterargument: The heuristic mistakes a property of documents for a property of problems.
  Whether a program calls a problem open or closed is a statement the program makes about itself, in
  its own vocabulary, under its own genre conventions, for its own audience — and the two programs
  being compared do not share any of those three. Analogical reasoning fails in a specific, well
  characterised way: retrieval runs on surface similarity, validity runs on structural correspondence,
  and the worst case for a reasoner is the cross-mapped one where familiar surfaces sit in unfamiliar
  roles. A shared problem-*name* across two traditions is precisely a surface. Psychology, which
  actually measured this, found tens of thousands of constructs and measures and had to formalise the
  jingle and jangle fallacies as named hazards because verbal identity and conceptual identity come
  apart routinely rather than exceptionally. And on the philosophical side the heuristic is asking for
  something the concept cannot supply: on Laudan's account "solved" is a verdict rendered inside a
  research tradition against that tradition's own standards, so two traditions disagreeing about
  solved-ness is the *expected* state of affairs, not an anomaly demanding explanation. Put together:
  the heuristic fires on a signal that is generated by documentation genre, fires hardest where
  vocabularies overlap but roles differ, and has no published base rate anywhere. Calling it "strong"
  is an unmeasured claim about a mechanism, which is the exact pattern ASSUMPTION-1289 flags.
  What would need to be true for C2A2 to be safe: The two programs would have to (a) share an operative
  definition of the problem at the level of roles and relations, not just its name; (b) both maintain
  genuine, maintained problem-status conventions, so that "open" and "closed" are asserted rather than
  inferred from silence; and (c) have the status difference survive a check that it is not an artefact
  of publication genre or of one program simply not having addressed the problem. Where all three hold,
  a status mismatch plausibly is informative. The Hawkins→Friston case may satisfy (a) and (b), since
  both are explicit computational programs with stated agendas — but that is a property of that pair,
  not of the heuristic, and the heuristic is being applied corpus-wide across fifteen traditions where
  most pairs will not satisfy (b) at all.
  How to test: Cheap and in-house, and it produces the base rate that is currently missing. Take every
  CROSS-* item minted on this heuristic since 08-17. For each, have an independent pass state, in one
  sentence each, what problem program A takes itself to have closed and what problem program B takes
  itself to have left open, at the level of the relation rather than the label. Then classify each into
  three bins: (1) same problem, genuine substantive gap; (2) same word, different problems (jingle —
  false positive); (3) same problem, different vocabulary, no actual status difference once translated
  (verbal artefact — false positive). The proportion in bin 1 *is* the heuristic's precision, and it is
  what the word "strong" is currently asserting without evidence. Sample 20 items; that is enough to
  distinguish a precision of 0.8 from one of 0.3. Run the complementary test for false negatives by
  sampling pairs where both programs agree the problem is open and checking how many contain a real
  gap — if that rate is comparable, the mismatch signal is carrying no information at all.
