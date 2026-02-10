from http.server import HTTPServer, SimpleHTTPRequestHandler

# Serve a single request for demo
server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
print("Serving at http://localhost:8000 (one request)")
server.handle_request()
