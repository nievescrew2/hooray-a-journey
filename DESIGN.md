Title: Absurd Ascension — Design Document

Concept & Tone
- Absurdist parody merging cultivation progression and cringy manhwa MC tropes.
- Lightly surreal humor, intentionally over-the-top praises, melodrama, and meta commentary.

Core Loop
- Each turn the player chooses an action: cultivate (gain Qi), train (gain Strength-ish progress), social-post (gain Followers / Cringe), or rest (recover).
- Resources: Qi (primary), Cringe (narrative currency), Followers (social power).
- Progression: XP-like "Aura" fills; when thresholds hit, player "Ascends" to next cultivation stage.
- Random events trigger parody scenes (rival drama, harem misinterpretation, ancient artifact advertisement).

Mechanics
- Actions:
  - Meditate: +Qi (chance of minor random event)
  - Drill: +Progress, costs Qi
  - Post: +Followers, +Cringe
  - Gamble Fate: high-risk high-reward (parody of plot armor)
- Cultivation Levels (example): Mortal Scribbler -> Seedling Influencer -> Overdramatic Ascendant -> Chapter-Cliffhanger God
- Events modify resources and sometimes change story flags (e.g., "You were publicly roasted").

Narrative & Characters
- Parody targets: cringy manhwa MC arrogance, cultivation game spammy progression, NPCs who offer terrible life advice.
- Example NPCs: "Mysterious Senior" (obligatory), "Harem Recruit" (overexcited follower), "Rival Author" (constantly edits your status)

UX Goals
- Short sessions (10–30 minutes) should feel like a ridiculous climb.
- Clear, cheeky text descriptions and absurd event outcomes.
- Save/load for mid-session breaks.

Minimum Viable Prototype (MVP)
- CLI app in Python
- Show status, present 4 actions, random event table, simple level progression, save/load JSON
- 200–400 lines max, no external deps

Future Enhancements
- Branching storylines, more parody targets, character art (ASCII), web port.
