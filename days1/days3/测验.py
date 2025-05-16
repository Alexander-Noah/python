from urllib.request import urlopen
response = urlopen('http://www.example.com')
html = response.read().decode('utf-8')
print(html)