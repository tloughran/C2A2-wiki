SEARCH-FOR-PRESUMPTION-972:
  Date searched: 2026-09-13
  Original item: PRESUMPTION-972
  Original statement: [inferred] That an empty 30- or 60-day window is evidence about a research
    tradition's activity, rather than about a single source's availability. The Wolfram specialist had to
    argue explicitly that a seven-week silence following a bereavement "reflects that hiatus, not a quiet
    research program."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-972
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the fact that the argument had to be made at all, and from the absence of any
        status in the hunt's vocabulary between active and quiet. Four traditions were read as quiet today
        under that vocabulary.
      15a: Searched bibliometrics and science-of-science for validation of publication cadence as a proxy
        for research activity, and specifically for any validation at the 30–60 day / single-source scale.
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web search across bibliometrics and scientometrics: publication counts as a research-output
    proxy; time-series bibliometric detection of emerging, maturing and declining fields; activity
    classification from publication time series; preprint posting rate as a real-time activity signal
    (COVID-19 as the test case); and publication-lag distributions. **Preliminary, not comprehensive** —
    no systematic database sweep; abstracts read via search summaries rather than fetched articles except
    where noted.

  Supporting evidence found: Partial

  Sources:
    1. "Bibliometric evaluation of research performance: where do we stand?" arXiv:1811.01635 (and the
       companion "How do you define and measure research productivity?" arXiv:1810.12830). — States the
       core supportive proposition directly: research output in the form of publications can be regarded as
       a proxy for research activity, and the literature offers ample justification for using publications
       as a proxy of research output in science and engineering. **SECONDARY** — search-summary level.
       Author attribution not verified (these arXiv numbers are commonly Abramo & D'Angelo); **DO-NOT-CITE
       the authorship** without checking the arXiv record.
    2. Kawamura, T., Yamashita, Y. & Matsumura, K., 2017. "Research Activity Classification based on Time
       Series Bibliometrics." arXiv:1708.01387. — The most on-point source found: builds features from the
       *time series* of an individual researcher's bibliometrics and classifies researchers by those
       features, reporting an F-measure of 80.0% over 114 researchers in two domains (JST data sets). This
       supports the specific idea that publication cadence, not just volume, carries classifiable signal
       about a research programme. **SECONDARY** — abstract via search result; the 80.0% figure is as
       stated in that abstract and has not been independently checked.
    3. "Detecting technological maturity from bibliometric patterns." Expert Systems with Applications
       (2022). — Supports the lifecycle limb: annual time series of scientific publications characterise
       distinct phases — emergence, growth, saturation, decline — and have universal features distinguishing
       emerging from growing technologies. i.e. a *declining* cadence is a recognised, validated signal.
       **SECONDARY**.
    4. OECD, "Artificial Intelligence in Science: What can bibliometrics contribute to understanding
       research productivity?" — Institutional endorsement of the same proxy, with the standard scope
       restriction (acceptable in the hard sciences; not in arts, humanities, much of social science).
       **SECONDARY**.
    5. COVID-19 preprint bibliometrics (e.g. the medRxiv "COVID-19 Preprints and Their Publishing Rate: An
       Improved Method" line of work). — The best available evidence that activity signal can be read on a
       *short* horizon: preprints were ~40% of the English-language COVID corpus early in the pandemic,
       falling to ~28% by mid-August 2020, and coronavirus submission-to-publication time shrank by ~49%.
       Preprint posting rate tracked a field-level activity surge in near-real time. **SECONDARY** — these
       percentages are reported in search summaries and are **DO-NOT-CITE as verified**.

  Strength of support: Weak-to-Moderate

  Summary: The proposition that publication cadence indexes research activity is explicitly endorsed in the
    scientometric literature, is the operating assumption of research-evaluation practice in the hard
    sciences, and has been operationalised well enough that a machine-learning classifier built on
    publication time series can sort researchers at around 80% F-measure. Time-series bibliometrics also
    validates the specific inferential move at issue — that a *falling* cadence marks a field entering
    saturation or decline. So the presumption's general form is supported. What is not supported is its
    applied form. Every validated instance found operates on annual counts, aggregated over fields or over
    a researcher's whole career, with multi-year windows. Nothing found validates a 30- or 60-day window,
    and nothing found validates inferring a *tradition's* state from a *single source's* output.

  Caveats:
    - Scale mismatch is decisive and cuts against the applied claim. The systematic review "Time from
      submission to publication varied widely for biomedical journals" (Current Medical Research and
      Opinion, 2021) reports median submission-to-publication spans ranging from 70 to 558 days across
      journals. A 30- or 60-day observation window is shorter than the *minimum* median lag in that range.
      An empty 30-day window is therefore substantially uninformative about activity even in principle —
      the publishing pipeline does not emit at that granularity. **SECONDARY** (search summary); the
      70–558 range should be re-verified before it is used in an estate document.
    - Unit-of-analysis mismatch. The bibliometric proxy is validated over corpora indexed in WoS/Scopus,
      not over one researcher's feed or one lab's page. The Wolfram specialist's objection is exactly a
      unit-of-analysis objection and the literature does not answer it.
    - The COVID preprint case is the only short-horizon support found, and it is asymmetric: it shows that
      a *surge* is detectable quickly. It says nothing about whether a *silence* is diagnostic. Detecting
      presence and inferring absence are not the same inference and the literature found only supports the
      first.
    - Even the supportive sources carry their own scope restriction (hard sciences only) and the standard
      warning that many bibliometric approaches rest on assumptions that invalidate them as supports for
      management decisions. That warning applies to the hunt's use of the indicator.
    - No source was fetched in full. All five are SECONDARY.

  Recommendation: PARTIALLY-SUPPORTED

NOVELTY-FLAG:
  Item: PRESUMPTION-972
  Searched: Bibliometrics / scientometrics literature on publication counts as activity proxy, time-series
    activity classification, lifecycle-phase detection, and short-horizon preprint signals.
  Finding: No existing literature was found that evaluates a 30- or 60-day empty publication window as a
    classifier of research-programme activity, nor that treats a single source's output as a proxy for a
    research tradition's state. The validated indicators all operate on annual counts over multi-year
    windows and over indexed corpora rather than single sources.
  Implication: The hunt's recency window is operating an indicator outside every regime in which that
    indicator has been validated. Either the window is a genuinely novel short-horizon instrument that
    would need its own validation, or — more likely — it is a scale error. Constructing and validating a
    "silence window" classifier, with an explicit third status between active and quiet for
    source-unavailable, would be an original contribution rather than an application of existing method.
  Recommended status: NOVEL (for the short-window/single-source limb only; the general cadence-as-activity
    limb is well covered by existing literature and is not novel)
