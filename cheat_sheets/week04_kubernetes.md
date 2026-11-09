# Week 4 cheat sheet: Kubernetes

Fill from memory (Thu Nov 12). Rewrite from blank (Sun Nov 15). Compare with K-h in `week_packs/week04_kubernetes.md` and mark what you missed.

Matched: ___ / ___ key points (target ≥ 80%)

## TOP: five things I'd say about Kubernetes

1.
2.
3.
4.
5.

## MIDDLE: key commands

| I want to… | Command |
| --- | --- |
| See why a pod is Pending | |
| See why the last container died (reason + exit code) | |
| Read the crashed container's logs | |
| See events, newest last | |
| See a pod's QoS class | |
| Live CPU/memory per container | |
| See what's already requested on a node | |
| Watch a rollout, then undo it | |
| Take a node out for maintenance safely, then bring it back | |
| See why the HPA isn't scaling | |
| Shell into a distroless pod | |
| Debug the node itself | |

## MIDDLE: failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Pending: `0/3 nodes are available: 3 Insufficient cpu` | | |
| CrashLoopBackOff, exit 1 | | |
| CrashLoopBackOff, exit 143, logs stop mid-startup, no error | | |
| OOMKilled, exit 137, node has plenty of free memory | | |
| Running, READY 0/1, 0 restarts | | |
| ImagePullBackOff | | |
| Rollout stuck, `ProgressDeadlineExceeded` | | |
| `kubectl drain` hangs on `Cannot evict pod…` | | |
| HPA TARGETS `<unknown>` | | |
| Pod `Evicted`: "The node was low on resource: memory" | | |
| Latency spikes while CPU usage is under the limit | | |

## BOTTOM: three interview questions and the story that fits each

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| | | |
| | | |
| | | |
