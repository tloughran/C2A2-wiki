# Phase A — source verification of the twenty fixture results

*Run 2026-09-01. Every row checked against the published record. Companion machine-readable
file: `pairings.json`. Provenance of the fixture itself: `SOURCE.md`.*

Phase A asked one question of each of the twenty results: **what event does its date name,
and is that date right?** The fixture places nodes on a single `Date Added:` field, so the
answer is load-bearing rather than pedantic — it is the quantity the vertical axis renders
and the quantity `rate_spread` measures.

## The finding: the two arms are measured with different rulers

This is the result Phase A was built to surface, and it is not a bookkeeping complaint.

**The deep-learning arm is nearly uniform.** Seven of ten rows place on the **arXiv v1
submission timestamp** — one event type, defined identically for every row, verifiable to
the minute. All seven were confirmed exact against arXiv; not one needed correcting. The
other three (AlexNet, AlphaGo, AlphaFold 2) have no arXiv preprint to place on, and each
is correct for the event it does name.

**The quantum arm uses seven different event types across ten rows**, plus one row with no
event at all, and two of the ten are placeholders rather than dates:

| row | date carried | what that date actually names |
|---|---|---|
| Planck | 1900-12-14 | presentation to the German Physical Society |
| Einstein | 1905-03-17 | **wrong** — journal receipt was 1905-03-18 |
| Bohr | 1913-07-01 | **month placeholder** — Part I is July 1913, day not established |
| Compton | 1922-12-01 | conference announcement (APS Chicago, 1–2 Dec 1922) |
| de Broglie | 1924-11-25 | thesis defence |
| Pauli | 1925-01-16 | journal submission |
| Heisenberg | 1925-07-29 | journal receipt |
| Schrödinger | 1926-01-27 | journal receipt |
| Dirac | 1930-05-29 | book publication — **and three results conflated**, see below |
| von Neumann | 1932-01-01 | **placeholder** — Jan 1 is not a date, it is an absence |

The compression claim the fixture exists to test — 32 years against 13 — is computed from
these two columns. **One column is a single well-defined quantity; the other is six
quantities in a trenchcoat, two of which are missing values dressed as measurements.**

And the deeper problem is that this cannot simply be repaired by picking one convention.
There is no 1925 arXiv. For the quantum arm, "the moment the result entered the record"
genuinely was a lecture for Planck, a defence for de Broglie, and a journal receipt for
Heisenberg. **The event type the deep-learning arm uses does not exist for the quantum
arm**, so a like-for-like comparison of the two spans is not available at the resolution
the axis renders.

That does not sink the compression claim. It does mean the claim is about **eras**, and
the axis is drawing it as though it were about **timestamps** — which is a different
statement with a false precision attached. Anyone quoting a rate ratio off this fixture
should quote it to the year, never the day.

## Defects found, ranked

1. **Dirac PRS-09 conflates three separate results.** The row is labelled 1930 and sourced
   to *The Principles of Quantum Mechanics*, but its Resource names the 1927 transformation
   theory *and* the relativistic wave equation, and its Solution claims spin, the magnetic
   moment and the prediction of antimatter — all consequences of the **January 1928**
   equation (submitted 2 Jan 1928, published 1 Feb 1928), not of the 1930 textbook. The
   precise date carried, 1930-05-29, is also unverifiable: sources place the book in
   "summer 1930" with no day. **Split into two rows or pick one.** As it stands the row
   asserts a 1928 achievement at a 1930 coordinate.
2. **von Neumann PRS-10 carries a placeholder.** 1932-01-01. The book is 1932; the day is
   not known and was invented to fill the field.
3. **AlphaGo PRS-03 (DL): the date and the claim point at different events.** Dated
   2016-01-28 (the *Nature* issue; online 27 Jan), while the Solution text cites the 4–1
   win over Lee Sedol, played 9–15 March 2016. Six weeks apart, and the row's own argument
   rests on the later one.
4. **Einstein PRS-02 is one day early.** 1905-03-17 carried; *Annalen der Physik* received
   it 18 March 1905.
5. **Bohr PRS-03 carries a month placeholder.** July 1913 is right; the 1st is filler.
6. **Compton PRS-04 places on announcement.** 1–2 Dec 1922 at the APS Chicago meeting is
   real and correctly dated, but it is a third convention again — submission was 13 Dec
   1922, publication May 1923. Worth stating that the row chooses announcement on purpose.
7. **AlexNet and AlphaFold 2 diverge from their own arm's convention.** AlexNet's
   2012-12-03 is the NeurIPS conference opening (3–6 Dec 2012, Lake Tahoe); there is no
   arXiv preprint. AlphaFold 2's 2021-07-15 is *Nature* online publication (received
   11 May 2021, accepted 12 July). Both dates are correct for what they name; neither is
   the arXiv-submission event the other eight rows use.

## Two prior suspicions that turned out to be wrong

Recorded because a cleared suspicion is worth as much as a confirmed one.

- **Pauli PRS-06 does not blur exclusion with spin.** The handoff warned that it did. It
  does not: the Resource says "a fourth two-valued quantum number," which is precisely
  Pauli's own January 1925 formulation, and spin is never claimed. The physical reading of
  that two-valuedness is Uhlenbeck and Goudsmit, *Naturwissenschaften*, letter dated
  17 October 1925 — different people, different result, and correctly absent here.
