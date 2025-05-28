# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 11:34
# @Company : *********** @****.com
# @Function : 请输入模块功能描述
from DrissionPage import *
browser = Chromium()
tab1 = browser.latest_tab
tab1.get('https://DrissionPage.cn')
tab2 = browser.new_tab('https://www.baidu.com')
tab3 = browser.get_tab(title='DrissionPage')
