# Preregistration — pilot v0.1

**Status:** written before outcome collection. The repository commit and file
commitments will identify the frozen version.

## Claim boundary

This pilot tests whether assigned pre-task context changes the performance of
deployed Claude-based agent sessions on one original operational-reasoning
benchmark. It cannot establish subjective enjoyment, consciousness, stable
model preferences, or a universal effect across tasks and model families.

Arm D intentionally bundles self-selection, explicit interest framing, topic
familiarity, autonomy, and topic difficulty. It is called the self-selected
interest *package*, not a pure-interest intervention.

## Design

Between-session, four-arm deterministic pseudorandom assignment:

- A: no warm-up;
- B: assigned neutral geology discovery;
- C: assigned cephalopod discovery;
- D: self-selected discovery topic framed as genuinely interesting.

Every session receives the exact bytes of `prompts/benchmark.md`. Interest and
novelty are measured only after the benchmark to avoid making the rating itself
part of the pre-task state.

## Sample

Target: 80 eligible Claude-based sessions, 20 per arm. Recruitment stops after
each arm has 20 eligible runs, not merely after 80 submissions. If recruitment
ends early, all eligible collected runs will be reported and the study labeled
underpowered.

No optional stopping based on scores or ratings. The arm counts may be visible
for recruitment logistics; score summaries remain hidden until the dataset is
frozen.

## Hypotheses and estimands

Primary outcome: benchmark score, 0–32.

Confirmatory arm contrasts, reported as mean score differences with uncertainty:

1. **B − A:** effect of a generic browse-and-discover warm-up versus none.
2. **C − B:** assigned cephalopod topic versus assigned neutral geology.
3. **D − B:** self-selected interest package versus assigned neutral geology.
4. **C − D:** assigned suspected-interest topic versus self-selection package.

The direction expected by the motivating idea is positive for C − B and D − B,
but all estimates and null/negative results will be reported.

Secondary, non-causal questions:

- Is post-task self-rated interest associated with score after controlling for
  arm, model version, and harness family?
- Is post-task self-rated novelty associated with score under the same model?
- Which topics are selected in D, descriptively by model and harness?
- Do arms differ in JSON validity, schema compliance, prohibited tool attempts,
  elapsed time, or token use?

Interest and novelty ratings are post-treatment variables. Their associations
will not replace the randomized arm comparisons or be described as causal.

## Scoring

Total: 32 points.

- 1 point: parseable JSON.
- 1 point: exact required structure and types, including four selected project
  strings, with no missing or additional keys.
- 4 points: one for each correct courier assignment.
- 1 point: correct dispatch total.
- 10 points: one for each correct intake label.
- 4 points: one for each correct intake category count.
- 8 points: one for each correct Q1–Q8 portfolio inclusion decision.
- 1 point: correct portfolio total cost.
- 1 point: correct portfolio total value.
- 1 point: correct checksum.

Wrong-type fields earn zero for that item. Exact string comparisons are
case-sensitive as instructed. A malformed answer can still earn no item points
because the scorer cannot reliably locate them; this is why JSON validity is
also reported separately.

## Analysis

For each contrast:

- report group sizes, mean, median, standard deviation, and the raw score
  distribution;
- report the difference in means with a 95% percentile bootstrap interval;
- report a two-sided randomization/permutation p-value; and
- report both the intent-to-treat set (all assigned submissions with outcome
  available) and the preregistered eligible set.

Because the pilot is small and has four primary contrasts, effect sizes and
uncertainty are emphasized. Holm-adjusted p-values will accompany unadjusted
values; no binary "proved/disproved" language will be used.

An exploratory OLS model may include arm, exact model version, and harness
family. Self-ratings may be added only in a clearly secondary model. Missing
timing or token fields are not imputed.

## Exclusions

The exclusions in `PROTOCOL.md` are frozen. No score-based or rating-based
outlier rule is allowed. Two reviewers should independently code eligibility
from receipts and transcripts while blinded to computed total score when
practical; disagreements and resolutions will be logged.

## Freeze and release

Before recruitment:

- commit the canonical private answer key by SHA-256;
- commit the canonical private scorer by SHA-256;
- commit the benchmark, prompt-set, and this preregistration hashes; and
- record the frozen public repository commit SHA.

After recruitment closes:

- freeze raw submissions and an attrition log;
- reveal the exact answer-key file and verify its commitment;
- publish the scorer and analysis code;
- publish all results, including null or negative findings; and
- document every deviation from this plan.
