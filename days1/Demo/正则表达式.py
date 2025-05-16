# import re
# content='https://www.baidu.com 643 432 hwllowqkdnd 15864956556'
# print(len(content))
# result = re.match(r'^[a-zA-z]+://[^\s]*\s\d{3}\s\d\d\d\s\w*\s\d{11}$',content)
# print(result)
# print(result.group())
# print(result.span())
# import re
# content = 'Hello 123456 World_This is a Demo'
# result = re.match(r'^Hello\s(\d+)\s\w.*Demo$',content)
# result = re.match(r'^Hello.*?(\d+)\s.*?Demo$',content)#非贪婪匹配
# result = re.match(r'^Hello.*(\d+).*Demo$',content)#贪婪匹配
# content = ('Hello 123456 World_This is a Regex Demo\n')
# result = re.match(r'^He.*?(\d+).*?Demo\n$',content,re.S)#匹配特殊字符
# print(result)
# print(result.group(1))
# print(result.span())

#re.search方法
# import re
# content = 'Hi my name is nuosi I like python Hello python 123456789 is a Demo\n'
# result = re.search(r'He.*?(\d+).*?Demo\n',content,re.S)
# print(result)
# print(result.group(1))
# print(result.span())
import requests
import re
import urllib.request
url="https://ssr1.scrape.center/"
response = requests.get(url)
html = response.text
# def get_one_shit(html):
#     for i in range(10):
results = re.findall(r'<img\s.*?>', html, re.I | re.S)
    # print(result.group())
# print(result)
# print(result.group())
# print(result.span())
# # print(html)
# def main():
#     html = response.text
#     get_one_shit(html)
#
# if __name__=='__main__':
#     main()
print(results)
print(type(results))
# for result in results:
# print(result[0], result[1], result[2])
# print(result)