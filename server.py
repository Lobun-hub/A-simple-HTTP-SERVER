#!/usr/bin/env python3
"""
Basic HTTP Server  serves static files if they exist,
otherwise responds with a default HTML page.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import os

# Default HTML response template
PAGE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Welcome to our HTTP Server</h1>
    <p>Server started at {timestamp}</p>
</body>
</html>
"""

# HTTP request handler — processes GET requests
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Creating full path to requested file
        full_path = os.getcwd() + self.path

        #  check path and  serve it
        if os.path.isfile(full_path):
            with open(full_path, "rb") as f:   # read in binary mode
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Content-Type", self.guess_type(full_path))
            self.end_headers()
            self.wfile.write(content)
        else:
            # use  the default HTML page
            html = PAGE.format(timestamp=datetime.datetime.now())
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

# Main entry point starts the HTTP server
def main():
    port = int(os.environ.get('PORT', '8000'))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Listening on 0.0.0.0:{port}")
    server.serve_forever()

if __name__ == '__main__':
    main()
