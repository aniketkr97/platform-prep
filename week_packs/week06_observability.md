# WEEK PACK — Week 6: Observability and reliability

Infra layer: SLIs, SLOs, error budgets, symptom-based alerting, retries with backoff and jitter, backpressure · Code: shortest paths with a twist (Dijkstra, 0-1 BFS, state-augmented Dijkstra, Bellman-Ford rounds) · Design: metrics and alerting pipeline · Story: an incident you owned, told as a postmortem · Ends with: **Gate 2**

**Rule for this file:** do every section cold first. Every answer, note, hint and reference is in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section. There is no LeetCode code anywhere in this file, and no template code either: problems go through the hint ladder one rung at a time, and the template drill is graded on your own file. The Gate 2 checklist is **§z**, the last section before the answer key, so you never scroll through answers to reach it.

Lab starter files (working service and configs; the SLO rules are blanks you fill): `week_packs/week06_lab/`.

---

## 0. Reviews first, then this week's plan

### 0a. Review pull: everything due from Weeks 1–5 (as of today, Fri Nov 6)

**Nothing has been logged since Oct 25.** The tracker's review queue, the error log's rep columns and every pack's mark column are blank. So every item below is either overdue or unknown. Reviews come before new material, and **more than 5 due means no new problems that day.**

| Week | Item | Stage | Was due | Counts toward the cap? |
| --- | --- | --- | --- | --- |
| 1 | **3\*** (23 submits), **1\*** (11), **11\*** (7), **49\*** (5) | Review 1 (seeded old solves) | Oct 19 | Yes: 4 |
| 1 | 992, 974, 1248, 933 | Review 1 | Oct 20–21 | Yes: 4 |
| 2 | **146\*** (14), **20\*** (15), **71\*** (last seen Mar 2026), 739 | First redo (seeded old solves) | Oct 22–25 | Yes: 4 |
| 3 | **236\*** (7), **124\*** (9), 98 (Jan 2025, fading), 102, 1114 | First redo (seeded old solves) | Nov 3–5 | Yes: 5 |
| 3 | 337 (R2 today), 968, 834, 609 (R1 by now) | Only if you did the first tries Nov 2–4 | Nov 3–6 | Yes, if done |
| 2 | 84, **33 (never solved)**, 1438, 410, 2398 (check) | First tries (new work, not reviews) | Oct 20–24 | No, but still unstarted |
| 3 | 2581 (check) | First try | Today | No: blocked by the cap |
| 4 | — | Week 4 starts Mon Nov 9 | — | — |
| 5 | — | No Week 5 pack yet | — | — |
| Concepts | Error-log F1–F8, Rep 3 | Spoken drill | Nov 1 | No (concept reviews never count) |

\* shaky by your LeetCode history (5+ submits or last seen before May 2026): these go first.

**Count: at least 17 problem reviews due today** (W1: 8, W2: 4, W3: 5) if none were done. That's over the cap, so **no new problems until it's 5 or fewer**, and that includes today's 2581 check.

**Burn-down at 6 a day, shaky and oldest first** (≈ 2 h a day):

