import urllib.request
response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=10)
print(response.read())