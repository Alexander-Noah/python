from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
def she():
    browser=Options()#创建设置浏览器对象
    browser.add_argument('--no-sandbox')#禁用沙盒模式
    browser.add_experimental_option('detach',True)#保持浏览器打开状态（默认是代码执行完毕自动关闭）
    browser1=webdriver.Chrome(service=Service(r"D:\chrome\chromedriver-win64\chromedriver.exe"),options=browser)
    browser1.implicitly_wait(10)
    return browser1
a1=she()
a1.get('https://www.news.cn/world/20250522/2080df2308ab432fba95679a5c01c482/c.html')
time.sleep(2)
#获取文本
a2=a1.find_element(By.XPATH,'/html/body/div[11]/div/div[1]/span').text
print(a2)
time.sleep(2)
#内容是否可见
a2=a1.find_element(By.XPATH,'/html/body/div[11]/div/div[1]/span').is_displayed()
print(a2)