# WEEK PACK — Week 4: Kubernetes

Infra layer: scheduler, kubelet, probes, requests and limits, QoS, HPA, KEDA · Code: heaps as schedulers, regret greedy, ordered sets · Design: multi-tenant Kubernetes platform · Story: Kubernetes fleet upgrade

**Rule for this file:** do every section cold first. Every answer, note, hint and reference is in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section. There is no LeetCode code anywhere in this file, and no template code either: problems go through the hint ladder one rung at a time, and the template drill is graded on your own file.

Lab starter files (working manifests you break on purpose, no answers): `week_packs/week04_lab/`.

---

## 0. This week's plan

### 0a. Dates

The plan puts Week 4 on Nov 2–8, but the Week 3 pack (made today, Nov 1) runs Week 3 on **Mon Nov 2 – Sun Nov 8**. So this pack runs **Mon Nov 9 – Sun Nov 15**. If you'd rather start Week 4 tomorrow, tell me and I'll shift every date back a week.

**Knock-on:** Gate 2 (planned Sat Nov 21) tests Weeks 4–6. With the one-week shift, the suggested new date is **Sat Nov 28**.

**Tools:** `kind`, `kubectl` and `docker` aren't installed on this Mac yet. Step 0 of the lab (§c) installs them. Do it Monday night.

**Unknown backlog:** I still have no redo results for Weeks 1–3. The review counts below assume every Week 3 redo is Clean. Tell me each result and I'll recount before Monday.

### 0b. This week's problems

