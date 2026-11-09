import http.server
import os

PORT = int(os.environ.get("PORT", "8080"))
DATA = "/app/data/visits.txt"


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        with open(DATA, "a") as f:
            f.write("visit\n")
        with open(DATA) as f:
            n = sum(1 for _ in f)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"visits={n} uid={os.getuid()}\n".encode())


print(f"listening on {PORT} as uid {os.getuid()}", flush=True)
http.server.HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
