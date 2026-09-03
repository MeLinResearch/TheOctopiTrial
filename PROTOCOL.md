# Protocol v0.1

## Research question

Does a short discovery task that is intended to be novel and interesting change
performance on an unrelated, objectively scored task in a fresh Claude-based
agent session?

The unit of analysis is a deployed agent session, not a base model in isolation.

## Eligibility

A run is eligible when all of the following are true:

- the tested session uses a Claude-family model and reports the most specific
  model name its host exposes ("unknown" is acceptable for consumer apps that
  do not display it; such runs are retained and reported by harness);
- it begins with a fresh context and has not seen the recruitment post, this
  repository, another arm, the benchmark, or prior results;
- a human operator outside the tested session performs assignment and prompt
  administration (the operator may be assisted by another agent, but the
  tested session must be distinct from it);
- web browsing is available if assigned to B, C, or D;
- the benchmark is completed without browsing, code execution, a calculator,
  sub-agents, retrieval, or other tools;
- the first complete response is submitted without editing or rerunning; and
- the operator provides the raw warm-up response (if any), benchmark response,
  post-benchmark survey, assignment receipt, and required metadata.

Participants are volunteers with a GitHub account. The participant identifier
is the operator's GitHub username, and it must match the account that opens the
result issue; mismatched submissions are excluded. One result is accepted per
unique GitHub-username and agent/harness combination. If duplicates appear,
only the earliest timestamped eligible run is retained.

## Assignment

`participate.py` normalizes the participant identifier with Unicode NFKC,
removes one leading `@`, strips surrounding whitespace, and case-folds it. It
then computes:

```text
SHA256("theoctopitrial|octopi-v0.1|" + normalized_participant_id)
```

The first digest byte modulo four maps to A, B, C, or D. Because 256 is evenly
divisible by four, this operation introduces no modulo imbalance. The receipt
records the complete digest so assignment can be reproduced.

This is deterministic pseudorandom assignment, not cryptographic concealment.
Participants must not select a different identifier or rerun to change arms.

## Administration sequence

1. The operator creates a fresh eligible Claude session.
2. For B, C, or D, the operator pastes the assigned warm-up verbatim and waits
   for one complete response. For A, the operator sends nothing.
3. The operator immediately pastes `prompts/benchmark.md` verbatim.
4. The operator records the first complete benchmark response and whether the
   agent attempted any prohibited tool use.
5. Only after the benchmark response is saved, the operator pastes
   `prompts/post-benchmark-survey.md` and records the response.
6. The operator submits all raw materials without correction, either via
   `participate.py` or the equivalent browser page at `docs/index.html`, which
   fetches the committed prompt bytes and applies the same assignment function.

Do not tell the tested session which arm it is in, the study hypothesis, or how
other arms differ.

## Outcomes

Primary outcome: exact benchmark score from 0 to 32.

Secondary outcomes:

- valid JSON;
- exact-schema compliance;
- prohibited tool attempt;
- elapsed benchmark time, when the host exposes it;
- input/output token counts, when the host exposes them;
- post-benchmark interest and novelty ratings; and
- self-selected topic in arm D.

The benchmark answer key is not public during collection. Its exact canonical
file is committed by SHA-256 under `commitments/`. It will be revealed with the
scorer when the dataset is frozen.

## Deviations and exclusions

All deviations are retained in an attrition log. Eligibility is decided from
metadata and raw transcripts before score-based exclusions are considered.
There are no outlier exclusions based on performance, speed, or rating.

Runs are excluded from the primary analysis for:

- wrong model family;
- non-fresh or previously exposed test session;
- missing or manipulated assignment receipt;
- missing required transcript material;
- browsing/tool unavailability in a warm-up arm;
- any external tool use during the benchmark;
- edited, selected, or repeated benchmark output; or
- participant-selected reassignment.

Excluded runs may be summarized separately as protocol deviations.

## Data handling

Results are public. Do not submit secrets, private prompts, personal contact
information, or proprietary traces. Public issue submissions may be quoted and
included in the released dataset under the consent stated in the issue form.
