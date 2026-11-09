# WEEK PACK — Week 7: Distributed systems (light week)

Infra layer: replication, quorums, Raft, leases, fencing tokens, consistent hashing · Code: state-machine, interval and bitmask DP · Design: distributed lock and lease service (not drawn this week) · Story: a technical disagreement I resolved

**Rule for this file:** do every section cold first. Every answer, note, hint and reference is in the **ANSWER KEY** at the bottom. Don't scroll down until you've tried the section. There is no LeetCode solution code anywhere in this file, and no template code either. Problems go through the hint ladder one rung at a time, and the template drill is graded on your own file.

**Light week:** weekday blocks only (Mon–Fri). No Friday design, no Saturday mock. Saturday and Sunday are reviews only, because the spacing schedule doesn't pause.

Lab files: `week_packs/week07_lab/etcd3.sh` (a helper that starts, kills and restarts a local 3-node etcd cluster; it has no answers in it).

---

## 0. Reviews first, then this week's plan

### 0a. The review pull (made Fri Nov 6, 2026)

I went through `tracker.md`, `error_log.md`, the Week 3 and 4 packs, and the coding page's seed list. **No redo result has been logged anywhere since Oct 25.** So, going by the record alone, this is what's due:

| From | Problems | Stage | Due since |
| --- | --- | --- | --- |
| Week 1 tracker | **3\***, **1\***, **11\***, **49\***, 992, 974, 1248, 933 | Review 1 | Oct 19–21 |
| Week 1 coding-page seeds | **560\***, **525\*** | First redo of an old solve | Oct 12–14 |
| Week 2 tracker, old solves | **146\***, **20\***, **71\***, 739 | First redo | Oct 22–25 |
| Week 2 coding-page seeds | **239\***, **907\***, **875\*** | First redo | Oct 19–21 |
| Week 2 tracker, first tries | 84, 33 ⚑, 1438, 2398, 410 | Unknown: if you did them, Review 1 is overdue; if not, they're still owed as first tries | Oct 20–24 |
| Week 3 pack (this week) | 337 (R2) · **124\***, 102, 98, 1114 (R1), plus earlier R1s if missed | As the Week 3 pack schedules | Nov 3–6 |
| Week 3 coding-page seeds | 1116, 388 | First redo | Nov 2 |
| Weeks 4–6 | Nothing yet. Week 4 starts Mon Nov 9 on your shifted calendar | — | — |

\* shaky by history (5+ submits, or last seen before May 2026). Do these first in any day. ⚑ never solved.

**Count: 24 problem reviews, plus 5 Week 2 problems with unknown status. That's far over the cap of 5, so no new problems today** (Fri Nov 6), and none on any morning that opens with more than 5 due.

**Concept reviews also overdue** (not counted toward the cap; do them in the 10-minute warm-up slot): error log F1–F8, Reps 1–3 (due Oct 26, Oct 28, Nov 1), none marked.

**What I need from you:** for every row above, Clean / Shaky / Failed and the date, or "not done". Then I'll recount and rewrite the dates. Until then, each morning: oldest first, shaky first, up to 5, and no new problem that day if more than 5 are left.

**Note on the coding page:** its "Due for review" list runs on the original plan calendar, one week ahead of yours. It will show Week 4's old solves (215, 56, 253, 295, 1797) now and Week 7's (139, 329, 516, 698, 322, 1143) from Nov 23. Use this pack's dates, not the page's.

### 0b. Reviews landing inside Week 7 (assuming every redo before then is Clean)

| Day | Fixed by the Week 4 pack | Week 7 items | Count before Weeks 5–6 |
| --- | --- | --- | --- |
| Mon Nov 30 | — | — | 0 |
| Tue Dec 1 | — | 309 (R1) | 1 |
| Wed Dec 2 | — | 312, 139 (R1) | 2 |
| Thu Dec 3 | — | 1235, 1472 (R1) | 2 |
| Fri Dec 4 | 1834 (R4) | 309 (R2) · 329, 322, 1143 (R1) | **5, at the cap** |
| Sat Dec 5 | 630, 295 (R4) | 312, 139 (R2) · 1039 (R1) | **5** |
| Sun Dec 6 | 220, 355 (R4) | 1235, 1472 (R2) | 4 |

Week 5 and 6 items (first tried Nov 16–29) will add R2 and R3 redos to every one of these days. Those packs don't exist yet, so I'll fill them in when they do. **Expect at least one day over the cap.** When that happens, that day's new problem moves to the next day under the cap. Friday's check (1039) still runs, since it's the week's test.

### 0c. Dates

The plan has Week 7 on Nov 23–29. Your calendar runs a week behind (Week 3 is Nov 2–8 and Week 4 is Nov 9–15), so this pack runs **Mon Nov 30 – Fri Dec 4**. Thanksgiving (Thu Nov 26) now falls in your Week 6. You asked for the light version anyway, so it stays light.

**Knock-on:** with the one-week shift, Week 9 lands on Dec 14–20, which is Week 10's mock week, and Gate 3 (Dec 12) would come before Week 9 ends. Decide by Week 6 whether to compress a week or drop the shift. Tell me and I'll re-date.

**Tools:** `etcd` isn't installed on this Mac (`brew install etcd` gives you `etcd` and `etcdctl`). Python 3 and git are present for the RaftScope lab.

### 0d. This week's problems

