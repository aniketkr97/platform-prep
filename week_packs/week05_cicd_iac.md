# WEEK PACK — Week 5: CI/CD and infrastructure as code

Infra layer: pipelines, caching, hermetic builds, promotion and rollback, Terraform state and locking, drift, Ansible idempotency, release engineering · Code: BFS/DFS, Kahn's topological sort, union-find, then bridges, two-level topological sort and two-class DSU · Design: CI/CD system with canary and rollback · Story: replacing Jenkins with the Airflow platform

**Rule for this file:** do every section cold first. Every answer, note, reference and interviewer sheet is in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section. There is no LeetCode code anywhere in this file. Problems go through the hint ladder one rung at a time, in session. The template reference in K1 is generic, and you open it only if your drill fails (see §1).

Lab starter files: `week_packs/week05_lab/` (lab1_pipeline, lab2_terraform, lab3_ansible). Labs 2 and 3 were run end to end on this Mac on Nov 6 (Terraform 1.17.1, ansible-core 2.22.0), and their expected output in K3 is what I actually saw. The cache and test stages of Lab 1 were run too. Its Kubernetes stages were **not** run, because Docker isn't installed here yet, so that part of K3 is expected output, not observed.

---

## 0. This week's plan

### 0a. Dates and tools

- **Week 5 runs Mon Nov 16 – Sun Nov 22.** The Week 4 pack moved Week 4 to Nov 9–15, and this follows it. If you're on a different week, tell me and I'll shift every date.
- **Knock-on:** Gate 2 (suggested Sat Nov 28 in the Week 4 pack) now falls in Thanksgiving week, which is Week 6. The plan's "lighter week" rule moves from Week 7 to Week 6.
- **Tools:** none of `docker`, `kind`, `kubectl`, `terraform` or `ansible` is installed on this Mac. Step 0 of the lab (§3) installs them Monday night. If you never did Week 4's Step 0, it's included.

### 0b. Reviews pulled from Weeks 1–4 (do these before anything new)

**Where the dates come from:** the review tables in the Week 2, 3 and 4 packs, assuming **every redo was Clean on its planned day**. No redo result has been logged since Oct 19: the tracker's review queue is blank, and Weeks 3–4 haven't happened yet. One Shaky or Failed mark moves a row, so **send me your marks before Mon Nov 16** and I'll recount.

| Day | Due from Weeks 1–4 (problems, ≤ 25 min each) | Count | Cap |
| --- | --- | --- | --- |
| **Mon Nov 16** | W4 R2: **56\***, **215\***, 253 · W3 R3: **124\***, 102, 98, 1114 · W2 R4: **71\***, 1438 | **9** | **Over 5: no new problem** |
| Tue Nov 17 | W2 R4: 2398 · W3 R3: 2581 · W4 R2: 1882 | 3 | ok |
| Wed Nov 18 | W2 R4: 410 · W3 R3: 979 (W3 mock) · W4 R2: W4 mock problem | 3 | ok |
| Thu Nov 19 | W2 R4: **146\***, **20\***, 739 | 3 | ok |
| Fri Nov 20 | W4 R3: 1834 (+ W4-T1/T2 if that drill failed) | 1 | ok |
| Sat Nov 21 | W4 R3: 630, 295 | 2 | ok |
| Sun Nov 22 | W4 R3: 220, 355 | 2 | ok |

\* shaky by history (5+ submits, or old and slow): do these first in their morning.

- **Week 1:** nothing falls in Week 5. Its R4s are Nov 12–14 and its R5s are Dec 12–14. The 2444 result is still unknown.
- **Error log F1–F8:** all three reps ended Nov 1. Nothing is due.
- **If you can't finish Monday's 9:** carry at most **2** to Tuesday, and make them the W2 R4s (1438, 71). A late R4 is harmless, because a longer gap is a harder test. Tuesday then sits at 5 and its new problems still run. If the W5 template drill fails too, carry only 1.
- **If the Week 1–2 redos never happened:** every one of them is at Review 1 today. Missed reviews don't stack, so each gets one redo, and that redo counts as Review 1. Feed them in at most 5 a morning. New Week 5 problems wait until a morning shows 5 or fewer. Tell me and I'll rebuild §0d.

