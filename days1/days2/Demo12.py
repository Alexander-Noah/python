# from lxml import etree
# import requests
# url="https://ssr1.scrape.center/page/4"
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                  '(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
#     }
# response = requests.get(url,headers=headers)
# # print(response.text)
# print(response.status_code)
# html = etree.HTML(response.text)
# div = html.xpath('//h2/text()')
# for div in div:
#     # DIV = etree.tostring(div,encoding='utf8').decode('utf8')
#     print(div)
#     print("*"*50)



import chardet,requests
proxies = {
  "http": "http://127.0.0.1:7897",
  "https": "http://127.0.0.1:7897",
}
headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}
url='https://movie.douban.com/top250'
response  = requests.get(url,proxies=proxies,headers=headers)
result = chardet.detect(response.content)

html_content = response.content.decode('utf-8')
print(result['encoding'])
print(response.status_code)
print(response.text)




















