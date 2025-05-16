from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID,'q')#ID属性
input_second = browser.find_element(By.CSS_SELECTOR,'#q')#CSS选择器
input_third = browser.find_element(By.XPATH,'//*[@id="q"]')#XPATH
print(input_first,input_second,input_third)
browser.close()