- **GPT-3 / DDPM are already in the right order.** GPT-3 arXiv v1 is 28 May 2020; DDPM is
  19 June 2020. The fixture has them that way round, so the fixture is correct.

  *Corrected later the same day, once the source image was supplied:* the reason given here
  first was wrong. The image **does** assert an ordering — it is a row of dominoes read
  left to right — and it places **DDPM before GPT-3**. So this is not a cleared suspicion
  but a real divergence in which the fixture follows the record and the image does not.
  See `SOURCE.md`.

## Row-by-row verification

Legend — **status**: `exact` (fixture date matches the record), `off-by-N`,
`placeholder` (a real date does not exist in the fixture), `mismatch` (date and claim name
different events), `conflated` (row covers more than one result).

### Quantum mechanics

| # | result | fixture date | event named | record | status |
|---|---|---|---|---|---|
| 01 | Planck, quantum of action | 1900-12-14 | DPG presentation | 14 Dec 1900; *h* enters here. The 19 Oct 1900 talk gave the empirical law without *h* | exact |
| 02 | Einstein, light quantum | 1905-03-17 | journal receipt | received 18 Mar 1905, *Annalen der Physik* 17, 132–148 | off-by-1 |
| 03 | Bohr, quantised atom | 1913-07-01 | publication | *Phil. Mag.* trilogy Part I, July 1913 (Parts II, III Sept, Nov) | placeholder (month right) |
| 04 | Compton, quantum momentum | 1922-12-01 | conference announcement | read at APS Chicago 1–2 Dec 1922; submitted *Phys. Rev.* 13 Dec 1922; published May 1923 | exact for announcement |
| 05 | de Broglie, matter waves | 1924-11-25 | thesis defence | defended 25 Nov 1924; published *Annales de Physique* early 1925 | exact |
| 06 | Pauli, exclusion principle | 1925-01-16 | submission | submitted 16 Jan 1925 | exact |
| 07 | Heisenberg, matrix mechanics | 1925-07-29 | journal receipt | received 29 Jul 1925, *Z. Phys.* 33, 879–893 | exact |
| 08 | Schrödinger, wave equation | 1926-01-27 | journal receipt | received 27 Jan 1926, *Ann. Phys.* — "Quantisierung als Eigenwertproblem" I | exact |
| 09 | Dirac, unification + relativistic electron | 1930-05-29 | book publication | *Principles* summer 1930 (no day sourced); relativistic equation submitted 2 Jan 1928, published 1 Feb 1928, *Proc. R. Soc. A* 117, 610–624; transformation theory 1927 | conflated + unsourced day |
| 10 | von Neumann, foundations | 1932-01-01 | — | *Mathematische Grundlagen der Quantenmechanik*, 1932; no day | placeholder |

### Deep learning

| # | result | fixture date | event named | record | status |
|---|---|---|---|---|---|
| 01 | AlexNet | 2012-12-03 | conference opening | NeurIPS 2012, 3–6 Dec, Lake Tahoe; no arXiv preprint | exact for conference |
| 02 | ResNet | 2015-12-10 | arXiv v1 | arXiv:1512.03385 v1, 10 Dec 2015 19:51:55 UTC | exact |
| 03 | AlphaGo | 2016-01-28 | *Nature* issue | issue 28 Jan 2016, online 27 Jan; **Lee Sedol match 9–15 Mar 2016** | mismatch (claim cites the match) |
| 04 | Transformer | 2017-06-12 | arXiv v1 | arXiv:1706.03762 v1, 12 Jun 2017 | exact |
| 05 | Neural scaling laws | 2020-01-23 | arXiv v1 | arXiv:2001.08361 v1, 23 Jan 2020 03:59:20 UTC | exact |
| 06 | GPT-3 | 2020-05-28 | arXiv v1 | arXiv:2005.14165 v1, 28 May 2020 | exact |
| 07 | DDPM | 2020-06-19 | arXiv v1 | arXiv:2006.11239 v1, 19 Jun 2020 | exact |
| 08 | AlphaFold 2 | 2021-07-15 | *Nature* online | received 11 May 2021, accepted 12 Jul, published online 15 Jul 2021 | exact for publication |
| 09 | InstructGPT / RLHF | 2022-03-04 | arXiv v1 | arXiv:2203.02155 v1, 4 Mar 2022 07:04:42 UTC | exact |
| 10 | DeepSeek-R1 | 2025-01-22 | arXiv v1 | arXiv:2501.12948 v1, 22 Jan 2025 | exact |

## What Phase A does not yet deliver

**Provenance note, added after the source image was supplied.** All twenty names and all
twenty *years* come from the image and match the fixture exactly; the fixture is sourced at
that level. What remains Claude-authored is the triplet prose, the **month and day** on
every date, and the six cross-connections. That matters for the ruler finding above rather
than weakening it: the image asserts years, and the day-level precision the fixture renders
was invented on top of them, drawn from seven kinds of event in the quantum row alone.

Phase A verified **dates and citations**. It did **not** do Phase B (coding the twenty
against a typed vocabulary of cascade roles) or Phase C (rebuilding the cross-links from
role and problem-structure rather than column position). The six cross-connections in
`vault/master/cross_program_index.md` remain Claude-authored and unvalidated — per
`SOURCE.md`, the source asserts no pairings at all, so there is nothing external to check
them against. **The fixture is not yet a labelled evaluation set.** Phases B and C are what
would make it one.
