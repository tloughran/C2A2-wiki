# Reconstruction as a third evidence class — the run, and its control

*2026-09-07. Scope: Tom's proposal that where the record does not state a dependency,
an argument for it can still be constructed and checked against the record.*

Harness: `../scripts/prs_reconstruct.py`. Data: `reconstructions.json` (batch 1),
`reconstructions_hard_controls.json` (batch 2).

---

## The question

`attested` **cites**. The proposal is a class that **argues**: show that solution S1 has
resource R1's shape, that S1 does not stand without R1, and that R1 was available. At
the frontier we should expect many links to be like this — reconstructible but never
written down, because the concept had no name yet, or transmission was a hallway rather
than a bibliography, or the technique became infrastructure and went invisible precisely
by being universal.

The risk is equally specific. **A model asked to construct an argument for a link will
nearly always succeed.** Producing a plausible mechanism is the thing language models are
best at and least trustworthy at. Added without a control this class manufactures a
dense, elegant, entirely fictional connectome that looks *better* than the real one. So
the control shipped in the same commit as the capability.

## What makes an argument checkable

The form demands commitments a bogus pair cannot honestly meet:

| field | what it forces |
|---|---|
| `component` | the specific part of S1 that fails without R1 — a part, not a topic |
| `necessity` | `required` / `used` / `dispensable` / `none` |
| `alternatives` | what else was on offer at the time |
| `exclusivity` | `sole` / `few` / `many` |
| `trace` | a verbatim phrase, **machine-checked against the corpus**, or an external citation with a locator |
| `refuters` | what would falsify this, stated before anyone looks |

`insufficient` is a first-class outcome. If it is never used, the test is rigged.

## Result

**Batch 1 — 20 items, shuffled, conditions withheld from the worksheet**

```
condition            n  reconstructed  insufficient nec=required  chkfail
target               8           100%            0%         75%        0
control_ruled_out    3             0%          100%          0%        0
control_random       9             0%          100%          0%        0
```

Batch 1's random controls were too easy: 6 of 9 were cross-epoch (Compton → AlexNet),
refusable without thought. So a second batch was drawn from the population that actually
resembles the connectome.

**Batch 2 — 10 hard controls: within-tradition, forward in time, none in the answer key**
(pool of 66, seed 20260902)

```
10 items, 1 reconstructed (10%), 0 trace-check failures
```

**Combined controls: 1 of 22.** And the one is not a fabrication.

**Trace verification: 17 of 17 `in_corpus` traces are verbatim substrings of the target
entry**, checked against the real corpus files. One trace is `in_literature` with a
citation locator.

## The one control that reconstructed was a defect in the answer key

**H07, Planck → Compton.** The Compton shift is `h/(m_e·c)·(1 − cos θ)`. Planck's
constant is a term in the predicted formula, not context. Remove h and the collision
calculation predicts no specific shift and cannot be compared with the measurement.

The key held **Einstein → Compton** (the light-quantum ontology) and had silently treated
that as the whole of Compton's inheritance. Two distinct components, two distinct
dependencies. The pair was drawn as a "random control" *because the key was incomplete*.

**The row has been added** (`quantum-PRS-01 → quantum-PRS-04`, textual `unexpressed` —
the Compton entry names neither Planck nor h), and the criteria numbers in `CRITERIA.md`
were regenerated against the corrected key.

Two things follow, and both are uncomfortable:

1. Scored conservatively as a control failure the rate is 1/22 (5%); scored as what it
   is, 0/22 fabrications with one key gap found. **Both readings belong in any quotation
   of this result.** The control population is contaminated with unlabelled true
   positives, which weakens the clean separation as evidence.
2. **The criteria had already proposed this pair** and it sat in the false-positive list
   as `quantum-PRS-01 → quantum-PRS-04 … 4.95 matching` — flagged for the wrong reason
   (shared benchmark-ish vocabulary), and dismissed by me. Labelling that list
   "unexamined, not wrong" rather than "false positives" turned out to be load-bearing.

## The four refusals that carry the weight

Anyone can refuse Pauli → DDPM. These had fluent arguments available and were refused:

