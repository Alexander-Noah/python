# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/27 19:28
# @Company : *********** @****.com
# @Function : 获取插件链接和title
import  urllib.parse
from DrissionPage import SessionPage

#创建页面对象
page = SessionPage()
for i in range(1,36):
    page.get(f'https://chrome.zzzmh.cn/extension?page={i}')
    #获取所有元素列表
    div_list=page.eles('.:col-md-12')
    # 遍历列表
    # print(tab)
    for div in div_list:
        title = div.ele('.:card-title').text
        url = div.ele('xpath:./a/@href')
        link = urllib.parse.urljoin('https://chrome.zzzmh.cn/',url)
        print(title)
        print(link)
