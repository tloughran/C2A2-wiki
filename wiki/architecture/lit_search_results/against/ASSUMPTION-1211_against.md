SEARCH-AGAINST-ASSUMPTION-1211:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1211
  Queue ref: LIT-QUEUE — 2026-08-25 (14a + 14b end-of-day intake cohort), Priority High
  Original statement: "The trap is durable because the writer assembles a plausible gloss from two
    real neighbouring fields." — offered as the mechanism behind the fifth Rohr PRS-03 label trap,
    where "the 'everything belongs' gloss is a splice: that title is the *Source* line of Rohr PRS-01,
    not the content of PRS-03."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1211
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa QC sweep, Day 130. Recorded as the day's most consequential single
           sentence: it converts the label-trap series from a defect log into a hypothesis about the
           generator, which is a different object of repair than the checks being proposed.
      15b: Searched for challenging literature. Four WebSearch queries covering LLM citation-
           hallucination mechanisms and field-level failure, human citation copying and error
           propagation, citation distortion/drift, and the methodology of single-incident causal
           attribution.
    Current status: PARTIALLY-CHALLENGED

  Search scope: Four WebSearch queries, executed 2026-08-26. Coverage reached: the 2024–2026 arXiv
    literature on citation hallucination in LLMs, including one mechanistic-interpretability paper on
    field-level hallucination; the scientometric literature on citation copying and misprint
    propagation; Greenberg's citation-distortion framework; and general incident-analysis literature on
    single-cause attribution. All sources read as search-result snippets only — **no full text or
    abstract was fetched**; all are marked SNIPPET-ONLY. NOT COVERED, and these matter for this item:
    (a) the retrieval-augmented-generation literature on *grounded* attribution error, which is the
    closest match to a writer working from a structured record set it can actually see — the papers I
    reached are mostly about closed-book fabrication, a different regime; (b) any paper testing the
    specific "splice of two adjacent fields of neighbouring records" hypothesis, which I did not find
    and may not exist; (c) the human-factors literature on transcription and copy errors in structured
    data entry, which would be the non-LLM analogue; (d) prompt- and context-window-level explanations
    (e.g. truncation, chunk-boundary effects) which are a competing mechanism I could not search for.
    This search is therefore adequate to show that the mechanism is under-determined, and inadequate to
    say which mechanism is right.

  Challenging evidence found: Partial

  Sources:
    1. [authors unverified] 2026. "Where Fake Citations Are Made: Tracing Field-Level Hallucination to
       Specific Neurons in LLMs." arXiv:2604.18880. https://arxiv.org/html/2604.18880 — The closest
       thing to a direct test of the assumption's mechanism, and it cuts both ways. It confirms that
       hallucination is *field-level* rather than whole-reference ("references often look correct at
       first glance but contain errors in one or more bibliographic fields") and that "author names
       fail far more often than other fields across all models and settings." But it locates the
       generative cause in specific neurons and in token-space overlap between records — "when multiple
       highly cited records overlap in token-space (similar titles/authors), internal retrieval can
       produce hybrid or contaminated bibliographic outputs — mixing details of different real papers."
       That is a *similarity*-driven account, not an *adjacency*-driven one. It challenges the C2A2
       hypothesis in its specifics: the predicted confusion partner is the most token-similar record,
       not the neighbouring one. In this corpus PRS-01 and PRS-03 of the same thinker are both adjacent
       *and* similar, so the observed instance does not discriminate between the two accounts.
       SNIPPET-ONLY.
    2. [authors unverified] 2026. "BibTeX Citation Hallucinations in Scientific Publishing Agents:
       Evaluation and Mitigation." arXiv:2604.03159. https://arxiv.org/pdf/2604.03159 — Independent
       evidence that the failure is distributed across bibliographic fields in agent pipelines
       generally, i.e. it is a property of the generation regime rather than of any particular record
       layout. Weakens the claim that this corpus's field adjacency is what makes the trap durable.
       SNIPPET-ONLY (title and framing).
    3. [authors unverified] 2026. "LLM hallucinations in the wild: Large-scale evidence from
       non-existent citations." arXiv:2605.07723. https://arxiv.org/abs/2605.07723 — Documents the
       *other* major failure regime — references that do not exist at all — at large scale. Relevant as
       a boundary condition: the C2A2 defect class is the resolvable-but-wrong kind, and this paper's
       regime is the non-resolvable kind, so results from the fabrication literature should not be
       imported wholesale into the C2A2 mechanism story. SNIPPET-ONLY (title only).
    4. Simkin, M.V. and Roychowdhury, V.P. 2005 [year and exact venue unverified], as reported in
       "The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research,"
       arXiv:2502.20581. https://arxiv.org/pdf/2502.20581 — Supplies a rival mechanism with a long
       empirical track record and no LLM in it: modelling misprint propagation in physics
       bibliographies, they "estimated that 70–90% of citations are copied from other papers' reference
       lists." Broadus (1983) [via the same source] found 23% of citing papers reproduced an identical
       bibliographic error from a well-known work; Kaplan (1965) [via the same source] raised the
       question of citations "simply lifted from the bibliography in someone else's work." If the
       dominant human mechanism for durable plausible-but-wrong attribution is *copying an existing
       wrong reference forward*, then a five-instance recurrence in a corpus that quotes itself is at
       least as well explained by propagation as by fresh splicing — and the two make different repair
       predictions. SNIPPET-ONLY; all three secondary attributions are as reported by arXiv:2502.20581,
       not verified against the originals.
    5. Greenberg, S.A. 2009. "How citation distortions create unfounded authority: analysis of a
       citation network." BMJ. https://pubmed.ncbi.nlm.nih.gov/19622839/ — Names three distinct
       mechanisms by which a claim becomes durably attached to a source that does not support it:
       *citation bias*, *amplification* (acceptance growing through citation of secondary sources
       rather than direct evidence), and *invention* (authors altering the nature of the claim and its
       evidence). "Amplification" in particular predicts durability without any splicing: the gloss
       becomes durable because later references cite the earlier gloss rather than the record. This is
       a competing full explanation of the observed durability. SNIPPET-ONLY.
    6. General incident-analysis literature on single-cause attribution — e.g.
       https://oneuptime.com/blog/post/2026-07-31-root-cause-vs-contributing-factors/view and
       https://en.wikipedia.org/wiki/Root-cause_analysis — "a failure can have many branches and
       depending on which branch you follow, you end up at a different root cause"; OSHA guidance that
       investigations "should not stop at a single triggering factor" and that there is often more than
       one root cause; NASA's framework distinguishing proximate, intermediate and root causes
       alongside contributing factors. This is methodological rather than substantive challenge, but it
       is the relevant challenge: the assumption is a monocausal mechanism inferred from one worked
       instance within a five-instance series, offered as *the* reason the trap is durable. SNIPPET-ONLY
       and low-grade sources (practitioner blogs and an encyclopaedia entry) — flagged as such; I did
       not reach the primary human-factors literature (Dekker, Hollnagel) that makes this argument
       properly.
    7. Counter-note against my own challenge, recorded for honesty: source 1's core finding — that
       hallucination is field-level, and that hybrid outputs mix details of *different real* records —
       is substantially what ASSUMPTION-1211 asserts. On the general shape of the mechanism the
       literature agrees with 14a. The challenge below is confined to the specific causal claim
       (adjacency, and "because" as the reason for durability) and to the inferential base.

  Strength of challenge: Moderate — but note what kind. No source contradicts the assumption; the
  challenge is that the mechanism is under-determined against two named rivals with different repair
  implications, and that its inferential base is one worked instance. On the graded recommendation
  scale that is WEAKLY-CHALLENGED, not CHALLENGED: the assumption survives, its exclusivity does not.

  Summary: This is a case where the literature partly agrees with the assumption and undercuts it in
  three specific places. It agrees that generators produce references that are wrong at the level of
  individual fields while remaining plausible and resolvable, and that hybrid outputs mixing details of
  two real records are a documented phenomenon. It undercuts the claim in the following respects.
  First, the best mechanistic account available attributes hybridisation to *token-space similarity*
  between records rather than to structural *adjacency* of fields; the Rohr instance cannot
  discriminate, since PRS-01 and PRS-03 of the same thinker are both. Second, the assumption explains
  durability by the splice, but the scientometric literature offers a well-attested rival account of
  durability that needs no splicing at all — copying. Estimates that 70–90% of citations are lifted
  from other reference lists, and Greenberg's "amplification," both predict that a wrong gloss persists
  because subsequent uses cite the gloss rather than the record. In a corpus that cites itself, that
  mechanism is available and was not considered. Third, the claim is a monocausal mechanism inferred
  from a single worked instance and offered as the explanation of a five-member series; standard
  incident-analysis guidance warns specifically against stopping at the first triggering factor,
  because different branches yield different root causes and therefore different repairs. Rated
  Moderate: the assumption is not contradicted, it is under-determined, and the alternatives have
  different repair implications — splicing points at the writer's record layout, copying points at the
  corpus's self-citation, similarity points at record naming.

  Specific risks: (a) Repair misdirection is the principal risk and it is concrete: if the mechanism is
  similarity rather than adjacency, the fix is disambiguating record titles; if it is propagation, the
  fix is finding and retracting the first instance and every citation of it; if it is adjacency, the
  fix is the writer's field-assembly step. These are three different pieces of work and the assumption
  selects one. (b) A monocausal account offered with the authority of a mechanism can close inquiry on
  a series that is still open — 14a's own note records this as "the day's most consequential single
  sentence," which is precisely the status at which under-determination becomes expensive. (c) If
  propagation is operative, then the five instances are not five independent generator events but one
  event with four descendants, and the corpus contains an unknown number of further descendants that
  no per-instance check will find. (d) If similarity is operative, the defect rate should scale with
  the number of same-thinker PRS records, so the trap will get worse as the corpus grows — a scale
  failure that the adjacency account does not predict. (e) The assumption inherits ASSUMPTION-1206's
  and PRESUMPTION-877's problem: every splice of this kind resolves, so no resolution-based check will
  ever quantify the class the mechanism is a mechanism for.

  Mitigations available:
    - Test the three accounts against each other on data already held. They make different predictions
      about which records get confused; see the test protocol below. This is the cheapest available
      discriminator and requires no literature.
    - Treat the mechanism as a hypothesis with a status field, not as a finding. The register already
      distinguishes stated from inferred; a mechanism inferred from n=1 within a series of 5 should
      carry that inferential base on its face.
    - Search the corpus for descendants of each known bad gloss before repairing the instance. If the
      copying account has any purchase, per-instance repair leaves the population intact.
    - Where record titles within a thinker are token-similar (PRS-01/PRS-02/PRS-03 of the same author),
      the similarity account predicts confusion; disambiguating identifiers or requiring the writer to
      quote the record's own id alongside its gloss would suppress it regardless of which account is
      right, and is a cheap dominant strategy.
    - Note that a single further worked instance, analysed for *which* record supplied the wrong field,
      would materially discriminate. The series has five members and only one has been analysed.

  STEELMAN:
    Item: ASSUMPTION-1211
    Strongest counterargument: The rival mechanisms I have raised are largely drawn from a setting
    unlike this one. Simkin and Roychowdhury, Broadus and Greenberg all describe *human authors* moving
    references between *published papers* over years, where copying from a bibliography is the cheap
    path and the original is expensive to obtain. In C2A2 the writer has the records in front of it,
    obtaining the original costs nothing, and the five instances arise inside a single generation
    regime rather than across a literature. Meanwhile the mechanistic paper I cite as a challenge in
    fact reports exactly the phenomenon 14a named — hybrid outputs assembled from the fields of two
    real records — and the difference between "adjacent" and "token-similar" is not a difference the
    Rohr instance was ever claiming to adjudicate; 14a said the gloss came from the *Source* line of
    PRS-01, which is a specific, checkable, and apparently correct claim about that instance. Demanding
    that a first causal account also rule out every alternative before it may be recorded sets a
    standard that would have prevented the account being offered at all — and the register's own note
    says this is the first causal account the series has received in five instances.
    What would need to be true for C2A2 to be safe: (i) the account must be held as a hypothesis about
    the *series* rather than a finding about the instance — the instance claim looks sound; (ii) at
    least one more of the five instances must be traced to its source field, so the account rests on
    more than one datum; (iii) the corpus must not be self-citing in a way that lets a bad gloss
    propagate — this is checkable and has not been checked; (iv) if the repair chosen is at the
    writer's field-assembly step, it must be one that also suppresses the similarity and propagation
    routes, or the choice among accounts must be made first; (v) the mechanism must not be quoted
    forward as established, since it entered the register as a single sentence in a QC sweep.
    How to test: For each of the five known label-trap instances, record (a) which record supplied the
    wrong content, (b) that record's *position* relative to the correct one in the source layout, and
    (c) its *token similarity* to the correct one. The three accounts make separable predictions: the
    splice account predicts positional adjacency dominates; the similarity account predicts token
    overlap dominates and position is incidental; the propagation account predicts that the wrong gloss
    appears verbatim in an earlier artefact that the later ones could have copied, in which case the
    first instance chronologically is the only true generator event. Then grep the corpus for the exact
    string of each bad gloss: if it appears more times than there are known instances, propagation is
    live and per-instance repair is insufficient. All three tests run against files already on disk.

  Recommendation: WEAKLY-CHALLENGED