- **R18, Heisenberg → Schrödinger.** The target names the source prominently, and the
  naming criterion C1 fires at strength 7.80 — third-highest in the corpus, from the tier
  that is otherwise precision 1.00. Refused: matrix mechanics is what wave mechanics is
  *contrasted with*, not built from. **Reconstruction is what separates a prominent
  mention from a dependency**, which is the whole question.
- **R10, Bohr → Dirac.** Refused for *transitivity*. Bohr reaches Dirac through
  Heisenberg and Schrödinger, both separately in the corpus. Admit transitive ancestry
  and the graph becomes its own transitive closure and says nothing.
- **H10, Pauli → Heisenberg.** Six months apart, same institutional circle, overlapping
  problem (the anomalous Zeeman effect). Refused as *contemporaries with a shared
  problem* — the reconstruction form of criterion C5, and the pair most likely to fool a
  vocabulary method.
- **H08, Einstein → Dirac.** Refused on *entry identity*. The tempting move credits
  Einstein for the relativity in Dirac's relativistic equation — but that is a different
  1905 paper, and this entry is specifically the light quantum. Crediting an entry with
  its author's other work is a distinct failure mode worth naming.

## The case that justifies the class

**R15, ResNet → Transformer.** Every Transformer sub-layer is wrapped in a residual
connection and the architecture does not train without it. Our corpus is *completely
silent*: the fixture's Transformer entry lists self-attention, positional encodings and
multiple heads and never mentions the residual stream. The lexical baseline scores the
pair 0.029 on a stopword leak; naming and inheritance both find nothing.

The argument reaches it, and the trace is external and citable — *Attention Is All You
Need*, §3.1, "a residual connection around each of the two sub-layers", citing He et al.
2016.

Necessity was `required` for 6 of 8 targets. The two weaker ones are recorded as weaker:
AlphaGo → DeepSeek R1 (`used`, exclusivity `many` — a family resemblance with a plausible
channel, not a required input) and Pauli → Dirac (`used` — a constraint the later work
must satisfy, not material it is built from).

## What this test is not

- **Not a blind trial.** The same model authored the reconstructions and knows the
  history of both traditions. Withholding conditions blinds the author to the *sampling
  condition*, not to the subject matter. What carries the weight is the structured
  commitments and the machine-checked trace, not ignorance. A real blind would need a
  second model instance with the pair identities stripped, which the prose makes hard.
- **Small n.** 8 targets, 22 controls.
- **One pair was duplicated** across batches (AlexNet → RLHF, as R16 and H03). Answered
  identically both times — the only consistency check this run contains. Batch 2 has 9
  fresh items, not 10.
- **Batch 1's control pool deviates from the harness's design.** `prs_reconstruct.py`
  samples pairs the criteria rejected; the run happened while the repo was unreadable, so
  batch 1 sampled forward pairs absent from the answer key instead. That is a *harder*
  population, not an easier one, but it is not the same one. Re-run the harness as
  written before treating batch 1's control rate as final.
- **The run was authored against a transcribed corpus.** Documents access was revoked
  mid-session, so the twenty entries were re-typed from context. On restore, all 17
  in-corpus traces were verified verbatim against the real files and the JSON was
  regenerated into the repo. That is good evidence of fidelity for the quoted phrases
  specifically, and not a guarantee about unquoted prose.

## The designed re-run, 2026-09-07 — and why its numbers are now provisional

Batch 1's control pool deviated from the harness as written: it sampled forward pairs
absent from the answer key, rather than pairs the criteria had actually rejected. The
harness was re-run as designed over 21 items (9 target, 3 ruled-out control, 9 random
control), 12 reconstructions reused and 9 newly authored, scored in
`SCORE_designed.txt`:

| condition | n | reconstructed | insufficient |
|---|---|---|---|
| target | 9 | **100%** | 0% |
| control_ruled_out | 3 | 0% | 100% |
| control_random | 9 | 11% | 89% |

Verdict: targets 100%, controls 8% — **MIXED**, separation real but controls not clean.

The single control positive is item **R15, Planck → Dirac**, argued from an
`in_literature` trace (Dirac, *Principles*, 1930, Ch. IV: the quantum conditions are posed
as qp − pq = i(h/2π)). That is the *second* control positive to turn out to be a gap in
the answer key rather than a fabrication, and it is what set off the h-denomination audit.

