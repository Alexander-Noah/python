import urllib.request
url="https://www.hnu.edu.cn/xyxk/xkzy/zylb.htm"
r=urllib.request.Request(url)
print(type(r))