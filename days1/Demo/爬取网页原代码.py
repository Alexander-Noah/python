import urllib.request;
response=urllib.request.urlopen('https://ssr1.scrape.center/');
print(response.read().decode('utf-8'));