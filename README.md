# A-simple-HTTP-SERVER
Title: Display request values in a debug page

Description:
Extend the server to render a debug HTML page showing various request-related values: current date and time, client host and port, request command (e.g., GET), and requested path.

Tasks:


Add a function create_page() that returns HTML containing a table of request-specific values (datetime, client IP, port, command, path).

Refactor do_GET to call create_page() and pass the generated content to a helper send_page(page).

Implement send_page(page, status=200) to send HTTP headers and body correctly.

(Optional) Add a simple manual test or unit test to verify that the fields are correctly shown in the HTML.
Acceptance Criteria:

A GET request to any path returns an HTML page showing a table of request values.
The response uses Content-Type: text/html and Content-Length headers correctly.
The page displays correct values for date/time, client address, request method, and path
