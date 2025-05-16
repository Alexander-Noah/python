from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service #用于管理谷歌驱动
def she():
    browser = Options()#创建设置浏览器对象
    browser.add_argument('--no-sandbox')#禁用沙盒模式
    browser.add_experimental_option('detach',True)#保持浏览器打开状态（默认是代码执行完毕自动关闭）
    browser1 = webdriver.Chrome(service=Service(r"D:\chrome\chromedriver-win64\chromedriver.exe"),options=browser)
    return browser1
a1=she()
#打开指导网址
a1.get("https://www.baidu.com")
time.sleep(2)
#浏览器最大化
a1.maximize_window()
# 浏览器最小化
time.sleep(2)
a1.minimize_window()
#关闭当前标签页
# a1.close()
#退出并释放驱动
# a1.quit()