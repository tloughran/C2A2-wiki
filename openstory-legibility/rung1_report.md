# Rung 1 - Uptake: is listening legible without a model?

_Generated 2026-06-30 17:33 from `open-story-snapshot.db` (read-only). Deterministic: TF-IDF, 200 shuffles, seed 1729. No model._

## Population

- turn-bearing sessions: **223**
- with a usable dialogue stream (>= 4 utterances): **16**
- skipped (too short for a control, < 4 utterances): **207**
- **substantive two-sided dialogues** (each role >=3 utts, >=10 utts total): **14** -- these are the only sessions where uptake is well-posed; the rest are single-prompt runs whose role-matched null is degenerate (lift==0 by construction).
- of measured, AI<->AI (`agent-*`): **0** (agent sessions are single-shot in this corpus; AI<->AI uptake is not yet measurable)

## The verdict (real predecessor vs. role-matched random partner)

`lift = mean(real adjacent cosine) - mean(role-matched random-partner cosine)`. Positive lift means an utterance resembles its ACTUAL predecessor more than a random same-role utterance from the same conversation -- specific uptake, not just shared topic. **Reported on the 14 substantive dialogues.**

- median real adjacent cosine: **0.098**
- median role-matched null cosine: **0.046**
- median **lift**: **+0.053**
- dialogues with positive lift: **14/14** (100%)
- dialogues where real beats role-matched null at p<0.05: **13/14** (93%)
- _(for contrast, across all 16 measured incl. degenerate runs: median lift +0.037, positive 16/16 -- the degenerate runs wash the median to ~0)_

## Direction (each is real - role-matched null, on substantive dialogues)

- mean **A->H** uptake lift (next human takes up the AI - the listening signal): **+0.034**, positive in **11/14**
- mean **H->A** uptake lift (AI takes up the human - sanity floor): **+0.063**, positive in **13/14**
- explicit back-reference rate on A->H pairs (marker or rare-term overlap): **62%**

## Per-session (substantive dialogues, top 20 by utterance count)

| session | utt | real | null | lift | p | A->H lift | H->A lift | ref% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `07ab764b-395e-` | 782 | 0.003 | 0.001 | +0.001 | 0.005 | +0.000 | +0.003 | 26% |
| `84f7ebea-2a49-` | 39 | 0.111 | 0.040 | +0.071 | 0.005 | +0.064 | +0.077 | 79% |
| `ea7b2dcd-1d77-` | 36 | 0.158 | 0.065 | +0.093 | 0.005 | +0.126 | +0.063 | 76% |
| `c9d9e7c9-dd6e-` | 28 | 0.143 | 0.061 | +0.082 | 0.005 | +0.073 | +0.087 | 92% |
| `02381065-11a5-` | 18 | 0.090 | 0.037 | +0.053 | 0.005 | +0.024 | +0.086 | 44% |
| `1b35066d-8389-` | 18 | 0.098 | 0.044 | +0.054 | 0.005 | +0.031 | +0.074 | 75% |
| `4f18c86c-9e34-` | 18 | 0.082 | 0.051 | +0.031 | 0.015 | +0.045 | +0.018 | 50% |
| `3788ad2c-8e63-` | 17 | 0.113 | 0.047 | +0.065 | 0.005 | -0.006 | +0.130 | 86% |
| `5568d1d6-8e4f-` | 14 | 0.179 | 0.083 | +0.096 | 0.005 | +0.096 | +0.098 | 67% |
| `119776ad-c95c-` | 13 | 0.073 | 0.043 | +0.031 | 0.005 | -0.012 | +0.071 | 67% |
| `35e9daf3-2489-` | 12 | 0.055 | 0.024 | +0.030 | 0.005 | +0.017 | +0.044 | 80% |
| `743bdd01-520c-` | 12 | 0.078 | 0.040 | +0.037 | 0.010 | +0.012 | +0.064 | 40% |
| `42ba591f-ff69-` | 11 | 0.103 | 0.068 | +0.035 | 0.020 | -0.016 | +0.081 | 60% |
| `848b16f9-3f90-` | 10 | 0.047 | 0.046 | +0.001 | 0.493 | +0.018 | -0.016 | 25% |

## Honest limit

TF-IDF is lexical, so short human backchannels that genuinely listen but reuse few words score ~0. This makes every number above a **conservative lower bound** on uptake. It also bears asymmetrically on direction: **H->A** (the AI reusing the human's own vocabulary to answer) is lexically easy to see, while **A->H** (a brief human reply taking up a long AI answer) is exactly where lexical goes blind. So A->H being the noisier, sometimes-negative direction is expected -- and it is precisely the signal Rung 2's semantic judgment would buy. Signal present even through this lens is strong evidence; weak A->H is not evidence of absence.

