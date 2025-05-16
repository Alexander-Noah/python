import requests
from lxml import etree
import csv

def set_data(url):
    url=url
    response = requests.get(url)
    html=etree.HTML(response.text)
    links=html.xpath('//div[2]/a/@href')
    new_urls = []
    host=[]
    for link in links:
        # 将每个提取到的链接与/detail/1组合
        new_url = 'https://ssr1.scrape.center' + link
        new_urls.append(new_url)
        print(new_url)
        resp = requests.get(new_url)
        html=etree.HTML(resp.text)
        title = html.xpath('//div/div[2]/a/h2/text()')[0]#提取标题
        type=html.xpath('//div/div[2]/div//button/span/text()')[:-1]#提取类别
        form = html.xpath('//div/div[2]/div[2]/span[1]/text()')#提取地点
        time = html.xpath('//div/div[2]/div[2]/span[3]/text()')#提取上映时间
        page=html.xpath('//div[2]/div[4]/p/text()')#提取简介
        eg={
            '标题':title,
            '类别':type,
            '地点':form,
            '时长':time,
            '简介':page,
        }
        host.append(eg)
        print(host[-1])
    return host

def main():
    all_data=[]
    for i in range(1,11,1):
        url='https://ssr1.scrape.center/page/{i}'.format(i=i)
        data=set_data(url)
        all_data.extend(data)
    fieldnames = ['标题','类别','地点','时长','简介']
    with open('dict.csv','w',newline='',encoding='utf-8-sig')as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for row in all_data:
            writer.writerow(row)

if __name__ == '__main__':
    main()
