# -*- coding: utf-8 -*-
# @Author : zheng
# @Time : 2025/5/26 07:58
# @Company : 湖南信息职业技术学院 @hnuit.com
# @Function : 用SessionPage已收发数据包的方式采集 gitee 网站数据
#导入用于收发数据包的页面类SessionPage
from DrissionPage import SessionPage
#构建SessionPage对象
page = SessionPage()
#遍历循环3次构造每页的url，每次使用get方法访问
for i in range(1,4):
    page.get('https://gitee.com/explore/all?order=starred&page={i}')
    links = page.eles('.title project-namespace-path')
    #遍历获取文本和链接
    for link in links:
        print(link.text,link.link)