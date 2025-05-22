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
a1.get("https://sahitest.com/demo/iframesTest.htm")
#获取iframe元素
a2=a1.find_element(By.XPATH,'/html/body/iframe')
#进入iframe嵌套页面
a1.switch_to.frame(a2)
#进入iframe页面操作元素点击
time.sleep(3)
a1.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/a[1]').click()
