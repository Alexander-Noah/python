# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 09:03
# @Function : 京东登入
from DrissionPage import Chromium
# 创建页面对象
tab = Chromium().latest_tab
# 访问个人中心页面（未登录，重定向到登录页面）
tab.get('https://www.jd.com/')
# tab.ele('.no_login_btn').click()
# tab.ele('@id:pwd-login').click()
# # 输入账号密码登录
# tab.ele('@id:loginname').input('16681317432')
# tab.ele('@id:nloginpwd').input('20051002Zht\n')
tab.wait.load_start()

# 切换到 s 模式
tab.change_mode()
# 登录后 session 模式的输出
print('登录后title：', tab.title, '\n')
tab.ele('.text')
tab.ele('.button').click()
tab.wait.load_start()