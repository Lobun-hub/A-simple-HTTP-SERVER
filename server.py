from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import html

class DebugHandler(BaseHTTPRequestHandler):

    def create_page(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        client_ip = self.client_address[0]
        client_port = self.client_address[1]

        command = self.command          # GET, POST, etc.
        path = html.escape(self.path)   # Escape to avoid HTML issues

        html_page = f"""
        <html>
        <head><title>Debug Page</title></head>
        <body>
            <h2>Request Debug Information</h2>
            <table border="1" cellpadding="6">
                <tr><th>Field</th><th>Value</th></tr>
                <tr><td>Date & Time</td><td>{now}</td></tr>
                <tr><td>Client IP</td><td>{client_ip}</td></tr>
                <tr><td>Client Port</td><td>{client_port}</td></tr>
                <tr><td>Command</td><td>{command}</td></tr>
                <tr><td>Requested Path</td><td>{path}</td></tr>
            </table>
        </body>
        </html>
        """
        return html_page

    def send_page(self, page, status=200):
        page_bytes = page.encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page_bytes)))
        self.end_headers()

        self.wfile.write(page_bytes)

    def do_GET(self):
        page = self.create_page()
        self.send_page(page)


def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, DebugHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
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
    <h1>Welcome to HTTP SERVER</h1>
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
    port = int(os.environ.get('PORT', '8000'))
    # Create and bind the HTTP server to 0.0.0.0 (listen on all interfaces)
    server = HTTPServer(('0.0.0.0', port), Handler)
    # Print the listening address and port
    print(f"Listening on 0.0.0.0:{port}")
    # Start the server and listen for requests indefinitely
    server.serve_forever()

# Run the main function if this script is executed directly


if __name__ == '__main__':
    main()
