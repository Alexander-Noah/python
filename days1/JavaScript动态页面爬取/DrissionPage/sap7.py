# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/27 21:15
# @Company : *********** @****.com
# @Function : 请输入模块功能描述
import urllib.parse
from DrissionPage import Chromium
tab = Chromium().latest_tab
tab.set.load_mode.none()
tab.get('https://spa7.scrape.center/')
response = tab.eles('.:el-col el-col-24 el-col-xs-24 el-col-sm-12 el-col-md-12 el-col-lg-6')
for item in response:
    print(item.text)
    img_src = item.ele('.:image')
    img = img_src.attr('src')
    print(img)