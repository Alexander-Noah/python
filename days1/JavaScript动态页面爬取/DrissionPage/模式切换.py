# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 08:36
# @Company : 湖南信息职业技术学院 @hnuit.com
# @Function : 切换模式是用来应付登录检查很严格的网站，
# 可以用浏览器处理登录，
# 再转换模式用收发数据包的形式来采集数据。
from DrissionPage import Chromium
tab = Chromium().latest_tab
tab.get('https://gitee.com/explore/all')
tab.change_mode()
items = tab.ele('.ui relaxed divided items explore-repo__list').eles('.item')
for item in items:
    print(item('t:h3').text)
    print(item('.project-desc mb-1').text)
    print()