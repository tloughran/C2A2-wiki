SEARCH-FOR-PRESUMPTION-955 (CORRECTIVE limb — standards retrieval):
  Date searched: 2026-10-06
  Original item: PRESUMPTION-955
  Original statement: "[inferred] That a status vocabulary's first duty is to protect the downstream
    alarm from false positives, and only its second to protect the reader from false assurance."
  Limb searched: corrective — that a ternary status vocabulary (PASS/DEGRADED/FAIL; OPC Good/Uncertain/
    Bad) carried on the datum dissolves the priority question (MONITOR-605 (a)). The realised harm
    (REVISE-457) was not searched.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-06)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-955
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption — status vocabulary design prioritising alarm precision
      15a (cycle 0): four vendor/practitioner summaries; ISA-18.2, IEC 62682, OPC UA NOT RETRIEVED
      15c: DISPOSITION-946 — held at MONITOR-605 as UNVERIFIED basis
      15d: re-triggered cycle 1; owed = standards retrieval
      15a (cycle 1, 2026-10-06): OPC UA Part 8 section retrieved from the OPC Foundation online
        reference; ISA-18.2 still not retrieved (paywalled) — definition obtained via fetched
        secondary
    Current status: PARTIALLY-SUPPORTED

  Search scope: 2 web searches (OPC UA Part 8 quality/severity; ISA-18.2/IEC 62682 alarm and alert
    definitions), 2 fetches (OPC 10000-8 §A.4.3.3; exida 2016 ISA-18.2 release note).

  Supporting evidence found: Partial

  Sources:
    1. OPC Foundation, OPC 10000-8 (OPC UA Part 8: Data Access), v1.05.07, §A.4.3.3 "Quality".
       reference.opcfoundation.org/specs/OPC-10000-8/a-4-3-3. [fetched — PRIMARY] — "The Quality of a
       Data Value in the OPC UA Server is represented as a StatusCode." The StatusCode's Severity field
       maps to the primary quality; Table A.7 maps Good / Uncertain / Bad (with subcodes such as
       Uncertain_LastUsableValue, Uncertain_SensorNotAccurate, Bad_NoCommunication) to OPC DA
       GOOD / UNCERTAIN / BAD. Confirms at primary source that the ternary quality vocabulary is carried
       ON THE DATUM (as part of the data value), not on a separate alarm channel.
    2. OPC 10000-8 §7.3 "Data Access status codes". [search-result — not fetched] — Search snippet:
       BAD severity "indicates a failure"; UNCERTAIN "indicates that the value has been generated under
       sub-normal conditions"; GOOD = success. Consistent with source 1; wording not verified at page.
    3. Stauffer, T., 2016. "New Version of ISA-18.2 Alarm Management Standard Is Released (2016)."
       exida blog. [fetched — secondary; author is an exida alarm-management practitioner writing on
       the standard's release] — Quotes ANSI/ISA-18.2-2016's alarm definition: "audible and/or visible
       means of indicating to the operator an equipment malfunction, process deviation, or abnormal
       condition requiring a timely response," noting "timely" was added for consistency with IEC 62682.
    4. ISA-18.2-2016 "alert" definition — "a notification of an abnormal condition that requires
       assessment or action and which does not meet the criteria for an alarm." [search-result —
       exida page, not fetched]

  NOT CONFIRMED this pass (stated plainly): (i) ISA-18.2 / IEC 62682 standard text itself — still
    paywalled, not retrieved; (ii) the "convert-to-indication" requirement — not found; (iii) the
    "value-NULL-on-Bad" rule — not in the Part 8 section fetched (it may sit in Part 4 services; not
    searched); (iv) any OPC/ISA mapping to PASS/DEGRADED/FAIL specifically.

  Strength of support: Moderate (for the vocabulary); Weak (for the "dissolves the priority" claim)

  Summary: The corrective's structural premise is now confirmed at a primary standard: OPC UA attaches a
    three-valued quality (Good/Uncertain/Bad) to each data value, with Uncertain reserved for sub-normal
    but usable data — i.e., the middle state exists precisely to tell a consumer "do not trust fully"
    without raising a failure. ISA-18.2's alarm definition (response-required, timely) together with a
    separate alert class supports keeping the alarm channel narrow while still informing the reader
    through a lower tier. Together these support the shape of the corrective: precision for the alarm
    and truthfulness for the reader can be served by different tiers rather than traded off.

  Caveats: The standards define the vocabulary; they do not test whether a third token is handled by
    consumers. MONITOR-605 (b) (the consumer-branching grep) remains the falsifier and is not a
    literature question. ISA-18.2 evidence remains secondary.

  Recommendation: PARTIALLY-SUPPORTED. OPC UA basis upgraded from UNVERIFIED to VERIFIED (primary, §A.4.3.3);
    ISA-18.2 basis remains secondary.
