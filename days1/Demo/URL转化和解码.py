#url转换
# from urllib.parse import quote
# keyword='壁纸'
# url = 'http://www.baidu.com/s?wd='+quote(keyword)
# print(url)


#URL解码
from urllib.parse import unquote
url='https ://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))