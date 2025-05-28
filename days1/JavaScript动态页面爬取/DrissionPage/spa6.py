# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/27 20:38
# @Company : *********** @****.com
# @Function : 爬取Ajax网页
from DrissionPage import Chromium
tab = Chromium().latest_tab
tab.set.load_mode.none()

for i in range(1,12):
    tab.listen.start('api/movie')#指定监听目标并启动监听
    tab.get(f"https://spa6.scrape.center/page/{i}")
    paket = tab.listen.wait()#等待数据包
    tab.stop_loading()#停止加载
    print(paket.response.body)#打印数据包正文
