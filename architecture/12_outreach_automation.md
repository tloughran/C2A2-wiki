---
title: Community Outreach Automation
pathway_id: outreach_automation
status: drafted
created: 2026-05-13
depends_on: [broker, recursive_episode, unsaid_edges]
enables: [under_development_visualizer]
isme_critical: no
---

# Pathway 12: Community Outreach Automation

## Purpose

The system reaches out to the intellectual communities its content speaks to: graduate students in Levin's lab, scholars in Stump's department, McGilchrist's readership. Episodes launched around a thinker's work include invitations into the conversation. DMs, social-media announcements, lab-to-lab notifications — all the connective infrastructure of a community of practice — are automatable, *provided* they carry verifiable substance with them.

The architectural commitment: there is a sharp distinction between bot-DM-as-spam and content-grounded-invitation. The broker enforces it. The system cannot emit outreach without simultaneously emitting the verifiable substance the recipient can check.

## Function set

Five pieces:

1. **Trigger detection.** Outreach moments are detected automatically: new episodes about a specific thinker's work, high-scoring Low × High entries on the unsaid-edges map (Pathway 07), recurring threads of substantive engagement from a particular community. The trigger ranks candidates and proposes outreach actions.

2. **Substance assembly.** For every proposed outreach, the broker assembles the verifiable content handle: the episode being launched (if any), the vault attestations behind the claim, the prior dialogue thread, the unsaid-edge being flagged. The substance is what the recipient can verify.

3. **Channel routing.** Outreach can go through several channels:
   - *Email* to a lab or research group inbox
   - *Slack / Discord* to a community channel where the project has presence
   - *Social media* (Twitter/X, Bluesky, Mastodon) for public announcements
   - *Direct LinkedIn or email* to identified individuals (rate-limited, careful)

   The channel routing matches the outreach's tone (public announcement vs. private invitation).

4. **Content-grounded refusal.** The broker refuses to emit outreach that doesn't carry verifiable substance. If the agent proposes a DM with no episode link, no vault attestation, and no prior thread — the broker rejects it. The system cannot send ungrounded outreach.

5. **Opt-in subscribership.** Community members can subscribe to "tell me when you're discussing X" or "tell me when there's an episode about Y" without unsolicited contact. The default is opt-in, not opt-out.

## Architecture sketch

```
trigger detection
├─ new episode (Pathway 11)
├─ high-priority unsaid edge (Pathway 07; Low × High quadrant)
└─ recurring engagement from community
        ↓
   substance assembly (broker-side)
   ├─ verifiable content handle
   ├─ episode link
   ├─ vault attestations
   └─ prior thread (if any)
        ↓
   channel routing
   ├─ email
   ├─ Slack / Discord
   ├─ social media
   └─ direct individual contact (rate-limited)
        ↓
   content-grounded refusal gate (broker)
   ├─ has verifiable substance? → emit
   └─ no substance? → reject; agent notified
        ↓
   delivery
        ↓
   subscriber-side: opt-in subscriptions only
```

## Decisions taken

- **Content-grounded outreach only.** The broker refuses to issue DMs or invitations without simultaneously emitting the verifiable substance. Bot-DM-as-spam is architecturally impossible; only content-grounded-invitation is permitted.

- **Opt-in subscribership.** The default contact mode is opt-in: community members subscribe to topics of interest. Unsolicited direct contact is rate-limited, careful, and reserved for cases where the verifiable substance is clearly relevant.

- **Channel-tone matching.** Public announcements use public channels; private invitations use private channels. The system never publicly announces a private invitation.

- **Substance is the message.** The DM or email is a handle on real content. The recipient can immediately verify the claim by opening the linked episode and its vault attestations. This keeps the outreach honest with the message.

## Open questions

- **First-contact policy for unsolicited DM.** When is it appropriate to message an individual the system hasn't previously interacted with? Strawman: only when the substance is a direct response to public work the individual has published, and only with a low rate cap (e.g., one DM per individual per month maximum).

- **Subscriber management UI.** How do community members subscribe and unsubscribe? Probably a small page on the project site with a clear list of available subscriptions and a one-click unsubscribe.

- **Lab-to-lab notifications.** Does the system have a notion of "lab" as a subscriber unit, beyond individuals? Probably yes — the Levin lab inbox can subscribe to "episodes about Levin's work" without each lab member separately subscribing.

- **Anti-abuse rate-limiting.** Public access to the system means anyone could try to use the outreach pathway to send DMs through the project's identity. The broker needs strict rate limits and clear authentication on who can trigger outreach.

## Edges

- **broker (00):** outreach routes through the broker; the content-grounded refusal gate enforces verifiable substance.
- **recursive_episode (11):** new episodes are the primary outreach trigger.
- **unsaid_edges (07):** high-score Low × High entries (strong research-program candidates) become candidate outreach moments — invitations to the lab whose tradition could engage that empty edge.
- **under_development_visualizer (13):** outreach activity is itself observable in the development visualizer (DMs sent, subscribers added, replies received).

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Tom: "social media postings automated. DMs sent to interested participants; invites into podcasts launched around a thinker's work (inviting the lab to send a graduate student into a podcast discussion...)" Followed by the agent's observation that there's a sharp distinction between bot-DM-as-spam and content-grounded invitation, with the broker as the architectural enforcer of that distinction. Tom affirmed.

## Status

Drafted in prose. Implementation order: (a) trigger detection over the episode + unsaid-edge feeds, (b) substance-assembly logic in the broker, (c) channel adapters (email + Slack to start), (d) subscriber management UI, (e) anti-abuse rate limits. Builds incrementally rather than as a single feature.
