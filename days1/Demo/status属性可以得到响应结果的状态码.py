import urllib.request
response = urllib.request.urlopen('https://ssr1.scrape.center/')
print(response.status)#输出状态码
print(response.getheaders())#输出响应头信息
print(response.getheader('Server'))
#；最后一个输出是调用getheader方法，并传人参数Server，获取了响应头中Server 的值，结果是nginx，意思为服务器是用Nginx搭建的。