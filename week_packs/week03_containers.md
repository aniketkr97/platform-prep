# WEEK PACK — Week 3: Containers

Infra layer: image layers, layer caching, multi-stage builds, non-root, signals and PID 1 · Code: trees that return state (tree DP, rerooting) + a concurrency starter · Design: safely deploying a containerised service to a VM fleet · Story: vulnerability remediation at scale

**Rule for this file:** do every section cold first. Every answer, note, hint and reference is in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section. There is no LeetCode code anywhere in this file: those problems go through the hint ladder only, one rung at a time.

Lab starter files (the broken starting points only, no fixes): `week_packs/week03_lab/`.

---

## 0. This week's plan

### 0a. Dates

The plan put Week 3 on Oct 26 – Nov 1. This pack was made Sun Nov 1, so the day plan below runs **Mon Nov 2 – Sun Nov 8**. That pushes Week 4 to Nov 9. Gate 1 (planned Sat Oct 31) has no result logged, and it includes "fix 3 broken Dockerfiles in 20 minutes", which is this week's material. Suggested new date: **Sun Nov 8**. If you already did part of Week 3 last week, tell me and I'll recount.

**Also due:** error-log Rep 3 for F1–F8 (Week 2 networking drills) was due Nov 1. Do them Monday as a 15-minute spoken round before anything new. Three of them are in §a.

