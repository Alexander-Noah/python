import urllib.request

proxies = {
  "http": "http://127.0.0.1:7897",
  "https": "http://127.0.0.1:7897",
}
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))