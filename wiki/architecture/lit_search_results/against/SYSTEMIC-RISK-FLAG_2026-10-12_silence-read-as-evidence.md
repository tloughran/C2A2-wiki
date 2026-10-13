SYSTEMIC-RISK-FLAG:
  Date: 2026-10-12
  Affected items: ASSUMPTION-1682 (MONITOR-617), ASSUMPTION-1684 (MONITOR-618), PRESUMPTION-991
    (MONITOR-610), PRESUMPTION-1101 (MONITOR-636)
  Related prior flag: SYSTEMIC-RISK-FLAG_2026-09-14_pre-check-instrument-fails-silently_982-983-988-
    989-991-1369.md (same family; this flag extends it from instrument FAILURE to instrument
    INSENSITIVITY and to human-channel silence).

  PROVENANCE:
    Origin: 15b (cross-item synthesis); underlying items originate 14a (1682, 1684) and 14b (991, 1101)
    Chain: [14a/14b → 15a, 15b → 15c → 15d → 15b (re-trigger 2026-10-11/12) → SYSTEMIC-RISK]
    Original items: ASSUMPTION-1682, ASSUMPTION-1684, PRESUMPTION-991, PRESUMPTION-1101
    Item type: mixed — 2 ASSUMPTION (stated), 2 PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14a/14b: items extracted/inferred (2026-09-13 .. 09-30)
      15c: each dispositioned to MONITOR
      15d (2026-10-11): re-triggered (cycles 1–3)
      15b (2026-10-12): searched independently per item; common vulnerability identified across files
        *_retrigger-2026-10-12_against.md
    Current status: FLAGGED
    Date: 2026-10-12

  Common vulnerability: each item treats the ABSENCE of a signal as information, without establishing
    that the channel producing the signal was alive and sensitive.
      - 1682: a null from an instrument that "could observe either outcome" is read as a proper null —
        sensitivity unstated.
      - 1684: "mechanical checks found nothing" is read as "still passes" — no check that the text was
        unchanged since the full review.
      - 991: the proposed loss condition is a threshold over a series whose instrument already froze
        silently (09-03); a miss can be re-attributed to the instrument.
      - 1101: reviewer silence is read as "hold pending decision"; with abandonment, silence actually
        means decisions are being lost.

  Literature basis:
    - ASA/ISA 330 para 16 [full text]: "The absence of misstatements detected by substantive procedures
      ... does not provide audit evidence that controls ... are effective"; paras 13–15: carry-forward
      only with affirmative change-evidence and a bounded horizon.
    - Dienes 2014, Front. Psychol. 5:781 [abstract]: a non-significant result counts against a theory
      only if data sensitivity is shown; otherwise it is insensitivity.
    - St Quinton & Trafimow 2025, Front. Psychol. 16:1633990 [full text]: pre-registered predictions are
      defeated (or rescued) by unregistered auxiliary assumptions — instrument validity chief among them.
    - Reneging-queue results (arXiv:1903.06870) [search-result]: overloaded queues with abandonment
      self-limit; loss appears as abandonment, not depth.

  Risk level: High

  Recommendation (what the system should consider, not a design decision): a single estate-wide rule
    that any "nothing found / no change / no response" reading must carry (a) a liveness statement for
    the channel over the window, and (b) a sensitivity statement (smallest event it would have caught);
    readings lacking either are recorded as INCONCLUSIVE rather than NULL/PASS/HOLD. 13 (pattern
    detector) and 15c could check new findings and dispositions for this pair of fields.