**Concept reviews from Week 4 (2–5 min each, recall warm-up slot, don't count toward the cap):**
- Mon: Labs 3–4 predictions, fleet-upgrade story
- Tue: Drill 2 (OOM), multi-tenant design redraw
- Wed: Week 4 cards, Drill 3 (stuck rollout)
- Sat: Labs 1–2 predictions
- Sun: T1–T3 teach-backs, Drill 1 (CrashLoopBackOff)

### 0c. This week's problems

| # | Problem | Diff | Role | Your history (LeetCode, Oct 6) | How it's run |
| --- | --- | --- | --- | --- | --- |
| 200 | Number of Islands | M | Core | Apr 2026, **5 submits (shaky)** | Cold redo, ≤ 25 min, first in its day |
| 210 | Course Schedule II | M | Core | Sep 2026, **5 submits (shaky)** | Cold redo, ≤ 25 min, first in its day |
| 684 | Redundant Connection | M | Core | Sep 2026, 3 submits | Cold redo, ≤ 25 min |
| 127 | Word Ladder | H | Core | May 2026, **10 submits (shaky)** | Cold redo **inside Saturday's mock**, 35 min, timed and recorded |
| 1192 | Critical Connections in a Network | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 1203 | Sort Items by Groups Respecting Dependencies | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 1579 | Remove Max Number of Edges to Keep Graph Fully Traversable | H | Required · Apply | New | First try, 50 min |
| 2349 | Design a Number Container System | M | Required · practical | New | **Moves to Week 6** (cap math below) |
| 2360 | (Friday check: don't open it before Friday) | H | Check | New | 45 min, alone, no hints, Friday |

**Why 2349 slides to Week 6:** each first try adds a review the next day and another three days after that. With Week 1–4 reviews filling the mornings, the week has room for only 6 first tries besides the check and the mock, and still keeps every morning through Mon Nov 23 at 5 or fewer. The plan's order is core first, then required, so the last required row, 2349, slides. I'll place it when I build Week 6.

**After-required rows (Week 6 extras, not this week):** 2392 and 685 are new. 2050, 1857, 310 and 815 are old solves from Sep 2026, so each gets a cold redo. None fits under this week's cap.

⚠ **The coding page's Week 5 template ("Tarjan bridges") is a worked solution to 1192.** Don't open it before your 1192 first try, or the try counts as "Needed the solution". The **Graphs for the NVIDIA Loop** page has traversal, topo-sort and DSU material: keep it closed until 200, 210 and 684 are redone.

### 0d. Day by day

| Day | Reviews first | Infra / apply | Code (new) | Other |
| --- | --- | --- | --- | --- |
| **Mon Nov 16** | **9** (§0b), shaky first | §A warm-up cold (10) → §2 questions cold → read → K2 (45) | §1 template drill (15). **No new problem: 9 due** | §3 Step 0 install (30) |
| **Tue Nov 17** | 3 (+ ≤ 2 carried) | §3 **Lab 1**: pipeline, cache, canary (70) | **200\*** cold redo → **1192** (Learn) | Recall warm-up (10) |
| **Wed Nov 18** | 3 + 200, 1192 (R1) = **5** | §5 teach-backs T1–T4, recorded (25) · §6 **Drill 1** (30) | **210\*** cold redo → **1203** (Learn) | — |
| **Thu Nov 19** | 3 + 210, 1203 (R1) = **5** | §3 **Lab 2** Terraform (40) + **Lab 3** Ansible (20) · cheat sheet from memory (30) · §8 story (20) | **684** cold redo → **1579** | — |
| **Fri Nov 20** | 1 + 684, 1579 (R1) = 3 | §7 design: **your drawing first** (40) · §6 **Drill 2** (30) | **2360** check, 45 min, alone | — |
| **Sat Nov 21** | 2 + 200, 1192 (R2) + 2360 (R1) = **5** | §9 **75-min full-loop mock** (coding = **127**) · design redrawn from memory (90) · §6 **Drill 3** timed 20 min · debrief (45) | 127 (in the mock) | — |
| **Sun Nov 22** | 2 + 210, 1203 (R2) + 127 (R1) = **5** | Cheat sheet rewritten from blank (30) · job pipeline (45) · plan Week 6 (15) | **None.** A first try today would put Mon Nov 23 at 6 | Spare: retake the template drill if it failed |

**Mon Nov 23 check:** 684, 1579 (R2) + 215, 56, 253 (W4 R3) = 5. That's at the cap, so Week 6 can open with its Learn row.

**Hours:** about 22–25 this week if every review takes 20 minutes, against the plan's 15. Reviews alone are 35 redos. Aim for 10–15 minutes on any R3+ redo of a problem you know. If time runs short, cut in this order: Lab 3 → Drill 3 → design redraw shortened to 45 min → Thursday story practice (move it to Sunday). **Never cut:** reviews, the Learn rows, the check, the mock, Labs 1–2.

### 0e. Session rules (same as Weeks 2–4)

- Say **"start 1192"** (or any number) and I log the start time. 60-second approach aloud, brute force first, complexity before code ("Real Engineers Always Build Code Tests Often").
- Hints: one rung per request (pattern → data structure → key insight → skeleton), only after 25 min stuck. A Learn row gets the full 40 minutes first. No hints in the Friday check. Ask for a solution and you get the next rung.
- I compile your file with `clang++ -std=c++17 -Wall -Wextra` and show compile errors. I never fix or rewrite your code.
- Marks: first tries **Solved alone / Needed the solution**. Redos **Clean** (first submit, < 25 min, no hint) / **Shaky** (slow, 2+ submits, or one hint) / **Failed**. R2 adds a twist: change one constraint and say what breaks. R3 is recorded with two edge cases traced.

---

## A. Day 1 recall warm-up (cold, aloud, before any reading)

10 questions: 7 Week 5 (you haven't read anything yet, so answer from experience) and 3 from earlier weeks. One or two sentences each. Mark each ✓ / ✗ before opening KA.

1. Your pipeline builds the Docker image again for staging and again for prod. Name two ways that hurts you.
2. What is a hermetic build? Name two things that make a build non-hermetic.
3. A CI cache key is `deps-${branch}`. What goes wrong, and what should the key contain instead?
4. Canary, blue-green, rolling update: one sentence each on how traffic moves, and what a rollback costs.
5. What does Terraform state hold, and why must two applies never write it at the same time?
6. A teammate changed a security group in the cloud console during an incident. What does Terraform call that, and what happens on the next `terraform apply`?
7. You run an Ansible playbook twice. What should the second PLAY RECAP say, and which kind of task usually breaks that?
8. *(Week 4)* `kubectl rollout status` exits with `ProgressDeadlineExceeded`. Two likely causes, and your first command.
9. *(Week 3)* Why does putting `COPY requirements.txt` before `COPY . .` make CI builds faster?
10. *(Week 1)* You `kill -9` a process that has a child running. What happens to the child? What does that imply for a `terraform apply` killed mid-run?

---

## 1. C++ template drill (Monday, blank file, 15 min, compiled)

**Templates:** W5-T1 multi-source BFS · W5-T2 iterative DFS components · W5-T3 Kahn's topological sort with layers · W5-T4 union-find.

**Format:**
1. Timer on, blank `w5_templates.cpp`. No notes, no autocomplete. Write the headers yourself (no `<bits/stdc++.h>` on Apple clang).
2. Write the four templates and a `main()` with `assert`s that prove every behaviour below. You write the asserts.
3. Say "compile" and I run `clang++ -std=c++17 -Wall -Wextra w5_templates.cpp && ./a.out`.

| # | Signature (yours to match) | Behaviour your asserts must prove |
| --- | --- | --- |
| T1 | `vector<int> bfsDist(const vector<vector<int>>& adj, const vector<int>& sources)` | Fewest edges from the **nearest** source, `-1` if unreachable. A duplicated source doesn't break it |
| T2 | `pair<vector<int>,int> components(const vector<vector<int>>& adj)` | Component id per node, plus the count. **No recursion.** |
| T3 | `pair<vector<int>,int> kahn(int n, const vector<pair<int,int>>& edges)` | A valid order and the number of **layers** (groups that could run in parallel). Empty order on any cycle, self-loops included |
| T4 | `struct DSU { int find(int); bool unite(int,int); int size(int); int comps; }` | `unite` returns `false` when the two are already connected. Path compression and union by size |

**Test data (build these in `main`):**
```
G   (undirected, n = 7): 0-1, 1-2, 2-3, 4-5        (6 is alone)
bfsDist(G, {0})    == {0,1,2,3,-1,-1,-1}
bfsDist(G, {0,3})  == {0,1,1,0,-1,-1,-1}
bfsDist(G, {6})    == {-1,-1,-1,-1,-1,-1,0}
bfsDist(G, {0,0})  == {0,1,2,3,-1,-1,-1}
components(G).count == 3; 0 and 3 share an id; 4 and 5 share an id; 0, 4, 6 all differ

CHAIN (undirected path 0-1-...-199999): components count == 1; bfsDist(CHAIN,{0})[199999] == 199999

D   (directed, n = 6): 0->1, 0->2, 1->3, 2->3, 3->4  (5 has no edges)
kahn(6, D): every edge u->v has u before v; all 6 nodes present; layers == 4
kahn(4, {0->1, 1->2, 2->0}).order is empty      (node 3 is free, still empty)
kahn(2, {0->0}).order is empty                  (self-loop)
kahn(1, {}) == ({0}, 1)
kahn(3, {0->1, 0->1}): valid order, layers == 2 (duplicate edge)

DSU(5): unite(0,1) && unite(1,2); !unite(0,2); comps == 3; size(2) == 3; size(4) == 1; find(3) != find(0)
        unite(3,4) → comps == 2
DSU(200000): unite(i, i+1) for all i → comps == 1; find(0) == find(199999); size(7) == 200000
```

**Then answer aloud:**
1. T1: why mark a node visited when you **push** it, not when you pop it? What breaks the other way?
2. T2: why must T2 avoid recursion for CHAIN? What actually happens on this Mac if it recurses?
3. T3: how does Kahn's detect a cycle? What's left in the graph when it stops early?
4. T3: what do "layers" mean for a CI pipeline's job graph?
5. T4: the cost per operation with both optimizations, and with only one of them?
6. Can union-find detect a cycle in a **directed** graph? Why not?
7. When would you pick union-find over BFS to answer "are a and b connected?"

**Pass** = under 15:00, zero warnings, every assert passes, no lookups. **Fail** = any of those missed, and the template goes on the review schedule like a problem (row in §9b). **If you pass, don't open K1 this week.** If you fail, read K1 once Monday, close it, and retype from blank Tuesday. That retype is its Review 1.

### 1b. The problems: one question to answer before you code

No pattern names here. They're rung 1 of the hint ladder.

| # | Say this before any code | Mark |
| --- | --- | --- |
| 200 | What do you do to a land cell the moment you first see it, and why then rather than later? | |
| 210 | At the end, how do you know whether an order exists at all? | |
| 684 | Which single fact about an edge's two endpoints, checked **before** adding the edge, proves it's redundant? | |
| 127 | What's a node, what's an edge, and what does the obvious way to find neighbours cost for 5,000 words of length 10? | |
| 1192 | What would you need to know about everything below v in a DFS to prove that (u, v) is the only link to it? | |
| 1203 | Groups must stay contiguous. What does a dependency between two items in **different** groups say about the groups? | |
| 1579 | Which edges should you add first, and why can that order never make the answer worse? | |
| 2360 | **Sealed until Friday** | |

---

## 2. Infra brief (Monday: questions cold, then read, then K2)

**Read:** Terraform docs *State*, *State: Locking*, *Backend Type: s3* (the `use_lockfile` section), the `terraform force-unlock` command page, and *Refresh-only mode* (under `terraform plan`). Ansible docs *Validating tasks: check mode and diff mode* and *Handlers: running operations on change*. Google SRE book **Chapter 8, Release Engineering**. Optional: SRE Workbook **Chapter 16, Canarying Releases**. Search the titles if a link moved.

**Before reading, answer from memory** (1–2 sentences each):

*Terraform state and locking*
- B1. What does state hold besides each resource's attributes? Which of it is dangerous to leak?
- B2. How does each of these lock: the local backend, S3 today, S3 the older way, GCS?
- B3. `-lock-timeout=60s` vs `-lock=false`: what does each do, and when is the second acceptable?
- B4. What does `terraform force-unlock` **not** do? Can it unlock a local state file held by another process?
- B5. `plan -refresh-only`, `apply -refresh-only`, `plan -detailed-exitcode`: what does each do, and what are the exit codes of the last one?

*Ansible*
- B6. `command` vs `shell`: what's the difference? Name three ways to make either one idempotent.
- B7. When do handlers run? What happens to a notified handler if a later task on that host fails?
- B8. What does `--check` do with `command` and `shell` tasks? Why does that matter?

*Release engineering (SRE ch. 8, Workbook ch. 16)*
- B9. The four principles of release engineering in the SRE book.
- B10. How does Google handle a fix that a release branch needs? Which direction does code never flow?
- B11. Why is a config change released like a binary?
- B12. Why compare the canary to a **control group** running at the same time, rather than to "before the deploy" or to the whole fleet?

**Then write your own "5 things I'd say about CI/CD and IaC" here, before opening K2:**

1.
2.
3.
4.
5.

**Failure modes (fill Cause and First check, then compare with K2):**

| Symptom | Cause | First check |
| --- | --- | --- |
| Every PR is green; `main` is red on the same job | | |
| Cache HIT, tests green, but the deployed build has the wrong dependency version | | |
| Same commit, built twice, two different image digests | | |
| Canary passed; at 100% the error rate climbs an hour later | | |
| `Error acquiring the state lock`, and the lock's `Created` time is hours old | | |
| `terraform plan` wants to change something nobody touched in code | | |
| An apply was killed; the next apply fails with "already exists" | | |
| Ansible's second run shows `changed=2`, and the service restarts every run | | |
| `--check` says `changed=0`, but the real run changes things | | |

---

## 3. Hands-on lab (Tuesday Lab 1, Thursday Labs 2–3; real commands, write what you see)

Write a prediction before each command, then what you observed. Expected output and what each step proves are in **K3**.

### Step 0: install and verify (Monday night, ~30 min)

```bash
# Skip any line whose tool is already installed (Week 4 Step 0 covers the first three)
brew install colima docker kind kubectl
colima start --cpu 4 --memory 8
brew tap hashicorp/tap && brew install hashicorp/tap/terraform
brew install ansible
terraform version            # Terraform v1.1x
ansible --version | head -1  # ansible [core 2.x]
kind create cluster --name w5
kubectl get nodes
```

Homebrew's own `terraform` formula stopped at 1.5.7 after the license change, so use HashiCorp's tap.

### Lab 1: a pipeline with a cache and a canary step (Tuesday, ~70 min)

```bash
cd "week_packs/week05_lab/lab1_pipeline"
cp pipeline.sh pipeline.sh.orig        # you'll break it on purpose; this restores it
```

Read `pipeline.sh` first (5 min). Say each stage aloud: what it does, what it caches, what it ships.

**L1a. Cold and warm cache (no Docker needed).**
```bash
./pipeline.sh --ci-only
./pipeline.sh --ci-only
```
Prediction (HIT or MISS, and the time for `deps`, each run): ______ Observed: ______

**L1b. Change an input.** Edit `app/requirements-dev.txt` to `pytest==8.3.5`, then run `./pipeline.sh --ci-only`.
Prediction: ______ Observed: ______

**L1c. Break the key on purpose (the "fails only on main" class).**
```bash
rm -rf .cache
sed -i '' 's|^CACHE_KEY=.*|CACHE_KEY="deps-main"|' pipeline.sh     # a branch-scoped key, like deps-${branch}
sed -i '' 's/pytest==8.3.5/pytest==8.3.3/' app/requirements-dev.txt
./pipeline.sh --ci-only
sed -i '' 's/pytest==8.3.3/pytest==8.3.5/' app/requirements-dev.txt
./pipeline.sh --ci-only
.cache/deps-main/bin/pytest --version ; cat app/requirements-dev.txt
cp pipeline.sh.orig pipeline.sh                                    # restore the correct key
```
Prediction: HIT or MISS on the second run? Which pytest is installed? ______ Observed: ______

**L1d. First full run: bootstrap stable.**
```bash
./pipeline.sh
kubectl get pods -l app=web -L track
```
Prediction: how many pods, and on which track? ______ Observed: ______

**L1e. Ship a change with no gate written yet.** Change the body text in `app/server.py` (`"hello from"` → `"hi from"`), then run `./pipeline.sh`.
Prediction: does it promote? ______ Observed: ______

**L1f. Write `canary_gate.sh` (20 min, yours to write).** The pipeline calls it after the bake with `CANARY_VERSION` and `STABLE_VERSION` set. Spec:
- Optional env: `REQUESTS` (default 300), `MAX_ERROR_RATE` (default 0.05), `MIN_SAMPLES` (default 15).
- Send `REQUESTS` requests to the `web` Service **from inside the cluster**. This traffic generator prints one `<status> <version>` line per request:
  ```bash
  kubectl run "load-$RANDOM" -i --rm --restart=Never --quiet \
    --image=curlimages/curl:8.10.1 --command -- sh -c \
    "for i in \$(seq $REQUESTS); do curl -s -o /dev/null -w '%{http_code} %header{x-version}\n' http://web/; done"
  ```
  kubectl may add its own lines to the output, so keep only lines matching `^[0-9]{3} `.
- For each version, count the samples and the 5xx responses.
- Print exactly one line: `gate canary=<v> n=<n> err=<e> rate=<r> | stable n=<n> err=<e> rate=<r> -> PASS|FAIL`
- Exit 0 **only if** the canary has at least `MIN_SAMPLES` samples **and** its error rate is ≤ `MAX_ERROR_RATE`. Anything else exits 1.
- `chmod +x canary_gate.sh`. Check its output format by hand once: `CANARY_VERSION=<stable tag> STABLE_VERSION=<stable tag> ./canary_gate.sh` (the stable tag is in `releases.log`).

**L1g. Ship a good change through the gate.** Run `./pipeline.sh` again (the L1e change is still there).
Prediction: roughly what share of requests reach the canary, and why? ______ Observed (your gate line): ______

**L1h. Ship a bad change.** In `app/server.py`, change the `FAIL_RATE` default from `"0"` to `"0.3"`. Then:
```bash
./pipeline.sh ; echo "exit=$?"
cat releases.log
kubectl get deploy -L track
```
Prediction: do the unit tests catch it? Does the readiness probe? Does the gate? ______ Observed: ______

**L1i. Skip the canary, then roll back by hand.**
```bash
docker images web                                   # find the bad tag from L1h
sed "s/IMAGE_TAG/<bad-tag>/g" k8s/stable.yaml | kubectl apply -f -
kubectl rollout status deploy/web-stable
kubectl rollout history deploy/web-stable
kubectl rollout undo deploy/web-stable && kubectl rollout status deploy/web-stable
```
Prediction: how long does the undo take, and why is it that fast? ______ Observed: ______

Finally, revert `server.py` to `FAIL_RATE "0"` and the original body text.

### Lab 2: break Terraform state locking on purpose, then drift (Thursday, ~40 min)

Use three terminals, all in `week_packs/week05_lab/lab2_terraform`. Read `main.tf` first: `local_file.app_config` stands in for real infrastructure, and `terraform_data.slow_rollout` sleeps so an apply holds the lock.

**L2a. Init and a first apply.**
```bash
terraform init
terraform apply -auto-approve -var slow_seconds=1
cat out/app.conf ; terraform state list
```

**L2b. Two applies at once (local backend).**
- Terminal A: `terraform apply -auto-approve -var replicas=4 -var slow_seconds=40`
- Terminal B, within 40 s: `terraform plan -var replicas=4`, then `cat .terraform.tfstate.lock.info`

Prediction: ______ Observed (copy the `Error message:` line and `Operation:`): ______

**L2c. Wait for the lock instead.** A: `terraform apply -auto-approve -var replicas=5 -var slow_seconds=40`. B, while A runs: `time terraform plan -var replicas=5 -lock-timeout=60s`
Prediction: ______ Observed: ______

**L2d. Kill an apply mid-run (local backend).**
- A: `terraform apply -auto-approve -var replicas=6 -var slow_seconds=60`
- B, after "rollout start" appears in A:
  ```bash
  pkill -9 -f "terraform apply"
  ls -la .terraform.tfstate.lock.info
  pgrep -fl "sleep 60"
  cat out/app.conf
  terraform plan -var replicas=6
  ```
Prediction: is the state still locked? Is anything still running? What does the plan want to do? ______ Observed: ______
Clean up: `pkill -f "sleep 60"`

**L2e. Move state to a remote backend with a lock that outlives the process.**
- Terminal C: `python3 lock_server.py` (leave it running and watch its log)
- B:
  ```bash
  cp backend_http.tf.example backend.tf
  terraform init -migrate-state          # answer: yes
  ls store ; wc -c terraform.tfstate
  terraform apply -auto-approve -var replicas=3 -var slow_seconds=1   # a clean, complete remote state
  ```

**L2f. Kill an apply again, now with the remote backend.**
- A: `terraform apply -auto-approve -var replicas=7 -var slow_seconds=60`
- B, after "rollout start":
  ```bash
  pkill -9 -f "terraform apply" ; pkill -f "sleep 60"
  terraform plan -var replicas=7
  cat store/lock.json
  ```
Prediction: ______ Observed: ______

Before you unlock, say aloud the two things you'd confirm in production. Then:
```bash
terraform force-unlock <ID from the error>      # answer: yes
terraform plan -var replicas=7
cat out/app.conf
```
Prediction: why does the plan want to **create** a file that exists? ______ Observed: ______

**L2g. Drift.**
```bash
terraform apply -auto-approve -var replicas=3 -var slow_seconds=1
terraform plan -detailed-exitcode -var replicas=3 ; echo "exit=$?"
echo "replicas=9" > out/app.conf                 # someone "fixed it in the console"
terraform plan -refresh-only -var replicas=3
terraform plan -detailed-exitcode -var replicas=3 ; echo "exit=$?"
```
Prediction (both exit codes): ______ Observed: ______
Say aloud the three ways to resolve drift, and when you'd pick each.

Clean up: `terraform destroy -auto-approve -var slow_seconds=1`, then stop the lock server (Ctrl-C in C).

### Lab 3: Ansible idempotency (Thursday, ~20 min)

```bash
cd week_packs/week05_lab/lab3_ansible
ansible-playbook -i inventory.ini site.yml
ansible-playbook -i inventory.ini site.yml
cat out/app.conf
ansible-playbook -i inventory.ini site.yml --check --diff
```
Prediction (the `changed=` count on each of the three runs, and the file's contents): ______ Observed: ______

**Then fix it yourself:** `rm -rf out`, and edit `site.yml` until **run 2 shows `changed=0`** and the handler doesn't run on run 2. Keep the "release marker" task, but stop it from reporting a change. Compare with K3 only after it works.

---

## 4. Flashcards (10 new cards: put them in Anki; backs in K4)

1. **Explain:** Why promote one artifact through environments instead of building per environment?
2. **Explain:** What makes a CI cache key correct, and what are the two ways it goes wrong?
3. **Explain:** Canary vs blue-green vs rolling update: when do you pick a canary?
4. **Explain:** How do you roll back a release that included a database schema change?
5. **Command:** Detect Terraform drift in a nightly job and fail the job when there is drift.
6. **Command:** A crashed CI job left a stale Terraform lock. Your steps, in order, with the command.
7. **Command:** A resource exists in the cloud but not in Terraform state. Bring it under management.
8. **Command:** Prove an Ansible playbook is idempotent, and name the trap in `--check`.
9. **Template:** Kahn's topological sort skeleton, with cycle detection.
10. **Template:** Union-find `find` with path compression and `unite` by size.

---

## 5. Teach-back prompts (Wednesday: 2 minutes each, recorded, no notes)

Record each cold, listen once, redo it if you stumble more than five times. Outlines and follow-up answers are in **K5**. Read them only after your first recording.

**T1. Hermetic builds and caching.** "How do you make CI builds fast without making them wrong?"
1. Your build passes on your laptop and fails in CI. Your first three suspects?
2. How would you prove a build is reproducible?
3. When is a partial cache match (`restore-keys`) safe, and when is it dangerous?
4. What's cache poisoning, and how do you prevent it?
5. CI runners are ephemeral, so the Docker layer cache is empty every time. Now what?

**T2. Promotion and rollback.** "Walk me through how a commit gets to production safely, and how you undo it."
1. Rolling update, blue-green or canary: which one, when?
2. The release ran a database migration. How do you roll back?
3. Which metrics does your canary gate on, and what happens if there's no data?
4. The canary passed, but the problem showed up at 100% two hours later. Why, and what do you change?
5. What's the difference between deploying and releasing?

**T3. Terraform state, locking and drift.** "What is Terraform state, why does it need a lock, and what is drift?"
1. Two engineers run `apply` at once with no lock. What exactly can go wrong?
2. A CI job died while holding the lock. Your steps?
3. How do you find drift across 200 stacks?
4. Someone fixed an outage in the console. Now what?
5. How do you split state across stacks, and why?

**T4. Idempotent configuration.** "What does idempotent mean in config management, and why does it matter for a fleet?"
1. What makes a task idempotent?
2. Why do non-idempotent tasks hurt on 13,000 VMs?
3. Ansible vs Terraform: what does each own?
4. How do you roll an Ansible change across a fleet safely?
5. Mutable configuration vs immutable images: when do you pick each?

---

## 6. Troubleshooting drills (symptoms only)

Answer in your routine, aloud, as to an interviewer: **Clarify → Scope → Stabilise → Hypothesise → Check → Fix and prevent** ("Can Some Students Handle Cold Fixes"). Ask me questions as you go, and I answer from the interviewer sheet in K6, which you don't read. I score each step afterwards. Your Week 2 error log says you tend to stop at the cause and skip Check and Fix: say a command and its expected output for every hypothesis.

### Drill 1: the pipeline fails only on main (Wednesday, 30 min)

Monday 10:40. The `main` pipeline for the `payments-client` repo has been red since 09:15. Every PR pipeline is green, including the two PRs merged this morning: #481 at 09:02 and #483 at 09:10. The failing job is `integration-tests`, which runs the same way on PRs and on main. The error is:

```
tests/test_retry.py::test_backoff_on_timeout FAILED
TypeError: connect() got an unexpected keyword argument 'timeout_ms'
```

Re-running main fails the same way. Nobody changed the CI config this week. Two other teams are blocked because they deploy from main. A teammate says "the CI cache is corrupted again" and wants to clear every cache. Another wants to revert both PRs.

### Drill 2: Terraform state lock and drift (Friday, 30 min)

Friday 02:10. The nightly `terraform apply` for the `prod-network` stack failed after 10 minutes:

```
Error: Error acquiring the state lock
Error message: operation error S3: PutObject, https response error StatusCode: 412, PreconditionFailed
Lock Info:
  ID:        6c1e0d3a-...
  Path:      tf-state-prod/network/terraform.tfstate
  Operation: OperationTypeApply
  Who:       runner@ci-7f9c
  Version:   1.17.1
  Created:   2026-11-19 23:47:12 UTC
```

The on-call engineer wants to run `terraform force-unlock` and re-run the apply right now. Last week's drift report for this stack showed one unexplained change. At 09:00 there is a planned change to this stack that the payments team is waiting on.

### Drill 3: the rollout stalls (Saturday, timed 20 min)

Saturday 14:05. A release of `checkout` started at 13:10. Its pipeline normally finishes in 25 minutes. The deploy tool shows:

```
release checkout 2026.11.21-3   step 2/6   canary weight 10%
analysis: success-rate   measurements 0/5   status: waiting
analysis: p99-latency    measurements 0/5   status: waiting
```

`kubectl get pods -l app=checkout` shows every pod `Running` and `1/1` ready. A product manager asks you to "just promote it": the release has a fix customers are waiting for.

---

## 7. Design prompt: CI/CD system with canary and rollback (Friday drawing, Saturday redraw)

**Prompt:** "Design the build-and-deploy system for a company with 300 engineers and about 400 services on Kubernetes in 3 regions. There are about 1,500 merges a day. Every change should reach production the same day, behind a canary with automatic rollback. Rollback must take under 5 minutes."

**Your drawing first (40 min, on paper, timed).** Walk the six steps: **"Real Apps Deserve Deep Failure Tests."**

1. **Requirements:** functional and non-functional. Do the scale math aloud: pipeline runs per day, runs per minute at peak, runner cores, registry storage per day.
2. **API:** what does an engineer or a bot call to start, watch, promote, abort and roll back a release?
3. **Data:** which records exist (release, step, analysis run, artifact, lock, audit)? What's the state machine of a release?
4. **Deep dive:** pick **one**: the canary analysis engine, **or** the release orchestrator that survives its own crash mid-rollout.
5. **Failures:** at least five, each with what the system does by itself.
6. **Tradeoffs:** at least three, plus what changes at 10× the merges.

Then compare with the outline in **K7** and mark every line you missed. Saturday: redraw from blank without looking. Gate 2 asks for this design in 45 minutes.

---

## 8. Story scaffold: replacing Jenkins with the Airflow platform (Thursday, 20 min)

**Rule:** only facts you give me. Every blank stays blank until you fill it. I won't suggest numbers.

**What I already have from you:** an Airflow orchestration platform running 200K+ executions a month across 42+ environments and 13,000+ VMs. I don't know which company it was at, or anything about the Jenkins side.

**Facts I need from you first:**
- Which company, which years? Your role, and the team size?
- What did Jenkins run: how many jobs, of what kind (deploys, patching, reboots, data jobs)? What hurt?
- Why Airflow, and which alternatives did you reject (Argo Workflows, Rundeck, Temporal, staying on Jenkins)?
- How did you migrate: big bang, or parallel runs? How long did it take?
- What broke, or nearly did, during or after the migration?
- Before and after numbers: failure rate, run time, on-call pages, onboarding time, or anything else you measured.

**Structure (2 minutes spoken, then stop):**

| Beat | ~Time | Your words |
| --- | --- | --- |
| **Situation**: what Jenkins ran, at what scale, and what hurt | 25 s | |
| **My decision**: what you chose and the one or two things you built yourself | 35 s | |
| **Tradeoff**: the option you rejected and what your choice cost you | 25 s | |
| **Number**: one or two results (executions, environments, VMs, plus a before/after you measured) | 15 s | |
| **Lesson**: one specific thing you'd do differently | 20 s | |

**Interviewer probes (practise each in ≤ 30 s):**
1. Airflow is a data-pipeline scheduler. Why use it for infrastructure jobs?
2. What didn't fit Airflow's model, and how did you work around it?
3. How did you move hundreds of Jenkins jobs without breaking the teams that relied on them?
4. A task fails halfway through on 300 VMs. What does a retry do? Is that safe?
5. How did you make the scheduler itself highly available? What happened when it went down?
6. How do secrets get to tasks?
7. How did you know the migration worked? Which number would you show your VP?
8. What would you build differently today?
9. Who disagreed with the move, and how did you handle it?
10. How does this compare to a CI/CD system like the one you designed in §7?

---

## 9. Saturday mock, review tables, cheat sheet

### 9a. Mock: full loop, 75 minutes, recorded

About 70% Week 5 and 30% Weeks 1–4. I'm the interviewer and run it from the sealed sheet in K9. You don't read K9.

| Time | Block | Content |
| --- | --- | --- |
| 0–5 | Intro | Your 90-second introduction |
| 5–40 | Coding | **127 Word Ladder**, cold, 35 min. 60-second approach, brute force first, your own tests. It counts as 127's first redo |
| 40–55 | Design | A 15-minute Week 5 design question (sealed) |
| 55–70 | Troubleshooting | One scenario mixing CI/CD with Weeks 1–4 (sealed) |
| 70–75 | Your questions | Two questions you'd ask a real interviewer |

**Scorecard (1–4 per area, with evidence):**

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

**Debrief (within an hour):** (1) where I stalled first, at what minute, for how long; (2) what I knew but didn't say; (3) what I didn't know at all; (4) which routine step I skipped; (5) one drill per stall, with a date. Every stall goes into `error_log.md` as Date | Problem or topic | What went wrong | Root cause | Rep 1 | Rep 2 | Rep 3.

### 9b. Review-due table

These dates assume every redo is Clean. Shaky → the same stage again in 2 days. Failed → back to Review 1 tomorrow. Rewrite the row when that happens.

**Problems**

| # | First try | Mark | R1 (+1) | Mark | R2 (+3) | Mark | R3 (+7) | Mark | R4 (+14) | Mark | R5 (+30) | R6 (+60) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 200\* | Tue Nov 17 | | Wed Nov 18 | | Sat Nov 21 | | Sat Nov 28 | | Sat Dec 12 | | Mon Jan 11 | Fri Mar 12 |
| 1192 | Tue Nov 17 | | Wed Nov 18 | | Sat Nov 21 | | Sat Nov 28 | | Sat Dec 12 | | Mon Jan 11 | Fri Mar 12 |
| 210\* | Wed Nov 18 | | Thu Nov 19 | | Sun Nov 22 | | Sun Nov 29 | | Sun Dec 13 | | Tue Jan 12 | Sat Mar 13 |
| 1203 | Wed Nov 18 | | Thu Nov 19 | | Sun Nov 22 | | Sun Nov 29 | | Sun Dec 13 | | Tue Jan 12 | Sat Mar 13 |
| 684 | Thu Nov 19 | | Fri Nov 20 | | Mon Nov 23 | | Mon Nov 30 | | Mon Dec 14 | | Wed Jan 13 | Sun Mar 14 |
| 1579 | Thu Nov 19 | | Fri Nov 20 | | Mon Nov 23 | | Mon Nov 30 | | Mon Dec 14 | | Wed Jan 13 | Sun Mar 14 |
| 2360 | Fri Nov 20 | | Sat Nov 21 | | Tue Nov 24 | | Tue Dec 1 | | Tue Dec 15 | | Thu Jan 14 | Mon Mar 15 |
| 127\* (mock) | Sat Nov 21 | | Sun Nov 22 | | Wed Nov 25 | | Wed Dec 2 | | Wed Dec 16 | | Fri Jan 15 | Tue Mar 16 |
| W5-T1–T4 (only if failed) | Mon Nov 16 | | Tue Nov 17 | | Fri Nov 20 | | Fri Nov 27 | | | | | |

\* For a cold redo of an old solve, "First try" is the first redo: mark it Clean / Shaky / Failed.

**Concepts** (2–5 min each in the warm-up slot; not counted toward the cap). Clean = a card answered word-perfect in under 30 s, a teach-back with ≤ 5 stumbles, a drill scoring ≥ 3, a lab whose predictions you rebuild from memory, the design hitting every K7 line.

| Item | First | Mark | +1 | Mark | +3 | Mark | +7 | Mark | +14 | +30 | +60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lab 1 pipeline | Tue Nov 17 | | Wed Nov 18 | | Sat Nov 21 | | Sat Nov 28 | | Sat Dec 12 | Mon Jan 11 | Fri Mar 12 |
| Labs 2–3 Terraform, Ansible | Thu Nov 19 | | Fri Nov 20 | | Mon Nov 23 | | Mon Nov 30 | | Mon Dec 14 | Wed Jan 13 | Sun Mar 14 |
| T1–T4 teach-backs | Wed Nov 18 | | Thu Nov 19 | | Sun Nov 22 | | Sun Nov 29 | | Sun Dec 13 | Tue Jan 12 | Sat Mar 13 |
| Drill 1 main-only failure | Wed Nov 18 | | Thu Nov 19 | | Sun Nov 22 | | Sun Nov 29 | | Sun Dec 13 | Tue Jan 12 | Sat Mar 13 |
| Story: Jenkins → Airflow | Thu Nov 19 | | Fri Nov 20 | | Mon Nov 23 | | Mon Nov 30 | | Mon Dec 14 | Wed Jan 13 | Sun Mar 14 |
| Design: CI/CD canary | Fri Nov 20 | | Sat Nov 21 (redraw) | | Tue Nov 24 | | Tue Dec 1 | | Tue Dec 15 | Thu Jan 14 | Mon Mar 15 |
| Drill 2 lock and drift | Fri Nov 20 | | Sat Nov 21 | | Tue Nov 24 | | Tue Dec 1 | | Tue Dec 15 | Thu Jan 14 | Mon Mar 15 |
| Drill 3 stalled rollout | Sat Nov 21 | | Sun Nov 22 | | Wed Nov 25 | | Wed Dec 2 | | Wed Dec 16 | Fri Jan 15 | Tue Mar 16 |
| Cards 1–10 (Anki: 1, 3, 7, 21 days) | Sat Nov 21 | | | | | | | | | | |

### 9c. Cheat sheet

File: `cheat_sheets/week05_cicd_iac.md`. Fill it Thursday with this pack closed, rewrite it from blank Sunday, then compare with **K-h** and count matches (target ≥ 80%).

---
---

# ANSWER KEY

Don't read a section here until you've attempted its matching section above.

---

## KA. Warm-up answers

1. (a) Two builds of one commit can differ (a moved base tag, a new transitive dependency), so prod runs something staging never tested. (b) Rollback and audit get muddy, because "version X" isn't one artifact. Build once, tag by digest, promote that digest, and change only config per environment.
2. Same inputs give the same output, with no dependence on the machine or the moment. It breaks with unpinned versions (`:latest`, `^1.2`), network fetches during the build, timestamps or hostnames baked in, and tools taken from the runner's PATH.
3. The key doesn't change when the dependencies change, so the build restores a stale cache and runs green on the wrong versions. Key it on a hash of every input that changes the result: the lockfile, the toolchain or runtime version, the OS and architecture. (You'll see this in L1c.)
4. Rolling: replace pods a batch at a time, and rollback is another rolling update. Blue-green: run two full stacks and flip the router, so rollback is an instant flip, at the cost of 2× capacity. Canary: send a small share of traffic to the new version, compare it with a control, then widen; rollback is removing the canary, and only that share of users was exposed.
5. A map from each resource address in code to the real object's ID, with its last-known attributes, dependencies, outputs, and a lineage plus serial number. Two writers both start from serial N, and the last write wins: resources created by the other run exist in the cloud but not in state (orphans, duplicates, "already exists" errors).
6. Drift. The next `plan` shows Terraform reverting it (code wins). In an incident, that can re-break the thing the console change fixed.
7. `changed=0`. `command`/`shell` tasks (they always report changed), appends with `>>`, and handlers notified by those tasks.
8. New pods never become Ready (a failing readiness probe, CrashLoopBackOff, an image pull error) or can't be scheduled (quota, insufficient resources). First command: `kubectl describe deploy <name>`, then look at the new ReplicaSet's pods (`kubectl get rs`; `kubectl describe pod`).
9. Docker caches layer by layer, and a layer's cache key includes the files it copies. Copying only the requirements file first means the slow `pip install` layer stays cached until the dependencies change. `COPY . .` first busts it on every code edit.
10. The child keeps running, reparented to init (or a subreaper). A `terraform apply` killed with `-9` leaves its provisioner children running, never writes the final state, and leaves real resources half-changed. You'll see an orphaned `sleep 60` in L2d.

---

## K1. Template drill reference (open only if your drill failed)

Compiled and run on this Mac with `clang++ -std=c++17 -Wall -Wextra`: zero warnings, every assert in §1 passes.

```cpp
#include <cassert>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

// T1. Multi-source BFS: fewest edges from the nearest source. -1 = unreachable.
vector<int> bfsDist(const Graph& adj, const vector<int>& sources) {
    vector<int> dist(adj.size(), -1);
    queue<int> q;
    for (int s : sources)
        if (dist[s] == -1) { dist[s] = 0; q.push(s); }   // mark on push: each node enters once
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u])
            if (dist[v] == -1) { dist[v] = dist[u] + 1; q.push(v); }
    }
    return dist;
}

// T2. Iterative DFS component labels. No recursion, so a 200k-long chain is fine.
pair<vector<int>, int> components(const Graph& adj) {
    const int n = adj.size();
    vector<int> comp(n, -1);
    int c = 0;
    for (int s = 0; s < n; ++s) {
        if (comp[s] != -1) continue;
        vector<int> st{s};
        comp[s] = c;
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (int v : adj[u])
                if (comp[v] == -1) { comp[v] = c; st.push_back(v); }
        }
        ++c;
    }
    return {comp, c};
}

// T3. Kahn's topological sort. Empty order = cycle. Also returns the layer count.
pair<vector<int>, int> kahn(int n, const vector<pair<int, int>>& edges) {
    Graph adj(n);
    vector<int> indeg(n, 0);
    for (auto [u, v] : edges) { adj[u].push_back(v); ++indeg[v]; }
    vector<int> order, cur;
    for (int i = 0; i < n; ++i) if (indeg[i] == 0) cur.push_back(i);
    int layers = 0;
    while (!cur.empty()) {
        ++layers;
        vector<int> nxt;
        for (int u : cur) {
            order.push_back(u);
            for (int v : adj[u]) if (--indeg[v] == 0) nxt.push_back(v);
        }
        cur.swap(nxt);
    }
    if ((int)order.size() < n) return {{}, 0};   // some node never reached indegree 0
    return {order, layers};
}

// T4. Union-find: path halving + union by size.
struct DSU {
    vector<int> parent, sz;
    int comps;
    explicit DSU(int n) : parent(n), sz(n, 1), comps(n) { iota(parent.begin(), parent.end(), 0); }
    int find(int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;                // already connected
        if (sz[a] < sz[b]) swap(a, b);
        parent[b] = a; sz[a] += sz[b]; --comps;
        return true;
    }
    int size(int x) { return sz[find(x)]; }
};
```

**The questions:**
1. Marking on push means each node enters the queue once, so the cost is O(V + E). Marking on pop lets a node be pushed by every neighbour before it's popped: duplicate work, and with multi-source BFS a node can get a distance from the wrong layer.
2. A recursive DFS on the 200,000-node chain **segfaulted here (exit 139) at both `-O0` and `-O2`**, with macOS's 8 MB main-thread stack (`ulimit -s` = 8176). Say "I'd use an explicit stack" before the interviewer asks. Tarjan (1192) needs real DFS order, so an iterative version keeps an edge index per frame.
3. Every node on a cycle, and everything downstream of it, keeps indegree ≥ 1, so it never enters the queue and `order.size() < n`. What's left is exactly the cyclic part plus its descendants. That's how you report which jobs are stuck.
4. Layers = the number of stages if every job in a layer runs in parallel = the length of the critical path, counted in jobs. It's the lower bound on a build DAG's wall time when every job takes one time unit (2050 uses real durations).
5. Both together: amortized inverse Ackermann, α(n), which is effectively constant. Path compression alone: O(log n) amortized. Union by size alone: O(log n) worst case.
6. No. Union-find only knows "same set", not direction. a→b and b→a look the same as a single undirected edge. Use Kahn's or three-colour DFS for directed graphs.
7. When edges arrive over time and you're asked between arrivals (online), or for "which edge first connects/closes a cycle" questions. BFS is better for a single query on a static graph, or when you need paths or distances. Neither handles deletions well: process them offline, in reverse, as additions.

**Common slips:** forgetting a duplicated source in T1, so it's pushed twice. `vector<int> st{s}` vs `st(s)`: the second makes `s` zeros. Not checking `order.size() == n` in T3. `unite` returning `true` when the roots are equal. Comparing `parent[a]` instead of `find(a)`.

---

## K2. Infra brief: notes, the 5 things, failure modes

### Reading notes (B1–B12)

- **B1.** Address → real ID, last-known attributes, the dependency graph (used for destroy order), outputs, and `lineage` (which history this state belongs to) plus `serial` (its version number). **Sensitive values are stored in plain text**, so encrypt the backend and restrict who can read it.
- **B2.** Local: an OS file lock on `terraform.tfstate`, plus a `.terraform.tfstate.lock.info` file. S3 today: `use_lockfile = true`, which writes a `.tflock` object next to the state with a conditional write (Terraform ≥ 1.10). S3 the older way: a DynamoDB lock table, now deprecated. GCS: a lock object, built in. Every state-writing command takes the lock, and `plan` does too.
- **B3.** `-lock-timeout=60s` retries for up to 60 s (the default is 0: fail at once). `-lock=false` skips locking entirely. Only use it for a read-only look when you know nothing else is running. Never for `apply`.
- **B4.** It removes the lock record. It doesn't stop the other process, doesn't touch state, and doesn't touch infrastructure. Terraform's own help says it: "Local state files cannot be unlocked by another process." You need the lock ID.
- **B5.** `plan -refresh-only`: shows how reality differs from state and proposes no config changes. `apply -refresh-only`: writes reality into state (accepts the drift). `plan -detailed-exitcode`: **0** no changes, **1** error, **2** changes present. That's the drift-check job.
- **B6.** `command` runs a program with no shell (no pipes, redirects or `$VAR`). `shell` runs through `/bin/sh`. Both report "changed" every time. Fix: use a state module (`lineinfile`, `copy`, `template`, `file`, `package`, `service`); add `creates:`/`removes:`; or set `changed_when:` (for example `changed_when: false` for a read-only command).
- **B7.** Once, at the end of the play (or at `meta: flush_handlers`), only if a notifying task reported changed, in the order the handlers are defined. If a later task fails on that host, its notified handlers don't run unless you pass `--force-handlers`. The new config is on disk, but the service never restarted.
- **B8.** It skips them (unless `check_mode: false`), so `--check` under-reports. Lab 3 shows it: `--check` says `changed=0` while a real run changes 2 things.
- **B9.** Self-service; high velocity; hermetic builds; enforcement of policies and procedures.
- **B10.** Cut a release branch from a mainline revision. Fix on mainline first, then cherry-pick into the release branch. Release branches are never merged back into mainline. You can rebuild any release exactly from its branch.
- **B11.** Config pushes cause outages as often as binaries do. So config is versioned, reviewed, rolled out gradually and roll-back-able, and pinned to the binary it was tested with.
- **B12.** A control group on the old version, the same size, taking the same traffic at the same time, cancels out time of day, traffic mix, and the cold-cache effect of new pods. "Before vs after" confuses your change with load changes. The whole fleet isn't a like-for-like comparison: different size, warm caches.

### The 5 things I'd say (compare with yours)

1. **Build once, promote the digest.** One immutable artifact per commit, signed, goes dev → staging → prod. Only config changes per environment. Rollback means redeploying the previous digest, never rebuilding.
2. **Hermetic builds; the cache is a speed-up, never a source of truth.** Pin everything (lockfiles, base images by digest, toolchains). Key every cache on a hash of all its inputs. Only trusted main-branch jobs write shared caches.
3. **Progressive delivery with automated judgement.** Canary next to a control, bake time, gate on user-facing signals (error rate, p99, saturation) with minimum samples, and **fail closed when there's no data**. Widen in steps (1 → 10 → 50 → 100%) and roll back automatically. DB changes go expand/contract, and feature flags separate deploying from releasing.
4. **Terraform state is the source of truth, so protect it.** Remote, versioned and encrypted, with locking. Small states per environment × component to limit blast radius and lock contention. Review the plan, apply the saved plan, and detect drift with a scheduled `plan -detailed-exitcode` (exit 2 = drift).
5. **Config management must converge.** Every task describes desired state, so run 2 reports `changed=0`. `shell`/`command` need `creates`/`changed_when`. Roll changes in batches (`serial`, `max_fail_percentage`) with a health check between batches. Prefer immutable images for stateless fleets.

### Failure modes, filled

| Symptom | Cause | First check |
| --- | --- | --- |
| Every PR green; `main` red on the same job | PRs tested against an old main. Two PRs each pass alone but conflict once merged (semantic conflict). Or main-only secrets, steps or caches | Which commit did each PR run test? Run CI on main before and after each merge (`git log --merges`) |
| Cache HIT, tests green, wrong dependency version shipped | The cache key misses an input (static or branch-scoped key, or a `restore-keys` fallback) | Compare the key's inputs with the lockfile hash; `pip freeze` / `npm ls` in the job vs the lockfile |
| Same commit, two image digests | Non-hermetic build: a moved base tag, unpinned transitive deps, timestamps, network fetches | `docker buildx imagetools inspect` both; diff `docker history`; pin `FROM` by digest |
| Canary passed; at 100% errors climb an hour later | Load-dependent bug or slow leak; too few canary samples on the bad code path; bake too short | Per-version error and memory graphs since promotion; canary sample counts |
| State lock, `Created` hours ago | A crashed or preempted run left the lock, or a run is still going | Lock `Who`/`Created`/`Operation` → is that runner/job alive? Then `force-unlock <ID>`, then `plan` (not `apply`) |
| Plan changes something nobody coded | Drift (console, another tool, an autoscaler) or a provider upgrade changing defaults | `terraform plan -refresh-only`; the cloud audit log (CloudTrail etc.) for who changed it |
| Killed apply, then "already exists" | The resource was created but never written to state | Find it in the cloud by name or tags; `terraform import` or an `import {}` block, then `plan` |
| Ansible run 2 `changed=2`, restarts every run | Non-idempotent `shell`/`command`/append tasks notifying handlers | Run twice and read the PLAY RECAP; look for `changed:` on run 2 |
| `--check` says 0, the real run changes things | Check mode skips `command`/`shell` | Look for `skipping:` lines in the check run |

---

## K3. Lab: expected output and what each step proves

### Lab 1

*L1a–L1c were run on this Mac (Python 3.13, Nov 6). L1d–L1i were not, because Docker isn't installed: the lines below are what the scripts and kubectl print.*

- **L1a (seen):** run 1 `cache MISS deps-py3.13-72a7d8916d99` (3 s), then `2 passed`. Run 2 `cache HIT  deps-py3.13-72a7d8916d99` (0 s). **Proves:** the key is the Python version plus a hash of the lockfile, so the same inputs restore.
- **L1b:** `cache MISS deps-py3.13-a0e201ecda2b`, a new key. (I ran this step with a different version bump, so the hash here is computed from `pytest==8.3.5`.) **Proves:** changing an input changes the key. The old entry is just never read again.
- **L1c (seen):** first run `cache MISS deps-main`, then after the bump `cache HIT  deps-main`, `2 passed`. `pytest 8.3.3` is installed while the lockfile says `pytest==8.3.5`. **Proves:** a key that doesn't include its inputs gives a green build on the wrong dependencies. On a real CI system, the main branch's cache entry goes stale and every branch that falls back to it inherits it. That's one way "it only fails on main" (or "only passes on main") happens.
- **L1d:** `deployment.apps/web-stable created`, `service/web created`, `deployment "web-stable" successfully rolled out`. 9 pods, all `track=stable`. `releases.log` gets a `BOOTSTRAP` line.
- **L1e:** the canary rolls out, the bake passes, then `canary_gate.sh is missing or not executable…` → `ROLLBACK: deleting canary web:<new>; stable stays on web:<old>`, and the log records `ROLLED_BACK(no-gate)`. **Proves:** the pipeline fails closed. With no judgement, nothing promotes.
- **L1f:** a correct gate is about 15 lines of shell (filter, count, compare, exit). Typical mistakes: counting kubectl's own lines as samples; treating 0 canary samples as rate 0 and passing; floating-point compare in pure `sh` (use `awk`).
- **L1g:** about **10%** of requests reach the canary, so roughly 30 of 300 (expect 20–40). The Service selects `app=web`, which matches 10 ready pods, and kube-proxy picks an endpoint at random per connection. Each `curl` is a new connection. Gate line roughly `canary=<new> n=31 err=0 rate=0.00 | stable n=269 err=0 … -> PASS`, then `PROMOTED web:<new>`. **Proves:** a replica-ratio canary works with no service mesh, but its traffic share is coarse (1 pod in 10) and only approximate.
- **L1h:** `2 passed` (the unit tests inject the random number, so they can't see the bad default). `deployment "web-canary" successfully rolled out` (`/healthz` still returns 200). The gate prints roughly `rate=0.30 … -> FAIL`, then `ROLLBACK`, and `exit=1`. `releases.log` ends with `ROLLED_BACK(gate-failed)`. **Proves:** unit tests and readiness probes passed a bad build. Only user-facing signals on real traffic caught it, and only about 10% of users saw errors, for about a minute.
- **L1i:** the bad version rolls out to all 9 pods. `rollout history` shows two or three revisions. `rollout undo` finishes in seconds. **Why it's fast:** the old ReplicaSet still exists (scaled to 0), the image is already on the node, and nothing is rebuilt. That's "rollback = redeploy the previous artifact". **Proves:** skipping the canary exposes 100% of users, and manual rollback works only because the old artifact is still there.

### Lab 2 (all seen on this Mac, Terraform 1.17.1)

- **L2a:** `Apply complete! Resources: 2 added, 0 changed, 0 destroyed.` `out/app.conf` = `replicas=3`.
- **L2b:** B fails immediately:
  ```
  Error: Error acquiring the state lock
  Error message: resource temporarily unavailable
  Lock Info:
    ID:        ec572d91-33fe-19fd-cbe1-6c31876b3ecf
    Path:      terraform.tfstate
    Operation: OperationTypeApply
    Who:       aniketkumar@Anikets-MacBook-Air.local
    Version:   1.17.1
  ```
  The `.lock.info` file holds the same JSON. **Proves:** even `plan` takes the lock. "Resource temporarily unavailable" is the OS file lock (`EAGAIN`).
- **L2c:** `Acquiring state lock. This may take a few moments...`, then a wait (31 s in my run), then `No changes.` **Proves:** `-lock-timeout` queues behind the other run. That's what a CI job should use instead of failing at once.
- **L2d:** `.terraform.tfstate.lock.info` **is still on disk**, but the plan runs with **no lock error**: the OS released the lock when the process died. `pgrep` shows `sleep 60` **still running**, an orphaned provisioner child (warm-up Q10). `out/app.conf` already says the new value, while the plan says `terraform_data.slow_rollout will be created` / `Plan: 1 to add`. **Proves:** a local lock dies with its process. A killed apply leaves reality ahead of state, and child processes keep running.
- **L2e:** `Successfully configured the backend "http"!`. `store/state.json` exists, and the local `terraform.tfstate` is now **0 bytes**. **Proves:** migration copies state to the backend and empties the local file.
- **L2f:** the plan fails:
  ```
  Error: Error acquiring the state lock
  Error message: HTTP remote state already locked:
  ID=f36e36cf-1952-6d10-40a1-c6e71bea59ea
  Lock Info:
    ID:        f36e36cf-1952-6d10-40a1-c6e71bea59ea
    Operation: OperationTypeApply
  ```
  The server log shows `LOCK refused: held by …` and the `423` status. **The lock outlived the process.** That's every real remote backend: an S3 lockfile, a DynamoDB item, a GCS object. **Before unlocking, confirm (1)** the process or CI job named in `Who` is really gone (job status, runner status, `ps`), and **(2)** nobody else is mid-apply. Then `Terraform state has been successfully unlocked!`, and the server logs an `UNLOCK` with status 200. The next plan says `local_file.app_config will be created` and `terraform_data.slow_rollout must be replaced`, `Plan: 2 to add, 0 to change, 1 to destroy`. **Why "create" a file that exists:** the killed apply wrote the new file but never wrote state, so state still says `replicas=3`. (Compare L2d: the local backend had already recorded the finished file step. The remote run, killed 6 s in, had written nothing, because Terraform saves remote state periodically during an apply, not after every resource.) On refresh, the provider sees content that doesn't match what it recorded and treats the old object as gone. **Proves:** force-unlock fixes the lock, not the partial apply, so you always `plan` after an unlock, never a blind `apply`.
  - A detail I saw: `force-unlock` on the http backend sends **no lock ID** in its request (the server got an empty UNLOCK body). So here the ID check happens only in your head. Treat the ID as your proof that you're unlocking the run you think you are.
- **L2g:** a clean plan gives `exit=0`. After the hand edit, `-refresh-only` prints `Note: Objects have changed outside of Terraform` and `# local_file.app_config has been deleted` (this provider models a content change as deletion; a cloud resource shows `~ update in-place` attributes instead). The plan then shows `local_file.app_config will be created`, `Plan: 1 to add`, and **`exit=2`**. **Proves:** a drift job is just a scheduled plan that alerts on exit 2. **The three resolutions:** (1) **revert**: `apply` the code (code wins); (2) **adopt**: change the code to match reality, then the plan is clean; (3) **accept into state**: `apply -refresh-only`, then fix the code. In an incident, (2) is usually right. (1) can re-break the thing the hand fix repaired.

### Lab 3 (all seen on this Mac, ansible-core 2.22.0)

- **Run 1:** `ok=5 changed=4` (the handler runs).
- **Run 2:** `ok=5 changed=2`. `Connection limit is set` and `Release marker is recorded` both show `changed:`, and the handler **runs again**.
- **File:** `replicas=3`, then `max_conns=100` **twice**.
- **`--check --diff`:** `Connection limit is set` and `Release marker is recorded` both show `skipping:`, and the recap says `ok=2 changed=0 … skipped=2`. **Check mode reports no changes while the real run changes two things.**
- **Your fix should end with:** run 2 `changed=0` and no handler. The connection-limit task becomes a state module that ensures one line exists (`ansible.builtin.lineinfile` with a `regexp`, so a later value replaces the old one instead of adding a second line). The marker task gets `changed_when: false`. **Proves:** idempotency is a property of how each task is written, not of the tool. On a 13,000-VM fleet, run 2's `changed=2` would mean 13,000 needless restarts, every run.

---

## K4. Flashcard backs

1. One tested artifact (by digest) goes to every environment, so prod runs exactly what staging tested. Rollback is "deploy the previous digest". Rebuilding can pick up new base layers or dependencies.
2. Correct: a hash of every input that changes the output (lockfile, toolchain version, OS/arch). Wrong: (a) too coarse (static or branch-scoped) → stale restores; (b) too fine (includes timestamps or commit SHA) → never hits.
3. Rolling: batch replace, cheap. Blue-green: two stacks, flip, instant rollback, 2× capacity. Canary: small share first, compared against a control. Pick a canary when bugs only show up under real traffic and you want to limit how many users a bad release reaches.
4. Expand/contract: add the new schema alongside the old (expand), deploy code that works with both, backfill, switch reads, and remove the old only after the release is final (contract). Every step can be rolled back, because the old code still works.
5. `terraform plan -detailed-exitcode -lock-timeout=5m` in a scheduled job: exit 2 → alert, 1 → job error, 0 → clean. `plan -refresh-only` shows only the out-of-band changes.
6. Read Lock Info (`Who`, `Created`, `Operation`) → confirm that job or runner is dead and nothing else is running → `terraform force-unlock <ID>` → `terraform plan` (not apply) to see what the dead run half-did → import or fix, then apply.
7. `terraform import <address> <cloud-id>`, or an `import { to = <address>, id = "<id>" }` block, then `terraform plan` (`-generate-config-out=gen.tf` drafts the resource code).
8. Run it twice; run 2's PLAY RECAP must say `changed=0`. Trap: `--check` skips `command`/`shell`, so a dry run can say 0 when the real run won't.
9. Count indegrees → queue every 0 → pop, append to the order, decrement neighbours, push any that reach 0 → cycle iff `order.size() < n`.
10. `find`: while `p[x] != x`: `p[x] = p[p[x]]; x = p[x];` return x. `unite`: `a = find(a), b = find(b)`; equal → false; attach the smaller under the larger, add the sizes, `--comps`, return true.

---

## K5. Teach-back outlines (6 beats each) and follow-up answers

### T1: Hermetic builds and caching
Beats: (1) the goal is fast **and** correct, in that order; (2) hermetic means the same inputs give the same output: pin deps, base images by digest, toolchains, no network in build steps; (3) caches skip work whose inputs haven't changed, so the key = a hash of the inputs; (4) layers: deps before source (Week 3); remote and shared caches for ephemeral runners; (5) the two failure directions: a stale key and green on the wrong code, or a key that never hits and slow builds; (6) trust: only trusted main jobs write the shared cache.
Follow-ups: 1. Unpinned or different versions, different OS or toolchain, hidden local state (env vars, files, a warm cache), network access. 2. Build twice in clean environments and compare digests; fix timestamps (`SOURCE_DATE_EPOCH`); diff the outputs. 3. Safe for download caches that the installer re-checks against the lockfile; dangerous for build outputs, because they're used as-is. 4. Whoever can write the cache can inject artifacts into everyone's build. PR jobs read-only, main writes, keys include the toolchain. 5. BuildKit `--cache-from`/`--cache-to type=registry`, cache mounts for package managers, and layer ordering.

### T2: Promotion and rollback
Beats: (1) build once, sign, store by digest; (2) promote the same digest through environments and gate each step (tests, approvals, policy); (3) canary next to a control, bake, judge on user-facing signals with minimum samples, fail closed; (4) widen in steps, per region; (5) rollback = previous digest, kept warm, in minutes; (6) what makes rollback safe: expand/contract schemas, feature flags, config versioned with the code.
Follow-ups: 1. Rolling for low-risk stateless changes; blue-green when you need instant cutover and can pay 2×; canary for risky changes, where real traffic is the test. 2. Expand/contract (K4 #4); if the migration was destructive, roll forward instead. 3. Error rate, p99 latency and saturation vs the control, with minimum request counts; no data = fail closed (pause or roll back, never promote). 4. Load-dependent or slow-burn bugs, a rare path the canary never hit, cold vs warm caches. Fix: longer bake for risky changes, more steps, and an auto-rollback watch window after 100%. 5. Deploy = the code is running; release = users get the behaviour. Flags let you deploy dark and switch off without a deploy.

### T3: Terraform state, locking and drift
Beats: (1) state maps code addresses to real IDs; without it Terraform can't tell update from create; (2) it holds secrets in plain text, so remote, encrypted, versioned, access-controlled; (3) locking: one writer at a time, and every write-capable command takes the lock; (4) local locks die with the process, while remote locks outlive it, so stale locks and force-unlock come with a checklist; (5) drift = reality ≠ state/code, found by a scheduled plan with exit code 2; (6) resolve by revert, adopt or accept, and limit blast radius with small states.
Follow-ups: 1. Both start from the same serial and the last write wins. The loser's resources exist but aren't in state, so you get duplicates and "already exists" errors on the next run. 2. Lock Info → confirm the job is dead → `force-unlock ID` → `plan`, then import any orphans. 3. A scheduled `plan -detailed-exitcode` per stack, results on a dashboard, alert on exit 2, `-lock-timeout` so it waits behind applies. 4. Don't blind-apply. Adopt the change in code, or decide deliberately to revert. Policy: break-glass changes land in code within a day. 5. Per environment × component (network, data, compute, app): smaller blast radius, less lock contention, faster plans. Share values through outputs or remote-state data sources.

### T4: Idempotent configuration
Beats: (1) idempotent = running it again changes nothing when the host is already right; (2) why: safe retries, fleet-wide reruns, and `changed` means something; (3) how: state modules, `creates`/`removes`, `changed_when`, templates; (4) handlers only on change, so non-idempotent tasks cause restarts every run; (5) verify by running twice (`changed=0`), and know that `--check` skips shell/command; (6) rollout: `serial` batches, `max_fail_percentage`, health checks, a canary group via `--limit`.
Follow-ups: 1. It describes an end state and checks before acting. 2. Restarts on every run, real changes buried in noise, and retries that aren't safe (double appends, double migrations). 3. Terraform: cloud resource lifecycle through APIs, with state. Ansible: config inside machines, no state (it inspects the host each run). Packer images sit between them. 4. `--check --diff` first, `--limit` a canary group, then `serial: [1%, 10%, 25%]` with `max_fail_percentage` and a health check per batch. Your 400-VM reboot story fits here. 5. Immutable images for stateless, replaceable fleets; config management for long-lived or stateful hosts (databases, like your Mongo fleet).

---

## K6. Troubleshooting: interviewer sheets and scoring

### Drill 1: the pipeline fails only on main

**Hidden facts (give only when asked):**
- #481 renamed `connect(timeout_ms=…)` to `connect(timeout=…)` in the client library and updated every caller that existed at the time. Its PR pipeline ran at 08:50 against main, and it was green.
- #483 was branched last Thursday. It adds `tests/test_retry.py::test_backoff_on_timeout`, which calls `connect(timeout_ms=…)`. Its PR pipeline ran at 08:30, **before #481 merged**, and it was green. It was never rebased.
- The repo doesn't require branches to be up to date before merging, and there's no merge queue.
- The main pipeline on the #481 merge commit (09:02) was **green**. The first red is the #483 merge commit (09:10).
- Cache keys include the lockfile hash; the lockfile hasn't changed. Same secrets, same runner image. Not flaky: 3 reruns, 3 identical failures.
- The library code is the same on main as on #481's branch.

**Model path:** Clarify (what changed: two merges; does main fail on every rerun: yes) → Scope (only main, only this job, starting at the #483 merge) → Stabilise (unblock deploys: revert **only #483**, or forward-fix the one call to `timeout=`; don't revert #481; don't wipe caches) → Hypothesise, ranked: (1) a semantic conflict between #481 and #483; (2) a main-only difference (secrets, env, cache scope); (3) flakiness → Check: run main's pipeline at 09:02 (green) and 09:10 (red); `git grep timeout_ms` on main finds only the new test; the reruns all fail identically (not flaky); the cache key is unchanged → Fix and prevent: forward-fix or revert #483. Require up-to-date branches or a **merge queue** that tests the exact merge result; add a CI check for removed public parameters (a deprecation period instead of a hard rename).

**Scoring (1–4 per step):** Clarify asks "what merged when?" · Scope narrows to the first red commit · Stabilise unblocks main without reverting both PRs or wiping caches · Hypotheses are ranked with semantic conflict first · each check names a command and the result that confirms or rules it out · prevention names a merge queue or the up-to-date rule.

### Drill 2: Terraform state lock and drift

**Hidden facts:**
- `ci-7f9c` was a **spot** runner. The 23:47 apply was a manual hotfix run that an engineer started to add a second NAT gateway. AWS reclaimed the spot instance at 23:52. The job log ends mid-apply with `runner lost`.
- The S3 backend uses `use_lockfile = true`. The `.tflock` object from 23:47 is still there, and that's why the nightly's conditional write got `412 PreconditionFailed`.
- `aws_nat_gateway.b` **was created** in AWS at 23:50 (tagged `Name = prod-nat-b`), but it's **not in state**, because the run died before writing state.
- Drift: during an incident at 23:30 last Thursday, on-call added a security-group ingress rule in the console (`tcp/8443` from a partner's CIDR) to restore a partner integration. No PR followed. A plan **removes** that rule, which would break the partner again.
- No other run is active. The state bucket has versioning on.

**Model path:** Clarify (what was the 23:47 run, who started it, is anything running now?) → Scope (only this stack; other nightlies fine) → Stabilise (**pause the nightly auto-apply for this stack**; don't force-unlock and apply blind) → Hypothesise: (1) a dead run left a stale lock; (2) a live run is still applying; (3) partial apply and drift waiting in the plan → Check: the job status for `ci-7f9c` (lost at 23:52); the instance (spot-terminated); the `.tflock` object's timestamp; nothing else running → `terraform force-unlock <ID>` → **`terraform plan` only**: it shows `aws_nat_gateway.b will be created` (one already exists → import it, don't create a duplicate) and the 8443 rule `will be destroyed` (drift → adopt it into code with a PR, or confirm with the partner team) → Fix and prevent: no applies on spot runners; prod applies only from a reviewed saved plan; a nightly drift job that alerts instead of auto-applying; break-glass console changes need a PR within 24 h; state versioning (already on) as the recovery path. Get the 09:00 change in after the import and the adopt PR.

**Scoring:** checks the lock holder is dead before unlocking · plans before applying · finds the orphan and imports it · treats the security-group change as drift with a deliberate decision · prevention covers runners, saved plans and drift alerts.

### Drill 3: the rollout stalls

**Hidden facts:**
- The analysis queries filter on the label `version="<release>"`. This release's Helm chart renamed that pod label to `app.kubernetes.io/version`, so **both queries return no data** and the analysis waits for measurements forever. No timeout is configured.
- Real canary health, visible in the ingress metrics (which aren't filtered by pod label) and in the canary pod's logs: **4% 5xx** on the canary vs 0.1% on stable, from `NullPointerException` in the new payment-method code. The canary takes 10% of traffic, so about 0.4% of all checkout requests fail.
- Readiness probes pass, because `/healthz` doesn't touch the payment path.
- Promote, abort and pause all work from the deploy tool.

**Model path:** Clarify (what's it waiting for? how long is normal?) → Scope (only this release's analysis; other services' canaries analyse fine) → Stabilise (**abort the canary to 0%**: it's serving real users, and you don't know its health; don't promote on no data) → Hypothesise: (1) the metric queries return nothing; (2) the metrics pipeline is down; (3) the canary gets no traffic → Check: run the query by hand (empty); run it without the version filter (data); compare pod labels between the old and new chart (renamed); ingress error rate by upstream pod (the canary at 4%); canary logs (NPE) → Fix and prevent: fix the bug and fix the query (or keep the old label too); analysis fails closed with a timeout (**no data = fail, not wait**); a minimum-sample check; a test in CI that renders the chart and checks the labels the analysis depends on. Tell the PM that promoting would have shipped a 4% checkout failure to everyone.

**Scoring:** stabilises by aborting, not promoting · finds "no data" as the cause of the stall · checks real error rates by another path · names fail-closed with a timeout as prevention.

---

## K7. Design reference outline: CI/CD system with canary and rollback

**Requirements**
- Functional: PR builds and tests; a merge queue that tests the exact merge result; build once, then sign and store by digest with provenance; promote dev → staging → prod per region; canary with automated analysis; automatic rollback; manual promote, abort and rollback; freeze windows; an audit log of who shipped what, when.
- Non-functional: PR feedback p50 < 10 min; merge to prod the same day (target < 1 h for low-risk services); **rollback < 5 min, and it must work even when the deploy system is degraded** (break-glass path); 99.9% availability for the control plane; one bad release must never touch all regions at once.
- Scale math (say it aloud): 1,500 merges a day, at about 5 CI runs per merge (pushes plus the queue) ≈ 7,500 runs a day ≈ 5 a minute on average, about 15–20 a minute at peak. At about 20 CPU-minutes per run that's 150,000 CPU-minutes a day ≈ 100 cores on average, 300–400 at peak → an autoscaled runner pool. Images: 1,500 a day × about 200 MB ≈ 300 GB a day raw, much less after layer dedupe → a retention policy (keep the last N per service, plus anything deployed in the last 90 days).

**API**
- `POST /releases {service, digest, strategy}` → `release_id`
- `GET /releases/{id}` (state, current step, analysis results)
- `POST /releases/{id}:promote | :abort | :pause`
- `POST /services/{svc}/rollback {to_digest?}` (defaults to the last known good)
- Webhooks or events for chat and paging. Everything is idempotent with a request ID.

**Data**
- `Artifact` (digest, service, commit, signature, SBOM, provenance) · `Release` (id, service, from_digest, to_digest, region wave, state) · `Step` (weight, bake time, result) · `AnalysisRun` (queries, thresholds, sample counts, verdict) · `ServiceLock` (one active release per service and environment, held as a lease with a fencing token) · `AuditEvent` (append-only).
- Release state machine: `PENDING → CANARY(step i) → ANALYZING → (next step | PROMOTING) → DONE`, with `→ ROLLING_BACK → ROLLED_BACK` from any step, and `PAUSED` on manual hold or missing data.

**Deep dive A: canary analysis**
- The canary and a **fresh control** (same image as stable, same pod count, deployed at the same time) take equal traffic. Compare the canary against the control, not against the old fleet, so warm-cache and time-of-day effects cancel out.
- Signals: error rate, p99 latency, saturation (CPU, memory), plus business metrics for key services. Each has a minimum sample count. A statistical test, or simple thresholds with margins.
- **Fail closed:** no data or too few samples → fail or pause, never pass. Every analysis has a timeout.
- Steps 1% → 5% → 25% → 50% → 100%, with bake times that grow with risk. Region waves: one region fully done, then the next.

**Deep dive B: an orchestrator that survives its own crash**
- Each release is a durable workflow: the state lives in a database, not in memory, and every step is idempotent ("set weight to 10%" is safe to repeat).
- On restart, the worker reconciles: it reads the release's state, observes the cluster, and continues or rolls back. A lease on the `ServiceLock` plus a fencing token stops two workers from driving the same release. (This is the same shape as your Airflow platform: tasks that retry safely, and state held outside the worker.)

**Failures (what the system does by itself)**
1. The orchestrator crashes mid-rollout → the lease expires, another worker resumes from durable state.
2. The metrics backend is down → analysis can't pass → the release pauses, and rollback is still allowed.
3. A bad config push → config is versioned and canaried like code, never pushed globally at once.
4. The registry is down → per-region pull-through caches; images pre-pulled on canary nodes; rollback uses images already on the nodes.
5. A canary passes, but a slow-burn bug appears after 100% → an auto-rollback watch window after promotion (for example 1 h on the same signals).
6. Rollback itself fails → forward-fix path; break-glass `kubectl` access with audit; old ReplicaSets kept for N revisions.
7. A destructive DB migration → policy blocks it in the release path; expand/contract only.
8. Two releases of dependent services at once → one lock per service; contract tests between them in CI.

**Tradeoffs**
- Speed vs safety: bake time and step count by risk tier.
- Push (the pipeline applies) vs pull (GitOps, e.g. Argo CD: drift correction and audit for free, slower feedback, harder imperative steps like analysis without a rollout controller).
- Merge queue batching (higher throughput, but a failure needs a bisect) vs serial (simple, slow).
- One central platform vs per-team pipelines (consistency vs freedom).
- Automatic vs human promotion for tier-0 services.

**At 10× the merges:** shard the orchestrator by service hash; regional control planes; a remote build cache plus test selection (run only affected tests); batched merge queues with automatic bisect; artifact retention and garbage collection become a real cost.

**Critique rubric (mark each Y/N on your drawing):** scale math done aloud · rollback < 5 min explained (old artifact warm, no rebuild) · control group, not before/after · fail-closed on no data · region waves · durable orchestrator state · one release per service at a time · DB migration rule · at least five failures with automatic responses · at least three tradeoffs.

---

## K8. Story rubric (coverage only; your facts, not mine)

- [ ] Situation names Jenkins' scale and **one concrete pain**, with a number if you have one
- [ ] "My decision" says what **you** chose or built (not "we")
- [ ] The tradeoff names the option you rejected and what your choice cost
- [ ] At least one number you measured, plus your scale facts (200K+ executions a month, 42+ environments, 13,000+ VMs)
- [ ] The lesson is specific (something you'd change), not "communication is important"
- [ ] Under 2:00 spoken, and you stop
- [ ] Probe 1 ("Airflow is for data") answered in ≤ 30 s without getting defensive
- [ ] Probe 4 (a retry on 300 VMs) connects to idempotency (Lab 3)

---

## K-h. Reference cheat-sheet points (compare after writing yours; target ≥ 80% matching)

**Top, 5 things:** build once and promote the digest · hermetic builds, cache keyed on inputs, main-only cache writes · canary vs control, bake, fail closed, step widening, auto-rollback · state remote, encrypted, locked, split per component; drift = plan exit 2 · idempotent config: run twice = `changed=0`; batch fleet rollouts.

**Commands:**

| I want to… | Command |
| --- | --- |
| Wait for another run's lock instead of failing | `terraform plan -lock-timeout=5m` |
| Clear a stale lock (after confirming the holder is dead) | `terraform force-unlock <ID>` |
| See drift only | `terraform plan -refresh-only` |
| Fail a CI job on drift | `terraform plan -detailed-exitcode` (2 = changes) |
| Accept reality into state | `terraform apply -refresh-only` |
| Adopt an orphaned resource | `terraform import <addr> <id>`, or an `import {}` block |
| See what's in state | `terraform state list` / `terraform state show <addr>` |
| Dry-run a playbook | `ansible-playbook site.yml --check --diff` (skips command/shell) |
| Roll a play over a fleet in batches | `serial: [1, "10%", "25%"]` + `max_fail_percentage` |
| Watch, list and undo a k8s rollout | `kubectl rollout status` / `history` / `undo deploy/<name>` |
| Compare two image digests | `docker buildx imagetools inspect <image>` |

**Failure modes:** the nine rows in K2.

**Questions and stories:** "How do you deploy safely at scale?" → Jenkins → Airflow, and the 400-VM rolling reboot · "Tell me about an IaC incident" → your facts only · "How do you keep 13,000 VMs consistent?" → idempotency, batched rollouts, the Airflow platform.

---

## K9. Mock interviewer sheet (for Claude on Saturday; don't read)

- **Intro (0–5):** 90-second intro. Then: "What does Terraform state store?" (W5) and "Your container takes exactly 30 s to stop on every deploy. Why?" (W3).
- **Coding (5–40):** 127 cold. Interrupt at minute 12 if no approach has been stated. Follow-ups if done early: bidirectional BFS and why it helps; return the actual path; the word list is 1M words, so what changes in memory?
- **Design (40–55):** "Design how a feature-flag/config change reaches 50,000 hosts safely in under 10 minutes, with a kill switch." Probe: staged rollout by percentage and region, versioned config, client-side caching with a last-known-good copy, what happens when the config service is down (hosts keep their last-known-good), and how you'd audit it.
- **Troubleshooting (55–70):** "Since we moved CI to a new runner pool in another VPC, `docker pull` from our registry hangs on large layers and times out, while small images pull fine. `curl` to the registry's `/v2/` works." Hidden: the new VPC's path goes over a tunnel with MTU 1400, ICMP frag-needed is blocked, so PMTUD fails and big TLS records stall (Week 2, F7). Check: `ping -D -s 1372` (macOS) / `ping -M do -s 1372` (Linux) succeeds while `-s 1472` fails; `tcpdump` shows retransmits of full-size segments. Fix: MSS clamping on the tunnel, or allow ICMP type 3 code 4. Prevention: an MTU check in the runner-pool bring-up.
- **Score** all eight areas with timestamps. Composure: how fast they recover after the minute-12 interrupt.
