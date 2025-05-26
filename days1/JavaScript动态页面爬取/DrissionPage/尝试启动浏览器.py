# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/25 22:31
# @Company : 湖南信息职业技术学院 @hnuit.com
# @Function : 浏览器启动尝试
from DrissionPage import Chromium
tab = Chromium().latest_tab
tab.get('https://DrissionPage.cn')