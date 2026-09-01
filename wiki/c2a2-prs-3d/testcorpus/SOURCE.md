# Source note — where this fixture's twenty results came from

*Written 2026-09-01; substantially corrected the same day once the image itself was
supplied. Corrects (a) an attribution error that stood in the assessment doc, the regen
wrapper and both triplet files from the moment the fixture was built, and (b) this file's
own first conclusion, which wrongly held that the twenty results and dates were
Claude-authored.*

## The source

**Welch Labs**, YouTube, <https://www.youtube.com/watch?v=QgH9sr7G13Q>.
A ~35-minute explainer whose subject is **residual networks (ResNets)** — the
December 2015 "Deep Residual Learning for Image Recognition" paper, the degradation
problem that motivated it, and the reconceptualization of depth that followed.

The fixture was originally credited to "Karpathy's domino image." **That is wrong.**
Andrej Karpathy has nothing to do with it. (The project folder is named
"RC Karpathy Wiki Project" for unrelated reasons; the error may have travelled that way.)

## What the video actually asserts

**Corrected 2026-09-01 (second pass), after Tom supplied the image itself.** The first
version of this file was written from the captions alone and concluded that the twenty
results and their dates were Claude-authored. **That was wrong**, and it was wrong in the
predictable direction: captions do not capture on-screen graphics, this file said so, and
the conclusion was drawn anyway as though the absence of narrated dates settled the matter.

### The narration (captions, retrieved 2026-09-01: 907 cues, 2117 s, read in full)

The quantum-mechanics material is a closing analogy of roughly one minute, at about
**32:20–33:30**, plus an aside at **~21:45**. The chain, in order: Planck resolves the
ultraviolet catastrophe by treating energy as emitted in discrete quanta, and regards it as
a mathematical device rather than a discovery; Einstein applies the idea to the
photoelectric effect; Bohr carries it into quantized electron energy states; "the dominoes
continued to fall," culminating in the late 1920s with Schrödinger, Heisenberg and Dirac;
Gamow's phrase *Thirty Years That Shook Physics* is quoted; the analogy is turned on deep
learning, with ResNets as an early domino.

**The narration speaks no dates and no list.** Note also that the captions are ASR and are
unreliable on exactly the tokens that matter here — proper nouns arrive mangled (Planck,
Niels, Schrödinger, Dirac, Gamow, Jian Sun, ImageNet, ReLU and He-initialization are all
corrupted). The names above are read through context, not transcribed.

### The image — this is the actual source

A photograph of twenty dominoes in two rows, green over black:

| # | green row (quantum) | year | black row (deep learning) | year |
|---|---|---|---|---|
| 1 | Planck | 1900 | AlexNet | 2012 |
| 2 | Einstein | 1905 | ResNet | 2015 |
| 3 | Bohr | 1913 | AlphaGo | 2016 |
| 4 | Compton | 1922 | Transformer | 2017 |
| 5 | de Broglie | 1924 | Neural Scaling | 2020 |
| 6 | Pauli | 1925 | DDPM | 2020 |
| 7 | Heisenberg | 1925 | GPT-3 | 2020 |
| 8 | Schrödinger | 1926 | AlphaFold | 2021 |
| 9 | Dirac | 1930 | RLHF | 2022 |
| 10 | von Neumann | 1932 | DeepSeek R1 | 2025 |

**All twenty names and all twenty years match the fixture exactly.** The fixture is sourced,
not invented, at that level.

### So what is, and is not, Claude-authored

**From the image:** the twenty results, their years, the two-tradition split, the
left-to-right order, the equal length of ten and ten, and the compression itself — 1900–1932
against 2012–2025, thirty-two years against thirteen.

**Claude-authored:** the PRS triplet prose (Problem / Resource / Solution) for all twenty;
the **month and day** on every date, since the image carries years only; and all six
cross-connections in `vault/master/cross_program_index.md`.

That day-level precision is not a harmless elaboration. The image asserts *years*. The
fixture renders *timestamps*, and `PAIRINGS.md` shows the invented precision is drawn from
seven different kinds of event in the quantum row alone. The compression claim is about
**eras**; the axis draws it as though it were about days. Quote any rate ratio to the year.

### Two things the image settles, and one it does not

1. **It does assert an ordering**, and on one pair the ordering is wrong. The image places
   **DDPM before GPT-3**; both are 2020, but the record is GPT-3 arXiv v1 on 28 May 2020 and
   DDPM on 19 June 2020. The fixture follows the record, so the fixture is right and the
   image is wrong here. An earlier note in this project recorded this suspicion as "cleared
   because the source asserts no ordering" — the verdict on the fixture was right, the reason
   was not.
2. **It explains the Dirac defect.** The image says 1930, which is *The Principles of Quantum
   Mechanics*; the fixture's triplet prose describes the January 1928 relativistic equation
   (spin, magnetic moment, antimatter). The row inherited the image's year and was then
   written about a different result.
3. **It does not settle correspondence.** The rows are laid out in aligned columns of ten,
   which is at least suggestive. But a domino chain is a picture of a *cascade*, and two rows
   of ten falling independently is an equally natural reading. The narration supports a shared
   **shape** — early device taken as a trick, cascade, late reconceptualization — and asserts
   no pairing of specific results. Treat column alignment as undetermined, not as a mapping.

**Consequence for the fixture's next use, unchanged:** the six cross-connections remain
Claude-authored with nothing external to check them against, so the fixture is still not a
labelled evaluation set for an analogy detector. That is what Step 1 Phases B and C exist for.

## Retrieval

Raw captions are **deliberately not committed** — this repository is public, and a
verbatim transcript of someone else's video is their content, not ours. The image is not
committed either, for the same reason; the table above records the twenty names and years
it carries, which is data rather than expression. The summary, the table and the URL are
the record. To re-retrieve the captions:

```bash
python3 -c "from youtube_transcript_api import YouTubeTranscriptApi as A; print(len(A().fetch('QgH9sr7G13Q', languages=['en'])))"
```
