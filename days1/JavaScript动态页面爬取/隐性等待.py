from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def she():
    browser=Options()
    browser.add_argument('--no-sandbox')
    browser.add_experimental_option('detach',True)
    browser1 = webdriver.Chrome(service=Service(r'D:\chrome\chromedriver-win64\chromedriver.exe'),options=browser)
    return browser1
a1=she()
# a1.get('https://ssr4.scrape.center/')
a1.get('https://www.baidu.com/')
#元素定位隐形等待（多少秒内找到元素就立刻执行，没有找到元素就报错
# a1.implicitly_wait(10)
# a2=a1.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/a').click()
a2=a1.find_element(By.ID,'kw').send_keys('selenium')
a3=a1.find_element(By.ID,'su').click()
a1.implicitly_wait(5)
a4 = a1.find_element(By.CSS_SELECTOR, ".cosc-title-a.cos-link.cosc-title-md").click()