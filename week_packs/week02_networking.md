# WEEK PACK — Week 2 (Oct 19–25): Networking

Infra layer: TCP, DNS, TLS, load balancers · Code: monotonic stack + monotonic deque, binary search on the answer · Design: distributed rate limiter · Gates ahead: **Oct 31** (Gate 1 includes the 8-minute "URL to response" explain and the rate limiter in 45 min), Nov 21, Dec 12, Dec 19

**Rule for this file:** do every section cold first. All answers are in the **ANSWER KEY** at the bottom. Don't scroll down until you've attempted the section. There are no solutions to this week's LeetCode problems anywhere in this file. Those go through the hint ladder only.

---

## 0. This week's plan

### 0a. Reviews first: the Week 1 backlog

All 8 Week 1 problems (1, 49, 3, 11 · 974, 1248, 992, 933) were first solved Oct 8–9, and none has been redone since. So all 8 are still at **Review 1**, overdue since Oct 9–10.

- **Missed reviews don't stack.** Each problem gets **one** redo now, and it counts as Review 1. If it's Clean, Review 2 comes 3 days after *that redo*, and Review 3 comes 7 days after that. Doing the 1-, 3- and 7-day reviews back to back would just be three redos in one sitting, with no spacing. The longer gap actually makes this first redo a harder test.
- **The cap blocks Monday's Learn row.** 8 due > 5, so Monday has **no new problem**. Your loop says "Monday reading + one Learn row", but the master rule wins. The Learn row (84) moves to Tuesday.
- **The 4 / 3 / 1 split** (Mon / Tue / Wed) is the only split that keeps every later morning at ≤ 5 due, so Thursday's two problems and Friday's check aren't blocked. The count is in 0c.
- **Order:** shaky-by-history first (3 had 23 submits, 1 had 11, 11 had 7, 49 had 5), then the required rows.
- **Week 1 loose ends:** tracker row 1 is blank and I have no result for **2444**. If you didn't pass 2444, the plan says to redo the Week 1 Learn rows (560, 1248) before Tuesday's 84, then retry 2444. Tell me which.

### 0b. This week's problems

