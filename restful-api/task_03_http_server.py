#!/usr/bin/python3
"""
Simple API server using Python's http.server.

Endpoints:
- /        -> plain text: "Hello, this is a simple API!"
- /data    -> JSON: {"name": "John", "age": 30, "city": "New York"}
- /info    -> JSON: {"version": "1.0", "description": "..."}
- /status  -> plain text: "OK"
- others   -> 404 plain text: "Endpoint not found"
"""

import json
import http.server


PORT = 8000


class ApiHandler(http.server.BaseHTTPRequestHandler):
    """Handle GET requests for a tiny API."""

    def do_GET(self):
        """Route requests and return text or JSON responses."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(payload).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            body = json.dumps(payload).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

    def log_message(self, format, *args):
        """Disable default request logging to keep output clean."""
        return


def main():
    """Start the HTTP server on port 8000."""
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, ApiHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