| # | Problem | Diff | Role | Your history (LeetCode, Oct 6) | How it's run |
| --- | --- | --- | --- | --- | --- |
| 322 | Coin Change | M | Core | May 2026, 3 submits | Cold redo, ≤ 25 min |
| 139 | Word Break | M | Core | **Dec 2024**, 1 submit (fading: shaky) | Cold redo, ≤ 25 min, **first in its day** |
| 1143 | Longest Common Subsequence | M | Core | May 2026, 1 submit | Cold redo, ≤ 20 min |
| 329 | Longest Increasing Path in a Matrix | H | Core | **Oct 2025**, 3 submits (fading: shaky) | Cold redo, ≤ 25 min, **first in its day** |
| 309 | Best Time to Buy and Sell Stock with Cooldown | M | Required · **Learn** | New | Learn row: 40 min alone |
| 312 | Burst Balloons | H | Required · Apply | New | First try, 50 min |
| 1235 | Maximum Profit in Job Scheduling | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 1472 | Design Browser History | M | Required · practical | New | First try, 15 min + follow-up aloud |
| 1039 | (Friday check: don't open it before Friday) | M | Check | New | 45 min, alone, no hints, Friday |

⚠ **The coding page's two Week 7 templates are full solutions: the interval DP one is 312 and the bitmask one is 1986.** Don't open them until your 312 first try is done, or it counts as "Needed the solution". Monday's drill (§d0) uses neutral problems instead.

⚠ **The coding page's "Core idea" column is a hint rung.** Cover it for 309, 312 and 1235 until 25 minutes have passed.

### 0e. Day by day

| Day | Reviews first | Infra / apply | Code | Other |
| --- | --- | --- | --- | --- |
| **Mon Nov 30** | Whatever 0a/0b leaves + W5–W6 items (30) | §a warm-up cold (10) → §b questions cold → read → K-b (45) | §d0 template drill (15) → **309** (Learn, 40) | `brew install etcd` tonight (5) |
| **Tue Dec 1** | 309 (R1) + carried (25) | §c Lab 1 RaftScope (30) + Lab 2 etcd (20) | **312** (50) → **139\*** cold redo if time is left, else Thu | Recall warm-up (10) |
| **Wed Dec 2** | 312, 139 (R1) (20) | §b2 teach-backs, recorded, no notes (25) · §e **Drill 1** split brain (30) | **1235** (Learn, 40) → **1472** (practical, 15) | — |
| **Thu Dec 3** | 1235, 1472 (R1) (15) | §h cheat sheet from memory (30) · §k story (20) | **329\***, **322**, **1143** cold redos (50) | — |
| **Fri Dec 4** | 309 (R2) · 329, 322, 1143 (R1) · 1834 (R4) = **5** (25) | §e **Drill 2** lease expires mid-write (30) · §e **Drill 3** election stuck, timed 20 min (in the freed design slot) | **1039** check, 45 min, alone | — |
| Sat Dec 5 | 312, 139 (R2) · 1039 (R1) · 630, 295 (R4) = **5** | Rest. Optional: §f design, 40 min | — | — |
| Sun Dec 6 | 1235, 1472 (R2) · 220, 355 (R4) = 4 | Cheat sheet rewritten from memory (30) · plan Week 8 (15) | Extras (§d2) only if reviews are at 0 | — |

\* shaky by history: first in their day.

### 0f. Session rules (same as Weeks 2–4)

- Say **"start 309"** (or any number) and I log the start time. 60-second approach aloud, brute force first, complexity before code.
- Hints: one rung per request, and only after 25 minutes stuck. A Learn row gets the full 40 minutes first. No hints at all during the Friday check. If you ask for a solution, you get the next rung instead.
- I compile your file with `clang++ -std=c++17 -Wall -Wextra` and show you the compile errors. I never fix or rewrite your code.
- Marks: first tries are **Solved alone / Needed the solution**. Redos are **Clean** (first submit, under 25 minutes, no hint), **Shaky** (slow, 2+ submits, or one hint) or **Failed**.

---

## (a) Day 1 recall warm-up (cold, aloud, before any reading)

10 questions: 7 from Week 7 (answer from what you already know) and 3 from earlier weeks. One or two sentences each. Mark each ✓ / ✗ before opening K-a.

1. A 3-replica store uses W = 2, R = 2. Why does a read see the latest acknowledged write? Name one way it still returns stale data.
2. Why do people run 3 or 5 consensus nodes, never 4?
3. In Raft, a follower hears nothing from the leader. Walk through what happens until a new leader exists.
4. Two nodes time out at the same moment and split the vote. What stops this from repeating forever?
5. A lock service grants a 30 s lease. The holder hits a 40 s GC pause, then writes. What goes wrong, and what one mechanism stops it?
6. You add a 5th cache node. With `hash(key) % N`, roughly what fraction of keys move? With a consistent-hash ring?
7. What's the difference between linearizability and serializability, in one sentence each?
8. *(Week 6)* What's an error budget, and what do you do when it's spent?
9. *(Week 2, F4)* Connect times cluster at exactly ~1 s and ~3 s under a burst. What's overflowing, and which kernel setting is involved?
10. *(Week 1)* What must PID 1 in a container do that a normal process doesn't?

---

## (b) Infra brief: questions first, then reading

**Read (Monday, 45 min total, skim the rest):**
- DDIA ch. 5: "Leaders and Followers", "Problems with Replication Lag", "Leaderless Replication: Quorums for reading and writing" and "Limitations of Quorum Consistency".
- DDIA ch. 9: "Linearizability" (what it is and the cost) and "Fault-Tolerant Consensus".
- DDIA ch. 8, the short section "The leader and the lock" / "Fencing tokens" (about 4 pages). Fencing tokens are in ch. 8, not ch. 9: check this in your edition.
- Raft paper (Ongaro and Ousterhout, 2014): §5.1–5.4 and Figure 2. Skim §8 (client interaction).

**The five things I'd say.** Before reading, try to state each one in a sentence. The reference versions are in K-b.

1. What a quorum guarantees, and the condition for it.
2. How Raft picks a leader, and who's *not allowed* to win.
3. When a Raft log entry counts as committed.
4. Why a lease alone doesn't give mutual exclusion, and what fixes it.
5. What consistent hashing buys you over `mod N`, and why virtual nodes exist.

**Failure modes to name unprompted (fill in the cause of each before reading K-b):**

| Symptom | Cause? |
| --- | --- |
| Two nodes both act as primary after a network blip | |
| A client reads a value older than one it wrote a moment ago | |
| Writes hang cluster-wide after two of three nodes die | |
| Leader changes every few seconds; term number keeps climbing | |
| A rejoining node forces a fresh election even though the leader is healthy | |
| A lease holder writes after its lease expired | |
| One cache node at 90% CPU, the others at 20% | |
| An acknowledged write is gone after failover | |

### (b2) Teach-backs: four 2-minute explains (Wednesday, recorded, no notes)

Redo any with more than 5 stumbles. Outlines and follow-up answers are in K-b2.

- **T1 Quorums.** N, W, R; why W + R > N; what it doesn't promise. *Follow-up: "With W = 1, R = N, what did you trade?"*
- **T2 Raft election and replication.** Terms, timeouts, votes, the election restriction, the commit rule. *Follow-up: "Why can't a new leader just count replicas of an old-term entry and commit it?"*
- **T3 Leases and fencing tokens.** Why a lease holder can still corrupt data, and what the storage must check. (This is a Gate 3 question word for word.) *Follow-up: "Your storage is S3. Where does the token check live?"*
- **T4 Consistent hashing.** Ring, virtual nodes, what moves when a node joins. *Follow-up: "One key is hot. Does the ring help?"*

---

## (c) Lab sheet (Tuesday, 50 min, real commands; write down what you see)

**Rule:** before each step, write your prediction in one line. Then run it and write what happened. Expected observations are in K-c.

### Lab 1: three Raft nodes in RaftScope, then kill the leader (30 min)

raft.github.io embeds RaftScope with **5** servers, and it has no setting for the count. A local copy with a one-line edit gives you 3.

```bash
cd ~/"Platform Prep"/week_packs/week07_lab
git clone --depth 1 https://github.com/ongardie/raftscope.git
cd raftscope
sed -i '' 's/^var NUM_SERVERS = 5;/var NUM_SERVERS = 3;/' raft.js
grep -n '^var NUM_SERVERS' raft.js        # expect: 13:var NUM_SERVERS = 3;
python3 -m http.server 8000               # leave running; Ctrl-C when done
```
Open `http://localhost:8000`. Controls: **Space** pauses, **C** sends a client request to the leader, **right-click a server** gives stop / resume / restart / time out / request, **click a server** shows its term, votedFor and commitIndex, and **right-click a message** lets you drop it. Drag the speed slider to slow things down.

| Step | Do | Predict first |
| --- | --- | --- |
| 1 | Let it run from the start | Who becomes leader, at what term, with how many votes? |
| 2 | Press **C** three times | When does each entry become committed? Check commitIndex on each server |
| 3 | Right-click the leader → **stop** | How long until a new leader? What term? Do client requests still commit? |
| 4 | Press **C** twice more, then **resume** the old leader | What role does it come back as? What happens to its log? |
| 5 | Stop the leader **and** one follower (one server left) | Does the last server ever become leader? What happens to its term? |
| 6 | Resume one of the two. Then: stop a follower, press **C** three times, stop the leader, resume the follower you stopped first | Two servers are alive and one log is behind. Which one can win, and why? |
| 7 | Press **C**, then **Space** at once (before the entry reaches anyone), stop the leader, unpause | Is that entry lost? Is that a safety bug? |

### Lab 2: the same thing in real etcd, plus a lease and a fencing token (20 min, or Thursday)

```bash
brew install etcd                          # once
cd ~/"Platform Prep"/week_packs/week07_lab
./etcd3.sh start                           # 3 nodes: clients on :2379, :22379, :32379
export EP=127.0.0.1:2379,127.0.0.1:22379,127.0.0.1:32379
etcdctl --endpoints=$EP endpoint health
etcdctl --endpoints=$EP put /cfg/x 1
```

**2a. Kill the leader.**
```bash
./etcd3.sh status                          # find IS LEADER = true; note RAFT TERM
./etcd3.sh kill <leader number>
sleep 3; ./etcd3.sh status
grep -h "became leader" etcd-data/n*.log | tail -2
etcdctl --endpoints=$EP put /cfg/x 2       # does it work?
```

**2b. Lose quorum.**
```bash
./etcd3.sh kill <another live node>        # one node left
etcdctl --endpoints=$EP --command-timeout=5s put /cfg/x 3
etcdctl --endpoints=$EP --command-timeout=5s get /cfg/x
etcdctl --endpoints=$EP get /cfg/x --consistency=s
./etcd3.sh up 1; ./etcd3.sh up 2; ./etcd3.sh up 3   # bring them back ("was not running" is fine)
```
Predict: which of the three commands answers, and is its answer guaranteed fresh?

**2c. A lease that expires.**
```bash
etcdctl --endpoints=$EP lease grant 15
etcdctl --endpoints=$EP put /locks/compaction worker-A --lease=<lease id>
etcdctl --endpoints=$EP lease timetolive <lease id>
sleep 16; etcdctl --endpoints=$EP get /locks/compaction
```

**2d. A lock, a paused holder, and the fencing token.** Use two terminals, both with `EP` exported.
```bash
# Terminal 1
etcdctl --endpoints=$EP lock --ttl=10 compaction        # prints the key it holds, then blocks
# Terminal 2
etcdctl --endpoints=$EP lock --ttl=10 compaction        # blocks: waiting
# Terminal 3 (or Terminal 2 after Ctrl-C): freeze holder #1 like a long GC pause
pgrep -f "lock --ttl=10 compaction" | head -1 | xargs kill -STOP
# wait ~12 s and watch Terminal 2
etcdctl --endpoints=$EP get --prefix compaction/ -w json  # note each key's create_revision
pgrep -f "lock --ttl=10 compaction" | head -1 | xargs kill -CONT   # wake holder #1; what does it print?
```
Predict: when does Terminal 2 get the lock? Which number could the storage use as a fencing token? Does holder #1 know, the moment it wakes, that it lost the lock?

**Cleanup:** `./etcd3.sh clean`

---

## (d) Coding

### (d0) Monday template drill (blank file, 15 min, compiled)

**Templates (names only; no reference code anywhere in this pack):**
- **W7-T1: Interval DP skeleton.** A bottom-up version filled by interval length, and a top-down memoised version. Toy problem: **matrix-chain multiplication cost** (`dims` has n+1 numbers for n matrices).
- **W7-T2: Bitmask DP skeleton.** Bit idioms, submask enumeration, and `dp[mask]`. Toy problem: **assignment**, where n workers take n jobs, one each, at minimum total cost, with `dp[mask]` = best cost once the jobs in `mask` are taken by the first `popcount(mask)` workers.

**Format:**
1. Start the timer on a blank `w7_templates.cpp`. No notes, no autocomplete, no lookups.
2. Write both templates and a `main()` with `assert`s that prove the behaviours below.
3. Say "compile" and I run `clang++ -std=c++17 -Wall -Wextra w7_templates.cpp && ./a.out`.

**Behaviours your asserts must prove:**

| T1 (interval DP) | T2 (bitmask DP) |
| --- | --- |
| `{10,30,5,60}` → 4500 | popcount of `0b1011` is 3 |
| `{40,20,30,10,30}` → 26000 | lowest set bit of 12 is 4; dropping it gives 8 |
| `{10,20,30,40,30}` → 30000 | the non-empty submasks of `0b1011` number exactly 7 |
| one matrix `{5,10}` → 0 | over every mask of n = 4, submasks including the empty one total 81 (= 3⁴) |
| bottom-up and top-down agree on every case above | assignment on `{{9,2,7,8},{6,4,3,7},{5,8,1,8},{7,6,9,4}}` → 13 |
| products are computed in `long long` | an "is bit i set" test written with explicit parentheses |

**Pass** = under 15:00, zero warnings, every assert passes, no lookup. **Fail** = any of those missed. A failed template goes on the review schedule like a problem (row in §i).

### (d1) Pattern map: the 9 problems

No pattern names here: the pattern is rung 1 of each ladder in K-d. Answer the question in the fourth column aloud before you code.

| # | Problem | Why it's in Week 7 | One question to answer before coding | Mark |
| --- | --- | --- | --- | --- |
| 322 | Coin Change | The base "min over choices" DP every other DP builds on | What's the smallest subproblem, and what's its answer? | |
| 139 | Word Break | Prefix DP: "can the first i characters be done?" | Given the answer for every shorter prefix, how do you decide prefix i? | |
| 1143 | Longest Common Subsequence | The 2-D table you'll reuse for diff and edit distance | What do you do when the two last characters match, and when they don't? | |
| 329 | Longest Increasing Path in a Matrix | DP over a graph whose edges only go "up", so it has no cycles | Why don't you need a visited set? | |
| 309 | Stock with Cooldown | A DP whose state is "what am I doing today", which is how a retry or backoff controller is modelled | List every state you can be in at the end of a day, and the arrows between them | |
| 312 | Burst Balloons | Interval DP, the hardest DP family in a typical loop | If you choose the *first* balloon to burst, why are the two sides not independent? | |
| 1235 | Max Profit in Job Scheduling | Weighted interval scheduling: which jobs to admit onto one machine | After sorting, how do you find the last job that doesn't overlap job i, fast? | |
| 1472 | Design Browser History | Practical: undo/redo history, the same shape as config rollback | What happens to the "forward" pages when you visit a new one? | |
| 1039 | Friday check | **Sealed until Friday** | **Sealed** | |

### (d2) After-required rows (Sunday, only if reviews are at 0)

In order: **516\*** (Jan 2025: an old-solve redo, the simplest interval DP) → **698\*** (Jan 2025, 8 submits: an old-solve redo, the first bitmask DP) → 1547 → 1986 → 188 → 1335 → 1723 → 1000 (stretch). 516 and 698 are already on the coding page's review list, so they count as reviews, not new problems. Ask me for hint ladders on any of these.

---

## (e) Troubleshooting drills (symptoms only)

Run each one aloud with "Can Some Students Handle Cold Fixes": **C**larify, **S**cope, **S**tabilize, **H**ypothesize, **C**heck, **F**ix and prevent. Ask me for facts as you would ask an interviewer. Each check must name the result that confirms or rules out a hypothesis. Interviewer sheets are in K-e.

### Drill 1: split brain (Wednesday, 30 min)

> 02:10. An order service runs a primary/standby Postgres pair, one VM in zone A and one in zone B. Failover is keepalived: the node that holds the virtual IP is the primary, and the standby promotes itself when it misses heartbeats. At 02:04 a network change dropped traffic between the two zones for about 40 seconds. Since then customers report orders that "vanish" after they refresh, and support has tickets for duplicate order numbers. Both database hosts are up and healthy on their dashboards.

### Drill 2: lease expires mid-write (Friday, 30 min)

> A nightly compaction job rewrites a table's data files in an object store and then overwrites a single `manifest.json` that lists the live files. Only one worker may compact a table at a time, so workers take a lock in etcd with a 30-second lease and renew it every 10 seconds. Last night, table `events_2026_12` started returning "file not found" for some reads. The manifest lists files from two different compaction runs. Both worker-A and worker-B logged "acquired lock for events_2026_12", about 50 seconds apart. Nobody changed the lock code this quarter.

### Drill 3: leader election stuck (Friday, timed 20 min)

> A 3-node etcd cluster backs a Kubernetes control plane. This afternoon `kubectl` calls started failing intermittently with `etcdserver: request timed out` and `etcdserver: leader changed`. `etcdctl endpoint status` shows the leader moving between nodes every few seconds, and RAFT TERM went from 41 at noon to over 3,000 now. All three etcd processes are running and every pair of nodes can ping each other. This morning the platform team moved the etcd nodes to a new instance type and storage class "to cut cost".

---

## (f) Design: distributed lock and lease service

**Not scheduled this week (light week, no Friday design).** It's a Gate 3 item ("draw the lock service with tradeoffs"), so draw it once before Gate 3. Saturday Dec 5 is the optional slot; otherwise use the first free design block in Week 8.

**Prompt:** Design a lock and lease service for your platform: Airflow workers, compaction jobs and controllers that need "only one of us at a time" on a named resource. About 10,000 clients and 5,000 lock operations a second at peak, inside one region across three zones.

**Your drawing first (40 min, on paper, from blank).** Walk the six steps, "Real Apps Deserve Deep Failure Tests":

1. **Requirements.** What does "holds the lock" promise? Fairness? Lock vs lease? Latency and scale numbers?
2. **API.** The calls, their arguments and their return values. What does acquire return besides "OK"?
3. **Data.** What's stored per lock and per lease, where, and how it survives a crash?
4. **Deep dive.** Pick one: (a) how expiry is measured and what happens to every lease when the server leader changes, or (b) how waiters queue without a thundering herd.
5. **Failures.** Server leader crash, client GC pause, network partition, clock jump, quorum loss.
6. **Tradeoffs.** Consensus-backed vs Redis; coarse vs fine locks; what changes at 10× clients.

Then compare against the rubric in K-f and redraw the misses from memory.

---

## (g) Flashcards (10 new cards: put them in Anki; answers in K-g)

| # | Type | Front |
| --- | --- | --- |
| 1 | Explain | W + R > N: what does it guarantee? Name two ways it still returns stale data. |
| 2 | Explain | Why can a lease holder still corrupt data? |
| 3 | Explain | What is a fencing token, who issues it, and who checks it? |
| 4 | Explain | Raft's election restriction: which candidate can't win, and why? |
| 5 | Explain | When is a Raft entry committed? |
| 6 | Explain | Why 3 or 5 consensus nodes, never 4? |
| 7 | Explain | Consistent hashing: what moves when a node joins, and why virtual nodes? |
| 8 | Command | etcd: which node is the leader, and what's the term? |
| 9 | Command | etcd: create a 15 s lease, attach a key to it, and see the time left. |
| 10 | Template | Write W7-T1 (interval DP) and W7-T2 (bitmask DP) skeletons from memory. |

---

## (h) Cheat sheet skeleton (Thursday: fill it from memory; Sunday: rewrite it from blank)

The skeleton is in `cheat_sheets/week07_distributed_systems.md`. Compare it with K-h after writing.

---

## (i) Review-due table (Week 7 items)

Dates assume every redo is **Clean** and that each first try happens on its planned day. **Shaky** → same stage again in 2 days. **Failed** → back to Review 1 tomorrow. Rewrite the row's dates when that happens.

### Problems

| # | First try | Mark | R1 (+1) | Mark | R2 (+3) | Mark | R3 (+7) | Mark | R4 (+14) | Mark | R5 (+30) | R6 (+60) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 309 | Mon Nov 30 | | Tue Dec 1 | | Fri Dec 4 | | Fri Dec 11 | | Fri Dec 25 | | Sun Jan 24 | Thu Mar 25 |
| 312 | Tue Dec 1 | | Wed Dec 2 | | Sat Dec 5 | | Sat Dec 12 | | Sat Dec 26 | | Mon Jan 25 | Fri Mar 26 |
| 139\* | Tue Dec 1 | | Wed Dec 2 | | Sat Dec 5 | | Sat Dec 12 | | Sat Dec 26 | | Mon Jan 25 | Fri Mar 26 |
| 1235 | Wed Dec 2 | | Thu Dec 3 | | Sun Dec 6 | | Sun Dec 13 | | Sun Dec 27 | | Tue Jan 26 | Sat Mar 27 |
| 1472 | Wed Dec 2 | | Thu Dec 3 | | Sun Dec 6 | | Sun Dec 13 | | Sun Dec 27 | | Tue Jan 26 | Sat Mar 27 |
| 329\* | Thu Dec 3 | | Fri Dec 4 | | Mon Dec 7 | | Mon Dec 14 | | Mon Dec 28 | | Wed Jan 27 | Sun Mar 28 |
| 322 | Thu Dec 3 | | Fri Dec 4 | | Mon Dec 7 | | Mon Dec 14 | | Mon Dec 28 | | Wed Jan 27 | Sun Mar 28 |
| 1143 | Thu Dec 3 | | Fri Dec 4 | | Mon Dec 7 | | Mon Dec 14 | | Mon Dec 28 | | Wed Jan 27 | Sun Mar 28 |
| 1039 | Fri Dec 4 | | Sat Dec 5 | | Tue Dec 8 | | Tue Dec 15 | | Tue Dec 29 | | Thu Jan 28 | Mon Mar 29 |
| W7-T1/T2 (only if failed) | Mon Nov 30 | | Tue Dec 1 | | Fri Dec 4 | | Fri Dec 11 | | | | | |

\* For a redo of an old solve, the "First try" column is the first redo; mark it Clean / Shaky / Failed. Week 7 R3 redos (Dec 11–15) land in Week 8 and Gate 3 week: count them there.

### Concepts (cards, labs, teach-backs, drills, design)

Same 1-3-7-14-30-60 spacing. A card is Clean if answered word-perfect in under 30 s, a teach-back if ≤ 5 stumbles, a drill if it scores ≥ 3 on the routine, the design if it hits every rubric line from memory. These take 2–5 minutes each and don't count toward the 5-problem cap.

| Item | First | Mark | +1 | Mark | +3 | Mark | +7 | Mark | +14 | Mark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cards 1–10 | Fri Dec 4 | | Sat Dec 5 | | Mon Dec 7 | | Fri Dec 11 | | Fri Dec 18 | |
| Lab 1–2 (redo the predictions from memory) | Tue Dec 1 | | Wed Dec 2 | | Fri Dec 4 | | Tue Dec 8 | | Tue Dec 15 | |
| T1–T4 teach-backs | Wed Dec 2 | | Thu Dec 3 | | Sat Dec 5 | | Wed Dec 9 | | Wed Dec 16 | |
| Drill 1 split brain | Wed Dec 2 | | Thu Dec 3 | | Sat Dec 5 | | Wed Dec 9 | | Wed Dec 16 | |
| Drill 2 lease mid-write | Fri Dec 4 | | Sat Dec 5 | | Mon Dec 7 | | Fri Dec 11 | | Fri Dec 18 | |
| Drill 3 election stuck | Fri Dec 4 | | Sat Dec 5 | | Mon Dec 7 | | Fri Dec 11 | | Fri Dec 18 | |
| Design: lock service | (when drawn) | | +1 (redraw) | | | | | | | |
| Story: disagreement | Thu Dec 3 | | Fri Dec 4 | | Sun Dec 6 | | Thu Dec 10 | | Thu Dec 17 | |

(For concepts, +3 / +7 / +14 count from the first attempt.)

---

## (j) No Saturday mock this week

It's a light week. Drills 1–3 and the Friday check stand in for it. The Week 8 mock draws 30% from Week 7: expect the lease/fencing question there.

---

## (k) Story: a technical disagreement I resolved

**Rule:** only facts you supply. Every blank stays blank until you fill it. I won't suggest events, people or numbers. The plan lists this as one of the two stories that need a real event from you.

**Facts I need from you first** (answer in a message, or write them here):
- Which company, which year, which system?
- Who disagreed with whom (by role: your lead, a peer team, a principal engineer, a manager)?
- What exactly was each side's position, in one sentence each?
- How was it settled (data, a prototype, a written proposal, a compromise, escalation)?
- What happened afterwards, and was there a number (latency, cost, incidents, time saved)?
- Were you wrong about anything?

Pick one where the disagreement was about a technical decision, not a person. A case where you changed your mind is as strong as one where you won.

**Structure (2 minutes spoken, then stop):**

| Beat | ~Time | Your words |
| --- | --- | --- |
| **Situation**: the system, the decision on the table, why it mattered | 20 s | |
| **The disagreement**: their position and its strongest reason; your position and yours | 20 s | |
| **My decision**: what you did to settle it (the evidence, the experiment, the doc, the conversation) | 35 s | |
| **Tradeoff**: what your chosen path cost, or what you gave up to reach agreement | 15 s | |
| **Number**: the measurable result | 10 s | |
| **Lesson**: one thing you now do differently in disagreements | 20 s | |

**Interviewer probes (practise each in ≤ 30 s):**
1. What was the strongest argument on the other side?
2. How did you make sure you weren't just being stubborn?
3. What data did you have, and what did you wish you had?
4. Did the other person agree in the end, or disagree and commit?
5. What would you have done if the decision had gone against you?
6. How did this affect your working relationship afterwards?
7. Looking back, was the decision right? What would you change?
8. Tell me about a time you were the one who was wrong.

---
---

# ANSWER KEY

## K-a. Warm-up answers

1. Any write set of size W and any read set of size R must share at least one replica when W + R > N (2 + 2 > 3), so every read touches someone with the latest acknowledged write and picks the highest version. Still stale: a sloppy quorum (hinted handoff writes to nodes outside the home N); two concurrent writes resolved last-writer-wins by skewed clocks; a write that succeeded on fewer than W nodes isn't rolled back and may or may not be seen; a node holding the new value fails and is restored from an older replica.
2. Majority quorum = ⌊N/2⌋ + 1. Three nodes tolerate 1 failure, 4 nodes still tolerate only 1 (quorum 3), and 5 tolerate 2. The 4th node adds cost and one more voter to wait for, with no extra fault tolerance, and an even split across two zones can leave neither side with a majority.
3. The follower's election timer fires (randomised, the paper uses 150–300 ms). It becomes a candidate: currentTerm + 1, votes for itself, sends RequestVote to all. Each server grants at most one vote per term, and only if the candidate's log is at least as up-to-date as its own. A majority of votes makes it leader; it immediately sends heartbeats (empty AppendEntries) to stop other elections. Seeing a higher term makes any candidate or leader step down.
4. Randomised election timeouts: after a split vote, each candidate picks a new random timeout, so one almost always fires first and wins before the others time out.
5. The lease expired during the pause and another client got the lock. The paused client doesn't know: from its point of view no time passed, so it writes, and two holders interleave. The fix is a **fencing token**: a number that goes up with every grant, sent with every write, with the storage rejecting any token lower than the highest it has seen.
6. Going from `% 4` to `% 5` moves about 4/5 of keys (a key stays only if `h % 4 == h % 5`). With a ring, only about 1/5 move: the keys in the arcs the new node takes over.
7. Linearizability: every operation appears to take effect at one instant between its call and return, so reads never go back in time (a property of single objects, about recency). Serializability: transactions give the same result as some serial order, which need not match real time (a property of multi-object transactions, about isolation).
8. *(W6)* Error budget = 1 − SLO over the window (99.9% over 30 days ≈ 43 minutes). When it's spent: freeze risky launches, put the effort into reliability work until it recovers. The policy is agreed beforehand, not debated during an incident.
9. *(W2 F4)* The server's listen (accept) queue overflows and the kernel silently drops SYNs; the client retransmits after 1 s, then 3 s. The settings are `net.core.somaxconn` and the app's `listen()` backlog. Check with `ss -lnt` (Recv-Q vs Send-Q) and `nstat -az | grep -i listen` (ListenOverflows, ListenDrops).
10. *(W1)* Reap zombie children (wait for orphans re-parented to it) and handle or forward signals, because the kernel doesn't apply default signal actions to PID 1 in a namespace: an unhandled SIGTERM is ignored. Use `tini` or `--init`, or exec-form so your app is PID 1 and handles SIGTERM itself.

---

## K-b. The five things I'd say, and the failure modes

**1. Quorums.** "With N replicas, writes wait for W acks and reads ask R nodes. If W + R > N, every read overlaps every write, so a read sees the latest acknowledged write. N = 3, W = 2, R = 2 is the common setting. It's not linearizable on its own: sloppy quorums, concurrent writes resolved by clocks, and partial failed writes all break it."

**2. Leader election.** "Raft splits time into terms; each term has at most one leader. A follower that misses heartbeats for a random timeout becomes a candidate, bumps the term and asks for votes. Each node votes once per term, and only for a candidate whose log is at least as up-to-date as its own (compared by last log term, then last index). So a node that's missing committed entries can't win."

**3. Commit rule.** "The leader appends the entry, replicates it with AppendEntries, and commits once a majority stores it. It only commits by counting replicas for entries from its own current term; older entries are committed indirectly when a newer entry from its term commits (Figure 8 in the paper). That's why a new leader commits a no-op at the start of its term. Committed entries are never lost; uncommitted ones can be overwritten."

**4. Leases and fencing.** "A lease is a lock with a timeout, so a dead holder can't block everyone forever. But expiry is measured on the server, and a holder can pause (GC, VM migration, page fault, SIGSTOP) past expiry without knowing. So the lock service hands out a monotonically increasing fencing token with each grant, the client sends it with every write, and the storage rejects tokens lower than the highest it has seen. Without a check at the resource, a lease only makes overlap unlikely, not impossible."

**5. Consistent hashing.** "Hash nodes and keys onto the same ring; a key belongs to the first node clockwise. Adding or removing a node only moves the keys in its arcs, about K/N, instead of nearly all keys with `mod N`. Each physical node gets 100 to 200 virtual nodes so load evens out, you can weight bigger machines, and a failed node's load spreads over many peers instead of one neighbour. It doesn't fix a single hot key: for that, replicate or split the key."

**Failure modes:**

| Symptom | Cause |
| --- | --- |
| Two primaries after a network blip | Split brain: failover decided by heartbeat, not by a majority; no fencing of the old primary |
| Client reads older than its own write | Async replication lag; read went to a follower (fix: read-your-writes by reading from the leader, or waiting for a replica to reach the client's last write position) |
| Writes hang after 2 of 3 die | Quorum loss: correct behaviour, the cluster prefers being unavailable to being wrong |
| Leader flaps, term climbs | Election timeout too short for real latency: slow disk fsync or network RTT delays heartbeats |
| Rejoining node forces an election | It timed out alone, bumped its term, and its higher term makes the leader step down. Fix: pre-vote |
| Lease holder writes after expiry | Process pause or clock jump; no fencing token check at the resource |
| One cache node hot | Too few virtual nodes (uneven arcs), or one hot key |
| Acknowledged write lost after failover | Async replication or `w:1` style acks: the old leader acknowledged before a majority had it, and the new leader never saw it (Mongo calls it a rollback) |

---

## K-b2. Teach-back outlines and follow-up answers

### T1: Quorums (2 minutes, 6 beats)
1. Setup: N replicas, W, R, versions on every value.
2. The overlap argument: W + R > N means at least one node is in both sets.
3. Common settings: 3/2/2; W = N for read-heavy (fast reads, writes stop if one node is down); R = N for write-heavy.
4. What it doesn't promise: sloppy quorums, concurrent writes with last-writer-wins, partial writes, not linearizable without read repair and more.
5. Fault tolerance: W < N lets writes survive N − W failures; R < N same for reads.
6. Contrast with Raft: a leader orders everything, so a majority quorum gives linearizable writes.

**Follow-up (W = 1, R = N):** writes are fast and survive N − 1 failures, but every read needs all N nodes up, so one dead replica stops reads. A write acked by one node can be lost if that node dies before replicating.

### T2: Raft election and replication (2 minutes, 6 beats)
1. Roles and terms; terms work as a logical clock; a higher term always wins.
2. Election: random timeout → candidate → term + 1 → RequestVote → majority → leader → heartbeats.
3. Safety of votes: one vote per term, persisted (currentTerm and votedFor go to disk before replying).
4. Election restriction: vote only for an up-to-date log (last term, then last index).
5. Replication: AppendEntries with prevLogIndex/prevLogTerm; followers reject on mismatch and the leader backs up until logs agree, then overwrites the follower's conflicting tail.
6. Commit: majority stored + entry from the current term; then apply to the state machine and reply to the client.

**Follow-up (old-term entries):** an entry from an older term can be on a majority and still be overwritten by a future leader that never had it (Figure 8): a server that missed it can still win an election with votes from servers that also missed it. Once an entry from the *current* term is on a majority, the election restriction guarantees every future leader has it and everything before it. So the leader commits old entries only indirectly.

### T3: Leases and fencing tokens (2 minutes, 6 beats)
1. Why leases: a lock whose holder died must free itself, so it gets a TTL.
2. The gap: the server decides expiry by its clock; the client can't observe its own pause.
3. Example: a 30 s lease, a 40 s GC pause, a new holder, then the old holder's write lands on top.
4. Fencing token: a monotonic number per grant (etcd revision, ZooKeeper zxid), sent with every write.
5. The resource checks it: rejects any token below the highest seen. That check must be atomic with the write.
6. Without that check (storage can't compare): a client-side safety margin (stop well before expiry), shorter work units, idempotent writes. All of these make it less likely, none make it impossible.

**Follow-up (S3 or GCS):** the object store doesn't know your token, so make the write conditional: put the token (or the version you read) in the object and write with a conditional PUT on the ETag or generation you last saw (`If-Match`, GCS `ifGenerationMatch`), or put a single metadata row in a store that supports compare-and-set (`etcd txn` comparing the revision, a database `UPDATE ... WHERE token < :mine`). The manifest swap is the one write that must be fenced.

### T4: Consistent hashing (2 minutes, 6 beats)
1. The problem: `mod N` remaps almost every key when N changes, causing a cache miss storm or a full data shuffle.
2. The ring: nodes and keys hashed into one space; a key goes to the first node clockwise.
3. Join and leave: only neighbouring arcs move, about K/N keys.
4. Virtual nodes: many points per node give even load, weighting, and failure load spread across many nodes.
5. Replication: store on the next R distinct physical nodes clockwise.
6. Alternatives: rendezvous (highest random weight) hashing, jump consistent hash, bounded-load consistent hashing.

**Follow-up (hot key):** no. The ring spreads keys, not load within one key. Fixes: replicate the hot key to several nodes and read from any of them, add a suffix to split it into K sub-keys, or put a local in-process cache in front.

---

## K-c. Lab: expected observations

### Lab 1 (RaftScope, 3 servers)

RaftScope's time unit is microseconds: election timeout 100–200 ms (random), heartbeats every 50 ms, message latency 10–15 ms.

1. All three start as followers in term 1. The first timer to expire becomes a candidate in **term 2**, votes for itself, and needs **one more vote** (2 of 3). It wins and starts sending heartbeats; the others' timers keep resetting. **Proves:** majority of 3 is 2; a leader exists only after votes, never by default.
2. Each entry shows up on the leader, then the followers. The leader's commitIndex advances once **one follower** has it (leader + 1 = 2 of 3); followers learn the new commitIndex on the next AppendEntries. **Proves:** commit = majority stored, not all.
3. After the leader stops, the next follower whose timer expires (100–200 ms later) becomes a candidate in term 3 and wins with 2 of 3 (itself + the other survivor). Requests commit again with 2 nodes. **Proves:** a 3-node cluster survives 1 failure.
4. The old leader comes back as a **follower** in its old term. The first message from the new leader carries a higher term, so it updates its term, and AppendEntries fills in the entries it missed. **Proves:** higher term wins; logs converge from the leader.
5. The last server times out over and over, term 4, 5, 6..., never getting a second vote. Client requests go nowhere. **Proves:** no quorum means no progress, and no wrong answers either (this is the "election stuck" pattern from Drill 3's first hypothesis).
6. The server that was stopped first is missing the committed entries. If it times out first, the other **rejects** its vote (its log is less up-to-date); the other eventually times out, wins, and repairs the lagging log. **Proves:** the election restriction: a node missing committed entries can't become leader.
7. The entry existed only on the old leader. The new leader is elected without it, and when the old leader comes back, its uncommitted entry is overwritten. **Not a safety bug:** it was never committed, so no client got "success". A client whose request timed out retries, which is why Raft §8 says clients must be able to retry safely (unique request IDs).

### Lab 2 (etcd)

- `endpoint health`: each endpoint `is healthy: successfully committed proposal: took = ...`.
- **2a:** `status` shows one row with IS LEADER = true and the same RAFT TERM on every row. After the kill, the dead endpoint shows a connection error; a new leader appears within about a second (etcd defaults: 100 ms heartbeat, 1 s election timeout), and RAFT TERM goes up by at least 1. The log line names the new leader and the new term. `put` works with 2 of 3. **Proves:** the same thing as RaftScope step 3, on a real system.
- **2b:** with one node left, `put` fails after the timeout (`context deadline exceeded`). The default `get` is linearizable (it must confirm with a quorum) and also fails. `get --consistency=s` (serializable) answers from the local node's copy: it works, but **it may be stale**, and nothing tells you. **Proves:** quorum loss blocks writes and fresh reads; local reads trade freshness for availability.
- **2c:** `lease grant 15` prints `lease <hex id> granted with TTL(15s)`; `timetolive` shows the remaining seconds counting down; after 16 s the `get` prints nothing because the key was deleted along with the lease. **Proves:** a lease takes its keys with it on expiry; nobody has to clean up.
- **2d:** Terminal 1 prints a key like `compaction/<lease id>` and holds. Terminal 2 waits. After the STOP, Terminal 1's keepalives stop, its 10 s lease expires, its key is deleted, and **Terminal 2 gets the lock about 10 s later**. `get --prefix -w json` shows Terminal 2's key with a **higher `create_revision`**: that revision is the fencing token, because the cluster-wide revision only ever goes up. When Terminal 1 wakes, write down what it prints. Whatever it is, any write it had in flight would carry the *lower* revision, and only a resource that checks the revision would stop it. **Proves:** Drill 2's whole story in 30 seconds.

---

## K-d0. Template drill: how it's graded (no reference code, by design)

You pass on your own file: zero warnings, every assert passes, under 15:00. After the timer stops, check your file for these common slips:

- **Fill order (T1):** bottom-up must loop over interval **length** on the outside (short intervals first), then the left end, then the split point. Looping `i` from 0 up and `j` from `i` up reads cells that aren't filled yet.
- **Split range (T1):** matrix chain splits at k from i to j − 1, with cost `d[i] * d[k+1] * d[j+1]`. Off-by-one in the dims index is the usual bug: test the one-matrix case.
- **Initial value (T1):** a min-DP cell starts at a large value, but the length-1 base case is 0. Starting everything at `INT_MAX` and then adding to it overflows: use `LLONG_MAX / 4` or check before adding.
- **Memo sentinel (T1):** `-1` means "not computed" only if no real answer can be −1. Costs here are ≥ 0, so it's fine. Say that aloud.
- **Shift width (T2):** `1 << n` is an `int`. At n ≥ 31 that's undefined behaviour; for big masks use `1LL << n` and `__builtin_popcountll`.
- **Precedence (T2):** `m & (1 << i) == 0` parses as `m & ((1 << i) == 0)`. Write `((m >> i) & 1) == 0`. This is why the drill asks for explicit parentheses.
- **Submask loop (T2):** `for (s = m; s; s = (s - 1) & m)` visits every **non-empty** submask; the empty one needs handling on its own if you want it. The 3ⁿ total comes from each element being in one of three states: not in m, in m but not in s, or in s.
- **Assignment worker index (T2):** the next worker is `popcount(mask)`; you don't need a second dimension for it. `dp` has `1 << n` cells, all large except `dp[0] = 0`.

---

## K-d. Hint ladders (one rung at a time, only after 25 minutes stuck)

Rungs: 1 pattern → 2 data structure → 3 key insight → 4 skeleton in words.

**322 Coin Change**
1. 1-D DP over the amount (unbounded knapsack: each coin can be reused).
2. An array `dp[0..amount]`, filled with an "impossible" value of `amount + 1` (not `INT_MAX`, which overflows on + 1).
3. `dp[a]` = 1 + min over coins `c ≤ a` of `dp[a − c]`, and `dp[0] = 0`. BFS over amounts is the same idea level by level.
4. Initialise → `dp[0] = 0` → for a from 1 to amount, for each coin ≤ a, take the min → answer `dp[amount]`, or −1 if it's still `amount + 1`. *R2 twist: count the ways instead (518). Which loop goes outside, and why?*

**139 Word Break**
1. 1-D DP over prefixes.
2. `dp[0..n]` of bools plus an `unordered_set` of words (note the longest word length).
3. `dp[i]` is true if some `j < i` has `dp[j]` true and `s[j..i)` is a word. Only check `j ≥ i − maxLen`.
4. `dp[0] = true` → for each i, try every j in range, break at the first hit → answer `dp[n]`. *R2 twist: return all sentences (140). What blows up?*

**1143 Longest Common Subsequence**
1. 2-D DP over two prefixes.
2. A `(n+1) × (m+1)` table with a zero row and column for the empty prefix.
3. Last characters equal → `dp[i−1][j−1] + 1`; otherwise → `max(dp[i−1][j], dp[i][j−1])`.
4. Fill row by row → answer bottom-right. Space: two rows of size `min(n, m) + 1`. *R2 twist: print the subsequence. What do you keep?*

**329 Longest Increasing Path in a Matrix**
1. DFS with memoisation on a DAG (or a topological sort, peeling cells with no bigger neighbour, layer by layer).
2. `memo[r][c]` = longest path starting at (r, c); 0 = not computed.
3. Strictly increasing means a path can never come back to a cell, so there are no cycles and no visited set. Each cell is computed once: O(R·C).
4. For every cell: `dfs(r, c)` = 1 + max of `dfs` over the up to 4 strictly bigger neighbours, stored in memo → answer is the max over all cells. *R2 twist: a 10⁴ × 10⁴ grid. What breaks? (Recursion depth: use the topological-sort version.)*

**309 Stock with Cooldown**
1. State-machine DP.
2. Three running values per day, no array needed: **hold** (own a share), **sold** (sold today), **rest** (no share, free to buy).
3. Draw it: hold → hold, rest → hold (buy: − price), hold → sold (+ price), sold → rest (the cooldown), rest → rest. Each day's new values must come only from yesterday's.
4. Start `hold = −prices[0]`, `sold = rest = 0` → each next day: compute the three new values from the old three (temporaries!) → answer `max(sold, rest)`. *R2 twist: a fee per transaction instead of a cooldown (714). Which arrow changes?*

**312 Burst Balloons**
1. Interval DP.
2. Pad the array with a 1 on each end; `dp[l][r]` = best coins from bursting everything strictly between l and r.
3. Choose the balloon k burst **last** in (l, r). When k goes, its neighbours are exactly l and r, so it earns `a[l]·a[k]·a[r]`, and the two sides (l, k) and (k, r) were independent before that.
4. For length 2 to n − 1, for each l (r = l + length), for each k strictly between: `dp[l][r] = max(dp[l][k] + dp[k][r] + a[l]·a[k]·a[r])` → answer `dp[0][last]`. O(n³).

**1235 Maximum Profit in Job Scheduling**
1. DP + binary search (weighted interval scheduling).
2. Jobs sorted by end time; `dp[i]` = best profit using the first i jobs; a sorted array of end times for `upper_bound`.
3. For job i: skip it (`dp[i−1]`), or take it plus the best of the jobs that end at or before its start. A job ending at time X is compatible with one starting at X, so use `upper_bound(start)`, not `lower_bound`.
4. Sort by end → `dp[0] = 0` → for i from 1 to n: `j = upper_bound(ends, start_i)` gives the count of compatible jobs → `dp[i] = max(dp[i−1], profit_i + dp[j])` → answer `dp[n]`. O(n log n). Watch the off-by-one between "count of jobs" and "index of a job".

**1472 Design Browser History**
1. Array with a cursor (or two stacks).
2. A `vector<string>`, the current index, and a logical end, so you don't need to erase.
3. `visit` overwrites the slot after the cursor and sets end = cursor + 1, which throws away the forward history in O(1). back and forward clamp.
4. visit: `++cur`, write at cur (overwrite, or push_back if at the vector's size), `end = cur + 1`. back(k): `cur = max(0, cur − k)`. forward(k): `cur = min(end − 1, cur + k)`. Return `pages[cur]`. *Follow-up aloud: "This is config history with rollback. What if every version must also be kept for audit?" (append-only log plus a separate pointer, never overwrite).*

**1039 (sealed: open only after Friday's check)**
<details><summary>Open after the check</summary>

1. Interval DP: the same loop as 312, with min instead of max.
2. `dp[i][j]` = minimum score to triangulate the polygon piece from vertex i to vertex j (with the edge i–j as one side).
3. The edge i–j must belong to exactly one triangle (i, k, j), for some k between them. That triangle splits the rest into the independent pieces (i..k) and (k..j).
4. `dp[i][i+1] = 0` → for length 2 to n − 1, for each i (j = i + length): `dp[i][j] = min over k in (i, j) of dp[i][k] + dp[k][j] + v[i]·v[k]·v[j]` → answer `dp[0][n−1]`. O(n³).

**Grading:** pass = correct in 45 minutes with no hints. Fail → re-read the 312 ladder, redo 312 and 516 before Week 8's new problems, then retry 1039 cold.
</details>

---

## K-e. Troubleshooting: interviewer sheets and scoring

Score each drill 1–4 on **Troubleshooting** (stabilizes first, ranks hypotheses, one check each) and **Communication**. A 4 stabilizes before diagnosing, names 2–3 ranked hypotheses, gives a check with its expected result for each, and ends with a prevention step and an alert.

### Drill 1: split brain

**Facts to give when asked:** both nodes show the VIP in `ip addr`; both keepalived logs say `Entering MASTER STATE` (zone B at 02:04:31, zone A never left it); zone B's Postgres was promoted (`pg_is_in_recovery()` returns false on both); the app's connection pool reconnected some instances to each node (ARP flip-flop on the VIP); new orders exist in both databases since 02:04 and the sequences overlap; there's no third node or witness.

**Reference path:**
- **Clarify:** since when, what changed (the network change at 02:04), are writes still landing on both?
- **Scope:** every app instance, or some? Which database is each connected to?
- **Stabilize first:** stop the split. Pick one primary (zone A, it holds the longer write history), take the VIP away from zone B and stop its keepalived, and **fence** zone B's Postgres (shut it down or make it read-only) so nothing writes there. Pause order intake for a few minutes if needed. Every minute both are writable creates more conflicting rows.
- **Hypotheses (ranked):** (1) a two-node failover with no quorum: both sides promoted during the partition. Check: keepalived logs on both and `pg_is_in_recovery()` on both. Both MASTER and both false confirms it. (2) A VIP/ARP problem alone, with one real primary. Check: `pg_is_in_recovery()`; if zone B is still a standby, this is a routing problem, not split brain. (3) App-side caching causing "vanishing" orders. Check: query both databases for an order ID a customer reported.
- **Fix:** reconcile: export the orders written to zone B since 02:04, re-insert them into zone A with new IDs (the overlapping sequence values mean IDs collide), tell customers whose numbers changed. Rebuild zone B as a standby from zone A (`pg_rewind` or a fresh base backup). Never let both serve again.
- **Prevent:** failover decided by a **majority** (3 voters: a witness or arbiter in a third zone, or Patroni with etcd); **fence** the old primary (STONITH, or a promotion epoch the app checks); writes go through a component that only talks to the current-epoch leader. **Alert:** "more than one node reports not-in-recovery" and "VIP seen on two hosts".
- **Key line to hear:** "A two-node cluster can't tell a dead peer from a partition. Only a majority can decide."

### Drill 2: lease expires mid-write

**Facts to give when asked:** worker-A's log has a gap from 01:13:05 to 01:13:52, with no lease renewals in between; the JVM GC log shows a 47 s stop-the-world pause at 01:13:05 (heap close to its limit); worker-B acquired at 01:13:36 (30 s lease + renewal jitter); A woke at 01:13:52, finished its file rewrites and wrote `manifest.json` at 01:14:10; B wrote its manifest at 01:13:58; A's manifest is the one in place, but it lists files that B's run deleted. The lock code renews the lease in a background thread and never checks it before writing.

**Reference path:**
- **Clarify:** which reads fail, since when, did anyone write to the table by hand?
- **Scope:** one table or many? Every night or just last night?
- **Stabilize:** pause compaction for this table (and any others with the same symptom); restore a consistent manifest. Either take B's manifest from object versioning, or rebuild one from the files that actually exist. Reads recover.
- **Hypotheses (ranked):** (1) worker-A paused past its lease; B legally got the lock; A resumed and wrote without knowing. Check: A's log gap + GC log + etcd lease events (lease revoked/expired at ~01:13:35). A gap longer than the TTL confirms it. (2) A bug in the lock code (two holders at once without a pause). Check: etcd shows the lock key's create_revision changed from A's lease to B's; if both keys existed together, the code is wrong. (3) Clock skew between workers making the logs look overlapped. Check: compare against etcd's revision order, which doesn't depend on clocks.
- **Fix:** **fencing token**: use the lock key's revision as the token; write it into the manifest; make the manifest swap a conditional write (`If-Match` on the ETag/generation you read at the start, or an etcd/database compare-and-set on the token), so a stale holder's write is rejected. Also check the lease's remaining time before each phase and abort if it's below a safety margin; fix the GC pressure (heap size or collector).
- **Prevent:** an alert on "lock acquired while the previous holder's last heartbeat is less than TTL old", on GC pauses longer than a third of the TTL, and on manifest writes rejected by the token check (that number should be 0 normally; when it's not, the fence just saved you).
- **Key line to hear:** "The lock service was right. The lease expired. The bug is that nothing at the storage checked who was writing."

### Drill 3: leader election stuck

**Facts to give when asked:** `etcdctl member list` shows the right 3 members; `endpoint health` intermittently reports a node unhealthy; etcd logs on every node: `slow fdatasync` warnings and `leader failed to send out heartbeat on time; took too long, leader is overloaded likely from slow disk`; `etcd_disk_wal_fsync_duration_seconds` p99 went from ~5 ms yesterday to ~800 ms after the move (new storage class is network-attached throughput-optimised HDD); election timeout is the default 1000 ms, heartbeat 100 ms; network RTT between nodes is < 1 ms; no node was down.

**Reference path:**
- **Clarify:** what changed (the instance type and storage move), which calls fail?
- **Scope:** all three nodes affected equally? Is the API server itself up?
- **Stabilize:** stop the flapping before tuning anything: move the etcd data back to SSD (roll back the storage change, one member at a time, keeping quorum the whole way). Pause non-critical controllers or jobs that write a lot to cut load. Take a snapshot (`etcdctl snapshot save`) before touching members.
- **Hypotheses (ranked):** (1) disk fsync slower than the heartbeat/election budget: the leader can't persist and send heartbeats in time, followers time out, the term climbs. Check: `etcd_disk_wal_fsync_duration_seconds` and `backend_commit` p99 (healthy is under ~10 ms) and the "slow fdatasync" logs. (2) Quorum or membership problem. Check: `member list` and `endpoint status`; 3 healthy members rules it out. (3) Network latency or packet loss between nodes. Check: RTT and loss between peers, `etcd_network_peer_round_trip_time_seconds`. Under 1 ms rules it out. (4) A disruptive node rejoining with a higher term. Check: is pre-vote on, and does one node's term jump ahead first?
- **Fix:** etcd on low-latency SSD storage (dedicated, not shared with logs); if anything, raise the election timeout only as a temporary bandage, and say why that's worse (slower failover). Verify: leader stable for an hour, term flat, fsync p99 back under 10 ms.
- **Prevent:** a storage-class change to etcd needs a benchmark first (`fio` with fdatasync, or `etcdctl check perf`); alerts on `etcd_server_leader_changes_seen_total` rate and fsync p99; etcd's storage pinned in the platform's infrastructure code so a cost cleanup can't change it silently.
- **Key line to hear:** "Raft is safe here, just not live. Elections need the timing rule: broadcast time much shorter than the election timeout. The disk broke that rule."

---

## K-f. Design: lock and lease service, critique rubric (an outline, not a full design)

Check your drawing against each line. A miss → redraw that part from memory the next day.

- **Requirements:** mutual exclusion **with fencing** (the honest promise is "at most one holder per token at the resource", not "at most one process thinks it holds the lock"); leases with a TTL; optional fairness (FIFO waiters); watch or notify on release; numbers stated (10k clients, 5k ops/s, p99 acquire in tens of ms inside a region).
- **API:** `Acquire(name, ttl, owner) → (token, leaseId)` (returns a token, not just OK) · `KeepAlive(leaseId) → remaining ttl` · `Release(name, token)` · `Wait/Watch(name)` · idempotent with a client request ID so retries don't double-acquire.
- **Data:** per lock: holder, leaseId, token, waiters queue; per lease: TTL, the keys attached to it. All writes go through a replicated log (5 voters across 3 zones survives a zone loss plus a node), with periodic snapshots so the log doesn't grow forever.
- **Deep dive, expiry:** only the leader counts lease time, with a **monotonic** clock. On a leader change, the new leader extends every lease by at least an election timeout (it can't know how much time passed, so it gives clients a grace period, as Chubby does). Clients treat their lease as expired earlier than the server does (a safety margin for clock rate differences).
- **Deep dive, waiters:** each waiter writes its own key and watches only the key just ahead of it (ordered by revision), so a release wakes one client, not all 10,000.
- **Tokens:** the token = the log index or revision of the grant (monotonic for free). The resource must check it; say what happens when it can't (margins, idempotent writes: unlikely, not impossible).
- **Failures:** leader crash (re-elect, grace period); client pause past TTL (fencing); partition (the minority side can't grant or renew, so its clients' leases run out); clock jump (monotonic clocks, no wall clock in expiry); quorum loss (the service stops granting; existing holders keep working until their own leases expire); thundering herd (per-waiter watch).
- **Tradeoffs:** consensus-backed (etcd, ZooKeeper, Chubby: correct under partitions, but each acquire is a quorum write) vs Redis or Redlock (fast, but relies on timing assumptions, and the fencing token problem remains); coarse locks held for minutes (Chubby's choice: low load) vs fine-grained locks per request (needs sharding); at 10× load, shard the lock namespace across several consensus groups with consistent hashing on the lock name, and say that cross-shard multi-lock acquisition then needs an ordering rule to avoid deadlock.

---

## K-g. Flashcard answers

1. Any read set overlaps any write set, so a read reaches a replica with the newest acknowledged value. Stale anyway: sloppy quorums and hinted handoff; concurrent writes resolved by last-writer-wins on skewed clocks; a write that reached fewer than W nodes isn't rolled back; restoring a failed replica from an older copy.
2. Expiry is measured on the server. The holder can pause (GC, VM pause, page fault) past expiry without noticing, then write after someone else got the lock. It needs a fencing token checked by the resource.
3. A number that increases with every lock grant (etcd revision, ZooKeeper zxid). The lock service issues it, the client sends it with every write, and the **resource** rejects anything lower than the highest it has seen, atomically with the write.
4. A candidate whose log is less up-to-date than the voter's (compare last log term, then last index). Every committed entry is on a majority, and any winning majority overlaps it, so the winner always has every committed entry.
5. When the leader has stored it on a majority **and** it's from the leader's current term (older entries are committed indirectly by a later current-term entry). Then it's applied and the client is answered.
6. A majority of 4 is 3, so 4 nodes tolerate 1 failure, the same as 3, with more cost, more voters to wait on, and a 2–2 split leaves no majority. 5 tolerates 2.
7. Only the keys in the arcs the new node takes over move, about K/N. Virtual nodes even out arc sizes, allow weighting, and spread a failed node's load over many nodes.
8. `etcdctl --endpoints=$EP endpoint status -w table` → IS LEADER and RAFT TERM columns.
9. `etcdctl lease grant 15` → `etcdctl put <key> <value> --lease=<id>` → `etcdctl lease timetolive <id>`.
10. Your own Monday file, once it passes the §d0 asserts. Grade against K-d0.

---

## K-h. Reference cheat-sheet points (compare after writing yours; target ≥ 80% matching)

**Top, five things:** the five statements in K-b, one line each: W + R > N overlap; one leader per term, vote only for an up-to-date log; commit = majority + current term; leases need fencing tokens checked at the resource; consistent hashing moves K/N keys, virtual nodes even the load.

**Commands:**
- Leader and term: `etcdctl endpoint status -w table --endpoints=...`
- Health: `etcdctl endpoint health --endpoints=...`
- Members: `etcdctl member list -w table`
- Lease: `etcdctl lease grant <ttl>`, `put --lease=<id>`, `lease timetolive <id>`, `lease keep-alive <id>`
- Lock: `etcdctl lock --ttl=<s> <name>`; fencing token = the lock key's `create_revision` (`get --prefix <name>/ -w json`)
- Stale-OK read: `etcdctl get <k> --consistency=s`
- Disk check: `etcd_disk_wal_fsync_duration_seconds` p99 under ~10 ms; `etcdctl check perf`
- Backup: `etcdctl snapshot save <file>`

**Failure modes:** the eight rows in K-b, each with cause and first check.

**Interview questions and stories:** "How would you build a distributed lock?" (the lock service design + fencing); "What happens when the leader dies?" (RaftScope and etcd lab results with real numbers: ~1 s failover with etcd defaults); "Tell me about a disagreement" (your §k story, once filled in). Any story where you ran a primary failover on your MongoDB fleet fits the replication questions, but only with facts you supply.

---

## K-k. Story reference beats (coverage check only, not content)

A strong answer: states the decision and why it mattered in one breath; gives the other side's best argument fairly (interviewers listen for this); shows how you settled it with evidence (data, a prototype, a written comparison, a time-boxed trial) rather than seniority or persistence; names what the chosen path cost; gives one number; ends with what you'd do the same or differently. It stays technical, never blames, and is under 2 minutes. If it ended in "disagree and commit", say so plainly; that's a good answer. Only your facts fill these.
