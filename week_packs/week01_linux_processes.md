# WEEK PACK — Week 1 (Oct 12–18): Linux and processes

Infra layer: signals, memory, files, cgroups · Code: prefix sums + sliding / exactly-K windows · Design: URL health-check service · Gates ahead: Oct 31, Nov 21, Dec 12, Dec 19

**Rule for this file:** do every section cold first. All answers are in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section.

---

## 0. This week's code (from the plan, in order)

Clear due reviews first. If more than 5 are due, do no new problems that day. LC 1 (11 submits) and LC 3 (23 submits) are shaky, so they go first in reviews.

| Day | Code block | Problems |
| --- | --- | --- |
| Mon Oct 12 | Template drill (§1), then required row 1 | 974 Subarray Sums Divisible by K |
| Tue Oct 13 | Required row 2 + any core you've never solved | 1248 Count Number of Nice Subarrays |
| Wed Oct 14 | Required row 3 + the practical row | 992 Subarrays with K Different Integers · 933 Number of Recent Calls |
| Thu Oct 15 | Rest of the core four, then "after required" rows | 1 Two Sum · 49 Group Anagrams · 3 Longest Substring Without Repeating Characters · 11 Container With Most Water |
| Fri Oct 16 | End-of-week check: unseen, 45 min, alone | **2444** (don't open it before Friday) |

For each problem, say "start 974" (or whichever number) and I'll log the start time. Hints come one rung at a time, and only after 25 minutes stuck.

---

## 1. C++ template drill (target: under 15 min, compiled, asserts passing)

Use a blank file and no notes. Compile with `g++ -std=c++17 -Wall -Wextra drill.cpp && ./a.out`.
⚠ On your Mac, `<bits/stdc++.h>` **does not exist** (Apple clang). Write the explicit headers from memory, which is part of the drill.

Write these five functions plus a `main` with asserts:

| # | Function | Spec |
| --- | --- | --- |
| T1 | `buildPrefix(a)` | `pre` such that `sum(l..r)` is one subtraction |
| T2 | `countSumEquals(a, target)` | number of subarrays summing to `target`; must work with negatives |
| T3 | `maxSumFixed(a, k)` | max sum over all length-k windows |
| T4 | `longestAtMost(a, s)` | longest window with sum ≤ s, `a` non-negative |
| T5 | `atMost(a, k)` + `exactly(a, k)` | count subarrays with sum ≤ k (non-negative `a`), then exactly k from that |

Asserts your code must pass:
```
a = {1,0,1,0,1}
pre[5] - pre[1] == 2
countSumEquals(a, 2) == 4
countSumEquals({1,-1,0}, 0) == 3
maxSumFixed({2,1,5,1,3,2}, 3) == 9
longestAtMost({3,1,2,1,1,4}, 5) == 4
exactly(a, 2) == 4
exactly(a, 0) == countSumEquals(a, 0)
```

Answer these aloud after the code compiles:
1. Why is `pre` of size n+1, and what is `pre[0]`?
2. In T2, why does the map start with one entry, and what goes wrong if you insert before you query?
3. In T5, what does `cnt += r - l + 1` count, exactly?
4. Why does `exactly(K) = atMost(K) − atMost(K−1)` hold? What property of the window cost must be true?
5. When does the shrinking-window template (T4/T5) break, and which template do you switch to?
6. What's the overflow risk in T2 at n = 10^5, |a[i]| ≤ 10^9?

---

## 2. Infra brief: the 5 things you'd say, plus failure modes

**Cold first.** Answer each prompt aloud in about 30 seconds, then compare with the key.

1. What does load average actually count, and how do you read it against CPU?
2. Memory runs out. What does the kernel do, and how does it pick a victim?
3. File, inode, directory entry, open file descriptor: how do they relate, and why does it matter in an outage?
4. Walk a process from `fork` to reaped. Where do signals and `SIGCHLD` fit?
5. Namespaces vs cgroups: what each one does, and what happens when a cgroup limit is hit?

**Failure modes: name the cause and your first check for each symptom.**

| # | Symptom |
| --- | --- |
| F1 | `No space left on device`, `df` 100%, `du` shows a fraction |
| F2 | `No space left on device`, `df -h` shows 40% free |
| F3 | Load 30 on 8 cores, CPU 90% idle |
| F4 | Process vanishes; exit code 137; nothing in app logs |
| F5 | `fork: Resource temporarily unavailable`; `ps` full of `<defunct>` |
| F6 | `docker stop` takes exactly 10 s every time |
| F7 | p99 latency spikes every few seconds; average CPU 30% of the limit |
| F8 | `accept: Too many open files` under load |

---

## 3. Hands-on lab (Tuesday, ~50 min)

**Step 0: you need a Linux box.** This Mac has no Docker or VM tooling installed, and `strace`, `vmstat`, cgroups and `/proc` are Linux-only. Use a throwaway VM, not your laptop:
```bash
brew install --cask multipass
multipass launch 24.04 --name lab --cpus 2 --memory 2G --disk 10G
multipass shell lab
sudo apt-get update && sudo apt-get install -y sysstat strace lsof stress-ng psmisc
```
(A small cloud VM works too.) Run everything below inside the VM. **For each step: predict the output, run it, then check the key (L1–L10).**

**L1. Baseline**
```bash
nproc; uptime; free -m; vmstat 1 5
```
Predict: which `free` column tells you real headroom? What should vmstat's `r` and `b` columns be on an idle box?

**L2. CPU saturation: load from runnable tasks**
```bash
stress-ng --cpu 2 --timeout 90s &
sleep 30; uptime; vmstat 1 5; top -b -n1 | head -15
```
Predict: `r`, `us`, `id` and the 1-min load after 30 s and after 90 s.

**L3. I/O saturation: load with idle CPU (this is Drill 2's mechanism)**
```bash
stress-ng --hdd 4 --hdd-opts dsync --timeout 90s &
sleep 15
vmstat 1 5
iostat -xz 1 3
ps -eo state,pid,comm | awk '$1=="D"'
cat /proc/pressure/io
uptime
```
Predict: which vmstat column climbs? What do `%util` and `w_await` look like? What state are the workers in?

**L4. strace on a live process**
```bash
python3 -c 'import time
while True:
    open("/etc/hostname").read(); time.sleep(0.5)' &
P=$!
sudo strace -p $P -e trace=openat,read -f 2>&1 | head -6
sudo strace -c -p $P & sleep 5; sudo kill -INT $!
```
Predict: the exact `openat` line, and which syscall dominates the `-c` summary.

**L5. lsof and /proc fds**
```bash
sudo lsof -p $P | tail -5
ls -l /proc/$P/fd
grep 'open files' /proc/$P/limits
kill $P
```
Predict: fds 0, 1, 2 point where? What's the soft limit?

**L6. Fill a disk and make du and df disagree (on a loop fs, so the VM's root is safe)**
```bash
fallocate -l 200M ~/disk.img && mkfs.ext4 -q ~/disk.img
sudo mkdir -p /mnt/small && sudo mount -o loop ~/disk.img /mnt/small && sudo chown $USER /mnt/small
df -h /mnt/small
dd if=/dev/zero of=/mnt/small/big.log bs=1M count=150 status=none
tail -f /mnt/small/big.log > /dev/null &  T=$!
rm /mnt/small/big.log
df -h /mnt/small; du -sh /mnt/small
sudo lsof +L1 /mnt/small
ls -l /proc/$T/fd
```
Predict: df vs du after the `rm`. What does `lsof +L1` show in the `NLINK` column? Now **free the space two ways**: (a) truncate through `/proc/$T/fd/<n>` *without* killing tail and re-check `df`; (b) `kill $T`. Which one would you use in prod, and why?

Then fill it to ENOSPC:
```bash
dd if=/dev/zero of=/mnt/small/fill bs=1M status=none; df -h /mnt/small
sudo tune2fs -l ~/disk.img | grep -i 'reserved block count'
```
Predict: the dd error message. Why is `Use%` 100% while `Used` < `Size`?

**L7. Inode exhaustion: ENOSPC with free space**
```bash
fallocate -l 50M ~/ino.img && mkfs.ext4 -q -N 256 ~/ino.img
sudo mkdir -p /mnt/ino && sudo mount -o loop ~/ino.img /mnt/ino && sudo chown $USER /mnt/ino
for i in $(seq 1 1000); do : > /mnt/ino/f$i || break; done
df -h /mnt/ino; df -i /mnt/ino
```
Predict: at roughly which `i` does it fail, and what do the two `df` calls show?

**L8. Create a zombie and reap it**
```bash
(sleep 1 & exec sleep 300) &  Z=$!
sleep 2; ps -o pid,ppid,stat,cmd --ppid $Z
sudo kill -9 $(ps -o pid= --ppid $Z)    # try to kill the zombie
ps -o pid,ppid,stat,cmd --ppid $Z
kill $Z; sleep 1; ps -eo pid,stat,cmd | awk '$2 ~ /Z/'
```
Predict: why does this one-liner make a zombie? What does `kill -9` on the zombie do? Who reaps it after you kill the parent?

**L9. Signals, and why PID 1 is special**
```bash
bash -c 'trap "echo got TERM; exit 0" TERM; while :; do sleep 1; done' &  B=$!
grep -E 'Sig(Ign|Cgt)' /proc/$B/status
kill -TERM $B; wait $B; echo "exit=$?"
sleep 300 & kill -KILL $!; wait $!; echo "exit=$?"

sudo unshare --pid --fork --mount-proc sleep 1000 &
sleep 1; P1=$(pgrep -nx sleep)
sudo nsenter -t $P1 -p -m ps -ef
sudo kill -TERM $P1; sleep 1; ps -p $P1 -o pid,stat,cmd
sudo kill -KILL $P1; sleep 1; ps -p $P1 -o pid,stat,cmd
```
Predict: both exit codes. What PID does `sleep` have inside the namespace? Does `SIGTERM` kill it? Does `SIGKILL`?

**L10. cgroups v2: memory OOM and CPU throttling**
```bash
stat -fc %T /sys/fs/cgroup; cat /sys/fs/cgroup/cgroup.subtree_control
sudo mkdir /sys/fs/cgroup/lab
echo 50M | sudo tee /sys/fs/cgroup/lab/memory.max
echo 0   | sudo tee /sys/fs/cgroup/lab/memory.swap.max
sudo bash -c 'echo $$ > /sys/fs/cgroup/lab/cgroup.procs; exec python3 -c "a = b\"x\" * (200 << 20)"'; echo "exit=$?"
cat /sys/fs/cgroup/lab/memory.events
sudo dmesg -T | grep -iE 'out of memory|killed process' | tail -2

echo "20000 100000" | sudo tee /sys/fs/cgroup/lab/cpu.max
sudo bash -c 'echo $$ > /sys/fs/cgroup/lab/cgroup.procs; exec timeout 15 sh -c "while :; do :; done"' &
sleep 5; top -b -n1 | grep ' sh$\| sh '; cat /sys/fs/cgroup/lab/cpu.stat
```
Predict: the exit code, the `memory.events` counters, the CPU% `top` shows for the busy loop, and which `cpu.stat` fields grow.

**Cleanup:** `sudo umount /mnt/small /mnt/ino; sudo rmdir /sys/fs/cgroup/lab; rm ~/disk.img ~/ino.img` (or `multipass delete --purge lab`).

**Readings that anchor this lab (Monday):** Brendan Gregg's USE method (brendangregg.com/usemethod.html) · `man 7 signal` · `man 7 cgroups` · `man 7 namespaces` (plus `man 7 pid_namespaces` for the PID 1 rule in L9).

---

## 4. Flashcards (10): fronts only, backs in the key

| # | Type | Front |
| --- | --- | --- |
| C1 | Command | A host rejects SSH. What do you run, in order, and what does each result tell you? |
| C2 | Explain | What is a zombie, why can't `kill -9` remove it, and how do you get rid of it? |
| C3 | Explain | Your app runs as PID 1 in a container. What two jobs does it now own, and what's the fix if it can't do them? |
| C4 | Explain | SIGTERM vs SIGKILL vs SIGSTOP. Which can be caught? What are exit codes 137 and 143? |
| C5 | Command | Was this process OOM-killed, and who's the next victim? |
| C6 | Command | p99 latency spikes, average CPU well under the container limit. What do you read? |
| C7 | Command | A process is stuck. How do you see what it's waiting on? |
| C8 | Command | `Too many open files`. What do you check? |
| C9 | Template | Write the skeleton for counting subarrays with exactly K (window cost monotone). |
| C10 | Template | Write the skeleton for counting subarrays whose sum is `target` (negatives allowed). |

---

## 5. Teach-back prompts (2 min each; record, listen once, redo if more than 5 stumbles)

The explain-by-Wednesday list is marked ★.

1. ★ **Load average vs CPU utilization.** What each measures, why they diverge, how you read "load 16" on an 8-core box.
2. ★ **The OOM killer's choice.** When it fires (global vs cgroup), how it scores, how you protect a process, where you see the evidence.
3. ★ **Why `du` and `df` disagree.** The mechanism, every cause you can name, the command that confirms each one.
4. ★ **What PID 1 must do.** Reaping, signals, what happens when it exits, and how containers get this wrong.
5. **Signals end to end.** From `kill -TERM` to the process exiting: dispositions, masks, handlers, exit status.
6. **cgroups vs namespaces: what a container actually is.** Then the USE method applied to one Linux box: one command per resource, for U, S and E.

---

## 6. Troubleshooting drills (symptom only; run "Can Some Students Handle Cold Fixes")

Out loud, 30 min each: **C**larify → **S**cope → **S**tabilize → **H**ypothesize (2–3, ranked) → **C**heck (one check per hypothesis, saying which result confirms it and which rules it out) → **F**ix and prevent (and name the alert you'd add). When you name a check, look up its result in the key's "interviewer reveals" table. Don't read the diagnosis until you've committed to one.

**Drill 1 (Wed): disk full but du disagrees**
> 02:10 page: `api-07` writes are failing with `No space left on device`. `df -h /var` shows `50G 50G 0 100%`. You run `sudo du -sh /var` and get `3.1G`. The service is still up but returning 500s on any request that writes. Nothing was deployed today.

**Drill 2 (Fri): high load, idle CPU**
> A customer reports that `worker-12` (8 vCPU) is "slow." SSH takes 20 s to give a prompt. `uptime` shows `load average: 41.2, 38.7, 30.1`. `top` shows `%Cpu(s): 3.1 us, 1.8 sy, 0.0 ni, 92.4 id ...`. `ls /home` returns instantly, but your `df -h` has hung and won't Ctrl-C.

---

## 7. Design prompt: URL health-check service ("Real Apps Deserve Deep Failure Tests")

> Design a service that monitors **50,000 customer URLs**. Each URL is checked every **30 s** from **3 regions**. Owners get alerted within **2 minutes** of a real outage, without false alarms. Owners can see 90 days of up/down and latency history.

45 min on paper. **Draw before you talk.** Fill all six boxes, then check the reference outline in the key.

| Step | Time | Your page must show |
| --- | --- | --- |
| **R**equirements | 5 | Functional + non-functional; your own back-of-envelope (checks/s, in-flight connections, bytes/day) |
| **A**PI | 5 | Endpoints for owners + the internal scheduler → checker contract |
| **D**ata | 5 | Config store vs results store, schemas, retention |
| (diagram) | 10 | Boxes and arrows, end to end |
| **D**eep dive | 15 | Pick one: (a) scheduling 1.7k checks/s/region with no double checks or misses, or (b) alerting fast without false positives |
| **F**ailures | 5 | At least 5, each with detection and mitigation |
| **T**radeoffs | 5 | At least 3, plus what changes at 10x (500k URLs) |

Week 1 tie-in: name **two Linux limits** that bite a checker worker at this scale.

---

## 8. Story scaffolds (your facts only; blanks stay blank)

### 8a. 90-second introduction (target 80–90 s spoken)

| Beat | Time | Fill in |
| --- | --- | --- |
| Present: who you are now | 15 s | Role/title: ______ · Company: ______ · What you own: ______ |
| Past: the arc | 40 s | Order and one-liner per company (Cisco / Scry AI / 23andMe / Sprinklr, *in your real order*): ______ |
| Proof: 2–3 numbers | 25 s | Pick from facts you've given me (attach each to the right company): 2000+ server MongoDB fleet across GCP/Azure/AWS · Airflow platform with 200K+ executions/month, 42+ environments, 13,000+ VMs · 10M+ events/day at Scry · 23andMe 40% latency and 30% throughput gains |
| Why this role | 10 s | ______ |

Check: one sentence per beat, no acronyms the interviewer has to ask about, and end on "why this role", not on your history.

### 8b. The 400-VM rolling reboot (under 2 min)

| Field | Fill in |
| --- | --- |
| Situation: why reboot, when, which company, what ran on the VMs | ______ |
| Constraint: downtime budget / SLA / window | ______ |
| My decision: batch size, ordering, health gate, abort rule | ______ |
| Tradeoff: what you gave up (speed vs blast radius, automation vs manual gate) | ______ |
| Number: duration, failed nodes, downtime, toil saved | ______ |
| Lesson: what you'd change or later automated | ______ |

Follow-ups to prepare (answer from memory, real facts only):
- How did you pick the batch size? What made a batch "healthy" before the next one went?
- Were any nodes stateful (DB primaries, leaders)? What did you do with them first? ______
- What happened when a node didn't come back? ______
- How would you build this as a service for 13,000 VMs? (This is the Week 9 fleet-orchestrator design.)

---

## 9. Template test bank (LeetCode, outside this week's scheduled set)

Use these as extra problems after the required rows, or when a template fails the Monday drill. Each first try goes on the redo schedule. The twist column is a question to answer before you code, not a hint.

**T1: prefix sums**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 303 | Range Sum Query – Immutable | E | None. This is T1 itself |
| 724 | Find Pivot Index | E | Which two prefix values do you compare at each index? |
| 304 | Range Sum Query 2D – Immutable | M | What's the 2D inclusion–exclusion formula, and why size (m+1)×(n+1)? |
| 238 | Product of Array Except Self | M | Prefix *and* suffix, in O(1) extra space |

**T2: prefix + hashmap**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 560 | Subarray Sum Equals K | M | None. This is T2 itself |
| 930 | Binary Subarrays With Sum | M | Solve it twice, with T2 and with T5. Which edge case does each handle differently? |
| 525 | Contiguous Array | M | Asks for longest, not a count: what goes in the map instead? |
| 523 | Continuous Subarray Sum | M | **Do after 974.** Length ≥ 2: how does that change the map? |
| 1590 | Make Sum Divisible by P | M | **Do after 974.** Shortest, and the target comes from the whole array |
| 1074 | Number of Submatrices That Sum to Target | H | T1 in 2D plus T2. Which dimension do you collapse? |

**T3: fixed window**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 643 | Maximum Average Subarray I | E | None. This is T3 itself |
| 1456 | Maximum Number of Vowels in a Substring of Given Length | M | The window state is a count, not a sum |
| 1423 | Maximum Points You Can Obtain from Cards | M | Taking from the ends: what's the window you *don't* take? |
| 2461 | Maximum Sum of Distinct Subarrays With Length K | M | The window also needs a validity check |

**T4: variable window (longest/shortest)**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 209 | Minimum Size Subarray Sum | M | Shortest with sum ≥ target: where does the "record" line move? |
| 1004 | Max Consecutive Ones III | M | What's the window cost? |
| 1838 | Frequency of the Most Frequent Element | M | Needs preprocessing first; what makes the cost monotone? |
| 1658 | Minimum Operations to Reduce X to Zero | M | Reframe it as a T4 window |
| 904 | Fruit Into Baskets | M | **Do after 992.** Cost is the number of distinct values |
| 862 | Shortest Subarray with Sum at Least K | H | **Drill Q5 in practice.** Negatives break T4; needs Week 2's monotonic deque. Try it now, fail fast, and note *why* T4 fails |

**T5: atMost / exactly-K counting**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 713 | Subarray Product Less Than K | M | None. This is T5's atMost with a product. Edge: k ≤ 1 |
| 2302 | Count Subarrays With Score Less Than K | H | Cost = sum × length. Is it still monotone? |
| 1358 | Number of Substrings Containing All Three Characters | M | "At least" instead of "at most": how does the count line change? |
| 2962 | Count Subarrays Where Max Element Appears at Least K Times | M | At-least counting again |
| 2537 | Count the Number of Good Subarrays | M | Cost = number of equal pairs; how does it update incrementally? |
| 3306 | Count of Substrings Containing Every Vowel and K Consonants II | M | Exactly-K, with an extra constraint on the window |
| 795 | Number of Subarrays with Bounded Maximum | M | **Hold until after Friday's check.** Too close to it |

**Suggested order:** 303 → 560 → 643 → 209 → 713 → 930 (both ways) → 1004 → 1358 → 2302 → 1074. That's one clean pass over all five templates, ending on two Hards.

---
---

# ANSWER KEY

## K1. Template drill

```cpp
#include <cassert>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
using ll = long long;

// T1. Prefix sums: pre[i] = a[0] + ... + a[i-1]; sum(l..r) = pre[r+1] - pre[l]
vector<ll> buildPrefix(const vector<int>& a) {
    vector<ll> pre(a.size() + 1, 0);
    for (size_t i = 0; i < a.size(); ++i) pre[i + 1] = pre[i] + a[i];
    return pre;
}

// T2. Prefix + hashmap: count subarrays with sum == target (works with negatives)
ll countSumEquals(const vector<int>& a, ll target) {
    unordered_map<ll, ll> seen{{0, 1}};          // empty prefix
    ll run = 0, cnt = 0;
    for (int x : a) {
        run += x;
        auto it = seen.find(run - target);        // query BEFORE insert
        if (it != seen.end()) cnt += it->second;
        ++seen[run];
    }
    return cnt;
}

// T3. Fixed-size window: max sum of any length-k window
ll maxSumFixed(const vector<int>& a, int k) {
    ll sum = 0, best = LLONG_MIN;
    for (int r = 0; r < (int)a.size(); ++r) {
        sum += a[r];
        if (r >= k) sum -= a[r - k];
        if (r >= k - 1) best = max(best, sum);
    }
    return best;
}

// T4. Variable window: longest window with sum <= s (non-negative a)
int longestAtMost(const vector<int>& a, ll s) {
    int best = 0; ll sum = 0;
    for (int l = 0, r = 0; r < (int)a.size(); ++r) {
        sum += a[r];                              // grow
        while (l <= r && sum > s) sum -= a[l++];  // shrink until valid
        best = max(best, r - l + 1);              // record
    }
    return best;
}

// T5. Count windows with cost <= k, then exactly-K = atMost(K) - atMost(K-1)
ll atMost(const vector<int>& a, ll k) {
    if (k < 0) return 0;
    ll cnt = 0, sum = 0;
    for (int l = 0, r = 0; r < (int)a.size(); ++r) {
        sum += a[r];
        while (sum > k) sum -= a[l++];
        cnt += r - l + 1;                         // subarrays ending at r
    }
    return cnt;
}
ll exactly(const vector<int>& a, ll k) { return atMost(a, k) - atMost(a, k - 1); }

int main() {
    vector<int> a{1, 0, 1, 0, 1};
    auto pre = buildPrefix(a);
    assert(pre[5] - pre[1] == 2);
    assert(countSumEquals(a, 2) == 4);
    assert(countSumEquals({1, -1, 0}, 0) == 3);
    assert(maxSumFixed({2, 1, 5, 1, 3, 2}, 3) == 9);
    assert(longestAtMost({3, 1, 2, 1, 1, 4}, 5) == 4);
    assert(exactly(a, 2) == 4);
    assert(exactly(a, 0) == countSumEquals(a, 0));
    cout << "all templates pass\n";
}
```
(This key was compiled and run with Apple clang, `-std=c++17 -Wall -Wextra`, and prints `all templates pass`.)

**Drill answers**
1. `pre[0] = 0` is the empty prefix. With size n+1, `sum(l..r) = pre[r+1] − pre[l]` works for `l = 0` with no special case.
2. `{0:1}` counts subarrays that start at index 0 (where `run == target`). Inserting before querying lets a prefix match itself, which counts empty subarrays, so `target = 0` over-counts by n.
3. It counts every subarray that *ends at r* and starts anywhere in `[l, r]`. All of those are valid, because shrinking a valid window keeps it valid.
4. Sets: {cost ≤ K} minus {cost ≤ K−1} = {cost = K}. This requires **monotone cost**: growing a window never lowers its cost, so the valid starts for each r form a contiguous range `[l, r]`. Examples: sums of non-negatives, the count of distinct values, the count of odd numbers.
5. With negative numbers (or any non-monotone cost), shrinking can make the window *worse*, so the two-pointer invariant is gone. Switch to T2 (prefix + hashmap, keyed on whatever the prefix encodes).
6. A prefix can reach 10^14, which overflows `int`. Use `long long` for `run`, the keys, and `cnt` (the count of subarrays is up to ~5·10^9, which also overflows `int`).

## K2. Infra brief: the 5 things you'd say

1. **Load average.** It's a 1/5/15-minute exponentially damped average of tasks that are **runnable (R) or in uninterruptible sleep (D)**. The D part is Linux-specific. Read it against `nproc`. Load ≈ cores with high CPU means saturated but keeping up. Load ≫ cores with high CPU means there's a run queue (vmstat `r`, PSI `cpu some`). Load ≫ cores with *idle* CPU means tasks are stuck in D, usually disk or NFS, so look at I/O. Load says how much demand there is. CPU% says how busy the cores are.
2. **OOM.** Linux overcommits: `malloc` succeeds, and pages are only backed when they're touched. If an allocation can't be satisfied after reclaim (page cache, swap), the OOM killer runs. That happens **globally**, or **per cgroup** when `memory.max` is hit. It scores each candidate by memory footprint (RSS + swap + page tables) as a share of what's allowed, adjusted by `oom_score_adj` (−1000 means never kill, +1000 means kill first). It SIGKILLs the highest `/proc/<pid>/oom_score`. The victim is the *biggest*, which isn't necessarily the *culprit*. Evidence: `dmesg`/`journalctl -k` show "Killed process …", the cgroup's `memory.events` shows `oom_kill`, and the exit code is 137.
3. **Files.** A directory entry is a *name* pointing to an inode. The inode holds the metadata and block map. An open fd is a reference from a process to the open file. Data is freed only when **link count = 0 AND no open fds**. So `rm` on a file a process still holds removes the name but not the space, and `du` (which walks names) can't see it while `df` (which asks the filesystem) can. Inodes are a separate finite pool, so you can run out with free blocks.
4. **Process lifecycle.** `fork` clones the process, `exec` replaces its image, and `exit` turns it into a **zombie**: just a PID slot plus an exit status. The parent gets `SIGCHLD` and must call `wait()` to reap it. If the parent dies first, the orphan is re-parented to PID 1 (or a subreaper), which reaps it. Signals are async notifications. Each has a disposition (default, ignore, or handler) and can be blocked by a mask. SIGKILL and SIGSTOP can't be caught, blocked or ignored. A process killed by signal N reports exit code 128+N.
5. **Namespaces vs cgroups.** Namespaces control **what a process can see**: pid, net, mnt, uts, ipc, user, cgroup, time. cgroups control **how much it can use**. cgroup v2 is a single hierarchy at `/sys/fs/cgroup` with controllers `cpu` (`cpu.max` quota/period, where going over means *throttling*, not killing), `memory` (`memory.high` throttles and reclaims, `memory.max` triggers the OOM kill), `io` (`io.max`) and `pids` (`pids.max`, which stops fork bombs). A container is just a process with its own namespaces, a cgroup, and a root filesystem.

**Failure modes**

| # | Cause | First check | Fix |
| --- | --- | --- | --- |
| F1 | Deleted file still held open (log rotated without a reopen) | `sudo lsof +L1` | Restart or HUP the holder, or truncate `/proc/PID/fd/N` |
| F2 | Inode exhaustion (millions of tiny files: sessions, cache, mail queue) | `df -i` | Delete the small files; for the long term, reformat with more inodes or use XFS (dynamic inodes) |
| F3 | Tasks in D state: disk saturated or failing, hung NFS | `vmstat 1` (`b`, `wa`), `ps -eo state,pid,comm \| awk '$1=="D"'` | Remove the I/O source or the hung mount |
| F4 | OOM kill (global or cgroup), 128+9 | `dmesg -T \| grep -i 'killed process'`, `memory.events` | Raise the limit, or fix the leak or the peak |
| F5 | Parent not reaping, so PIDs run out (`pid_max` or `pids.max`) | `ps -eo pid,ppid,stat,cmd \| awk '$3~/Z/'`, then look at the PPID | Fix or restart the parent; use an init (tini) in containers |
| F6 | PID 1 doesn't handle SIGTERM (shell-form CMD, or no handler) → SIGKILL after the grace period | `docker inspect` CMD/Entrypoint; check SigCgt in `/proc/1/status` | Exec form, `exec` in scripts, `--init`/tini |
| F7 | CFS quota throttling: bursts use up the quota early in each 100 ms period | `cpu.stat` `nr_throttled`, `throttled_usec` | Raise or remove the CPU limit, tune the thread pool to the quota |
| F8 | fd limit (EMFILE); every socket is an fd | `ls /proc/PID/fd \| wc -l` vs `grep 'open files' /proc/PID/limits` | `LimitNOFILE=` in systemd, `ulimit -n`; fix any fd leak |

## K3. Lab: expected output and what each step proves
*(Your numbers will differ. Check the shape, not the digits.)*

- **L1.** `nproc` → `2`. Load ≈ `0.0x`. In `free -m`, the **`available`** column is the real headroom (`free` is misleading because page cache is reclaimable). vmstat `r` 0–1, `b` 0, `id` ~99. *Proves:* you know the baseline.
- **L2.** vmstat `r` ≈ 2, `us` ≈ 100, `id` ≈ 0, `wa` 0. Load climbs toward **2.0** (about 1.2–1.5 at 30 s, near 2 by 90 s, because it's a damped average). *Proves:* runnable tasks = load; load ≈ cores means saturated but no queue.
- **L3.** vmstat **`b`** ≥ 1–4, `wa` high, `us` low. iostat: the device's `%util` near 100, `w_await` in the tens to hundreds of ms, `aqu-sz` > 1. `ps` shows `D stress-ng-hdd` lines (some samples catch them in R). `/proc/pressure/io` `some avg10=` well above 0. Load rises above 2 while the CPU is mostly idle or iowait. *Proves:* D-state tasks raise load without using CPU, which is Drill 2.
- **L4.** `openat(AT_FDCWD, "/etc/hostname", O_RDONLY|O_CLOEXEC) = 3` then `read(3, "lab\n", ...) = 4`. The `-c` table is dominated by `clock_nanosleep` (or `select`/`pselect6`, depending on the Python version) in calls/time, plus `openat`, `read`, `close`, `fstat`/`newfstatat`. *Proves:* you can see what a live process is doing without touching its code. Note the `sudo`: Ubuntu's Yama `ptrace_scope=1` blocks attaching to a non-child.
- **L5.** fds 0/1/2 → `/dev/pts/N` (your terminal); the soft limit is usually `1024` (hard `1048576` or `524288`). *Proves:* every open thing is an fd, and the limits are per process.
- **L6.** First `df` ≈ 2% used. After the `rm`: **df still shows ~150M used, du shows ~20K.** `lsof +L1` shows `tail … /mnt/small/big.log (deleted)` with **NLINK 0**. `ls -l /proc/$T/fd` shows `3 -> /mnt/small/big.log (deleted)` (the fd number may vary). (a) `: > /proc/$T/fd/3` brings df back down immediately while tail keeps running. (b) `kill $T` frees it too. **In prod, truncate first** when the holder is the critical service (no restart, no outage). Then fix the root cause (logrotate `postrotate` HUP or `copytruncate`). Fill: `dd: error writing '/mnt/small/fill': No space left on device`. `Use%` shows 100% while `Used` < `Size` because of the **reserved blocks** (5% by default, ~10k 1K-blocks here): `Avail` hits 0 for non-root users, and only root can write into the reserve. *Proves:* the mechanisms behind du/df, ENOSPC and reserved blocks, by hand.
- **L7.** It fails around **i ≈ 245** (256 inodes minus ~11 reserved/used by ext4): `: /mnt/ino/fNNN: No space left on device`. `df -h` shows lots free; `df -i` shows **`IUse% 100%`**. *Proves:* ENOSPC can be an inode problem. `df -i` is always your second command.
- **L8.** The subshell forks `sleep 1`, then **`exec`s into `sleep 300`**. The child is still its child, but `sleep` never calls `wait()`. Output: `… Z … [sleep] <defunct>` with PPID = `$Z`. `kill -9` on the zombie does **nothing**: it's already dead, and only its parent's `wait` clears it. After `kill $Z`, the zombie is re-parented to PID 1 (systemd), which reaps it, and the `awk` prints nothing. *Proves:* you fix zombies through the parent, never the zombie.
- **L9.** `SigCgt` has bit 15 (SIGTERM) set after `trap`. Output `got TERM` and `exit=0` (the handler ran and chose its own exit code). The second one prints `exit=137` (128+9). Inside the namespace, `ps -ef` shows **`sleep` as PID 1**. `SIGTERM` **does not kill it**, and `ps` still lists it. `SIGKILL` kills it. *Proves:* the kernel drops signals sent to a namespace's init unless init installed a handler; only SIGKILL/SIGSTOP from an ancestor namespace get through (`pid_namespaces(7)`). That's why a container whose PID 1 doesn't handle SIGTERM takes the full grace period and then gets SIGKILLed.
- **L10.** `cgroup2fs`; `subtree_control` lists `cpu … memory pids` (if `cpu` or `memory` is missing: `echo "+cpu +memory" | sudo tee /sys/fs/cgroup/cgroup.subtree_control`). The python run prints `Killed` and `exit=137`. `memory.events` shows `max N` and **`oom 1`, `oom_kill 1`**. dmesg shows `Memory cgroup out of memory: Killed process NNNN (python3) …`. CPU: the busy loop sits at **~20%** in `top`, and `cpu.stat` `nr_throttled` and `throttled_usec` grow. *Proves:* `memory.max` kills and `cpu.max` throttles, so F4 and F7 both come from cgroup limits and only one of them is visible as a crash.

## K4. Flashcard backs

- **C1. SSH rejected.** From the client: `ssh -vvv user@host`, and see where it stops. **Connection refused** means nothing is listening, or a firewall REJECT. **Timeout** means the network, a security group, or a firewall DROP. **Permission denied (publickey)** means an auth problem. `nc -vz host 22` isolates the TCP layer. On the host (console/serial): `systemctl status ssh` (sshd on RHEL), `ss -tlnp | grep :22`, `journalctl -u ssh -n 50` or `/var/log/auth.log` (`/var/log/secure` on RHEL), `sshd -t` (config syntax), `~/.ssh` 700 and `authorized_keys` 600 owned by the user (StrictModes), `df -h /` (a full disk breaks logins), fail2ban/iptables, `MaxStartups`.
- **C2. Zombie.** A process that exited but whose parent hasn't called `wait()`. It's only a PID entry plus an exit status, with no memory or CPU. It's already dead, so signals do nothing. Make the parent reap it (a SIGCHLD handler or `wait`), or kill/restart the parent so PID 1 adopts and reaps it. The real risk is PID exhaustion. Find them with `ps -eo pid,ppid,stat,cmd | awk '$3~/Z/'`.
- **C3. PID 1.** (1) **Reap** orphaned zombies re-parented to it. (2) **Handle signals**: the kernel applies no default action to unhandled signals sent to PID 1, so SIGTERM is ignored unless there's a handler, and PID 1 must forward signals to its children. When PID 1 exits, every process in the namespace is SIGKILLed. Fix: `docker run --init` / tini / dumb-init, exec-form `ENTRYPOINT`, `exec "$@"` in wrapper scripts.
- **C4.** SIGTERM (15) is a polite request: it can be caught, so you get a graceful shutdown. SIGKILL (9) can't be caught or ignored, so death is immediate with no cleanup. SIGSTOP can't be caught and pauses the process (SIGCONT resumes it). Exit codes are 128 + signal: **137 = SIGKILL** (often OOM), **143 = SIGTERM**.
- **C5.** `dmesg -T | grep -iE 'out of memory|killed process'` or `journalctl -k --since -1h | grep -i oom`; the cgroup's `memory.events` (`oom_kill`). Next victim: the highest `cat /proc/*/oom_score`; protect a process with `oom_score_adj` (−1000 = never) or `OOMScoreAdjust=` in systemd.
- **C6.** `cat /sys/fs/cgroup/<path>/cpu.stat` → `nr_periods`, `nr_throttled`, `throttled_usec` growing; `cat cpu.max` (quota per 100 ms period). Average CPU hides bursts that use up the quota early in each period.
- **C7.** `ps -o pid,stat,wchan:32,cmd -p PID` (state, plus the kernel function it's sleeping in); `sudo cat /proc/PID/stack`; `sudo strace -fp PID` (which syscall it's blocked in); `sudo lsof -p PID` (which file or socket). D state → I/O/NFS; S in `futex` → lock; S in `recvfrom`/`epoll_wait` → waiting on the network.
- **C8.** `ls /proc/PID/fd | wc -l` vs `grep 'open files' /proc/PID/limits`; `lsof -p PID | awk '{print $5}' | sort | uniq -c` (what kind of fd is leaking); system-wide `cat /proc/sys/fs/file-nr`. Fix: `LimitNOFILE=` (systemd), `ulimit -n`, fix the leak (sockets not closed, CLOSE_WAIT piling up).
- **C9.** `atMost(k)`: `if k<0 return 0; for r: add a[r]; while cost>k: remove a[l++]; cnt += r-l+1`. Then `exactly(K) = atMost(K) - atMost(K-1)`. (Full code in K1, T5.)
- **C10.** `map{{0,1}}; run=0; for x: run+=x; cnt += map[run-target] (query first); ++map[run]`. (Full code in K1, T2.)

## K5. Teach-back must-hit checklist

1. **Load vs CPU:** R+D tasks; damped 1/5/15 averages; compare against `nproc`; CPU% = busy time; the three divergence cases (K2 #1); vmstat `r` vs `b`; PSI (`/proc/pressure/*`) as the modern saturation metric.
2. **OOM:** overcommit, and the kill happens at page-touch time; global vs cgroup (`memory.max`); the scoring (footprint share + `oom_score_adj`); the biggest isn't necessarily the culprit; SIGKILL → 137; `memory.oom.group` kills the whole cgroup; evidence in dmesg and `memory.events`; Kubernetes "OOMKilled" is the cgroup case (Week 4 link).
3. **du vs df:** df = filesystem allocation (statfs); du = walk the names. Causes: deleted-but-open (`lsof +L1`); files hidden under a mount point (bind-mount `/` to `/mnt/root` and `du` there); reserved blocks (`tune2fs -l`); journal/metadata; `du -x` vs crossing mounts; snapshots/CoW. Separately: inodes (`df -i`). Fix the deleted-open case without a restart: truncate through `/proc/PID/fd/N`.
4. **PID 1:** reap orphans; no default signal actions, so it needs handlers and must forward signals; its death kills the namespace; shell-form CMD makes `/bin/sh` PID 1, and sh doesn't forward signals; fixes: tini/`--init`, exec form, `exec` in scripts; subreapers (`PR_SET_CHILD_SUBREAPER`).
5. **Signals:** generated → pending → delivered when unblocked; disposition default/ignore/handler; SIGKILL/SIGSTOP are special; handlers must be async-signal-safe (set a flag, act in the main loop); SIGCHLD, SIGHUP (reload), SIGPIPE (servers ignore it); `kill -0 PID` tests whether a process exists; exit 128+N.
6. **cgroups/namespaces + USE:** see what you can (namespaces) vs use how much (cgroups); a container = namespaces + cgroup + rootfs. USE per resource: **CPU** U=`mpstat`/vmstat `us+sy`, S=vmstat `r` > nproc / PSI cpu, E=rare. **Memory** U=`free` available, S=vmstat `si/so`, PSI memory, E=OOM in dmesg. **Disk** U=`iostat -x` %util, S=`aqu-sz`/`await`, E=dmesg I/O errors, `smartctl`. **Network** U=`sar -n DEV`, S=`nstat`/`netstat -s` retransmits and drops, E=`ip -s link` errors. Also software resources: fds, PIDs, conntrack.

## K6. Troubleshooting diagnoses

### Drill 1: disk full but du disagrees

**Interviewer reveals (what each check would show):**

| You run | You see |
| --- | --- |
| `df -i /var` | `IUse% 3%` (inodes are fine) |
| `sudo lsof +L1 /var` | `java 2231 app 41w REG … 47.2G 0 … /var/log/app/app.log.1 (deleted)` |
| `ls -l /var/log/app/` | a fresh `app.log` at 12K, last modified 00:00 |
| `cat /etc/logrotate.d/app` | `daily`, `rotate 7`, `compress`, **no `postrotate` and no `copytruncate`** |
| `mount \| grep /var` | a single filesystem, nothing mounted on top of subdirectories |
| `sudo tune2fs -l <dev> \| grep Reserved` | 5% (explains ~2.5G, not 47G) |

**Diagnosis:** at midnight, logrotate renamed `app.log` → `app.log.1`, then deleted `app.log.1` (compress + rotate). The JVM still holds fd 41 open to the old inode and keeps appending to it. That inode has 0 links, so `du` can't see it, but its blocks are still allocated, so `df` shows them as used.
- **Clarify:** what's failing (writes), since when (~2am, growing since midnight?), what changed (no deploy, but the rotation at 00:00).
- **Scope:** one host or the fleet? Every host on the same logrotate config will hit this at a different time, depending on traffic.
- **Stabilize:** pull `api-07` from the LB if 500s are user-visible. Free space *without* a restart: `sudo truncate -s 0 /proc/2231/fd/41` (or `: >`). df drops right away. Deleting more files would gain nothing, because the space isn't in a named file.
- **Hypotheses (ranked):** (1) a deleted-but-open file → `lsof +L1`; (2) data hidden under a mount point → `mount`, bind-mount check; (3) reserved blocks or metadata → `tune2fs` (explains a few %, not 47G); (rule out) inodes → `df -i`.
- **Fix:** `copytruncate`, or a `postrotate` that signals the app to reopen its logs (and confirm the app actually reopens on that signal). Restart the JVM in the next window to drop the fd cleanly.
- **Prevent and alert:** disk-usage alerts on % *and* rate of growth (predict time-to-full); an alert when the gap between `df` and `du` is large, or a periodic `lsof +L1` check for open files with deleted names over 1G; logs on a separate volume so `/var` filling doesn't take down writes; ship logs off-host instead of keeping them locally.

### Drill 2: high load, idle CPU

**Interviewer reveals:**

| You run | You see |
| --- | --- |
| `vmstat 1 5` | `r` 0–1, **`b` 38–41**, `wa` 0–2 (!), `id` 92 |
| `ps -eo state,pid,ppid,wchan:32,cmd \| awk '$1=="D"'` | ~40 lines: `df`, `ls /mnt/shared`, cron `backup.sh`, `node_exporter`, all with wchan `nfs_…`/`rpc_wait_bit_killable` |
| `mount \| grep nfs` | `filer-02:/export/shared on /mnt/shared type nfs4 (rw,hard,…)` |
| `dmesg -T \| tail` | `nfs: server filer-02 not responding, still trying` and `INFO: task df:31877 blocked for more than 120 seconds` |
| `iostat -xz 1 3` | local disks idle (`%util` < 5) |
| `ping filer-02` / `rpcinfo -p filer-02` | ping OK; rpcinfo hangs (NFS service down, host alive) |

**Diagnosis:** the NFS server `filer-02` stopped answering. The mount is `hard`, so every process that touches `/mnt/shared` blocks in uninterruptible sleep (D) until the server comes back. Each one adds 1 to the load average. The CPU stays idle. `wa` is low because tasks blocked on NFS RPCs usually aren't counted as block-device iowait. That's the trap: "low iowait" doesn't rule out an I/O problem. `df` hung because it calls `statfs` on every mount, NFS included. Ctrl-C doesn't work because D-state ignores signals (`hard` without `intr`; newer kernels let SIGKILL through for NFS waits, marked `_killable`).
- **Clarify:** what "slow" means and since when; any change to the filer or the network.
- **Scope:** every client of `filer-02`? (Check one other host: `timeout 5 stat /mnt/shared`.)
- **Stabilize:** fail over or restart the NFS service on the filer, or redirect clients to a replica. On the clients, stop the cron jobs that keep piling up blocked processes. `umount -f -l /mnt/shared` detaches the mount so new callers stop blocking; the processes already stuck stay stuck until the server returns, or until a SIGKILL if the wait is killable.
- **Hypotheses (ranked):** (1) a hung network filesystem → D tasks with an `nfs` wchan, dmesg "not responding"; (2) a saturated or failing local disk → `iostat` `%util`/`await`, dmesg I/O errors (ruled out: disks idle); (3) kernel lock contention, or a runaway number of threads in D (e.g., a memory reclaim storm) → `/proc/PID/stack`, PSI memory.
- **Fix:** restore the filer. Reconsider the mount options (`soft,timeo=` for non-critical data, accepting EIO risk; or `hard` but keep NFS paths away from health checks, monitoring agents and cron).
- **Prevent and alert:** alert on vmstat `b`/procs_blocked and PSI io, not just CPU; a synthetic `timeout 5 stat` probe per NFS mount; exporters (`node_exporter` here) shouldn't stat NFS mounts (its filesystem collector can exclude mount points); dmesg hung-task alerting.
- **Other branch, if they say "no NFS":** the same symptoms with `iostat` showing `sdb` at `%util 100`, `await 900ms` and dmesg `I/O error, dev sdb, sector …` means a failing disk. Stabilize: drain the host and fail the disk out of RAID; check `smartctl -a /dev/sdb`.

## K7. Design reference outline: URL health-check service

**Requirements**
- Functional: register a URL plus its check config (method, expected status/body, interval, timeout); check from multiple regions; alert owners (email/Slack/PagerDuty) on down and on recovery; 90-day history and a status page.
- Non-functional: detection within 2 min; **few false positives** (that's the product); checks keep running when any one region or component fails; config writes are rare, results writes are constant.
- Back-of-envelope: 50k URLs / 30 s ≈ **1.7k checks/s per region**, ×3 regions ≈ **5k checks/s**. In flight (Little's law): 1.7k/s × (0.3 s typical … 10 s timeout) ≈ 500 typical, **up to 17k** concurrent per region in a bad minute, so use async I/O (epoll), not thread-per-check. Results: ~100 B × 5k/s ≈ **0.5 MB/s ≈ 43 GB/day raw**, so keep raw data 7 days and 1-min rollups 90 days (≈ 50k × 3 × 1440 × 90 ≈ 19B rows → compress, or roll up further to 5-min after 14 days).

**API**
- Owners: `POST /checks {url, interval, timeout, expect, regions, notify}`, `GET /checks/{id}/status`, `GET /checks/{id}/history?from&to&res=1m`, `PUT/DELETE /checks/{id}`.
- Internal: scheduler → checker: `CheckTask{check_id, url, timeout, expect, deadline}`. Checker → results: `Result{check_id, region, ts, ok, status, latency_ms, error_class(dns|connect|tls|timeout|status|body)}`.

**Data**
- Config: Postgres (`checks`, `owners`, `notify_channels`), small and relational, with a cache in each region.
- Results: a time-series store (or Cassandra keyed by `(check_id, day)`, clustered by ts), behind a Kafka topic so a slow DB never blocks the checkers.
- State: `check_state{check_id → per-region last N results, current status, alert_id}` in Redis or the alerting service's memory, rebuilt from Kafka.

**Diagram:** owners → API → Postgres → (CDC/poll) → **schedulers** (partitioned) → per-region queue → **checker pool** (async workers) → Kafka `results` → (a) TSDB writer, (b) **evaluator** (state machine plus cross-region quorum) → alert dedup/routing → notifiers. Plus a status page reading the TSDB and state.

**Deep dive (a): scheduling.** Split check IDs into ~1024 partitions. Each scheduler instance holds **leases** on a set of partitions (etcd/ZooKeeper or a DB row with a TTL), so a crash means the lease expires and another instance takes over within one interval. No double checks thanks to lease ownership and fencing tokens (Week 7 link). Within a partition, use a **timing wheel** or a min-heap by `next_run`, and add **jitter** (`next = now + interval ± hash(check_id) % interval`) so 50k checks don't all fire at :00. Skip a check if the previous one for that ID is still in flight (no pile-up on slow targets).

**Deep dive (b): alerting without false positives.** Mark a URL DOWN only when **≥ 2 of 3 regions** see **N = 2 consecutive** failures, and recover after 2 consecutive passes (hysteresis). Detection ≈ 2 intervals + evaluation ≈ 60–75 s, under the 2-min SLO. Distrust your own checkers: canary URLs (your own known-good endpoints) in each region, and if a region's canaries fail, that region's votes are discarded. Group alerts: when > X% of all URLs go down at once, it's probably you or a shared provider (CDN/DNS), so send one incident, not 10k pages.

**Failures (detection → mitigation)**
1. A checker region is partitioned or degraded, so everything "fails" from there → canaries; drop that region's votes.
2. A scheduler crashes → lease expiry and reassignment; alert on a "checks executed/s" drop per partition.
3. Kafka or the TSDB is slow → checkers keep running (they write to Kafka; Kafka buffers); the evaluator reads from Kafka, not the DB.
4. DNS resolver flakiness looks like an outage → separate local resolver caches per region, classify `error_class=dns` separately, and confirm with a second resolver.
5. Thundering herd at interval boundaries → jitter.
6. A shared-provider outage causes an alert storm → grouping, dedup, rate-limited notifications.
7. Target rate-limits or blocks us → a stable published source IP list, a custom User-Agent, back off on 429.
8. A notifier is down (Slack API) → retry queue plus fallback channel; at-least-once delivery with an idempotency key on `alert_id`.

**Tradeoffs**
- Check frequency vs cost and target load (30 s vs 60 s halves the fleet).
- Quorum + N consecutive = fewer false alarms but slower detection.
- Kafka in the middle = durability and decoupling, but more to operate.
- Per-region evaluation (faster) vs central evaluation (simpler, single brain).
- **10x (500k URLs, ~17k checks/s per region):** more partitions and checker nodes; connection reuse per host (many URLs share hosts); move raw results to cheaper storage sooner; evaluate in stream processors partitioned by `check_id`.

**Week 1 tie-in: Linux limits on a checker worker:** **fds** (each in-flight check is a socket: 17k concurrent > a default `ulimit -n` of 1024, so set `LimitNOFILE`); **ephemeral ports/TIME_WAIT** (`net.ipv4.ip_local_port_range`; many connections to the same `ip:port` can exhaust the 4-tuple; Week 2 link); **memory cgroup limit** (TLS buffers × 17k connections → OOMKilled → exit 137); **conntrack table** full on NAT'd hosts (`nf_conntrack: table full, dropping packet`).

## K8. Story rubric (no answers; your facts only)

- Intro: under 90 s; present → past → proof → why. Every number attached to the right company. Ends on "why this role".
- 400-VM reboot: under 2 min; one clear decision *you* made; one tradeoff said out loud; at least one number; the lesson is concrete. The follow-ups in §8b are the likely interviewer probes. If a blank stays blank, it stays out of the story.
