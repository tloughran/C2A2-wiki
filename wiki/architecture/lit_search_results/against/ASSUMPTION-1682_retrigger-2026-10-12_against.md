SEARCH-AGAINST-ASSUMPTION-1682 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-12
  Original item: ASSUMPTION-1682
  Original statement: FINDING-091 rationale: "The same instrument could observe either outcome, so it
    works as a proper null hypothesis." (Count limb — PRS 867 → 956 — verified by 14a; not under test.)
  Under test this cycle (MONITOR-617, Medium): the 15c net reading — supported as a NECESSARY
    condition, challenged as SUFFICIENT; "wording should carry a power/sensitivity clause"; would tip to
    INCORPORATE if restated as necessary-not-sufficient with a sensitivity requirement. I searched for
    challenges to (a) the criterion and (b) the proposed fix (a power clause).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/ or 15a sections of
    lit_search_returns.md. I read my own cycle-0 file (sources: Mayo 2018; Lakens 2017; Duhem–Quine)
    and did not repeat them. No fetch refused as "already fetched".

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1682
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-09-28): Extracted from bc6bea9e; count verified at source, rationale unverified.
      15a (cycle 0): [not read — independence]
      15b (cycle 0, 2026-09-29): PARTIALLY-CHALLENGED (Moderate) — Mayo, Lakens, Duhem–Quine.
      15c: DISPOSITION-1001 → MONITOR-617 (Medium).
      15d (2026-10-11): re-triggered, cycle 0 → 1.
      15b (cycle 1, 2026-10-12): 2 searches (equivalence/insensitive data; Dienes 2014); 2 fetches
        (Dienes 2014 abstract record; ASA 330 requirements, full text — shared with ASSUMPTION-1684).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: Dienes 2014 [abstract]; ASA/ISA 330 para 16 [full text of requirements];
      equivalence-testing summaries (TOST/SESOI) [search-result only].
    Date: 2026-10-12

  EVIDENCE GRADE: PRELIMINARY — one methods abstract, one standard read in full, one search summary.

  Challenging evidence found: Partial

  Sources:
    1. Dienes, Z. (2014). "Using Bayes to get the most out of non-significant results." Frontiers in
       Psychology 5:781. doi:10.3389/fpsyg.2014.00781. [fetched, abstract only] "No scientific conclusion
       follows automatically from a statistically non-significant result"; to tell a null that counts
       against a theory from mere "data insensitivity" one needs power, intervals, or a Bayes factor;
       Dienes argues power is the weakest of these because it does not use the data themselves to
       determine sensitivity, and power/intervals require a minimal interesting effect. Bearing: this
       challenges MONITOR-617's proposed REMEDY as much as the item. A "power clause" is the weakest
       version of the sensitivity requirement; for a single-instance estate finding (no repeated
       sampling, no conventional power calculation) the defensible clause is "the observed data
       discriminate the outcomes" (a data-based sensitivity statement), not "the instrument had power".
    2. Auditing and Assurance Standards Board (AU), ASA 330 (Dec 2021, conforming to ISA 330),
       Requirements para 16. [fetched, full text of Requirements] "The absence of misstatements detected
       by substantive procedures, however, does not provide audit evidence that controls related to the
       assertion being tested are effective." Bearing: a mature evidence-practice discipline codifies
       that a null from an instrument that COULD have detected the event is not evidence about the
       mechanism of interest unless the instrument was designed to test that mechanism. "Could observe
       either outcome" is a capability statement; the standard asks for a design statement.
    3. Equivalence testing / SESOI summaries (Lakens line; r-bloggers 2016 "Absence of evidence is not
       evidence of absence: Testing for equivalence"; TQMP 19(1)). [search-result only] A null is
       informative only if bounds (smallest effect of interest) were set a priori and the interval falls
       inside them. Bearing: the criterion needs a pre-stated smallest effect, which FINDING-091 does not
       carry.

  Strength of challenge: Moderate (unchanged level; now also challenges the proposed fix)

  Summary: The literature agrees with 15c that "could observe either outcome" is necessary, not
    sufficient. New this cycle: the fix proposed (add a power clause) is itself the weakest form of the
    needed sensitivity requirement. For one-off estate findings, power is often undefined; what is
    needed is (i) a pre-stated smallest effect that matters and (ii) a statement, from the data, that
    the observation discriminates the two outcomes at that size. Auditing practice adds that a null
    tells you nothing about a mechanism the procedure was not designed to probe.

  Specific risks: FINDING-091 (and future findings using the same template) are incorporated with a
    formal-looking power clause that cannot be computed, giving false assurance; nulls from insensitive
    observations accumulate as "proper nulls".

  Mitigations available: restate as: "necessary: the instrument can register either outcome; sufficient
    only with: a pre-stated smallest effect of interest, and evidence from the observation that it
    discriminates outcomes at that size (interval inside bounds, or a Bayes factor away from 1)";
    otherwise label the finding INCONCLUSIVE, not NULL.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1682 / MONITOR-617
  Strongest counterargument: An instrument that can see both outcomes in principle can still be blind
    in practice to effects of the size that matter, and the remedy on the table — "add power" — does
    not fix that for one-off observations where power cannot be computed. Dienes shows that whether a
    null is evidence or mere insensitivity must be read from the data; auditing standards write the
    same rule into law: not finding a problem is not evidence the mechanism works.
  What would need to be true for C2A2 to be safe: each "proper null" states its smallest effect of
    interest in advance and shows the observation could have distinguished it.
  How to test: audit the last 20 FINDING entries labelled null; count how many state a smallest effect
    and a sensitivity statement. Those without are re-labelled INCONCLUSIVE.

  Search scope: preliminary — 2 searches, 2 fetches (one shared with ASSUMPTION-1684).
