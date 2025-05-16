from selenium.webdriver.common.by import By
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')#打开页面
input = browser.find_element(By.ID,'q')
input.send_keys('iPhone')#搜索iPhone
time.sleep(10)#等待2秒
input.clear()#清空输入框
input.send_keys('iPad')#搜索iPad
button = browser.find_element(By.CLASS_NAME,'btn-search')#获取搜索按钮
button.click()#关闭