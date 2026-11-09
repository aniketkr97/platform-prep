#!/usr/bin/env python3
"""Tiny Terraform HTTP state backend with locking (lab use only).

State is kept in ./store/state.json and the lock in ./store/lock.json, so a lock
survives the terraform process that took it, the way an S3 lockfile or a
DynamoDB lock item does. Run: python3 lock_server.py
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

STORE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")
STATE = os.path.join(STORE, "state.json")
LOCK = os.path.join(STORE, "lock.json")
os.makedirs(STORE, exist_ok=True)


def read(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return f.read()


class Handler(BaseHTTPRequestHandler):
    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n else b""

    def reply(self, code, data=b""):
        self.send_response(code)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def current_lock_id(self):
        raw = read(LOCK)
        return json.loads(raw)["ID"] if raw else None

    def do_GET(self):
        data = read(STATE)
        self.reply(200, data) if data else self.reply(404)

    def do_POST(self):  # write state (like S3, it does not check the lock)
        with open(STATE, "wb") as f:
            f.write(self.body())
        self.reply(200)

    def do_DELETE(self):
        if os.path.exists(STATE):
            os.remove(STATE)
        self.reply(200)

    def do_LOCK(self):
        info = self.body()
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)  # atomic create-if-absent
        except FileExistsError:
            self.log_message("LOCK refused: held by %s", self.current_lock_id())
            return self.reply(423, read(LOCK))
        with os.fdopen(fd, "wb") as f:
            f.write(info)
        self.log_message("LOCK granted: %s", json.loads(info)["ID"])
        self.reply(200)

    def do_UNLOCK(self):
        raw = self.body()
        want = json.loads(raw).get("ID") if raw else None
        held = self.current_lock_id()
        if held is None:
            return self.reply(200)
        if want is None:  # `terraform force-unlock` sends no lock info
            os.remove(LOCK)
            self.log_message("FORCE-UNLOCK: removed %s", held)
            return self.reply(200)
        if want != held:
            self.log_message("UNLOCK refused: asked %s, held %s", want, held)
            return self.reply(409, read(LOCK))
        os.remove(LOCK)
        self.log_message("UNLOCK: %s", held)
        self.reply(200)


if __name__ == "__main__":
    print("lock server on http://127.0.0.1:8765  (store: %s)" % STORE, flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