**Both consequences have to be stated together.** The audit added four rows to the key, so
the numbers above were computed against a key that no longer exists. `build_sample` draws
its targets from `attested` rows the corpus cannot express, and all four additions are
exactly that, so the target set grows from 9 to 13 and the random pool shrinks. The
worksheet must be regenerated and the four new items authored before this table is quoted
again. It is left standing, with this warning attached, because deleting a measurement
because its key improved is how a project loses the record of why it improved.

A second fix shipped alongside: `check_row` demanded a `trace` and a `trace_kind` of every
row, so all ten honest `insufficient` rows — complete in every other field — were printed
as failing their checks. A verdict of `insufficient` has no trace by construction. It is
now accepted with `trace_kind: "none"`, and only on an `insufficient` verdict; a
`reconstructed` row with no trace still fails, and the verbatim in-corpus check is
untouched. No rate in the table above moved.

## Re-run against the 32-row key, 2026-10-06

The worksheet was regenerated (`worksheet_designed.md`, `reconstruction_key.json`): 25
items, 13 target, 3 ruled-out control, 9 random control from a pool of 150. 15 items are
pairs already authored in an earlier batch and were carried over by pair, re-labelled to
their new item ids. The other 10 were authored **blind by a separate agent** that was
given only those 10 worksheet entries — not the key, not the earlier authorings, not this
file, which names the h-denomination pairs. That is a stronger blind than the earlier
runs, where the author had seen the key's construction. It is still the same model family
and still knows the history of physics; the caveat in "Not a blind trial" stands.

Scored in `SCORE_designed_2026-10-06.txt`; `SCORE_designed.txt` stays as the 09-07 record.

| condition | n | reconstructed | insufficient |
|---|---|---|---|
| target | 13 | **100%** | 0% |
| control_ruled_out | 3 | 0% | 100% |
| control_random | 9 | 11% | 89% |

Verdict unchanged: targets 100%, controls 8% — **MIXED**. All four h-denomination targets
reconstructed; three of them (Planck → de Broglie, → Heisenberg, → Schrödinger) were
authored by the blind agent with `in_corpus` traces that pass the verbatim check, and the
fourth (Planck → Dirac) is the reused 09-07 row.

**The one control positive is R20, Schrödinger → von Neumann** (`quantum-PRS-08 →
quantum-PRS-10`, necessity `used`): von Neumann's Hilbert space is argued to unify the
function-space (wave mechanics) and sequence-space (matrix mechanics) realisations, with
the spectral treatment of Schrödinger's differential Hamiltonian as the component. This
is **not** the von Neumann row refused in the 09-09 audit — that refusal was about
*Planck's h* reaching von Neumann, and this is *Schrödinger's wave mechanics* reaching
him. Whether it is a third gap in the key or the control decaying into narrative is a
human ruling, not this harness's; it is recorded here unruled.

**Harness fix.** The 09-09 exemption for declines never took effect: `check_row` loops
over every required field before reaching it, so a blank `trace` on an `insufficient` row
still failed. The earlier declines passed only because their authors typed filler into
`trace` ("No trace in the 2016 system."). The blind agent left `trace` blank and, on
cross-epoch pairs with no component, `alternatives` empty; six honest declines read as
FAIL. Declines with `trace_kind: "none"` are now exempt from both fields. Exercised both
ways: those six pass, and R08 with its trace stripped still fails. No rate moved.

## Recommended

1. **Add `reconstructed` as a fifth status**, with the row carrying the argument — claim,
   component, necessity, alternatives, trace, refuters — never a flag. A reader must be
   able to attack the reasoning.
2. **Re-audit the answer key for missing component-level dependencies.** One was found by
   accident in a sample of ten; there are likely more.
3. **The model never writes its own status.** Code does timing and candidate generation,
   the model drafts the argument, a human accepts or rules out.
4. **Keep the control permanent.** Every future batch ships with within-tradition
   controls from the same pool and reports the rate. When that rate climbs, the class is
   decaying into narrative.

## Running it

```bash
python3 wiki/c2a2-prs-3d/scripts/prs_reconstruct.py worksheet --out /tmp/worksheet.md
python3 wiki/c2a2-prs-3d/scripts/prs_reconstruct.py score --reconstructions \
    wiki/c2a2-prs-3d/testcorpus/reconstructions.json
```

The worksheet withholds conditions; `reconstruction_key.json` holds them and must not be
opened until every item is authored.
