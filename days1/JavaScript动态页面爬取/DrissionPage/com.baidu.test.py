# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 10:54
# @Company : *********** @****.com
# @Function : 百度页面输入与搜索
from DrissionPage import Chromium
try:
    tab = Chromium().latest_tab
    tab.get('https://www.baidu.com/')
    ele = tab.ele('#kw')
    ele.input("DrissionPage")
    ele = tab.ele('#su')
    ele.click()
    links = tab.eles('tag:h3')
    for link in links:
        print(link.text)
except Exception as e:
    print(e)
