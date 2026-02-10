# Python by Example: HTTP Server

The `http.server` module provides a simple HTTP server for development. It serves files from the current directory. Useful for testing static sites or sharing files on a local network. For production, use a proper server like gunicorn or uwsgi.

**What you'll learn:**
- Starting a basic HTTP server
- `SimpleHTTPRequestHandler` serves files

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Serve a single request for demo
server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
print("Serving at http://localhost:8000 (one request)")
server.handle_request()
```

The server binds to `localhost:8000`. `handle_request()` serves one request and exits. For a long-running server, use `server.serve_forever()`.

To run this program:

```bash
$ python source/http-server.py
Serving at http://localhost:8000 (one request)
```

**Tip:** Run `python -m http.server 8000` from a directory to serve files—no script needed. Press Ctrl+C to stop.

**Try it:** Change to `serve_forever()` and visit http://localhost:8000 in a browser. Serve a directory that has an `index.html`.

Source: [http-server.py](../source/http-server.py)

Next: [Random Numbers](random-numbers.md)
