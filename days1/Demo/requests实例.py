# import requests
# r=requests.get('https://www.baidu.com/')
# print(type(r))#响应类型
# print(r.status_code)#状态码
# print(type(r.text))#响应体类型
# print(r.text[:100])#内容
# print(r.cookies)#Cookie
# import requests
#
# r = requests.get('https://scrape.center/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
import requests
response = requests.get('https://ssr4.scrape.center/')
print(response.text)
print(response.headers)
print(response.status_code)
print(response.cookies)
# def parse_one_page(html):
#     pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#                          +'.*?>(.*?)</a>*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#                           +'.*?integer">(.*?)</i>*?fraction">(.*?)</i>*?</dd>',re.S)
#     items=re.findall(pattern,html)
#     print(items)
