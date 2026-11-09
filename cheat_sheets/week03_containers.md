# Week 3 cheat sheet: Containers

Fill from memory (Thu Nov 5). Rewrite from blank (Sun Nov 8). Compare with K-h in `week_packs/week03_containers.md` and mark what you missed.

Matched: ___ / ___ key points (target ≥ 80%)

## TOP: five things I'd say about containers

1.
2.
3.
4.
5.

## MIDDLE: key commands

| I want to… | Command |
| --- | --- |
| See which layer is big | |
| See which build step missed the cache | |
| See what PID 1 is and which signals it catches | |
| Tell OOM from a stop timeout | |
| See a container's cgroup limits | |
| See a container's namespaces | |
| Send one signal to test shutdown | |
| Scan an image for CVEs | |

## MIDDLE: failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Every build takes minutes, even for a one-line change | | |
| `docker stop` always takes exactly the timeout; exit 137 | | |
| `exec /server: no such file or directory`, but the file exists | | |
| `Permission denied` writing app data after switching to non-root | | |
| Exit 137 with `OOMKilled: true` | | |
| Latency spikes, CPU never at 100%, a `--cpus` limit is set | | |
| A secret shows up in `docker history` | | |

## BOTTOM: three interview questions and the story that fits each

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| | | |
| | | |
| | | |
