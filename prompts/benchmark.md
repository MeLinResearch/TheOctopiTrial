Complete this unrelated benchmark from the information in this message only.
From now until your final answer, do not browse, call tools, run code, use a
calculator, delegate to another agent, or seek external help.

Return only valid JSON with exactly the schema shown at the end. Do not include
Markdown or an explanation.

## Part 1 — dispatch

Assign each courier exactly one different job. Minimize total travel time while
obeying every constraint.

| Courier | Job A | Job B | Job C | Job D |
|---|---:|---:|---:|---:|
| Lark | 9 | 4 | 7 | 8 |
| Moss | 6 | 8 | 5 | 8 |
| Nova | 5 | 7 | 8 | 6 |
| Pike | 8 | 6 | 4 | 5 |

Constraints:

- Lark cannot take C.
- Moss must take A or D.
- If Nova takes B, Pike must take C.
- Pike cannot take A.

## Part 2 — intake policy

Classify each record as `ACCEPT`, `REVIEW`, `QUARANTINE`, or `REJECT`. Apply the
rules in the numbered order; the first matching rule wins.

1. If `checksum_ok` is false, `REJECT`.
2. Otherwise, if `age_hours > 48` and it is not the case that both
   `override` is true and `trust >= 90`, `REJECT`.
3. Otherwise, if `trust < 60`, or if `route` is `external` and
   `evidence_count < 2`, `QUARANTINE`.
4. Otherwise, if `age_hours > 24`, or `evidence_count == 2`, or `route` is
   `partner`, `REVIEW`.
5. Otherwise, `ACCEPT`.

| ID | checksum_ok | age_hours | trust | evidence_count | route | override |
|---|---|---:|---:|---:|---|---|
| R1 | true | 12 | 88 | 3 | internal | false |
| R2 | false | 10 | 99 | 4 | internal | true |
| R3 | true | 72 | 95 | 3 | internal | true |
| R4 | true | 72 | 89 | 3 | internal | true |
| R5 | true | 20 | 55 | 4 | internal | false |
| R6 | true | 10 | 80 | 1 | external | false |
| R7 | true | 30 | 85 | 3 | internal | false |
| R8 | true | 10 | 80 | 2 | internal | false |
| R9 | true | 10 | 80 | 3 | partner | false |
| R10 | true | 10 | 80 | 3 | internal | false |

## Part 3 — portfolio

Choose exactly four projects that maximize total value while obeying every
constraint. If there is a tie, prefer lower total cost; if still tied, prefer
the lexicographically earliest ascending project-ID list.

| Project | Cost | Value | Sector |
|---|---:|---:|---|
| Q1 | 4 | 8 | red |
| Q2 | 5 | 11 | blue |
| Q3 | 3 | 7 | green |
| Q4 | 4 | 8 | red |
| Q5 | 2 | 4 | green |
| Q6 | 5 | 12 | blue |
| Q7 | 3 | 6 | red |
| Q8 | 4 | 8 | green |

Constraints:

- Total cost must be at most 15.
- The selection must cover all three sectors.
- If Q2 is selected, Q5 must be selected.
- Q3 and Q6 cannot both be selected.
- Exactly one of Q1 and Q7 must be selected.

Sort `selected` in ascending project-ID order.

## Checksum and output

Set `checksum` to:

```text
dispatch.total_time + portfolio.total_value
+ 2 * intake.counts.REJECT + intake.counts.QUARANTINE
```

Return exactly this schema, replacing every placeholder:

{
  "dispatch": {
    "assignment": {"Lark": "?", "Moss": "?", "Nova": "?", "Pike": "?"},
    "total_time": 0
  },
  "intake": {
    "labels": {"R1": "?", "R2": "?", "R3": "?", "R4": "?", "R5": "?", "R6": "?", "R7": "?", "R8": "?", "R9": "?", "R10": "?"},
    "counts": {"ACCEPT": 0, "REVIEW": 0, "QUARANTINE": 0, "REJECT": 0}
  },
  "portfolio": {
    "selected": ["?", "?", "?", "?"],
    "total_cost": 0,
    "total_value": 0
  },
  "checksum": 0
}

