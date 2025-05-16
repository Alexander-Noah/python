from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'#这里假设目标网站 https://httpbin.org/ 需要 Basic Auth 认证，用户名和密码均为 admin。
p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler =HTTPBasicAuthHandler(p)
opener =build_opener(auth_handler)
try:
 result = opener.open(url)
 html = result.read().decode('utf-8')
 print(html)
except URLError as e:
    print(e.reason)
