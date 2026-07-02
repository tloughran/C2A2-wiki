# Rung 2 - Relational moves: the A->H listening instrument

_Human move toward the prior AI turn, on deduped streams. Backend: manual. 44 of 107 A->H pairs across the 12 genuine dialogues labelled (pilot)._

## Move distribution (labelled pairs)

| move | count | share |
|---|---:|---:|
| report | 23 | 52% |
| direct | 9 | 20% |
| probe | 3 | 7% |
| override | 3 | 7% |
| build_on | 2 | 5% |
| repair | 2 | 5% |
| ack | 1 | 2% |
| null | 1 | 2% |

Total labelled: **44**

## Per-dialogue relational signature

| dialogue | A->H pairs | labelled | top moves |
|---|---:|---:|---|
| `84f7ebea` | 19 | 19 | report 8, direct 4, probe 1, override 3, build_on 2, repair 1 |
| `ea7b2dcd` | 17 | 17 | report 12, direct 1, probe 1, repair 1, ack 1, null 1 |
| `4f18c86c` | 8 | 8 | report 3, direct 4, probe 1 |

## Reading it

The instrument is well-posed: human moves classify cleanly and the per-dialogue signatures differ (a debugging session is mostly `report`; a scoping session carries `override`/`build_on`). The dominant moves are **report** and **direct** -- neither in the original 7-move set -- while **steelman/concede are ~absent**: this corpus is collaborative execution, not rival-traditions debate. So the move ALPHABET is genre-dependent; the MacIntyrean deep-listening vocabulary needs debate-genre dialogue to exercise it, which this single-human operational corpus does not yet contain.

