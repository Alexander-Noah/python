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

for i in range(1,3):
    a1=she()
    a1.get('E:\java\python\days1\JavaScript动态页面爬取\测试.html')
    a2=a1.find_element(By.XPATH,'/html/body/form/div[1]/div[2]/label[2]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[2]/div[2]/label[1]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[2]/div[2]/label[2]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[2]/div[2]/label[3]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[3]/select/option[3]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[4]/input').send_keys("002025-10-02")
    a2=a1.find_element(By.XPATH,'/html/body/form/div[5]/div[2]/div[1]/div[2]/span[5]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[5]/div[2]/div[2]/div[2]/span[5]').click()
    a2=a1.find_element(By.XPATH,'/html/body/form/div[6]/div[2]/input').send_keys(r'E:\java\python\days1\JavaScript动态页面爬取\1.png')
    a2=a1.find_element(By.XPATH,'/html/body/form/button').click()
    a2=a1.window_handles
    print(a2)
    time.sleep(3)
    a2=a1.find_element(By.XPATH,'/html/body/div/div[3]/a[2]').click()
    a1.close()
