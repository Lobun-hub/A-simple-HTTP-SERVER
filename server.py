#!/usr/bin/env python3
"""
Basic HTTP Server skeleton — listens on a port and responds with
a fixed HTML page. Python 3 only (uses http.server).
"""

# Import HTTP server components and utilities
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime  # For timestamp in the response
import os  # For reading environment variables (PORT)

# HTML response template with a placeholder for the current timestamp
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
        # Send HTTP 200 OK status
        self.send_response(200)
        # Set response content type to HTML
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        # End the header section
        self.end_headers()
        # Format the HTML template with the current timestamp
        html = PAGE.format(timestamp=datetime.datetime.now())
        # Send the HTML response body
        self.wfile.write(html.encode('utf-8'))


# Main entry point — starts the HTTP server
def main():
    # Read PORT from environment variable, default to 8000 if not set
    port = int(os.environ.get('PORT', '8080'))
    # Create and bind the HTTP server to 0.0.0.0 (listen on all interfaces)
    server = HTTPServer(('0.0.0.0', port), Handler)
    # Print the listening address and port
    print(f"Listening on 0.0.0.0:{port}")
    # Start the server and listen for requests indefinitely
    server.serve_forever()


if __name__ == '__main__':
    main()
