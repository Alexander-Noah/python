import urllib.request#爬取源代码
response =urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(type(response))#响应头信息
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(response.status)#响应状态码
print(response.getheaders())
print(response.getheader('Server'))