| # | Problem | Diff | Role | Your history (LeetCode, Oct 6) | How it's run |
| --- | --- | --- | --- | --- | --- |
| 20 | Valid Parentheses | E | Core | Solved Apr 2026, **15 submits** (shaky) | Cold redo, ≤ 25 min (aim for 10) |
| 739 | Daily Temperatures | M | Core | Solved Aug 2026, 2 submits | Cold redo, ≤ 25 min |
| **33** | **Search in Rotated Sorted Array** | M | Core | **⚑ Never solved** | First try, 35 min alone |
| 146 | LRU Cache | M | Core | Solved Sep 2026, **14 submits** (shaky) | Cold redo, ≤ 25 min |
| 84 | Largest Rectangle in Histogram | H | Required · **Learn** | New | Learn row: 40 min alone before any hint, 50 total |
| 1438 | Longest Continuous Subarray With Absolute Diff ≤ Limit | M | Required · Apply | New | First try, 35 min |
| 410 | Split Array Largest Sum | H | Required · Apply | New | First try, inside Saturday's mock |
| 71 | Simplify Path | M | Required · practical | Solved Mar 2026, 4 submits (shaky: last seen before May) | Cold redo, ≤ 25 min |
| 2398 | (Friday check: don't open it before Friday) | H | Check | Untouched | 45 min, alone, Friday |

**Old solves** (20, 739, 146, 71) get a cold redo as their first attempt this week, marked **Clean / Shaky / Failed**, and that result starts their spacing. **Never solved** (33, 84, 1438, 410) get normal first tries, marked **Solved alone / Needed the solution**. The coding page's other Learn rows (907, 239, 875) are old solves, so they're in §9 as extras. If the page shows them as due, tell me and I'll recount the cap.

### 0c. Day by day

| Day | Reviews first (blank editor, ≤ 25 min each) | Infra / apply | Code: new | Other |
| --- | --- | --- | --- | --- |
| **Mon Oct 19** | **3, 1, 11, 49** (W1, Review 1) | **Recall first:** answer §2 and the three ★ prompts in §5 aloud, cold. *Then* read (list below), only for what you missed (45) | §1 template drill (15). **No new problem: 8 due** | Recall warm-up (10) |
| **Tue Oct 20** | **992, 974, 1248** (W1, Review 1) | §3 lab: dig +trace, curl -v, ss, tcpdump (50) | **84**: Learn row | Recall warm-up (10) |
| **Wed Oct 21** | **933** (W1, Review 1) · **84** (Review 1) | ★ Explain-aloud list, **no notes, recorded** (25) · Drill 1 aloud (30; the plan's Wednesday slot) | **33 ⚑**: never solved | — |
| **Thu Oct 22** | **3, 1, 11, 49** (Review 2, with a twist) · **33** (Review 1) | Story practice §8 (20) | **1438** (Learn: first deque problem) + **71** (mixed: practical, cold redo) | — |
| **Fri Oct 23** | **992, 974, 1248** (Review 2) · **1438, 71** (Review 1) | Design §7: **your drawing first** (45), then read K7 and mark gaps · Drill 2 aloud (30) | **2398** check, 45 min, alone | — |
| **Sat Oct 24** | **933, 84** (Review 2) · **2398** (Review 1) | Design redrawn from memory (90) · cheat-sheet writing · **90-min debrief** | **75-min mock** (0e) | — |
| **Sun Oct 25** | **33** (Review 2) · **410** (Review 1) | Cheat sheet rewritten from memory (30) · tracker row · plan Week 3 | Extras (≤ 60): **146, 20, 739** (cold redos) | — |

**Reviews due each morning, if every redo is Clean:** Mon 8 · Tue 4 · Wed 2 · Thu 5 · Fri 5 · Sat 3 · Sun 2 · next Mon (Oct 26) 5. Thursday and Friday sit exactly at the cap.

**Shaky** brings a problem back 2 days later at the same stage, and **Failed** brings it back the next day. Either one can push a morning over 5, so **tell me each result and I'll recount before you start.** If a morning is over 5, that day's new problem slides and the reviews take its slot.

**Monday reading (only after the cold recall):**
- Julia Evans' zines: *How DNS Works!* and *Bite Size Networking!* (wizardzines.com). If you don't own them, the free ones are *Networking! ACK!* and *Let's learn tcpdump!*. Optional hands-on: messwithdns.net.
- TLS: *The Illustrated TLS 1.3 Connection* (tls13.xargs.org). Read the handshake records only (ClientHello through client Finished).

### 0d. If you're starting today (the pack landed Tue Oct 20, 01:00)

If none of Monday's column happened, use this instead. It keeps the cap, Friday's check and Saturday's mock.

| Day | Reviews first | Rest of the day |
| --- | --- | --- |
| Tue Oct 20 | 3, 1, 11, 49 | Monday's column: recall-first reading, template drill. No new problem (8 due) |
| Wed Oct 21 | 992, 974, 1248 | Lab · **84** (Learn row) |
| Thu Oct 22 | 933 · 84 (R1) | **33 ⚑** · Explain-aloud (recorded) · Drill 1 · story practice |
| Fri Oct 23 | 3, 1, 11, 49 (R2) · 33 (R1) = 5 | **2398** check · design drawing + compare · Drill 2 |
| Sat Oct 24 | 992, 974, 1248 (R2) · 2398 (R1) | Mock: P1 timed redo (84 or 33), P2 **410** · redraw · sheet · debrief |
| Sun Oct 25 | 933, 84 (R2) · 410 (R1) | Cheat sheet from memory · extras: **1438 + 71** · tracker |
| Mon Oct 26 | (Week 3 starts) | **146, 20, 739** carry over as Week 3 Monday's code block, before any Week 3 new problem |

### 0e. Problem-session rules

- Say **"start 84"** (or any number) and I'll log the start time. For each problem: the 60-second approach aloud, brute force first, and the complexity before the code ("Real Engineers Always Build Code Tests Often").
- **Hints:** for first tries, one rung per request, and only after 25 min stuck. The rungs go pattern name → data structure → key insight → skeleton. A **Learn row (84) gets the full 40 minutes before any hint.** I never write or rewrite your code, and if you ask for the solution I'll offer the next rung instead.
- **Cold redos and reviews:** blank editor, no notes, ≤ 25 min. Review 2 adds a twist: change one constraint and say what breaks. Review 3 is recorded, with two edge cases traced.
- **Marks:** **Clean** means first submit, < 25 min, no hint. **Shaky** means slow, 2+ submits, or one hint. **Failed** means not finished or needed the solution. After two Fails on the same problem, solve one more problem with the same pattern before you retry it.
- **Compiling:** I'll run `g++ -std=c++17 -Wall -Wextra` on your file and show you compile errors. I won't show fixes.

### 0f. ⚑ LC 33 is never solved, and the final gate requires it

- **Slot:** Wed Oct 21 (Thu Oct 22 if you're starting late). The plan puts never-solved core problems on Tuesday. The review backlog pushed it one day.
- **It counts only if it's a real first try:** you say "start 33", 35 min alone, no reading about rotated arrays beforehand, hint rungs only after 25 min stuck. Keep 153, 81 and 154 closed until you've attempted it (§9).
- **Backup slots if Wednesday slips:** Thursday's first code slot, then Sunday's first extras slot. **The week does not close without it.** Either result goes on the review schedule (Review 1 the next day).

### 0g. Saturday mock and debrief

- **Mock (75 min, recorded, coding only in weeks 1–2):**
  - 5 min: your 90-second intro (Week 1 §8a).
  - **P1: a timed redo, 25 min.** I pick it at the start from 84 / 33 / 1438 / 71. If it's due that day, it counts as that review.
  - **P2: 410, first attempt, about 35 min.**
  - 5 min: your questions.
- **Scoring:** 1–4 per area, with evidence, on Approach, Working code, Fluency, Testing, Communication and Composure. **Design depth** is scored on Saturday's redraw and **Troubleshooting** on Friday's Drill 2, so all eight areas get a number this week.
- **Cheat sheet (one page):** top, the 5 things you'd say; middle, commands and failure modes; bottom, 3 interview questions and the story that fits. I'll save it as `cheat_sheets/week02_networking.md`.
- **Debrief (90 min):** I interview you on the mock and the week's stalls, and each stall becomes an error-log row (with rep dates) plus one drill. Then this week's flashcards, and the review numbers for the tracker.
- **This week runs ~17 h, not 15, because of the backlog.** If time runs short, cut in this order: §9 extras → lab step L6c → Sunday's extras (they carry to Monday). **Never cut:** reviews, 33, the check, the mock.

---

## 1. C++ template drill (target: under 15 min, compiled, asserts passing)

Use a blank file and no notes. Compile with `g++ -std=c++17 -Wall -Wextra drill.cpp && ./a.out`. Write the headers explicitly from memory (no `<bits/stdc++.h>` on Apple clang). If you can't finish in 15 min, the template goes on the review schedule like a problem.

| # | Function | Spec |
| --- | --- | --- |
| T1 | `boundaries(a)` | **One pass, one stack.** Returns `prv[i]` = index of the previous **strictly smaller** element (or −1) and `nxt[i]` = index of the next **smaller-or-equal** element (or n) |
| T2 | `windowMin(a, k)` | Minimum of every length-k window, O(n), using a deque |
| T3 | `firstTrue(lo, hi, ok)` | `ok` is F…F T…T on [lo, hi] and `ok(hi)` is true. Returns the first true |
| T4 | `lastTrue(lo, hi, ok)` + `floorSqrt(n)` | Mirror of T3: `ok` is T…T F…F and `ok(lo)` is true. Returns the last true. `floorSqrt` must use `lastTrue` and must not overflow |

Asserts your code must pass:
```
a = {3,1,2,4,2}
prv == {-1,-1,1,2,1}
nxt == {1,5,4,4,5}
windowMin({4,2,12,3,8,1,7}, 3) == {2,2,3,1,1}
windowMin(a, 1) == a
firstTrue(0, 100, x*x >= 50) == 8
firstTrue(7, 7, always true) == 7
floorSqrt(0)==0, floorSqrt(1)==1, floorSqrt(15)==3, floorSqrt(16)==4
floorSqrt(2147483647) == 46340
sum over i of (i - prv[i]) * (nxt[i] - i) == n*(n+1)/2
```

Answer these aloud after the code compiles:
1. In T1, which comparison in the pop loop (`>=` or `>`) gives "previous strictly smaller" and "next smaller-or-equal" at the same time? What happens to both arrays if you flip it?
2. What does `(i − prv[i]) × (nxt[i] − i)` count? With repeated values, why does the strict / non-strict split count every subarray exactly once? (That's what the last assert checks.)
3. Why is T1 O(n) even though it has a `while` inside a `for`?
4. T2: why does the deque hold indices and not values? Why is checking only the front enough to evict expired elements?
5. T4: why must `mid` round **up**? Trace `lo=3, hi=4, ok(4)=false` with round-down.
6. T3 never evaluates `ok(hi)`. Why not, and how does that let you handle "no answer exists"?
7. Why `x <= n / x` and not `x * x <= n`?

---

## 2. Infra brief: the 5 things you'd say, plus failure modes

**Cold first, Monday, before any reading.** Answer each prompt aloud in about 30 seconds, then compare with the key.

1. Walk a TCP connection from `connect()` to both sides fully closed. Where do the SYN queue, the accept queue, TIME_WAIT and CLOSE_WAIT fit?
2. An app calls `getaddrinfo("api.example.com")`. Name every hop and every cache between the call and the answer.
3. What happens in a TLS 1.3 handshake, what does the client verify, and what's still sent in cleartext?
4. L4 vs L7 load balancing: what each one sees, what each can do, and when you pick each.
5. "Connection refused", "connection timed out" and "connection reset": what each means at the packet level. Name four places on a Linux host where packets get dropped.

**Failure modes: name the cause, your first check, and the fix for each symptom.**

| # | Symptom |
| --- | --- |
| F1 | A client calling one backend at high request rates gets `connect: Cannot assign requested address` |
| F2 | `ss` shows 9,000 sockets in `CLOSE-WAIT` on a service, which later fails with `Too many open files` |
| F3 | `curl` to a new service fails instantly with exit 7 from one host, and after 75 s with exit 28 from another |
| F4 | Under bursts, clients' connect times jump to exactly ~1 s or ~3 s. Server CPU is fine |
| F5 | `curl` and Java say `unable to get local issuer certificate`. Browsers load the site fine |
| F6 | After a DNS cutover, some hosts reach the new IP and some keep hitting the old one for hours |
| F7 | SSH logs in fine but `cat` of a big file hangs. HTTPS stalls mid-handshake, but only over the VPN |
| F8 | A busy NAT / Kubernetes node: random connection timeouts, and `dmesg` says `nf_conntrack: table full, dropping packet` |

---

## 3. Hands-on lab (Tuesday, ~50 min)

**Where to run it:** `ss` and `nstat` are Linux-only, so use a Linux VM (the Week 1 one if it still exists; `multipass` isn't installed on this Mac any more):
```bash
brew install --cask multipass
multipass launch 24.04 --name lab --cpus 2 --memory 2G --disk 10G
multipass shell lab
sudo apt-get update && sudo apt-get install -y bind9-dnsutils tcpdump curl python3 iproute2
```
Mac-only fallbacks are marked **(mac)**. Say **"start lab"** and I'll run the Mac-side steps alongside you. **For each step: predict the output, run it, then check the key (L1–L7).**

**L1. What does the app actually use to resolve names?**
```bash
cat /etc/resolv.conf
resolvectl status | sed -n '1,25p'
grep '^hosts' /etc/nsswitch.conf
getent hosts example.com; getent ahosts example.com | head -4
```
(mac) `scutil --dns | head -20` · `dscacheutil -q host -a name example.com`
Predict: the `nameserver` line, where the *real* upstream resolver shows up, and the order of sources in `nsswitch`. Why can `getent` and `dig` disagree?

**L2. One query: read every section**
```bash
dig example.com
sleep 10; dig example.com | grep -E 'IN\s+A|Query time|SERVER'
```
Predict: `status`, the `flags`, how many A records, whether `aa` is set, and what happens to the TTL and the query time on the second run.

**L3. The full resolution path**
```bash
dig +trace example.com
```
(mac) `dig +trace @198.41.0.4 example.com` (see the key for why the plain form fails on the Mac)

Then do the hops by hand:
```bash
dig @a.root-servers.net com. NS +norec
dig @a.gtld-servers.net example.com NS +norec
dig @$(dig +short NS example.com | head -1) example.com A +norec
```
Predict: how many hops, who answers at each level, which response has the `aa` flag, and why `.com`'s servers return NS records but no A record.

**L4. Negative answers**
```bash
dig nope-zzzz.iana.org | grep -E 'status|SOA'
dig nope-zzzz.example.com | grep -E 'status|SOA'
```
Predict: the status of each. For how long will a resolver cache "this name doesn't exist", and where does that number come from?

**L5. One HTTPS request, phase by phase**
```bash
curl -sv -o /dev/null https://example.com 2>&1 | grep -E '^\*|^>|^<' | head -40
for i in 1 2 3; do curl -s -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\n' https://example.com; done
curl -sS http://127.0.0.1:9/; echo "exit=$?"
curl -sS --connect-timeout 3 http://10.255.255.1/; echo "exit=$?"
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -enddate
openssl s_client -connect example.com:443 -noservername </dev/null 2>&1 | grep -iE 'alert|no peer'
```
((mac) drop `-noservername`: LibreSSL doesn't send SNI unless you pass `-servername`.)

Predict:
- **curl -v:** the order of the TLS handshake messages, the TLS version, what ALPN negotiates, and IPv4 or IPv6 first.
- **Timings:** which `-w` gap equals one round trip, and whether these numbers are durations or something else.
- **The two failing curls:** both exit codes, and how long each takes.
- **The two `s_client` runs:** what you get without SNI.

**L6. Socket states with `ss`**
```bash
ss -s
ss -tlnp
ss -tan | awk 'NR>1{print $1}' | sort | uniq -c
```
Predict: what `Recv-Q` and `Send-Q` mean on a **LISTEN** row (it isn't what they mean on ESTAB).

*L6a. Who gets TIME_WAIT?*
```bash
python3 -m http.server 8000 --bind 127.0.0.1 >/dev/null 2>&1 & H=$!
sleep 1; for i in 1 2 3 4 5; do curl -s -o /dev/null http://127.0.0.1:8000/; done
ss -tan state time-wait '( sport = :8000 or dport = :8000 )'
sleep 61; ss -tan state time-wait '( sport = :8000 )' | wc -l; kill $H
```
(mac) `netstat -an -p tcp | grep '\.8000 '`
Predict: are the TIME-WAIT sockets on port 8000 (server) or on curl's ephemeral ports (client)? Why? What's left after 61 s?

*L6b. What CLOSE_WAIT means*
```bash
python3 -c 'import socket,time; s=socket.socket(); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); s.bind(("127.0.0.1",9000)); s.listen(); c,_=s.accept(); time.sleep(120)' & P=$!
sleep 1; python3 -c 'import socket; socket.create_connection(("127.0.0.1",9000)).close()'
ss -tanp '( sport = :9000 or dport = :9000 )'; kill $P
```
Predict: the state of each end, and which process owns the CLOSE-WAIT socket.

*L6c (stretch). Overflowing the accept queue*
```bash
python3 -c 'import socket,time; s=socket.socket(); s.bind(("127.0.0.1",9001)); s.listen(2); time.sleep(60)' &
sleep 1; for i in $(seq 10); do timeout 4 python3 -c 'import socket,time; socket.create_connection(("127.0.0.1",9001),timeout=2); time.sleep(3)' & done; sleep 2
ss -tln '( sport = :9001 )'; nstat -az TcpExtListenOverflows TcpExtListenDrops
```
Predict: the LISTEN row's Recv-Q and Send-Q, and whether the counters move.

**L7. tcpdump on one request**

Terminal A:
```bash
sudo tcpdump -i any -nn 'udp port 53 or (tcp port 80 and host example.com)'
```
Terminal B:
```bash
sudo resolvectl flush-caches; curl -4 -s -o /dev/null http://example.com/
```
Then check whether SNI goes over the wire in cleartext:
```bash
sudo tcpdump -i any -nn -A -s0 -c 20 'tcp port 443 and host example.com' 2>/dev/null | grep -a -m1 -o 'example.com' &
sleep 1; curl -4 -s -o /dev/null https://example.com/; wait
```
(mac) `-i en0` instead of `-i any`, and skip the flush.

Predict:
- **The DNS packets:** how many, which record types, and to which server or servers.
- **The TCP flags, in order:** the handshake, the request, the response, the close.
- **Who sends the first FIN**, so which side ends in TIME_WAIT.
- **The SNI check:** whether `example.com` shows up in the 443 capture.

**Cleanup:** `multipass delete --purge lab` (or keep it for Week 3).

---

## 4. Flashcards (10): fronts only, backs in the key

| # | Type | Front |
| --- | --- | --- |
| C1 | Explain | TIME_WAIT: which side gets it, the two reasons it exists, how long it lasts on Linux, and what it breaks at scale |
| C2 | Command | "Is it DNS?" What do you run, in order, to tell an app-side, resolver-side or authoritative-side problem apart? |
| C3 | Command | Take a census of a host's TCP states, count TIME_WAIT toward one backend, and check for accept-queue overflow |
| C4 | Explain | L4 vs L7 load balancer: what each sees, what each can do, and one failure each one causes |
| C5 | Explain | 502 vs 503 vs 504 from a load balancer: what each says about the backend, and how you tell who generated it |
| C6 | Command | Check a server's certificate chain, its expiry and its SAN from the CLI. What changes if you leave out SNI? |
| C7 | Command | Break one HTTPS request into DNS / connect / TLS / first-byte times |
| C8 | Explain | Thousands of CLOSE_WAIT sockets: whose bug is it, and why doesn't the kernel clean them up? |
| C9 | Template | Write the monotonic deque skeleton for the max of every length-k window |
| C10 | Template | Write `firstTrue` for binary search on the answer, plus the two conditions you must state before using it |

---

## 5. Teach-back prompts (2 min each; record, listen once, redo if more than 5 stumbles)

**The spine: "What happens when you open https://example.com?"** Name the stations yourself first, then check them against K5. Do the 2-minute version this week. It's also **Gate 1's 8-minute explain on Oct 31**, which goes down to processes and containers, so each prompt below is one station of the spine done in depth.

The explain-by-Wednesday list is marked ★. Answer it **aloud with no notes**.

1. ★ **The TCP handshake and TIME_WAIT.** Both handshakes, both queues on the server, which side gets TIME_WAIT and why, and what that does to a client making 2,000 requests/s to one backend.
2. ★ **The full DNS resolution path.** From `getaddrinfo` to an authoritative answer and back: every cache, every TTL, and the record flags.
3. ★ **L4 vs L7 load balancing.** Connection vs request, what each can and can't do, health checks, client IP, long-lived HTTP/2 / gRPC connections.
4. **The TLS 1.3 handshake.** Messages, round trips, what's verified, what's in cleartext, and what changes with mTLS and 0-RTT.
5. **502 vs 503 vs 504.** Who generates each, what it means about the backend, and your first check for each.
6. **Refused vs timeout vs reset, and where packets drop on a Linux host.**

---

## 6. Troubleshooting drills (symptom only; run "Can Some Students Handle Cold Fixes")

Out loud, 30 min each: **C**larify → **S**cope → **S**tabilize → **H**ypothesize (2–3, ranked) → **C**heck (one check per hypothesis, saying which result confirms it and which rules it out) → **F**ix and prevent (and name the alert you'd add). When you name a check, look up its result in the key's "interviewer reveals" table. Don't read the diagnosis until you've committed to one.

**Drill 1 (Wed): DNS fails intermittently**
> 10:05 page. Airflow tasks on the `us-east-1` worker pool (about 120 EC2 VMs) are failing with `socket.gaierror: [Errno -3] Temporary failure in name resolution`. It isn't one name: `db-primary.internal`, `secrets.internal` and `sts.us-east-1.amazonaws.com` all show up. About 2% of task starts fail, mostly in the first minute of each hour, when ~4,000 tasks launch. Retries usually succeed. It started Monday. The worker image was rebuilt and rolled out last Friday. From your laptop, `dig db-primary.internal` works every time.

**Drill 2 (Fri): 502s behind a load balancer**
> Wednesday 09:30. Since Tuesday's release of `profile-api`, about 0.3% of requests through the nginx tier return `502 Bad Gateway`. The rate is *higher overnight*, when traffic is low, than at peak. The service's own logs show no errors and no trace of the failing requests. All 12 backends pass health checks. The release moved `profile-api` from a JVM service to Node.js, and rolling back is slow because a schema migration shipped with it.

---

## 7. Design prompt: distributed rate limiter ("Real Apps Deserve Deep Failure Tests")

> Design rate limiting for a public API served by **200 gateway nodes in 3 regions**, peaking at **1M requests/s** globally, with **10M API keys**. Limits are per API key (e.g. 1,000 requests/min with short bursts allowed), per client IP for unauthenticated traffic, and per-endpoint overrides for expensive calls. Rejected requests get a **429** with `Retry-After`. The limiter may add at most **2 ms at p99**, and the API must keep serving if the limiter's storage fails.

45 min on paper. **Draw before you talk.** Fill all six boxes, then compare with your **Oct 10 baseline** and the reference outline in the key. (Gate 1 asks for this in 45 min *with failure modes*.)

| Step | Time | Your page must show |
| --- | --- | --- |
| **R**equirements | 5 | Functional + non-functional; your own back-of-envelope (ops/s on the store, memory per key, total memory) |
| **A**PI | 5 | The gateway → limiter call, the response headers, the config API |
| **D**ata | 5 | What state each algorithm needs per key, where it lives, how it expires |
| (diagram) | 10 | Boxes and arrows, client to backend |
| **D**eep dive | 15 | Pick one: (a) the algorithm and atomicity at 1M req/s within 2 ms, or (b) enforcing a *global* limit across 3 regions |
| **F**ailures | 5 | At least 5, each with detection and mitigation, including "the store is down" |
| **T**radeoffs | 5 | At least 3, plus what changes at 10x |

Week 2 tie-in: behind an L7 load balancer, **how do you know the client's real IP**, and why can't you just trust what arrives? What does a 429 still cost you at the TLS layer?

---

## 8. Story scaffold: 23andMe encryption and key rotation (your facts only; blanks stay blank)

Target under 2 minutes. Fill in only what you remember for certain.

| Field | Fill in |
| --- | --- |
| Situation: what data, why encryption or rotation was needed now (compliance, audit, incident, policy), your role | ______ |
| Constraint: downtime budget, data volume, read/write rate, deadline | ______ |
| My decision: where keys lived (KMS / HSM / Vault / other), the encryption scheme (e.g. envelope encryption?), how rotation worked without downtime | ______ |
| Tradeoff: what you gave up (latency vs security, re-encrypt everything vs re-encrypt lazily, complexity vs blast radius) | ______ |
| Number: data size, keys rotated, time taken, downtime, latency impact | ______ |
| Lesson: what you'd change, or what you automated afterwards | ______ |

⚠ The **40% latency and 30% throughput gains** at 23andMe belong in this story **only if they came from this project**. If they came from different work, leave them out of this one.

Follow-ups to prepare (answer from memory, real facts only):
- How did reads keep working mid-rotation? (Which key version decrypts old data?) ______
- What happens to data encrypted under the old key: re-encrypted in bulk, re-encrypted lazily on access, or kept? ______
- How did you prove nothing was left on the old key before retiring it? ______
- What if a key were compromised tomorrow: what's the blast radius, and how fast could you rotate? ______
- Encryption in transit: TLS / mTLS between services, and how *certificates* were rotated. (This is this week's TLS tie-in.) ______

---

## 9. Template test bank (LeetCode, outside this week's scheduled set)

Use these after the scheduled set, or when a template fails Monday's drill. Each first try goes on the redo schedule. The twist column is a question to answer before you code, not a hint.

**T1: monotonic stack / previous–next smaller**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 496 | Next Greater Element I | E | The template in the other direction: what flips? |
| 503 | Next Greater Element II | M | Circular: how many passes, and what do you push on the second? |
| 901 | Online Stock Span | M | Streaming: the stack must store something besides indices |
| 907 | Sum of Subarray Minimums | M | Coding-page Learn row (old solve). Drill Q2 in practice. Mod arithmetic |
| 2104 | Sum of Subarray Ranges | M | 907 run twice: what's the second run? |
| 85 | Maximal Rectangle | H | **Do after 84.** Say the reduction aloud before coding |
| 1944 | Number of Visible People in a Queue | H | What does each pop *count*? |

**T2: monotonic deque**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 239 | Sliding Window Maximum | H | Coding-page Learn row (old solve). T2 with max instead of min |
| 1696 | Jump Game VI | M | The deque holds DP values, not array values |
| 1425 | Constrained Subsequence Sum | H | Like 1696, but you may skip starting points: what changes? |
| 1499 | Max Value of Equation | H | Rewrite the expression so one part depends only on j |
| 862 | Shortest Subarray with Sum at Least K | H | The deque runs over prefix sums. Why does the front get popped for a *different* reason here? |

**T3/T4: binary search on the answer**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 875 | Koko Eating Bananas | M | Coding-page Learn row (old solve). State lo, hi and why ok() is monotone |
| 1283 | Find the Smallest Divisor Given a Threshold | M | Same shape as 875: write it in under 10 min |
| 1482 | Minimum Number of Days to Make m Bouquets | M | When is the answer −1, *before* you search? |
| 1552 | Magnetic Force Between Two Balls | M | Maximize the minimum: firstTrue or lastTrue? |
| 2226 | Maximum Candies Allocated to K Children | M | Where does lo start, and what does 0 mean? |
| 1011 | Capacity To Ship Packages Within D Days | M | **Hold until after your 410 attempt** |
| 2064 | Minimized Maximum of Products Distributed to Any Store | M | **Hold until after 410.** The check uses ceiling division |
| 2141 | Maximum Running Time of N Computers | H | Why is the check not "each computer independently"? |

**Rotated arrays (only after your 33 first attempt)**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 153 | Find Minimum in Rotated Sorted Array | M | What does comparing to `a[hi]` tell you that `a[lo]` doesn't? |
| 81 | Search in Rotated Sorted Array II | M | Duplicates: which case loses the log n bound, and why? |
| 154 | Find Minimum in Rotated Sorted Array II | H | The worst case is O(n): give the input |

**Stacks for parsing (after 20 and 71)**
| LC | Problem | Diff | Twist vs template |
| --- | --- | --- | --- |
| 1249 | Minimum Remove to Make Valid Parentheses | M | What goes on the stack, characters or indices? |
| 150 | Evaluate Reverse Polish Notation | M | Operand order on `-` and `/` |
| 394 | Decode String | M | Two stacks, or one stack of pairs? |
| 32 | Longest Valid Parentheses | H | What's the stack's sentinel, and when do you reset it? |
| 224 | Basic Calculator | H | What do you push when you see `(`? |

**Suggested order:** 496 → 901 → 2104 → 85 → 1696 → 1425 → 1283 → 1552 → 1011 → 153 → 862 → 2141. That's one clean pass over all four templates, ending on two Hards.

---
---

# ANSWER KEY

## K1. Template drill

```cpp
#include <cassert>
#include <deque>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
using ll = long long;

// T1. Monotonic stack, one pass: previous STRICTLY smaller (or -1), next smaller-OR-EQUAL (or n).
pair<vector<int>, vector<int>> boundaries(const vector<int>& a) {
    const int n = a.size();
    vector<int> prv(n, -1), nxt(n, n), st;           // st holds indices, values increasing
    for (int i = 0; i < n; ++i) {
        while (!st.empty() && a[st.back()] >= a[i]) { // a[i] is the next <= for everything it pops
            nxt[st.back()] = i;
            st.pop_back();
        }
        prv[i] = st.empty() ? -1 : st.back();         // survivor is strictly smaller
        st.push_back(i);
    }
    return {prv, nxt};
}

// T2. Monotonic deque: min of every length-k window. Values increasing front to back.
vector<int> windowMin(const vector<int>& a, int k) {
    deque<int> dq;
    vector<int> out;
    for (int i = 0; i < (int)a.size(); ++i) {
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back(); // can never be the min again
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();                   // slid out of the window
        if (i >= k - 1) out.push_back(a[dq.front()]);
    }
    return out;
}

// T3. Binary search on the answer: ok() is F..F T..T on [lo, hi], ok(hi) must be true.
template <class F>
ll firstTrue(ll lo, ll hi, F ok) {
    while (lo < hi) {
        ll mid = lo + (hi - lo) / 2;          // rounds down: hi = mid always shrinks
        if (ok(mid)) hi = mid; else lo = mid + 1;
    }
    return lo;
}

// T4. Mirror: ok() is T..T F..F on [lo, hi], ok(lo) must be true. Returns the last true.
template <class F>
ll lastTrue(ll lo, ll hi, F ok) {
    while (lo < hi) {
        ll mid = lo + (hi - lo + 1) / 2;      // rounds UP, or lo = mid loops forever
        if (ok(mid)) lo = mid; else hi = mid - 1;
    }
    return lo;
}
ll floorSqrt(ll n) {
    return lastTrue(0, n, [&](ll x) { return x == 0 || x <= n / x; });   // x*x <= n without overflow
}

int main() {
    vector<int> a{3, 1, 2, 4, 2};
    auto [prv, nxt] = boundaries(a);
    assert((prv == vector<int>{-1, -1, 1, 2, 1}));
    assert((nxt == vector<int>{1, 5, 4, 4, 5}));
    assert((windowMin({4, 2, 12, 3, 8, 1, 7}, 3) == vector<int>{2, 2, 3, 1, 1}));
    assert(windowMin(a, 1) == a);
    assert(firstTrue(0, 100, [](ll x) { return x * x >= 50; }) == 8);
    assert(firstTrue(7, 7, [](ll) { return true; }) == 7);
    assert(floorSqrt(0) == 0 && floorSqrt(1) == 1 && floorSqrt(15) == 3 && floorSqrt(16) == 4);
    assert(floorSqrt(2147483647LL) == 46340);
    ll total = 0;                                         // contribution check for Q2
    for (int i = 0; i < (int)a.size(); ++i) total += (ll)(i - prv[i]) * (nxt[i] - i);
    assert(total == (ll)a.size() * (a.size() + 1) / 2);
    cout << "all templates pass\n";
}
```
(This key was compiled and run with Apple clang, `-std=c++17 -Wall -Wextra`, and prints `all templates pass`.)

**Drill answers**
1. **`>=`.** It pops equal values too, so the survivor below `i` is strictly smaller (prv), and every popped index, including equal ones, gets `i` as its next smaller-or-equal (nxt). With `>`, equal values survive: prv becomes "previous smaller-or-equal" and nxt becomes "next strictly smaller". Both flip together.
2. It counts the subarrays in which `a[i]` is the minimum: there are `i − prv[i]` choices of left end and `nxt[i] − i` choices of right end. The left side may include values equal to `a[i]` (the stop is strictly smaller), but the right side stops at the first equal value. So each subarray is assigned to the **rightmost** occurrence of its minimum, exactly once, and the total is n(n+1)/2. If both sides used the same comparison, ties would be counted twice (both strict) or not at all (both non-strict). This is the "duplicates rule" interviewers check.
3. Each index is pushed once and popped at most once, so all the `while` iterations together are ≤ n. That's amortized O(n) total.
4. With indices you can tell whether the front has left the window (`front ≤ i − k`). Values can't tell you that. Only the front can be expired: everything behind it is newer (larger index), so if the front is still inside the window, so is everything else.
5. With round-down, `lo=3, hi=4` gives `mid=3`, and if `ok(3)` is true then `lo = 3`, which makes no progress, so it loops forever. Rounding up gives `mid=4`: if `ok(4)` is false, `hi = 3` and the loop ends at `lo = 3`.
6. While `lo < hi`, `mid < hi` always, so `ok(hi)` is never called. Pass `hi = last + 1` as a sentinel meaning "true by definition", and a result of `last + 1` means no answer exists. The mirror holds for lastTrue: `ok(lo)` is never called, so use `lo = first − 1`.
7. `x * x` overflows `long long` once x passes ~3·10^9, and hi = n can be far bigger than that. `x ≤ n / x` (integer division, x > 0) is exactly equivalent to `x² ≤ n` for integers.

## K2. Infra brief: the 5 things you'd say

1. **TCP lifecycle.**
   - **Open:** the client sends SYN with its ISN and options (MSS, window scale, SACK, timestamps). The server replies SYN-ACK, and the client ACKs. That costs **1 RTT** before any data.
   - **Two queues on the server:** half-open connections sit in the **SYN queue** (SYN_RECV; SYN cookies kick in when it's full). Completed connections sit in the **accept queue** until the app calls `accept()`. The accept queue's size is `min(backlog, net.core.somaxconn)`, and when it's full, SYNs and final ACKs get dropped (counted in `ListenOverflows`).
   - **Close:** FIN/ACK in each direction. The **active closer** (whoever sends FIN first) goes FIN_WAIT_1 → FIN_WAIT_2 → **TIME_WAIT**, for 2×MSL (**fixed at 60 s on Linux**, `TCP_TIMEWAIT_LEN`). The **passive closer** sits in **CLOSE_WAIT** until *its application* calls `close()`, then LAST_ACK.
   - **Why TIME_WAIT exists:** (1) to re-send the final ACK if the peer's FIN is retransmitted; (2) so stray segments from the old connection can't be accepted by a new connection on the same 4-tuple.
   - **What it costs:** it pins the 4-tuple. A client hitting one `ip:port` gets about 28k ephemeral ports (`ip_local_port_range` 32768–60999) per 60 s, so roughly **470 new connections/s** before `EADDRNOTAVAIL`.
   - **Fixes:** keep-alive / pooling, `tcp_tw_reuse=1` (outgoing only), more destination IPs or ports. Never `tcp_tw_recycle`: it broke NAT and was removed in Linux 4.12.
2. **DNS path.**
   - **In the app's process:** `getaddrinfo` → glibc reads `/etc/nsswitch.conf` (`hosts: files dns`) → `/etc/hosts` → `/etc/resolv.conf` (nameservers, `search`, `ndots`, `timeout`, `attempts`).
   - **Stub and recursive resolver:** the query goes to a stub such as **systemd-resolved at 127.0.0.53** (it caches), which forwards to a **recursive resolver** (VPC resolver, CoreDNS, 8.8.8.8). The recursive resolver also caches.
   - **On a cache miss, it iterates:** a **root** server (13 names, anycast) refers it to the **TLD** servers (`a–m.gtld-servers.net` for .com), which refer it to the domain's **authoritative** NS (with glue). The authoritative server answers with the `aa` flag.
   - **Caching:** every layer (browser, OS, stub, resolver) caches for the record's **TTL**. "No such name" is cached too (**negative caching**), for min(SOA TTL, SOA minimum).
   - **Transport and details:** UDP 53, with a TCP retry on truncation (TC bit). The resolver chases CNAMEs. A and AAAA are queried in parallel.
   - **The interview point:** `dig` bypasses nsswitch and `/etc/hosts`, so use `getent hosts` to see what the app sees.
3. **TLS 1.3.**
   - **Client → server:** ClientHello with supported versions, cipher suites, an **ECDHE key share**, **SNI** (the hostname, sent in **cleartext** unless ECH is used) and **ALPN** (h2 / http/1.1).
   - **Server → client:** ServerHello (chosen suite and its key share). From here on everything is encrypted: EncryptedExtensions (ALPN result), **Certificate**, **CertificateVerify** (a signature over the transcript, proving the server holds the private key), Finished.
   - **What the client verifies:** the chain up to a trusted root, the **hostname against the SAN**, and the validity dates. Then it sends its own Finished.
   - **Cost and resumption:** **1 RTT** (TLS 1.2 needed 2). Resumption uses PSK tickets. **0-RTT** early data can be replayed, so only idempotent requests should use it.
   - **Properties:** forward secrecy comes from the ephemeral ECDHE keys. With mTLS, the server sends a CertificateRequest and the client presents a certificate.
   - **Common failures:** expired cert, missing intermediate, SNI mismatch (you get the default cert), clock skew.
4. **L4 vs L7.**
   - **L4** sees the 5-tuple and routes **per connection**, without parsing the payload. It runs as NAT, as a full TCP proxy, or with DSR (direct server return). It's fast, cheap and protocol-agnostic, and its health checks are TCP connects.
   - **The L4 catch:** long-lived HTTP/2 or gRPC connections pin all their requests to one backend, so load ends up uneven. The client IP survives through pass-through modes or the **PROXY protocol**.
   - **L7** terminates TCP and TLS and parses HTTP, so it routes **per request** (host, path, header). It can retry, apply timeouts, do canary weights, auth and rate limiting, add `X-Forwarded-For`, and balance HTTP/2 streams.
   - **The L7 cost:** it holds the certificates, spends CPU on TLS, adds latency, and is the thing that *generates* 502s and 504s.
   - **Algorithms:** round robin, least outstanding requests, power of two choices, consistent hashing (for affinity). Health checks are active, passive (outlier detection), or both. Plan for **connection draining** when a backend is deregistered.
5. **Refused, timeout, reset, and where packets drop.**
   - **Refused:** you got an **RST** in reply to your SYN, so nothing is listening on that ip:port (often bound to 127.0.0.1 only) or a firewall REJECTs it. It fails instantly.
   - **Timeout:** **silence**. A firewall or security group DROPs it, a route is missing, the host is down, or the SYN / accept queue is full. The client retransmits the SYN at 1 s, then 3 s, 7 s, and so on.
   - **Reset mid-connection:** the peer's process died, the peer closed a socket that still had unread data, or a middlebox (LB, NAT, conntrack) forgot the flow.
   - **Drop points on a Linux host:** NIC ring (`ethtool -S`), softnet backlog (`/proc/net/softnet_stat`), **conntrack table full**, iptables/nftables, the SYN and accept queues (`nstat ListenOverflows`), socket buffers (`UdpRcvbufErrors`). Every socket is also an fd (Week 1, EMFILE).

**Failure modes**

| # | Cause | First check | Fix |
| --- | --- | --- | --- |
| F1 | Ephemeral port exhaustion: TIME_WAIT on the client toward one `ip:port` | `ss -tan state time-wait dst <ip> \| wc -l` vs `sysctl net.ipv4.ip_local_port_range` | Connection pooling / keep-alive; `tcp_tw_reuse=1`; more backend IPs; widen the port range |
| F2 | The app doesn't `close()` after the peer's FIN (leaked responses or connections), so each leaked socket holds an fd | `ss -tanp state close-wait` (process + peer); `ls /proc/PID/fd \| wc -l` | Fix the leak in code. A restart only buys time |
| F3 | Refused (RST: not listening, or bound to 127.0.0.1, or REJECT) vs timeout (DROP: security group/firewall, routing) | On the server: `ss -tlnp` (bind address!); from each client: `nc -vz host port`; `tcpdump 'tcp[tcpflags] & tcp-syn != 0'` on the server | Bind to 0.0.0.0, fix the SG/firewall rule |
| F4 | Accept queue overflow: SYNs dropped, so clients retry at 1 s, then 3 s | `ss -tln` on the port (LISTEN Recv-Q at Send-Q); `nstat -az TcpExtListenOverflows TcpExtListenDrops` | Raise the `listen()` backlog and `net.core.somaxconn`; accept faster (more workers) |
| F5 | The server sends only the leaf certificate (missing intermediate). Browsers paper over it with cached intermediates / AIA fetching | `openssl s_client -connect h:443 -servername h -showcerts` shows only depth 0; `Verify return code: 20/21` | Serve the full chain (`fullchain.pem`) |
| F6 | Caching: TTL not lowered before the cutover, negative caching, or app-level caches (the JVM's `networkaddress.cache.ttl`) | `dig name @<each resolver>` (compare answers and remaining TTL); check the app's DNS cache settings | Lower TTLs a day ahead; respect TTL in the app; restart the stragglers |
| F7 | Path-MTU black hole: the tunnel/VPN has a smaller MTU and ICMP "fragmentation needed" is blocked, so full-size packets vanish | `ping -M do -s 1472 host`, then step down; `ip link` (MTU); tcpdump shows full-size segments retransmitted | Allow ICMP type 3 code 4; clamp MSS (`--clamp-mss-to-pmtu`); lower the MTU |
| F8 | The conntrack table is full, so new flows get dropped | `sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max`; `conntrack -S` | Raise `nf_conntrack_max` (and the hash size); shorten timeouts; NOTRACK high-volume flows |

## K3. Lab: expected output and what each step proves
*(Your numbers will differ. Check the shape, not the digits. Values marked "seen" were captured on this Mac on Oct 20.)*

- **L1.** Ubuntu: `nameserver 127.0.0.53` and `options edns0 trust-ad` (the systemd-resolved stub). The real upstream appears under `resolvectl status` → `Current DNS Server` (multipass: usually the host bridge, e.g. 192.168.64.1). `hosts: files dns` (cloud image). `getent hosts` prints one address, often the IPv6 one; `getent ahosts` lists all of them. On this Mac, `scutil --dns` shows 8.8.8.8 and 8.8.4.4. *Proves:* the app resolves through nsswitch → `/etc/hosts` → stub → upstream, while `dig` talks DNS directly. That's why "dig works but the app fails" is possible: think `/etc/hosts`, search domains, nscd.
- **L2.** `status: NOERROR`, flags `qr rd ra` (plus `ad` if the resolver validates DNSSEC; seen with 8.8.8.8). **No `aa`**, because the answer comes from a recursive resolver, not the authority. Two A records (seen: `104.20.23.154`, `172.66.147.243`) with TTL ≤ 300. On the second run, the **TTL has counted down** (a cached copy) and the query time is ~0–1 ms (seen: 37 ms on the first run). `SERVER: 127.0.0.53#53` on Ubuntu. *Proves:* how to read the header, the flags and caching.
- **L3.**
  - **The Mac gotcha:** dig 9.10.6 here prints only `;; Received 28 bytes from 8.8.8.8` and stops, because its first step (asking the system resolver for the root NS) comes back empty. Starting at a root server works.
  - **Four hops:** your resolver gives the root list → **root** refers you to `com.` (`a–m.gtld-servers.net`, TTL 172800) → **gtld** refers you to `example.com. NS hera.ns.cloudflare.com. / elliott.ns.cloudflare.com.` (plus DS records) → **Cloudflare's NS** answers `A 104.20.23.154 / 172.66.147.243` (TTL 300). Seen: `Received 1097 bytes from 198.41.0.4`, `… from j.root-servers.net`, `… from d.gtld-servers.net`, `… from hera.ns.cloudflare.com`.
  - **The manual hops:** the root and gtld replies have flags `qr` with **no `aa`**, ANSWER 0, and the AUTHORITY section filled (a **referral**). The last reply has **`qr aa`**.
  - **Why no A record from `.com`:** delegation. `.com` only knows *who* is authoritative for example.com, not its records.
  - *Proves:* the resolution path, hop by hop, and which server actually owns the answer.
- **L4.**
  - **`nope-zzzz.iana.org`:** `status: NXDOMAIN`, with an SOA in AUTHORITY. The negative TTL is min(SOA TTL, SOA minimum) (RFC 2308).
  - **`nope-zzzz.example.com`:** `status: NOERROR` with an empty answer plus an SOA (seen: `example.com. 1800 IN SOA elliott.ns.cloudflare.com. dns.cloudflare.com. … 1800`). Cloudflare synthesizes "name exists, no record" (NODATA) instead of NXDOMAIN, part of its DNSSEC "black lies" scheme. Either way, the miss is cached for **1800 s**.
  - *Proves:* create the record **before** anything looks it up, or the "missing" answer is cached for 30 minutes. It also shows that a status of NOERROR doesn't mean the name exists.
- **L5.**
  - **The `-v` lines, in order (seen):** `IPv6: 2606:4700:…` / `IPv4: …`, then `Trying [2606:4700:10::ac42:93f3]:443` (IPv6 first: happy eyeballs), `Connected`, `ALPN: curl offers h2,http/1.1`, then the handshake: `Client hello (1)` → `Server hello (2)` → `Unknown (8)` (that's **EncryptedExtensions**; Ubuntu's OpenSSL names it) → `Certificate (11)` → `CERT verify (15)` → `Finished (20)`, then `(OUT) Finished (20)`. After that: `SSL connection using TLSv1.3 / …`, `ALPN: server accepted h2`, `subject: CN=example.com`, `issuer: … CN=Cloudflare TLS Issuing ECC CA 3`, `expire date: Dec 25 … 2026`, `> GET / HTTP/2`, `< HTTP/2 200`. TLS 1.3 has no ServerKeyExchange and no ChangeCipherSpec.
  - **The `-w` numbers are cumulative from the start, not durations.** Seen: `dns=0.002 connect=0.025 tls=0.053 ttfb=0.081`. So connect − dns ≈ **1 RTT** (TCP), tls − connect ≈ **1 RTT** (TLS 1.3), and ttfb − tls ≈ 1 RTT plus server time. DNS is ~0 because it was cached.
  - **The two failing curls:** `curl: (7) Failed to connect to 127.0.0.1 port 9 after 0 ms: Couldn't connect to server` (RST, instant), and `curl: (28) Failed to connect to 10.255.255.1 port 80 after 3001 ms: Timeout was reached` (silence).
  - **`s_client`:** with SNI you get `subject= /CN=example.com`, `notAfter=Dec 25 22:56:35 2026 GMT`. **Without SNI: `alert handshake failure … SSL alert number 40`, `no peer certificate available`**, because a shared edge can't pick a certificate without the name.
  - *Proves:* every phase of the spine on one request, and what refused vs timeout looks like from the client.
- **L6.**
  - **`ss -s`:** a summary with `estab`, `timewait` and so on.
  - **On a LISTEN row,** `Recv-Q` is the **current accept-queue length** and `Send-Q` is the **backlog limit** (e.g. 4096, the default `somaxconn` on kernels ≥ 5.4, or whatever the app passed to `listen()`). On ESTAB rows they're unread / unacked bytes.
  - **L6a:** the TIME-WAIT rows are on the **server's** side, `127.0.0.1:8000 → 127.0.0.1:5xxxx`. Python's `http.server` speaks HTTP/1.0 and closes after each response, so the **server is the active closer**. Seen on the Mac: three `127.0.0.1.8765 … TIME_WAIT` rows. After 61 s the count is **0** (Linux's fixed 60 s; macOS uses 2×MSL = 30 s, since `net.inet.tcp.msl: 15000`). The common confusion: `tcp_fin_timeout` controls FIN_WAIT_2, not TIME_WAIT. Against example.com, curl closes first, so TIME_WAIT lands on the **client**.
  - **L6b:** `CLOSE-WAIT 127.0.0.1:9000 → 127.0.0.1:5xxxx`, owned by `python3` (the server that never called `close()`), and `FIN-WAIT-2` on the client side. Seen: exactly that pair. The orphaned FIN-WAIT-2 times out on its own (`tcp_fin_timeout`), but **CLOSE-WAIT lasts until the app closes, so forever if it leaks**.
  - **L6c:** the LISTEN row shows `Recv-Q 3`, `Send-Q 2` (Linux admits backlog + 1). `TcpExtListenOverflows` and `ListenDrops` climb. The extra clients' SYNs get dropped, they retry at 1 s and 3 s, and some hit their 2 s timeout. That's F4 by hand.
  - *Proves:* the active closer gets TIME_WAIT, CLOSE_WAIT is always an application bug, and how to read queue depth.
- **L7.**
  - **DNS:** from curl to `127.0.0.53` you see `A? example.com.` (only A, because `-4` asks for IPv4 only; drop `-4` and an `AAAA?` appears next to it). systemd-resolved then forwards the query upstream on the external interface, and the answer comes back (`A 104.20.23.154, A 172.66.147.243`). So that's 2 queries on the wire for one lookup: stub, then upstream.
  - **TCP open:** `Flags [S]`, `[S.]`, `[.]`.
  - **Request and response:** `[P.] … length 7x: HTTP: GET / HTTP/1.1`, then `[.]`, then `[P.] … HTTP/1.1 200 OK` (or a redirect) over one or more segments.
  - **Close:** **curl sends `[F.]` first**, the server sends `[F.]`, curl sends `[.]`. So the client is the active closer and the **client** gets TIME_WAIT.
  - **SNI check:** prints `example.com`, so the SNI went over the wire in cleartext (ECH is what would hide it).
  - *Proves:* you can point at every packet of the spine, and you have physical evidence for the TIME_WAIT and SNI claims.

## K4. Flashcard backs

- **C1. TIME_WAIT.**
  - **Who:** the **active closer** (whoever sent FIN first).
  - **Why:** (1) it can re-send the last ACK if the peer's FIN is retransmitted; (2) old duplicate segments can't leak into a new connection on the same 4-tuple.
  - **How long:** 2×MSL, **60 s fixed** on Linux.
  - **What breaks at scale:** a client making many short connections to one `ip:port` runs out of ephemeral ports (~28k / 60 s ≈ 470 conn/s) and gets `EADDRNOTAVAIL`.
  - **Fixes:** pooling and keep-alive, `tcp_tw_reuse=1`, more destination IPs. Server-side TIME_WAIT is mostly harmless.
- **C2. Is it DNS?**
  - `getent hosts name` shows what the app sees (nsswitch + `/etc/hosts` + search list).
  - `dig name` asks the default resolver.
  - `dig @<each nameserver in resolv.conf> name` checks each resolver.
  - `dig @<authoritative NS> name +norec` checks the source of truth.
  - `dig +trace name` walks the delegation.
  - Compare answers, status codes (NXDOMAIN / SERVFAIL / timeout) and TTLs. On systemd-resolved: `resolvectl query name`, `resolvectl statistics`. Timeouts point to the path or the resolver; SERVFAIL points to the authority or DNSSEC; a wrong answer points to caching or a stale record.
- **C3.** `ss -s` · `ss -tan | awk 'NR>1{print $1}' | sort | uniq -c` · `ss -tan state time-wait dst 10.0.0.5 | wc -l` · `ss -tlnp` (LISTEN Recv-Q vs Send-Q) · `nstat -az TcpExtListenOverflows TcpExtListenDrops`.
- **C4. L4 vs L7.**
  - **L4:** works on connections (the 5-tuple), with no payload parsing. Fast, protocol-agnostic, TCP health checks, client IP via pass-through or PROXY protocol. *Failure:* one long-lived HTTP/2 or gRPC connection pins all its requests to one backend.
  - **L7:** terminates TLS and routes per request (host, path, header), with retries, timeouts, `X-Forwarded-For`, rate limiting and canaries. *Failure:* it's an extra hop that generates 502s and 504s itself (idle-timeout mismatches, header limits), and it costs TLS CPU.
- **C5. 502 vs 503 vs 504.**
  - **502:** the proxy got an **invalid or no response**: refused or reset, the upstream closed early (keep-alive race), a crash mid-response, or a malformed header.
  - **503:** **no healthy upstream**, overload or load shedding, maintenance, or (for some proxies) a rate limit.
  - **504:** the upstream **accepted but didn't answer** within the proxy's timeout.
  - **Who generated it:** check the response's `Server` / `Via` headers and the body, and whether the LB access log shows an LB status vs an upstream status (and the upstream response time). An app can return 502 or 503 itself too.
- **C6.** `openssl s_client -connect host:443 -servername host -showcerts </dev/null` gives the chain and `Verify return code: 0 (ok)`. Pipe it to `openssl x509 -noout -subject -issuer -dates` (and `-ext subjectAltName` on OpenSSL ≥ 1.1.1). Leave out SNI and a shared front end serves the default certificate or aborts the handshake (seen on example.com: **alert 40**, no peer certificate).
- **C7.** `curl -s -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\n' URL`. The times are **cumulative**, so subtract neighbours to get each phase.
- **C8. CLOSE_WAIT.** The peer sent FIN and the kernel ACKed it, but **your application never called `close()`**. The kernel can't close a socket the app still owns, so there's no timeout. It's an app bug: an unclosed response body or connection, a stuck worker, or a pool that leaks. Each socket holds an fd, so it ends in EMFILE. `ss -tanp state close-wait` tells you which process.
- **C9.**
  ```cpp
  deque<int> dq;                                                   // indices, values decreasing
  for (int i = 0; i < n; ++i) {
      while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
      dq.push_back(i);
      if (dq.front() <= i - k) dq.pop_front();
      if (i >= k - 1) out.push_back(a[dq.front()]);
  }
  ```
- **C10.** `while (lo < hi) { mid = lo + (hi - lo) / 2; if (ok(mid)) hi = mid; else lo = mid + 1; } return lo;` State two things before you use it: **(1) ok() is monotone** over [lo, hi] (F…F T…T), and **(2) the answer lies in [lo, hi]** (hi is a valid answer, or a sentinel).

## K5. Teach-back must-hit checklist

0. **The spine (opening https://example.com).** One line per station:
   1. **Browser:** URL parse; HSTS (forces https); caches; reuse of an existing HTTP/2 connection.
   2. **DNS:** `getaddrinfo` → stub → recursive → root / TLD / authoritative; TTL caches; A + AAAA; happy eyeballs.
   3. **TCP:** pick an ephemeral port; route lookup plus ARP / neighbour discovery for the next hop; SYN / SYN-ACK / ACK (1 RTT); the server's accept queue.
   4. **TLS 1.3:** ClientHello (SNI, ALPN, key share); certificate chain, SAN and dates checked; 1 RTT.
   5. **HTTP/2:** a request on a stream.
   6. **Edge:** CDN / L4 → L7 proxy (TLS termination, routing by host or path, `X-Forwarded-For`, a health-checked pool, retries and timeouts).
   7. **Backend:** `accept()` → a worker handles the request (**Week 1:** fds, threads, PID 1 in a container, cgroup limits) → calls to the database and cache (more DNS, TCP and TLS).
   8. **Response:** keep-alive or close, and TIME_WAIT on the active closer; the browser renders and reuses the connection for subresources.

   *For the 8-minute Gate 1 version, add:* container networking (veth, bridge, iptables NAT, conntrack; that's Week 3) and where each layer fails (DNS → NXDOMAIN or timeout, TCP → refused or timeout, TLS → cert errors, LB → 502 / 503 / 504, app → 5xx).
1. **TCP / TIME_WAIT:** the 3-way handshake with ISNs; both queues and `somaxconn`; the 4-way close; active closer → TIME_WAIT for 60 s, both reasons; passive closer → CLOSE_WAIT (the app must close); ~470 conn/s per destination limit; pooling and `tw_reuse`; never `tw_recycle`.
2. **DNS:** nsswitch → hosts → resolv.conf (`search`, `ndots`, `timeout`, `attempts`) → stub → recursive → root → TLD → authoritative (`aa`) → cache by TTL; negative caching from the SOA; UDP with TCP fallback; CNAME chains; `dig` vs `getent`; lower the TTL before migrations.
3. **L4 vs L7:** per connection vs per request; what each can inspect; health checks; client IP (PROXY protocol vs XFF); HTTP/2 / gRPC imbalance at L4; TLS termination at L7; connection draining; the algorithms (least requests, P2C, consistent hashing); and that L7 is where 502 / 504 come from.
4. **TLS 1.3:** ClientHello / ServerHello key shares; encrypted EncryptedExtensions, Certificate, CertificateVerify, Finished; 1 RTT vs TLS 1.2's 2 RTT; what's verified (chain, SAN, dates); SNI in cleartext (ECH); forward secrecy; resumption and 0-RTT replay risk; mTLS CertificateRequest; the common failures (expired, missing intermediate, SNI mismatch, clock skew).
5. **502 / 503 / 504:** the definitions in C5. First checks: the proxy's error log (the reason string), the upstream response time (~0 means a connection or keep-alive problem; ≈ the timeout means a slow backend), the split by backend and by method, and deploy correlation.
6. **Refused / timeout / reset:** RST vs silence vs mid-stream RST; the SYN retransmit backoff; the drop points (NIC ring, softnet, conntrack, firewall, SYN / accept queue, socket buffers), each with its counter.

## K6. Troubleshooting diagnoses

### Drill 1: DNS fails intermittently

**Interviewer reveals (what each check would show):**

| You run | You see |
| --- | --- |
| `cat /etc/resolv.conf` on a worker | `nameserver 10.20.0.2` · `search ec2.internal` · `options timeout:2 attempts:2` (the old image had `nameserver 127.0.0.53`) |
| `systemctl is-active systemd-resolved nscd` | `inactive` `inactive`. The Friday image dropped the local caching stub |
| `getent hosts db-primary.internal` 200× in a loop | at :00:20, 3–5 failures, each taking ~4 s; at :30:00, 0 failures |
| `sudo tcpdump -nn -i ens5 udp port 53` at :00:10, counted per second | ~1,800–2,500 queries/s from **one** VM: the same ~6 names over and over, A and AAAA for each |
| `ethtool -S ens5 \| grep allowance` | `linklocal_allowance_exceeded: 48213`, jumping at every top of the hour · `pps_allowance_exceeded: 0` |
| `dig @10.20.0.2 db-primary.internal` from a worker at :20 | answers in < 1 ms, NOERROR |
| Resolver-side metrics | no SERVFAILs, no errors |
| The same image on the `eu-west-1` pool | fine: about 600 task starts per hour, much lower bursts |

**Diagnosis:** the Friday image removed the local caching resolver and pointed `resolv.conf` straight at the VPC resolver. Now every `getaddrinfo` from every task goes over the network. At the top of the hour, each VM bursts thousands of DNS packets per second: A and AAAA, times every short-lived connection, with nothing cached. AWS allows **1,024 packets/s per network interface** to link-local services (VPC DNS, the metadata service, time sync). The excess is dropped silently at the hypervisor, and the `linklocal_allowance_exceeded` counter is the proof. glibc times out and retries (`timeout:2 attempts:2`), and the lookups that lose every retry return `EAI_AGAIN`. Your laptop is fine because it takes a different path and has no burst.
- **Clarify:** *many* names fail, not one record, so suspect the resolution path. The top of the hour points at load. What changed: the image, on Friday.
- **Scope:** one region's pool, in proportion to task volume. The same image elsewhere is fine at a lower rate. That rules out the record and the resolver service itself.
- **Stabilize:** re-enable systemd-resolved (or roll back the image) on the pool through config management; add jitter to task start times so the hourly burst flattens; retry name resolution with backoff.
- **Hypotheses (ranked):**
  1. Per-host DNS packets being dropped (a rate limit) → the `ethtool` allowance counter, and query rate vs failures in tcpdump.
  2. The resolver returning SERVFAIL for some names → tcpdump shows responses with `ServFail`, not missing responses (ruled out: the responses are just absent).
  3. Host-side UDP drops or conntrack → `nstat -az UdpRcvbufErrors UdpInErrors`, `conntrack -S` (clean).
- **Fix:** a local caching stub in the image (systemd-resolved, unbound or dnsmasq), which caches positive *and* negative answers. Connection pooling in tasks, so there are fewer new lookups. Jittered scheduling.
- **Prevent and alert:** alert on `linklocal_allowance_exceeded > 0` (ENA metrics via the CloudWatch agent or a node_exporter ethtool collector); a synthetic `getent` probe per pool (failure rate and latency); an image test that asserts the stub resolver is running; a per-host DNS query rate metric.
- **Other branches, if the reveals differ:**
  - **Kubernetes:** a conntrack race on parallel A/AAAA lookups from one socket gives 5 s stalls (fix: NodeLocal DNSCache or `options single-request-reopen`), and `ndots:5` multiplies queries through the search list (Week 4).
  - **A dead nameserver in resolv.conf** gives *slow* lookups (glibc moves on to the next one), not failures.
  - **SERVFAIL** for a single zone points to a broken authoritative server or expired DNSSEC.
  - **A record created after the first lookup** stays "missing" for the negative TTL.

### Drill 2: 502s behind a load balancer

**Interviewer reveals:**

| You run | You see |
| --- | --- |
| nginx `error.log` around a 502 | `upstream prematurely closed connection while reading response header from upstream … upstream: "http://10.1.4.22:8080/v1/profile"` and some `recv() failed (104: Connection reset by peer) while reading response header from upstream` |
| 502s by method (access log) | 93% `POST`/`PATCH`, 7% `GET` |
| 502s by `$upstream_addr` | spread evenly across all 12 backends |
| `$upstream_response_time` on the 502 lines | `0.000`–`0.002` (instant, not a timeout) |
| The nginx `upstream` block | `keepalive 64; keepalive_timeout 60s;` and `proxy_http_version 1.1; proxy_set_header Connection "";` |
| The new service's HTTP server settings | Node.js defaults: `keepAliveTimeout` = **5 s**. The old JVM service had a 75 s idle timeout configured |
| `curl` straight to a backend, 1,000 times | all 200 |
| `tcpdump -nn -i any 'tcp port 8080 and tcp[tcpflags] & (tcp-fin\|tcp-rst) != 0'` on a backend | the backend sends `[F.]` on connections idle ~5 s; milliseconds later nginx writes a request on that same connection and the backend answers `[R]` |
| Backend restarts / OOM (`journalctl`, exit codes) | none |

**Diagnosis:** a **keep-alive idle-timeout mismatch**. nginx keeps idle upstream connections for up to 60 s and reuses them, while Node closes idle connections after 5 s. When nginx picks a connection the backend has just closed, the request meets a FIN or RST, and nginx returns 502. That explains each clue:
- **Worse overnight:** at low traffic, more connections sit idle past 5 s.
- **POST-heavy:** nginx retries a failed request on the next upstream (`proxy_next_upstream error timeout`), but it won't retry **non-idempotent** methods once the request was sent. So the GET failures are mostly retried away and the POSTs reach the client.
- **No app log:** the request never reached a handler.
- **Instant failure:** the upstream response time is ~0, so it isn't a slow backend.

The method:
- **Clarify:** exactly which status (502, not 504), since when (the release), who generates it (nginx: the error log, `Server: nginx`), and the split by method and endpoint.
- **Scope:** all backends equally and all endpoints, so it's the runtime or proxy config, not one host or one code path.
- **Stabilize:** reload nginx with the upstream `keepalive_timeout 4s` (below the backend's). It's a config reload, so no rollback is needed. Don't turn on `non_idempotent` retries unless the POSTs carry idempotency keys.
- **Hypotheses (ranked):**
  1. Idle-timeout mismatch → compare the two timeouts; tcpdump shows the FIN at ~5 s idle followed by an RST.
  2. Backends crashing or restarting → the error log would say `connect() failed (111: Connection refused)`, and there would be restarts or exit 137 (ruled out).
  3. Response headers too large / protocol errors → a different error-log string (`upstream sent too big header`).
  4. No connection draining on deploys → 502s only during deploys (ruled out: they're steady).
- **Fix:** **the idle timeout on the side that receives requests must be longer than on the side that reuses connections.** In Node: `server.keepAliveTimeout = 65000` and `server.headersTimeout = 66000` (headersTimeout above keepAliveTimeout). Keep nginx's (or an ALB's, 60 s by default) lower.
- **Prevent and alert:** alert on 502 rate per upstream, grouped by the error-log reason; a deploy checklist / config lint ("backend idle timeout > proxy idle timeout"); a synthetic low-rate POST canary (it catches this overnight); idempotency keys so POSTs can be retried safely.
- **Other branches:**
  - **`no live upstreams`:** every backend has been marked failed (`max_fails`); look at why they're failing.
  - **504 with `upstream timed out (110)`:** the backend is slow.
  - **502s only during deploys:** missing deregistration delay or preStop draining.
  - **`SSL_do_handshake() failed`:** a TLS problem between nginx and the upstream.
  - **An ALB in front instead of nginx:** the same idle-timeout rule applies (ALB idle timeout 60 s by default, so the backend's keep-alive must be longer).

## K7. Design reference outline: distributed rate limiter

**Requirements**
- **Functional:** per-key limits with bursts; per-IP limits for anonymous traffic; per-endpoint and per-tier overrides; 429 plus `Retry-After` and `RateLimit-Limit/Remaining/Reset` headers; limits change without a deploy.
- **Non-functional:** ≤ 2 ms p99 overhead; **the API stays up if the limiter fails** (fail-open by default, fail-closed for abuse-sensitive endpoints); ~5–10% over-admission is acceptable; limits are enforced across the whole fleet, not per node.
- **Back-of-envelope:**
  - **A central check per request** means 1M ops/s on the store. A Redis shard does ~100–200k simple ops/s (fewer with Lua), so that's ~10–20 shards per region at peak.
  - **Token-bucket state** (tokens, last refill time, plus the key) is ~64–100 B × 10M keys ≈ **≤ 1 GB**. That's fine.
  - **A sliding log** at 1,000 req/min stores up to 1,000 timestamps per key (~16 KB), which is far too much at 10M keys. Reject it.

**API**
- **Gateway → limiter:** `check(key, cost=1) → {allowed, remaining, reset_ms}`, an in-process filter with a remote store.
- **Config:** `PUT /limits/{scope}` (key / tier / endpoint), pushed to the gateways and cached locally.
- **Response headers:** `429`, `Retry-After`, `RateLimit-*`.

**Data**
- **Token bucket per key:** `{tokens, last_ts}`. Refill lazily: `tokens = min(burst, tokens + (now − last_ts) × rate)`.
- **Sliding-window counter per key:** two counters (current window, previous window), with `estimate = prev × (1 − elapsed/W) + curr`.
- **Where it lives:** Redis Cluster, keyed `rl:{api_key}` (the hash tag keeps a key on one shard), with a TTL of about 2× the window so idle keys expire. Limit configs live in Postgres and are pushed to the gateways.

**Diagram:** client → **L4 LB** → **L7 gateway** fleet (limiter filter + local cache) → per-region **Redis Cluster** → backends. Off to the side: config service → gateways; metrics (allowed / limited / store errors and latency).

**Deep dive (a): algorithm, atomicity, latency**
- **Algorithm:** token bucket (allows bursts; two fields) or sliding-window counter (smooth; two counters). A **fixed window** allows 2× bursts at window boundaries. A **sliding log** is exact but too expensive in memory.
- **Atomicity:** read-modify-write must be atomic, so use a **Lua script** (`EVALSHA`). GET-then-SET races under concurrency. For counter algorithms, `INCR` plus `EXPIRE` works.
- **Time:** take it from one source (Redis `TIME`, or gateway clocks with bounded skew).
- **Latency:** pipeline requests; keep connections pooled and pinned per shard; set a **1–2 ms timeout** on the limiter call, and fall back on timeout.
- **Hot keys** (one huge customer, one hot shard): **local token leasing**. A gateway takes a batch of N tokens per refill and spends them locally. Store traffic drops N×, at the cost of up to N × (number of gateways) over-admission, so size N to the key's rate.

**Deep dive (b): global limits across 3 regions**
- **Split the limit per region** (limit / 3): simple, but unfair when traffic is skewed.
- **Per-region enforcement plus async sync:** count locally and gossip or replicate counts every 100–500 ms (CRDT-style G-counters). Over-admission is bounded by sync interval × rate. **This is the usual choice.** State the bound out loud.
- **One global store:** a 50–100 ms cross-region RTT breaks the 2 ms budget. Reject it.

**Failures (detection → mitigation)**
1. **A store shard is down or slow** → the timeout fires and the circuit breaker opens → **fail open** to a local per-node bucket (limit / number of nodes). Fail closed only on expensive or abuse endpoints. Alert on the fallback rate.
2. **Store failover** loses recent counts → brief over-admission. Accept it and say so.
3. **A hot key** saturates one shard → leasing or key splitting; per-shard CPU alerts.
4. **A bad config push** (limit = 0, so mass 429s) → validation, canary rollout of configs, one-click rollback; alert on a 429-rate spike.
5. **Clients retry storms on 429s** → `Retry-After` with jitter; client SDKs back off.
6. **Clock skew between gateways** → use the store's time, or tolerate skew in the window maths.
7. **A cross-region partition** → each region keeps enforcing its local share and reconciles when the link heals.
8. **A volumetric or L4 attack** → the L7 limiter can't help, because each 429 still costs a TCP and TLS handshake. Rely on SYN cookies, edge or cloud DDoS protection, and connection limits at the L4 LB.

**Tradeoffs**
- Accuracy vs latency: a central check vs local leasing / async sync.
- Fail-open vs fail-closed: availability vs protection.
- Token bucket (bursty APIs) vs sliding window (smooth).
- Exactness vs memory: log vs counters.
- **At 10x (10M req/s):** local leasing becomes mandatory; shard per region at ~100+ nodes, or move to gateway-to-gateway gossip; approximate per-IP heavy hitters with a count-min sketch.

**Week 2 tie-in**
- **Client IP:** behind an L7 LB the TCP source address is the LB. Use `X-Forwarded-For`, but trust only entries appended by your own proxies: take the right-most untrusted address, because clients can forge the left side. At L4, use the PROXY protocol. Aggregate IPv6 to /64.
- **429 vs 503:** 429 means "you are over your limit"; 503 means "we are overloaded".
- **What a 429 still costs:** a TCP handshake plus a full TLS handshake, which is why volumetric defence belongs at L3/L4 and the edge.

## K8. Story rubric (no answers; your facts only)

- Under 2 minutes. Situation → **your** decision → the tradeoff said out loud → one number → a concrete lesson.
- The interviewer should be able to tell **data-at-rest key rotation** (KMS / envelope keys, re-encryption) from **in-transit certificate rotation** (TLS / mTLS). Say which one your story is, or both.
- The rotation mechanism has to survive the follow-up "how did reads work mid-rotation?". If you don't remember, say what you'd verify, and don't fill it in.
- A number only goes in if it's real and from this project. The 40% / 30% gains stay out unless they came from this work.
- If a blank in §8 stays blank, that part stays out of the story.
