# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/25 22:39
# @Company : 湖南信息职业技术学院 @hnuit.com
# @Function : gitee自动化登入
from DrissionPage import Chromium
#启动浏览器
tab = Chromium().latest_tab
#跳转到登入页面
tab.get('https://gitee.com/login')
#定位到账号输入框，获取文本框元素
ele = tab.ele('#user_login')
#对文本框输入账号
ele.input('19944744630')
#定位到密码框并输入密码
tab.ele('#user_password').input('20051002Zht')
#点击登入按钮
tab.ele('@commit').click()