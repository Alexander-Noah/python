from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
lis = browser.find_elements(By.CSS_SELECTOR,'li')
print(lis)
browser.close()