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
