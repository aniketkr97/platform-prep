#!/usr/bin/env python3
"""Toy service for the Week 6 lab. Python stdlib only, no installs.

  GET /work                                -> 200, or 500 at the injected error rate
  GET /fault?error_rate=0.2&latency_ms=300 -> inject faults (either field alone is fine)
  GET /fault?clear=1                       -> back to healthy
  GET /metrics                             -> Prometheus text format

Run:  python3 app.py            (listens on :8000)
"""
import random
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

BUCKETS = [0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]

lock = threading.Lock()
req_count = {200: 0, 500: 0}        # status code -> count; start at 0 so the error series exists
bucket_count = [0] * len(BUCKETS)   # per-bucket (not cumulative) counts
dur_sum = 0.0
dur_count = 0
fault = {"error_rate": 0.0, "latency_ms": 0}


def observe(code, seconds):
    global dur_sum, dur_count
    with lock:
        req_count[code] = req_count.get(code, 0) + 1
        dur_sum += seconds
        dur_count += 1
        for i, le in enumerate(BUCKETS):
            if seconds <= le:
                bucket_count[i] += 1
                break


def render_metrics():
    with lock:
        lines = [
            "# HELP http_requests_total Requests to /work by status code.",
            "# TYPE http_requests_total counter",
        ]
        for code in sorted(req_count):
            lines.append(f'http_requests_total{{handler="/work",code="{code}"}} {req_count[code]}')
        lines += [
            "# HELP http_request_duration_seconds Latency of /work.",
            "# TYPE http_request_duration_seconds histogram",
        ]
        running = 0
        for le, n in zip(BUCKETS, bucket_count):
            running += n
            lines.append(f'http_request_duration_seconds_bucket{{handler="/work",le="{le}"}} {running}')
        lines.append(f'http_request_duration_seconds_bucket{{handler="/work",le="+Inf"}} {dur_count}')
        lines.append(f'http_request_duration_seconds_sum{{handler="/work"}} {dur_sum:.6f}')
        lines.append(f'http_request_duration_seconds_count{{handler="/work"}} {dur_count}')
        lines += [
            "# HELP toy_fault_error_rate Injected error rate (0 = healthy).",
            "# TYPE toy_fault_error_rate gauge",
            f"toy_fault_error_rate {fault['error_rate']}",
        ]
    return "\n".join(lines) + "\n"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):   # keep the terminal quiet
        pass

    def reply(self, code, body, ctype="text/plain"):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        q = parse_qs(url.query)
        if url.path == "/work":
            start = time.monotonic()
            time.sleep(random.uniform(0.010, 0.040) + fault["latency_ms"] / 1000)
            code = 500 if random.random() < fault["error_rate"] else 200
            self.reply(code, "ok\n" if code == 200 else "boom\n")
            observe(code, time.monotonic() - start)
        elif url.path == "/metrics":
            self.reply(200, render_metrics(), "text/plain; version=0.0.4")
        elif url.path == "/fault":
            with lock:
                if "clear" in q:
                    fault.update(error_rate=0.0, latency_ms=0)
                if "error_rate" in q:
                    fault["error_rate"] = min(max(float(q["error_rate"][0]), 0.0), 1.0)
                if "latency_ms" in q:
                    fault["latency_ms"] = max(int(q["latency_ms"][0]), 0)
                state = dict(fault)
            self.reply(200, f"fault now: {state}\n")
        else:
            self.reply(404, "not found\n")


if __name__ == "__main__":
    print("toy service on :8000  (/work /fault /metrics)")
    ThreadingHTTPServer(("", 8000), Handler).serve_forever()
