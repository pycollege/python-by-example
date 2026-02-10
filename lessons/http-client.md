# Python by Example: HTTP Client

Fetching URLs is common—APIs, web scraping, downloads. The built-in `urllib.request` works without extra packages. Use `urlopen()` to get a response; read the body with `.read()`. For simpler APIs, the `requests` library is popular—it handles encoding, JSON, and sessions with less code.

**What you'll learn:**
- Using `urllib.request.urlopen()`
- Reading the response body

```python
from urllib.request import urlopen

# Fetch a URL (example uses a simple public API)
with urlopen("https://httpbin.org/get") as response:
    body = response.read().decode()
    print(body[:200] + "...")
```

`urlopen` returns a file-like object. `.read()` gives bytes; `.decode()` converts to a string. The `with` block ensures the connection is closed.

To run this program:

```bash
$ python source/http-client.py
{"args": {}, "headers": {"Accept-Encoding": "identity", ...
```

**Tip:** For JSON responses, use `json.loads(response.read().decode())`. With `requests`, it's `response.json()`.

**Try it:** Fetch a different URL (e.g., https://example.com) and print the first 500 characters.

Source: [http-client.py](../source/http-client.py)

Next: [HTTP Server](http-server.md)
