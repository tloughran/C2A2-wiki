SEARCH-FOR-ASSUMPTION-1211:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1211
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 2 of 14 — Priority High
  Original statement: "The trap is durable because the writer assembles a plausible gloss from two
    real neighbouring fields." — offered as the mechanism behind the **fifth** Rohr PRS-03 label trap,
    where "the 'everything belongs' gloss is a splice: that title is the *Source* line of Rohr PRS-01,
    not the content of PRS-03."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1211
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa QC sweep, Day 130 — the first causal account given for a defect
        class previously recorded only as recurring incidents. Recorded as the day's most
        consequential single sentence: it converts the label-trap series from a defect log into a
        hypothesis about the generator, which is a different object of repair than the checks being
        proposed.
      15a: Searched for supporting literature
    Current status: UNTESTED (entering 15a); 15a result SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch was unavailable to this run (the tool refused
    every URL outside the provenance set); an attempt on https://arxiv.org/abs/2604.18880 was blocked
    and is recorded here as a blocked URL. **All sources below are SNIPPET-ONLY.**
    Queries covered: (a) LLM citation hallucination mechanisms, specifically recombination of real
    metadata fields into plausible-but-wrong references; (b) field-level hallucination and its
    localisation in model internals; (c) citation distortion, drift and quotation-error propagation
    in human scholarly literature; (d) analogous support from human memory research — memory
    conjunction errors and source-monitoring errors.
    Assessment: **good coverage, and the mechanism is directly documented.** Limbs NOT covered:
    (i) the retrieval-augmented-generation literature on attribution errors where the retrieved
    passage is correct but the span alignment is wrong — likely a close analogue and unsearched;
    (ii) database/record-linkage literature on field misalignment and column-shift errors during
    ingest, which would speak to whether the splice originates in the writer or upstream in how the
    record was serialised for it; (iii) the specific "adjacent field of the *same* record" variant —
    my queries reached "modify one or more metadata fields of a real reference," which is close but
    not identical.

  Supporting evidence found: Yes

  Sources:
    1. "Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs."
       arXiv:2604.18880. [authors unverified]
       https://arxiv.org/html/2604.18880 · https://arxiv.org/pdf/2604.18880
       — The closest located match to the stated mechanism. Frames citation hallucination as
       **field-level**: hallucinated citations are constructed by taking a real reference and
       modifying one or more metadata fields while preserving overall plausibility and valid citation
       structure. That is the splice hypothesis in the literature's own vocabulary, and the paper
       goes further by localising the behaviour to specific model components — i.e. it treats the
       defect as a property of the *generator*, which is precisely 14a's reframing. Full text was
       BLOCKED to this run (see Search scope); SNIPPET-ONLY.
    2. "BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation."
       arXiv:2604.03159. [authors unverified] https://arxiv.org/pdf/2604.03159
       — Documents the two-mode taxonomy directly relevant here: the model either fabricates a
       non-existent reference, **or cites a real paper with corrupted metadata (wrong authors, title,
       year, venue, DOI)** — references that "look correct at first glance but contain errors in one
       or more bibliographic fields." The second mode is the durable one, and durability-by-
       plausibility is exactly what 14a claims. SNIPPET-ONLY.
    3. "CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text."
       arXiv:2605.27700. [authors unverified]
       https://arxiv.org/pdf/2605.27700 · https://arxiv.org/html/2605.27700v1
       — States the failure profile: LLM-generated references "appear plausible while containing
       corrupted metadata or pointing to papers that do not exist," and that "real-sounding surnames
       from the target field are recombined into author lists that do not correspond to any actual
       paper." Recombination of genuine elements is named as the generative mechanism. SNIPPET-ONLY.
    4. "Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research
       Agents." arXiv:2604.03173. [authors unverified] https://arxiv.org/html/2604.03173v1
       — Extends the finding to agentic/deep-research settings, which is C2A2's operating regime
       rather than the single-turn chat regime. SNIPPET-ONLY.
    5. "Citation Hallucinations." EmergentMind topic page. https://www.emergentmind.com/topics/citation-hallucinations
       — Secondary/aggregator source, cited only for its statement of causal factors:
       over-generalisation, training-data redundancy, and retrieval gaps leading to "probabilistic
       assembly of citation details," with structurally plausible but factually incorrect references
       produced "at alarming rates when operating from parametric memory alone." Low evidential weight
       (not peer-reviewed); included for the phrase "probabilistic assembly," which is the general
       form of the splice claim. SNIPPET-ONLY.
    6. Greenberg, S. A. (2009). "How citation distortions create unfounded authority: analysis of a
       citation network." BMJ.
       https://www.semanticscholar.org/paper/d860c6d3e941e1cb28fd9f899035fb926fba7747
       — Human-authored analogue: shows that a gloss can drift from its source (a qualifier silently
       dropped, a hypothesis upgraded to fact) while the citation apparatus remains intact, and that
       such distortions are *durable* precisely because each link looks sound. Establishes that the
       durability-by-plausibility claim is not specific to machine generation. SNIPPET-ONLY.
    7. Sarol, M. J. et al. (2025). "Automatic Identification of Citation Distortions in Biomedical
       Literature: A Case Study." Proc. Assoc. Inf. Sci. Technol. 62(1), DOI 10.1002/pra2.1281.
       https://jodischneider.com/pubs/asist2025.pdf
       — Recent automated detection work on the Greenberg distortion classes. [co-authors partially
       verified.] SNIPPET-ONLY.
    8. "Source-monitoring error." Wikipedia (entry point to the Johnson/Hashtroudi/Lindsay
       source-monitoring framework). https://en.wikipedia.org/wiki/Source-monitoring_error
       — Analogous support from human cognition: a source-monitoring error is a memory error in which
       the *content* is real but its *source* is misattributed, and such errors "arise due to the
       similarity of the sources." Adjacency of fields within one record is a similarity condition.
       Tertiary source; used as a pointer, not as evidence in itself. SNIPPET-ONLY.
    9. "Observation inflation as source confusion: Symmetrical conflation of memories based on action
       performance and observation." PMC12531383. [authors, journal and year unverified]
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12531383/
       — On memory conjunction errors: "the components of an event are authentic, but the combination
       of those components is false"; details from one memory are "incorrectly incorporated into
       another, forming conjunction errors that elude typical reality monitoring checks"; and
       conjunction errors are **more likely when details are partially rather than fully recombined,
       due to increased plausibility**. This is the strongest analogous support located: it states,
       for a completely independent system, the exact durability mechanism 14a proposes — partial
       recombination of authentic components is more plausible than wholesale fabrication and
       therefore survives checking. SNIPPET-ONLY.
   10. "Feature and Conjunction Errors in Recognition Memory: Evidence for Dual-Process Theory."
       [authors, journal and year unverified]
       https://www.researchgate.net/publication/222132905
       — Background on the conjunction-error paradigm in recognition memory. SNIPPET-ONLY.

  Strength of support: Moderate to Strong

  Summary: The mechanism 14a proposes is documented, named, and currently an active research target.
    The citation-hallucination literature describes exactly this failure mode: a hallucinated
    reference is typically **derived from a real reference by altering one or more fields while
    preserving structural plausibility** (source 1), and models "recombine" genuine elements —
    real surnames, real titles, real venues — into combinations that correspond to no actual record
    (3). Recent work treats this as *field-level* hallucination and localises it inside the model,
    which corroborates 14a's key move of reframing a defect log as a hypothesis about the generator
    (1). The durability half of the claim is separately supported from two directions: the
    citation-hallucination papers note that such references "look correct at first glance" and pass
    casual inspection (2), and the memory literature supplies an independent-system analogue in which
    partial recombination of authentic components is *more* likely to survive monitoring than full
    fabrication, precisely because it is more plausible (9). Greenberg's citation-network analysis
    shows the same durability in human-authored literature: distortions persist because each
    individual link resolves and reads as sound (6).

  Caveats: (1) All sources SNIPPET-ONLY; several are 2026 arXiv preprints whose authorship I could
    not verify and which have not been through review. Weight accordingly. (2) **Domain transfer is
    the main limitation.** The literature concerns *bibliographic* fields of *external* references
    (author, title, year, venue, DOI). 14a's case is a splice between fields of an *internal wiki
    record* — the Source line of PRS-01 borrowed as the content gloss for PRS-03. The structural
    analogy is close and the causal story is the same (adjacent, similar, co-occurring fields of a
    real record), but I found no source that studies internal-record field splicing directly. (3) The
    literature is largely descriptive and benchmark-oriented; it establishes that the mechanism
    occurs, not that it is the mechanism in *this* five-instance series. Confirming that requires an
    internal test — e.g. checking whether each of the five traps is traceable to a specific adjacent
    field, which for the Rohr case 14a has already done once. (4) Source 5 is an aggregator page and
    source 8 is an encyclopaedia entry; neither is primary evidence. (5) Publication-bias note: the
    2026 arXiv corpus on citation hallucination is large and fast-moving, and detection/mitigation
    papers have a structural incentive to characterise the defect vividly. The *existence* of the
    mechanism is nonetheless attested across independent groups.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1211
    Supported sub-claims: (i) that generators produce plausible-but-wrong attributions by modifying
      or recombining fields of *real* records rather than fabricating from nothing; (ii) that this is
      a field-level phenomenon with identifiable internal correlates in the model; (iii) that partial
      recombination of authentic components is *more* durable than outright fabrication because it is
      more plausible — attested independently in human memory research; (iv) that such defects survive
      resolution-based checking (see also PRESUMPTION-877_for.md).
    Unaddressed sub-claim: **the specific case of a splice between two adjacent fields of the same
      internal record in a self-authored knowledge base** — e.g. a Source line read as content. All
      located work concerns external bibliographic metadata. C2A2's five-instance label-trap series
      is, so far as this search found, an undescribed variant, and it has a property the published
      cases lack: the "correct" value is present in the same corpus, one field away, which makes it
      unusually cheap to test and to detect automatically (compare each gloss against the sibling
      fields of neighbouring records in the same file).
    Implication: the *mechanism* is not novel and should not be treated as an original contribution;
      the *instance class* and a field-adjacency detector for it may be.