| Day | Reviews |
| --- | --- |
| A | 3\*, 1\*, 146\*, 20\*, 11\*, 49\* |
| B | 992, 974, 1248, 933, 71\*, 739 |
| C | 236\*, 124\*, 98, 102, 1114 (+ any W3 R1/R2 you've earned) |

**What I need from you:** one line per item you've already done: `number · date · Clean / Shaky / Failed`. I'll update `tracker.md`, write the dates into the queue and recount. Until then, assume everything above is due.

### 0b. Dates

The plan puts Week 6 on Nov 16–22. The packs have slipped one week at a time (Week 3: Nov 2–8, Week 4: Nov 9–15), so Week 5 is Nov 16–22 and this pack runs **Mon Nov 23 – Sun Nov 29**.

- **Thanksgiving is Thu Nov 26.** That day is a morning only: reviews, the cheat sheet, the story and one drill. No new problems.
- **Gate 2 is Sat Nov 28 – Sun Nov 29** (the date the Week 4 pack suggested). Gate 2 tests Weeks 4–6, so it closes this week.
- **Week 5 has no pack yet.** The review counts below assume it copies Week 4's layout: Learn row Monday, 2 rows Tuesday, 2 Wednesday, core redos Thursday, check Friday, mock Saturday. I'll recount when Week 5 exists.
- **The two-week slip moves the plan's end from Dec 20 to about Jan 3.** Gate 3 and the final gate move with it unless a later week gets cut. Your call, but decide before Week 7.

**Tools:** Prometheus, Alertmanager, Docker and kind aren't installed on this Mac. Python 3, `jq`, `curl` and `brew` are. Lab Step 0 (§c) installs Prometheus and Alertmanager with Homebrew, with no Docker needed. Do it Monday night.

### 0c. This week's problems

Your history is from your LeetCode account (read Oct 6). The coding page counts 5+ submits as shaky, so **all four core problems are shaky**.

| # | Problem | Diff | Role | Your history | How it's run |
| --- | --- | --- | --- | --- | --- |
| 743 ⚑ | Network Delay Time | M | Core | Sep 2026, **11 submits: shaky, flagged** | Cold redo, ≤ 25 min, **first thing Monday**, before the template drill |
| 778 | Swim in Rising Water | H | Core | Sep 2026, **9 submits (shaky)** | Cold redo, ≤ 25 min |
| 787 | Cheapest Flights Within K Stops | M | Core | Sep 2026, **8 submits (shaky)** | Cold redo, ≤ 25 min |
| 1631 | Path With Minimum Effort | M | Core | Sep 2026, **5 submits (shaky)** | Cold redo, ≤ 25 min |
| 1368 | Min Cost to Make at Least One Valid Path in a Grid | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 1928 | Minimum Cost to Reach Destination in Time | H | Required · **Learn** | New | Learn row: 40 min alone, 50 total |
| 2203 | Minimum Weighted Subgraph With the Required Paths | H | Required · Apply | New | First try, 50 min |
| 2353 | Design a Food Rating System | M | Required · practical | New | First try, 35 min + follow-up aloud |
| 2577 | (Friday check: don't open it before Friday) | H | Check | New (verified untouched) | 45 min, alone, no hints, Friday |

⚑ **743 flag:** 11 submits on a plain Dijkstra means trial and error. It runs first on Monday, cold, before you type the template. If it isn't Clean, it goes in `error_log.md` that day with what broke, and it comes back in 2 days.

⚠ **The coding page's two Week 6 templates are worked solutions to 1368 (0-1 BFS) and 1976 (Dijkstra with path counting).** Don't open them before your first tries on those two, or the tries count as "Needed the solution". Monday's drill (§d0) is graded on your own file instead.

⚠ **The core redos are seeded reviews** (old solves the coding page put on the schedule). They count toward the cap, but they're allowed on a capped day, because reviews always run.

### 0d. Day by day

Counts are **projected**, assuming every redo is Clean and Week 5 copies Week 4's layout. The cap is "more than 5". Exactly 5 still allows new problems.

| Day | Reviews first | Infra / apply | Code | Other |
| --- | --- | --- | --- | --- |
| **Mon Nov 23** | W4 R3: 215, 56, 253 · W5 R2: Thu core redos (3–4) · seeded **743⚑** = **7–8, over the cap** | §a warm-up cold (10) → §b questions cold → read → K-b (45) | 743 is a review, so it runs, first. Then §d0 template drill (15). **No new problems.** | Lab Step 0 tonight (15) |
| **Tue Nov 24** | W4 R3: 1882 · W5 R2: 2360 · 743 (R1) · seeded **778** = 4 | §c labs 1–4 (≈ 70) | **1368** (Learn) → **2353** (practical) | Recall warm-up (10) |
| **Wed Nov 25** | W4 mock (R3) · W5 mock (R2) · 778, 1368, 2353 (R1) = **5, at the cap** | §b2 teach-backs, recorded, no notes (25) · §e Drill 1 (30) | **1928** (Learn) → **2203** | — |
| **Thu Nov 26** 🦃 morning only | 1928, 2203 (R1) · seeded **787**, **1631** = 4 | §h cheat sheet from memory (30) · §k story (20) · §e Drill 3 (30) | No new problems (holiday) | — |
| **Fri Nov 27** | W5 R3: Monday's Learn row · W3 R4: 337 · 743 (R2) · 787, 1631 (R1) = **5, at the cap** | §f design: your drawing first (40) · §e Drill 2 (30) | **2577** check, 45 min, alone | — |
| **Sat Nov 28** **GATE 2, day 1** | W5 R3 ×2 · W3 R4: 968, 236 · 778, 1368, 2353 (R2) · 2577 (R1) = **8** | §z gate items 1, 2, 4, 5a (≈ 3 h, details in §j and §z) | Gate problems only | Debrief (30) |
| **Sun Nov 29** **GATE 2, day 2** | W5 R3 ×2 · W3 R4: 834, 609 · 1928, 2203 (R2) · gate problems (R1) = **8** | §z gate items 3, 5b, 5c, 6 (≈ 2.5 h) · score the gate (15) | None (cap) | Plan Week 7 (15) |

**On gate days, the gate runs first** (fresh, under test conditions). The gate problems are tests, not practice, so the cap doesn't block them. All 8 reviews still happen that day, after the gate.

**The weekend is heavy:** about 5–6 h a day (gate + 8 reviews), on Thanksgiving weekend. If that's too much, say so and I'll move Gate 2 to Sat Dec 5 – Sun Dec 6. Then this Saturday is a normal Week 6 mock plus the design redraw. **Mon Nov 30 projects to 9–10 reviews** (787, 1631 R2; W5 R3 ×3–4; W3 R4: 124, 102, 98, 1114), so Week 7 opens capped as well.

Extras (§d2) don't fit this week: every day with spare time is at or over the cap. They roll into Week 7.

### 0e. Session rules (same as Weeks 2–4)

- Say **"start 1368"** (or any number) and I log the start time. 60-second approach aloud, brute force first, complexity before code.
- Hints: one rung per request (pattern → data structure → key insight → skeleton), only after 25 min stuck. A Learn row gets the full 40 minutes first. No hints in the Friday check or the gate. If you ask for a solution, you get the next rung instead.
- I compile your file with `clang++ -std=c++17 -Wall -Wextra` and show compile errors. I never fix or rewrite your code.
- Marks: first tries **Solved alone / Needed the solution**. Redos **Clean** (first submit, < 25 min, no hint) / **Shaky** (slow, 2+ submits, or one hint) / **Failed**.

---

## (a) Day 1 recall warm-up (cold, aloud, before any reading)

10 questions: 7 on Week 6 (answer from what you already know) and 3 from earlier weeks. One or two sentences each. Mark each ✓ / ✗ before opening K-a.

1. Define SLI, SLO and error budget, one line each.
2. An SLO is 99.9% over 30 days. How many minutes of total outage is the whole budget?
3. Why is "CPU > 90% for 5 minutes" a bad thing to page on?
4. A client retries immediately on failure, up to 5 times. What happens when the server is overloaded? Name the two changes that fix it.
5. p50 vs p99: what's the difference, and why does an average hide a latency problem?
6. What does a bounded queue force you to do that an unbounded queue doesn't?
7. Why does Dijkstra break with negative edge weights? And which single line handles stale heap entries?
8. *(Week 4)* A container goes over its CPU limit; another goes over its memory limit. What happens to each?
9. *(Week 2, F1)* After a library upgrade turns off keep-alive, a client host fills with TIME_WAIT sockets. What runs out, and what error shows up?
10. *(Week 1)* Load average 40 on an 8-core box, but CPU is 10% busy. What's the likely cause, and what do you run?

---

## (b) Reading: questions first, then the brief

**Read:** Google SRE book: *Service Level Objectives*, *Monitoring Distributed Systems*, *Handling Overload*, *Addressing Cascading Failures*. SRE Workbook: *Alerting on SLOs*. All free at sre.google. Search by title, since chapter numbers vary between editions.

**Before reading, answer from memory** (aloud or on paper, 1–2 sentences each):

*SLOs and error budgets*
- B1. SLI vs SLO vs SLA. Which one has money attached, and which is stricter?
- B2. Why is 100% the wrong target? Give two reasons.
- B3. Budget in minutes per 30 days for 99.9% and for 99.99%.
- B4. The budget runs out on day 12. What does an error-budget policy say happens next, and who agreed to it?

*Monitoring and alerting*
- B5. The four golden signals. Then RED and USE: what each is for.
- B6. Symptom vs cause alerts. Which page, and which go to tickets or dashboards?
- B7. What is a **burn rate**? What does burn rate 1 mean?
- B8. Why does a good SLO alert check **two** windows (e.g. 1 h and 5 min)? What breaks with only the long one? With only the short one?

*Overload and cascading failures*
- B9. Exponential backoff, jitter, retry budget: one line each. Why does backoff alone still cause waves?
- B10. Backpressure vs load shedding vs circuit breaker.
- B11. What is deadline propagation, and what goes wrong without it?
- B12. The trigger is gone, but the outage continues. What keeps it going?

Then read **only for what you missed**, and compare with the brief in **K-b**.

### (b2) Explain-aloud: four 2-minute teach-backs (Wednesday, recorded, no notes)

Record each one cold. Listen once. Stumbled more than five times? Redo it. Outlines and follow-up answers are in **K-b2**. Read them only after your first recording.

**T1. SLI, SLO and the error budget.** "How would you set an SLO for a service you own, and what is the error budget for?"
Most likely follow-ups:
1. Why not 100%?
2. Request-based SLI vs time-based ("good minutes") SLI: when do you use each?
3. The budget is gone mid-month. What happens, and who decides?
4. How do you pick 99.9 vs 99.99?
5. What's the SLO for a batch platform like your Airflow platform, where there are no "requests"?

**T2. Symptom-based alerting and burn rates.** "How do you decide what pages a human at 3 a.m.?"
Most likely follow-ups:
1. Why two windows?
2. Where does 14.4 come from?
3. A service gets 10 requests a minute. What breaks in your alert, and what do you do?
4. Who watches the watcher? How do you know alerting itself is alive?
5. You get 300 pages in 5 minutes. What Alertmanager features stop that from happening again?

**T3. Retries with backoff and jitter.** "A dependency is flaky. How should its clients retry?"
Most likely follow-ups:
1. Which requests are safe to retry? How do you make a POST safe?
2. Write the full-jitter formula.
3. Three layers each retry 3 times. What does one user request cost the bottom layer?
4. Retry budget vs circuit breaker: which problem does each solve?
5. How does the server tell clients to back off?

**T4. Backpressure and cascading failure.** "How does one slow dependency take down a fleet, and how do you stop it?"
Most likely follow-ups:
1. A bounded queue is full: block or drop? When is each right?
2. What is deadline propagation, and where do you set the first deadline?
3. Under overload, which requests do you shed first?
4. Why doesn't the system recover when the trigger goes away (metastable failure)?
5. Kafka consumer lag is growing. Is that backpressure working or failing?

---

## (c) Lab sheet: Prometheus with an SLO alert on a toy service; trigger it, then silence it

Run everything from `week_packs/week06_lab/`. **Before each step, say your prediction aloud**, then run it and note what you saw. Expected observations are in **K-c**.

| File | What it is |
| --- | --- |
| `app.py` | Toy service on :8000. `/work` returns 200 or 500; `/fault?error_rate=0.2&latency_ms=300` injects faults; `/fault?clear=1` heals; `/metrics` for Prometheus. Python stdlib only. |
| `receiver.py` | Fake pager on :5001. Prints one line per notification Alertmanager sends. |
| `loadgen.sh` | About 20 requests/s until Ctrl-C. |
| `prometheus.yml` | Scrapes the toy every 5 s; evaluates rules every 5 s; sends alerts to :9093. |
| `alertmanager.yml` | Groups by `slo`; short timers; an inhibit rule (a page holds back the ticket for the same SLO). |
| `slo_rules.yml` | **Your blanks.** Four SLI recording rules + a fast-burn page + a slow-burn ticket. |
| `slo_rules_test.yml` | Grader. Checks how your rules behave, not their exact PromQL. |

The toy service and fake pager were tested here. **Prometheus and Alertmanager weren't run in this session (they couldn't be installed), so the rule files haven't been through `promtool` yet.** If `promtool` rejects the test file itself (not your rules), show me the error and I'll fix the file.

### Step 0: install and verify (Monday night, ~15 min)

```bash
brew install prometheus alertmanager
prometheus --version && promtool --version
alertmanager --version && amtool --version
```
Each prints a version line. If `amtool` is missing, it ships in the Alertmanager release tarball from GitHub.

### Lab 1: write the SLO rules from memory, then prove them offline (Tuesday, 15 min)

SLO: **99.9% of `/work` requests are non-5xx, over 30 days.** Fill every `TODO` in `slo_rules.yml` with no notes: four error-ratio recording rules (5m, 30m, 1h, 6h) and two burn-rate alerts (fast = page, slow = ticket).

```bash
promtool check rules slo_rules.yml
promtool test rules slo_rules_test.yml
promtool check config prometheus.yml
amtool check-config alertmanager.yml
```
Prediction first: what does each command prove, and what does a failure in each look like?

### Lab 2: start the stack and read the SLI (Tuesday, 15 min)

Five terminals, all in `week06_lab/`:

```bash
python3 app.py                                                                   # T1
python3 receiver.py                                                              # T2
alertmanager --config.file=alertmanager.yml --storage.path=./am-data             # T3
prometheus --config.file=prometheus.yml --storage.tsdb.path=./prom-data          # T4
./loadgen.sh                                                                     # T5
```

Then, in a sixth terminal:

```bash
curl -s localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .labels.job, health}'
curl -s localhost:9090/api/v1/query --data-urlencode 'query=sum(rate(http_requests_total[1m]))' | jq -r '.data.result[0].value[1]'
curl -s localhost:9090/api/v1/query --data-urlencode 'query=slo:sli_error:ratio_rate5m' | jq -r '.data.result[0].value[1]'
curl -s localhost:9090/api/v1/query --data-urlencode 'query=histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[1m])))' | jq -r '.data.result[0].value[1]'
```
Predict all four outputs before you run them. **Let it run clean for 10 minutes before Lab 3.** The timing in K-c assumes that.

### Lab 3: trigger the page (Tuesday, 15 min)

```bash
curl 'localhost:8000/fault?error_rate=0.2'
while true; do date +%T; curl -s localhost:9090/api/v1/alerts | jq -r '.data.alerts[] | "  \(.labels.alertname) \(.state)"'; sleep 5; done
```
Predict before you run it: which alert goes `pending` first, and why? Roughly when does each go `firing`? What does the fake pager (T2) print, and in what order?

Once both are firing, ask Alertmanager what it's holding back:

```bash
curl -s localhost:9093/api/v2/alerts | jq -r '.[] | "\(.labels.alertname)  \(.status.state)  inhibitedBy=\(.status.inhibitedBy)"'
```

### Lab 4: silence it, un-silence it, heal it (Tuesday, 15 min)

```bash
AM=--alertmanager.url=http://localhost:9093
amtool $AM silence add alertname=ToyAvailabilityFastBurn --duration=15m --author="$USER" --comment="lab: known fault injection"
amtool $AM silence query
```
Watch T2 for 3 minutes (longer than `repeat_interval`). Prediction: does the page stop? Does the ticket come back now that the page is silenced?

```bash
amtool $AM silence expire $(amtool $AM silence query -q)
curl 'localhost:8000/fault?clear=1'
```
Keep the alert loop from Lab 3 running. Predict: how long after the fix does the page resolve? The ticket? Why are they different?

### Lab 5 (optional, 10 min): a latency SLI

```bash
curl 'localhost:8000/fault?latency_ms=300'
```
Rerun the p99 query from Lab 2 every 30 s. Predict the value it settles at, and explain why it isn't 0.33.

**Clean up:** Ctrl-C every terminal, then `rm -rf prom-data am-data`.

---

## (d) Coding

### (d0) Monday template drill (blank file, 15 min, compiled)

**743⚑ runs first, cold.** Then the drill.

**Templates (names only; no reference code anywhere in this pack):**
- **W6-T1: Dijkstra with a binary heap** (adjacency list, `long long` distances, lazy deletion).
- **W6-T2: 0-1 BFS with a deque.**

**Format:**
1. Timer starts on a blank `w6_templates.cpp`. No notes, no autocomplete, no lookups.
2. Write both templates and a `main()` with `assert`s that prove the behaviours below. You write the asserts too.
3. Say "compile" and I run `clang++ -std=c++17 -Wall -Wextra w6_templates.cpp && ./a.out`.

**Behaviours your asserts must prove:**

| T1 Dijkstra | T2 0-1 BFS |
| --- | --- |
| A 3-edge path that's cheaper than a direct edge wins | Same distances as your T1 on a fixed graph with 0 and 1 weights |
| An unreachable node stays at "infinity" and nothing overflows | Same distances as T1 on 100 random 0/1-weight graphs (fixed seed) |
| A node pushed 3 times is **settled** exactly once | A node reached first by a 1-edge, then by a cheaper 0-edge path, ends with the cheaper distance |
| Weights up to 1e9 on a 1e5-node chain: distance correct, no overflow | Grid form: 4 directions, bounds checked, one direction free per cell |
| A parent array rebuilds the exact shortest path to a target | Unreachable cell reported as −1 (or your sentinel) |
| Stopping when the target pops gives the same answer as the full run | |

**Pass** = under 15:00, zero warnings, every assert passes, no lookups. **Fail** = any of those missed. A failed template goes on the review schedule like a problem (row in §i). Grading notes are in K-d0. Don't open them before 743 is done.

### (d1) Pattern map: the 9 problems

Patterns are hidden on purpose: naming the pattern is rung 1 of the ladder. The ladders are in **K-d**, one rung at a time, after 25 minutes stuck.

| # | Problem | Why it's in Week 6 | One question to answer before coding | Mark |
| --- | --- | --- | --- | --- |
| 743⚑ | Network Delay Time | The base problem: how long until a config push reaches every node | When is a node's distance final, and what do you return if one node never hears? | |
| 787 | Cheapest Flights Within K Stops | A route with a hop limit, like a TTL | Why can the cheapest way into a city be the wrong one to extend? | |
| 1631 | Path With Minimum Effort | The cost of a path is its worst step, not the sum | Does your relaxation still only ever make a path's cost go up? Why does that matter? | |
| 778 | Swim in Rising Water | Bottleneck path, the same idea as the worst hop on a network route | What's the cost of standing on the start cell? | |
| 1368 | Min Cost Valid Path in a Grid | Weights that are only 0 or 1 | If every edge costs 0 or 1, what does the heap ever hold? | |
| 1928 | Min Cost to Reach Destination in Time | Two costs at once (fees and time): a budgeted route | When can you safely throw away a second, more expensive visit to the same city? | |
| 2203 | Min Weighted Subgraph With Required Paths | Two sources merging into one sink, like two data centres replicating to one | What shape does the optimal subgraph have, and where do the two paths meet? | |
| 2353 | Design a Food Rating System | Practical: two indexes kept in sync, like a leaderboard or placement service | When a rating changes, which entry do you remove, and before or after updating what? | |
| 2577 | Friday check | **Sealed until Friday** | **Sealed** | |

### (d2) After-required rows (roll into Week 7; no room this week)

In order: 2290 (do it in 15 min after 1368), 1976\*, 2812, 2045, 1584, 1489 (last result WA: counts as new), 882. \* 1976 is the coding page's second template, so do it before opening that template.

---

## (e) Troubleshooting drills (symptoms only)

Answer in your routine, out loud, as if to an interviewer: **Clarify → Scope → Stabilise → Hypothesise → Check → Fix-and-prevent** ("Can Some Students Handle Cold Fixes"). Ask me questions as you go and I answer from the interviewer sheet in K-e (which you don't read). I score each step afterwards.

**From your Week 2 drills and the error log:** you skipped Check and Fix in 5 of 8 drills. For each hypothesis, name the command or metric **and** the result that confirms or kills it. Every change you propose needs a **why** and a **risk**.

### Drill 1: latency doubled after a release (Wednesday, 30 min)

> You're on call for `checkout-api` (Kubernetes, 30 pods, about 3,000 req/s). Release v2.31 finished rolling out at 14:10. At 14:35 the latency SLO alert fires: **p99 went from 180 ms to 390 ms**; p50 went from 40 ms to 46 ms. Error rate is flat. Traffic is normal for a Tuesday. The canary ran at 5% for 15 minutes and passed. Go.

### Drill 2: alert storm (Friday, 30 min)

> 02:13 on a Saturday. Your phone gets **312 pages in 7 minutes** from 41 services: `HighCPU`, `PodNotReady`, `HTTP5xxRate`, `KafkaConsumerLag`, `DiskLatencyHigh`, `ProbeFailed`, `TargetDown`. Several pages arrive twice. The pager app has frozen. The #alerts Slack channel scrolls faster than you can read. You're the only one on call. Go.

### Drill 3: triage a suddenly slow service (Thursday, 30 min, open-ended)

> "Search is slow since about 10:00." No deploys today. `search-api` runs on 12 VMs behind an L7 load balancer, with a 6-shard Redis cache and a Postgres primary plus 2 read replicas. Dashboards: **p99 went from 120 ms to 1.8 s**, p50 from 30 ms to 60 ms, and errors from 0.3% to 2% (all timeouts). Users say they're searching as usual. Go.

---

## (f) Design: "Metrics and alerting pipeline"

**Your drawing first** (Friday, 40 min, paper, timer on). Then compare with K-f. Redraw from blank the following Saturday.

> Design the metrics and alerting pipeline for an infrastructure org: **15,000 VMs and 40 Kubernetes clusters across 3 clouds, about 200 teams.** About **20 million active time series**, scraped every 15 s. Teams write their own alert rules. A page must reach on-call **within 2 minutes** of a user-facing problem starting. Keep **13 months** of data for capacity planning. **Alerting must keep working when one region, or the central store, is down.**

Walk it with **"Real Apps Deserve Deep Failure Tests"**:

| Step | Your notes (write before you draw) |
| --- | --- |
| **Requirements**: functional, non-functional, and the numbers you derive (samples/s, bytes/day, memory) | |
| **API**: how data gets in (pull or push), how rules and queries get out, how teams register alerts | |
| **Data**: series model, labels, retention tiers, what's stored where | |
| **Deep dive**: pick ONE: high cardinality, where rules are evaluated, or Alertmanager HA | |
| **Failures**: at least 5, each with its detection and mitigation | |
| **Tradeoffs**: at least 3, each with what you'd change at 10× | |

Say the number for samples per second and bytes per day **out loud** before you draw any box.

---

## (g) Flashcards (10 new cards: put them in Anki; answers in K-g)

| # | Type | Front |
| --- | --- | --- |
| 1 | Explain | SLI vs SLO vs SLA vs error budget, one sentence each. |
| 2 | Explain | 99.9% over 30 days: how many minutes of budget? What does a 14.4× burn rate mean? |
| 3 | Explain | Why does a burn-rate alert check a long window **and** a short one? |
| 4 | Explain | Symptom vs cause alerts: which page, and where do the others go? |
| 5 | Explain | Why exponential backoff, and why add jitter on top of it? |
| 6 | Explain | Three layers each try 3 times. What reaches the bottom, and what are the fixes? |
| 7 | Explain | Backpressure vs load shedding vs circuit breaker. |
| 8 | Command | PromQL: 5-minute error ratio, and p99 latency from a histogram. |
| 9 | Command | amtool: silence an alert for 1 h, list silences, expire one. |
| 10 | Template | Write W6-T1 (Dijkstra) and W6-T2 (0-1 BFS) from memory. |

---

## (h) Cheat sheet skeleton (Thursday: fill it from memory; Sunday: rewrite it from blank at the gate)

File: `cheat_sheets/week06_observability.md`. Fill it with this pack closed. Then compare with **K-h** and count matches (target ≥ 80%).

---

## (i) Review-due table (template)

Dates assume every redo is **Clean** and that each first try happens on its planned day. **Shaky** → same stage again in 2 days. **Failed** → back to Review 1 tomorrow. Rewrite the row's dates when that happens. Reviews 5 and 6 fall after the plan ends. Keep them anyway.

### Problems

| # | First try | Mark | R1 (+1) | Mark | R2 (+3) | Mark | R3 (+7) | Mark | R4 (+14) | Mark | R5 (+30) | R6 (+60) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 743⚑ | Mon Nov 23 | | Tue Nov 24 | | Fri Nov 27 | | Fri Dec 4 | | Fri Dec 18 | | Sun Jan 17 | Thu Mar 18 |
| 778 | Tue Nov 24 | | Wed Nov 25 | | Sat Nov 28 | | Sat Dec 5 | | Sat Dec 19 | | Mon Jan 18 | Fri Mar 19 |
| 1368 | Tue Nov 24 | | Wed Nov 25 | | Sat Nov 28 | | Sat Dec 5 | | Sat Dec 19 | | Mon Jan 18 | Fri Mar 19 |
| 2353 | Tue Nov 24 | | Wed Nov 25 | | Sat Nov 28 | | Sat Dec 5 | | Sat Dec 19 | | Mon Jan 18 | Fri Mar 19 |
| 1928 | Wed Nov 25 | | Thu Nov 26 | | Sun Nov 29 | | Sun Dec 6 | | Sun Dec 20 | | Tue Jan 19 | Sat Mar 20 |
| 2203 | Wed Nov 25 | | Thu Nov 26 | | Sun Nov 29 | | Sun Dec 6 | | Sun Dec 20 | | Tue Jan 19 | Sat Mar 20 |
| 787 | Thu Nov 26 | | Fri Nov 27 | | Mon Nov 30 | | Mon Dec 7 | | Mon Dec 21 | | Wed Jan 20 | Sun Mar 21 |
| 1631 | Thu Nov 26 | | Fri Nov 27 | | Mon Nov 30 | | Mon Dec 7 | | Mon Dec 21 | | Wed Jan 20 | Sun Mar 21 |
| 2577 | Fri Nov 27 | | Sat Nov 28 | | Tue Dec 1 | | Tue Dec 8 | | Tue Dec 22 | | Thu Jan 21 | Mon Mar 22 |
| Gate G1 | Sat Nov 28 | | Sun Nov 29 | | Wed Dec 2 | | Wed Dec 9 | | Wed Dec 23 | | Fri Jan 22 | Tue Mar 23 |
| Gate G2 | Sat Nov 28 | | Sun Nov 29 | | Wed Dec 2 | | Wed Dec 9 | | Wed Dec 23 | | Fri Jan 22 | Tue Mar 23 |
| W6-T1/T2 (only if failed) | Mon Nov 23 | | Tue Nov 24 | | Fri Nov 27 | | Fri Dec 4 | | | | | |

For the core redos (743, 778, 787, 1631), the "First try" column is the first redo. Mark it Clean / Shaky / Failed.

### Concepts (cards, lab, teach-backs, drills, design, story)

Same 1-3-7-14-30-60 spacing, counted from the first attempt. A card is Clean if answered word-perfect in under 30 s, a teach-back if ≤ 5 stumbles, a drill if it scores ≥ 3 on the routine, the design if it hits every K-f checklist line from memory.

| Item | First | Mark | +1 | Mark | +3 | Mark | +7 | Mark | +14 | Mark | +30 | +60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cards 1–10 | Sun Nov 29 | | Mon Nov 30 | | Thu Dec 3 | | Thu Dec 10 | | Thu Dec 24 | | Sat Jan 23 | Wed Mar 24 |
| Labs 1–4 (redo the predictions from memory) | Tue Nov 24 | | Wed Nov 25 | | Sat Nov 28 | | Sat Dec 5 | | Sat Dec 19 | | Mon Jan 18 | Fri Mar 19 |
| T1–T4 teach-backs | Wed Nov 25 | | Thu Nov 26 | | Sun Nov 29 | | Sun Dec 6 | | Sun Dec 20 | | Tue Jan 19 | Sat Mar 20 |
| Drill 1 latency after release | Wed Nov 25 | | Thu Nov 26 | | Sun Nov 29 | | Sun Dec 6 | | Sun Dec 20 | | Tue Jan 19 | Sat Mar 20 |
| Drill 3 suddenly slow service | Thu Nov 26 | | Fri Nov 27 | | Mon Nov 30 | | Mon Dec 7 | | Mon Dec 21 | | Wed Jan 20 | Sun Mar 21 |
| Drill 2 alert storm | Fri Nov 27 | | Sat Nov 28 | | Tue Dec 1 | | Tue Dec 8 | | Tue Dec 22 | | Thu Jan 21 | Mon Mar 22 |
| Design: metrics pipeline | Fri Nov 27 | | Sat Dec 5 (redraw) | | Tue Dec 8 | | Tue Dec 15 | | Tue Dec 29 | | Thu Jan 28 | Mon Mar 29 |
| Story: incident postmortem | Thu Nov 26 | | Fri Nov 27 | | Mon Nov 30 | | Mon Dec 7 | | Mon Dec 21 | | Wed Jan 20 | Sun Mar 21 |

The design's +1 redraw moves to the following Saturday (Dec 5), because Sat Nov 28 is gate day. The later dates count from that redraw. Concept reviews take 2–5 minutes each, don't count toward the 5-problem cap, and go in the recall warm-up slot.

---

## (j) Saturday: Gate 2 day 1 (the Week 6 mock is folded in)

The first 75 minutes of the gate **are** the Week 6 mock, in the plan's mock format, recorded and scored. That score goes into the gate's mock average. I run it from the sealed sheet in K-j. You don't read K-j or K-gate.

| Time | Block | Content | Gate item |
| --- | --- | --- | --- |
| 0–5 | Intro | Your 90-second intro (Week 1 story) | — |
| 5–45 | Coding | One unseen shortest-path variant. 60-second approach, brute force first, your own tests | **§z item 2** (40 min) |
| 45–70 | Troubleshooting | One unseen Kubernetes scenario, full six steps | **§z item 5a** |
| 70–75 | Your questions | Two questions you'd ask a real interviewer | — |
| break | | 10 minutes | |
| +45 | Design | CI/CD with canary and automatic rollback, drawn from blank | **§z item 4** |
| +35 | Coding | One unseen graph or heap medium | **§z item 1** |
| +30 | Debrief | Scorecard evidence, error-log rows | — |

### Scorecard (1–4 per area, with evidence), for the 75-minute mock block

| Area | Score | Evidence (timestamp + what happened) |
| --- | --- | --- |
| Approach | | |
| Working code | | |
| Fluency | | |
| Testing | | |
| Communication | | |
| Design depth | | (scored on the canary design block) |
| Troubleshooting | | |
| Composure | | |
| **Average** | | Gate 2 needs the W4–W6 mock average ≥ 3.0 |

### Debrief template (within an hour)

1. Where did I stall first, at what minute, and for how long?
2. What did I know but fail to say?
3. What did I not know at all?
4. Which routine step did I skip (coding, design or troubleshooting)?
5. One drill per stall, with a date.

Copy every miss into `error_log.md` in its standard format (Date | Problem or topic | What went wrong | Root cause | Rep 1 | Rep 2 | Rep 3).

---

## (k) Story: an incident you owned, told as a postmortem

**Rule:** only facts you supply. Every blank stays blank until you fill it. I won't suggest numbers or events. This is also the "Incident you led" story that `interview_packs/devplatform_2R.md` §j still needs, so one story covers both.

**Facts I need from you first** (answer in a message, or write them here):
- Which incident? Company, year, the system (Mongo fleet, Airflow platform, Scry inference pipeline, something else)?
- What did users or teams see, and for how long? Who noticed first: an alert, a person, a customer?
- What was your role: incident lead, the engineer who fixed it, the owner of the system?
- The first thing you did to stop the damage, and the option you didn't take.
- The root cause, and any contributing factors (process, alerting, missing tests).
- The action items: which shipped, and what changed afterwards (a number if you have one).

**Postmortem shape (2 minutes spoken, then stop):**

| Beat | ~Time | Your words |
| --- | --- | --- |
| **Situation**: the system, its scale, what broke, when | 20 s | |
| **Impact**: who was hurt, how much, for how long (numbers) | 15 s | |
| **My decision**: how it was detected, what you did first to stabilise, and the option you rejected | 35 s | |
| **Tradeoff**: what that decision cost (lost data, slower rollback, a risk you accepted) | 15 s | |
| **Root cause**: technical cause plus one contributing factor, said blamelessly | 15 s | |
| **Number**: the measurable result (time to mitigate, budget burned, repeat incidents after) | 10 s | |
| **Lesson**: one action item that shipped, and what you'd do differently | 10 s | |

**Interviewer probes (practise answering each in ≤ 30 s):**
1. How was it detected? How long from the start until someone noticed?
2. Why did you choose that mitigation and not a rollback (or a rollback and not a fix forward)?
3. How did you communicate during it, to whom, and how often?
4. What was the root cause, and how did you confirm it?
5. Was anyone at fault? How did you write that part?
6. Which action items actually shipped? Which didn't, and why?
7. How much error budget (or SLA) did it burn?
8. What alert would have caught it earlier?
9. Has anything like it happened since?
10. What would you do differently in the first 10 minutes?

---

## (z) GATE 2 checklist (Sat Nov 28 – Sun Nov 29)

Gate 2 closes Phase 2 (Weeks 4–6). **Pass every line to move to Phase 3.** Fail any line: repeat the weakest week of 4–6 once, then retake only the failed lines. Scores use the 1–4 scorecard. Gate items run with **no hints**. Claude picks the unseen items from the sealed list in K-gate and asks you "have you ever opened this?" before each timer starts.

### Before the gate (prerequisites, by Fri Nov 27)

| Prerequisite | Status today (Nov 6) | Needed |
| --- | --- | --- |
| Week 5 pack exists and was worked | **Not built** | Ask for it before Nov 16 |
| Reference cheat-sheet points for every week 1–6 | W3, W4 have K-h; W6 has K-h (this pack); **W1, W2 have none**; W5 not built | I write W1/W2 reference points; W5 comes with its pack |
| Mock scores for Weeks 4 and 5 | **None logged** | Score each mock within an hour, into `tracker.md` |
| Redo marks in the tracker | **None logged since Oct 25** | Send results (§0a) so the clean-redo rate can be computed |

### Gate lines

| # | Line | Standard | When | Result |
| --- | --- | --- | --- | --- |
| 1 | **Unseen graph or heap medium** | Solved in **35 min**, approach and complexity said in the first 5, passes your own tests + 2 edge cases traced | Sat | ☐ |
| 2 | **Unseen shortest-path variant** | Solved in **40 min**, same standard (this is the mock's coding block) | Sat | ☐ |
| 3a | **Explain the pod lifecycle** | ≤ 2 min, ≤ 5 stumbles, every rubric beat in K-gate, one follow-up answered | Sun | ☐ |
| 3b | **Explain requests vs limits** (with QoS) | Same | Sun | ☐ |
| 3c | **Explain an SLO with its error budget** (with a number and the burn-rate alert) | Same | Sun | ☐ |
| 4 | **CI/CD canary with rollback, drawn** | From blank in **45 min**: all 6 design steps, rollback trigger metrics named, Design depth ≥ 3 | Sat | ☐ |
| 5a | **Kubernetes scenario 1** (in the mock) | Troubleshooting ≥ 3: at least 5 of 6 steps said, one check per hypothesis | Sat | ☐ |
| 5b | **Kubernetes scenario 2** | Same, 20 min | Sun | ☐ |
| 5c | **Kubernetes scenario 3** | Same, 20 min | Sun | ☐ |
| 6 | **6 cheat sheets** (Weeks 1–6) rewritten from blank | Each ≥ **80%** of its reference points matched (count and write `n / N`) | Sun | ☐ ☐ ☐ ☐ ☐ ☐ |
| 7 | **Mock average** | (W4 + W5 + W6 mock averages) ÷ 3 **≥ 3.0** | Sun | ☐ |
| 8 | **End-of-week checks** 1882, 2360, 2577 | Each passed, or failed and retried the same week | Sun | ☐ ☐ ☐ |
| 9 | **Clean redo rate** | ≥ **70%** over Weeks 4–6 (Clean ÷ all redos, from the tracker) | Sun | ☐ |

**Result:** ☐ PASS → Phase 3 (Week 7, distributed systems) starts Mon Nov 30; Core-tier applications open. ☐ FAIL → weakest week: ____ ; retake lines ____ on ____.

---
---

# ANSWER KEY

Do not read a section here until you've attempted its matching section above.

---

## K-a. Warm-up answers

1. **SLI**: a measured ratio of good events to all events (e.g. requests that are non-5xx and under 300 ms). **SLO**: the target for that SLI over a window (99.9% over 30 days). **Error budget**: 1 − SLO, the bad events you're allowed (0.1%).
2. **43.2 minutes** (30 × 1,440 × 0.001).
3. It's a cause, not a symptom. Users can be fine at 90% CPU (a page for nothing) and hurting at 40% (lock contention, a slow dependency). Page on user-facing SLO burn; CPU goes to dashboards and capacity tickets.
4. Retries add load to a server that's already overloaded, and they arrive in synchronized waves, so it never recovers (a retry storm). Fix: **capped exponential backoff with jitter**, plus a **retry budget / max attempts**. Retry only idempotent calls.
5. p50 is the median request; p99 is the boundary of the slowest 1%. An average hides the tail: 1% of requests taking 2 s barely moves the mean, but a page that makes 100 backend calls hits the tail on most loads.
6. Make a choice when it's full: **block the producer** (backpressure) or **reject** (load shedding). An unbounded queue just grows latency and memory until timeouts or an OOM.
7. Dijkstra treats a node as final once it pops with the smallest distance; a negative edge found later could lower it. Stale entries: `if (d > dist[u]) continue;` right after the pop.
8. CPU over the limit → **throttled** by the CFS quota, never killed. Memory over the limit → **OOM-killed** (exit 137, `OOMKilled`).
9. **Ephemeral ports** for that one destination IP:port run out → `connect: Cannot assign requested address` (EADDRNOTAVAIL). Check: `ss -tan state time-wait | wc -l`. Fix: keep-alive / connection pooling. Stopgap: widen `ip_local_port_range`, `tcp_tw_reuse=1`.
10. Many tasks in **uninterruptible sleep (D state)**, usually waiting on disk or NFS. Linux load counts D-state tasks. Run `vmstat 1` (the `b` and `wa` columns), `ps -eo state,pid,cmd | awk '$1=="D"'`, and `iostat -x 1` (await, %util).

---

## K-b. The infra brief (short on purpose)

### Five things I'd say

1. **An SLO turns "reliable" into a number, and the budget turns it into a decision.** 99.9% good requests over 30 days = 43 minutes of budget. Spend it on releases and experiments; when it's gone, freeze risky changes until it recovers.
2. **Page on symptoms, through burn rate.** Page when the budget burns fast (14.4× over 1 h **and** 5 min = 2% of the month's budget in an hour). Ticket on a slow burn (6× over 6 h and 30 min). Causes (CPU, disk, restarts) go to dashboards.
3. **RED for services, USE for resources.** Rate, Errors, Duration tell you users hurt. Utilization, Saturation, Errors tell you why. Saturation (queue depth, pool waits) is the early warning.
4. **Retries need four guards:** only idempotent calls, capped exponential backoff with **full jitter**, retries at **one** layer inside a **retry budget** (~10%), all under a deadline.
5. **Bound everything so one slow dependency can't take the fleet down:** bounded queues, timeouts shorter than the caller's, deadlines passed down, load shed early, circuit breakers on failing dependencies.

### Reading answers (B1–B12, one line each)

- **B1** SLA = contract with penalties (money). The SLO is stricter than the SLA, so you notice before you pay.
- **B2** Users can't tell 99.999% from 100% (their own network is worse), and every extra 9 costs more and freezes change.
- **B3** 99.9% = 43.2 min / 30 days. 99.99% = 4.32 min.
- **B4** The policy (agreed in advance by the product and SRE owners) says: freeze non-critical releases, put reliability work first, and write a postmortem for any single big spend.
- **B5** Golden signals: latency, traffic, errors, saturation. RED (rate, errors, duration) for request-driven services. USE (utilization, saturation, errors) for resources such as CPU, disk, queues and pools.
- **B6** Symptoms that users feel page. Causes go to tickets or dashboards, unless they predict imminent user pain (disk full in 4 h).
- **B7** Burn rate = error ratio ÷ (1 − SLO). Burn rate 1 spends exactly the budget over the whole window.
- **B8** Long window alone: slow to fire, and it stays firing for up to an hour after the fix. Short window alone: fires on blips. Both together: significant **and** still happening. The short window is about 1/12 of the long one.
- **B9** Backoff: wait longer after each failure (base × 2ⁿ, capped). Jitter: randomise the wait so clients spread out. Retry budget: cap retries at a share of total traffic. Backoff without jitter keeps clients in lockstep, so they all retry at the same instants.
- **B10** Backpressure: the consumer slows the producer. Load shedding: the server drops excess work early and cheaply. Circuit breaker: the client stops calling a failing dependency for a cool-off, then probes it.
- **B11** Every hop gets the **remaining** time, not a fresh timeout. Without it, servers keep working on requests whose callers have already given up, which is wasted capacity during overload.
- **B12** The **load caused by the failure** keeps it going: retries, cold caches, queued backlogs (a metastable failure). Recovery needs that extra load removed (shed, stop retries), not just the trigger.

### Failure modes

| Symptom | Cause | First check |
| --- | --- | --- |
| Alert fires and clears every few minutes | Threshold on a raw noisy signal, short window, no `for` | Plot the expression over 6 h; move to multiwindow burn rate |
| 300 pages in 5 minutes | Cause-based alerts all page; grouping per instance; no inhibition | Group the firing alerts by shared labels (zone, cluster) |
| Users report errors, no alert fired | Alerting on hosts, not the edge; or scrapes failing silently | `up == 0`; edge SLI; is the always-firing Watchdog alert still arriving? |
| Average latency fine, users angry | The mean hides the tail; one route or version is slow | `histogram_quantile(0.99, …)` split by version and route |
| A 30-second dependency blip turns into a 1-hour outage | Immediate retries, no jitter, retries at several layers | Retry rate vs request rate; requests per user call |
| Latency climbs, then everything times out | Unbounded queues, no deadlines, thread pool saturated | Queue depth, pool active/max, time spent waiting for a connection |
| Prometheus OOMs or queries crawl | Cardinality explosion (a `user_id` or `path` label) | `curl -s localhost:9090/api/v1/status/tsdb \| jq .data.seriesCountByMetricName` |

---

## K-b2. Teach-back outlines and follow-up answers

### T1: SLI, SLO and the error budget (6 beats)

1. Start from the user: what does "working" mean to them? (Requests succeed, fast enough.)
2. **SLI** = good events ÷ all events, measured as close to the user as possible (load balancer or client, not the host).
3. **SLO** = a target plus a window: 99.9% over a rolling 30 days.
4. **Budget** = 1 − SLO = 43 min a month, or 1 in 1,000 requests.
5. **Policy**: the budget decides release speed. Budget left → ship. Budget gone → freeze, fix reliability first. Agreed in advance.
6. **Alert on the budget**, not raw errors (burn rate), and review the SLO every quarter against what users actually complain about.

Follow-ups:
1. Users can't tell the difference; each 9 costs about 10× more; and you'd never ship.
2. Request-based for high-traffic APIs. Time-based ("good minutes") for low traffic, or when one bad minute matters regardless of request count.
3. The error-budget policy kicks in: freeze non-urgent changes, staff reliability work. Agreed beforehand by the product owner and the SRE/platform owner, so it isn't argued mid-incident.
4. Start from what the dependencies can give you and what users notice. You can't beat your dependencies' combined availability. Start lower and tighten later.
5. Freshness and success: "99% of DAG runs start within 5 minutes of schedule" and "99.5% of runs that fail do so because of the task, not the platform". Measured per run, not per request.

### T2: Symptom-based alerting and burn rates (6 beats)

1. A page must be **urgent, actionable and user-facing**. Anything else is a ticket or a dashboard.
2. Measure the SLI at the edge; alert on **burn rate** = error ratio ÷ budget.
3. **Fast burn → page:** 14.4× over 1 h and 5 m (2% of the month's budget in an hour).
4. **Slow burn → ticket:** 6× over 6 h and 30 m (5% in 6 hours).
5. Two windows: the long one = significant, the short one = still happening (fast reset after the fix).
6. Make the pipeline quiet: group by service/zone, inhibit downstream noise, and a Watchdog alert that always fires so silence itself is detectable.

Follow-ups:
1. See beat 5. Long-only stays firing ~1 h after the fix; short-only pages on blips.
2. 2% of a 30-day budget in 1 hour: 0.02 × 720 hours = 14.4.
3. A few failures swing the ratio wildly. Use longer windows, a minimum request count (`and sum(rate(...)) > N`), synthetic probe traffic, or a time-based SLI.
4. A **dead man's switch**: an always-firing Watchdog alert routed to an external service that pages if it **stops** arriving.
5. `group_by` (zone, cluster, alertname, not instance), `inhibit_rules` (zone down → mute per-service alerts), routing causes to tickets, and clustered Alertmanager replicas so pages aren't duplicated.

### T3: Retries with backoff and jitter (6 beats)

1. Retries fix **transient** failures and make **overload** worse. The design is about telling them apart.
2. Only retry **idempotent** operations, or make them idempotent (idempotency key on POST).
3. **Capped exponential backoff with full jitter**: `sleep = random(0, min(cap, base × 2^attempt))`.
4. Retry at **one** layer (usually the edge or the client nearest the failure), never at every hop.
5. A **retry budget**: retries ≤ ~10% of requests; past that, fail fast.
6. Honour server signals (429/503 + `Retry-After`), and stop when the request's deadline is spent.

Follow-ups:
1. GET/PUT/DELETE by definition; reads in general. For POST: the client sends an idempotency key; the server stores key → result and returns the stored result on a repeat.
2. `sleep = rand_uniform(0, min(cap, base * 2^attempt))`.
3. 3 × 3 × 3 = **27** calls at the bottom for one user request, arriving exactly when the bottom layer is struggling.
4. A retry budget caps the extra load from retries. A circuit breaker stops **all** calls to a dependency that's clearly down, and probes for recovery.
5. 429 or 503 with `Retry-After`; gRPC `RESOURCE_EXHAUSTED` / `UNAVAILABLE` plus pushback metadata. Clients must treat them as "back off", not "retry now".

### T4: Backpressure and cascading failure (6 beats)

1. The chain: a dependency slows → callers' threads and connections wait → their queues fill → they time out → callers retry → more load → the next layer slows.
2. **Bound every queue and pool.** When full: block (backpressure) or reject (shed).
3. **Timeouts shorter than the caller's**, and **deadlines propagated** down the stack.
4. **Shed early and cheaply**: reject at the front door before doing work; drop the lowest-priority traffic first.
5. **Circuit breakers** on dependencies; **graceful degradation** (serve stale or partial results).
6. Watch for **metastable** states: if the extra load (retries, cold cache) keeps the system down after the trigger is gone, remove that load deliberately.

Follow-ups:
1. Block when the producer can wait and the work must not be lost (a pipeline, a queue consumer). Drop when it's interactive and a late answer is worthless (shed with a fast 503).
2. Each hop sends the remaining time; the first deadline is set at the edge from the user-facing latency target.
3. Lowest priority first (batch, prefetch, retries), then the oldest queued requests: their callers have probably given up already.
4. The trigger caused extra load (retries, cache misses, a backlog) that's larger than the capacity left. That load keeps it down. Shed load, stop retries, warm the cache, then let traffic back in gradually.
5. Lag growing while consumers are healthy and the backlog is durable = backpressure working (the queue absorbs a burst). Lag growing without bound past retention, or consumers falling behind forever = failing; add consumers, or shed or sample.

---

## K-c. Lab: expected observations and reference rules

### Reference `slo_rules.yml` expressions (check only after `promtool test rules` has run)

```yaml
# recording rules: one per window; only the [5m] changes
- record: slo:sli_error:ratio_rate5m
  expr: |
    sum(rate(http_requests_total{job="toy",code=~"5.."}[5m]))
    /
    sum(rate(http_requests_total{job="toy"}[5m]))
# ... same for [30m], [1h], [6h]

# fast burn: 14.4x the 0.1% budget, over 1h AND 5m
expr: slo:sli_error:ratio_rate1h > (14.4 * 0.001) and slo:sli_error:ratio_rate5m > (14.4 * 0.001)

# slow burn: 6x the budget, over 6h AND 30m
expr: slo:sli_error:ratio_rate6h > (6 * 0.001) and slo:sli_error:ratio_rate30m > (6 * 0.001)
```

Common slips: `sum by (code)` in the SLI (wrong labels, so `and` matches nothing or the test labels don't match), `rate()` on the ratio instead of a ratio of rates, `0.1` instead of `0.001` for the budget, `or` instead of `and`.

### What each step shows

| Step | Expect | What it proves |
| --- | --- | --- |
| `promtool check rules` | `SUCCESS: 6 rules found` | Your PromQL parses. Run it in CI on every rule change. |
| `promtool test rules` | `SUCCESS` | Your alerts fire on the synthetic outage and stay quiet on the healthy hour, before they ever see real traffic. |
| `promtool check config` | `SUCCESS` for the config and the rule file it loads | A bad rule file can't take down a Prometheus reload. |
| `amtool check-config` | `Checking 'alertmanager.yml'  SUCCESS`, then a summary of routes, receivers and inhibit rules | Same, for routing. |
| Targets | `{"job": "toy", "health": "up"}` | Scrapes work. `up` is the first thing to check when an alert should have fired. |
| Request rate | About **15–20** (req/s; curl in a shell loop doesn't reach a full 20) | Load is flowing. |
| SLI 5m | **`0`**, not empty. The app starts its 500 counter at 0. A counter that only appears after the first error gives an **empty** SLI, so alerts silently never evaluate. Initialise error counters at 0 in real services. | |
| p99 | About **0.049**: latencies of 10–40 ms all fall in the 25–50 ms bucket, and `histogram_quantile` interpolates inside a bucket | Quantiles from histograms are only as precise as the bucket edges. Put a bucket edge at your SLO threshold. |
| Lab 3: `pending` | **SlowBurn first** (after roughly 20–30 s), then FastBurn (after roughly 45–60 s). The slow alert's threshold (0.6%) is lower, and its long window is still mostly clean data, so it crosses first. | Thresholds and windows set detection time. |
| Lab 3: `firing` | Each one about **1 minute after `pending`** (`for: 1m`). | `for` trades detection speed for flap resistance. |
| Lab 3: fake pager | One group per `slo` label. You may get a SlowBurn line first. Once FastBurn fires, the ticket drops out of the notifications. | Grouping + inhibition: one page, not two. |
| Lab 3: v2 alerts | FastBurn `active  inhibitedBy=[]` · SlowBurn `suppressed  inhibitedBy=["<id>"]` | The ticket is still known. It's inhibited, not lost. |
| Lab 4: silence | `silence add` prints an ID. The pager goes quiet for 3+ minutes (past the 2 m `repeat_interval`). | Silences mute notifications only. The alert still fires in Prometheus (check `/api/v1/alerts`). |
| Lab 4: ticket while page is silenced | Current Alertmanager evaluates inhibition from **firing** alerts whether or not they're silenced, so the ticket should stay suppressed. **Check what your version does and write it down.** | Silencing a source doesn't unleash its targets. |
| Lab 4: heal | **FastBurn resolves about 4–5 min after the fix**: the 5 m window has to drain. **SlowBurn keeps firing for about 30 min** (its short window is 30 m), and **its ticket appears once the page resolves**, because inhibition only lasts while the page fires. | Short window = fast reset. Inhibition has an edge: name it as a tradeoff. |
| Lab 5 p99 | Settles near **0.49**: 310–340 ms falls in the 250–500 ms bucket and gets interpolated toward the top of that bucket | Same bucket lesson. A 300 ms latency SLO needs a 0.3 bucket edge. |

Timings are estimates from the window maths, not measured here. Write down your real times; the differences are worth explaining.

---

## K-d0. Template drill: how it's graded

You pass on your own file: compiles with zero warnings, every assert passes, under 15:00. **The template in words** (check your file against it after the timer stops):

**W6-T1 Dijkstra**
1. `dist(n, INF)` as `long long`; `dist[s] = 0`; min-heap of `(dist, node)`; push `(0, s)`.
2. Pop `(d, u)`. **If `d > dist[u]`, skip**: it's a stale entry.
3. (Optional) If `u` is the target, stop: it's final.
4. For each edge `(v, w)`: if `d + w < dist[v]`, set `dist[v]`, set `parent[v] = u`, push `(dist[v], v)`.
5. After the loop, `INF` means unreachable. Check before using it.

**W6-T2 0-1 BFS**
1. `dist(n, INF)`; `dist[s] = 0`; deque holding `s`.
2. Pop from the **front**.
3. For each edge `(v, w)` with `w` in {0, 1}: if `dist[u] + w < dist[v]`, update, then **0-edge → `push_front`, 1-edge → `push_back`**.
4. No visited array. A node may sit in the deque twice; the stale copy does no harm. Correct because the deque only ever holds distances `d` and `d + 1`, smaller ones in front: it's a heap with two values.

**Common slips**
- `priority_queue<P, vector<P>, greater<P>>` is the **min**-heap; the pair must be `(dist, node)`, distance first.
- `int` distances: 1e5 edges × 1e9 weights overflows. Use `long long` and an INF like `LLONG_MAX / 4`, so `INF + w` can't wrap.
- Marking "visited" at **push** time instead of pop time: breaks Dijkstra whenever a better path arrives later.
- Counting settles in the wrong place: a node is settled when it pops **and** passes the stale check, not when it's pushed.
- 0-1 BFS: putting a 1-edge at the front, or skipping a node already seen (the 0-edge improvement then never happens).
- Grid form: forgetting bounds on **both** coordinates, or mixing up `(r, c)` with `(x, y)`.

---

## K-d. Hint ladders (one rung at a time, only after 25 minutes stuck)

**743⚑ Network Delay Time**
1. Pattern: single-source shortest path with non-negative weights.
2. Data structure: adjacency list, a min-heap of `(time, node)`, a distance array set to infinity.
3. Key insight: the answer is the **largest** shortest distance, and **−1 if any node is still infinite**. With 11 submits, the usual suspects are: nodes are **1-indexed**, the stale-entry check, and taking the max over an infinite value.
4. Skeleton: build `adj` (size n + 1) → `dist[k] = 0`, push → pop, skip stale, relax each edge, push on improvement → scan nodes 1..n: any infinite → −1, else the max.

**787 Cheapest Flights Within K Stops**
1. Pattern: shortest path with a hop limit. Bellman-Ford, limited to k + 1 rounds (or BFS level by level over `(city, stops)`).
2. Data structure: a cost array plus a **copy** of it each round.
3. Key insight: k stops = **k + 1 edges**. Each round must relax from the **previous round's** costs (the copy). Relaxing in place lets one round chain several flights and breaks the limit. Plain Dijkstra fails because the cheapest arrival may already have used too many stops.
4. Skeleton: `cost[src] = 0` → repeat k + 1 times: `next = cost`; for each flight `(u, v, p)` with `cost[u]` finite, `next[v] = min(next[v], cost[u] + p)`; `cost = next` → `cost[dst]` or −1.

**1631 Path With Minimum Effort**
1. Pattern: minimax path. Dijkstra where a path's cost is its **largest** step, not the sum. (Alternatives: binary search the answer + BFS; union-find over sorted edges.)
2. Data structure: min-heap of `(effort, r, c)` and an effort grid set to infinity.
3. Key insight: relax with `max(effort so far, |h[u] − h[v]|)`. Taking a max never lowers a path's cost, which is exactly the property Dijkstra needs. You can return when the target pops.
4. Skeleton: `effort[0][0] = 0`, push → pop, skip stale, return at the target → 4 neighbours: candidate = max(d, abs diff); if smaller, update and push.

**778 Swim in Rising Water**
1. Pattern: minimax path again: the answer is the highest cell you must pass through.
2. Data structure: min-heap keyed by "highest elevation seen so far", plus a visited grid. (Or binary search on t + BFS; or union-find adding cells in height order.)
3. Key insight: the start costs **`grid[0][0]`, not 0**. Entering a cell costs `max(cost so far, grid[v])`. The answer is the cost when the bottom-right cell pops.
4. Skeleton: push `(grid[0][0], 0, 0)` → pop the smallest; if it's the target, return it; mark visited → push each unvisited neighbour with `max(t, grid[v])`.

**1368 Min Cost Valid Path in a Grid**
1. Pattern: shortest path where every edge costs 0 or 1 → **0-1 BFS**.
2. Data structure: a deque of cells and a distance grid.
3. Key insight: moving the way the cell's arrow points costs **0**; any other direction costs **1** (you change that arrow once). Arrow codes: 1 right, 2 left, 3 down, 4 up. 0-cost moves go to the front, 1-cost moves to the back. The deque stays sorted by distance, which is why it can replace the heap.
4. Skeleton: `dist[0][0] = 0`, deque = {start} → pop front → for each of the 4 directions: w = (arrow matches ? 0 : 1); if `dist + w` improves the neighbour, update, then push front (w = 0) or back (w = 1) → return the bottom-right distance.

**1928 Minimum Cost to Reach Destination in Time**
1. Pattern: state-augmented shortest path: the real state is **(city, time used)**, not just the city.
2. Data structure: min-heap of `(fees, time, city)` ordered by fees, plus `bestTime[city]`. (Alternative: DP `dp[t][city]` = min fees to stand at city at time t, for t ≤ maxTime.)
3. Key insight: pop states in fee order. A later state at the same city is worth keeping **only if it arrives with less time** than every earlier, cheaper one. Cheaper **and** faster dominates. The fee counts the start city too. (It's safe to prune at push time because every edge into city v adds the same fee, `passingFees[v]`.)
4. Skeleton: push `(fees[0], 0, 0)`, `bestTime[0] = 0` → pop `(c, t, u)`; if u is the last city, return c → for each `(v, w)`: nt = t + w; if nt ≤ maxTime and nt < bestTime[v], update `bestTime[v]` and push `(c + fees[v], nt, v)` → after the loop, −1.

**2203 Minimum Weighted Subgraph With the Required Paths**
1. Pattern: several Dijkstras combined, one of them on the **reversed** graph.
2. Data structure: three `long long` distance arrays: from src1, from src2 (forward graph), and **to** dest (Dijkstra from dest on the reversed graph).
3. Key insight: the best subgraph is a **Y**: src1 → m and src2 → m, then a shared m → dest. Answer = min over every m of `d1[m] + d2[m] + dRev[m]`. The shared leg is counted once because it's shared. Sums reach about 1e10, so use `long long`.
4. Skeleton: build `adj` and `radj` → three Dijkstra runs → loop over m with all three finite, take the min → −1 if none.

**2353 Design a Food Rating System**
1. Pattern: a design with two indexes kept in sync (same family as Week 5's 2349).
2. Data structure: `food → (cuisine, rating)` and `cuisine → set<pair<int, string>>` holding `(−rating, name)`, so the set's first element is the answer. (Alternative: a heap per cuisine with lazy deletion, the Week 4 template.)
3. Key insight: on `changeRating`, **erase the old pair first** (using the old rating from the map), then update the map, then insert the new pair. Updating the map first means you erase a pair that doesn't exist, and the stale one stays. Negating the rating makes "highest rating, then smallest name" the set's natural order.
4. Skeleton: constructor fills both maps → change: look up cuisine and old rating; erase `(−old, food)`; store the new rating; insert `(−new, food)` → highest: `begin()->second`.

**2577 (sealed: read only after Friday's check)**
<details><summary>Open after the check</summary>

1. Pattern: Dijkstra on arrival time over cells, with a waiting rule.
2. Data structure: min-heap of `(time, r, c)` and a time grid.
3. Key insight: if both neighbours of the start need time > 1, you can never move: return −1. Otherwise you can always wait by stepping back and forth (2 s per bounce). Arrival times at a cell all have the same parity as `r + c` (each move flips it). So to enter a cell needing `g` at time `t`: if `t + 1 ≥ g`, arrive at `t + 1`; else arrive at `g` if `g − t` is odd, or `g + 1` if it's even.
4. Skeleton: the −1 check → standard Dijkstra; pop, skip stale, return at the target → for each neighbour, compute the arrival with the wait rule, relax, push.
</details>

---

## K-e. Troubleshooting: interviewer sheets and scoring

**Scoring per drill (out of 6, mapped to the 1–4 Troubleshooting score):** 1 point per routine step done fully. 6 = 4, 5 = 3, 3–4 = 2, ≤ 2 = 1. A step counts only if you **said** it. A Check counts only with the expected result named. A change counts only with its why and its risk.

### Drill 1: latency doubled after a release

**Facts to give when asked:**
- *What changed:* v2.31 = feature-flag cleanup plus dependency bumps, including a **major version of the HTTP client library** used to call `payments` and `inventory`.
- *Scope:* all 30 pods, all regions, but only endpoints that call `payments` or `inventory`. Endpoints with no downstream calls are unaffected.
- *Canary:* the analysis compared **error rate and mean latency**. Mean went 52 → 58 ms, inside its threshold. Nobody compared p99 per version.
- *Downstreams' own server-side latency:* unchanged.
- *Traces:* a new span, "acquire connection", p99 150–200 ms (was ~0).
- *On a pod:* `ss -tan | awk 'NR>1{print $1}' | sort | uniq -c` → about 10 `ESTAB` to the downstream (was ~60), **4,000+ `TIME-WAIT`** (was ~100).
- *CPU:* up 15% per pod (more TLS handshakes). Not throttled (`container_cpu_cfs_throttled_periods_total` flat).
- *Rollback:* available, about 8 minutes. v2.31 has no schema migration.

**Root cause:** the new client's default pool is **10 connections per host** (was 100), with a short idle timeout. At full load, requests queue for a connection (the tail grows; the median barely moves), and connections churn (TIME_WAIT climbs, handshake CPU rises).

**Strong answer:** *Clarify* what changed and when, p99 vs p50, which endpoints. *Scope*: all pods, only downstream-calling routes → not one bad node. *Stabilise*: **roll back** (the SLO is burning, there's a known-good version, no migration). Risk: lose v2.31's fixes. *Hypothesise*, ranked: (1) client-side wait from the new library (pool, DNS or TLS), (2) slower downstream, (3) CPU throttling, (4) GC. *Check*: p99 by version; client-side vs server-side latency for the downstream (the gap means the client is waiting); connection-acquire spans; `ss` counts; throttling metric. *Fix*: set the pool size and idle timeout explicitly; re-release through a canary. *Prevent*: canary analysis on **p99 and saturation per version**, not the mean; pin client defaults in config; read major-version release notes; keep the latency SLO alert, which did fire.

### Drill 2: alert storm

**Facts to give when asked:**
- *Grouping by labels:* 290 of 312 alerts carry `zone="use1-az2"`. The other 22 are services in other zones that call az2 services.
- *User impact (edge SLO dashboard):* checkout availability 99.95% → 97% and burning; search and login fine.
- *Cloud status page* at 02:20: "Increased EBS latency in one Availability Zone".
- *Load balancers* still send traffic to az2 targets: health checks are TCP-only.
- *Alertmanager config:* `group_by: [alertname, instance]`, no inhibit rules, every rule `severity: page`.
- *Duplicates:* the two Alertmanager replicas show **0 cluster peers** (`amtool cluster show`). Each sends every notification.
- *Help:* a secondary on-call exists and hasn't been paged.

**Root cause:** the incident is a zonal storage degradation. The storm is an **alerting design** problem: cause-based alerts all page, grouping per instance, no inhibition, and unclustered Alertmanagers doubling every page.

**Strong answer:** *Clarify*: are users hurting? Which signal is a symptom? *Scope*: group by shared labels → one zone. *Stabilise*: declare an incident, page the secondary, one incident lead. **Silence the cause alerts for `zone=use1-az2` for 1 h with a comment, keeping SLO pages live** (risk: you miss a second, unrelated problem in that zone, so keep the edge SLO pages unsilenced). Drain the zone at the load balancer (risk: the other zones need the headroom, so check capacity first). *Hypothesise*: zonal infra event; a shared dependency (DNS, Kafka, a database primary in az2); the monitoring itself is broken (one Prometheus in az2 losing scrapes = a `TargetDown` storm). *Check*: alert labels grouped; the cloud status page; `iostat -x 1` on an az2 node (await); the edge SLI. *Fix and prevent*: page only on symptom burn at the edge; causes become tickets; `group_by: [alertname, cluster, zone]`; inhibit rule "zone down → mute per-service alerts in that zone"; fix Alertmanager clustering; deep health checks so the load balancer drains a bad zone itself; a weekly page-count review.

### Drill 3: suddenly slow service

**Facts to give when asked:**
- *Hosts:* all 12 VMs equally slow, so not one bad host. CPU 45% (was 30%), no steal, disks idle. **App thread pool 200 of 200 busy**, queue growing.
- *Load balancer:* RPS **4.0k → 5.5k**, although users are searching as usual. The upstream BFF retries search calls **twice** on timeout.
- *Redis:* **shard 4 was replaced at 09:58** by auto-repair. The new node is empty. Hit rate **92% → 70%**.
- *Postgres replicas:* CPU 95%; connections at the max (500); query p99 8 ms → 600 ms.
- *App client:* 200 ms DB timeout, then **up to 3 immediate retries**, no backoff. `retry_attempts_total` is now ~2× the query rate.
- *Primary DB:* fine (search only reads from replicas).

**Root cause:** a cold cache shard sent misses to the read replicas. The replicas slowed, queries hit the 200 ms timeout, and immediate retries at two layers (app ×3, BFF ×2) multiplied the load. The replicas stay saturated even as the cache warms: the retries keep it down (metastable).

**Strong answer:** *Clarify*: since when, which requests, did anything change (no deploy → look for infra changes: the shard replacement). *Scope*: all hosts → shared dependency, not a host. *Stabilise*: **cut the amplification first**: turn off app-level retries (flag or config) and cap BFF retries (risk: some transient failures now reach users, but far fewer than the timeouts now). Shed or rate-limit at the load balancer; serve stale or degraded results; add a read replica if one's quick. *Hypothesise*, ranked: (1) a dependency slowed (cache or DB), (2) retry amplification, (3) host resources, (4) GC or thread pool sizing. *Check*: RED per dependency; cache hit rate by shard; replica connections and latency; retries ÷ requests; LB RPS vs user sessions. *Fix*: warm shard 4 (or let it warm with retries off), then restore traffic gradually. *Prevent*: backoff with full jitter, a retry budget, retries at one layer only, deadline propagation, a circuit breaker on the DB client; warm replacement cache nodes before they take traffic; a ticket alert on hit-rate drops; a load test with one cold shard.

---

## K-f. Design: reference outline (compare after your drawing)

**Requirements and numbers (say these first)**
- 20M active series ÷ 15 s ≈ **1.3M samples/s** ingested.
- At ~1.3 bytes/sample compressed: 1.3M × 86,400 × 1.3 ≈ **150 GB/day** at full resolution.
- 13 months at full resolution ≈ 60 TB. With **downsampling** (raw for 30 days, 5-min after that): ~4.5 TB + ~3 TB ≈ **under 10 TB** in object storage.
- Recent data in memory: about 3–8 KB per active series → **60–160 GB per replica**, × 3 replicas, sharded across ingesters.
- Page within 2 minutes: scrape 15 s + rule evaluation every 30 s + `for: 1m` + Alertmanager `group_wait` 30 s ≈ 2 min. Say this budget out loud.

**API**
- **Pull** with per-cluster/per-region Prometheus (or agents / OpenTelemetry collectors) scraping exporters; **`remote_write`** to a central store.
- Rules as code: each team's rules live in Git, are checked with `promtool` in CI, and are loaded per tenant.
- Query: PromQL through a query frontend (splits long queries, caches results).

**Data**
- Series = metric name + labels. Tenant = team. **Per-tenant limits** on series count and ingestion rate.
- Hot: ingesters (memory + WAL), replicated 3×. Cold: blocks in object storage, compacted and downsampled.
- Central store: a horizontally scalable Prometheus-compatible TSDB (Mimir, Thanos, Cortex, VictoriaMetrics, M3). Name one, and why.

**Deep dive (pick one)**
- *Where rules run:* **critical SLO pages evaluate locally** in each region's Prometheus (they survive a central outage); global and cross-region rules run on the central ruler. Tradeoff: duplicated rules vs blast radius.
- *Cardinality:* limits per tenant and per metric; reject or drop at ingest; a "top series by metric" report; ban unbounded labels (user ID, full URL path) in review.
- *Alertmanager HA:* 3 replicas, gossip-clustered; each Prometheus sends to **all** replicas; the cluster dedupes. Accept a rare duplicate over a missed page.

**Failures (at least 5)**
1. Central store down → regional Prometheus keeps alerting locally; `remote_write` buffers in the WAL (~2 h) and replays.
2. A region is lost → its local alerts die with it, so **cross-region probes** (blackbox) and the edge SLI from other regions must page.
3. Cardinality explosion → ingester OOM → per-tenant limits shed the bad tenant, not everyone.
4. Alertmanager split brain → duplicate pages (acceptable) rather than missed pages.
5. The whole pipeline silently stops → **Watchdog dead man's switch** to an external service.
6. A bad rule deploy → the CI `promtool` check, staged rollout of rule changes.
7. A slow query takes down the query path → query limits, timeouts, a separate read path from the write path.

**Tradeoffs (at least 3)**
- Pull vs push: pull gives `up` for free and server-side control; push suits short-lived jobs and firewalled networks.
- Local vs central evaluation: resilience vs a global view.
- Retention vs cost: downsampling loses spikes, so keep raw data longer for SLO metrics.
- Kafka between ingest and store: replay and decoupling vs another system to run.
- **At 10×:** shard by tenant, add ingester zones, more aggressive downsampling, and push cardinality budgets onto teams.

**Critique rubric:** numbers said before boxes ☐ · local alerting survives a central outage ☐ · meta-monitoring named ☐ · cardinality controls ☐ · Alertmanager HA and dedupe ☐ · 5+ failures with mitigations ☐ · 3+ tradeoffs ☐ · the 2-minute page budget broken into parts ☐.

---

## K-g. Flashcard answers

1. **SLI**: measured good ÷ total. **SLO**: target for the SLI over a window. **SLA**: a contract with penalties, looser than the SLO. **Error budget**: 1 − SLO, the bad events you're allowed, spent on change.
2. **43.2 min.** Burn rate 1 spends the whole budget in exactly 30 days. 14.4× sustained for 1 h spends **2%** of the month's budget; left alone, it would spend the whole budget in about 2 days.
3. The long window proves the problem is significant, not a blip. The short window (≈ 1/12 of it) proves it's still happening, so the alert resets minutes after the fix instead of an hour.
4. Page on **symptoms** users feel (SLO burn at the edge). **Causes** (CPU, disk, restarts, lag) go to tickets or dashboards, unless they predict imminent user pain.
5. Backoff spaces retries out so a struggling server has room to recover. Jitter spreads clients apart so they don't retry in synchronized waves. Full jitter: `random(0, min(cap, base × 2^n))`.
6. Up to **27** calls at the bottom per user request. Fixes: retry at one layer only, a retry budget (≤ ~10%), backoff with jitter, honour 429/503 + `Retry-After`.
7. **Backpressure**: a full consumer slows the producer (block). **Load shedding**: the server rejects excess work early and cheaply. **Circuit breaker**: the client stops calling a failing dependency for a cool-off, then probes it.
8. `sum(rate(http_requests_total{code=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))` · `histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))`
9. `amtool --alertmanager.url=http://localhost:9093 silence add alertname=X --duration=1h --comment="why"` · `amtool silence query` · `amtool silence expire <id>`
10. Your own Monday file, once it passes the §d0 asserts. Grade against K-d0.

---

## K-h. Reference cheat-sheet points (compare after writing yours; target ≥ 80% matching)

**Top five:**
1. An SLO turns "reliable" into a number; the error budget turns it into a release decision. 99.9% = 43 min a month.
2. Page on symptoms through burn rate: 14.4× over 1 h and 5 m pages, 6× over 6 h and 30 m tickets, causes go to dashboards.
3. RED for services, USE for resources; saturation is the early warning.
4. Retries: idempotent only, capped exponential backoff with full jitter, one layer, a retry budget, under a deadline.
5. Bound every queue, propagate deadlines, shed early, break circuits, or one slow dependency takes down the fleet.

**Commands:**

| I want to… | Command |
| --- | --- |
| See which scrape targets are down | `up == 0` · `curl -s localhost:9090/api/v1/targets \| jq '.data.activeTargets[] \| {job: .labels.job, health}'` |
| 5-minute error ratio | `sum(rate(http_requests_total{code=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))` |
| p99 latency | `histogram_quantile(0.99, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))` |
| Burn rate | error ratio ÷ (1 − SLO) |
| Validate and unit-test rules | `promtool check rules r.yml` · `promtool test rules t.yml` |
| See firing and pending alerts | `curl -s localhost:9090/api/v1/alerts \| jq` |
| See inhibited or silenced alerts | `curl -s localhost:9093/api/v2/alerts \| jq '.[] \| {n: .labels.alertname, s: .status}'` |
| Silence, list, expire | `amtool silence add alertname=X --duration=1h --comment=…` · `amtool silence query` · `amtool silence expire <id>` |
| Find high-cardinality metrics | `curl -s localhost:9090/api/v1/status/tsdb \| jq .data.seriesCountByMetricName` |
| Count TIME_WAIT / pool churn on a client | `ss -tan state time-wait \| wc -l` |

**Failure modes:** the seven rows of the K-b table.

**Bottom: three interview questions and the story that fits:**

| Interview question | Story | The number to say |
| --- | --- | --- |
| "Tell me about an incident you owned." | Your §k postmortem | (yours: time to mitigate, impact) |
| "How do you decide what to alert on?" | SLO-based alerting on your Airflow platform, **only if you actually did it** | (yours) |
| "How would you make a flaky dependency safe to call?" | Retries and backpressure on the Scry event pipeline (10M+ events/day), **only if true** | (yours) |

---

## K-j. Saturday mock interviewer sheet (for Claude; don't read)

- 0–5: 90-second intro. Score Communication.
- 5–45: **gate G2**, one shortest-path variant from the K-gate pool, confirmed unseen. No hints (it's a gate item). Score Approach, Working code, Fluency, Testing.
- 45–70: **gate S1**, the first K8s scenario from the K-gate pool. Answer only from its facts. Score Troubleshooting with the 6-step rule.
- 70–75: candidate's questions.
- Composure: note the time from any visible mistake to recovery.
- Then canary design (score Design depth), then G1.

---

## K-gate. Gate 2 sealed sheet (for Claude; don't read)

<details><summary>Sealed. Claude only.</summary>

**Unseen pools.** None were attempted on the account as of Oct 6. Confirm with the candidate before starting; if seen, take the next one.
- **G1, graph or heap medium (35 min):** 2101 Detonate the Maximum Bombs · 1801 Number of Orders in the Backlog · 2462 Total Cost to Hire K Workers.
- **G2, shortest-path variant (40 min):** 1786 Number of Restricted Paths From First to Last Node · 1129 Shortest Path with Alternating Colors · 1514 Path with Maximum Probability (in the plan's optional warm-up list, so ask).

**Kubernetes scenarios (none used in the Week 4 drills or the devplatform lab):**
- **S1. Pods stuck Pending after a node-group change; the PVC is bound.** Facts: events say `volume node affinity conflict`; the PV is in zone a, the new nodes are only in zone b; the StorageClass uses `Immediate` binding. Fix: nodes in zone a, or restore the volume in zone b; prevent with `volumeBindingMode: WaitForFirstConsumer` and zone-spread node groups.
- **S2. Intermittent ~5 s delays on outbound calls from pods.** Facts: `/etc/resolv.conf` has `ndots:5` and 3 search domains; CoreDNS latency is fine; `conntrack -S` shows `insert_failed` climbing (a race when A and AAAA queries go out in parallel over UDP); the 5 s = the resolver timeout. Fix: NodeLocal DNSCache, `dnsConfig` with `ndots: 2` or FQDNs with a trailing dot, the `single-request-reopen` option.
- **S3. A node goes NotReady and pods get evicted with `DiskPressure`.** Facts: `kubectl describe node` shows DiskPressure; `kubectl debug node/<n>` → `df -h /host/var/lib/containerd` 92%; one pod writes 2 GB/h of logs to stdout; log rotation is at defaults. Fix: rotate (`containerLogMaxSize`), fix the noisy app, image GC thresholds, `ephemeral-storage` requests and limits.
- **Spare. ImagePullBackOff only on the new node group.** Facts: the node IAM role on the new group lacks registry read; the old group's role has it. Fix: attach the policy; prevent with node-group templates in IaC.

**Explain rubrics (all beats, ≤ 2 min, ≤ 5 stumbles):**
- *Pod lifecycle:* phases Pending → Running → Succeeded / Failed (+ Unknown) · scheduler binds, kubelet runs (CRI, CNI, volumes) · init containers in order, then app containers · startup → liveness / readiness probes · container states Waiting / Running / Terminated, restart policy, CrashLoopBackOff (10 s doubling, capped at 5 min) · deletion: endpoints removed and preStop run, SIGTERM, grace period (30 s default), SIGKILL.
- *Requests vs limits:* requests = scheduling reservation and CPU weight · limits = cgroup ceiling · CPU over the limit throttles, memory over the limit OOM-kills · QoS classes from those rules · eviction order under node pressure · a position on CPU limits, and memory limit = request for critical pods.
- *SLO + error budget:* SLI definition · target and window · the budget as a number (43.2 min / 30 d at 99.9%) · burn-rate alerting (14.4× over 1 h and 5 m) · the error-budget policy and who agrees to it.

**Canary design rubric (45 min, Design depth ≥ 3):** build once, immutable artifact by digest · canary small (1–5%), compared against a **baseline of the same age**, not the old fleet · analysis on error rate, **p99**, saturation and a business metric · stepped promotion with bake times · **automatic rollback** when analysis fails or the SLO burns · rollback = re-point to the previous digest, no rebuild · database changes in expand/contract form so rollback is safe · feature flags to decouple deploy from release · failures: low-traffic canary is noisy, config changes that skip the pipeline, a rollback that fails because of a migration, a stuck rollout · tradeoffs: speed vs safety, canary size vs signal, automatic vs human gates.

</details>

---

## K-k. Story reference beats (coverage check only, not content)

Your story should contain each of these. Tick what you said in your recording:

- ☐ The system and its scale, in one sentence
- ☐ User or business impact as a number (duration, requests, customers, jobs)
- ☐ How it was detected and how long that took
- ☐ **Stabilise before fixing**: what you did first, and the option you rejected
- ☐ The cost or risk of that choice
- ☐ Communication: who, which channel, how often
- ☐ The root cause, plus one contributing factor, with no blame on a person
- ☐ An action item that **shipped**, with what it changed (a number if you have one)
- ☐ What you'd do differently in the first 10 minutes
- ☐ Under 2 minutes, then you stopped
