# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/27 08:03
# @Company : *********** @****.com
# @Function : 请输入模块功能描述
from DrissionPage import Chromium
browser = Chromium()
browser.new_tab('https://drissionpage.cn/')
tab = browser.get_tab(title='DrissionPage')
print(tab)


