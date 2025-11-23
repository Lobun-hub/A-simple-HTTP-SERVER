Purpose
This file tells AI coding agents how to be productive in this repository.

Repository snapshot
- Name: `A-simple-HTTP-SERVER`
- Branch: `main`
- Key files: `hello.py` (currently empty), `README.md` (title only)

Big picture (what I can assume from the repo)
- This repository is a minimal, single-file Python HTTP server project. At present there is no implementation in `hello.py` and the `README.md` only contains the project title.
- Design intent: keep changes small and self-contained. The project appears to favour a tiny, single-file server rather than a multi-module package.

Immediate developer workflows
- Run locally: if `hello.py` is implemented, run with `python hello.py` (Windows: `py -3 hello.py`).
- Debug: use `python -m pdb hello.py` or run the file inside an IDE debugger. For quick logging, write to stdout (the project has no logging framework yet).

Project-specific conventions and expectations for AI agents
- Minimal changes: prefer small, incremental edits and open a quick PR for review. Do not bootstrap a full package layout unless the user asks.
- Entrypoint: add a guarded entrypoint when implementing: `if __name__ == "__main__":` and keep the server startup logic under a small function (e.g., `main()`).
- Configuration: prefer environment variables for port/config (example: `PORT = int(os.environ.get('PORT', '8000'))`) to keep the server container-friendly.
- Dependencies: this repo currently has none. If you add third-party packages, also add a `requirements.txt` (or `pyproject.toml`) and update `README.md` run instructions.

Patterns and examples (recommended, minimal)
- Recommended server layout (small, single-file pattern):

  - Define a handler function or class near top of `hello.py`.
  - Provide a `main()` that reads `PORT` from environment, binds to `0.0.0.0`, and starts the server.

  Example (recommended minimal pattern to use as a template):

  ```py
  import os
  from http.server import HTTPServer, BaseHTTPRequestHandler

  class Handler(BaseHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-Type', 'text/plain; charset=utf-8')
          self.end_headers()
          self.wfile.write(b'Hello\n')

  def main():
      port = int(os.environ.get('PORT', '8000'))
      server = HTTPServer(('0.0.0.0', port), Handler)
      print(f"Listening on 0.0.0.0:{port}")
      server.serve_forever()

  if __name__ == '__main__':
      main()
  ```

What to change in this repo (rules for agents)
- If implementing `hello.py`, add unit tests only if the user asks — the repository currently has no test harness.
- When you modify or add dependencies, update `README.md` with run and install instructions.
- Keep changes focused: prefer a single commit that implements a minimal server and README update rather than a large refactor.

Integration points and external dependencies
- None currently. If you expose an HTTP endpoint, document the port and any expected paths in `README.md`.

PR and review guidance for generated changes
- Small PRs: include a short description, list changed files (`hello.py`, `README.md`, optionally `requirements.txt`).
- Include a one-line run example in the PR body (e.g., `python hello.py` or `PORT=8080 python hello.py`).

If anything here is ambiguous or you want the repo to be converted into a package structure, ask the maintainer before changing the layout.

Notes for humans
- `hello.py` is empty today. Before implementing non-trivial features, confirm desired behaviour (static response vs. proxy vs. app server).

Request for feedback
- If any of the conventions above are wrong or you'd like the repo expanded into a package, tell me which direction to take and I'll update this file.
