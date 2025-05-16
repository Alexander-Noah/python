import requests
from lxml import etree
from pyquery import PyQuery as pq
import csv

url='https://ssr1.scrape.center/'
headers = {
   " user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}
response = requests.get(url)
html= etree.HTML(response.text)
doc=pq(html)
title=html.xpath('/html/body/div/div[2]/div[1]/div[1]')[0]
movies=[]
for title in title:
    titles=title.xpath('.//div/div/div[2]/a/h2/text()')[0]
    # titles=etree.tostring(titles,encoding='utf-8').decode('utf-8')
    # titles = [title.strip() for title in titles]
    utl=title.xpath('.//div/div/div[2]/a/@href')
    url_one='https://ssr1.scrape.center'+utl[0]
    categories=title.xpath("//div[@class='categories']//button[@class='el-button category el-button--primary el-button--mini']/span/text()")[0]
    show= title.xpath('/html/body/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]')
    eg={
        'titles':titles,
        'utl':url_one,
        'categories':categories,
        'show':show,
    }
    movies.append(eg)

with open('movies.csv','w',encoding='utf-8')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(movies[0].keys())
    for movie in movies:
        writer.writerow(movie.values())






























