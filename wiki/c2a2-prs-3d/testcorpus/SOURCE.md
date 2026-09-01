# Source note — where this fixture's twenty results came from

*Written 2026-09-01. Corrects an attribution error that stood in the assessment doc,
the regen wrapper and both triplet files from the moment the fixture was built.*

## The source

**Welch Labs**, YouTube, <https://www.youtube.com/watch?v=QgH9sr7G13Q>.
A ~35-minute explainer whose subject is **residual networks (ResNets)** — the
December 2015 "Deep Residual Learning for Image Recognition" paper, the degradation
problem that motivated it, and the reconceptualization of depth that followed.

The fixture was originally credited to "Karpathy's domino image." **That is wrong.**
Andrej Karpathy has nothing to do with it. (The project folder is named
"RC Karpathy Wiki Project" for unrelated reasons; the error may have travelled that way.)

## What the video actually asserts

Auto-generated English captions were retrieved 2026-09-01 (907 cues, 2117 s) and read
in full. The quantum-mechanics material is **not** a chart of twenty results. It is a
closing analogy of roughly one minute, at about **32:20–33:30**, plus one aside at
**~21:45** where the interviewee mentions studying quantum mechanics and being struck
by representation theory.

The narrated chain, in order, is:

1. Planck resolves the ultraviolet catastrophe by treating energy as emitted and
   absorbed in discrete quanta — and regards this as a mathematical device rather
   than a discovery about nature;
2. Einstein applies the idea to the photoelectric effect;
3. Bohr carries it into quantized electron energy states in the atom;
4. "the dominoes continued to fall," culminating in the late 1920s with Schrödinger,
   Heisenberg and Dirac, and a complete reconceptualization of matter and energy;
5. Gamow's phrase for the buildup — *Thirty Years That Shook Physics* — is quoted;
6. the analogy is then turned on deep learning: ResNets were one of the early
   dominoes, and it is left open whether most of this wave's dominoes have already
   fallen.

**No dates are spoken. No ten-and-ten list is spoken. No pairwise correspondence
between a quantum result and a deep-learning result is spoken.**

## What this means for the fixture — read this before trusting any number in it

Captions do not capture on-screen graphics. A visual domino chart may well appear
during that closing minute; it cannot be confirmed or denied from the transcript, and
whoever next works on this should simply watch 32:00–34:00 and say what is on screen.

Either way, two things are now established:

- **The twenty results, and every date attached to them, are Claude-authored.** They
  were written from model knowledge and were already flagged uncitable. Nothing in the
  narration sources them.
- **The six cross-connections are Claude-authored too.** The assessment doc claimed
  they stated "the correspondences the image asserts." The narration asserts a shared
  *shape* — an early device taken as a trick, a cascade, a late reconceptualization —
  and no pairing of specific results at all.

This does not weaken the fixture's use to date. It was built to be structurally known
in advance and to break an instrument, and it did: the τ=90 axis pressed 32 years into
1.66 of 40 column units, six coils rendered NaN, and `max_share` read 5.0 % on the
inverted picture. **A synthetic corpus is a valid probe of a renderer.**

It does block the fixture's *next* intended use. It cannot serve as a labelled
evaluation set for an analogy detector while its labels are the same model's guesses.
That is what Step 1 Phase A exists to fix.

## Retrieval

Raw captions are **deliberately not committed** — this repository is public, and a
verbatim transcript of someone else's video is their content, not ours. The summary
above and the URL are the record. To re-retrieve:

```bash
python3 -c "from youtube_transcript_api import YouTubeTranscriptApi as A; print(len(A().fetch('QgH9sr7G13Q', languages=['en'])))"
```
