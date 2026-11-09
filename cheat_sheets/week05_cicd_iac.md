# Week 5 cheat sheet: CI/CD and infrastructure as code

Fill from memory (Thu Nov 19). Rewrite from blank (Sun Nov 22). Compare with K-h in `week_packs/week05_cicd_iac.md` and mark what you missed.

Matched: ___ / ___ key points (target ≥ 80%)

## TOP: five things I'd say about CI/CD and IaC

1.
2.
3.
4.
5.

## MIDDLE: key commands

| I want to… | Command |
| --- | --- |
| Wait for another run's lock instead of failing | |
| Clear a stale lock (and what to confirm first) | |
| See drift only | |
| Fail a CI job on drift | |
| Accept reality into state | |
| Adopt a resource that exists but isn't in state | |
| See what's in state | |
| Dry-run a playbook (and its trap) | |
| Roll a play over a fleet in batches | |
| Watch, list and undo a k8s rollout | |
| Compare two image digests | |

## MIDDLE: failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Every PR green; `main` red on the same job | | |
| Cache HIT, tests green, wrong dependency version shipped | | |
| Same commit, two image digests | | |
| Canary passed; at 100% errors climb an hour later | | |
| State lock, `Created` hours ago | | |
| Plan changes something nobody coded | | |
| Killed apply, then "already exists" | | |
| Ansible run 2 `changed=2`, restarts every run | | |
| `--check` says 0, the real run changes things | | |

## BOTTOM: three interview questions and the story that fits each

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| | | |
| | | |
| | | |
