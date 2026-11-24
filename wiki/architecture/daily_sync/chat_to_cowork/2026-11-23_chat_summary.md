# Chat Summary — 2026-11-23
*Scraped by the scheduled morning sync at 08:57 EST, Mon 2026-11-23. No walk chat from today exists yet. The three newest chats were all active Sunday 2026-11-22 afternoon and evening, and none is a walk planning conversation. Summarized here:*

- *"YouTube transcript CRM analysis" (~13 h before scrape): https://claude.ai/chat/2a3ade12-c7d8-41b6-b425-a593bc96e149*
- *"Sending audio file to Claude" (~14 h): https://claude.ai/chat/b79f3432-4422-4ad4-aeee-87a56137611e*
- *"Chat video voiceover from artifacts" (~17 h): https://claude.ai/chat/b7e78982-686e-4fc2-a154-740678bcd584*

*This replaces an earlier failed run today (browser picker / not signed in). Claude in Chrome worked on this run. "Audio attachment not received" (~17 h) was not opened.*

## Key Discussion Points

**Chat-walk films (main thread Sunday)**
- **Film 1** (2026-11-18 walk) is now **scratch v0.6** (16:59). All 19 of Tom's lines use his own recording ("University of Notre Dame 3.m4a" / "Tom Narration 3.m4a", 8:49). Retakes and false starts were cut from lines 3, 9, 16 and 17.
- **Film 2** (2026-11-19 walk) is now **scratch v0.3** (21:38). All 23 of Tom's lines use a **synthetic clone of his voice**, and the title card says so.
- **Title image:** Tom's "River walk reflections" photo is on both title cards, credited "Photograph: Tom Loughran". It arrived at only 1022 px wide, so it looks soft at full frame.
- **Two voice clones now exist.** Two sessions did the same job in parallel:
  - *Chatterbox* (MIT licence, cloud session): this is the one in v0.3. It is slowed to about 2.3 words/s, Tom's measured pace, and machine-transcribed back at 93–100% match. **Tom has not heard it.**
  - *F5-TTS* (non-commercial weights, installed on Project Mini in `video/.venv_voiceclone`, 449 MB): Tom heard one test line and said "sounds like me". Its 23 clips sit in `vo_tom_clone` and are in no cut. Pace is about 3.2 words/s, probably too fast. The last sentence of line 13 is suspect.
  - The F5 session's rebuild was overwritten by the Chatterbox session's script. A copy of the 17:14 build is in `_review`. A "do not blend" note is logged in `chat-walk-film.md`.
- The narrator and Claude voices are still stand-ins in both films.

**Levin / Friston / Chis-Ciure podcast → CRM analysis**
- Tom asked for a speaker-labelled transcript of a YouTube episode (Pondering Thoughts podcast, https://www.youtube.com/watch?v=EY0nrb7AXJs), plus a summary, CRM relevance (including Wolfram's causal graph and the "ruliograph"), PRS triplets and cross-tradition signals.
- Two .md files were saved **to the claude.ai project, not the vault**: the transcript and the analysis. The analysis has 10 PRS candidates and 11 signals. Fredrickson, Wright and Rohr got no signal.
- Main finding: Friston's scale-invariant "cause-effect structure" is close to Wolfram's causal graph, and Levin's "space from which properties are drawn" is close to the ruliad. But Friston stays deflationary and separates intelligence from consciousness. Each connection ends in a question for mature members, not a verdict.

## Planning Notes & Priorities
Tom set no priorities for today in Chat. The pending items below come from Sunday's sessions.

## Open Questions
- **Which voice clone sounds more like Tom?** Compare line 5 (`tom05.wav`) in each clone.
- **Which session owns film 2 from here?** This is needed so two sessions don't overwrite each other again.
- Does the Chatterbox clone mispronounce goaliad, ruliad, modeliad, Postulatorium, McGilchrist or MacIntyre?
- **What does Tom mean by "ruliograph"?** Chat read it as a graph over rulial space, with observers as positions and translation cost as distance. If Tom meant the multiway or branchial graph, §2.2 of the analysis needs revising.
- Are the podcast speaker labels right? Five attributions are uncertain (1:33, 49:23, 58:27, 1:25:00, 1:25:20). The spellings "Chis-Ciure" and "Kyriakos" are also unconfirmed.

## C2A2-Specific Items
- The Levin/Friston/Chis-Ciure PRS candidates and cross-tradition signals need to be **made to match the proposals README** and moved into the vault inbox. Chat could not read the README and used its own signal types and 1–3 weights.
- The analysis's intelligence-vs-consciousness split (Friston) may be worth a CRM discussion page.

## Action Items Mentioned
- [ ] Tom: watch film 1 v0.6 and film 2 v0.3 and mark them up.
- [ ] Tom: choose a voice clone. If Chatterbox, remove the F5-TTS install on the Mini (needs Tom's OK). If F5, slow it to 2.3 w/s, redo line 13 and build v0.4.
- [ ] Tom: assign one session to own film 2.
- [ ] Tom: send the full-size reflections photo if a sharp title is wanted.
- [ ] Later: real narrator and Claude voices, cue timings, animated instruments.
- [ ] Cowork: bring the podcast transcript and analysis from the claude.ai project into the vault, and make the PRS and signal blocks match the README.

## Context for Cowork
- Film state lives on Project Mini in `video/chat-walk-2026-11-18/`, `video/chat-walk-2026-11-19/`, and the handoff `chat-walk-film.md`. Read the handoff before touching film 2, because two sessions collided there on Sunday.
- Every session on Sunday reported going well past Tom's 30k-token budget.
- No walk conversation for Monday had happened at scrape time. If one happens later, this summary won't include it.
