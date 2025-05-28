# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 11:17
# @Company : *********** @****.com
# @Function : 请输入模块功能描述
from DrissionPage import Chromium
browser = Chromium()
browser.set.retry_times(10)

tab = browser.latest_tab
# browser.quit()