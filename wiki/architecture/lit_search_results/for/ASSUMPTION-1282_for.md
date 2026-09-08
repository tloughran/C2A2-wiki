SEARCH-FOR-ASSUMPTION-1282:
  Date searched: 2026-09-08
  Original item: ASSUMPTION-1282
  Original statement: "The fix for this class of problem is procedural and external, not declarative and
    internal; a system that accepts declarations in lieu of procedure will tend to produce more of the
    thing declared, not less."
  Routed question (as narrowed by 14a): does the human-disclosure finding survive when the "reader" is
    an automated downstream agent and the annotation is a structured machine-readable tag rather than
    prose? The human-disclosure sources (Cain/Loewenstein/Moore, Sumner 2014 etc.) were read in the
    09-07 cycle and were NOT re-searched this run.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1282
    Item type: ASSUMPTION (stated — quoted from an agent-authored SYSTEMIC-RISK-FLAG, 2026-09-07,
      "declaration-substitutes-for-procedure," High, filed by the delegated 15b subagent on
      ASSUMPTION-1274 / PRESUMPTION-918)
    Transform at each step:
      14a: Extracted verbatim; narrowed the routed question to the machine/pipeline generalisation,
        since the human-case sources were read in the 09-07 cycle and should not be re-searched.
      15a: Searched for supporting literature (2026-09-08), FOR direction only, machine-transfer case.
    Current status: SUPPORTED (limb 1); PARTIALLY-SUPPORTED (limb 2)

  Supporting evidence found: Yes

  Note on structure: the statement has two limbs, and the evidence found is asymmetric between them.
    LIMB 1 — a declarative annotation alone does not change downstream behaviour; procedure/enforcement
      is what changes it.
    LIMB 2 — a system that accepts declarations in lieu of procedure produces MORE of the declared thing
      (i.e. the annotation proliferates while the underlying condition worsens or is unaffected).
    Limb 1 transfers to the machine case with strong support. Limb 2 transfers with partial support.

  Sources:
    1. Longpre, S. et al. (Data Provenance Initiative), 2023/2024. "The Data Provenance Initiative: A
       Large Scale Audit of Dataset Licensing & Attribution in AI," arXiv:2310.16787; published as "A
       large-scale audit of dataset licensing and attribution in AI," Nature Machine Intelligence, 2024,
       DOI 10.1038/s42256-024-00878-8.
       [VERIFIED: title, arXiv id, Nature MI venue and DOI via nature.com and arXiv listings retrieved
       this run; the audit figures below from search-result summaries of the paper and the DPI project
       page. FULL TEXT NOT READ — ABSTRACT/SUMMARY-LEVEL ONLY] — 1,858 datasets across 44 popular
       finetuning collections. Reported licence OMISSION rates of >70% and licence ERROR rates of >50%
       on popular dataset hosting sites. CLAIM RESTING ON THIS SOURCE (summary-level): a structured,
       machine-readable qualifier (a licence field) attached at the point of publication is, in the
       majority of cases, absent or wrong by the time an automated downstream consumer reads it. Limb 1,
       machine case, direct.
    2. Longpre, S. et al., 2024. "Consent in Crisis: The Rapid Decline of the AI Data Commons."
       arXiv:2407.14933; NeurIPS 2024 Datasets and Benchmarks Track.
       [VERIFIED: title, arXiv id, NeurIPS 2024 D&B track acceptance via neurips.cc poster page,
       papers.nips.cc hash page and OpenReview listing retrieved this run; findings from search-result
       summaries. FULL TEXT NOT READ — ABSTRACT/SUMMARY-LEVEL ONLY] — Longitudinal audit of 14,000 web
       domains underlying C4, RefinedWeb and Dolma. robots.txt is precisely the case the routed question
       asks about: a structured machine-readable declaration whose reader is an automated agent. The
       paper reports "general inconsistencies between websites' expressed intentions in their Terms of
       Service and their robots.txt," and diagnoses these as "symptoms of ineffective web protocols, not
       designed to cope with the widespread re-purposing of the internet for AI." Limb 1, machine case:
       the declarative channel does not carry the intent, and the authors' own remedy language is
       protocol/procedural rather than annotational. NOTE: I did not read the sections that would
       establish whether crawlers actually *honour* the tags — the reported finding I am relying on is
       declaration-vs-intent divergence, not measured non-compliance.
    3. Sawant, A.A., Robbes, R., Bacchelli, A., 2016/2018. "On the reaction to deprecation of 25,357
       clients of 4+1 popular Java APIs" (ICSME 2016), extended as "On the reaction to deprecation of
       clients of 4 + 1 popular Java APIs and the JDK," Empirical Software Engineering.
       [VERIFIED: titles, authors (Sawant with Robbes; co-authorship confirmed via Semantic Scholar
       listing), venues via ICSME'16 author-hosted PDF listing (anandsaw.github.io), Semantic Scholar
       and ResearchGate records retrieved this run; the quoted finding from search-result summaries.
       FULL TEXT NOT READ — SUMMARY-LEVEL ONLY] — The `@Deprecated` annotation is the cleanest
       machine-readable-tag-with-machine-reader case in software: the compiler consumes the tag and
       emits a warning automatically. Across 25,357 client projects, maintainers largely did not migrate
       as long as execution was not broken; the reported conclusion is that "the deprecation mechanism
       is not achieving its stated goal" and that "simple compiler warnings for deprecation might not be
       sufficient." Limb 1, direct: a structured tag, automatically propagated by a machine, does not by
       itself change downstream behaviour. Behaviour changes when the artefact *breaks* — i.e. when the
       gate is procedural.
    4. Static-analysis warning suppression and non-blocking CI checks. Two items:
       (a) an empirical study of suppressed static-analysis warnings (FSE 2025; software-lab.org PDF and
       ACM PACMSE listing DOI 10.1145/3715729) and (b) "Quieting the Static: A Study of Static Analysis
       Alert Suppressions," arXiv:2311.07482.
       [VERIFIED: titles, venues, DOI/arXiv identifiers via ACM DL, software-lab.org and arXiv listings
       retrieved this run. AUTHORS NOT VERIFIED — I did not open either paper, and I am deliberately not
       naming authors I have not confirmed. FINDINGS ARE SEARCH-SUMMARY LEVEL ONLY — WEAK] — The
       reported findings I am relying on: 56% of SAST warnings in a corpus of 30 open-source Java
       projects were never addressed in project history; CI builds "almost never fail due to a potential
       bug detection by a static analyzer," because developers do not configure analysers to break
       builds. This is the blocking-versus-advisory distinction stated directly: the same finding,
       delivered advisorily, is ignored; delivered as a build break, it is not. Supports limb 1 and, via
       the growth of suppression annotations, is the closest thing found to limb 2 in a software
       pipeline — the declarative channel accumulates *more* declarations (suppressions) rather than
       fewer defects. I flag that I have not read enough to assert the suppression-growth trend as fact.
    5. Retraction metadata and downstream propagation. Two items, treated together:
       (a) "Reducing the Inadvertent Spread of Retracted Science: recommendations from the RISRS
       report," PMC9483880; (b) "Propagation of errors in citation networks: a study involving the
       entire citation network of a widely cited paper published in, and later retracted from, the
       journal Nature," PMC5793988.
       [VERIFIED: titles and PMC identifiers via search results retrieved this run. FULL TEXT NOT
       RETRIEVED for either — the PMC fetch returned a reCAPTCHA interstitial. Authors, years and
       journals NOT verified. Findings are search-summary level only — WEAK] — The reported RISRS
       finding I am relying on: although many databases flag retracted papers, "many systems that
       aggregate scholarly influence do not discount citations from such articles, nor do they always
       notify downstream users of a paper's retracted status," and citation software developers are
       *recommended* to add retraction flags, with only partial adoption. This is the archetypal
       machine-readable qualifier (Crossref retraction metadata) with automated downstream readers
       (indexes, reference managers) failing to act on it. Limb 1, machine case, by analogy from the
       scholarly-record pipeline.

  Strength of support: Moderate — verified at the level of citation identity and reported headline
    findings, not at the level of read primary text. The direction of the evidence is consistent across
    five independent domains (AI dataset licensing, web crawl consent protocols, Java API deprecation,
    static analysis in CI, scholarly retraction metadata), which is what carries the weight; no single
    source is strong enough on its own at the verification level I achieved.

  Summary: The transfer condition the SYSTEMIC-RISK-FLAG did not state does appear to hold for limb 1.
  In five independent machine-pipeline settings, a structured, machine-readable qualifier attached at
  the point of origin fails to change what the automated downstream consumer does: licence fields are
  omitted >70% of the time and wrong >50% of the time in the datasets AI systems are actually finetuned
  on (Longpre et al.); robots.txt declarations diverge from the stated intentions they are supposed to
  encode, which the authors attribute to protocol inadequacy rather than to inadequate annotation
  (Consent in Crisis); the `@Deprecated` tag, machine-emitted as a compiler warning, does not move
  25,357 client projects until something actually breaks (Sawant et al.); static-analysis findings are
  overwhelmingly unaddressed precisely where the check is advisory rather than build-breaking; and
  retraction flags, the best-standardised machine-readable qualifier in the scholarly record, are not
  acted on by the downstream aggregators that ingest them. The consistent shape across all five is the
  assumption's own shape: the annotation exists, the machine reads it, and nothing procedural is
  attached to it, so nothing downstream changes. Limb 2 — that the system produces *more* of the
  declared thing — has only one candidate line of evidence in the machine case (accumulating suppression
  annotations in static analysis), and I did not verify it to the standard required to assert it.

  Caveats:
  (a) VERIFICATION LEVEL IS THE MAIN WEAKNESS OF THIS RESULT. Not one of the five sources was read in
      full text this run. Sources 1, 2, 3 are verified as existing publications in the venues named,
      with headline findings taken from search-result summaries; sources 4 and 5 are verified only as
      titles/identifiers, with authors deliberately left unnamed rather than guessed. Per REVISE-437
      every substantive claim above is tagged with the specific source it rests on. This result should
      be re-run at full-text level before it is allowed to bear weight on REVISE-437/438.
  (b) LIMB 2 IS NOT ESTABLISHED IN THE MACHINE CASE. "Will tend to produce more of the thing declared"
      is the interesting and load-bearing half of the assumption — it is what makes the declaration
      actively harmful rather than merely inert. In the human-disclosure literature it has a mechanism
      (moral licensing / strategic exaggeration after disclosure). I found no machine-pipeline study
      that measures qualifier *proliferation* alongside outcome *deterioration*. The five sources above
      support inertness, not perversity.
  (c) A COMPETING READING SURVIVES ALL FIVE SOURCES. Every case above is also consistent with "the
      annotation was under-specified, under-adopted, or badly tooled" rather than "declarative
      annotation is the wrong category of fix." Longpre et al.'s own remedy is better provenance
      standards; the RISRS recommendation is to add *more* flags to reference managers. If the
      literature's own authors respond to these findings by improving the declarative layer, that is
      evidence against reading their findings as a case for abandoning it. 15b will likely press this.
  (d) DOMAIN DISTANCE. C2A2's case is a provenance chain read by an LLM agent, not a compiler or a
      crawler. None of the five sources involves an LLM reader, whose failure modes (attention to
      salient text, instruction-following on prose caveats) may differ in both directions from a
      compiler's. The transfer is one domain closer than the human-disclosure sources, not all the way.
  (e) SEARCH SCOPE. Preliminary — broader search recommended. Five queries in this direction. The
      W3C PROV / provenance-attrition line named in 14a's Search hint was searched and returned nothing
      usable: I found no empirical study of downstream consumption of PROV qualifiers. Taint tracking
      and label propagation were NOT searched. FAIR-data qualifier attrition was NOT searched. The
      question of whether structured caveats propagate BETTER than prose caveats — Sumner 2014's
      mechanism run in a machine pipeline — was not answered by anything I found, and may be a genuine
      gap.

  Recommendation: PARTIALLY-SUPPORTED
    (limb 1 — declarative annotation alone does not move an automated downstream reader: SUPPORTED,
     Moderate, five independent domains, verification level low;
     limb 2 — declarations proliferate and worsen the thing declared: NO-SUPPORT-FOUND in the machine
     case.)

  NOVELTY-FLAG (partial):
    Item: ASSUMPTION-1282, limb 2, machine-transfer case
    Searched: five queries across machine-readable provenance, robots.txt/consent protocols, API
      deprecation annotations, static-analysis suppression, and retraction metadata propagation.
    Finding: No literature found that measures whether a machine-readable qualifier regime *increases*
      the incidence of the condition it annotates. The inertness finding is well attested; the
      perversity finding is not, in the machine case.
    Implication: If C2A2 can measure qualifier proliferation against outcome deterioration in its own
      provenance chain, that would be an original contribution — and it is a measurement C2A2 is
      unusually well placed to make, since it holds both the tag counts and the outcome register.
    Recommended status: NOVEL (limb 2 only)
