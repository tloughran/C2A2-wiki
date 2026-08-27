#!/usr/bin/env python3
"""Tests for scripts/ingest_ledger.py.

Every assertion here is driven through its FAILURE path: each fixture is built so the
buggy behaviour would produce a different answer than the fixed behaviour. Tests that
cannot fail when the logic changes are not tests (Rule 9).

The two regression tests at the end encode WHY the two defects mattered, not just that
the regexes changed:
  - ASCII arrow: 61 live log lines used it and were invisible to the old gate.
  - SUPP id shape: the Hawkins supplement produced 6 triplets and was still read as
    un-ingested, causing a re-derivation that qc_prs.py had to clean up downstream.

    python3 scripts/test_ingest_ledger.py
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ingest_ledger as il  # noqa: E402

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append("%s\n     got:  %r\n     want: %r" % (name, got, want))
        print("FAIL  %s" % name)
    else:
        print("ok    %s" % name)


def build_vault(root, triplets=None, log="", approved=None, staging=None):
    """Minimal vault: traditions/<t>/prs_triplets.md, inbox/PROCESSED_LOG.md, queues."""
    for trad, body in (triplets or {}).items():
        d = os.path.join(root, "traditions", trad)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "prs_triplets.md"), "w").write(body)
    os.makedirs(os.path.join(root, "traditions"), exist_ok=True)
    inbox = os.path.join(root, "inbox")
    os.makedirs(inbox, exist_ok=True)
    open(os.path.join(inbox, "PROCESSED_LOG.md"), "w").write(log)
    ap = os.path.join(inbox, "proposals", "approved")
    os.makedirs(ap, exist_ok=True)
    for fn, body in (approved or {}).items():
        open(os.path.join(ap, fn), "w").write(body)
    pend = os.path.join(inbox, "proposals", "pending")
    os.makedirs(pend, exist_ok=True)
    # pending card that is NOT ingested -- must never be counted as open
    open(os.path.join(pend, "2026-08-01_levin_awaiting-decision.md"), "w").write(
        "---\nproposal_id: PROP-2026-08-01-999\n---\n")
    for fn, body in (staging or {}).items():
        open(os.path.join(inbox, fn), "w").write(body)
    return root


def card(pid):
    return "---\nproposal_id: %s\ntradition_key: levin\n---\n\nPRS-CANDIDATE-01:\n" % pid


def run():
    tmp = tempfile.mkdtemp()
    try:
        # ---- 1. tradition-file citation is recognised (source A) ----------------
        v = build_vault(os.path.join(tmp, "v1"),
                        triplets={"levin": "PRS-01:\n  Label: P1 (PROP-2026-05-01-001)\n"},
                        approved={"2026-05-01_levin_a.md": card("PROP-2026-05-01-001"),
                                  "2026-05-02_levin_b.md": card("PROP-2026-05-02-001")})
        d = il.survey(v)
        check("tradition citation marks a card ingested",
              d["queues"]["approved"]["open"], 1)
        check("the open one is the uncited card",
              d["queues"]["approved"]["open_files"][0]["proposal_id"], "PROP-2026-05-02-001")

        # ---- 2. pending/ is never counted -------------------------------------
        check("pending queue is not surveyed", "pending" in d["queues"], False)

        # ---- 3. REGRESSION: ASCII arrow in the log (defect 1) -------------------
        # Old gate matched only U+2192, so this line was invisible and the card
        # would have been reported OPEN. 61 live log lines have this shape.
        v = build_vault(os.path.join(tmp, "v2"),
                        triplets={"levin": "PRS-01:\n  nothing cited here\n"},
                        log="- PROP-2026-05-03-001 levin_x -> levin PRS-42 (+1)\n",
                        approved={"2026-05-03_levin_x.md": card("PROP-2026-05-03-001")})
        check("ASCII '->' ingestion line is recognised",
              il.survey(v)["queues"]["approved"]["open"], 0)

        # ---- 4. Unicode arrow still works (do not regress the fix) -------------
        v = build_vault(os.path.join(tmp, "v3"),
                        triplets={"levin": "PRS-01:\n  nothing cited here\n"},
                        log="- PROP-2026-05-04-001 levin_y → levin PRS-43 (+1)\n",
                        approved={"2026-05-04_levin_y.md": card("PROP-2026-05-04-001")})
        check("Unicode arrow ingestion line is recognised",
              il.survey(v)["queues"]["approved"]["open"], 0)

        # ---- 5. REGRESSION: SUPP-shaped proposal id (defect 2) ------------------
        # The real case: hawkins PRS-10..15 all carry PROP-2026-04-09-SUPP-001.
        # Old id regex could not match it, so the card was re-staged and six
        # duplicate triplets were re-derived before qc_prs.py dropped them.
        v = build_vault(os.path.join(tmp, "v4"),
                        triplets={"hawkins": "PRS-10:\n  Label: P10 (PROP-2026-04-09-SUPP-001)\n"},
                        approved={"2026-04-09_hawkins_supp.md": card("PROP-2026-04-09-SUPP-001")})
        check("SUPP-shaped proposal id is recognised as ingested",
              il.survey(v)["queues"]["approved"]["open"], 0)

        # ---- 6. placeholder '00x' id shape -------------------------------------
        v = build_vault(os.path.join(tmp, "v5"),
                        triplets={"hoffman": "PRS-18:\n  Label: (PROP-2026-07-28-00x)\n"},
                        approved={"2026-07-28_hoffman_z.md": card("PROP-2026-07-28-00x")})
        check("placeholder '00x' id is recognised as ingested",
              il.survey(v)["queues"]["approved"]["open"], 0)

        # ---- 7. '+0' / HELD is a DECIDED outcome, not a gap --------------------
        # This is the distinction that separates OPEN=5 from OPEN=20 on the live
        # vault. A card the pipeline looked at and deliberately yielded nothing on is
        # not backlog. It must be counted, named, and kept OUT of open.
        v = build_vault(os.path.join(tmp, "v6"),
                        triplets={"levin": "PRS-01:\n  nothing\n"},
                        log="- PROP-2026-06-01-001 levin_held -> levin +0 triplets [HELD]\n",
                        approved={"2026-06-01_levin_held.md": card("PROP-2026-06-01-001")})
        d = il.survey(v)
        check("a '+0' outcome is NOT counted as open", d["queues"]["approved"]["open"], 0)
        check("a '+0' outcome is counted as decided-zero",
              d["queues"]["approved"]["decided_zero"], 1)
        check("a '+0' outcome is not counted as ingested",
              d["queues"]["approved"]["ingested"], 0)

        # ---- 7b. a card mentioned in the log with NO outcome stays OPEN --------
        # The failure mode in the other direction: a bare mention (a deposit line)
        # must not clear a card. This is what the earlier slug-presence test got wrong.
        v = build_vault(os.path.join(tmp, "v6b"),
                        triplets={"levin": "PRS-01:\n  nothing\n"},
                        log="Phase 2: levin deposited PROP-2026-06-02-001 today.\n",
                        approved={"2026-06-02_levin_deposit.md": card("PROP-2026-06-02-001")})
        check("a bare deposit mention does not clear a card",
              il.survey(v)["queues"]["approved"]["open"], 1)

        # ---- 7c. ingested wins over a zero marker on the same id --------------
        v = build_vault(os.path.join(tmp, "v6c"),
                        triplets={"levin": "PRS-09:\n  Label: (PROP-2026-06-03-001)\n"},
                        log="- PROP-2026-06-03-001 levin_x -> levin no-net-new (+0)\n",
                        approved={"2026-06-03_levin_x.md": card("PROP-2026-06-03-001")})
        d = il.survey(v)
        check("tradition citation outranks a zero marker",
              (d["queues"]["approved"]["ingested"], d["queues"]["approved"]["decided_zero"]),
              (1, 0))

        # ---- 8. a card with no proposal_id is surfaced, not silently counted ----
        v = build_vault(os.path.join(tmp, "v7"),
                        triplets={"levin": "PRS-01:\n"},
                        approved={"2026-06-02_levin_nopid.md": "---\ntradition_key: levin\n---\n"})
        d = il.survey(v)
        check("card with no proposal_id is reported separately",
              len(d["no_proposal_id"]), 1)
        check("card with no proposal_id is not counted as open",
              d["queues"]["approved"]["open"], 0)

        # ---- 9. planted un-ingested card moves the count (the falsifier) -------
        v = build_vault(os.path.join(tmp, "v8"),
                        triplets={"levin": "PRS-01:\n  Label: (PROP-2026-05-01-001)\n"},
                        approved={"2026-05-01_levin_a.md": card("PROP-2026-05-01-001")})
        before = il.survey(v)["queues"]["approved"]["open"]
        open(os.path.join(v, "inbox", "proposals", "approved", "2026-08-26_levin_planted.md"),
             "w").write(card("PROP-2026-08-26-001"))
        after = il.survey(v)["queues"]["approved"]["open"]
        check("planting one un-ingested card raises OPEN by exactly 1", after - before, 1)

        # ---- 10. staging queue is surveyed independently ------------------------
        v = build_vault(os.path.join(tmp, "v9"),
                        triplets={"levin": "PRS-01:\n"},
                        staging={"2026-04-08_levin_stage.md": card("PROP-2026-04-08-001"),
                                 "PROCESSED_NOTES.md": "not a card\n"})
        d = il.survey(v)
        check("staging queue counts only dated cards", d["queues"]["staging"]["total"], 1)
        check("un-ingested staging card is open", d["queues"]["staging"]["open"], 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if FAILS:
        print("%d FAILED" % len(FAILS))
        for f in FAILS:
            print("  - %s" % f)
        return 1
    print("all assertions passed")
    return 0


if __name__ == "__main__":
    sys.exit(run())
