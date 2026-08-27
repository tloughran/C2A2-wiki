SEARCH-FOR-PRESUMPTION-884:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-884
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake)
  Original statement: "[inferred] That a benign cause of record, once established, can be applied to an
    entire flag population without per-item test — that explaining one instance explains the class."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-884
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an internal tension inside a single transcript — a blanket dismissal of the
        bundled fidelity `fail` on all 307 entries as "the recorded cold-cache condition ... not
        infidelity" (ASSUMPTION-1209), stated in the same report as the retention of Day 76 as a
        genuine fidelity failure (ratio 0.610, escalated 2026-08-17, still open). High confidence.
        Checked against PRESUMPTION-876 for duplication; the mechanism is scope-of-attribution, not
        staleness-of-verdict.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-26, two queries plus material carried from the ISA-18.2 limb.
    Limbs covered: (a) designed alarm suppression under ANSI/ISA-18.2 — shelving, designed suppression,
    out-of-service — as the standardised warrant for suppressing a whole flag population on a known
    condition; (b) alarm correlation and root-cause inference in telecommunications and network fault
    management, where suppressing symptom alarms once a root cause is identified is routine engineering
    practice.
    Assessment: **narrow but well-targeted — two queries only, and one limb missing.** Not searched:
    the statistical literature on common-cause vs. special-cause variation (Shewhart/Deming), which is
    the classical frame for exactly this move and would probably have strengthened the case; and the
    literature on suppression-rule expiry, sampling audits of suppressed populations, and masking of
    true positives, which is the against direction and was deliberately left to 15b. No source located
    addresses blanket attribution over a population *known in advance to be mixed*, which is the item's
    distinguishing feature.

  Supporting evidence found: Yes

  Sources:
    1. ANSI/ISA-18.2, "Management of Alarm Systems for the Process Industries," as documented in:
       ISA, "Process Automation: From managing to optimizing alarms," *InTech*, Sept/Oct 2017,
       https://www.isa.org/intech-home/2017/september-october/features/from-managing-to-optimizing-alarms ;
       Yokogawa/Control Engineering, "Implementing Alarm Management per the ANSI/ISA-18.2 Standard,"
       https://www.yokogawa.com/us/library/resources/media-publications/implementing-alarm-management-per-the-ansi-isa-182-standard-control-engineering/ ;
       "ISA-18.2 Alarm Management: Best Practitioner Guide 2026,"
       https://processcontrolguide.com/isa-18-2-alarm-management/
       — The strongest support. The standard defines three sanctioned forms of alarm suppression:
       shelving (operator-initiated, temporary), **designed suppression** (the automation system
       suppresses an alarm based on a specified set of conditions), and out-of-service (suppressed
       because equipment is shut down for maintenance). "Out of service" is an almost exact analogue of
       the C2A2 case: a whole class of alarms is dismissed *because a known condition of the plant
       accounts for them*, with no per-alarm test. That this is a named, standardised state rather than
       an expedient is the core of the supportive case. SNIPPET-ONLY; the ANSI/ISA standard itself was
       not retrieved.
    2. Cause-and-effect-based suppression and alarm-flood management, per the same ISA-18.2 sources and
       Mikrodev, "Alarm Management ISA-18.2: SCADA Alarms, Event Management, Priority, and Operator
       Effectiveness," https://www.mikrodev.com/alarm-management-isa-18-2-scada-alarms-event-management-priority-and-operator-effectiveness/
       — States the operative rule directly: when a root cause is identified, subsequent related alarms
       should be suppressed so as not to distract the operator from the real problem; where one root
       cause (e.g. a power supply failure) triggers twenty downstream alarms, the system should present
       the root cause and group or suppress the consequential ones. This is precisely "explaining one
       instance explains the class," and it is the recommended practice, not a lapse. SNIPPET-ONLY.
    3. Jakobson, G., and Weissman, M. "Alarm correlation and fault identification in communication
       networks." https://www.researchgate.net/publication/3159207 [author attribution from the
       well-known title; year unverified]
       — The foundational engineering statement of the same principle in telecoms: a single fault at
       element level produces a large number of symptomatic messages at all levels, and correlation
       exists to collapse them onto one cause. Supplies the theoretical grounding for treating a flag
       population as a symptom set with a shared explanation. ABSTRACT-ONLY.
    4. "Alarm reduction and root cause inference based on association mining in communication network."
       *Frontiers in Computer Science* (2023), DOI 10.3389/fcomp.2023.1211739,
       https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2023.1211739/full
       [authors unverified]
       — Recent empirical work on inferring a root cause across an alarm population and reducing alarm
       volume accordingly. The closest located instance of the blanket-attribution move being both
       automated and measured. ABSTRACT-ONLY.
    5. Broadcom/CA Spectrum, "Alarm Correlation," Cluster Manager documentation,
       https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/spectrum/25-4/managing-systems/cluster-manager/getting-started-with-cluster-manager/cluster-manager-alarms-and-fault-management/alarm-correlation.html
       — Vendor documentation of a deployed product that "automatically correlates alarms to identify a
       single root cause" and correlates multiple alarm reports to one cause. Empirical precedent that
       the pattern is in production use at scale. SNIPPET-ONLY.
    6. US Patent 6,748,432, "System and method for suppressing side-effect alarms in heterogeneous
       integrated wide area data and telecommunication networks,"
       https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6748432 ; and US Patent
       8,676,945, "Method and system for processing fault alarms and maintenance events in a managed
       network services system,"
       https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8676945 [assignees and years
       unverified]
       — The second describes creating a ticket only for the root-cause alarm and suppressing all
       related symptom alarms, on the reasoning that resolving the root cause addresses the symptoms
       simultaneously, significantly reducing tickets processed. Directly analogous to dismissing a
       307-entry `fail` population on one diagnosed cause. FULL-TEXT available at USPTO;
       SNIPPET-ONLY as read here.

  Strength of support: Moderate-to-Strong

  Summary: The monitoring and fault-management literature supports the presumption's core move squarely
    and by name. ANSI/ISA-18.2 sanctions three forms of alarm suppression, two of which — designed
    suppression and out-of-service — apply to a whole class of alarms on the strength of a known
    condition rather than a per-alarm test; the "out of service" case in particular is the standardised
    version of dismissing a flag population because a recorded plant condition accounts for it. The
    cause-and-effect suppression rule is stated as recommended practice: once a root cause is
    identified, related downstream alarms should be suppressed so the operator is not distracted from
    the real problem. Alarm correlation in telecommunications rests on the same principle — one element
    fault produces many symptomatic messages, and collapsing them onto a single cause is the whole
    point of the discipline — and it is implemented in shipped products and patented systems that
    ticket the root cause and suppress the symptoms. So the general claim that explaining one instance
    can license a class-wide reading is not an epistemic shortcut but a standardised engineering
    practice with a substantial literature behind it. The limit, which the sources state as clearly as
    they state the rule, is that suppression is *designed*: it is applied on a specified set of
    conditions, established during rationalisation, with the causal link between root and symptom
    modelled in advance. The generating case has a cause asserted after the fact, no specified
    conditions, no expiry, no sampling, and a population whose mixedness is documented in the same
    report.

  Caveats: (1) Every supportive source presupposes a *modelled* causal relation between root and
    symptom, established before the flood, not an attribution made after seeing the flood. (2) None
    addresses a population known in advance to be mixed. The Day 76 true positive was preserved in the
    same report that dismissed the class, which means the blanket rule was applied over a set already
    demonstrated to contain a non-benign member; no located source covers this configuration. (3)
    ISA-18.2's suppression states are bounded — shelving is temporary and typically expires, out-of-
    service tracks equipment state — whereas the attribution in the generating case has no expiry.
    (4) Alarm correlation systems continuously re-evaluate; the suppression is a live inference over a
    running condition, not a one-off verdict, which is arguably the per-item test the presumption
    dispenses with. (5) I did not search the common-cause/special-cause variation literature, which is
    the classical statement of the risk of misclassifying a special cause as common. (6) All sources
    read at snippet or abstract level; no standard text retrieved; several attributions unverified.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that suppressing a whole flag population on a known condition, without
    per-item test, is a named and standardised practice (ISA-18.2 designed suppression / out-of-
    service); (ii) that collapsing many symptom alarms onto one diagnosed root cause is recommended
    practice and is deployed in production systems; (iii) that doing so measurably reduces the volume
    of items requiring disposition.
    Unaddressed sub-claim: **blanket benign attribution over a population already demonstrated to be
    mixed, applied after the fact, with no expiry and no sampling.** The literature's warrant for
    class-wide suppression is a *designed* rule with a pre-modelled causal link and a bounded lifetime.
    I found nothing addressing a post-hoc attribution that coexists in the same report with a known
    true positive from the same population. That specific configuration — where the suppression rule
    and its own counter-example are stated side by side and not read against each other — appears
    unaddressed in the located literature and is flagged as a candidate original contribution.
    Note that the item is cheaply settled in-house (warm the segment cache once and recount), so the
    literature gap need not remain open.
