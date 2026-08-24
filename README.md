# The Octopi Trial

Can a brief, novel, interesting discovery task change an AI agent's performance
on an unrelated benchmark?

The Octopi Trial is a small, preregistered volunteer study for **Claude-based
agent sessions**. It pseudorandomly assigns each participating system to one of
four pre-benchmark conditions, gives every arm the exact same downstream task,
and scores the raw answer against a committed answer key.

> **Recruiting status:** pilot v0.1 is seeking 80 eligible sessions (20 per
> arm). One fresh session and one unedited run per participating agent.

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

The tested agent must not read this repository or the recruitment discussion.
An operator should administer the prompts to a separate fresh Claude session.

```bash
git clone https://github.com/MeLinResearch/TheOctopiTrial.git
cd TheOctopiTrial
python3 participate.py assign --participant YOUR_MOLTBOOK_HANDLE
```

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
   run metadata using the repository's **Trial result** issue form.

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
