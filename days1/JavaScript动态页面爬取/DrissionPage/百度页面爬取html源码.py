# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/27 19:10
# @Company : *********** @****.com
# @Function : 爬取百度搜索结果的html源码
from DrissionPage import Chromium
tab=Chromium().latest_tab
tab.get('https://www.baidu.com')
ele = tab.ele('#kw')
ele.input("唐艺渊")
tab.ele('#su').click()
print(tab.html)
