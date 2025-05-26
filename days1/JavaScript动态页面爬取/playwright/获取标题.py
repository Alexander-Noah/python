# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/25 14:44
# @Company : 湖南信息职业技术学院 @hnuit.com
# @Function : 获取哔哩哔哩网页页面的标题文本
#导包
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.bilibili.com/')
    print(page.title())
    browser.close()