# Week 6 cheat sheet: Observability and reliability

Fill from memory (Thu Nov 26). Rewrite from blank at Gate 2 (Sun Nov 29). Compare with K-h in `week_packs/week06_observability.md` and mark what you missed.

Matched: ___ / ___ key points (target ≥ 80%)

## TOP: five things I'd say about observability and reliability

1.
2.
3.
4.
5.

## MIDDLE: key commands

| I want to… | Command |
| --- | --- |
| See which scrape targets are down | |
| 5-minute error ratio | |
| p99 latency from a histogram | |
| Burn rate | |
| Validate and unit-test alert rules | |
| See firing and pending alerts | |
| See inhibited or silenced alerts | |
| Silence, list, expire | |
| Find high-cardinality metrics | |
| Count TIME_WAIT / connection churn on a client | |

## MIDDLE: failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Alert fires and clears every few minutes | | |
| 300 pages in 5 minutes | | |
| Users report errors, no alert fired | | |
| Average latency fine, users angry | | |
| A 30-second dependency blip turns into a 1-hour outage | | |
| Latency climbs, then everything times out | | |
| Prometheus OOMs or queries crawl | | |

## BOTTOM: three interview questions and the story that fits each

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| | | |
| | | |
| | | |