**Unknown backlog:** I have no redo results for the Week 1–2 problems (the tracker's review queue is blank). Tell me each result before Monday so I can count the >5 cap.

**Docker isn't installed on this Mac** (`docker: command not found`). Install it before Tuesday's lab (§c, step 0).

### 0b. This week's problems

| # | Problem | Diff | Role | Your history (LeetCode, Oct 6) | How it's run |
| --- | --- | --- | --- | --- | --- |
| 102 | Binary Tree Level Order Traversal | M | Core | Apr 2026, 1 submit | Cold redo, ≤ 25 min (aim 12) |
| 236 | Lowest Common Ancestor of a Binary Tree | M | Core | Jan 2026, **7 submits (shaky)** | Cold redo, ≤ 25 min, **first in its day** |
| 98 | Validate Binary Search Tree | M | Core | **Jan 2025**, 3 submits (fading) | Cold redo, ≤ 25 min |
| 124 | Binary Tree Maximum Path Sum | H | Core | Jun 2026, **9 submits (shaky)** | Cold redo, ≤ 25 min |
| 1114 | Print in Order | E | Core (concurrency starter) | Mar 2026, 1 submit | Cold redo, ≤ 15 min |
| 337 | House Robber III | M | Required · **Learn** | New | Learn row: 40 min alone |
| 968 | Binary Tree Cameras | H | Required · Apply | New | First try, 50 min |
| 834 | Sum of Distances in Tree | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 609 | Find Duplicate File in System | M | Required · practical | New | First try, 35 min + follow-up aloud |
| 2581 | (Friday check: don't open it before Friday) | H | Check | Untouched | 45 min, alone, Friday |

⚠ **The coding page's two Week 3 templates (tree DP with three states, rerooting) are worked solutions to 968 and 834.** Don't open them before your first tries on those two, or the tries count as "Needed the solution". Monday's template drill (§d0) uses generic tree templates instead.

⚠ **You solved 1188 (bounded blocking queue) in Mar 2026, 5 submits**, and the coding page's Week 8 template is a full implementation of it. Don't open it before the §d2 starter.

### 0c. Day by day

| Day | Reviews first | Infra / apply | Code | Other |
| --- | --- | --- | --- | --- |
| **Mon Nov 2** | W1–W2 backlog (tell me) · error-log F1–F8 Rep 3 aloud (15) | §a warm-up cold (10) → §b questions cold → read → K-b (45) | §d0 template drill (15) → **337** (Learn, 40) | — |
| **Tue Nov 3** | 337 (R1) | §c labs 1–3 (50+; Docker installed beforehand) | **968** → **236\*** cold redo | Recall warm-up (10) |
| **Wed Nov 4** | 968, 236 (R1) | §b2 teach-back, recorded, no notes (25) · §e Drill 1 (30) | **834** (Learn) → **609** (practical) | — |
| **Thu Nov 5** | 834, 609 (R1) | §h cheat sheet from memory (30) · §k story practice (20) | **124\***, **102**, **98**, **1114** cold redos | — |
| **Fri Nov 6** | 337 (R2) · 124, 102, 98, 1114 (R1) = **5, at the cap** | §f design: your drawing first (40) · §e Drill 2 (30) | **2581** check, 45 min, alone | — |
| **Sat Nov 7** | 968, 236 (R2) · 2581 (R1) | §j **75-min full-loop mock** · design redrawn from memory (90) · §e Drill 3 timed 20 min · debrief (45) | (mock coding) | — |
| **Sun Nov 8** | 834, 609 (R2) · mock problem (R1) | Cheat sheet rewritten from memory (30) · **Gate 1?** | §d2 struct drill (20) + blocking-queue starter (40) · extras: 979\*\*, 1373, 1116, 388, 297, 2458 | Plan Week 4 (15) |

\* shaky by history. \*\* 979 is used in Saturday's mock; if the mock used a different problem, it's an extra.

**Week 3 reviews due each morning, if every redo is Clean:** Tue 1 · Wed 2 · Thu 2 · Fri 5 · Sat 3 · Sun 3 · Mon Nov 9: 4. That's before the W1–W2 backlog. Shaky brings an item back in 2 days at the same stage; Failed brings it back tomorrow. **Tell me each result and I'll recount before you start.**

### 0d. Session rules (same as Week 2)

- Say **"start 337"** (or any number) and I log the start time. 60-second approach aloud, brute force first, complexity before code.
- Hints: one rung per request, only after 25 min stuck. A Learn row gets the full 40 minutes first. No hints at all during the Friday check.
- I compile your file with `clang++ -std=c++17 -Wall -Wextra` and show compile errors. I never fix or rewrite your code.
- Marks: first tries **Solved alone / Needed the solution**. Redos **Clean** (first submit, < 25 min, no hint) / **Shaky** (slow, 2+ submits, or one hint) / **Failed**.

---

## (a) Day 1 recall warm-up (cold, aloud, before any reading)

10 questions: 7 Week 3 (you haven't read anything yet, so answer from what you already know) and 3 from earlier weeks (error-log reps). One or two sentences each. Mark each ✓ / ✗ before opening K-a.

1. Which Dockerfile instructions add a filesystem layer, and which only change metadata?
2. You install packages in one `RUN`, then delete `/var/lib/apt/lists/*` in the next `RUN`. Does the image get smaller? Why?
3. What decides whether a `COPY` step is a cache hit? A `RUN` step?
4. `CMD python app.py` vs `CMD ["python", "app.py"]`: what is PID 1 in each?
5. What does the kernel do differently with signals sent to PID 1 of a PID namespace?
6. Walk through `docker stop`: what's sent, how long it waits by default, and the exit code if it has to escalate.
7. Is root inside a container root on the host? What limits it?
8. *(Week 2, F3)* `curl` fails instantly with exit 7, or after 75 s with exit 28. What's different on the wire, and what's your first check?
9. *(Week 2, F8)* A Docker host logs `nf_conntrack: table full, dropping packet`. What is being tracked, and why does Docker's networking add to it?
10. *(Week 1, F4)* A process vanishes with exit code 137 and nothing in the app logs. Two possible causes, and one command that tells them apart.

---

## (b) Reading: questions first, then the notes

**Read:** Docker's "Building best practices" page and the "Multi-stage builds" page (both under docs.docker.com/build/building/; Docker moves its docs often, so search the titles if a link is dead).

**Before reading, answer from memory** (aloud or on paper, 1–2 sentences each):

- B1. Name five rules from the best-practices guide.
- B2. Why combine `apt-get update` and `apt-get install` in one `RUN`?
- B3. What do `--no-install-recommends` and `rm -rf /var/lib/apt/lists/*` each save?
- B4. `ADD` vs `COPY`: when is `ADD` justified?
- B5. What does `.dockerignore` change?
- B6. Why pin `FROM` to a digest, and what does pinning cost you?
- B7. In a multi-stage build, what ends up in the final image?
- B8. What does `--target` do, and what does BuildKit skip that the legacy builder doesn't?
- B9. Can `COPY --from=` point at an image that isn't a stage in your Dockerfile?
- B10. Why does the guide want an explicit UID/GID with `USER`, and why no `sudo`?

Then read the two pages **only for what you missed**, then compare with the notes in **K-b**.

### (b2) Explain-aloud: three 2-minute teach-backs (Wednesday, recorded, no notes)

Record each one cold. Listen once. If you stumbled more than five times, redo it. The script outlines are in **K-b2**. Read them only after your first recording.

**T1. Layer caching order.** "Explain how Docker's build cache works and how you order a Dockerfile around it."
Most likely follow-ups:
1. Why does `COPY . .` before installing dependencies hurt, and what's the fix?
2. `RUN apt-get update` was cached three months ago. What goes wrong?
3. CI runners are fresh VMs every run. How do you keep a build cache?
4. Does touching a file (new mtime, same content) bust the `COPY` cache?
5. How do you use a secret at build time without leaking it into a layer?

**T2. Exec form vs shell form.** "What's the difference, and why does it matter in production?"
Most likely follow-ups:
1. What happens to `docker run img --debug` if `ENTRYPOINT` uses shell form?
2. Exec form doesn't expand `$PORT`. How do you get env vars into the command?
3. Your entrypoint script must run migrations first. How do you keep signals working?
4. What does `docker run --init` (tini) do, and when do you need it?
5. How do you prove what PID 1 is in a running container?

**T3. Namespaces and cgroups under a container.** "What is a container, at the kernel level?"
Most likely follow-ups:
1. Which namespaces does a Docker container get by default, and which one doesn't it get?
2. A container hits its memory limit. What happens, exactly, and where do you see it?
3. `--cpus=0.5`: how is it enforced, and what symptom does it cause?
4. Why isn't a container a VM, security-wise?
5. Why do `free` or `nproc` inside a container sometimes show the host's numbers?

---

## (c) Lab sheet (Tuesday, real commands, record what you see)

Run everything for real. Fill each **Observed** blank before you look at **K-c**. The targets tell you when you're done; how you get there is up to you.

**Mac note:** Docker on macOS runs containers inside a Linux VM. `ps` on your Mac won't show container processes, and kernel facts (cgroups, namespaces, sysctls) are the VM's, not macOS's.

### Step 0: install and verify (do this Monday night)

Pick one:

```sh
# Option A: Docker Desktop (BuildKit is the default builder)
brew install --cask docker-desktop     # if Homebrew says no such cask, the older name is: docker
open -a Docker                         # wait for "Engine running"

# Option B: Colima (free, CLI only)
brew install colima docker docker-buildx
mkdir -p ~/.docker/cli-plugins
ln -sfn "$(brew --prefix)/opt/docker-buildx/bin/docker-buildx" ~/.docker/cli-plugins/docker-buildx
colima start --cpu 4 --memory 6
```

Verify:

```sh
docker run --rm hello-world                          # expect: "Hello from Docker!"
docker buildx version                                # expect: a version line (BuildKit available)
docker info --format '{{.CgroupVersion}}'            # expect: 2
```

Observed: ______

### Lab 1: shrink a ~1 GB image to under 150 MB

```sh
cd "$HOME/Platform Prep/week_packs/week03_lab/lab1_shrink"
./make_testdata.sh                                   # creates 200 MB of "test fixtures"
time docker build -f Dockerfile.bloated -t lab1:bloated .
docker image ls lab1
docker history lab1:bloated
```

1. Record: build time ______ · the `transferring context` size in the build output ______ · image size ______ · the three biggest layers and the instruction behind each ______
2. Cache test: change the string `"ok\n"` in `app.py`, then run the same `time docker build ...` again. Record: build time ______ · which steps say `CACHED` ______ · which step was the first to rebuild ______
3. Write your own `Dockerfile` (and anything else you need) in this folder. Build it as `lab1:slim`.

**Targets:**

| Check | Command | Target |
| --- | --- | --- |
| Size | `docker image ls lab1` | `slim` < 150 MB |
| It works | `docker run -d --rm -p 8080:8080 --name l1 lab1:slim && sleep 2 && curl -s localhost:8080/healthz && docker stop l1` | prints `ok` |
| Code-only rebuild | change `app.py`, `time docker build -t lab1:slim .` | < 10 s, dependency step `CACHED` |
| No junk | `docker run --rm lab1:slim sh -c 'ls /app; command -v gcc vim curl; true'` | no `testdata/`, no compilers or editors |
| Layers | `docker history lab1:slim` | you can say what every layer is |

Observed (sizes, rebuild time, what got you each big drop): ______

What it proves: you can read `docker history`, you know which levers move size (base, context, build tools) and which move rebuild time (instruction order).

### Lab 2: make a container handle SIGTERM gracefully

```sh
cd "$HOME/Platform Prep/week_packs/week03_lab/lab2_sigterm"
docker build -t lab2:broken .
docker run -d --name l2 -p 8081:8080 lab2:broken
docker top l2                                          # who is running, as seen from outside
docker exec l2 sh -c 'tr "\0" " " < /proc/1/cmdline; echo'   # PID 1's command line
docker exec l2 grep -E 'SigCgt|SigIgn' /proc/1/status        # which signals PID 1 catches / ignores (hex masks)
```

1. Record: PID 1 is ______ · `SigCgt` mask ______. SIGTERM is signal 15, which is bit `0x4000` in these masks. Is it set? ______
2. Stop it while a request is in flight:

```sh
(curl -s localhost:8081/work; echo "curl exit=$?") &   # a 5-second request, in the background
sleep 1; time docker stop l2
docker inspect -f '{{.State.ExitCode}}' l2
docker logs l2
docker rm l2
```

Record: stop time ______ · exit code ______ · what curl printed and its exit code ______ · any shutdown line in the logs? ______

3. Fix it **in stages**, rebuilding and re-running step 2 after each one, and record every result:
   - Stage A: change only the entrypoint script. Stop time ______ · exit ______ · surprised? Why? ______
   - Stage B: change the app so SIGTERM finishes in-flight work and exits cleanly. Stop time ______ · exit ______ · curl got `done`? ______
   - Stage C: run the **original** `lab2:broken` with `docker run -d --init --name l2 -p 8081:8080 lab2:broken`, then repeat step 2. PID 1 is now ______ · stop time ______ · exit ______ · did the in-flight request finish? ______

**Target (after Stage B):** `docker stop` returns well under the 10 s timeout, the in-flight `/work` request prints `done`, the exit code is `0`, and the logs show a shutdown line.

What it proves: the PID 1 rule, the difference between forwarding a signal and handling it, and why `--init` alone isn't "graceful".

### Lab 3: run a container as non-root

```sh
cd "$HOME/Platform Prep/week_packs/week03_lab/lab3_nonroot"
docker build -f Dockerfile.root -t lab3:root .
docker run --rm lab3:root id
docker run --rm lab3:root grep -E '^(Uid|CapEff)' /proc/self/status
docker run --rm lab3:root sh -c 'echo pwned >> /etc/passwd && tail -1 /etc/passwd'
```

1. Record: `id` ______ · `CapEff` ______ · did the write to `/etc/passwd` work? ______
2. Write your own `Dockerfile` so the app runs as **UID 10001, GID 10001**, and can still write `/app/data`. Build it as `lab3:nonroot`.

**Targets:**

| Check | Command | Target |
| --- | --- | --- |
| Identity | `docker run --rm lab3:nonroot id` | `uid=10001` |
| Capabilities | `docker run --rm lab3:nonroot grep CapEff /proc/self/status` | all zeros |
| Can't touch the system | `docker run --rm lab3:nonroot sh -c 'echo x >> /etc/passwd'` | `Permission denied` |
| App still writes | `docker run -d --rm --name l3 -p 8082:8080 lab3:nonroot && sleep 1 && curl -s localhost:8082/ && curl -s localhost:8082/ && docker stop l3` | `visits=2 uid=10001` |
| Read-only rootfs | `docker run -d --rm --name l3 --read-only --tmpfs /tmp -v l3data:/app/data -p 8082:8080 lab3:nonroot && sleep 1 && curl -s localhost:8082/ && docker stop l3` | works |
| Least privilege | add `--cap-drop ALL --security-opt no-new-privileges` to the run above | still works |

3. Two traps. Record what happens and explain it before checking K-c:
   - `docker run --rm -e PORT=80 -p 8083:80 lab3:nonroot` as UID 10001. Does binding port 80 fail? ______ Then run `docker run --rm alpine sysctl net.ipv4.ip_unprivileged_port_start` ______
   - `docker run --rm -v l3data:/d alpine ls -ln /d`. Who owns the files in the named volume, and why? ______

What it proves: you can say exactly what "non-root" changes (UID, effective capabilities, file ownership) and what it doesn't.

### Lab 4 (optional, 15 min, feeds teach-back T3)

```sh
docker run -d --name ns1 --memory 64m --cpus 0.5 --pids-limit 50 python:3.12-slim sleep 3600
docker exec ns1 sh -c 'cat /sys/fs/cgroup/memory.max /sys/fs/cgroup/cpu.max /sys/fs/cgroup/pids.max'
docker exec ns1 ls -l /proc/self/ns
docker exec ns1 cat /proc/self/cgroup
docker run --name oom --memory 64m --memory-swap 64m python:3.12-slim python -c "b = bytearray(200 * 1024 * 1024)"
docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}}' oom
docker rm -f ns1 oom
```

Record each output and explain every number: ______

---

## (d) Coding

### (d0) Monday template drill (under 15 min, compiled, asserts passing)

Blank file, no notes, explicit headers (no `<bits/stdc++.h>` on Apple clang). `clang++ -std=c++17 -Wall -Wextra drill.cpp && ./a.out`. These are generic tree tools, not any problem's solution.

| # | Function | Spec |
| --- | --- | --- |
| T1 | `TreeNode* build(const vector<optional<int>>& lv)` | Build a tree from LeetCode's level-order format with nulls |
| T2 | `vector<int> inorder(TreeNode*)` | Iterative, explicit stack, no recursion |
| T3 | `Info info(TreeNode*)` | Post-order DFS that **returns** a struct `{height, size, sum}` (height counts nodes, null = 0) |
| T4 | `rootAt0(n, edges, parent, order)` + `subtreeSizes(n, parent, order)` | From an undirected edge list: parent array and a top-down visit order, **iteratively**; then subtree sizes bottom-up from that order |

Asserts your code must pass:

```
r = build({1, 2, 3, nullopt, 4})
inorder(r) == {2, 4, 1, 3}
info(r) == {height 3, size 4, sum 10}
build({}) == nullptr and info(nullptr).size == 0
edges {0,1},{0,2},{2,3},{2,4}: order[0] == 0, parent[3] == 2, size[0] == 5, size[2] == 3, size[1] == 1
a 100,000-node chain: subtreeSizes(...)[0] == 100000, with no crash
```

Answer aloud after it compiles:
1. Why does T4 need `parent` (or a visited array), when a binary tree DFS doesn't?
2. Why does walking `order` backwards give a valid bottom-up (post-order) pass?
3. What would the 100,000-node chain do to a recursive DFS, and roughly why?
4. In T3, why return a struct instead of updating globals?

### (d1) Pattern map: the 10 problems

Pattern and "why it's here" only. The **Socratic question** is for before you start; the **hint ladders** are sealed in K-d, opened one rung at a time after 25 minutes stuck.

| # | Pattern | Why it's in this week | Socratic question (answer before coding) |
| --- | --- | --- | --- |
| 102 | BFS by levels | The baseline traversal everything else assumes; also the shape of "roll out in waves" | How do you know where one level ends without storing a depth on every node? |
| 236 | Post-order: return a pointer up | The first "children report, parent decides" problem; 7 submits says the reporting rule isn't fixed yet | If a subtree contains exactly one of p and q, what should it report to its parent? |
| 98 | DFS with inherited bounds (or in-order) | Passing state *down*, the mirror image of tree DP passing state *up* | Why isn't "each node is between its two children" enough? |
| 124 | Post-order: return one thing, record another | The bridge to tree DP: what a node returns differs from what it counts | What can a node hand its parent, and what can it only count as a candidate answer? |
| 1114 | Ordering threads with a condition variable / promise | Concurrency starter (week 8 builds on it); pairs with the blocking-queue spec in §d2 | How does the second thread learn that the first has finished, without spinning? |
| 337 | Tree DP returning a pair | **Learn row:** the smallest "return a tuple" problem | For any subtree, which two numbers does its parent need? |
| 968 | Tree DP with several states, greedy from the leaves | **Apply:** multi-state returns; proving the greedy is part of the answer | Is it ever better to put a camera on a leaf than on its parent? |
| 834 | Rerooting (two passes) | **Learn row:** an answer for every root in O(n) instead of O(n²) | If you know the answer for root p, what changes when the root moves to its child u? |
| 609 | Parsing + hash map grouping | **Practical row:** the real interview question is the follow-up about GB-sized files | What do you group by, and what's wrong with doing that for 10 GB files? |
| 2581 | Tree DP / rerooting (per the plan) | **End-of-week check:** unseen, 45 min, alone. No Socratic question, no hints during the attempt | — |

After each problem, answer the five pattern-notebook questions: the invariant, why the complexity holds, edge cases, the second-best approach, and what changes if one constraint changes.

### (d2) C++ extras

#### Struct layout drill (Sunday, 20 min)

Target: 64-bit Linux / macOS (LP64). `char` 1, `bool` 1, `short` 2, `int` 4, `double` 8, pointers 8. For each struct, write **sizeof** and **alignof** on paper first. Commit your answers by writing them as `static_assert(sizeof(S1) == ?, "");` lines under the definitions. Then tell me and I'll compile it: any wrong answer shows up as a compile error. Don't open K-d2 until you've committed.

```cpp
struct S1 { char a; int b; char c; };
struct S2 { char a; char c; int b; };
struct S3 { double d; char c; };
struct S4 { char c; double d; int i; };
struct S5 { int a; short b; char c; };
struct S6 { char a[3]; short s; };
struct S7 { char c; S1 inner; };
struct S8 { bool b; void* p; bool b2; };
struct Empty {};
struct S9 { Empty e; int x; };
struct S10 { virtual ~S10() {} int x; };
```

Bonus (say aloud): (1) Reorder S4's members for the smallest size. What is it? (2) `struct S9b : Empty { int x; };`: sizeof? Why is it different from S9? (3) Give the offset of every member of `struct S11 { int16_t a; int64_t b; int8_t c; int32_t d; };`. (4) Why did this drill leave out `long double` and bit-fields?

#### Bounded blocking queue: starter spec (Sunday, 40 min)

**Spec only.** Write it from a blank file, then I compile and run it with ThreadSanitizer. I won't fix it.

```
template <class T> class BoundedBlockingQueue {
public:
    explicit BoundedBlockingQueue(size_t capacity);   // capacity >= 1
    void push(T item);              // blocks while full
    T pop();                        // blocks while empty; FIFO order
    size_t size() const;            // a snapshot, thread-safe
    // Stretch (do after the four above pass):
    void close();                   // wakes every waiter; push after close returns false / is rejected
    std::optional<T> pop_or_closed(); // empty optional once closed AND drained
    bool try_push_for(T item, std::chrono::milliseconds timeout);
};
```

Requirements: no busy-waiting; correct under spurious wakeups; no lost wakeups; works with a move-only `T` (e.g. `std::unique_ptr<int>`); `size()` callable from a `const` reference.

Tests to write yourself:
1. 1 producer, 1 consumer, 10,000 items: the consumer sees 0..9999 in order.
2. 4 producers × 4 consumers, 100,000 items in total: the sum consumed equals the sum produced, and nothing hangs.
3. Capacity 1: a strict ping-pong still finishes.
4. `push` into a full queue blocks until a `pop` happens (prove it with a timestamp or a flag).
5. Stretch: `close()` while consumers are blocked: all of them return.

Build: `clang++ -std=c++17 -g -O1 -fsanitize=thread -pthread bq.cpp -o bq && ./bq`. Expect no `WARNING: ThreadSanitizer` lines.

Say aloud afterwards: why the predicate form of `wait`; one condition variable or two, and why; what goes wrong with `notify_one` if both producers and consumers share one condition variable.

---

## (e) Troubleshooting drills (symptoms only)

Use your routine aloud: **Clarify, Scope, Stabilise, Hypothesise, Check, Fix-and-prevent** ("Can Some Students Handle Cold Fixes"). Ask me clarifying questions; I answer from the sealed interviewer sheet in K-e. Scoring is in K-e.

**This week, Check and Fix-and-prevent count double.** Your error log shows "no check command, no fix" on 6 of the 8 Week 2 drills.

### Drill 1: the slow, bloated build (Wednesday, 30 min)

> The payments-api team says CI is "unusable". Every pipeline run builds the service image, and it takes 11–14 minutes even for a one-line README change. The image is 2.1 GB. Pushing it to the registry takes about 3 minutes, and a freshly created VM takes about 6 minutes to become healthy because it has to pull the image. The build log starts with `=> [internal] load build context` … `transferring context: 1.6GB`. The team says nobody has touched the Dockerfile in months.

### Drill 2: the container ignores SIGTERM (Friday, 30 min)

> A rolling deploy updates a service across 120 VMs, one container per VM, behind an L7 load balancer. On every VM swap the load balancer shows a burst of 502s and clients report `connection reset by peer`. Each VM sits in "stopping" for about 10 seconds. On a VM that has finished, `docker ps -a` shows `Exited (137) 3 minutes ago`, and the app's logs have no shutdown line. The team says: "The app definitely handles shutdown. We tested it locally, Ctrl-C stops it cleanly."

### Drill 3: three broken Dockerfiles (Saturday, 20 min total, the Gate 1 standard)

For each file: list every fault, say what breaks in production because of it, and rank the faults by severity. Don't rewrite the files; name the fix in one line per fault.

**Dockerfile A: Python API**

```dockerfile
FROM python:latest
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y build-essential libpq-dev curl
RUN pip install -r requirements.txt
ENV DATABASE_URL=postgres://app:Sup3rS3cret@db.internal:5432/payments
EXPOSE 8080
CMD python -m gunicorn app:server -b 0.0.0.0:8080
```

**Dockerfile B: Go service on Alpine**

```dockerfile
FROM golang:1.23 AS build
WORKDIR /src
COPY . .
RUN go build -o /out/server ./cmd/server
FROM alpine:3.20
COPY --from=build /out/server /server
USER nobody
ENTRYPOINT /server --port=8080
```

(`./cmd/server` is an HTTP server that uses `net/http`.)

**Dockerfile C: Node app with an entrypoint script**

```dockerfile
FROM node:20
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build && rm -rf src node_modules/.cache
RUN chown -R node:node /app
USER node
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["node", "dist/server.js"]
```

`docker-entrypoint.sh`:

```sh
#!/bin/sh
./scripts/migrate.sh
node dist/server.js
```

(The repo has `package-lock.json` and no `.dockerignore`. Developers run `npm install` on their Macs, so the repo checkout has a local `node_modules/`.)

---

## (f) Design: "Safely deploying a containerised service to a VM fleet"

**Prompt (as an interviewer would say it):**

> We run a stateless HTTP service, packaged as a container image, on a few thousand Linux VMs across more than one cloud. Design the system that ships a new version to that fleet safely. 45 minutes.

**Rules:** draw on paper first, from blank, for 40 minutes (Friday). Then send me a photo or type it out, and I critique it against the checklist and the sealed rubric in K-f. I don't draw it for you. Saturday: redraw from memory.

**Blank-page checklist (Real Apps Deserve Deep Failure Tests).** Your drawing must answer every line. These are questions, not answers.

**Requirements (5 min)**
- [ ] Fleet size, regions/clouds, containers per VM, deploys per day
- [ ] What "safe" means, in numbers: maximum blast radius (% of capacity a bad build can reach), rollback time, error budget spent during a deploy
- [ ] Zero-downtime required? Any state on the VM (local disk, sessions)?
- [ ] Who triggers a deploy, and who can stop one?

**API (5 min)**
- [ ] The deployer's API: create a release, promote, pause, resume, roll back, status
- [ ] Controller ↔ VM protocol: push or pull? What does a VM report back, and how often?

**Data (5 min)**
- [ ] What you store: release, image identity, desired version per host group, wave state, health samples, audit log
- [ ] Image identity: tag or digest? Why?
- [ ] Where the state lives and what happens if it's lost

**Deep dive (15 min): pick one and go deep**
- [ ] The wave / canary controller: wave sizes, health gates, bake time, automatic halt and rollback
- [ ] The per-VM update sequence: pull, verify, start new, health-check, switch traffic, drain old, stop old, SIGTERM timing
- [ ] Image distribution at scale: registry limits, regional mirrors, pre-pulling

**Failures (5 min)**
- [ ] The controller dies mid-rollout
- [ ] A VM never reports back
- [ ] The registry is down or slow
- [ ] The new image passes health checks but fails 20 minutes later
- [ ] Two releases started at once
- [ ] The rollback image is gone or itself broken

**Tradeoffs (5 min)**
- [ ] Push vs pull · in-place vs blue/green on the same VM vs replacing the VM · wave size (speed vs safety) · automatic vs manual promotion
- [ ] What changes at 10× the fleet, or 10× the deploy rate

**Numbers that must appear on your page:** wave sizes as % · bake time per wave · health-gate thresholds · drain seconds · stop timeout · rollback time end to end.

---

## (g) Flashcards (10 new cards: put them in Anki; answers in K-g)

| # | Type | Front |
| --- | --- | --- |
| 1 | Explain | Why does a container ignore SIGTERM? |
| 2 | Explain | Why doesn't deleting a file in a later `RUN` shrink the image? |
| 3 | Explain | Shell form vs exec form: what's the difference that matters in production? |
| 4 | Explain | Namespaces vs cgroups: what does each give a container? |
| 5 | Explain | What does a multi-stage build put in the final image, and why does that shrink it? |
| 6 | Command | `docker stop` takes 10 s and the exit is 137. Show what PID 1 is and whether it catches SIGTERM. |
| 7 | Command | The image is 1.2 GB. Which layer is the problem? |
| 8 | Command | A container exited 137. Was it the OOM killer? |
| 9 | Template | Write a cache-friendly, multi-stage, non-root Dockerfile skeleton for a Python service. |
| 10 | Template | Write an entrypoint script that runs a setup step and still delivers signals to the app. |

---

## (h) Cheat sheet skeleton (Thursday: fill it from memory; Sunday: rewrite it from blank)

A copy of this skeleton is in `cheat_sheets/week03_containers.md`. Fill it with no notes, then compare with K-h and mark the points you missed.

**TOP: the five things I'd say about containers in an interview**
1. ______
2. ______
3. ______
4. ______
5. ______

**MIDDLE: key commands**

| I want to… | Command |
| --- | --- |
| See which layer is big | ______ |
| See which build step missed the cache | ______ |
| See what PID 1 is and which signals it catches | ______ |
| Tell OOM from a stop timeout | ______ |
| See a container's cgroup limits | ______ |
| See a container's namespaces | ______ |
| Send one signal to test shutdown | ______ |
| Scan an image for CVEs | ______ |

**MIDDLE: failure modes**

| Symptom | Cause | First check |
| --- | --- | --- |
| Every build takes minutes, even for a one-line change | ______ | ______ |
| `docker stop` always takes exactly the timeout; exit 137 | ______ | ______ |
| `exec /server: no such file or directory`, but the file exists | ______ | ______ |
| `Permission denied` writing app data after switching to non-root | ______ | ______ |
| Exit 137 with `OOMKilled: true` | ______ | ______ |
| Latency spikes, CPU never at 100%, a `--cpus` limit is set | ______ | ______ |
| A secret shows up in `docker history` | ______ | ______ |

**BOTTOM: three interview questions and the story from my work that fits each**

| Interview question | My story | The number I'll say |
| --- | --- | --- |
| ______ | ______ | ______ |
| ______ | ______ | ______ |
| ______ | ______ | ______ |

---

## (i) Review-due table (template)

Every problem and every concept gets a self-mark: **Clean / Shaky / Failed**. Spacing counts from the day of the last redo: 1 → 3 → 7 → 14 → 30 → 60 days. **Clean** → next interval · **Shaky** → same stage in 2 days · **Failed** → back to 1 day. Dates below assume Clean every time. Tell me any other mark and I'll redo the row.

### Problems

| # | Problem | Day 0 | Mark | +1 | +3 | +7 | +14 | +30 | +60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 337 | House Robber III | Mon Nov 2 | | Nov 3 | Nov 6 | Nov 13 | Nov 27 | Dec 27 | Feb 25 |
| 968 | Binary Tree Cameras | Tue Nov 3 | | Nov 4 | Nov 7 | Nov 14 | Nov 28 | Dec 28 | Feb 26 |
| 236 | LCA of a Binary Tree | Tue Nov 3 | | Nov 4 | Nov 7 | Nov 14 | Nov 28 | Dec 28 | Feb 26 |
| 834 | Sum of Distances in Tree | Wed Nov 4 | | Nov 5 | Nov 8 | Nov 15 | Nov 29 | Dec 29 | Feb 27 |
| 609 | Find Duplicate File in System | Wed Nov 4 | | Nov 5 | Nov 8 | Nov 15 | Nov 29 | Dec 29 | Feb 27 |
| 124 | Binary Tree Max Path Sum | Thu Nov 5 | | Nov 6 | Nov 9 | Nov 16 | Nov 30 | Dec 30 | Feb 28 |
| 102 | Level Order Traversal | Thu Nov 5 | | Nov 6 | Nov 9 | Nov 16 | Nov 30 | Dec 30 | Feb 28 |
| 98 | Validate BST | Thu Nov 5 | | Nov 6 | Nov 9 | Nov 16 | Nov 30 | Dec 30 | Feb 28 |
| 1114 | Print in Order | Thu Nov 5 | | Nov 6 | Nov 9 | Nov 16 | Nov 30 | Dec 30 | Feb 28 |
| 2581 | (check) | Fri Nov 6 | | Nov 7 | Nov 10 | Nov 17 | Dec 1 | Dec 31 | Mar 1 |
| 979 | Distribute Coins (mock) | Sat Nov 7 | | Nov 8 | Nov 11 | Nov 18 | Dec 2 | Jan 1 | Mar 2 |

Each gap counts from the previous redo, so the dates are cumulative: Day 0, then +1, then +3 from that, and so on.

### Concepts (cards, labs, drills, design)

| Item | Day 0 | Mark | +1 | +3 | +7 | +14 | +30 | +60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| §d0 template drill | Mon Nov 2 | | | | | | | |
| Lab 1: shrink (redo from blank, no notes) | Tue Nov 3 | | | | | | | |
| Lab 2: SIGTERM | Tue Nov 3 | | | | | | | |
| Lab 3: non-root | Tue Nov 3 | | | | | | | |
| T1 teach-back: caching order | Wed Nov 4 | | | | | | | |
| T2 teach-back: exec vs shell | Wed Nov 4 | | | | | | | |
| T3 teach-back: namespaces + cgroups | Wed Nov 4 | | | | | | | |
| Drill 1: slow build | Wed Nov 4 | | | | | | | |
| Drill 2: ignores SIGTERM | Fri Nov 6 | | | | | | | |
| Design: deploy to VM fleet | Fri Nov 6 | | | | | | | |
| Drill 3: broken Dockerfiles | Sat Nov 7 | | | | | | | |
| Struct layout drill | Sun Nov 8 | | | | | | | |
| Blocking queue | Sun Nov 8 | | | | | | | |
| Flashcards 1–10 (Anki: 1, 3, 7, 21 days) | Mon Nov 2 | | | | | | | |

---

## (j) Saturday mock: full loop, 75 minutes, recorded

70% Week 3, 30% Weeks 1–2 (Linux, networking). I'm the interviewer, running from the sealed sheet in K-j. **Don't read K-j.**

| Time | Block | Mix |
| --- | --- | --- |
| 0–5 | Intro: your 90-second intro + 2 rapid recall questions | Weeks 1–2 |
| 5–40 | Coding: one unseen tree problem, C++, talked through | Week 3 |
| 40–55 | Troubleshooting: one scenario, six-step routine | Week 3 + Week 2 |
| 55–70 | Mini design: a fleet rollout under time pressure | Week 3 + Week 1 story |
| 70–75 | Your questions for me | — |

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
| **Average** | | |

### Debrief template (within an hour of the mock)

1. What was asked, block by block: ______
2. Where I stalled (timestamp, what I was thinking, what I should have said): ______
3. What I'd say differently in the first 60 seconds of each block: ______
4. One drill per stall (goes on the review schedule): ______

### Mock error-log table

| Problem / topic | Mark (Clean / Shaky / Failed) | Miss type (pattern / syntax / edge case / concept / routine step / communication) | Fix (the drill) |
| --- | --- | --- | --- |
| | | | |
| | | | |

Each row also goes into `error_log.md` in its own format (Date | Problem or topic | What went wrong | Root cause | Rep 1 | Rep 2 | Rep 3), with reps at +1, +3, +7 days.

---

## (k) Story: vulnerability remediation at scale

From your plan: vulnerability remediation across 13,000+ VMs. **Blanks stay blank until you fill them with real facts.** I won't invent any of them.

| Part | Your words (under 2 minutes in total) |
| --- | --- |
| Situation (what was vulnerable, how many hosts/images, what deadline or risk) | ______ |
| My decision (what *you* chose to do, not the team) | ______ |
| The tradeoff (what you gave up: speed vs safety, coverage vs disruption) | ______ |
| The number (hosts patched, time to remediate, % done by the deadline, incidents caused) | ______ |
| Lesson (what you'd do differently or what you built because of it) | ______ |

**Deep-dive questions to answer aloud before writing the story** (this is the "theme" a hiring manager drills into):
1. How did you know which hosts or images were affected, within an hour of a CVE landing?
2. How did you decide what to patch first?
3. A container image and the VM under it can both be vulnerable. How did each get fixed?
4. How did you roll the fix out without causing an outage?
5. How did you prove it was fixed, and what happened to the hosts that couldn't be patched?
6. What metric did you report upward?

Reference beats for a strong answer are in K-k. Use them to check your coverage, not to fill the blanks.

---
---

# ANSWER KEY

Stop. Everything below is answers. Open only the part for the section you've finished.

---

## K-a. Warm-up answers

1. `RUN`, `COPY` and `ADD` add filesystem layers. Most other instructions (`ENV`, `LABEL`, `CMD`, `ENTRYPOINT`, `EXPOSE`, `USER`) only change the image config; they show as 0 B in `docker history`.
2. No. Layers are immutable and stacked. The later delete only adds a "whiteout" entry that hides the files; the bytes stay in the earlier layer. Delete in the same `RUN` that created them, or build in a stage you throw away.
3. `COPY`/`ADD`: the instruction plus a checksum of the files' contents (mtime is ignored). `RUN`: only the command string on top of the same parent layer; Docker doesn't check what the command would download. The first miss rebuilds every step after it.
4. Shell form runs `/bin/sh -c "python app.py"`, so PID 1 is `sh`, unless that shell happens to `exec` a lone command (some do, so check rather than assume). Exec form: `python` is PID 1.
5. The kernel doesn't apply default actions to a namespace's PID 1: a signal with no installed handler is dropped. SIGKILL and SIGSTOP from the parent namespace are the exception. So a PID 1 with no SIGTERM handler ignores SIGTERM.
6. SIGTERM (or the image's `STOPSIGNAL`) to PID 1 → wait 10 s (`docker stop -t N`, or `--stop-timeout` at run time) → SIGKILL. Exit 137 = 128 + 9. A process that died from the SIGTERM itself exits 143 = 128 + 15.
7. Yes: it's UID 0 on the host unless user namespaces are on (rootless Docker or `userns-remap`). It's limited by a reduced capability set, seccomp, AppArmor/SELinux and its mount namespace. `--privileged`, a mounted `docker.sock` or a kernel bug turns it into full host root.
8. Exit 7 instantly = the client got an RST: the host is reachable but nothing listens on that port (or a REJECT rule). Exit 28 after the timeout = silence: SYNs dropped somewhere (DROP rule, routing, dead host). Check: `ss -ltnp` on the server, `tcpdump -nn host <ip> and port <p>` on both ends.
9. conntrack keeps every stateful/NAT flow in a fixed-size table (`nf_conntrack_max`). Docker's bridge networking and `-p` port publishing are iptables NAT (DNAT in, MASQUERADE out), so every container connection gets an entry. Full table → new connections dropped. Check: `cat /proc/sys/net/netfilter/nf_conntrack_count` vs `nf_conntrack_max` (or `conntrack -C`). Fix: raise max and hashsize, shorten timeouts, cut connection churn with keep-alive and pooling.
10. 137 = killed by SIGKILL: the OOM killer, or something sent `kill -9` (including `docker stop` escalating after its timeout). Check: `dmesg -T | grep -iE 'oom|killed process'` (or `journalctl -k`), and for a container `docker inspect -f '{{.State.OOMKilled}}' <c>`.

---

## K-b. Reading notes

Check your B1–B10 answers against these. Docker reorganises its docs often. These notes describe the pages' content, not exact section numbers.

### "Building best practices", the rules
- **Multi-stage builds** to keep build tools out of the final image.
- **Right base image:** trusted (Docker Official Images, Verified Publisher) and small.
- **Rebuild often:** `docker build --pull` gets a fresh base; `--no-cache` forces a full rebuild so patched packages actually land.
- **`.dockerignore`** keeps files out of the build context, and so out of `COPY . .`.
- **Ephemeral containers:** stop, destroy, replace, with minimal setup.
- **No unnecessary packages.** **One concern per container.**
- **Sort multi-line arguments** (fewer duplicates, easier review).
- **Use the build cache:** order steps from least to most often changed.
- **Pin base image versions.** Tags are mutable; a digest (`FROM python:3.12-slim@sha256:…`) isn't. The cost: you stop getting base-image security fixes automatically, so pair digest pins with an automated bump (Renovate, Dependabot).
- **Build and test in CI.**

### Instruction notes
- **RUN + apt (B2, B3):** `apt-get update && apt-get install -y --no-install-recommends pkg && rm -rf /var/lib/apt/lists/*` in **one** `RUN`. On its own, `update` gets cached, so a later `install` uses stale indexes (cache busting is the reason to combine them). `--no-install-recommends` skips optional packages; deleting the lists saves the package indexes, tens of MB. Official Debian/Ubuntu images already run `apt-get clean`. For pipes, use `set -o pipefail` (needs bash, e.g. `SHELL ["/bin/bash", "-o", "pipefail", "-c"]`), or a failed first command is hidden.
- **CMD / ENTRYPOINT:** exec form. `ENTRYPOINT` is the main command, `CMD` its default arguments. A helper script must end with `exec "$@"`.
- **EXPOSE** is documentation only. It doesn't publish a port.
- **ENV:** each `ENV` persists in the image config. Unsetting it in a later step doesn't remove it from history. For a temporary value, set and use it inside one `RUN`.
- **ADD vs COPY (B4):** `COPY` for local files. `ADD` only for remote URLs or Git sources (with `--checksum`) or to auto-extract a local tar. For files needed during one `RUN` only, use `RUN --mount=type=bind`.
- **USER (B10):** use an explicit UID/GID, so file ownership and host or Kubernetes policies (`runAsUser`, volume permissions) are predictable. No `sudo`: it has unpredictable TTY and signal-forwarding behaviour; use `gosu` if a root init step is unavoidable. Avoid switching `USER` back and forth.
- **WORKDIR:** absolute paths; never `RUN cd …`.
- **VOLUME** for mutable data. **ONBUILD** triggers run in child images.

### Multi-stage builds
- Every `FROM` starts a stage. Only the **last stage** (or the `--target` stage) becomes the image; earlier stages' files are left behind unless you `COPY --from` them (B7).
- Name stages: `FROM golang:1.23 AS build`, then `COPY --from=build /out/app /app`. Unnamed stages are numbered from 0.
- `--target <stage>` stops at that stage: debug, test and prod images from one file. **BuildKit builds only the stages the target depends on; the legacy builder builds every stage up to the target** (B8).
- `COPY --from=` can name any image, e.g. `COPY --from=nginx:1.27 /etc/nginx/nginx.conf /nginx.conf` (B9).
- A stage can start from an earlier one: `FROM build AS test`.

---

## K-b2. Teach-back outlines and follow-up answers

### T1: Layer caching order (2 minutes, 6 beats)
1. An image is a stack of read-only, content-addressed layers. `RUN`, `COPY` and `ADD` each add one.
2. The builder walks top-down. A step is reused if its parent layer and its instruction are identical, plus the file checksums for `COPY`/`ADD`.
3. The first miss invalidates every step below it.
4. So: base → system packages → copy only the dependency manifest → install dependencies → copy the source → build.
5. Result: a code change rebuilds only the last layers (minutes → seconds), and the big dependency layer is pulled once per host and shared.
6. Traps: a lone `apt-get update`; no `.dockerignore` (a changing `.git/` busts `COPY . .`); ephemeral CI runners start with no cache.

Follow-ups:
1. Any file change busts the `COPY` layer, so the dependency install reruns every time. Copy the manifest first, install, then copy the source.
2. Its old package index is reused, so an `install` added later can 404 or install stale versions. Keep `update && install` in one `RUN`; use `--pull` / `--no-cache` on scheduled rebuilds.
3. Export the cache to the registry: `docker buildx build --cache-to type=registry,ref=<repo>:buildcache,mode=max --cache-from type=registry,ref=<repo>:buildcache .` Use cache mounts (`RUN --mount=type=cache,target=/root/.cache/pip`) for package-manager caches.
4. No. The checksum covers file contents (Docker's docs say last-modified and last-accessed times are ignored).
5. `RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci`, built with `--secret id=npmrc,src=$HOME/.npmrc`. Never `ARG` or `ENV`: both are visible in `docker history` / the image config.

### T2: Exec form vs shell form (2 minutes, 6 beats)
1. Exec form is a JSON array, run directly. Shell form is a string, run as `/bin/sh -c "<string>"`.
2. With shell form the shell is PID 1. `docker stop` signals PID 1 only. A shell with no SIGTERM handler, as PID 1, ignores it, and the app never hears it → 10 s → SIGKILL → 137 → in-flight requests cut.
3. A shell-form `ENTRYPOINT` also ignores `CMD` and any `docker run` arguments.
4. Exec form has no shell, so no `$VAR` expansion, globs or pipes. It also needs double quotes; invalid JSON silently falls back to shell form.
5. Need setup steps or env expansion? Use an entrypoint script that ends with `exec "$@"`, so the app *replaces* the shell as PID 1.
6. Then the app itself must handle SIGTERM (it's PID 1 now) and reap children if it forks, or run with `--init`.

Follow-ups:
1. `--debug` is dropped: shell-form `ENTRYPOINT` ignores `CMD` and run arguments.
2. `ENTRYPOINT ["sh", "-c", "exec myapp --port \"$PORT\""]`, or an entrypoint script. The key word is `exec`.
3. Run the migrations in the script, then `exec "$@"` with `CMD` holding the app command.
4. `--init` makes a tiny init (tini, as `docker-init`) PID 1. It forwards signals to its child and reaps zombies. Needed when the app can't be PID 1 safely: it forks children, or you can't add a handler. It forwards a signal; it doesn't make the app drain gracefully.
5. `docker exec <c> cat /proc/1/cmdline | tr '\0' ' '`, `docker top <c>`, and `docker inspect -f '{{json .Config.Entrypoint}} {{json .Config.Cmd}}' <c>`. Signal mask: `grep SigCgt /proc/1/status` (SIGTERM = bit 0x4000).

### T3: Namespaces and cgroups (2 minutes, 6 beats)
1. A container is an ordinary Linux process with namespaces (what it can see), cgroups (what it can use), a root filesystem made from image layers (overlayfs), and reduced privileges (capabilities, seccomp, LSM).
2. Namespaces: **pid** (its own PID 1), **net** (own interfaces; a veth pair to the `docker0` bridge), **mnt** (the image rootfs), **uts** (hostname), **ipc**, and **cgroup** (the default on cgroup v2). **user** is *not* on by default.
3. cgroups v2: `memory.max` (over it → OOM kill inside the cgroup), `cpu.max` (CFS quota → throttling, never a kill), `pids.max` (fork fails with EAGAIN).
4. One shared kernel: it's not a VM. A kernel bug crosses the boundary, and `/proc/meminfo` and `/proc/cpuinfo` aren't namespaced.
5. Proof on a host: `ls -l /proc/<pid>/ns`, `cat /proc/<pid>/cgroup`, the `memory.max` file in that cgroup, `nsenter -t <pid> -n ip addr`.
6. It's all Week 1 and Week 2 again: same OOM killer, same signals, same netfilter and conntrack doing the NAT.

Follow-ups:
1. pid, net, mnt, uts, ipc, cgroup (private by default on cgroup v2). Not user, unless rootless or `userns-remap`.
2. The kernel OOM-kills a process in that cgroup. If that's PID 1, the container exits 137 and `docker inspect` shows `OOMKilled: true`. The `oom_kill` count in `memory.events` goes up; `dmesg` shows the kill.
3. CFS bandwidth: `cpu.max` = `50000 100000` (50 ms of CPU every 100 ms). Symptom: latency spikes and p99 tails while average CPU looks low. Check `nr_throttled` / `throttled_usec` in `cpu.stat`.
4. Shared kernel. Defences: drop capabilities, keep the default seccomp profile, non-root, user namespaces, read-only rootfs; for hostile tenants, a sandbox runtime (gVisor) or microVMs (Kata, Firecracker).
5. `/proc/meminfo` and `/proc/cpuinfo` show the host's. Runtimes have to read the cgroup files (modern JVMs and Go do; old ones don't). LXCFS can fake those `/proc` files.

---

## K-c. Lab: expected observations and hint rungs

Open a rung only after you're stuck. No finished Dockerfiles here, by design.

### Step 0
`hello-world` prints "Hello from Docker!", `buildx version` prints a version, cgroup version is `2`.

### Lab 1
**Expected baseline:** about 1.2–1.4 GB (the `python:3.12` base alone is roughly 1 GB, plus the 200 MB fixture plus vim). The context transfer shows ~200 MB. After a one-line code change, the `pip install` step reruns, because `COPY . .` comes before it.
**Size caveats:** exact sizes depend on the image version, your CPU architecture (arm64 on your Mac) and whether Docker uses the containerd image store, which reports sizes differently from the classic store. Compare before and after **with the same command**. If a `-slim` base plus Flask lands just over 150 MB on arm64, that's a finding: explain it, then try `-alpine` (musl: some wheels need compiling) or a distroless Python base.

- **Rung 1 (direction):** measure first. `docker history` tells you which three things to attack.
- **Rung 2 (key insight):** size has three separate levers: a smaller base, keeping junk out of the context, and building anything you need to compile in a stage you throw away. Rebuild time has one lever: instruction order.
- **Rung 3 (skeleton in words):** a `.dockerignore`; a `-slim` base; copy only the requirements file, install with no pip cache (or a cache mount), then copy the code; exec-form `CMD`. If you need compilers, use a builder stage that creates a virtualenv, and copy only the virtualenv into the slim stage.

### Lab 2
**Expected:**
- Baseline: PID 1 = `/bin/sh /app/entrypoint.sh`; `SigCgt` lacks bit `0x4000`; stop ≈ 10 s; exit 137; curl fails (exit 52 "empty reply" or 56 "reset"; record which); no shutdown log line.
- Stage A (only adding `exec` to the script): PID 1 = `python /app/app.py`, **and it still takes ≈ 10 s with exit 137.** Python installs no SIGTERM handler by default, and as PID 1 an unhandled SIGTERM is dropped. This is the lesson.
- Stage B (a handler in the app): `SigCgt` now has `0x4000`; stop ≈ 4–5 s (it waits for `/work`); curl prints `done`; exit 0; your shutdown line in the logs.
- Stage C (`--init`, original image): PID 1 = `/sbin/docker-init`. Stop is fast, but I expect the in-flight request to be cut and exit 143 rather than 0: tini forwards SIGTERM to its child (`sh`), which isn't PID 1 and so dies on the default action; when the container's init exits, the kernel kills everything left in the PID namespace, Python included. **Verify this one; I haven't run it on your machine.** Forwarding ≠ graceful.

- **Rung 1:** find out who PID 1 is and whether it catches SIGTERM (the `SigCgt` mask).
- **Rung 2:** there are two independent faults: the shell isn't replaced by the app, and the app has no SIGTERM handler. Fixing one isn't enough.
- **Rung 3:** the script's last line execs the app. The handler shouldn't call `server.shutdown()` on the thread that's running `serve_forever()`: that call waits for the loop to stop, the loop can't stop while the handler is running on its thread, and the process hangs. Trigger the shutdown from another thread. `ThreadingTCPServer.server_close()` waits for request threads (Python 3.7+, `block_on_close`), so in-flight work finishes before you exit 0.

### Lab 3
**Expected baseline:** `uid=0(root) gid=0(root) groups=0(root)`; `CapEff: 00000000a80425fb` (Docker's default capability set); the `/etc/passwd` write succeeds.
**After:** `uid=10001`; `CapEff: 0000000000000000` (a non-root process gets no effective capabilities at `exec`, even though the bounding set still holds them); the `/etc` write fails; visits work once `/app/data` belongs to 10001.
**Traps:**
- Port 80 as non-root **usually works** on Docker 20.10 and later: Docker sets `net.ipv4.ip_unprivileged_port_start=0` inside the container's network namespace, so the sysctl prints `0`. It isn't set with `--network host`, and other runtimes may differ, so check rather than assume.
- A **new** named volume mounted over a directory that has content in the image is pre-filled from the image, including ownership. So `/app/data` owned by 10001 in the image → the volume starts owned by 10001. Bind mounts get no such copy (and on macOS, bind-mount ownership goes through Docker Desktop's file sharing, which behaves differently again).

- **Rung 1:** two things change for a non-root user: who owns the files the app writes, and the process UID.
- **Rung 2:** files from `COPY` / `RUN mkdir` are owned by root unless you say otherwise. Fix ownership as the files are created, not with a later `chown -R` layer (that copies every file into a new layer).
- **Rung 3:** create a group and user with fixed IDs 10001, give the data directory to them in the same layer that creates it (or `COPY --chown`), then `USER 10001:10001` before `CMD`.

### Lab 4
`memory.max` = `67108864` · `cpu.max` = `50000 100000` · `pids.max` = `50` · `/proc/self/ns` lists cgroup, ipc, mnt, net, pid, uts (plus `pid_for_children`, `time`, `time_for_children` and `user`; Docker doesn't give the container its own `user` or `time` namespace by default) · `/proc/self/cgroup` = `0::/` (private cgroup namespace) · the `oom` container exits `137 true`.

---

## K-d0. Template drill (compiled and run on your Mac: all asserts pass)

```cpp
#include <cassert>
#include <optional>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
struct TreeNode { int val; TreeNode *left = nullptr, *right = nullptr; explicit TreeNode(int v) : val(v) {} };

// T1: level-order with nulls -> tree (LeetCode's input format)
TreeNode* build(const vector<optional<int>>& lv) {
    if (lv.empty() || !lv[0]) return nullptr;
    TreeNode* root = new TreeNode(*lv[0]);
    queue<TreeNode*> q; q.push(root);
    for (size_t i = 1; i < lv.size(); ) {
        TreeNode* cur = q.front(); q.pop();
        if (i < lv.size() && lv[i]) { cur->left = new TreeNode(*lv[i]); q.push(cur->left); } ++i;
        if (i < lv.size() && lv[i]) { cur->right = new TreeNode(*lv[i]); q.push(cur->right); } ++i;
    }
    return root;
}
// T2: iterative inorder
vector<int> inorder(TreeNode* root) {
    vector<int> out; stack<TreeNode*> st; TreeNode* cur = root;
    while (cur || !st.empty()) {
        while (cur) { st.push(cur); cur = cur->left; }
        cur = st.top(); st.pop();
        out.push_back(cur->val);
        cur = cur->right;
    }
    return out;
}
// T3: post-order DFS that RETURNS a struct
struct Info { int height; int size; long long sum; };
Info info(TreeNode* n) {
    if (!n) return {0, 0, 0};
    Info l = info(n->left), r = info(n->right);
    return {1 + max(l.height, r.height), 1 + l.size + r.size, n->val + l.sum + r.sum};
}
// T4: edges -> parent + preorder order, iteratively; then subtree sizes bottom-up
void rootAt0(int n, const vector<vector<int>>& edges, vector<int>& parent, vector<int>& order) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }
    parent.assign(n, -1); order.clear(); order.reserve(n);
    vector<int> stk{0};
    while (!stk.empty()) {
        int u = stk.back(); stk.pop_back();
        order.push_back(u);
        for (int v : adj[u]) if (v != parent[u]) { parent[v] = u; stk.push_back(v); }
    }
}
vector<int> subtreeSizes(int n, const vector<int>& parent, const vector<int>& order) {
    vector<int> sz(n, 1);
    for (int i = n - 1; i > 0; --i) sz[parent[order[i]]] += sz[order[i]];
    return sz;
}
```

Spoken answers: (1) An undirected edge list has no direction, so without `parent` you walk back up the edge you came from, forever. (2) In a preorder `order`, every parent appears before its children, so walking it backwards visits children first. (3) A recursion 100,000 frames deep can overflow the default 8 MB main-thread stack (smaller on secondary threads) → segfault. (4) A returned struct makes each subtree's answer local and composable, with no reset bugs between test cases.

---

## K-d. Hint ladders (one rung at a time, only after 25 minutes stuck)

**102 Level order**
1. Direction: breadth-first with a queue.
2. Key insight: at the start of each level, the queue holds exactly that level, so take its size *before* the loop.
3. Skeleton: while the queue isn't empty, read its size k, pop k nodes into this level's list while pushing their children, then append the list.

**236 LCA**
1. Direction: post-order; each call returns a node pointer, or null.
2. Key insight: if the current node is p or q, return it. If both sides return non-null, the current node is the answer. Otherwise pass up whichever side is non-null.
3. Skeleton: base case null/p/q → return it; recurse left and right; both non-null → return the current node; else return the non-null one.

**98 Validate BST**
1. Direction: carry an allowed (low, high) range down the tree, or do an in-order walk.
2. Key insight: a node must satisfy *every* ancestor's bound, not just its parent's. Values can be `INT_MIN`/`INT_MAX`, so use `long long` bounds or nullable pointers.
3. Skeleton: check(node, lo, hi): null → true; value outside (lo, hi) → false; recurse left with (lo, value) and right with (value, hi). Or: in-order, values strictly increasing, comparing with a "previous" node.

**124 Max path sum**
1. Direction: post-order, with one global best.
2. Key insight: a node returns its value plus **at most one** branch, dropping negative branches (max with 0). The candidate answer at the node uses **both** branches.
3. Skeleton: gain(node) = value + max(0, left gain, right gain) with only one side added; update best with value + max(0, left) + max(0, right); initialise best to the smallest possible value (all-negative trees).

**1114 Print in order**
1. Direction: shared state plus a synchronisation primitive; no sleeping or spinning.
2. Key insight: one counter ("which step is allowed now") behind a mutex, with a condition variable whose `wait` uses a predicate. Or: two one-shot signals (`std::promise<void>` / `std::future<void>`).
3. Skeleton: `second` waits until step ≥ 2, prints, sets step = 3, notifies all; `first` prints, sets step = 2, notifies all; `third` waits until step ≥ 3.

**337 House Robber III (Learn)**
1. Direction: tree DP. Each call returns two numbers.
2. Key insight: rob(node) = value + skip(left) + skip(right); skip(node) = best(left) + best(right), where best is the max of a child's two numbers.
3. Skeleton: post-order returns the pair; null → (0, 0); the answer is the max of the root's pair.

**968 Cameras**
1. Direction: post-order greedy. Each node reports one of three states.
2. Key insight: never put a camera on a leaf; put it on the leaf's parent, which covers more. States: "not covered", "covered, no camera", "has camera". A null child counts as covered.
3. Skeleton: if any child is not covered → place a camera here; else if any child has a camera → covered; else → not covered (the parent will handle it). After the root, add one camera if the root is still not covered.

**834 Sum of distances (Learn)**
1. Direction: two passes over the tree, one bottom-up and one top-down (rerooting).
2. Key insight: moving the root from p to a child u brings the `count[u]` nodes in u's subtree one step closer and pushes the other `n − count[u]` one step farther.
3. Skeleton: pass 1 (post-order from node 0): subtree counts, and the answer for node 0. Pass 2 (pre-order): each child's answer from its parent's using the rule above. Iterative traversal (your §d0 T4) because n reaches 3·10⁴ and the tree can be a chain.

**609 Duplicate files**
1. Direction: parse each line, then hash map from content to list of full paths.
2. Key insight: each line is `dir name(content) name(content)…`: split on spaces, the first token is the directory, then split each file token at `(`. Keep only groups with 2+ paths.
3. Skeleton, plus the follow-up they really ask: for real files, group by **size** first, then by a hash of the first 4 KB, then a full hash, then a byte-by-byte comparison (hash collisions). Stream through files, never load them. Discuss symlinks, permissions, and files changing mid-scan.

**2581 (check):** no hints during the 45 minutes. If you fail it, the ladder for the redo opens after your attempt is marked: ask me for it then.

---

## K-d2. Struct layout answers (verified with Apple clang 17 on arm64; x86-64 Linux gives the same numbers for these types)

| Struct | sizeof | alignof | Why |
| --- | --- | --- | --- |
| S1 `{char; int; char}` | 12 | 4 | 1 + 3 pad + 4 + 1 + 3 tail pad |
| S2 `{char; char; int}` | 8 | 4 | 2 + 2 pad + 4 |
| S3 `{double; char}` | 16 | 8 | 8 + 1 + 7 tail pad (arrays must keep `double` aligned) |
| S4 `{char; double; int}` | 24 | 8 | 1 + 7 + 8 + 4 + 4 tail |
| S5 `{int; short; char}` | 8 | 4 | 4 + 2 + 1 + 1 tail |
| S6 `{char[3]; short}` | 6 | 2 | 3 + 1 pad + 2 |
| S7 `{char; S1}` | 16 | 4 | 1 + 3 pad + 12; a nested struct aligns to *its* alignment (4), at offset 4 |
| S8 `{bool; void*; bool}` | 24 | 8 | 1 + 7 + 8 + 1 + 7 |
| Empty | 1 | 1 | every object needs a distinct address |
| S9 `{Empty; int}` | 8 | 4 | the member still takes 1 byte + 3 pad. No empty-base optimisation for *members* (C++20 `[[no_unique_address]]` fixes that) |
| S10 `{virtual dtor; int}` | 16 | 8 | 8-byte vptr + 4 + 4 tail |

Bonus: (1) `{double; int; char}` → 16. (2) `S9b : Empty {int}` → 4: the empty-base optimisation applies to base classes. (3) S11: `a` @0, `b` @8, `c` @16, `d` @20, sizeof 24, alignof 8. (4) `long double` is 16 bytes on x86-64 Linux but 8 on arm64 macOS, and bit-field layout is ABI-specific, so neither has one right answer.

Rules to say aloud: each member sits at a multiple of its own alignment; the struct's alignment is its largest member's; sizeof rounds up to a multiple of that alignment; order members largest-first to cut padding.

---

## K-e. Troubleshooting: interviewer sheets and scoring

**Scoring (per drill).** Each of the six steps scores 0 (missing), 1 (present) or 2 (specific: a named command and the result that would confirm or rule it out). **Check and Fix-and-prevent are doubled this week**, for a total of 16. 15–16 → 4 · 11–14 → 3 · 7–10 → 2 · below 7 → 1. That's your Troubleshooting score on the scorecard. Every missed step becomes an error-log row.

### Drill 1: slow, bloated build
**Facts, only if asked:**
- CI runners are fresh VMs on every run; nothing is cached locally.
- The Dockerfile: `FROM python:3.11` (floating tag), then `COPY . .`, then `apt-get install` of build tools, then `pip install`, single stage.
- The repo has `.git/` (300 MB) and `ml_fixtures/` (1.3 GB), and no `.dockerignore`.
- What changed: `ml_fixtures/` was added about 3 months ago. Build times grew then.
- No outage, but releases are slow and a hotfix last week took 40 minutes to ship.

**Diagnosis, ranked:**
1. A huge context plus `COPY . .` before the dependency install: every commit busts the dependency layers, and the fixtures ship inside the image.
2. Ephemeral runners: no cache at all, so even a perfect order rebuilds everything.
3. Single stage: compilers and headers ship to production; bigger pulls, more CVEs.

**Checks:** `--progress=plain` output (where `CACHED` stops); `du -sh .git ml_fixtures`; `docker history` (the `COPY` layer ≈ 1.6 GB); runner config (ephemeral?).
**Stabilise:** it's not an outage, so stabilise = keep shipping. Pin the last good image for hotfixes and change one thing at a time.
**Fix:** `.dockerignore`; manifest-first order; multi-stage onto `-slim`; registry cache (`--cache-to/--cache-from type=registry`); cache mounts for pip; pin the base by digest with automated bumps.
**Prevent:** a CI gate on image size; an alert on build-duration p50; a rule that test data never lives in the build context.

### Drill 2: container ignores SIGTERM
**Facts, only if asked:**
- `ENTRYPOINT ["/start.sh"]`; `start.sh` does `. /env.sh` and then `python server.py`, without `exec`.
- `docker top` shows PID 1 as `/bin/sh /start.sh`.
- The app has a handler for `KeyboardInterrupt` (SIGINT, which is what Ctrl-C sends) and nothing for SIGTERM.
- The deploy script runs `docker stop`, then removes the VM from the load balancer, then starts the new container.
- The LB health check runs every 10 s and marks a target unhealthy after 3 failures.

**Diagnosis, ranked:**
1. `sh` is PID 1 and never forwards SIGTERM → 10 s → SIGKILL → 137.
2. Even with `exec`, the app handles SIGINT, not SIGTERM. Ctrl-C proved the wrong signal.
3. Wrong deploy order: the container stops *before* the LB stops sending traffic, so even a graceful app would see 502s.

**Checks:** `docker inspect -f '{{json .Config.Entrypoint}} {{json .Config.Cmd}}'`; `docker exec c cat /proc/1/cmdline`; `grep SigCgt /proc/1/status` (bit 0x4000); `docker kill -s TERM c` then `docker logs c`; the order of steps in the deploy script.
**Stabilise:** pause the rollout. Temporarily deregister from the LB first, wait out the drain, then stop.
**Fix:** `exec` in the script; a SIGTERM handler that stops accepting, drains, then exits 0; deploy order deregister → drain (≥ the LB deregistration delay) → SIGTERM → wait up to the stop timeout (`docker stop -t 30`) → SIGKILL. `STOPSIGNAL` only if the app expects a different signal.
**Prevent:** a CI test that runs the image, sends SIGTERM, and asserts exit 0 within N s; an alert on 137 exits and on 5xx during deploys.

### Drill 3: broken Dockerfiles (fault list; count how many you found)

**A (9 faults):**
1. A real secret in `ENV`, readable by anyone with the image (`docker history`, `docker inspect`). Rotate the password now. Inject it at runtime (secret store / env at run time); for build-time secrets use `--mount=type=secret`. **Most severe.**
2. Runs as root. Add a fixed-UID user.
3. `python:latest`: unpinned and floating; builds aren't reproducible and can jump major versions. Pin a version, ideally by digest.
4. `COPY . .` before `pip install`: every code change reinstalls dependencies. Copy `requirements.txt` first.
5. `apt-get update` in its own `RUN`: a stale cached index, so installs break later. Combine with `install`.
6. No `--no-install-recommends`, apt lists not removed.
7. `build-essential` and `libpq-dev` in the runtime image: bigger and more CVEs. Build wheels in a builder stage; keep only `libpq5` at runtime.
8. Shell-form `CMD`: `sh` may be PID 1 and swallow SIGTERM, and gunicorn's graceful shutdown never runs. Use exec form.
9. Full `python` base (~1 GB) with no `.dockerignore`: the whole context ends up in the image. Use `-slim` and a `.dockerignore`.

**B (5 faults):**
1. The binary is built with cgo on by default in `golang:1.23`, and `net/http` pulls in the cgo DNS resolver, so it's dynamically linked against glibc. Alpine uses musl and has no glibc loader, so the binary can't start: the error says `not found` / `no such file or directory` even though the file is there. Fix: `CGO_ENABLED=0` (static), or a glibc-based runtime image (distroless/base, debian-slim). **Most severe: it never starts.**
2. Shell-form `ENTRYPOINT`: `sh -c` is PID 1, so signals don't reach the server, and `CMD` / run arguments are ignored. Use exec form.
3. `COPY . .` before `go mod download`: every change re-downloads modules. Copy `go.mod`/`go.sum` first, download, then copy the source (or use cache mounts).
4. `USER nobody`: works, but it's a shared UID (65534) used by other things on many hosts; prefer a dedicated fixed UID. (Minor.)
5. No `.dockerignore`. (Minor in this file: the build stage gets thrown away, but the context still goes up to the builder.)
Not a fault: the port is 8080, so the low-port question doesn't apply.

**C (7 faults):**
1. The entrypoint script ignores `CMD` (no `exec "$@"`) and doesn't `exec` node, so `sh` is PID 1 and SIGTERM never reaches the app. **Most severe in production: every deploy drops requests.**
2. Node as PID 1 doesn't handle SIGTERM by default either: the app needs its own handler (or `--init` just to forward the signal).
3. No `.dockerignore`: `COPY . .` copies the Mac's `node_modules` over the image's, and native modules built for macOS crash on Linux.
4. Only `package.json` copied and `npm install` run: the lockfile is ignored, so builds aren't reproducible. Copy `package-lock.json` too and use `npm ci`.
5. Dev dependencies and the full `node:20` base ship to production. Build in one stage, then `npm ci --omit=dev` (or copy `dist/` and production `node_modules`) into a `-slim` stage.
6. `rm -rf src …` in a later layer saves nothing (the files stay in the earlier layer).
7. `RUN chown -R node:node /app` duplicates every file in /app into a new layer, roughly doubling that part of the image. Use `COPY --chown=node:node`.

Gate standard: within 20 minutes, the most severe fault in each file found and ≥ 70% of the faults named with a one-line fix.

---

## K-f. Design: facts and critique rubric (not a design)

**Facts the interviewer gives, only if you ask:** 3,000 VMs; 3 clouds, 9 regions; 1 container per VM; 4 deploys a day; a bad build should reach no more than 5% of capacity; rollback within 10 minutes; requests are short (p99 < 2 s); no local state; a private registry per cloud; VMs can reach the registry but the controller can't SSH into everything.

**I'll critique your drawing against these. A 4 hits most of them unprompted:**
- Requirements turned into numbers on the page: blast radius %, rollback time, deploy rate, fleet size.
- The image is identified by **digest**, not a mutable tag, from build all the way to the hosts. A rollback = a known previous digest.
- A clear control model (a pull agent on each VM is the usual answer to "can't SSH everywhere"), with **desired vs reported version**, reconciled.
- Waves: canary (1 host / 1%) → growing wave sizes → the whole fleet, with bake times. Either spread each wave across regions and clouds, or go region by region, and say why.
- Health gates measured from **outside** the container (LB 5xx, latency, error logs) against the old version's baseline, not just "the container is running". Automatic halt and rollback when a gate fails.
- The per-VM sequence includes **drain before stop**: deregister from the LB → wait → SIGTERM → stop timeout → SIGKILL. That ties back to this week's PID 1 lab.
- Image distribution: pre-pull before the wave's slot, regional mirrors, registry rate limits; don't let 3,000 hosts pull at once.
- Failures: the controller is stateless with the rollout state in a durable store, so it can resume; unreachable hosts are skipped and counted, not waited on forever; a lock or lease so only one rollout runs per service; "fails 20 minutes later" → a longer bake on early waves plus a fast rollback path; the rollback image is kept and pinned in the registry.
- Tradeoffs said aloud: push vs pull; in-place swap vs blue/green on the VM (two containers + LB swap; needs spare memory/CPU) vs new VM images (slowest, cleanest); speed vs safety in wave sizes; and what changes at 10× (a hierarchical controller, more regional mirrors, peer-to-peer image distribution).
- A link to your real work (the 400-VM rolling reboot, the 42+ environment Airflow platform), with a real number from it.

---

## K-g. Flashcard answers

1. **Explain:** Docker sends SIGTERM only to PID 1. If PID 1 is a shell (shell form or a script without `exec`) or an app with no SIGTERM handler, the kernel drops the signal because PID 1 has no default action, so the container gets SIGKILLed after the timeout (exit 137).
2. **Explain:** layers are immutable and stacked, so a later delete only adds a whiteout entry that hides the file. The bytes are still in the earlier layer, and you download them.
3. **Explain:** exec form (`["app", "arg"]`) runs the app directly as PID 1, so it gets signals; shell form runs `/bin/sh -c`, so the shell gets them (and shell-form `ENTRYPOINT` drops `CMD` and run arguments). Exec form doesn't expand variables, so use a script that ends in `exec "$@"` when you need that.
4. **Explain:** namespaces limit what a process can **see** (PIDs, network, mounts, hostname, IPC, cgroups); cgroups limit what it can **use** (memory, CPU, PIDs, IO). Both are features of one shared kernel, which is why a container isn't a VM.
5. **Explain:** only the last stage's layers (plus anything you `COPY --from` earlier stages). Compilers, headers, caches and source stay behind in the build stages.
6. **Command:** `docker exec <c> cat /proc/1/cmdline | tr '\0' ' '` and `docker exec <c> grep SigCgt /proc/1/status` (SIGTERM = bit 0x4000); from outside, `docker top <c>` and `docker inspect -f '{{json .Config.Entrypoint}} {{json .Config.Cmd}}' <c>`.
7. **Command:** `docker history --no-trunc --format '{{.Size}}\t{{.CreatedBy}}' <img>`.
8. **Command:** `docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}}' <c>`, and `dmesg -T | grep -i oom` on the host.
9. **Template:**
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim AS build
WORKDIR /app
RUN python -m venv /venv
COPY requirements.txt .
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
RUN groupadd -g 10001 app && useradd -u 10001 -g app -M -s /usr/sbin/nologin app
WORKDIR /app
COPY --from=build /venv /venv
COPY --chown=10001:10001 . .
USER 10001:10001
ENV PATH=/venv/bin:$PATH PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["python", "app.py"]
```
Plus a `.dockerignore` (`.git`, test data, `__pycache__`, `.venv`). In production, pin the base by digest. This card is the *pattern*. Lab 1 still wants your own version from a blank file, built and measured.
10. **Template:**
```sh
#!/bin/sh
set -e
./scripts/migrate.sh   # setup steps
exec "$@"              # the app (CMD) replaces the shell and becomes PID 1
```
With `ENTRYPOINT ["/entrypoint.sh"]` and `CMD ["python", "app.py"]`.

---

## K-h. Reference cheat-sheet points (compare after writing yours; target ≥ 80% matching)

**Five things:**
1. A container is a process: namespaces for what it sees, cgroups for what it uses, one shared kernel.
2. An image is a stack of immutable layers; the cache reuses steps until the first change, so order steps from stable to volatile.
3. Multi-stage builds ship only what runs: small images pull faster and carry fewer CVEs.
4. PID 1 is special: exec form, `exec "$@"`, a real SIGTERM handler, drain before stop.
5. Run as a fixed non-root UID with capabilities dropped and a read-only rootfs; pin images by digest and rebuild often.

**Commands:** `docker history` · `docker build --progress=plain` · `/proc/1/cmdline` + `SigCgt` in `/proc/1/status` · `docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}}'` · the `/sys/fs/cgroup/{memory,cpu,pids}.max` files · `ls -l /proc/<pid>/ns` · `docker kill -s TERM <c>` · `trivy image --severity HIGH,CRITICAL <img>` or `docker scout cves <img>`.

**Failure modes:**
- Slow builds → cache order or context size; check where `CACHED` stops.
- Stop always takes the full timeout → PID 1 doesn't handle SIGTERM; check `SigCgt`.
- `exec … no such file or directory` with the file present → a dynamic binary on the wrong libc, or a script's `#!` interpreter missing (or CRLF line endings in it); check `file <binary>` / `ldd`.
- Permission denied after going non-root → files owned by root; check `ls -ln`.
- OOMKilled → the cgroup memory limit; check `memory.events`.
- CPU-limit latency → CFS throttling; check `cpu.stat`.
- A secret in history → `ENV` / `ARG` / a copied file; rotate it, then use secret mounts.

**Questions → stories (suggested; your numbers):**
1. "A risky change to a large fleet" → the 400-VM rolling reboot.
2. "A critical CVE across your fleet" → vulnerability remediation, 13,000+ VMs.
3. "Making deploys safer or faster for other teams" → the Airflow platform (200K+ executions a month, 42+ environments).

---

## K-j. Mock interviewer sheet (for Claude on Saturday; don't read)

- **0–5:** "Give me your 90-second intro." Then: "What does load average count?" (W1) and "Which side holds TIME_WAIT, and why does it exist?" (W2).
- **5–40, coding:** LC 979, Distribute Coins in Binary Tree (first try; Week 3 Apply row). Probe: restate, small example, complexity before code, two edge cases. Follow-ups: "The tree is 100,000 deep and skewed. What happens?" and "This is rebalancing load across a tree of nodes. What does an edge's value mean?"
- **40–55, troubleshooting:** "We moved the service into a container on 3 VMs. `docker ps` shows `0.0.0.0:8080->8080/tcp`. From another VM, `curl http://vm1:8080/healthz` fails instantly: `curl: (7) Failed to connect … Connection refused`. Inside the container, a request to `localhost:8080` works." Facts if asked: `docker exec c cat /proc/net/tcp` shows the listener at `0100007F:1F90` (127.0.0.1:8080); the app's default bind address is 127.0.0.1; no firewall changes. Expected: RST = nothing listening on the address the traffic reaches (W2); the app is bound to the container's loopback, and the published port DNATs to the container's eth0 address (W3 network namespace); fix = bind 0.0.0.0; prevent = health checks from outside the namespace. Escalation if time: "Fixed. Now under load it exits 137 every ~20 minutes" → `OOMKilled`, cgroup memory limit.
- **55–70, mini design:** "A critical OpenSSL CVE hits this service's base image. Get a rebuilt image onto all 400 VMs within 24 hours without dropping requests." Listen for: scope via SBOM/scan, rebuild with `--pull` and pin the new digest, waves with health gates, drain-before-stop, verifying with a scan after the rollout, stragglers and exceptions, reporting % done. Link to the 400-VM reboot story.
- Score each area 1–4 with timestamps; every stall → an error-log row + one drill.

---

## K-k. Story reference beats (coverage check only)

A strong answer covers:
1. **Inventory:** an SBOM or package inventory per image and host, so "who's affected?" is a query, not a hunt.
2. **Priority:** severity plus exploitability (known exploited, internet-facing, reachable code), not CVSS alone.
3. **Two paths:** container images get rebuilt from a patched base and redeployed (never patched in place); VMs get patched through config management or replaced from a new VM image.
4. **Safe rollout:** canary, then waves, health gates, a pause button; reboots coordinated with capacity.
5. **Proof:** a re-scan after rollout; a dashboard of % remediated per severity; exceptions with an owner and an expiry date.
6. **The metric upward:** time to remediate per severity, and % of the fleet within the SLA.
