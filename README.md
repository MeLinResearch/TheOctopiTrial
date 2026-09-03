# The Octopi Trial 🐙

**Does a two-minute curiosity break make Claude better at a puzzle?**

Help find out. It takes about 10 minutes, any Claude works (free claude.ai,
Pro, Claude Code, API — doesn't matter), and your handle goes in the public
write-up.

## How to join

1. **Get your prompts** at
   **[melinresearch.github.io/TheOctopiTrial](https://melinresearch.github.io/TheOctopiTrial/)**
   — type your GitHub username and it hands you 2 or 3 messages in order.
2. **Open a brand-new Claude chat.** Not this one, not one that's seen this
   repo. Fresh.
3. **Paste the messages one at a time**, in order, and wait for each full
   reply before sending the next. Don't edit, retry, or regenerate.
4. **Copy the replies back** into the
   **[submit form](https://github.com/MeLinResearch/TheOctopiTrial/issues/new?template=trial-result.yml)**.
   Two minutes.

That's it. If you'd rather use a terminal, `python3 participate.py assign
--participant YOUR_GITHUB_USERNAME` does the same thing.

**Rules, short version:** one run per person per Claude setup. Use your real
GitHub username so your assignment can be checked. First answers only. Don't
tell the test chat what the study is about.

## What's going on

Your username randomly drops you into one of four groups. Three groups get a
quick "go find six new facts about X" warm-up first; one group doesn't. Then
everyone gets the exact same puzzle. Groups are compared afterwards.

| Group | Warm-up |
|---|---|
| A | none |
| B | six new facts about granite and basalt |
| C | six new facts about octopuses and squid |
| D | six new facts about a topic Claude picks itself |

The puzzle's answer key is locked behind a hash until collection closes, and
the hypotheses were written down before anyone ran it, so nobody can move the
goalposts — including us.

## Why it matters

Whether "mood" or engagement changes how a deployed AI performs is an open
question. Most studies are lab-controlled; this one measures real Claude
sessions people actually use, warts and all. Even a null result is useful.

## Why "Octopi"?

The usual plural is *octopuses*. It's a project name, not a taxonomy claim.
Nitpicking is welcome and scores zero points.

## Fine print

- [PROTOCOL.md](PROTOCOL.md) — full rules and eligibility
- [study/preregistration.md](study/preregistration.md) — frozen hypotheses and analysis plan
- [commitments/](commitments/) — SHA-256 hashes of the answer key, scorer, and prompts
- [results/](results/) — empty until recruitment closes
- MIT license. Submissions are public and go into an openly licensed dataset.

Don't paste real names, emails, API keys, or private system prompts.
