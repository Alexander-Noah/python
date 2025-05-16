import requests
from lxml import etree
import csv
from days1.文件.csv文件存储.moviescsv文件存储Demo import movies

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "bid": "Nms_aH8Azy0",
    "_pk_id.100001.4cf6": "b57b15780b05354b.1744706475.",
    "_pk_ses.100001.4cf6": "1",
    "ap_v": "0,6.0",
    "__utma": "223695111.996073787.1744706475.1744706475.1744706475.1",
    "__utmb": "223695111.0.10.1744706475",
    "__utmc": "223695111",
    "__utmz": "223695111.1744706475.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "__yadk_uid": "caqAAFzRgfgN65BoZwEDCH5j9oJ5HbcH"
}


def set_html():
    host = []
    for i in range(0, 250, 25):
        url_html = f'https://movie.douban.com/top250?start={i}&filter='
        response = requests.get(url=url_html, headers=headers, cookies=cookies)
        html = etree.HTML(response.text)
        movies = html.xpath('//div[@id="wrapper"]/div/div/div/ol/li')

        for movie in movies:
            try:
                title1 = movie.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
                title2 = movie.xpath('.//div[@class="hd"]/a/span[2]/text()')
                title2 = title2[0].replace('\xa0', '') if title2 else ''
                title3 = movie.xpath('.//div[@class="hd"]/a/span[3]/text()')
                title3 = title3[0].replace('\xa0', '') if title3 else ''
                direct = movie.xpath('.//div[@class="bd"]/p[1]/text()')[0]
                direct = direct.replace('\xa0', '').strip()
                score = movie.xpath('.//div[@class="bd"]/div/span[@class="rating_num"]/text()')[0]
                protagonist = movie.xpath('.//div/div[2]/div[2]/p[2]/span/text()')
                protagonist = protagonist[0] if protagonist else ''
                href = movie.xpath('.//div[@class="hd"]/a/@href')[0]
                eg = {
                    'title': title1,
                    'title2': title2,
                    'title3': title3,
                    '导演和主演': direct,
                    '评分': score,
                    'protagonist': protagonist,
                    '链接': href,
                }
                host.append(eg)
            except IndexError:
                print(f"提取 {href} 数据时出错，可能页面结构有变化。")
    return host


def save_to_csv(data, filename='douban_top250.csv'):
    fieldnames = ['title', 'title2', 'title3', '导演和主演', '评分', 'protagonist', '链接']
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    movies = set_html()
    save_to_csv(movies)


if __name__ == '__main__':
    main()
