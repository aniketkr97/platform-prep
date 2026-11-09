"""Toy web service for the Week 5 pipeline lab.

VERSION   - reported in the X-Version header and the body
FAIL_RATE - fraction of GET / requests that return 500 (0.0 = healthy)
/healthz always returns 200, even when / is failing.
"""
import os
import random
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = os.environ.get("VERSION", "dev")
FAIL_RATE = float(os.environ.get("FAIL_RATE", "0"))


def handle(path, rng=random.random):
    if path == "/healthz":
        return 200, "ok\n"
    if rng() < FAIL_RATE:
        return 500, f"error from {VERSION}\n"
    return 200, f"hello from {VERSION}\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        code, body = handle(self.path)
        data = body.encode()
        self.send_response(code)
        self.send_header("X-Version", VERSION)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
