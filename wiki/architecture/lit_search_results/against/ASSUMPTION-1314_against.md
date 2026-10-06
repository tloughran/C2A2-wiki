SEARCH-AGAINST-ASSUMPTION-1314:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1314
  Original statement: "Status file rewritten as `PASS` with an explicit `VERIFIED-NOT-REGENERATED`
    qualifier — **a bare `FAIL` would have fired `morning-system-health` over feeds that are genuinely
    current, and a bare `PASS` would have claimed work I didn't do.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1314
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. The day's one status decision made FOR the downstream reader's
        alarm rather than for the register, and the fourth item today to end in a request for a ruling
        from a channel silent since 2026-08-27. The direction of the protection is PRESUMPTION-955.
      15b: Searched for challenging literature; found the diagnosis is correct and standard, but the
        REPAIR is the known anti-pattern — the third value was not invented, it already exists as a
        first-class state, and encoding it as a qualifier inside `PASS` is the specific mistake.
    Current status: PARTIALLY-CHALLENGED — and the challenge is to the repair, not the diagnosis

  Register pre-check:
    - PREMISE-141 (ACTIVE) — "ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER
      TWO... Cristian's failure-semantics taxonomy separates a component that runs and produces no
      response from one that crashes." **This is the pre-answer and it runs FOR the item's first limb**:
      a third state is formally correct, and this register already says so.
    - PREMISE-167 (ACTIVE) — "AN ESCALATION AND A MEASUREMENT ARE DIFFERENT OBJECTS AND MUST BE STORED AS
      DIFFERENT OBJECTS... an escalation expressed only as a WITHHELD PASS-MARK has no representation on
      disk distinct from staleness." **Exact pre-answer to the encoding question**, and it denies the
      qualifier-in-a-string approach.
    - PREMISE-100 (ACTIVE) — a health check that cannot execute in its runtime context reports as
      PASSING rather than as ABSENT; monitoring that conflates the two produces false-green at a rate
      proportional to the number of inoperable checks. **This is the risk the repair creates.**
    - PREMISE-110 (ACTIVE) — detectors do not degrade gracefully, they invert: a monitor whose failure
      presents as a nominal reading becomes MORE reassuring as the condition worsens (stuck-at-nominal).
    - PREMISE-063 (ACTIVE) — gap-honest visualization: absence must be encoded as distinct from a true
      zero, and inferred values shown as inferred.
    - PREMISE-103 (ACTIVE) — downgrading confidence is not a valid substitute for an explicit state.
      Symmetrically: upgrading-with-a-qualifier is not either.
    - PREMISE-155 (ACTIVE) — a state assertion binds to a resolved artefact identity, not to a name, and
      an assertion taken at an internal stage is not a guarantee for consumers.
    - PREMISE-179 (ACTIVE) — a regex-defined reader over a heterogeneous record is a SILENT-FAILURE
      interface: a record in an unanticipated shape is not rejected, it is not seen, and no error is
      raised. **Directly predicts how `PASS VERIFIED-NOT-REGENERATED` will be read downstream.**

  Challenging evidence found: Yes — on the second limb

  LIMB STRUCTURE — three limbs, and the recommendation turns entirely on the third:
    LIMB A — "a binary status vocabulary cannot carry 'verified current but not produced by me'."
      (True, and already PREMISE-141.)
    LIMB B — "a third value is the right repair." (True, and already standard practice — see below.)
    LIMB C — "the third value should be a QUALIFIER ATTACHED TO `PASS`." (The actual act taken, and the
      anti-pattern.)
    (Plus the unstated limb D: "a task that did not do its work should nevertheless not FAIL.")

  Sources:
    1. The Nagios/Monitoring-Plugins return-code standard, as documented across Icinga 2's Monitoring
       Basics and Service Monitoring docs, the monitoring-plugins.org `negate` man page, the O'Reilly
       *Nagios 2nd Edition* §4.3 "States of Hosts and Services," and the olorin/nagiosplugin library. —
       SECONDARY (four independent sources retrieved via search and read at summary level; I attempted
       the monitoring-plugins.org developer guidelines page directly and it was outside my fetch
       provenance set, so the canonical text is unread) — **The third value was not invented.** The
       standard plugin API has had four states for two decades: **0 OK, 1 WARNING, 2 CRITICAL, 3
       UNKNOWN**, where UNKNOWN specifically means *the check could not be carried out* — which is
       exactly the state the telemetry refresh was in. The severity ordering is OK → UNKNOWN → WARNING →
       CRITICAL, i.e. UNKNOWN is deliberately non-alarming but non-green. A monitoring system that needed
       a third value invented had not looked at the monitoring literature; the correct repair was to
       adopt `UNKNOWN`, and it would have satisfied both stated constraints without a new vocabulary.
    2. Enum forward-compatibility practice (protobuf): Wealthfront Engineering, "Protobufs backward and
       forward"; Yokota, "Understanding Protobuf Compatibility"; protocolbuffers/protobuf issue #3971;
       Atomic Object, "Using Protobuf Fields & Compatibility." — SECONDARY (multiple independent
       engineering sources retrieved) — the documented pitfall is that a consumer which does not know a
       value silently maps it to the default and proceeds, and the documented remedy is to **reserve an
       explicit `UNKNOWN` as a first-class enum member** so that unrecognised states are identifiable
       rather than silently defaulted. Same answer as (1), reached independently from a different
       discipline: make the third state a *value*, never a modifier on an existing value.
    3. The fail-open argument, which is the decisive one and needs no external citation. Any consumer
       written as `status == "PASS"`, `status.startswith("PASS")`, `grep -q PASS`, or `"PASS" in line`
       will read `PASS VERIFIED-NOT-REGENERATED` as **green**. That is not a hypothetical: PREMISE-179
       (ACTIVE) holds that a regex-defined reader over a heterogeneous record file does not reject an
       unanticipated shape, it *fails to see it*, and raises no error. So the qualifier protects the
       alarm only for readers that were specifically taught about it, and produces false-green for every
       reader that was not — which is PREMISE-100's failure mode, deliberately introduced.
       — VERIFIED (by inspection of the encoding as stated in the item).
    4. On limb D (should it simply FAIL?) — the alarm-fatigue tradition (EEMUA 191 / ISA-18.2 lineage,
       reached via the Nagios severity-ordering sources) supports the run: firing CRITICAL over feeds
       that are genuinely current is a false alarm, and false alarms degrade the responsiveness of the
       whole channel. — SECONDARY/UNVERIFIED (I did not retrieve either standard; this is stated as the
       general position of that literature and carries little weight). But note that this argument
       supports **WARNING or UNKNOWN**, not `PASS`-with-a-qualifier. It is an argument against a bare
       FAIL, not an argument for a decorated PASS.

  Strength of challenge: Strong on LIMB C; None on LIMB A; None on LIMB B in substance (though it is
    challenged as to *novelty* — the value did not need inventing).

  Summary: The run diagnosed the problem correctly and then made the one repair the literature warns
    against. That a two-valued status cannot carry "verified current but not produced by me" is right,
    and this register already holds it as PREMISE-141: absence of a report is a third terminal state, not
    a value of the other two. That a third value is the answer is also right — and it is so standard that
    calling it an invention is the tell. The Nagios plugin API, which is the de facto standard for
    exactly this problem, has carried OK / WARNING / CRITICAL / UNKNOWN for two decades, with UNKNOWN
    defined as "the check could not be carried out" and deliberately ordered as non-alarming but
    non-green. Protobuf practice reaches the same design independently: reserve an explicit UNKNOWN as a
    first-class value, because consumers silently default anything they do not recognise. What the run
    did instead was attach a qualifier to `PASS`, and that is the fail-open configuration: every
    downstream consumer matching on the string `PASS` reads green, and by PREMISE-179 none of them will
    raise an error about it. PREMISE-167 already names this exact defect — an escalation with no
    representation on disk distinct from the normal case. The run protected the alarm at the cost of
    protecting the reader, which is precisely what PRESUMPTION-955 asserts.

  Specific risks: `morning-system-health` was the reader the encoding was designed for, so it probably
    handles the qualifier. Every *other* consumer is the exposure, and they are unenumerated. Concretely:
    any dashboard, any aggregate "all checks green" roll-up, any human skimming a status file, and any
    future script will read `PASS`. That yields false-green — PREMISE-100 — at a rate proportional to the
    number of consumers not taught the qualifier, and PREMISE-110 says the failure inverts: the more
    often the sandbox cannot regenerate, the more `PASS` lines accumulate and the healthier the system
    looks. The second risk is precedent. A qualifier-on-PASS convention, once established, will be reused
    for the next irreducible-third-case, and the status vocabulary becomes a free-text field with a
    parseable prefix — which is PREMISE-179's silent-failure interface by construction. The third risk is
    that the ruling was requested from a channel silent since 2026-08-27, so the convention is now the
    default by inaction, which PREMISE-102 says converts a one-time signal into a standing policy of
    non-coverage.

  Mitigations available:
    - **Adopt the existing vocabulary rather than extending the existing value.** Write `UNKNOWN` (or
      `WARNING`) as the status token, with `VERIFIED-NOT-REGENERATED` as the *reason*. This satisfies
      both of the run's stated constraints exactly — it does not fire CRITICAL over current feeds, and it
      does not claim work that was not done — and it fails *closed* for naive consumers rather than open.
      This is a one-token change and it is the whole recommendation.
    - Split the two facts into two fields, per PREMISE-167: `regenerated: false` and `feeds_current:
      true` are independent observations and should be stored independently. A single status token is
      then derivable by whatever policy the reader wants, and no reader has to parse prose.
    - Enumerate the consumers before ruling. `grep -rl` for the status file across the fleet; any
      consumer matching on `PASS` as a substring is already mis-reading today.
    - Reserve the token space: declare the permitted status values explicitly, so an unrecognised value
      is an error rather than a default. This is the protobuf remedy and it prevents the next
      qualifier.
    - Per PREMISE-173, name the final element: what ACTION does `VERIFIED-NOT-REGENERATED` trigger, and
      in whom? If the answer is "none," it is a note, not a state, and the task should FAIL.

  STEELMAN:
    Item: ASSUMPTION-1314
    Strongest counterargument: The run faced a genuine three-valued reality with a two-valued interface it
      did not own, and chose the option that preserved the most information at the least risk of breaking
      a consumer. Introducing a brand-new status token into a file that `morning-system-health` parses is
      not a free action — an unrecognised token might itself have been mishandled, possibly worse than a
      recognised one with extra text, and the run had no authority to change the consumer. Appending a
      qualifier is the *backward-compatible* move: existing consumers behave exactly as before, and the
      additional information is available to anyone who looks. The run also did the one thing this estate
      most often fails to do — it stated the ambiguity explicitly and asked for a ruling, naming the exact
      alternative ("if you'd rather this task hard-FAIL... say so and I'll flip the convention"). Judged
      as a decision made under an unowned interface with no authority to change it, this is close to
      optimal, and the criticism is really of the silent ruling channel, not of the encoding.
    What would need to be true for C2A2 to be safe: (1) every consumer of this status file must be
      enumerated and must handle the qualifier — and that set must be *closed*, i.e. no new consumer can
      be added without being taught; (2) the qualifier must be machine-parseable and stable, not prose;
      (3) the feed-currency verification that justifies the non-FAIL must itself be a real check with its
      own evidence, not an assertion (PREMISE-195: voluntary self-report is not a detection control); and
      (4) the ruling request must actually be answered — an unanswered convention question becomes a
      convention, and PREMISE-102 says that is the worst outcome of the three.
    How to test: Two cheap in-house checks. (a) **Fail-open test:** grep the fleet for consumers of this
      status file and classify each by how it matches — exact equality, prefix, or substring. Any
      substring or prefix matcher is reading `PASS VERIFIED-NOT-REGENERATED` as green today, and the
      count of such consumers is the size of the false-green exposure. This takes minutes. (b)
      **Injection test:** write `UNKNOWN` into the status file once and observe what `morning-system-
      health` actually does. That settles the steelman's central empirical claim — that a new token might
      be mishandled worse than a decorated old one — by observation rather than by supposition, and it is
      the discriminating test PREMISE-107 requires before choosing between the two repairs.

  Search scope: comprehensive on monitoring status vocabularies and enum forward-compatibility;
    preliminary on alarm management. Searched: Nagios/Icinga plugin return codes and state semantics;
    monitoring-plugins developer guidelines (canonical page NOT retrieved — it fell outside my fetch
    provenance set, so the four-state API is documented here from four secondary sources rather than from
    the standard itself); protobuf enum compatibility and unknown-value handling; HTTP/status-code
    extensibility. NOT searched in depth: EEMUA 191 / ISA-18.2 alarm rationalisation (the asymmetric-cost
    literature the intake note anticipated), and the SRE literature on symptom-vs-cause alerting — either
    would sharpen limb D, which I have treated lightly.

  Recommendation: PARTIALLY-CHALLENGED — resting entirely on LIMB C (the encoding). LIMB A is
    NO-CHALLENGE-FOUND and is already PREMISE-141. LIMB B is upheld in substance but corrected as to
    novelty: the third value is `UNKNOWN`, it has existed as a first-class state for twenty years, and
    the repair is to use it rather than to decorate `PASS`. The single actionable line: **change the
    token, keep the reason.**
