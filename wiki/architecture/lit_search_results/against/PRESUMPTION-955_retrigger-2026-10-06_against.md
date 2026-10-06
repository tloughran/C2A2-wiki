SEARCH-AGAINST-PRESUMPTION-955 (RE-TRIGGER cycle 1, CORRECTIVE limb only):
  Date searched: 2026-10-06
  Original item: PRESUMPTION-955
  Original statement: "[inferred] That a status vocabulary's first duty is to protect the downstream alarm
    from false positives, and only its second to protect the reader from false assurance." Held at
    MONITOR-605 as the corrective: a ternary vocabulary (PASS/DEGRADED/FAIL; OPC GOOD/UNCERTAIN/BAD) carried
    on the datum and enforced at the consumer dissolves the priority question. Realised harm (REVISE-457) is
    out of scope.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Note: my first fetch of the OPC Part 8 A.4.3.3 page was
    refused as "already fetched in this session" by another caller; I did not see that content and
    retrieved the parent section A.4.3 (which contains A.4.3.3) myself.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-955
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the stated ordering of reasons in a run asked for this ruling.
      15b (2026-09-11): CHALLENGED via ternary-quality standards (secondary sources).
      15c: DISPOSITION-946; corrective held as MONITOR-605 (standards not retrieved).
      15d (2026-09-20): Re-triggered; owed = standards retrieval.
      15b (re-trigger cycle 1): Retrieved OPC UA Part 8 Annex A.4.3 at source (OPC Foundation online
        reference, v1.05.07). ISA-18.2 and IEC 62682 NOT retrieved (paywalled). Searched practitioner
        reports on Uncertain handling. Found the standard itself collapsing the ternary at a boundary.
    Current status: PARTIALLY-CHALLENGED (the corrective, not the original presumption)

  Challenging evidence found: Yes

  Sources:
    1. OPC Foundation. OPC UA Part 8 (IEC 62541-8) Data Access, v1.05.07, Annex A.4.3 "Data and error
       mapping" (A.4.3.1, A.4.3.3, Table A.7). reference.opcfoundation.org/specs/OPC-10000-8/a-4-3
       [fetched] (a) "For successful operations (StatusCode of Good and Uncertain), the COM UA Proxy maps the
       Status Code ... to the OPC DA Quality. But in case of error (StatusCode of Bad), the Status Code is
       mapped to the OPC DA Error code." — at the UA→DA bridge the three states split 2+1, with Uncertain on
       the SUCCESS side. (b) Table A.7: Uncertain carries sub-codes (SubNormal, SensorNotAccurate,
       EngineeringUnitsExceeded, LastUsableValue); Bad carries eight. (c) "Uncertain_LastUsableValue" — the
       STALE case — is classed Uncertain, not Bad.
    2. Inductive Automation forum, "Tag stopped updating quality still showed good"; "Tag quality changes
       generate alarm" (forum.inductiveautomation.com) [search-result, practitioner, low evidential grade]
       Tags going offline move to Uncertain while preserving values; no new alarm fires unless a quality alarm
       is separately configured.
    3. OPC UA Part 9 Annex E — mapping to IEC 62682 alarm states [search-result] The IEC 62682 / ISA-18.2
       model is an ALARM-LIFECYCLE state model (suppressed, shelved, out-of-service, latched), not a datum-
       quality vocabulary. [background-knowledge: ISA-18.2 handles bad input quality as a separate
       instrument-diagnostic/"bad PV" alarm, not as a middle state — NOT verified at source.]

  Strength of challenge: Moderate

  Summary: The canonical ternary vocabulary does not stay ternary at the consumer. OPC's own mapping, at the
    one boundary it specifies normatively, sorts Uncertain with Good as a successful read and only Bad as an
    error; any consumer that branches on success/error — the commonest consumer — reads Uncertain as success.
    The stale-data case, which is the estate's actual failure (REVISE-457), is assigned to Uncertain, i.e. to
    the state most likely to be collapsed into "fine". Second, OPC's third state works (where it works)
    because it is severity PLUS a typed sub-code; a bare three-token vocabulary (PASS/DEGRADED/FAIL) imports
    the token without the sub-code that makes it actionable. Third, the alarm standards do not adopt a
    middle state at all; they keep alarms binary and route bad quality to a separate diagnostic channel —
    which is the age-alarm design, not the ternary-token design. This confirms 15b's prior consumer-audit
    falsifier as the deciding test.

  Specific risks: DEGRADED is silently read as PASS by consumers that test "not FAIL", reproducing the
    stuck-at-nominal false-green (PREMISE-110) with an extra token; staleness lands in DEGRADED and is ignored.

  Mitigations available: Enforce at the consumer by exhaustive match (no default branch); attach a typed
    reason sub-code to DEGRADED; keep staleness on the separate age alarm (REVISE-457); run MONITOR-605 (b).

  Recommendation: PARTIALLY-CHALLENGED. OPC Part 8 now VERIFIED at source for the mapping clause; ISA-18.2 /
    IEC 62682 still NOT retrieved; Part 4 StatusCode severity definitions not fetched (budget).

STEELMAN:
  Item: PRESUMPTION-955 (corrective)
  Strongest counterargument: The industry's own reference vocabulary shows what happens to a middle state:
    at the first interface that only understands success and failure, it is filed under success. OPC's
    normative bridge does exactly that, and puts "last usable value" — staleness — on the success side.
    The alarm standards, for their part, never adopted a middle alarm state; they keep the alarm binary and
    send data-quality problems down a separate channel. A third token without exhaustive consumer handling
    and typed sub-codes is not a correction; it is a new place for false assurance to hide.
  What would need to be true for C2A2 to be safe: every automated consumer branches exhaustively on all
    three values, DEGRADED carries a reason code, and staleness is alarmed separately.
  How to test: MONITOR-605 (b) — one grep of every status-token consumer for a default/else branch.
