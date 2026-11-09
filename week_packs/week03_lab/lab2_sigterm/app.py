import http.server
import socketserver
import time


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/work":
            time.sleep(5)  # an in-flight request that a graceful stop must let finish
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"done\n")


print("listening on 8080")
server = socketserver.ThreadingTCPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
