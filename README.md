# Second Brain

An automated "second brain" for work, built on the system described in the reference screenshots
(Power Automate → raw dumps → dedup prefilter → Claude synthesis → PARA/Obsidian), adapted for a
Google Workspace + Slack ecosystem where Claude itself does the harvesting.

Open this repo folder as an Obsidian vault (or sync it into your existing vault — see
[Syncing with Obsidian](#syncing-with-obsidian)).

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  NIGHTLY (scheduled Claude session / Routine)                │
│                                                              │
│  1. HARVEST   Pull since-last-run items via connectors:      │
│               Gmail, Google Calendar, Slack, Fathom/Granola  │
│               (meeting transcripts), Drive. Dump each source │
│               to raw/<source>.md                             │
│                                                              │
│  2. PREFILTER scripts/prefilter.py hashes every content      │
│               block, diffs against state/seen.json, and      │
│               emits ONLY new/changed blocks to               │
│               state/new-since-last-run.md                    │
│                                                              │
│  3. SYNTHESIZE Claude reads the new blocks + context.md +    │
│               relationships.md and files atomic notes into   │
│               the PARA tree (rules live in CLAUDE.md)        │
│                                                              │
│  4. FLAG      Low-confidence extractions go to               │
│               00-inbox/needs-clarification.md for your       │
│               morning review                                 │
│                                                              │
│  5. COMMIT    git commit + push → Obsidian Git plugin pulls  │
│               it into your vault on your devices             │
└─────────────────────────────────────────────────────────────┘
```

This mirrors the original system 1:1, with two substitutions:

| Original (screenshots)                  | This repo                                        |
| --------------------------------------- | ------------------------------------------------ |
| Power Automate scrapes M365 nightly     | Claude Routine pulls Gmail/Calendar/Slack/Fathom |
| OneNote as meeting-notes landing zone   | Fathom/Granola transcripts pulled directly       |
| Local folder Claude is "pointed at"     | This git repo, synced to Obsidian via git        |
| Python hash prefilter                   | Same (`scripts/prefilter.py`)                    |
| PARA + Zettelkasten atomic notes        | Same (`10-projects/` … `40-archive/`)            |
| 8am "needs clarification" ping          | `00-inbox/needs-clarification.md` + optional push notification |

## Folder layout

```
context.md            Who you are, your firm, coworkers, active projects (you maintain this)
relationships.md      Extracted people/org relationship map (Claude maintains, you correct)
CLAUDE.md             The "master prompt" — synthesis rules the nightly agent follows
raw/                  Nightly source dumps land here (one file per source, overwritten each run)
state/                seen.json hash ledger + new-since-last-run.md (machine-managed)
scripts/prefilter.py  The dedup prefilter
00-inbox/             needs-clarification.md + anything not yet filed
10-projects/          One folder per active project, each with atomic notes:
                        README.md, decisions.md, meetings.md, contacts.md,
                        action-items.md, timeline.md, data.md
20-areas/             Ongoing responsibilities (no end date): e.g. team, budget, clients
30-resources/         Reference material not tied to a project
40-archive/           Completed/inactive projects moved here wholesale
_templates/           Note templates the agent uses when scaffolding a new project
```

## How a query works later

Because everything is distilled into small, linked markdown files, questions like
*"why did the design for the canopy change — was it a meeting I wasn't in?"* or
*"did we ever evaluate option X?"* are answered by opening
`10-projects/<project>/decisions.md` (each decision logs the options considered and a
`[[meetings#...]]` link back to where it happened) — either by you in Obsidian, or by
asking Claude, which greps the vault instead of re-reading months of email.

## Setup

1. **Fill in `context.md`** — the more the agent knows about your firm, projects, and
   coworkers, the better it files things. This is the grounding document.
2. **Connect sources** — in your Claude session, ensure Gmail, Google Calendar, Slack,
   and Fathom/Granola connectors are authorized (they already are in this environment).
3. **Schedule the nightly run** — ask Claude to create a Routine (e.g. 2am daily) with a
   prompt like: *"Run the second-brain nightly sync per CLAUDE.md in johncalafiore/general:
   harvest, prefilter, synthesize, commit, push."* Fresh-session-per-fire is recommended.
4. **Sync to Obsidian** — see below.
5. **Morning habit** — check `00-inbox/needs-clarification.md`; answer or delete items.
   Your answers get folded in on the next run.

## Syncing with Obsidian

Option A (recommended): install the community **Obsidian Git** plugin, clone this repo as
(or into) your vault, and set auto-pull on an interval. The nightly push lands in your
vault before you wake up.

Option B: clone the repo anywhere and symlink the PARA folders into your existing vault.

Obsidian-friendly conventions the agent follows: YAML frontmatter on every note,
`[[wikilinks]]` between notes, `#tags` for status, one H2 per atomic entry so links can
target `[[file#heading]]`.
