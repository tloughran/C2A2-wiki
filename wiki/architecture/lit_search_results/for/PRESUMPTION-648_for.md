SEARCH-FOR-PRESUMPTION-648:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-648
  Original statement: That instrumenting the specific path which failed
    protects the sibling paths that have not yet failed — the blind validator
    on those paths having been bypassed with `|| true` rather than repaired.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-648
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that a guard was added to
        the failed path while the blind validator was suppressed with
        `|| true` rather than fixed
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Defect clustering / Pareto principle in software testing (ISTQB seven
       principles; surveyed in BrowserStack, TestDevLab and TestingDocs
       treatments, 2025-2026). — Supports the weaker reading: defects are not
       uniformly distributed, roughly 20% of modules carry ~80% of defects,
       and historically faulty components predict future faults. Instrumenting
       where a failure occurred is therefore a high-yield placement.
    2. Google Project Zero, 0-day-in-the-wild year-in-review analyses (2022
       cycle; reported via SecurityWeek and SecurityAffairs). — The direct
       counterweight: 17 of 41 exploited 0-days (41%) were variants of
       previously patched issues, and four were variants of the prior year's
       in-the-wild bugs. Where only the observed execution flow was patched
       and the root cause left standing (Windows win32k, Chromium property-
       access interceptor), the same defect was re-reached by a different path.
    3. Google Cloud / Mandiant, 2025. "Look What You Made Us Patch: 2025
       Zero-Days in Review." — Continues the same finding into the current
       reporting period and repeats the recommendation to invest in root-cause
       analysis, variant analysis and patch analysis rather than path-specific
       fixes.
    4. Incident postmortem literature (incident.io, 2025-2026; secportal
       after-action review guidance). — Recommends naming contributing factors
       as system classes (detection gap, control gap, evidence gap) rather
       than as instances, and framing corrective actions so that correct
       behaviour becomes automatic and incorrect behaviour impossible.

  Strength of support: Weak

  Summary: Support attaches to a weaker claim than the one presumed. Defect-
    clustering evidence genuinely backs the proposition that the path which
    just failed is the highest-yield place to spend an instrumentation budget,
    because faults recur where faults have been. It does not back the
    proposition that instrumenting that path confers protection on the paths
    that have not failed — and the variant-analysis evidence contradicts that
    proposition sharply, with roughly two-fifths of exploited 0-days in the
    surveyed period being re-reaches of previously patched defects via
    unpatched sibling routes. The postmortem literature converges on the same
    prescription: remediate the class, not the instance. Nothing located
    supports suppressing a validator with `|| true`; that is a separate move
    for which the CI literature offers only warnings about masking and
    accumulated debt.

  Caveats: The defect-clustering principle is practitioner canon rather than a
    single controlled result, and the specific 80/20 figures are heuristic. The
    variant-analysis evidence is drawn from security vulnerabilities, where an
    adversary actively probes sibling paths; in a non-adversarial setting the
    generalisation failure would surface more slowly but would not be avoided.
    Support would strengthen materially if the sibling paths were shown to
    share no root cause with the failed one.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: defect-class coverage;
    generalisation of post-incident fixes to sibling failure modes; variant
    analysis and incomplete patches; root-cause vs execution-flow patching;
    systemic vs instance-level corrective actions in postmortems; suppression
    of validation in CI pipelines and the masking of failures.
