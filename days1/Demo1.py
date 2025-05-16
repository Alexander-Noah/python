import requests
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://accounts.douban.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}
cookies = {
    "ll": "\"118267\"",
    "bid": "pQcD9BzOawM",
    "viewed": "\"1422036\"",
    "ap_v": "0,6.0",
    "dbcl2": "\"288354835:zZkRyWxVujY\"",
    "ck": "NLRu",
    "push_noty_num": "0",
    "push_doumail_num": "0"
}

url='https://movie.douban.com/subject/1292052/'
response = requests.get(url, headers=headers, cookies=cookies)
html=etree.HTML(response.text)
direct = html.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[2]/a/text()')
scriptwriter = html.xpath('//div[@id="info"]//span[contains(., "编剧")]/following-sibling::span[1]/a/text()')
clean_writers = [w.strip() for w in scriptwriter if w.strip()]
actors = html.xpath('//div[@id="info"]//span[contains(., "主演")]/following-sibling::span[1]/a/text()')
clean_actors = [actor.strip() for actor in actors if actor.strip()]
eg={
    '导演': direct,
    '编剧': clean_writers,
    '主演': clean_actors,
}
print(eg)