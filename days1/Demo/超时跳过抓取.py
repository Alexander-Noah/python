import socket;
import urllib.request;
import urllib.error;
try:
    response = urllib.request.urlopen('https://www.httpbin.org/get',timeout=0.1);
except urllib.error.URLError as e:
    if(isinstance(e.reason,socket.timeout)):
       print('TIME OUT');
       # 这里我们请求了https: // www.httpbin.org / get
       # 这个测试链接，设置超时时间为0.1秒，然后捕获到URLError这个异常，并判断异常类型是socket.timeout，意思是超时异常，
       # 因此得出确实是因为超时而报错的结论，最后打印输出了TIMEOUT。