| # | Problem | Diff | Role | Your history (LeetCode, Oct 6) | How it's run |
| --- | --- | --- | --- | --- | --- |
| 215 | Kth Largest Element in an Array | M | Core | Apr 2026, **7 submits (shaky)** | Cold redo, ≤ 25 min, **first in its day** |
| 56 | Merge Intervals | M | Core | Aug 2026, **16 submits (shaky)** | Cold redo, ≤ 25 min, **first in its day** |
| 253 | Meeting Rooms II (Premium; free mirror: LintCode 919) | M | Core | **Nov 2024**, 3 submits (fading) | Cold redo, ≤ 25 min |
| 295 | Find Median from Data Stream | H | Core | Sep 2025, **last result WA → counts as new** | First try, 50 min |
| 1834 | Single-Threaded CPU | M | Required · **Learn** | New | Learn row: 40 min alone |
| 630 | Course Schedule III | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 220 | Contains Duplicate III | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 355 | Design Twitter | M | Required · practical | New | First try, 35 min + follow-up aloud |
| 1882 | (Friday check: don't open it before Friday) | M | Check | New | 45 min, alone, no hints, Friday |

⚠ **The coding page's three Week 4 templates are worked solutions to 1834, 630 and 220.** Don't open the Week 4 templates on the coding page until all three first tries are done, or they count as "Needed the solution". Monday's drill (§d0) uses two generic templates instead.

⚠ **Don't open 2402 or 1851 before Saturday.** One of them is the mock's coding problem.

### 0c. Day by day

| Day | Reviews first | Infra / apply | Code | Other |
| --- | --- | --- | --- | --- |
| **Mon Nov 9** | W3: 124, 102, 98, 1114 (R2) = 4 | §a warm-up cold (10) → §b questions cold → read → K-b (45) | §d0 template drill (15) → **1834** (Learn, 40) | Lab Step 0 tonight (20) |
| **Tue Nov 10** | 1834 (R1) · W3: 2581 (R2) = 2 | §c labs 1–2 (50) | **630** (Learn) → **295** (first try) | Recall warm-up (10) |
| **Wed Nov 11** | 630, 295 (R1) · W3: mock problem (R2) = 3 | §b2 teach-backs, recorded, no notes (25) · §e Drill 1 (30) | **220** (Learn) → **355** (practical) | — |
| **Thu Nov 12** | 220, 355 (R1) = 2 | §c labs 3–4 (50) · §h cheat sheet from memory (30) · §k story (20) | **215\***, **56\***, **253** cold redos | — |
| **Fri Nov 13** | 1834 (R2) · 215, 56, 253 (R1) · W3: 337 (R3) = **5, at the cap** | §f design: your drawing first (40) · §e Drill 2 (30) | **1882** check, 45 min, alone | — |
| **Sat Nov 14** | 630, 295 (R2) · 1882 (R1) · W3: 968, 236 (R3) = **5** | §j **75-min full-loop mock** · design redrawn from memory (90) · §e Drill 3 timed 20 min · debrief (45) | (mock coding) | — |
| **Sun Nov 15** | 220, 355 (R2) · mock problem (R1) · W3: 834, 609 (R3) = **5** | Cheat sheet rewritten from memory (30) | Extras (§d2), as many as fit (60) | Plan Week 5 (15) |

\* shaky by history: do these first on Thursday, before 253.

The plan's Tuesday lab slot is 50 minutes, and four labs take about 100, so labs 3–4 go on Thursday. **One Shaky or Failed redo pushes Fri–Sun past the cap of 5.** If that happens, Friday's check still runs (it's the week's test), but Sunday's extras are cancelled.

### 0d. Session rules (same as Weeks 2–3)

- Say **"start 1834"** (or any number) and I log the start time. 60-second approach aloud, brute force first, complexity before code.
- Hints: one rung per request, only after 25 min stuck. A Learn row gets the full 40 minutes first. No hints at all during the Friday check. If you ask for a solution, you get the next rung instead.
- I compile your file with `clang++ -std=c++17 -Wall -Wextra` and show compile errors. I never fix or rewrite your code.
- Marks: first tries **Solved alone / Needed the solution**. Redos **Clean** (first submit, < 25 min, no hint) / **Shaky** (slow, 2+ submits, or one hint) / **Failed**.

---

## (a) Day 1 recall warm-up (cold, aloud, before any reading)

10 questions: 7 Week 4 (you haven't read anything yet, so answer from what you already know) and 3 from earlier weeks. One or two sentences each. Mark each ✓ / ✗ before opening K-a.

1. You `kubectl apply` a Deployment. Name, in order, every component that acts before a container is running on a node.
2. Which component picks the node? Does it look at a node's actual CPU usage, or something else?
3. A liveness probe fails 3 times in a row. Who acts, and what happens? Same question for a readiness probe.
4. A container goes over its CPU limit. Then another goes over its memory limit. What happens to each?
5. Name the three QoS classes and the exact rule that puts a pod in each.
6. What does `CrashLoopBackOff` mean? Is it a pod phase? How long does the kubelet wait between restarts?
7. An HPA targets 50% CPU. 3 pods average 90%. How many replicas does it ask for? Show the formula.
8. *(Week 3)* A pod takes exactly 30 s to terminate on every rollout and its last state shows exit 137. What's the likely cause, and where does the 30 come from?
9. *(Week 2, F8)* In a Kubernetes cluster, what fills the `nf_conntrack` table, and what do you see when it's full?
10. *(Week 1)* How does the kernel OOM killer pick its victim, and which file lets you bias it?

---

## (b) Reading: questions first, then the notes

**Read:** Kubernetes docs: *Pod Lifecycle*, *Resource Management for Pods and Containers*, *Debug Pods*, *Horizontal Pod Autoscaling*; the KEDA *Concepts* page (keda.sh/docs → Concepts). Search the titles if a link moved.

**Before reading, answer from memory** (aloud or on paper, 1–2 sentences each):

*Pod lifecycle*
- B1. Name the five pod phases. Where does `CrashLoopBackOff` live, if not in the phase?
- B2. The three `restartPolicy` values and the default. Which one does a Deployment allow?
- B3. Walk through `kubectl delete pod`: what happens, in what order, with which default timeout?
- B4. The default `periodSeconds`, `timeoutSeconds` and `failureThreshold` for a probe. What does a startup probe switch off while it runs?

*Resource management*
- B5. `cpu: 250m` and `memory: 128Mi` mean what, exactly? What does `memory: 128m` mean, and why is it a bug?
- B6. You set a limit but no request. What request does the container get?
- B7. Which kernel mechanism enforces each kind of limit?

*Debug Pods*
- B8. Pod is `Pending`; pod is `Waiting` (e.g. `ImagePullBackOff`); pod is crashing. First command for each?
- B9. Three forms of `kubectl debug` and when you'd use each.

*HPA*
- B10. The HPA formula, how often it runs, its tolerance, and the default scale-down delay.
- B11. Which metrics APIs can an HPA read, and what serves the basic one?

*KEDA*
- B12. What does KEDA add that a plain HPA can't do? Name its two main custom resources and say who scales 0 ↔ 1 vs 1 ↔ N.

Then read the five pages **only for what you missed**, then compare with the notes in **K-b**.

### (b2) Explain-aloud: three 2-minute teach-backs (Wednesday, recorded, no notes)

Record each one cold. Listen once. Stumbled more than five times? Redo it. Outlines and follow-up answers are in **K-b2**. Read them only after your first recording.

**T1. Scheduler vs kubelet: who decides what.** "Walk me through what the scheduler does and what the kubelet does."
Most likely follow-ups:
1. A pod has been `Pending` for 10 minutes. Whose problem is it, and what do you look at?
2. Does the scheduler place pods using actual node CPU usage?
3. A node dies. Who moves its pods, and how long does it take by default?
4. Can a pod run without going through the scheduler? Give two ways.
5. A pod is scheduled but stuck in `ContainerCreating`. Whose problem now?

**T2. Requests vs limits and the three QoS classes.** "What's the difference between requests and limits, and what are QoS classes for?"
Most likely follow-ups:
1. Should you set CPU limits? Defend your answer.
2. A node runs low on memory. Which pods go first, and is that the same thing as an OOM kill?
3. A container sets limits but no requests. What QoS class is the pod?
4. How do you stop teams from deploying pods with no requests at all?
5. Your p99 latency spikes while CPU usage is well under the limit. What's going on?

**T3. Why a pod gets OOMKilled, including when the node has free memory.**
Most likely follow-ups:
1. How do you tell an OOM kill from an eviction from a liveness kill?
2. A JVM runs in a 1 GiB container with `-Xmx1g`. What's wrong?
3. `kubectl top` showed 700Mi one minute before the kill at a 1Gi limit. How?
4. Does page cache count against the container's limit?
5. Where on the node do you confirm the kernel did the kill?

---

## (c) Lab sheet (Tuesday labs 1–2, Thursday labs 3–4; real commands, record what you see)

Run everything for real. For every step: write your **Prediction** before running, then the **Observed** result, then **What this proves** in one line. Expected observations are in **K-c**. Open it only after you've filled your own.

**Mac note:** kind runs each Kubernetes node as a Docker container inside the Colima (or Docker Desktop) Linux VM. "Node memory" is the VM's memory. Run all commands from `~/Platform Prep`.

### Step 0: install and verify (Monday night, ~20 min)

```bash
brew install kind kubectl
# If Docker isn't set up from Week 3: pick ONE runtime
brew install colima docker && colima start --cpu 4 --memory 8      # or install Docker Desktop
kind create cluster --name w4 --config week_packs/week04_lab/kind.yaml
kubectl get nodes -o wide
```

Prediction: how many nodes, what roles, and which node won't take your pods (and why)? ______
Observed: ______

### Lab 1: break a probe and watch the kubelet (Tuesday)

`week_packs/week04_lab/lab1_probes/web.yaml` is a working nginx Deployment (2 replicas) + Service. Readiness checks `/index.html`; liveness checks `/50x.html`. Both files ship inside the nginx image.

```bash
kubectl apply -f week_packs/week04_lab/lab1_probes/web.yaml
kubectl get pods -l app=web -o wide
P=$(kubectl get pod -l app=web -o name | head -1); echo $P
# Helper: list each endpoint behind the Service with its ready flag
EPS='{range .items[*].endpoints[*]}{.addresses[0]}{"  ready="}{.conditions.ready}{"\n"}{end}'
kubectl get endpointslices -l kubernetes.io/service-name=web -o jsonpath="$EPS"
```

**1a. Break readiness on one pod.**
```bash
kubectl exec $P -- rm /usr/share/nginx/html/index.html
kubectl get pods -l app=web -w            # Ctrl-C after ~30 s
kubectl get endpointslices -l kubernetes.io/service-name=web -o jsonpath="$EPS"
kubectl describe $P | tail -15
```
Prediction (READY, RESTARTS, endpoint, after 30 s): ______
Observed (include the exact Event text and status code): ______
What this proves: ______

Restore it: `kubectl exec $P -- sh -c 'echo ok > /usr/share/nginx/html/index.html'`. How long until it's back in the endpoints? ______

**1b. Break liveness on the same pod.**
```bash
kubectl exec $P -- rm /usr/share/nginx/html/50x.html
kubectl get pods -l app=web -w            # time it from the rm
kubectl describe $P | tail -15
kubectl exec $P -- ls /usr/share/nginx/html/
```
Prediction (how many seconds until something happens; is the pod name/IP the same after; is `50x.html` back?): ______
Observed: ______
What this proves: ______

**1c. Break liveness permanently.**
```bash
kubectl patch deployment web --type=json \
  -p='[{"op":"replace","path":"/spec/template/spec/containers/0/livenessProbe/httpGet/path","value":"/nope"}]'
kubectl rollout status deployment web
kubectl get pods -l app=web -w            # leave it 5 minutes
P2=$(kubectl get pod -l app=web -o name | head -1)
kubectl get $P2 -o jsonpath='{.status.containerStatuses[0].lastState.terminated}{"\n"}'
```
Predictions: (i) does the rollout finish? (ii) what STATUS values do you see over 5 min? (iii) what exit code and reason will `lastState` show? ______
Observed: ______
What this proves (about exit codes in particular): ______

**1d (optional, 10 min). Startup probe.** Put liveness back, then add a startup probe that always fails:
```bash
kubectl rollout undo deployment web
kubectl patch deployment web --type=json \
  -p='[{"op":"add","path":"/spec/template/spec/containers/0/startupProbe","value":{"httpGet":{"path":"/nope","port":80},"periodSeconds":5,"failureThreshold":4}}]'
kubectl get pods -l app=web -w
```
Prediction (READY of the new pod; seconds until its first restart; does the rollout finish?): ______
Observed: ______
Clean up: `kubectl rollout undo deployment web`

### Lab 2: produce an OOMKill, and read QoS from the node's point of view (Tuesday)

`lab2_oom/hog.yaml` allocates 10 MiB every half second and prints the running total. Its memory limit is 100Mi.

**2a. OOMKill.**
```bash
kubectl apply -f week_packs/week04_lab/lab2_oom/hog.yaml
kubectl get pod hog -w                     # leave it ~3 minutes
kubectl logs hog --previous | tail -3
kubectl get pod hog -o jsonpath='{.status.containerStatuses[0].lastState.terminated}{"\n"}'
kubectl describe pod hog | sed -n '/Last State/,/Restart Count/p'
```
Prediction (the last line it prints before dying; STATUS values over 3 min; gap between restarts): ______
Observed: ______

**2b. The node still has free memory.**
```bash
N=$(kubectl get pod hog -o jsonpath='{.spec.nodeName}'); echo $N
docker exec $N free -m
kubectl describe node $N | sed -n '/Allocated resources/,/Events/p'
```
Prediction: ______
Observed (free MiB on the node at the time of the kill): ______
What this proves: ______

**2c. Find the limit the kernel enforced.**
```bash
kubectl apply -f week_packs/week04_lab/lab2_oom/qos.yaml
kubectl exec qos-c -- cat /sys/fs/cgroup/memory.max /sys/fs/cgroup/cpu.max
# cgroup v1 fallback, if those files don't exist: /sys/fs/cgroup/memory/memory.limit_in_bytes
```
Prediction (both values, exactly, given `qos-c` has 64Mi and 100m): ______
Observed: ______

**2d. QoS classes and OOM scores.**
```bash
kubectl get pod qos-a qos-b qos-c -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass
for p in qos-a qos-b qos-c; do printf "%s " $p; kubectl exec $p -- cat /proc/1/oom_score_adj; done
kubectl get node $(kubectl get pod qos-b -o jsonpath='{.spec.nodeName}') -o jsonpath='{.status.capacity.memory}{"\n"}'
```
Prediction (class and `oom_score_adj` for each; for qos-b, work the number out from the node's memory capacity before you run it): ______
Observed: ______
What this proves (who dies first if the whole node runs out): ______

Clean up: `kubectl delete pod hog qos-a qos-b qos-c`

### Lab 3: drain a node, watch eviction and rescheduling (Thursday)

```bash
kubectl delete deployment web --ignore-not-found
kubectl apply -f week_packs/week04_lab/lab1_probes/web.yaml
kubectl scale deployment web --replicas=6
kubectl apply -f week_packs/week04_lab/lab3_drain/lonely.yaml     # bare pod, pinned to w4-worker
kubectl get pods -o wide                                         # tally pods per node
```

**3a. Drain with no flags.**
```bash
kubectl drain w4-worker
kubectl get nodes
```
Prediction (does it succeed? what state is the node left in?): ______
Observed (the exact reasons it gives): ______

**3b. Add a strict PDB, then drain with flags.** Open a second terminal: `kubectl get pods -l app=web -o wide -w`
```bash
kubectl apply -f week_packs/week04_lab/lab3_drain/pdb-strict.yaml
kubectl get pdb
kubectl drain w4-worker --ignore-daemonsets --force --timeout=60s
```
Prediction (what happens to `lonely`, to the web pods, to the drain command): ______
Observed: ______

**3c. Loosen the PDB and drain again.**
```bash
kubectl patch pdb web-pdb --type=merge -p '{"spec":{"maxUnavailable":1}}'
kubectl drain w4-worker --ignore-daemonsets --force
kubectl get pods -o wide
kubectl get pod lonely
```
Prediction (order and pace of evictions; pod names and IPs of the replacements; where `lonely` ends up): ______
Observed: ______

**3d. Uncordon.**
```bash
kubectl uncordon w4-worker
kubectl get pods -l app=web -o wide          # wait a minute
```
Prediction (do any pods move back?): ______
Observed: ______
What 3a–3d prove (one line on "moved" vs "replaced", one on what a PDB protects against): ______

Clean up: `kubectl delete deployment web; kubectl delete pdb web-pdb`

### Lab 4: add an HPA and drive load until it scales (Thursday)

**4a. Install metrics-server** (kind's kubelets use self-signed certs, hence the extra flag):
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl -n kube-system patch deployment metrics-server --type=json \
  -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
kubectl -n kube-system rollout status deployment metrics-server
kubectl top nodes                          # may need ~60 s before it returns data
```

**4b. HPA on a Deployment with no requests.** `lab4_hpa/cpu-app.yaml` burns CPU on every GET. It deliberately has no `resources` block.
```bash
kubectl apply -f week_packs/week04_lab/lab4_hpa/cpu-app.yaml
kubectl autoscale deployment cpu-app --cpu-percent=50 --min=1 --max=6
# If your kubectl prints a deprecation notice for --cpu-percent, use the flag it suggests.
kubectl get hpa cpu-app
kubectl describe hpa cpu-app | tail -15
```
Prediction (TARGETS column; the condition message): ______
Observed: ______

**4c. Add requests.**
```bash
kubectl set resources deployment cpu-app -c app --requests=cpu=100m --limits=cpu=500m
kubectl get hpa cpu-app -w                 # wait until TARGETS shows a number, then Ctrl-C
```

**4d. Drive load.** Terminal 2: `kubectl get hpa cpu-app -w` · Terminal 3: `kubectl get pods -l app=cpu-app -w`
```bash
kubectl run load --image=busybox:1.36 --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://cpu-app:8080 >/dev/null; done"
```
Log a row every time TARGETS or REPLICAS changes:

| Clock time | TARGETS | REPLICAS | Your formula check: ceil(replicas × current / 50) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

Prediction (the highest utilization % one pod can ever report here, and why; roughly where replicas settle): ______
Observed: ______

**4e. Remove load.**
```bash
kubectl delete pod load
kubectl get hpa cpu-app -w
```
Prediction (minutes until the first scale-down): ______
Observed: ______
What 4b–4e prove: ______

**4f (10 min, paper only). KEDA.** Without installing it: write the `ScaledObject` you'd use to scale `cpu-app` from 0 to 20 on a queue's length (any queue you know). List the fields you'd set and the two numbers you'd tune first. Compare with K-c.

Clean up the whole lab: `kind delete cluster --name w4`

---

## (d) Coding

### (d0) Monday template drill (blank file, 15 min, compiled)

**Templates (names only, no reference code is given anywhere in this pack):**
- **W4-T1: Heap with a custom comparator, plus lazy deletion.**
- **W4-T2: Ordered-set (`std::multiset`) idioms.**

**Format:**
1. Timer starts on a blank `w4_templates.cpp`. No notes, no autocomplete, no lookups.
2. Write both templates and a `main()` with `assert`s that prove the behaviours below. You write the asserts too.
3. Say "compile" and I run `clang++ -std=c++17 -Wall -Wextra w4_templates.cpp && ./a.out`.

**Behaviours your asserts must prove:**

| T1 | T2 |
| --- | --- |
| A min-heap of `(priority, id)` pairs pops ties by smaller id | Inserting a duplicate keeps both copies |
| A max-heap built with a **comparator struct** (not `less<>`) | Erasing **exactly one** copy of a duplicated value |
| A heap ordered by a **lambda** comparator | Smallest value ≥ x, and "none exists" handled |
| Lazy deletion: mark an id as removed; a "clean the top" step skips it when it surfaces; the next valid top is correct | Largest value ≤ x, including the case where x is below the minimum |
| Sums of values up to 1e9 don't overflow | Min and max in O(1) |

**Pass** = under 15:00, zero warnings, every assert passes, no lookup. **Fail** = any of those missed. A failed template goes on the review schedule like a problem (row in §i).

### (d1) Pattern map: the 9 problems

The pattern name is given up front this week because you asked for it. The hint ladders (direction → key insight → skeleton in words) are in **K-d**, one rung at a time, after 25 minutes stuck.

| # | Problem | Pattern | Why it's in Week 4 | One question to answer before coding | First try / redo mark |
| --- | --- | --- | --- | --- | --- |
| 215 | Kth Largest | Size-k heap (or quickselect) | The smallest heap problem; the "keep only k" idea is the base of every top-k dashboard | Why does a **min**-heap find the k-th **largest**? | |
| 56 | Merge Intervals | Sort by start + one-pass merge | Intervals are time windows: maintenance windows, leases, reservations | After sorting, which intervals can a new one possibly overlap? | |
| 253 | Meeting Rooms II | Min-heap of end times (or sweep line) | A resource allocator: how many slots do concurrent jobs need? | When a meeting starts, which room is the only one worth checking? | |
| 295 | Median from Data Stream | Two heaps | Streaming percentiles: the p50 of a latency stream | What must be true of the two halves for the median to be O(1)? | |
| 1834 | Single-Threaded CPU | Event simulation: sort + min-heap + clock | Literally a CPU scheduler: the platform interview's favourite heap problem | When the CPU is free, which tasks are even eligible, and what if none are? | |
| 630 | Course Schedule III | Regret greedy (max-heap) | "Admit greedily, evict the worst when over budget": admission control | If adding this course makes you late, which earlier choice do you give up, and why is that never worse? | |
| 220 | Contains Duplicate III | Ordered set over a sliding window | Your thinnest technique (4 ordered-set solves); same idioms as the scheduler's free list | In a window of values, what single query tells you whether anything is within `valueDiff` of x? | |
| 355 | Design Twitter | k-way merge heap + hash maps | Practical: a feed is a merge of sorted streams (log merging, too) | To get the 10 newest across all followees, how much of each followee's list do you need to look at? | |
| 1882 | Friday check | **Sealed until Friday** | **Sealed** | **Sealed** | |

### (d2) After-required rows (Thursday leftovers and Sunday extras)

In order: 871, 502, 480, 218, 632, 352, 1797. **Not 2402 or 1851 before Saturday.** Ask me for each one's hint ladder only when you're stuck.

---

## (e) Troubleshooting drills (symptoms only)

Answer in your routine, out loud, as if to an interviewer: **Clarify → Scope → Stabilise → Hypothesise → Check → Fix-and-prevent** ("Can Some Students Handle Cold Fixes"). Ask me questions as you go and I answer from the interviewer sheet in K-e (which you don't read). I score each step afterwards.

### Drill 1: CrashLoopBackOff (Wednesday, 30 min)

> In staging (Deployment strategy `Recreate`, 3 replicas), the `orders-api` team released v2.14.0 at 14:05. The release adds database schema migrations that run when the app starts. Since then:
>
> ```
> $ kubectl get pods -n orders -l app=orders-api
> NAME                          READY   STATUS             RESTARTS        AGE
> orders-api-7d9c6b5f8d-2kq4m   0/1     CrashLoopBackOff   6 (2m11s ago)   19m
> orders-api-7d9c6b5f8d-9xw7p   0/1     Running          6 (48s ago)     19m
> orders-api-7d9c6b5f8d-tq5zn   0/1     CrashLoopBackOff   6 (1m30s ago)   19m
>
> $ kubectl logs -n orders orders-api-7d9c6b5f8d-2kq4m --previous
> 2026-11-11T14:21:03Z INFO  Starting orders-api v2.14.0
> 2026-11-11T14:21:04Z INFO  Connected to postgres orders-db:5432
> 2026-11-11T14:21:04Z INFO  Running schema migrations (142 pending)...
> 2026-11-11T14:21:31Z INFO  Migration 0057 applied
>
> $ kubectl describe pod -n orders orders-api-7d9c6b5f8d-2kq4m | grep -A3 "Last State"
>     Last State:     Terminated
>       Reason:       Error
>       Exit Code:    143
> ```
>
> No stack trace. The developer says: "It starts fine on my laptop with `docker run`. It just takes a few minutes."

### Drill 2: OOMKilled while the node has free memory (Friday, 30 min)

> `pricing-svc` (Java 17, Spring Boot, Netty client) runs in production, 6 replicas. Pods restart 3–6 times a day, mostly at peak traffic.
>
> ```
> $ kubectl get pod -n pricing pricing-svc-5c7f9b8d6-x2vbn \
>     -o jsonpath='{.status.containerStatuses[0].lastState.terminated}'
> {"exitCode":137,"reason":"OOMKilled","startedAt":"2026-11-13T09:02:11Z","finishedAt":"2026-11-13T11:47:40Z"}
> ```
>
> The pod's node (64 GiB) showed 38 GiB available at 11:47. Grafana's JVM heap panel peaks at 610 MiB. `kubectl top pod` at 11:46 showed 742Mi. The on-call engineer says: "The node has tons of free memory, so it isn't a memory problem. It must be a JVM bug. Let's open a vendor ticket."

### Drill 3: a deployment stuck at 50% rollout (Saturday, timed 20 min)

> ```
> $ kubectl rollout status deploy/checkout -n shop
> Waiting for deployment "checkout" rollout to finish: 5 out of 10 new replicas have been updated...
> ```
>
> It has printed that for 40 minutes.
>
> ```
> $ kubectl get rs -n shop -l app=checkout
> NAME                  DESIRED   CURRENT   READY   AGE
> checkout-58d7f6c9b4   5         5         0       41m
> checkout-7b9c8d5f6a   8         8         8       12d
>
> $ kubectl get pods -n shop -l pod-template-hash=58d7f6c9b4
> NAME                        READY   STATUS    RESTARTS   AGE
> checkout-58d7f6c9b4-4jx2p   0/1     Running   0          41m
> checkout-58d7f6c9b4-8kd9w   0/1     Running   0          41m
> checkout-58d7f6c9b4-cq7rt   0/1     Running   0          41m
> checkout-58d7f6c9b4-m2hz5   0/1     Running   0          41m
> checkout-58d7f6c9b4-w9lfn   0/1     Running   0          41m
> ```
>
> The checkout error rate looks normal. This release adds a call to a new `promo-engine` service in the `promotions` namespace. The developer says: "`curl promo-engine.promotions:8080/health` works fine from my laptop over the VPN."
>
> **Bonus (answer first, 1 min):** the Deployment uses the default rolling-update settings. Why is it stuck at exactly 5 new and 8 old, and not some other split?

---

## (f) Design: "Multi-tenant Kubernetes platform"

**Prompt (as an interviewer would say it):**

> About 60 product teams each run their own Kubernetes cluster today: roughly 80 clusters, most at 10–20% utilisation, every one upgraded on a different schedule. Design a shared, multi-tenant Kubernetes platform that teams onboard onto. One team must not be able to hurt another. 45 minutes.

**Rules:** draw on paper first, from blank, for 40 minutes (Friday). Then send me a photo or type it out, and I critique it against this checklist and the rubric in K-f. I don't draw it for you. Saturday: redraw from memory.

**Blank-page checklist (Real Apps Deserve Deep Failure Tests).** Your drawing must answer every line. These are questions, not answers.

**Requirements (5 min)**
- [ ] Who are the tenants: internal teams that trust each other somewhat, or untrusted code? What does that decide?
- [ ] Scale: tenants, workloads per tenant, clusters, regions, pods per cluster
- [ ] What "can't hurt each other" means, listed: CPU/memory, network, API server, secrets, cost, upgrades
- [ ] Platform SLOs: onboarding time, cluster availability, upgrade cadence

**API (5 min)**
- [ ] The tenant-facing interface: how does a team get a tenant, change its quota, add a member? (CLI, API, Git repo?)
- [ ] What a tenant can do on its own and what needs the platform team
- [ ] What the platform hands back: namespaces, credentials, endpoints, dashboards

**Data (5 min)**
- [ ] The source of truth for tenants: what record, which fields, stored where?
- [ ] How that record becomes cluster objects, and what happens when someone edits a cluster object by hand
- [ ] Usage and cost data: where it comes from, how it's attributed to a tenant

**Deep dive (15 min): pick ONE and go deep**
- [ ] The isolation model and its boundary: what exactly separates tenant A from tenant B at each layer (compute, network, API, node, kernel)?
- [ ] Noisy neighbours: what stops one tenant from eating a node, a cluster, or the API server?
- [ ] Upgrades across a shared fleet without breaking 60 teams

**Failures (5 min)**
- [ ] One tenant's workload or autoscaler eats all spare capacity
- [ ] One tenant installs something cluster-wide that breaks everyone (a webhook, a CRD, a controller)
- [ ] A tenant's controller floods the API server
- [ ] A node, a zone, a whole cluster goes down: how many tenants are hit?
- [ ] A tenant's credentials leak
- [ ] A Kubernetes upgrade removes an API a tenant still uses

**Tradeoffs (5 min)**
- [ ] Namespace per tenant vs virtual cluster vs cluster per tenant
- [ ] Few big clusters vs many small ones
- [ ] Self-service vs guardrails; hard quotas vs overcommit
- [ ] What changes at 10× the tenants

**Numbers that must appear on your page:** tenants per cluster · nodes and pods per cluster (vs Kubernetes' documented limits) · per-tenant quota (CPU, memory, pods) · target cluster utilisation · onboarding time · % of tenants hit by one cluster outage · upgrade cadence.

---

## (g) Flashcards (10 new cards: put them in Anki; answers in K-g)

| # | Type | Front |
| --- | --- | --- |
| 1 | Explain | Scheduler vs kubelet: who decides what? |
| 2 | Explain | Liveness, readiness and startup probe failures: what happens for each? |
| 3 | Explain | The three QoS classes and the rule for each. |
| 4 | Explain | Why can a container be OOMKilled while its node has free memory? |
| 5 | Explain | The HPA formula, and why a CPU-percentage HPA needs requests. |
| 6 | Explain | What does KEDA add on top of the HPA? |
| 7 | Command | A pod keeps restarting and its current logs look clean. How do you find out why the last container died? |
| 8 | Command | A rollout has stopped progressing. Check it, see both ReplicaSets, and roll it back. |
| 9 | Template | Write W4-T1 (heap with a custom comparator + lazy deletion) from memory. |
| 10 | Template | Write W4-T2 (multiset idioms) from memory. |

---

## (h) Cheat sheet skeleton (Thursday: fill it from memory; Sunday: rewrite it from blank)

File: `cheat_sheets/week04_kubernetes.md`. Fill it with this pack closed. Then compare with **K-h** and count matches (target ≥ 80%).

---

## (i) Review-due table (template)

Dates assume every redo is **Clean** and that the first try happens on its planned day. **Shaky** → same stage again in 2 days. **Failed** → back to Review 1 tomorrow. Rewrite the row's dates when that happens. Reviews 5 and 6 fall after the plan ends (Dec 20). Keep them anyway.

### Problems

| # | First try | Mark | R1 (+1) | Mark | R2 (+3) | Mark | R3 (+7) | Mark | R4 (+14) | Mark | R5 (+30) | R6 (+60) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1834 | Mon Nov 9 | | Tue Nov 10 | | Fri Nov 13 | | Fri Nov 20 | | Fri Dec 4 | | Sun Jan 3 | Thu Mar 4 |
| 630 | Tue Nov 10 | | Wed Nov 11 | | Sat Nov 14 | | Sat Nov 21 | | Sat Dec 5 | | Mon Jan 4 | Fri Mar 5 |
| 295 | Tue Nov 10 | | Wed Nov 11 | | Sat Nov 14 | | Sat Nov 21 | | Sat Dec 5 | | Mon Jan 4 | Fri Mar 5 |
| 220 | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| 355 | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| 215\* | Thu Nov 12 | | Fri Nov 13 | | Mon Nov 16 | | Mon Nov 23 | | Mon Dec 7 | | Wed Jan 6 | Sun Mar 7 |
| 56\* | Thu Nov 12 | | Fri Nov 13 | | Mon Nov 16 | | Mon Nov 23 | | Mon Dec 7 | | Wed Jan 6 | Sun Mar 7 |
| 253 | Thu Nov 12 | | Fri Nov 13 | | Mon Nov 16 | | Mon Nov 23 | | Mon Dec 7 | | Wed Jan 6 | Sun Mar 7 |
| 1882 | Fri Nov 13 | | Sat Nov 14 | | Tue Nov 17 | | Tue Nov 24 | | Tue Dec 8 | | Thu Jan 7 | Mon Mar 8 |
| Mock problem | Sat Nov 14 | | Sun Nov 15 | | Wed Nov 18 | | Wed Nov 25 | | Wed Dec 9 | | Fri Jan 8 | Tue Mar 9 |
| W4-T1/T2 (only if failed) | Mon Nov 9 | | Tue Nov 10 | | Fri Nov 13 | | Fri Nov 20 | | | | | |

\* For a redo of an old solve, the "First try" column is the first redo; mark it Clean / Shaky / Failed.

### Concepts (cards, labs, teach-backs, drills, design)

Same 1-3-7-14-30-60 spacing, counted from the first attempt. Mark each Clean / Shaky / Failed when it comes due: a card is Clean if answered word-perfect in under 30 s, a teach-back if ≤ 5 stumbles, a drill if it scores ≥ 3 on the routine, the design if it hits every checklist line from memory.

| Item | First | Mark | +1 | Mark | +3 | Mark | +7 | Mark | +14 | Mark | +30 | +60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cards 1–10 | Sat Nov 14 | | Sun Nov 15 | | Wed Nov 18 | | Wed Nov 25 | | Wed Dec 9 | | Fri Jan 8 | Tue Mar 9 |
| Lab 1–2 (redo the predictions from memory) | Tue Nov 10 | | Wed Nov 11 | | Sat Nov 14 | | Sat Nov 21 | | Sat Dec 5 | | Mon Jan 4 | Fri Mar 5 |
| Lab 3–4 (same) | Thu Nov 12 | | Fri Nov 13 | | Mon Nov 16 | | Mon Nov 23 | | Mon Dec 7 | | Wed Jan 6 | Sun Mar 7 |
| T1 scheduler vs kubelet | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| T2 requests/limits/QoS | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| T3 OOMKilled with free memory | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| Drill 1 CrashLoopBackOff | Wed Nov 11 | | Thu Nov 12 | | Sun Nov 15 | | Sun Nov 22 | | Sun Dec 6 | | Tue Jan 5 | Sat Mar 6 |
| Drill 2 OOM, free node memory | Fri Nov 13 | | Sat Nov 14 | | Tue Nov 17 | | Tue Nov 24 | | Tue Dec 8 | | Thu Jan 7 | Mon Mar 8 |
| Drill 3 stuck rollout | Sat Nov 14 | | Sun Nov 15 | | Wed Nov 18 | | Wed Nov 25 | | Wed Dec 9 | | Fri Jan 8 | Tue Mar 9 |
| Design: multi-tenant platform | Fri Nov 13 | | Sat Nov 14 (redraw) | | Tue Nov 17 | | Tue Nov 24 | | Tue Dec 8 | | Thu Jan 7 | Mon Mar 8 |
| Story: fleet upgrade | Thu Nov 12 | | Fri Nov 13 | | Mon Nov 16 | | Mon Nov 23 | | Mon Dec 7 | | Wed Jan 6 | Sun Mar 7 |

Concept reviews take 2–5 minutes each and don't count toward the 5-problem cap. Do them in the recall warm-up slot.

---

## (j) Saturday mock: full loop, 75 minutes, recorded

Mix: about 70% Week 4, 30% Weeks 1–3. I'm the interviewer and run it from the sealed sheet in K-j. You don't read K-j.

| Time | Block | Content |
| --- | --- | --- |
| 0–5 | Intro | Your 90-second intro (Week 1 story) |
| 5–40 | Coding | One unseen Week 4 Hard. 60-second approach, brute force first, run it on your own tests |
| 40–55 | Design | A 15-minute Week 4 design question |
| 55–70 | Troubleshooting | One scenario mixing Kubernetes with Weeks 1–3 (Linux, networking, containers) |
| 70–75 | Your questions | Two questions you'd ask a real interviewer |

### Scorecard (1–4 per area, with evidence)

| Area | Score | Evidence (timestamp + what happened) |
| --- | --- | --- |
| Approach | | |
| Working code | | |
| Fluency | | |
| Testing | | |
| Communication | | |
| Design depth | | |
| Troubleshooting | | |
| Composure | | |
| **Average** | | Gate 2 needs ≥ 3.0 |

### Debrief template (within an hour of the mock)

1. Where did I stall first, at what minute, and for how long?
2. What did I know but fail to say?
3. What did I not know at all?
4. Which routine step did I skip (coding, design or troubleshooting)?
5. One drill per stall, with a date.

### Mock error-log table

| Problem | Mark (Clean / Shaky / Failed) | Miss type (recall / pattern / edge case / syntax / routine step skipped / communication / time) | Fix (the drill, and when) |
| --- | --- | --- | --- |
| | | | |
| | | | |

Copy every row into `error_log.md` in its standard format (Date | Problem or topic | What went wrong | Root cause | Rep 1 | Rep 2 | Rep 3).

---

## (k) Story: Kubernetes fleet upgrade

**Rule:** only facts you supply. Every blank stays blank until you fill it. I won't suggest numbers.

**Facts I need from you first** (answer in a message, or write them here):
- Which company and year? Which Kubernetes distribution (EKS, GKE, AKS, self-managed)? From which version to which?
- How many clusters and nodes, and what ran on them?
- Why the upgrade was needed (end of support, a CVE, a feature, a removed API)?
- What was your role, and who else was involved?
- What went wrong, or nearly did?

**Structure (2 minutes spoken, then stop):**

| Beat | ~Time | Your words |
| --- | --- | --- |
| **Situation**: the fleet, the versions, the deadline | 20 s | |
| **Stakes**: what breaks, for whom, if it goes wrong or doesn't happen | 15 s | |
| **My actions**: 3 decisions you made yourself, each with the option you rejected | 50 s | 1. <br>2. <br>3. |
| **Measurable result**: one or two numbers (duration, downtime, incidents, clusters done) | 15 s | |
| **What I'd do differently**: one specific change | 20 s | |

**Interviewer probes (practise answering each in ≤ 30 s):**
1. Why couldn't you just skip versions and go straight to the target?
2. How did you find workloads using APIs that the new version removes?
3. What order did you upgrade components in, and why that order?
4. What was your rollback plan, and could you actually roll back the control plane?
5. A drain hung on one node. What did you do?
6. How did you know each cluster was healthy before moving to the next?
7. How did you communicate with the teams running on the clusters?
8. What would you automate if you had to do this every quarter?
9. What went wrong, and what did you change because of it?
10. If you had half the time, what would you cut?

---
---

# ANSWER KEY

Do not read a section here until you've attempted its matching section above.

---

## K-a. Warm-up answers

1. API server (validates, stores in etcd) → Deployment controller creates a ReplicaSet → ReplicaSet controller creates Pods → **scheduler** binds each Pod to a node (sets `spec.nodeName`) → that node's **kubelet** sees it → container runtime (via CRI) creates the sandbox, CNI gives it an IP, volumes mount, images pull, init containers run, then app containers start.
2. The scheduler. It compares the pod's **requests** with each node's **allocatable** minus what's already requested, plus taints/tolerations, node selectors and affinity. It doesn't look at actual usage by default.
3. Both are the kubelet. Liveness: it kills the container and restarts it per `restartPolicy`. Readiness: the pod is marked not Ready and taken out of Service endpoints; nothing is restarted, and probing continues.
4. CPU over limit → **throttled** (CFS quota), never killed. Memory over limit → the kernel **OOM-kills** it (exit 137, reason `OOMKilled`).
5. **Guaranteed:** every container has CPU and memory limits, and requests equal to limits. **BestEffort:** no container has any request or limit. **Burstable:** everything else (at least one request or limit somewhere).
6. A container keeps exiting and the kubelet is waiting before the next restart. It's a container **waiting reason**, not a phase (the phase usually stays `Running`). Backoff: 10 s, doubling each time, capped at 5 min, reset after the container runs 10 min without trouble. Newer releases are changing these numbers behind feature gates; check yours.
7. `desired = ceil(current × currentMetric / target)` = ceil(3 × 90 / 50) = ceil(5.4) = **6**.
8. PID 1 ignores SIGTERM (shell-form `CMD`, or a script that doesn't `exec`), so the kubelet waits out `terminationGracePeriodSeconds` (default **30**), then sends SIGKILL → 137.
9. kube-proxy's iptables/IPVS NAT for Service traffic: every connection through a ClusterIP or NodePort gets a conntrack entry (DNS over UDP adds a lot). When the table is full, the kernel logs `nf_conntrack: table full, dropping packet` and new connections drop silently: timeouts, SYN retries.
10. It kills the process with the highest `oom_score`, which is roughly its share of memory adjusted by `/proc/<pid>/oom_score_adj` (−1000 to 1000; −1000 = never kill).

---

## K-b. Reading notes (short on purpose)

**Pod lifecycle**
- Phases: **Pending, Running, Succeeded, Failed, Unknown**. `CrashLoopBackOff`, `ImagePullBackOff` and `ContainerCreating` are container *waiting reasons*, not phases.
- Container states: **Waiting, Running, Terminated**. `lastState.terminated` holds the previous exit (reason + exit code).
- `restartPolicy`: Always (default), OnFailure, Never. Deployments only allow **Always**.
- A pod is scheduled **once**. It's never moved; it's deleted and a controller makes a new one.
- Delete flow: pod gets a deletion timestamp → endpoint controllers drop it from Services **at the same time** as the kubelet starts shutdown → `preStop` hook → SIGTERM → wait up to `terminationGracePeriodSeconds` (30 s, which includes the preStop time) → SIGKILL. The race between those two is why people add a short `preStop` sleep.
- Probes: exec, httpGet (200–399 = success), tcpSocket, grpc. Defaults: `periodSeconds 10`, `timeoutSeconds 1`, `failureThreshold 3`, `successThreshold 1`, `initialDelaySeconds 0`.
- A startup probe disables liveness and readiness until it succeeds. If it fails `failureThreshold × periodSeconds`, the container is killed.
- Native sidecars: an init container with `restartPolicy: Always` keeps running alongside the app (on by default since 1.29).

**Resource management**
- CPU in cores (`250m` = a quarter core). Memory in bytes: `128Mi` = 128 × 2²⁰, `128M` = 128 × 10⁶, and `128m` = 0.128 **bytes** (a classic typo).
- Limit set, request not set → request **defaults to the limit**.
- Requests → scheduling and CPU weight. Limits → enforced by the kernel's cgroups: CPU via CFS quota (`cpu.max`), memory via `memory.max` and the OOM killer.
- Node **allocatable** = capacity minus system/kube reservations minus the eviction threshold.
- Node-pressure eviction (kubelet): default hard threshold `memory.available<100Mi` on Linux. Ranking: pods using more than their request go first, then by priority, then by how far over their request they are.

**Debug Pods**
- Pending → `kubectl describe pod` → Events (`FailedScheduling`: insufficient CPU, taints, affinity, unbound PVC).
- Waiting → `describe` (image name, pull secret, registry reachability).
- Crashing → `kubectl logs <pod> --previous` + `lastState` exit code.
- Running but wrong → compare the live spec with what you meant (`kubectl get pod -o yaml`); typos in field names can be silently dropped.
- `kubectl debug -it <pod> --image=busybox:1.36 --target=<container>`: an ephemeral container that shares the target's process namespace (for distroless images).
- `kubectl debug <pod> -it --copy-to=<new> --container=<c> -- sh`: a copy with a changed command, for a pod that crashes too fast to exec into.
- `kubectl debug node/<node> -it --image=busybox:1.36`: a pod on the node with the host filesystem at `/host`.

**HPA**
- `desired = ceil(current × current/target)`. Runs every **15 s**. Tolerance **10%** (no change if the ratio is within 0.9–1.1).
- CPU utilisation is a percentage **of the request**. No request → the HPA can't compute it.
- Defaults: scale-up has no stabilisation (it can add the larger of 100% or 4 pods every 15 s); scale-down waits for a **300 s** stabilisation window. Tunable via `spec.behavior`.
- Several metrics → it computes each and takes the **largest** replica count.
- Metric APIs: `metrics.k8s.io` (resource metrics, served by **metrics-server**), `custom.metrics.k8s.io` and `external.metrics.k8s.io` (served by adapters such as Prometheus Adapter or KEDA).
- Minimum is 1 replica unless the alpha `HPAScaleToZero` feature gate is on.

**KEDA**
- Adds **event sources** (60+ scalers: Kafka, SQS, Prometheus, cron, …) and **scale to zero**.
- Parts: the operator (activates 0 ↔ 1 and creates/owns an HPA), a metrics adapter (serves external metrics to that HPA), and admission webhooks.
- `ScaledObject` scales a Deployment/StatefulSet (anything with `/scale`); `ScaledJob` launches Jobs per batch of events (good for long-running work you don't want killed by scale-down).
- KEDA does 0 ↔ 1; the HPA it creates does 1 ↔ N. Defaults: `pollingInterval` 30 s, `cooldownPeriod` 300 s (only applies to scaling back to 0), `minReplicaCount` 0.

---

## K-b2. Teach-back outlines and follow-up answers

### T1: Scheduler vs kubelet (2 minutes, 6 beats)

1. **One line:** the scheduler decides *where*; the kubelet makes it *happen* and keeps it alive. Neither calls the other: both watch the API server.
2. **Scheduler:** watches pods with no `nodeName` → **filter** (requests fit allocatable, taints/tolerations, selectors/affinity, host ports, volume zone) → **score** (spreading, balanced use, image locality) → **bind** (writes `nodeName`). Uses requests, not usage. Starts nothing.
3. **Kubelet:** one per node → sees pods bound to it → admits → CRI: sandbox, CNI, volumes, image pull, init containers, app containers → runs probes → restarts per policy → reports status → evicts under node pressure.
4. **Nobody moves pods:** a dead node is tainted by the node lifecycle controller; pods are evicted after `tolerationSeconds` (300 s default); the ReplicaSet makes new pods; the scheduler places them.
5. **Debug mapping:** `Pending` = scheduler. Anything after binding (`ContainerCreating`, crash loops, OOM, probe failures) = kubelet and the node.
6. **Your example** (from your own work, or leave it out).

Follow-ups:
1. The scheduler's problem. `kubectl describe pod` → `FailedScheduling`, e.g. `0/3 nodes are available: 3 Insufficient cpu`. Then: requests too large, taints without tolerations, affinity nobody satisfies, PVC in another zone, cluster autoscaler at its max.
2. No: sum of requests vs allocatable. A node can be 95% busy and still "fit" a pod. That's why honest requests matter.
3. Nobody "moves" them. After about 5 min (default `tolerationSeconds: 300` for `not-ready`/`unreachable`) they're evicted and the controllers make replacements. StatefulSet pods on an unreachable node aren't replaced until the old pod is confirmed gone (or force-deleted), to avoid two copies.
4. Set `spec.nodeName` yourself (bypasses the scheduler), or a **static pod** (the kubelet reads manifests from a directory, which is how kubeadm runs the control plane). DaemonSet pods do go through the default scheduler.
5. The kubelet/node: image pull, volume attach/mount (CSI), CNI not handing out an IP. `describe` events tell you which.

### T2: Requests vs limits and QoS (2 minutes, 6 beats)

1. **Request** = a reservation: the scheduler uses it, and it sets CPU weight. **Limit** = a ceiling the kernel enforces.
2. CPU is compressible → over the limit you're **throttled**. Memory isn't → over the limit you're **killed**.
3. QoS is **derived**, not set: Guaranteed (requests = limits for CPU and memory, every container), BestEffort (nothing set), Burstable (the rest).
4. Why it matters: under node pressure it shapes who's evicted first and each container's `oom_score_adj` (Guaranteed −997, BestEffort 1000, Burstable in between, scaled by memory request).
5. Practice: memory request = limit; CPU request always; CPU limit is a tradeoff; enforce with LimitRange defaults and ResourceQuota.
6. **Your example** (a number from your fleet, or leave it out).

Follow-ups:
1. Tradeoff, say both sides: CPU limits give predictability and stop one pod hogging a node, but throttle even when the node is idle (latency spikes). A common default: CPU requests on everything, CPU limits only where you need Guaranteed or strict isolation.
2. The kubelet evicts pods using more than their request first, then by priority, then by how far over. BestEffort is usually first because its request is 0. Eviction ≠ OOM kill: evicted pods show `Evicted` with "The node was low on resource: memory" and are replaced. An OOM kill is the kernel, restarts the container in place, and says `OOMKilled`.
3. Requests default to the limits. If every container sets both CPU and memory limits, the pod is **Guaranteed**; otherwise Burstable.
4. A LimitRange gives defaults (and min/max) per container. A ResourceQuota on `requests.cpu`/`requests.memory` makes the API server **reject** pods without requests in that namespace. Policy engines (Kyverno, Gatekeeper, built-in ValidatingAdmissionPolicy) can enforce it too.
5. CFS throttling: the quota is spent within each 100 ms period by bursts (many threads), so the container waits out the rest of the period even though average usage is low. Check `nr_throttled`/`throttled_usec` in `cpu.stat`, or the `container_cpu_cfs_throttled_periods_total` metric.

### T3: OOMKilled with free node memory (2 minutes, 6 beats)

1. OOM is per **cgroup**. The container's limit is `memory.max`; hit it and the kernel's memory-cgroup OOM killer kills a process **inside that cgroup**. Exit 137, `OOMKilled`. The node's free memory never comes into it.
2. What counts toward the limit: anonymous memory (heap, stacks, native buffers), page cache charged to the cgroup (clean cache is reclaimed first; tmpfs and `emptyDir: {medium: Memory}` can't be dropped).
3. Why the graphs lie: `kubectl top` shows the working set, sampled every ~15 s by default, so a spike between samples is invisible. The heap panel shows only the heap.
4. Three different killers: **container OOM** (kernel, this cgroup), **node-pressure eviction** (kubelet, `Evicted`), **system OOM** (kernel, whole node, picks by `oom_score_adj`).
5. Confirm: `lastState.terminated.reason`; on the node, `dmesg` shows `Memory cgroup out of memory: Killed process …` (get there with `kubectl debug node/…`).
6. Fix and prevent: size the limit from p99 usage plus headroom; size runtimes to the limit (JVM `-XX:MaxRAMPercentage`, cap direct memory); alert when working set > 90% of the limit.

Follow-ups:
1. OOM: `lastState.terminated.reason: OOMKilled`, exit 137, same pod restarts. Eviction: pod `status.reason: Evicted`, phase Failed, a new pod replaces it. Liveness: Events say "failed liveness probe, will be restarted"; exit code is 137 or 143, or 0 if the app exits cleanly on SIGTERM.
2. `-Xmx` caps only the heap. Metaspace, thread stacks, code cache, GC structures and direct/NIO buffers sit on top, so the process goes over 1 GiB. Leave headroom: heap around 60–75% of the limit.
3. Sampling (spikes between scrapes) and what's measured (working set, not peak). A burst of allocations can go from 742Mi to 1Gi in under a second.
4. Yes, it's charged to the cgroup. The kernel reclaims clean cache before OOM-killing, so it usually isn't the cause. Dirty pages under heavy writes and tmpfs/memory-backed `emptyDir` can be.
5. Kernel log on that node: `dmesg -T | grep -i "out of memory"`, via `kubectl debug node/<n> -it --image=busybox:1.36` then `chroot /host`, or SSH.

---

## K-c. Lab: expected observations

Timings are approximate. Exact message wording varies a little by Kubernetes version.

**Step 0.** 4 nodes, all `Ready` within 1–2 min: `w4-control-plane` (role `control-plane`) and `w4-worker`, `w4-worker2`, `w4-worker3`. Your pods won't land on the control plane: it has the taint `node-role.kubernetes.io/control-plane:NoSchedule`.

**1a.** Within ~5 s: READY `0/1`, RESTARTS stays `0`. Event: `Readiness probe failed: HTTP probe failed with statuscode: 403` (nginx returns 403 for `/` with no index file). That endpoint shows `ready=false`. It stays that way forever, because readiness never restarts anything. After you restore the file it's back in ~5 s (`periodSeconds: 5`). **Proves:** readiness controls traffic, not lifecycle.

**1b.** About 20–30 s after the `rm` (3 failures × 10 s; the first may land at any point in a period): `Liveness probe failed: HTTP probe failed with statuscode: 404`, then `Container web failed liveness probe, will be restarted`. RESTARTS → 1. **Same pod name, same IP, same node.** `50x.html` is back: a restarted container starts from the image again, and writes to its own filesystem are lost. **Proves:** liveness restarts the *container* in place; the pod is not replaced.

**1c.** (i) The rollout **finishes**: new pods pass readiness, and liveness doesn't gate a rollout. (ii) Restarts every ~30 s at first, then STATUS shows `CrashLoopBackOff` between restarts as the backoff grows (10 s, 20 s, 40 s, …). (iii) You'll most likely see **exit code 0, reason `Completed`**: nginx shuts down cleanly on the kubelet's SIGTERM. You'd only see 137 if the process ignored SIGTERM for the whole grace period. **Proves:** an exit code alone can't tell you it was a liveness kill. Events can.

**1d.** The new pod stays `0/1` (readiness doesn't run until the startup probe passes). First restart ~20 s after start (4 × 5 s). The rollout **does not** finish: with 2 replicas, `maxUnavailable` 25% rounds down to 0, so the old pods stay until a new one is Ready.

**2a.** It prints 10, 20, … and dies around **80 or 90 MiB** (Python itself takes several MiB of the 100 MiB). STATUS: `OOMKilled` → `Running` → `OOMKilled` → `CrashLoopBackOff`, with gaps of about 10 s, 20 s, 40 s, 80 s… `lastState`: `"exitCode":137,"reason":"OOMKilled"`.

**2b.** `free -m` on the node shows gigabytes free (it's the VM's memory). Allocated memory requests are small. **Proves:** the kill came from the container's own cgroup limit, not from node memory.

**2c.** `memory.max` = `67108864` (64 × 1024 × 1024). `cpu.max` = `10000 100000`: 10 ms of CPU per 100 ms period = 100m.

**2d.**
- `qos-a`: BestEffort, `1000`.
- `qos-b`: Burstable, `1000 − (1000 × request ÷ node memory capacity)`, rounded the kernel's way. With a 64Mi request on an ~8 GiB node that's about **992–993**. Use your node's exact capacity.
- `qos-c`: Guaranteed, `-997`.

**Proves:** if the whole node runs out, the kernel kills BestEffort first and Guaranteed last.

**3a.** **Fails.** It still **cordons** the node first (`Ready,SchedulingDisabled`), then refuses, listing both problems: DaemonSet-managed pods (`kindnet-…`, `kube-proxy-…`; "use --ignore-daemonsets") and a pod with no controller (`default/lonely`; "use --force"). The node stays cordoned even though the drain failed.

**3b.** `lonely` is deleted with a warning about pods that declare no controller; it's gone for good, because nothing recreates it. Each web pod eviction is refused: `Cannot evict pod as it would violate the pod's disruption budget`, retried every ~5 s, until the 60 s timeout fails the drain. No web pod leaves the node.

**3c.** Evictions happen **one at a time**: evict → old pod Terminating → replacement created **with a new name and a new IP on another node** → becomes Ready → the PDB allows the next eviction. `kubectl get pdb` shows ALLOWED DISRUPTIONS going 1 → 0 → 1. `kubectl get pod lonely` → `NotFound`.

**3d.** Nothing moves back. Kubernetes doesn't rebalance running pods; only new pods can land on the node (a descheduler can rebalance if you want that). **Proves:** pods are replaced, not moved. A PDB limits *voluntary* disruptions (drains, evictions); it does nothing against a node crash.

**4b.** TARGETS `<unknown>/50%` (newer kubectl: `cpu: <unknown>/50%`). `describe hpa`: condition `ScalingActive False`, reason `FailedGetResourceMetric`, message containing `missing request for cpu`.

**4c.** After ~1 min, TARGETS shows a small number (0–5%).

**4d.** One pod's utilisation can't go above **500%**: the 500m limit ÷ 100m request. It jumps toward that within 30–90 s. Replicas step up (the default allows doubling, or +4 pods, every 15 s), then per-pod utilisation falls as the single load loop spreads across pods. Replicas settle where total CPU ÷ (replicas × 100m) is about 50% (within the 10% tolerance), capped at 6. Your formula column should match each step.

**4e.** No scale-down for about **5 minutes** (the default 300 s stabilisation window), then a drop toward 1.

**4f.** A strong answer contains:
- `scaleTargetRef: cpu-app`; `minReplicaCount: 0`; `maxReplicaCount: 20`.
- A trigger (e.g. `aws-sqs-queue` or `rabbitmq` or `kafka`) with a target per replica (queue length / lag per pod) and an `activationThreshold` (the level that wakes it from 0).
- A `TriggerAuthentication` for credentials.
- Tune first: the per-replica target, and `cooldownPeriod` (how long at zero-demand before scaling back to 0). Also mention `pollingInterval` and that scale-to-zero adds cold-start latency.

---

## K-d0. Template drill: how it's graded (no reference code, by design)

You pass on your own file: compiles with zero warnings, every assert passes, under 15:00. Check your file against these common slips after the timer stops:

- `priority_queue<T, vector<T>, greater<T>>` is a **min**-heap. The comparator answers "does `a` go *below* `b`?", which is backwards from `sort`.
- A lambda comparator needs `decltype(cmp)` in the type **and** `cmp` passed to the constructor. In C++17, lambdas aren't default-constructible (C++20 relaxes this for capture-less ones).
- Lazy deletion: the "clean the top" loop must run before every `top()`, not only after `pop()`. The size you report must exclude marked items.
- `ms.erase(x)` removes **every** copy; `ms.erase(ms.find(x))` removes one, and `find` returning `end()` must be checked first.
- Largest ≤ x: `upper_bound(x)` then `prev`. Guard the `begin()` case: `prev(begin())` is undefined behaviour.
- Max in O(1): `*prev(ms.end())` or `*ms.rbegin()`, only when not empty.

---

## K-d. Hint ladders (one rung at a time, only after 25 minutes stuck)

**215 Kth Largest**
1. You don't need everything sorted, only the boundary of the top k.
2. A min-heap holding exactly k items: its top is the k-th largest so far, and anything smaller than the top can't be in the top k. O(n log k). Quickselect is O(n) on average but O(n²) worst case, and LeetCode's tests punish a fixed pivot and long runs of duplicates: random pivot plus a three-way partition.
3. Heap: push each value; if the size passes k, pop; the answer is the top. Quickselect: target position n − k in ascending order; partition around a random pivot into less / equal / greater; recurse only into the part that holds the target.

**56 Merge Intervals**
1. Sort first. Then one pass.
2. After sorting by start, a new interval can only overlap the **last merged** one. Touching counts as overlapping (`[1,4]` and `[4,5]` → `[1,5]`). Extend the end with the **max** of the two ends, or a contained interval (`[1,10]`, `[2,3]`) shrinks it. Those two lines are where many-submit histories usually come from.
3. Sort by start → the result starts with the first interval → for each next one: if it overlaps the result's last, extend that end; otherwise append it.

**253 Meeting Rooms II**
1. Go through meetings in start order and track which rooms are in use.
2. The only room worth checking is the one that frees up **earliest**: a min-heap of end times. A room freed at t can host a meeting starting at t. (Sweep-line alternative: +1 at each start, −1 at each end, ends before starts at equal times; the answer is the peak.)
3. Sort by start → min-heap of end times → for each meeting: if the earliest end ≤ this start, pop it → push this end → the answer is the largest heap size.

**295 Median from Data Stream**
1. You only need the middle: split the numbers into a lower half and an upper half.
2. A max-heap for the lower half and a min-heap for the upper. Two invariants after every add: every lower value ≤ every upper value, and the sizes differ by at most one (pick which side holds the extra). Your last result here was WA: check the even-count median (integer division, or overflow from adding two ints).
3. Add: push to one side → move that side's top to the other (restores ordering) → if the sizes break your rule, move one top back. Find: odd count → the bigger side's top; even → the average of both tops, computed as a double.

**1834 Single-Threaded CPU**
1. Simulate the clock. At any moment only tasks with enqueue time ≤ now can be picked.
2. Sort task **indices** by enqueue time. Arrived tasks go in a min-heap keyed by (processing time, index). If the heap is empty, **jump** the clock to the next arrival instead of stepping. The clock can reach about 10¹⁴ (10⁵ tasks × 10⁹), so it needs `long long`.
3. Sorted indices + a pointer → loop until all n are done: if the heap is empty and the clock is behind the next arrival, jump → push every task that has arrived → pop one, advance the clock by its processing time, record its index.

**630 Course Schedule III**
1. Visit courses in deadline order, keeping a running total of time used.
2. Always take the current course. If the total passes its deadline, drop the **longest** course taken so far (it may be this one). Dropping any one course gives the same count, and dropping the longest frees the most time, so it's never worse (exchange argument; say it aloud). Max-heap of durations.
3. Sort by deadline → for each course: add its duration to the total and the heap → if the total is past this deadline, subtract the heap's max and pop it → the answer is the heap's size.

**220 Contains Duplicate III**
1. For index i, only the last `indexDiff` values matter: a sliding window of values. You need "the closest value to x in the window", fast.
2. An ordered set: `lower_bound(x − valueDiff)` is the smallest window value ≥ x − valueDiff; it's a match if it exists and is ≤ x + valueDiff. Do the ± in `long long`. (O(n) alternative: buckets of width valueDiff + 1, where only the same and adjacent buckets can match.)
3. For each i: query the window → match? return true → insert a[i] → if the window holds more than `indexDiff` values, erase a[i − indexDiff] (one copy) → after the loop, return false.

**355 Design Twitter**
1. Give every tweet a global, increasing timestamp. Keep each user's tweets in posting order.
2. The feed = the 10 newest across self + followees = a merge of sorted lists, newest first. Seed a max-heap with each user's newest tweet; pop, then push that user's next-older tweet; stop at 10. O(F + 10 log F) per feed.
3. Maps: user → list of (time, tweet id); user → set of followees. Post appends. Follow inserts (ignore following yourself); unfollow erases. Feed: seed the heap with the last index of each non-empty list (self included) → pop up to 10, pushing index − 1 while it's ≥ 0. Traps: unfollowing yourself, users who've never posted. Follow-up to say aloud: fan-out on write vs on read, and the hybrid for celebrities.

**1882 (sealed: read only after Friday's check)**
<details><summary>Open after the check</summary>

Pattern: two heaps, a free pool and a busy pool, plus a clock that jumps (the same loop as 1834, with a second heap).
1. Servers are either free or busy; task j becomes available at second j.
2. Free servers in a min-heap by (weight, index); busy ones in a min-heap by (time free, weight, index). Before assigning, move every busy server whose free time ≤ now back to the free heap. If no server is free, jump the clock to the earliest free time. Times need `long long`.
3. For each task j: clock = max(clock, j) → release finished servers → if none free, clock = earliest free time and release again → take the best free server, assign it, push it busy until clock + duration.
</details>

---

## K-e. Troubleshooting: interviewer sheets and scoring

**Scoring per drill (out of 6, then mapped to the 1–4 Troubleshooting score):** 1 point per routine step done fully. 6 = 4, 5 = 3, 3–4 = 2, ≤ 2 = 1. A step counts only if you **said** it. In the Week 2 drills, F1, F2, F4, F6 and F7 all skipped Check and Fix, so those two steps get looked at first in the debrief.

### Drill 1: CrashLoopBackOff

**Hidden cause:** the liveness probe kills the container before startup finishes. Migrations take ~4 minutes on staging's data; liveness is `httpGet /healthz`, `initialDelaySeconds: 30`, `periodSeconds: 10`, `failureThreshold: 3`, so it's killed ~50–60 s in. Exit 143 = the JVM exited on SIGTERM. Each restart reruns migrations from where they stopped. No startup probe.

**Reveal only when asked:**

| They ask about… | Reveal |
| --- | --- |
| Events | `Liveness probe failed: Get "http://10.244.1.17:8080/healthz": dial tcp 10.244.1.17:8080: connect: connection refused` ×3, then `Container orders-api failed liveness probe, will be restarted` |
| Probe config | Liveness as above; readiness on `/ready`; no startup probe |
| How long startup takes | ~4 min on the laptop with a small DB; staging's DB is larger |
| What changed | Migrations at startup are new in v2.14.0 |
| Exit 143 | 128 + 15 = terminated by SIGTERM |
| OOM? | No: reason `Error`, not `OOMKilled`; memory well under limit |
| DB state | The migrations table shows partial progress; one later restart logs `waiting for migration lock` |

**Full marks look like:**
- **Clarify:** what changed (the release), staging or prod, what's crashing.
- **Scope:** all pods of this version, staging only.
- **Stabilise:** staging, but behave as if prod: `kubectl rollout undo`, or pause; check the migration lock isn't left held.
- **Hypothesise (ranked):** (1) liveness kills a slow start, because 143 means a SIGTERM and the logs stop mid-migration with no error; (2) app crash on config: unlikely (it would exit 1 with an error); (3) OOM: ruled out by reason and code.
- **Check:** `kubectl describe pod` Events; `kubectl get deploy orders-api -o yaml` → probe spec; time from the start log to the kill.
- **Fix-and-prevent:** add a `startupProbe` with `failureThreshold × periodSeconds` above worst-case startup (e.g. 30 × 10 s); move migrations out of app start (a Job or pre-deploy step) so a restart can't half-apply them; liveness checks only the process; alert on restart rate.

### Drill 2: OOMKilled with free node memory

**Hidden cause:** limit = request = 1Gi; the JVM has `-Xmx768m`. Off-heap: Netty direct buffers (no `MaxDirectMemorySize` set, so the default cap equals the heap max), ~400 threads at ~1 MiB stack each (committed less, but growing), metaspace ~140 MiB. At peak, direct buffers spike and RSS passes 1 GiB → the memory cgroup OOM killer fires. Node memory is irrelevant.

**Reveal only when asked:**

| They ask about… | Reveal |
| --- | --- |
| Limits / requests | memory 1Gi / 1Gi; CPU 1 / none |
| JVM flags | `-Xmx768m`, nothing else memory-related |
| Native Memory Tracking (if they ask to enable it) | heap 768 MiB reserved, ~610 committed at peak; threads 412; metaspace 142 MiB; "Other" (direct buffers) swings 40–260 MiB |
| Node `dmesg` | `Memory cgroup out of memory: Killed process 482113 (java) total-vm:… anon-rss:1046… ` |
| Working set at 15 s resolution | Climbs to ~1.0Gi in the last sample before each kill |
| Traffic | Kills line up with the 11:00–12:00 peak |
| Recent change | Netty client added two releases ago for a new upstream |

**Full marks look like:**
- **Clarify:** OOMKilled confirmed by `lastState`; how often; since when; what changed (the Netty client).
- **Scope:** all replicas, peak hours only.
- **Stabilise:** raise the memory limit temporarily (e.g. 1.5Gi) or add replicas to cut per-pod load; don't open a vendor ticket first.
- **Hypothesise:** (1) off-heap growth past the cgroup limit; (2) heap leak: ruled out by the heap panel; (3) a node-level problem: ruled out because the container limit is what fired.
- **Check:** `dmesg` on the node via `kubectl debug node/…`; NMT (`-XX:NativeMemoryTracking=summary`, then `jcmd <pid> VM.native_memory summary`); working set vs limit at fine resolution.
- **Fix-and-prevent:** cap direct memory (`-XX:MaxDirectMemorySize`), size the heap as a percentage (`-XX:MaxRAMPercentage`) with headroom, set the limit from measured p99 RSS; alert at working set > 90% of limit; load test at peak.

### Drill 3: deployment stuck at 50%

**Bonus answer:** defaults are `maxSurge: 25%` (rounds **up**: 3) and `maxUnavailable: 25%` (rounds **down**: 2) on 10 replicas. So at most 13 pods total and at least 8 available. The new ReplicaSet goes to 3, the old drops to 8, which lets the new one go to 5 (13 − 8). None of the 5 become Ready, so the old can't go below 8. Stuck at **5 new, 8 old**.

**Hidden cause:** v2's `/ready` checks the new `promo-engine` dependency. Namespace `shop` has a default-deny **egress** NetworkPolicy plus allow rules for DNS and `payments` only, so calls to `promotions` time out and readiness returns 503. The laptop works because the VPN path doesn't go through the cluster's network policy.

**Reveal only when asked:**

| They ask about… | Reveal |
| --- | --- |
| Pod events | `Readiness probe failed: HTTP probe failed with statuscode: 503` |
| App logs | `readiness: dependency promo-engine unhealthy: dial tcp 10.96.44.12:8080: i/o timeout` |
| Deployment conditions | `Progressing False ProgressDeadlineExceeded` (default `progressDeadlineSeconds: 600`) |
| NetworkPolicies in `shop` | `default-deny-egress`, `allow-dns`, `allow-payments-egress` |
| From inside a new pod (`kubectl exec … -- wget -T 3 promo-engine.promotions:8080/health`) | times out; DNS resolves fine |
| Capacity | 8 of 10 replicas serving, CPU at 70% at the current traffic level |

**Full marks look like:**
- **Clarify:** what changed (new dependency), is the customer impacted (no, but capacity is down to 8/10).
- **Scope:** only the new ReplicaSet; only the `shop` namespace.
- **Stabilise:** `kubectl rollout undo deploy/checkout` (or `rollout pause`) to get back to 10 serving pods before peak.
- **Hypothesise (ranked):** (1) readiness fails on a dependency → network policy or the dependency itself; (2) readiness path/port mismatch in the new image; (3) resource or scheduling: ruled out (pods are Running, 0 restarts).
- **Check:** pod Events (503 vs 404 tells (1) from (2)); app logs; `kubectl exec` a request from **inside** the pod; `kubectl get networkpolicy -n shop`.
- **Fix-and-prevent:** an egress rule from `shop` to `promotions` (and ingress on their side if they deny); readiness should check only what the pod needs to serve (degrade if `promo-engine` is down instead of going unready); alert on `ProgressDeadlineExceeded`; test network paths in a pre-prod namespace with the same policies; canary first.

---

## K-f. Design: facts and critique rubric (not a design)

I critique your drawing against the checklist in §f. These are the facts the critique checks for. A 4 uses most of them **unprompted**.

- **Namespaces are a soft boundary.** Tenants still share the kernel, the control plane, cluster-scoped objects (CRDs, webhooks, ClusterRoles, StorageClasses) and node resources. Say what that means for untrusted tenants.
- **The usual namespace-per-tenant set:** RBAC (Role/RoleBinding per namespace), ResourceQuota (total CPU, memory, pods and object counts per namespace), LimitRange (per-container defaults and min/max), NetworkPolicy with **default deny** (needs a CNI that enforces it), Pod Security Admission (`restricted` / `baseline` / `privileged`, set by namespace label).
- **Stronger isolation options,** in rough order of cost: dedicated node pools per tenant (taints/tolerations plus enforced selectors), sandboxed runtimes (gVisor, Kata), virtual clusters (a per-tenant control plane on shared nodes), and a cluster per tenant.
- **The API server is shared:** API Priority and Fairness limits how much any one client can take; a tenant's misbehaving controller is a known way to hurt everyone.
- **Admission control is where guardrails live:** built-in ValidatingAdmissionPolicy, Kyverno or Gatekeeper. A broken webhook with `failurePolicy: Fail` can block every deploy in the cluster, so platform-owned only, with timeouts.
- **PriorityClass and preemption** decide who loses when capacity runs out; the cluster autoscaler must have per-tenant limits or quota must cap it.
- **Kubernetes' documented scaling limits:** ≤ 5,000 nodes, ≤ 150,000 pods, ≤ 300,000 containers per cluster, ≤ 110 pods per node (default).
- **Cost:** per-namespace usage attributed by labels (OpenCost-style); showback before chargeback.
- **Upgrades:** version skew (kubelet up to three minor versions behind the API server since 1.28); deprecated-API scans before each upgrade; canary cluster first; PDBs make drains safe but can block them.
- **Blast radius math:** with N clusters and tenants spread evenly, one cluster outage hits ~1/N of tenants. Your page must show the number.

---

## K-g. Flashcard answers

1. The scheduler only picks a node: it filters and scores nodes on requests, taints and affinity, then writes `nodeName`. The kubelet on that node makes it real: it starts the containers through the runtime, runs probes, restarts, reports status and evicts under pressure.
2. Liveness failure: the kubelet kills and restarts the container. Readiness failure: the pod leaves Service endpoints, no restart. Startup probe: liveness and readiness are off until it passes, and if it never does, the container is killed.
3. Guaranteed: every container has CPU and memory requests equal to limits. BestEffort: no requests or limits anywhere. Burstable: everything else.
4. The limit is enforced per cgroup: when the container's own `memory.max` is hit, the kernel kills inside that cgroup regardless of node free memory. Off-heap memory, tmpfs, and spikes between metric samples are the usual reasons it's a surprise.
5. `desired = ceil(current × current/target)`, every 15 s, with a 10% tolerance. CPU percentage is measured against the **request**, so with no request there's nothing to divide by (`<unknown>`).
6. KEDA adds event-source triggers (queues, streams, Prometheus, cron) and scale to/from zero. It does 0 ↔ 1 itself and creates an HPA, fed by its metrics adapter, for 1 ↔ N.
7. `kubectl describe pod <p>` (Last State + Events) · `kubectl get pod <p> -o jsonpath='{.status.containerStatuses[*].lastState.terminated}'` · `kubectl logs <p> --previous`
8. `kubectl rollout status deploy/<d>` · `kubectl get rs -l app=<d>` · `kubectl describe deploy <d>` (Conditions) · `kubectl rollout undo deploy/<d>`
9. Your own Monday file, once it passes the §d0 asserts. Grade against K-d0.
10. Same.

---

## K-h. Reference cheat-sheet points (compare after writing yours; target ≥ 80% matching)

**Top five:**
1. The scheduler decides where (requests, taints, affinity); the kubelet makes it run and keeps it alive. Pods are replaced, never moved.
2. Requests reserve, limits enforce: CPU throttles, memory kills.
3. QoS is derived from requests and limits and decides who dies first under pressure.
4. Liveness restarts, readiness removes from traffic, startup protects slow starters. Never put dependencies in liveness.
5. The HPA scales on usage ÷ request every 15 s and waits 5 min to scale down; KEDA adds event sources and scale to zero by feeding an HPA.

**Commands:**

| I want to… | Command |
| --- | --- |
| See why a pod is Pending | `kubectl describe pod <p>` → Events |
| See why the last container died | `kubectl get pod <p> -o jsonpath='{.status.containerStatuses[*].lastState.terminated}'` |
| Read the crashed container's logs | `kubectl logs <p> --previous` |
| See events, newest last | `kubectl get events --sort-by=.lastTimestamp` |
| See a pod's QoS class | `kubectl get pod <p> -o jsonpath='{.status.qosClass}'` |
| Live CPU/memory per container | `kubectl top pod <p> --containers` |
| See what's requested on a node | `kubectl describe node <n>` → Allocated resources |
| Watch or undo a rollout | `kubectl rollout status deploy/<d>` · `kubectl rollout undo deploy/<d>` |
| Take a node out safely | `kubectl drain <n> --ignore-daemonsets --delete-emptydir-data` · `kubectl uncordon <n>` |
| See why the HPA isn't scaling | `kubectl describe hpa <h>` → Conditions and Events |
| Shell into a distroless pod | `kubectl debug -it <p> --image=busybox:1.36 --target=<c>` |
| Debug the node itself | `kubectl debug node/<n> -it --image=busybox:1.36` (host at `/host`) |

**Failure modes:**

| Symptom | Cause | First check |
| --- | --- | --- |
| Pending, `Insufficient cpu` | Requests don't fit any node | `describe pod`; `describe node` Allocated |
| CrashLoopBackOff, exit 1 | App fails at startup | `logs --previous` |
| CrashLoopBackOff, exit 143/137, logs stop mid-startup | Liveness kills a slow start | Events; add a startup probe |
| OOMKilled 137, node has free memory | The container's own memory limit | `lastState`; node `dmesg` |
| Running, 0/1, 0 restarts | Readiness failing | Events (status code) |
| ImagePullBackOff | Wrong image/tag, auth, registry unreachable | `describe pod` Events |
| Rollout stuck, `ProgressDeadlineExceeded` | New pods never Ready (or can't be created: quota) | `get rs`; new pods' Events |
| Drain hangs | A PDB allows 0 disruptions | `kubectl get pdb` |
| HPA `<unknown>` | No requests, or metrics-server down | `describe hpa` |
| Pod `Evicted`, "low on resource: memory" | Node-pressure eviction by the kubelet | `describe node` Conditions |
| Latency spikes, CPU under limit | CFS throttling | `cpu.stat` throttled counts |

**Bottom (questions only; the stories are yours):**
1. "Tell me about a large infrastructure upgrade you led." → fleet upgrade.
2. "How do you stop one team's workload from hurting another's?" → your story with a quota/isolation decision.
3. "Tell me about a production incident on your platform." → your choice.

---

## K-j. Mock interviewer sheet (for Claude on Saturday; don't read)

- **Coding (35 min):** 2402 Meeting Rooms III. If 2402 was opened during the week, use 1851. Score: approach in 60 s; brute-force idea stated; two heaps named; `long long` end times unprompted; ties by room id; traces example 1.
- **Design (15 min):** "A queue-consumer fleet processes uploads. Traffic is 0 overnight and 50k messages/min at peak. Design its autoscaling on Kubernetes." Look for: KEDA ScaledObject on queue lag, per-replica target computed from throughput per pod, scale to zero plus the cold-start cost, cooldown, max replicas bounded by downstream capacity and quota, scale-down interrupting in-flight work (graceful shutdown, `terminationGracePeriodSeconds`, or `ScaledJob`), what happens if the metrics source is down (KEDA `fallback`).
- **Troubleshooting (15 min, Weeks 1–3 heavy):** "After moving a service onto Kubernetes, about 1% of requests are exactly 5 s slower. Only outbound calls by hostname are affected." Hidden: a conntrack insert race when glibc sends A and AAAA queries in parallel from one UDP socket; one reply is dropped and the resolver waits its 5 s timeout. Reveal on request: `conntrack -S` shows `insert_failed` climbing; `ndots:5` in `/etc/resolv.conf` multiplies lookups; `tcpdump` on port 53 shows a query with no answer. Fixes: NodeLocal DNSCache, `single-request-reopen` in `dnsConfig` options (glibc only, not musl/Alpine), FQDNs with a trailing dot, or lower `ndots`.

---

## K-k. Story reference beats (coverage check only, not content)

A strong answer covers: why the upgrade couldn't wait; the order (control plane first, then node pools; one minor version at a time); how removed APIs were found before the upgrade (a scan of manifests and live objects); a canary cluster before the fleet; how drains were made safe (PDBs, surge capacity) and what happened when one blocked; how health was judged between steps; the rollback limit (control-plane downgrades aren't supported, so the rollback is "don't proceed"); one number; one lesson. Only your facts fill these.
