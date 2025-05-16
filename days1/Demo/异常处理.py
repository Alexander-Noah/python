# from urllib import request,error
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.URLError as e:
#     print(e.reason)
#http异常处理
# from urllib import request,error
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')
#改良版
# from urllib import request,error
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfilly')
#强制抛出timeout异常
import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('https:baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')