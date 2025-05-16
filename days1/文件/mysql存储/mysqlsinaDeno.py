import requests
from lxml import etree
import pymysql

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
cookies = {
    "_s_tentry": "cn.bing.com",
    "UOR": "cn.bing.com,s.weibo.com,cn.bing.com",
    "Apache": "566194259143.7108.1743766694172",
    "SINAGLOBAL": "566194259143.7108.1743766694172",
    "ULV": "1743766694189:1:1:1:566194259143.7108.1743766694172:",
    "SCF": "Apd6xwq_HSTENcNBZyMCQWCWt0e-jhvCxy2Is7tgyKJOW5BxxMpc3qC9rabEget7eEdP6SUZz5-gA28HIgpd7rY.",
    "SUB": "_2A25K67fmDeRhGeBG7VEY8CzIwzuIHXVpiLUurDV8PUNbmtB-LWTHkW9NRhFIhpasGgmJPrKHecZUTsoJWCENTRU-",
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WWyDY.uZ72nN41pvF_zYmTR5NHD95Qc1hq01K5EShnNWs4Dqcjni--ciKLsi-8si--ci-88i-zfi--Ni-2NiKyFShq41K-t",
    "ALF": "02_1746359478"
}
url = "https://s.weibo.com/top/summary?display=0&retcode=6102#39"
response = requests.get(url, headers=headers, cookies=cookies)

saad = etree.HTML(response.text)
trs = saad.xpath('//table/tbody/tr')[1:]

try:
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='sinahot')
    cursor = db.cursor()
    for tr in trs:
        event = tr.xpath('./td[2]/a/text()')[0]
        Urls = tr.xpath('./td[2]/a/@href')
        hot_elements = tr.xpath('./td[2]/span[1]/text()')
        hot = hot_elements[0] if hot_elements else "0"
        weibo = 'https://s.weibo.com' + Urls[0]
        weibo1 = 'https://s.weibo.com' + ''.join(Urls)

        data = {
            "id": event,
            "hots": hot,
            "Link": weibo1
        }
        table = 'hot1'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'
        try:
            if cursor.execute(sql, tuple(data.values())):
                print("Successfully inserted a record.")
                db.commit()
        except pymysql.Error as e:
            print(f"Database insert operation failed: {e}")
            db.rollback()
except pymysql.Error as e:
    print(f"Database connection failed: {e}")
finally:
    if 'db' in locals() and db.open:
        db.close()