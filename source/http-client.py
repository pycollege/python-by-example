from urllib.request import urlopen

# Fetch a URL
with urlopen("https://httpbin.org/get") as response:
    body = response.read().decode()
    print(body[:200] + "...")
