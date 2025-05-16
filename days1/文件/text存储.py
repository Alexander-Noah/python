# import requests
# from lxml import etree
#
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Cache-Control": "max-age=0",
#     "Connection": "keep-alive",
#     "Referer": "https://scrape.center/",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
#     "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\""
# }
# url = "https://ssr2.scrape.center/"
# response = requests.get(url, headers=headers)
# html = etree.HTML(response.text)
# movietitle=html.xpath('//div[@class="el-card item m-t is-hover-shadow"]/div/div/div[2]/a/h2')
# link=html.xpath("//a[@class='name']/@href")
# print(movietitle)
# print(link)
import requests
from lxml import etree
from pyquery import PyQuery as pq
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
base_domain = 'https://movie.douban.com/top250'
next_page_url = '?start=0&filter='  # 初始页面路径

while next_page_url:
    full_url = base_domain + next_page_url
    response = requests.get(full_url,headers=headers)
    html = etree.HTML(response.text)
    # print(response.text)
    # 解析当前页数据
    print(f'正在抓取: {full_url}')
    # 此处添加页面解析逻辑
    title=html.xpath("""(//ol[@class='grid_view']/li//div[@class='info']/div[@class='hd']/a/span[1]/text())""")
    url = html.xpath('//div[@class="hd"]/a/@href')[0]
    print(title)
    print(url)
    # 获取下一页路径
    next_btn = html.xpath('//span[@class="next"]/a/@href')
    # next_page_url = next_btn.attr('href') if next_btn else None
    next_page_url = next_btn[0] if next_btn else None

    # 防止死循环
    if next_page_url == full_url:
        break