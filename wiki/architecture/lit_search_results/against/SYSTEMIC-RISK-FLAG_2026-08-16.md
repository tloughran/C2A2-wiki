SYSTEMIC-RISK-FLAG:
  Date: 2026-08-16
  Filed by: Agent 15b (two independent searchers, disjoint item sets, no sight of each other's work)
  Escalated by 15c as: REVISE-340 (High)
  Affected items: ASSUMPTION-1086, 1094, 1096, 1097; PRESUMPTION-808, 809, 810, 811, 812, 813, 814,
    815, 816, 817 — i.e. the entire 2026-08-15 intake cohort.

## WHY THIS IS ONE FLAG AND NOT TWO

Two 15b searchers were given disjoint item sets and were forbidden to read each other's output or the
supportive direction's files. Each independently concluded that the cohort shares a defect, and each
described it in its own vocabulary. The two descriptions are the same defect seen from the two ends of
an item: one searcher looked at what the items MEASURE, the other at what the items PROPOSE. The
convergence is the evidence. Both wordings are preserved below rather than merged, because merging them
would destroy the fact that they were arrived at separately (PREMISE-120).

## COMMON VULNERABILITY (A) — as filed by the assumptions searcher

All four assumptions propose to change an INSTRUMENT, A RULE, OR A RECORD on the strength of a
measurement produced INSIDE the thing being changed, with no out-of-band referent. In three of the four,
the proposed change DESTROYS THE EVIDENCE that would have permitted the check:

  - ASSUMPTION-1086 compares two instrument generations with different denominators (78+4+0 = 82 checks
    against 78+1+5 = 84) across a documented instrument replacement, and reads the identical OK count as
    a control. PREMISE-105 forbids the reading; the coincidence is doing the work.
  - ASSUMPTION-1094 reads a six-of-six rate from runs that the band table itself triggered. The
    denominator is undeclared and there are zero recorded propagations to compare against.
  - ASSUMPTION-1096 licenses a 307-field recount that ERASES THE PRIOR VALUES, on an unaudited single
    channel, before anyone has read the two parsers whose disagreement is the whole dispute.
  - ASSUMPTION-1097 proposes moving a boundary using the judgment of the parties who breached it, on a
    gauge whose measurement error consumes 30-50% of the tolerance.

Literature basis, convergent across four unrelated fields: total-survey-error theory and Mahalanobis's
interpenetrating subsamples (sample estimates are often more accurate than complete enumeration, and
non-sampling error rises with operation size); the U.S. Post-Enumeration Survey, which exists to audit a
census with a sample; Park et al. (MSR 2012) and Google Project Zero on checking the instance rather
than the mechanism; and the Rogers Commission on waivers granted inside the office producing them.

## COMMON VULNERABILITY (B) — as filed by the presumptions searchers

The items' CORRECTIVES are drafted without a register pre-check. The diagnoses are mostly sound; the
remedies are where the failure concentrates, and in four cases the register has ALREADY CONSIDERED AND
EXPLICITLY EXCLUDED the proposed remedy:

  - PRESUMPTION-813 proposes a carrier swap. PREMISE-125 records that this fleet already added a second
    path to THIS channel and availability went DOWN.
  - PRESUMPTION-814 proposes a production throttle. PREMISE-119 (2026-07-21) contains a named
    `EXCLUDED:` clause against exactly that remedy, with the arithmetic: where service is zero, no
    reduction in arrivals bounds the queue.
  - PRESUMPTION-815 proposes "two undefined measurands, both correct" as a general disposition.
    PREMISE-114's definitional exit holds the opposite for frozen-snapshot quantities, where convergence
    is the EXPECTED outcome and the remedy is to write the counting definition.
  - PRESUMPTION-817 proposes publishing a refutation rate. PREMISE-143 already holds that a retraction
    count measures the PRODUCING layer, and PREMISE-117's publish-then-revise standard already governs
    the prose side.

Additionally: 808 restates PREMISE-141's explicit open scope limit; 809 restates PREMISE-086/100/110;
810 runs against PREMISE-162's validated remedy; 811 restates PREMISE-135's warrant conditions; 812
restates PREMISE-102. The consequences are grade inflation, register duplication (PREMISE-105), and —
later and worse — FALSE INDEPENDENT CORROBORATION when a duplicate is cited as a second source
(PREMISE-111, PREMISE-120).

## RISK LEVEL

High. Not Critical, and the reason is worth stating: the DIAGNOSES in this cohort are largely correct
and several are valuable. The failure is confined to grading and to remedy selection, and both are
recoverable at the intake gate. What raises it above Moderate is that this is the SECOND CONSECUTIVE
NIGHT in the same family — REVISE-335 and REVISE-336 were filed on 2026-08-15 for the frame-provenance
and unidentified-number versions of the same intake defect — and that the corrective proposed for it
last night has not been implemented.

## THIS IS AN ENFORCEMENT GAP, NOT A KNOWLEDGE GAP

PREMISE-096 ("no self-produced artefact may certify itself"), PREMISE-124 (nothing uncalibrated against
an external baseline is a measurement) and PREMISE-164 already hold the principle. Per PREMISE-138
clause (1), repetition inside a channel with no effector is not a remedy, and per PREMISE-135
terminality is not purchased by accumulating instances. NO NEW PREMISE IS MINTED FOR THIS FLAG. Per
PREMISE-143 clause (3), the instrument-defect record this implies outlives the run that filed it and is
NOT CLOSABLE BY THAT RUN — including this one.

## RECOMMENDATION (requires Tom; amends two agent contracts)

  1. PRECONDITION ON INTAKE: an item whose remedy is a change to an instrument, rule or record may not
     be queued until it NAMES ITS OUT-OF-BAND REFERENT and states whether the change destroys the
     evidence for that check.
  2. `REGISTER-CHECKED:` FIELD ON THE REMEDY CLAUSE, not only on the diagnosis. An item whose remedy the
     register explicitly excludes must cite that exclusion and argue against it, or be filed as a
     re-mint under PREMISE-138.

Both are one line in each of the 14a and 14b contracts. Neither is actionable by 14a or 14b themselves
under PREMISE-096, because they would be amending their own intake gate.

## THE OBSERVATION MOST WORTH CARRYING FORWARD

From the 808-812 searcher, and it is the highest-value item in this file. In PRESUMPTION-809 the real
defect is not the presumption at all: it is that AN ACTIVE PREMISE WAS UNENFORCED ON A SURFACE NOBODY
MEASURED. PREMISE-086 — alarm on the age of the last dated result — was live and ACTIVE for the entire
period during which three launchd agents sat at `runs = 0`. Nothing in this architecture measures
PREMISE-TO-INSTRUMENT DIVERGENCE: the count of ACTIVE premises that have no instrument on the surface
they govern. It is cheap to produce — for each ACTIVE premise, name the instrument that would detect its
violation, or record that none exists — and on this evidence it is the highest-value unwritten number in
the system.

## DECLARED LIMITATIONS OF THIS FLAG

  - Both filings rest on register checks performed with the string grep that ASSUMPTION-1052 measured at
    ~56% recall. Every "the register already holds X" claim above is a LOWER BOUND on the overlap, and
    the replacement instrument has still not been built (sixth consecutive night).
  - Per PREMISE-124 the convergence between the two searchers is not a calibrated measurement. They
    share a model, a contract, and a prompt structure; per PREMISE-120 that is a re-run sharing
    components, not two independent observations, and it is recorded as such. The independence that WAS
    preserved is of item sets and of written output, not of method.
  - Neither searcher read the supportive direction. Where 15a found genuine support for an item's
    remedy, that is not reflected here and is reflected in the 15c dispositions instead.
