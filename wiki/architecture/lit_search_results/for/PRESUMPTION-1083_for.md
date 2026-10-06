SEARCH-FOR-PRESUMPTION-1083:
  Date searched: 2026-09-24
  Original item: PRESUMPTION-1083
  Original statement: Monitoring instruments that report unchanged values cannot, from their output
    alone, distinguish a stable system from frozen inputs.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1083
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred the unstated presumption that flat readings are ambiguous without a liveness signal.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed
       Systems." Journal of the ACM (preliminary version PODC 1991). — Foundational result context:
       in asynchronous systems it is impossible, from observed behavior alone, to distinguish a
       crashed process from a slow one; detection requires additional assumptions or oracles.
       Theoretical analogue: absence of change is not self-interpreting.
    2. Sensor-fault taxonomy in wireless sensor networks, e.g. "Fault Detection in Wireless Sensor
       Networks through the Random Forest Classifier," Sensors 2019 (PMC6480196; authors unconfirmed).
       — Defines the "stuck-at" fault as zero variance in the sensed series; detection relies on
       classifiers, neighbours, or expected-variability models, i.e., information beyond the single
       sensor's output.
    3. Vaughan, D., 1996. The Challenger Launch Decision: Risky Technology, Culture, and Deviance at
       NASA. University of Chicago Press. — Normalization of deviance: repeated uneventful readings
       shift the baseline so an anomalous steady state is read as normal. Organizational support for
       why unchanged readings get interpreted as stability.
    4. Data-freshness / heartbeat practice (e.g., industrial dataflow diagnosis distinguishing "comms
       OK but value stale" from "good status but flatline"). — Practitioners add out-of-band
       heartbeats precisely because stale data "looks perfectly normal."

  Strength of support: Moderate

  Summary: Distributed-systems theory establishes that silence or non-change cannot by itself
    distinguish failure from normal slowness, and sensor-fault engineering defines a distinct
    "stuck-at" fault class whose detection requires context beyond the sensor's own output. Operational
    practice responds by adding heartbeats and freshness SLAs, which is an implicit acknowledgment of
    the presumption. Vaughan supplies the human-side mechanism by which flat readings get normalized.

  Caveats: The claim holds "from output alone"; instruments that emit timestamps, sequence numbers or
    variance metadata are not purely value outputs and can discriminate. Chandra–Toueg concerns
    process liveness, not data freshness — the transfer is by analogy. Sensor sources are
    domain-specific (WSN, industrial).

  Search scope: Preliminary — four searches (freshness/heartbeat/flatline; stuck-at sensor faults;
    failure detectors; normalization of deviance).

  Excluded results: Vendor blogs (DEV Community, Conduktor, Sifflet, Streamkap, PipeCode) — used only
    as evidence of practice, not cited individually; glama.ai MCP tool listing (aggregator);
    Utah Avalanche Center and psychsafety blogs on Vaughan (secondary; book cited).

  Recommendation: SUPPORTED
