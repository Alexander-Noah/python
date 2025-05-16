import requests
from lxml import etree
from pyquery import PyQuery as pq
import xlwt

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
def data_one_shia(url,sheet1,is_first_page):
    response = requests.get(url,headers = headers)
    html = etree.HTML(response.text)
    add= html.xpath('//ol/li/div/div[2]')
    moves=[]
    for i in add:
        title = i.xpath('.//div[1]/a/span[1]')
        url = i.xpath(".//div[1]/a/@href")
        eg={
            "title":title[0].text,
            "url":url[0]
        }
        moves.append(eg)
    print(moves)
    if is_first_page:
        keys = list(moves[0].keys())
        for col,key in enumerate(keys):
            sheet1.write(0,col,key)
    for row,moves in enumerate(moves,start=1 if is_first_page else sheet1.last_used_row+1):
        for col,key in enumerate(moves.keys()):
            sheet1.write(row,col,moves[key])
    return len(moves)


def main():
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('豆瓣排行版')
    is_first_page=True
    for i in range(0,250,25):
        base_domain = 'https://movie.douban.com/top250'
        next_page_url = '?start={}&filter='.format(i)
        url = base_domain + next_page_url
        print("正在爬取"+url)
        data_one_shia(url,sheet1,is_first_page)
        is_first_page = False
    workbook.save("豆瓣排行榜.xls")
    print("保存成功")
if __name__ == '__main__':
    main()






















































# import requests
# from lxml import etree
# import xlwt
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
# }
#
#
# def data_one_shia(url, sheet1, is_first_page):
#     response = requests.get(url, headers=headers)
#     html = etree.HTML(response.text)
#     items = html.xpath('//ol[@class="grid_view"]/li')  # 修正 XPath 匹配电影条目
#
#     moves = []
#     for item in items:
#         title = item.xpath('.//span[@class="title"][1]/text()')  # 提取主标题
#         url = item.xpath('.//div[@class="hd"]/a/@href')
#         if title and url:  # 检查是否提取到数据
#             eg = {
#                 "title": title[0],
#                 "url": url[0]
#             }
#             moves.append(eg)
#
#     # 只在第一页写入表头
#     if is_first_page:
#         keys = list(moves[0].keys()) if moves else []
#         for col, key in enumerate(keys):
#             sheet1.write(0, col, key)
#
#     # 写入数据
#     for row, move in enumerate(moves, start=1 if is_first_page else sheet1.last_used_row + 1):#sheet1最后一行加1
#         for col, key in enumerate(move.keys()):
#             sheet1.write(row, col, move[key])
#
#     return len(moves)  # 返回当前页的数据行数
#
#
# def main():
#     # 初始化 Excel
#     workbook = xlwt.Workbook()
#     sheet1 = workbook.add_sheet('豆瓣排行榜')
#     is_first_page = True
#
#     for i in range(0, 250, 25):
#         url = f'https://movie.douban.com/top250?start={i}&filter='
#         print(f"正在爬取: {url}")
#         data_one_shia(url, sheet1, is_first_page)
#         is_first_page = False  # 后续页面不写表头
#
#     workbook.save("豆瓣排行榜.xls")
#     print("数据保存成功！")
#
#
# if __name__ == '__main__':
#     main()