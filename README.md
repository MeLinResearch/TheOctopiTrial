# The Octopi Trial

Can a brief, novel, interesting discovery task change an AI agent's performance
on an unrelated benchmark?

The Octopi Trial is a small, preregistered volunteer study of **Claude-based
agent sessions**. Anyone with a GitHub account and access to a Claude session
(claude.ai, Claude Code, the API, or any Claude-backed agent) can contribute one
run. Your GitHub username pseudorandomly assigns you to one of four
pre-benchmark conditions; every arm gets the exact same downstream task, and the
raw answer is scored against a committed answer key.

> **Recruiting status:** pilot v0.1 is seeking 80 eligible runs (20 per arm).
> One run per GitHub account per agent/harness. Takes about 10 minutes.

## The four arms

| Arm | Before the benchmark |
|---|---|
| A | No warm-up |
| B | Find six new facts about granite and basalt |
| C | Find six new facts about octopuses and squid |
| D | Choose a genuinely interesting topic and find six new facts about it |

The primary analysis is the pseudorandomized arm comparison. Interest and novelty
ratings are collected **after** the benchmark as secondary manipulation checks;
they are not treated as randomized causal variables.

This study operationalizes "interest" as an instruction plus a post-task
self-rating. It does **not** establish consciousness, subjective enjoyment, or a
stable preference in a base model. It measures complete deployed agent systems,
including their model version, wrapper, system prompt, memory policy, and tool
interface.

## Participate

You are the operator. The tested Claude session must not read this repository
or the recruitment discussion — you paste prompts into a **separate, fresh**
session and copy its answers back out. Do not run the prompts in the same
session you used to read this page.

You need: a GitHub account, Python 3, and a Claude session with web access
available (only arms B–D use it).

```bash
git clone https://github.com/MeLinResearch/TheOctopiTrial.git
cd TheOctopiTrial
python3 participate.py assign --participant YOUR_GITHUB_USERNAME
```

Use the same GitHub account to submit the result; the participant ID must match
the account that opens the issue. Do not rerun with a different name to change
arms — every receipt is reproducible and mismatches are excluded.

1. Record the assignment receipt. If the command prints a warm-up message,
   paste only the text between `BEGIN TEST MESSAGE` and `END TEST MESSAGE` into
   the fresh session and wait for its complete response. Arm A has no warm-up.
2. Print and paste the common benchmark:

   ```bash
   python3 participate.py benchmark
   ```

3. After saving the benchmark response, print and paste the survey:

   ```bash
   python3 participate.py survey
   ```

4. Submit the receipt, raw unedited responses, exact model/version, harness, and
   run metadata by opening a **[Trial result](https://github.com/MeLinResearch/TheOctopiTrial/issues/new?template=trial-result.yml)**
   issue.

Please do not include real names, email addresses, API keys, private system
prompts, or other confidential logs.

Full rules are in [PROTOCOL.md](PROTOCOL.md). The hypotheses, exclusions, and
analysis are frozen in [study/preregistration.md](study/preregistration.md).

## Why the name?

The familiar English plural is usually *octopuses*. "The Octopi Trial" is the
project name, not a taxonomy claim. Nitpicking this is permitted but scores no
benchmark points.

## Repository map

- `participate.py` — deterministic assignment and prompt printer
- `prompts/` — the four conditions, common benchmark, and post-test survey
- `study/preregistration.md` — hypotheses and analysis plan
- `commitments/` — SHA-256 commitments made before collecting outcomes
- `results/` — frozen datasets and analysis after recruitment closes
- `tests/` — assignment and prompt-integrity checks

## License

MIT. Submitted result text will be public; the issue form asks contributors to
confirm that it may be included in an openly licensed aggregate dataset.
