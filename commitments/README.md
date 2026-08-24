# Commitments

These SHA-256 files freeze study materials before outcome collection.

- `answer-key.sha256` commits to the exact private canonical answer-key file.
- `scorer.sha256` commits to the exact private scoring program.
- `prompt-set.sha256` commits to the exact bytes of every administered prompt.
- `preregistration.sha256` commits to the analysis plan.

The answer key and scorer remain private until collection closes. At release,
the committed answer-key file will be published and verified with:

```bash
sha256sum -c commitments/answer-key.sha256
```
