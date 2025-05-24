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
a1.get('https://sahitest.com/demo/alertTest.htm')
a1.find_element(By.XPATH,'/html/body/form/input[1]').click()
a1.find_element(By.XPATH,'/html/body/form/input[1]').send_keys('alert')
a1.find_element(By.XPATH,'/html/body/form/input[2]').click()
time.sleep(1)
#获取弹窗内容
print(a1.switch_to.alert.text)
#点击弹窗确定按钮
a1.switch_to.alert.accept()

