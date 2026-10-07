SEARCH-FOR-PRESUMPTION-896 (OWED LIMBS ONLY — remediation rate; moral-licensing replication status):
  Date searched: 2026-10-07
  Original item: PRESUMPTION-896
  Original statement: [inferred] Filing a defect discharges the obligation to fix it, in a case where the fix
    was already computed.
  DIRECTION NOTE (carried from cycle 0): the item is a presumption filed as unsafe. "Support" here means
    literature supporting 14b's finding that filing can stand in for fixing, i.e. that filed defects often
    go unremediated and that the act of filing/disclosing can license non-action.
  Limbs searched: (1) remediation-rate literature: what fraction of filed software defects / static-analysis
    warnings are ever fixed; (2) replication status of the moral-licensing evidence. Owed per 15d
    re-trigger 2026-09-20 (MONITOR-585). Not searched: whether C2A2 has a downstream remediation stage
    with measured throughput. That is in-house and is the actual discriminator per MONITOR-585.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-07)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-896
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption: a computed fix was filed rather than applied
      15a (cycle 0, 2026-08-31): PARTIALLY-SUPPORTED (Moderate). Two queries under the reserved-budget
        protocol. One on-point peer-reviewed moral-licensing source (boardroom disclosure, J. Bus. Ethics)
        plus vulnerability-backlog trade sources.
      15c: DISPOSITION-875 → MONITOR-585 (symmetric partials; deliberately under-searched)
      15d: re-triggered cycle 1 2026-09-20; owed = remediation-rate literature + licensing replication check
      15a (cycle 1, 2026-10-07): 3 searches, 2 fetches on the owed limbs; see below
    Current status: PARTIALLY-SUPPORTED

  Search scope: 3 web searches (static-analysis warning fix rates; bug-report never-fixed proportions;
    moral-licensing meta-analysis/replication). 2 fetches (Kuper & Bott 2019 landing page with abstract;
    Li & Yang arXiv:2210.02651 HTML, introduction and abstract read, body not read in full). One intended
    fetch (arXiv abs page for the Coverity study) was blocked by the fetch tool's provenance gate and not
    retried. Preliminary scope; broader search recommended only on limb (1).

  Supporting evidence found: Partial

  Sources:
    1. Kuper, N. & Bott, A., 2019. "Has the evidence for moral licensing been inflated by publication
       bias?" Meta-Psychology 3. doi:10.15626/MP.2018.878. [fetched, abstract level] Prior meta-analyses
       give d > .30. After PET-PEESE and 3-PSM correction the effect falls to d = -0.05 (n.s.) and
       d = 0.18 (p = .002). The authors conclude that both the evidence for the effect and its size "has
       likely been inflated by publication bias". THIS WEAKENS the cycle-0 mechanism. It is reported here
       because the owed question was replication status, and the honest answer is "contested, with a small
       residual effect at best".
    2. Blanken, I., van de Ven, N., Zeelenberg, M. & Meijers, M. H. C., 2014. "Three attempts to replicate
       the moral licensing effect." Social Psychology. [search-result] Three replications of Sachdeva et
       al. (2009), including an MTurk sample of N = 940, did not reproduce the effect. Same direction as (1).
    3. Coverity usage study, "How Do Developers Act on Static Analysis Alerts? An Empirical Study of
       Coverity Usage" (Microsoft Research listing). [search-result; full text NOT read] Five OSS projects
       (Linux, Firefox, Samba, Kodi, oVirt-engine) with ≥5 years of Coverity use. Actionable alerts were
       27.4–49.5% (median 36.7%). Fixes were small (median 4 LOC) but took 36–245 days (median 96).
       Supportive on the "filed ≠ fixed promptly" limb: even cheap, already-localised fixes sit for months.
    4. Li, J. & Yang, J., "Tracking the Evolution of Static Code Warnings: the State-of-the-Art and a
       Better Approach." arXiv:2210.02651v2. [fetched, abstract and introduction] States that static
       detectors report warnings "far beyond what resources are allowed to resolve" and that "a
       significant portion of static code warnings remain unresolved by developers". Also notes that
       integrating warnings into code review/CI raises response rates, i.e. routing to a stage with an owner
       matters. That point bears directly on MONITOR-585's "downstream stage exists?" test.
    5. Eclipse/Mozilla bug-resolution studies (Anvik et al. 2005 UBC TR-2005-20; "Not All Bug Reports Get
       Fixed", Making Software ch. 24; Eclipse longitudinal analyses). [search-result] Roughly 18–20% of
       Eclipse bugs end WONTFIX. Only 58% (Eclipse) and 44% (Firefox) of reports were in OPEN/FIXED states
       that could lead to code change. Supportive in a general way: a material fraction of filed defects is
       never remediated. Note that much of the shortfall is triage (invalid/duplicate), not neglect of
       valid defects.

  Strength of support: Moderate on limb (1) (filed defects are frequently not fixed, or fixed slowly, even
    when cheap). Weak on limb (2): the licensing MECHANISM is now worse supported than at cycle 0.

  Summary: The owed remediation-rate literature exists and runs in the presumption's direction. In mature
    OSS projects a large share of filed bugs and static warnings are never fixed. Even actionable,
    already-localised static-analysis fixes (median 4 LOC) wait a median of ~96 days. The literature also
    says response rises when warnings are routed into a stage with an owner (code review/CI). That is the
    same structural variable MONITOR-585 names. On the owed replication check, the moral-licensing
    literature does not hold up well: a bias-corrected meta-analysis shrinks the effect to between null and
    d ≈ 0.18, and a three-study direct replication failed. The supportive case therefore shifts from a
    psychological mechanism (licensing) to a structural one (no owner/stage downstream of filing), and
    software-engineering data support that structural one better.

  Caveats: (i) Coverity and Eclipse figures are search-result level; the Coverity paper was not read.
    (ii) Non-remediation in OSS is confounded by triage (invalid/duplicate) and by legitimate
    deprioritisation, so it is not evidence of "discharge by filing" as such. (iii) None of the
    remediation sources measures the case in the statement, where the fix was ALREADY COMPUTED at filing
    time. The closest analogue is the small-fix/long-latency Coverity result. (iv) Kuper & Bott read at
    abstract level only.

  Recommendation: PARTIALLY-SUPPORTED. Re-weight the support from the licensing mechanism (now weak) to
    the structural no-downstream-owner reading (moderate). Further literature is unlikely to settle this
    item. MONITOR-585's own test (does a filing-triggered remediation stage with measured throughput exist)
    remains the discriminator.

  NOVELTY-FLAG: No.
