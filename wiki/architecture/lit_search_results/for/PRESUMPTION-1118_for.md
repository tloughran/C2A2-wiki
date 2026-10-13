SEARCH-FOR-PRESUMPTION-1118:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1118
  Original statement: A one-word aggregate health verdict is presumed to cover everything, though the instrument
    inspected a disjoint scope. Question: Should health verdicts carry explicit scope and an UNKNOWN state for
    uninspected components?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1118
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a run report whose single-word health verdict was read as system-wide although the inspecting
        instrument covered a disjoint component set; queued 2026-10-09
      15a (2026-10-10): 3 web searches, 1 fetch (succeeded; oversized page saved and partially read). Found established
        engineering precedent for UNKNOWN as a first-class monitoring state (Nagios/Monitoring Plugins exit code 3;
        Kubernetes True/False/Unknown conditions) and for treating missing data as a distinct alert state (Grafana
        NoData; Prometheus absent_over_time). Kubernetes docs state that a single summary value "cannot capture the full
        picture". Kleene three-valued logic gives the theoretical basis for roll-up. Little found on explicit SCOPE
        labels on verdicts.
    Current status: SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) Nagios UNKNOWN state semantics; (b) SRE/Prometheus/Grafana absence of
    data / no-data alert state; (c) Kubernetes condition status Unknown plus Kleene three-valued logic. 1 fetch:
    kubernetes.io Pod Conditions page (succeeded; ~106k chars saved to disk; only the meta-description and header lines
    were read). A grep of the saved text found no occurrence of "Unknown", so the Unknown-status claim (source 2b) rests
    on search results, not the fetched page. Google SRE book not reached.

  Supporting evidence found: Yes (Moderate)

  Sources:
    1. Nagios Core / Monitoring Plugins: plugin exit code 3 = UNKNOWN (O'Reilly "Nagios, 2nd ed." §4.3; nagiosplug-devel
       list 2005; Nagios support forum). [search-result] UNKNOWN is a distinct state meaning the check could not
       measure. It explicitly does NOT mean the service is down or up. Notification of UNKNOWN is configurable ("u").
       Relevance: decades-old industry precedent for a non-OK/non-fail "could not determine" verdict. Caveat: in 2005
       Galstad advised reserving UNKNOWN for plugin/argument errors and treating timeouts as CRITICAL, i.e. conservative
       mapping of non-observation to failure, not to OK.
    2. Kubernetes documentation, "Pod Conditions" (kubernetes.io, modified 2026-06-20).
       (a) [fetched, partial] Meta-description: "A Pod's phase provides a high-level summary ... but a single value cannot
       capture the full picture ... Pod conditions complement the phase by tracking multiple aspects of the Pod's state
       independently." Relevance: direct statement against a one-word aggregate verdict.
       (b) [search-result] Condition status takes the values "True", "False" or "Unknown". Unknown means the system
       could not determine the status. The pod phase Unknown is reserved for when the state "could not be obtained",
       typically from loss of contact with the node. Not confirmed in the fetched page text (see Search scope).
    3. Grafana Alerting docs, "Handle missing data" (v11–v13). [search-result] Prometheus does not fire on empty query
       results, which the docs call a "silent failure". Grafana provides a distinct "No Data" state (default raises
       DatasourceNoData), and absent_over_time() is recommended for detecting missing series. Relevance: practitioner
       consensus that absence of signal must be surfaced as its own state, not folded into OK.
    4. Kleene strong three-valued logic (general reference, e.g. Wikipedia "Three-valued logic"). [search-result] An
       AND-style roll-up yields False if any input is False and Unknown if none is False but any is Unknown. Relevance:
       theoretical basis. An aggregate "healthy" is licensed only if every component is True, so uninspected components
       force at most Unknown.

  Strength of support: Moderate. UNKNOWN-as-first-class-state is well established in widely deployed monitoring
    systems (strong practice precedent, but vendor docs rather than peer-reviewed research). The "explicit scope on the
    verdict" half has only indirect support (Kubernetes per-aspect conditions; Grafana per-series absence).

  Summary: Mainstream monitoring systems already reject the presumption. Nagios has a dedicated UNKNOWN exit state,
    Kubernetes uses True/False/Unknown conditions and states that a single summary value cannot capture pod health, and
    Grafana treats missing data as a distinct alert state because silent absence otherwise passes as healthy. Kleene
    logic formalises the roll-up rule: an aggregate is OK only when every in-scope component is observed OK. Together
    these support verdicts of the form "OK for components {A,B}; UNKNOWN for {C..N}; not inspected". No academic
    literature on alert semantics was reached in this preliminary search.

  Transfer caveats: (i) Monitoring-system evidence is design convention, not an empirical demonstration that UNKNOWN
    reduces missed incidents. (ii) Practitioners disagree on how to treat UNKNOWN (alert vs. map to CRITICAL), so the
    literature supports making it visible, not a particular escalation policy. (iii) Explicit scope enumeration on
    every verdict may be noisy at scale; the sources favour per-component states over prose scope statements.

  NOVELTY flag: partial. UNKNOWN as a state is standard. Requiring an aggregate verdict to declare its inspected scope
    was not found as an explicit, named practice in this search.

  Recommendation: SUPPORTED (Moderate). Preliminary search; broader search recommended (Google SRE book monitoring
    chapters; academic work on alert semantics / observability coverage).
