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
a1.get("https://www.baidu.com")
#浏览器打开位置
a1.set_window_position(0,0)
#浏览器打开尺寸
a1.set_window_size(1000,800)