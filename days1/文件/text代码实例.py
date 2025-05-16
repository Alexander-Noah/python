import requests
from pyquery import PyQuery as pq
import re
url='https://ssr1.scrape.center/'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}
response  = requests.get(url,headers=headers)
html =response.text
doc = pq(html)
items = doc('.el-card').items()
file = open('movies.text','w',encoding = 'utf-8')#以写的方式打开文档
for item in items:
    name = item.find('a>h2').text()
    file.write(f'名称：{name}\n')#写入
    categories = [item.text()for item in item.find('.categories button span').items()]
    file.write(f'类别:{categories}\n')
    published_at = item.find('.info:contains(上映)').text()
    published_at = re.search(r'(\d{4}-\d{2}-\d{2})',published_at).group(1) if published_at and re.search(r'\d{4}-\d{2}-\d{2}',published_at) else None
    file.write(f'上映时间：{published_at}\n')
    score = item.find('p.score').text()
    file.write(f'评分：{score}\n')
    file.write(f'{"="*50}\n')
file.close()