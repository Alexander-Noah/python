import requests
from lxml import etree
import time
import csv

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


def get_html():
    host = []
    for i in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={i}&filter='
        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            html = etree.HTML(response.text)
            hrefs = html.xpath('//div[@class="hd"]/a/@href')
            time.sleep(2)

            for detail_url in hrefs:
                try:
                    responses = requests.get(detail_url, headers=headers, cookies=cookies)
                    responses.raise_for_status()
                    html = etree.HTML(responses.text)
                    moviename = html.xpath('//*[@id="content"]/h1/span[1]/text()')
                    year = html.xpath('//*[@id="content"]/h1/span[2]/text()')
                    direct = html.xpath(
                        '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/span[2]/a/text()')
                    scriptwriter = html.xpath(
                        '//div[@id="info"]//span[contains(., "编剧")]/following-sibling::span[1]/a/text()')
                    clean_writers = [w.strip() for w in scriptwriter if w.strip()]
                    actors = html.xpath(
                        '//div[@id="info"]//span[contains(., "主演")]/following-sibling::span[1]/a/text()')
                    clean_actors = [actor.strip() for actor in actors if actor.strip()]
                    type = html.xpath('//span[@property="v:genre"]/text()')
                    fromt = html.xpath('//span[contains(text(),"制片国家/地区")]/following-sibling::text()[1]')
                    language = html.xpath('//span[contains(text(),"语言")]/following-sibling::text()[1]')
                    language = language[0].strip() if language else ''
                    release = html.xpath('//span[@property="v:initialReleaseDate"]/text()')
                    time1 = html.xpath('//span[@property="v:runtime"]/text()')
                    aliasname = html.xpath('//span[contains(text(),"又名")]/following-sibling::text()[1]')
                    number = html.xpath('//span[contains(text(),"IMDb")]/following-sibling::text()[1]')
                    mark = html.xpath('//strong[@property="v:average"]/text()')
                    abstract = html.xpath('//span[@property="v:summary"]/text()')
                    abstract = ''.join(abstract).strip()

                    eg = {
                        '电影名': ''.join(moviename),
                        '年份': ''.join(year),
                        '导演': direct,
                        '编剧': clean_writers,
                        '主演': clean_actors,
                        '类型': ', '.join(type),
                        '地区': ''.join(fromt),
                        '语言': language,
                        '上映日期': ', '.join(release),
                        '片长': ''.join(time1),
                        '又名': ''.join(aliasname),
                        'number': ''.join(number),
                        '评分': ''.join(mark),
                        '简介': abstract,
                    }
                    host.append(eg)
                except requests.RequestException as e:
                    print(f"请求详情页 {detail_url} 时出错: {e}")
        except requests.RequestException as e:
            print(f"请求列表页 {url} 时出错: {e}")
    return host


def save_to_csv(data, filename='movies.csv'):
    fieldnames = ['电影名', '年份', '导演', '编剧', '主演', '类型', '地区', '语言', '上映日期', '片长', '又名',
                  'number', '评分', '简介']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"数据已成功保存到 {filename}")
    except Exception as e:
        print(f"保存数据到 {filename} 时出错: {e}")


def main():
    namenas = get_html()
    for movie in namenas:
        print(movie)
    save_to_csv(namenas)


if __name__ == '__main__':
    main()
