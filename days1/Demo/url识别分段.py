# from urllib.parse import urlparse
# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result))
# print(result)
#API用法
# from urllib.parse import urlparse
# result = urlparse('www.baidu.com/index.html;user?id=4#comment',scheme='https')
# print(result)


#urlsplit应用
# from urllib.parse import urlsplit
# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result)
# print(result.scheme,result[0])

#合成完整链接
# from urllib.parse import urlunsplit
# data = ['https','wwww.baidu.com','index.html','a=6','comment']
# print(urlunsplit(data))


#链接合并
from urllib.parse import urljoin
print(urljoin('https://www.baidu.com','FAQ.html'))
print(urljoin('https://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html','https://www.baidu.com/FAQ.html?question=2'))
print(urljoin('https://baidu.com?wd=abc','https;//cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com#comment','?category=2'))