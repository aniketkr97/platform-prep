#!/usr/bin/env python3
"""Fake pager for the Week 6 lab. Alertmanager POSTs here; every notification prints one line.

Run:  python3 receiver.py       (listens on :5001)
"""
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


class Pager(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        stamp = time.strftime("%H:%M:%S")
        for a in body.get("alerts", []):
            print(f'{stamp}  NOTIFY  {a["status"]:8}  {a["labels"].get("alertname")}  '
                  f'severity={a["labels"].get("severity")}  slo={a["labels"].get("slo")}', flush=True)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    print("fake pager on :5001", flush=True)
    HTTPServer(("", 5001), Pager).serve_forever()
