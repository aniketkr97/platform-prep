# Week 7 cheat sheet: Distributed systems

Fill from memory (Thu Dec 3). Rewrite from blank (Sun Dec 6). Compare with K-h in `week_packs/week07_distributed_systems.md` and mark what you missed.

Matched: ___ / ___ key points (target ≥ 80%)

## TOP: five things I'd say about distributed systems

1.
2.
3.
4.
5.

## MIDDLE: key commands

| I want to… | Command |
| --- | --- |
| See which etcd node is leader, and the term | |
| Check every member is healthy | |
| List members (spot stale ones) | |
| Create a lease, attach a key, see time left | |
| Take a lock with a TTL | |
| Find the fencing token for a lock | |
| Read without a quorum (and know the risk) | |
| Check the disk is fast enough for etcd | |
| Back up etcd before touching members | |

## MIDDLE: failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Two nodes both act as primary after a network blip | | |
| A client reads older data than it just wrote | | |
| Writes hang after 2 of 3 nodes die | | |
| Leader changes every few seconds; term keeps climbing | | |
| A rejoining node forces an election with a healthy leader | | |
| A lease holder writes after its lease expired | | |
| One cache node hot, the rest idle | | |
| An acknowledged write is gone after failover | | |

## BOTTOM: three interview questions and the story that fits each

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| | | |
| | | |
| | | |
