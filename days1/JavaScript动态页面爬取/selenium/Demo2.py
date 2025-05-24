from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()#谷歌浏览器
# browser = webdriver.Firefox()#火狐浏览器
browser = webdriver.Edge()#ie浏览器
# browser = webdriver.Safari()#苹果浏览器

try:
    browser.get('https://www.baidu.com')#使用GET方法请求页面链接
    input = browser.find_element(By.ID,'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)#打印页面源代码
finally:
    browser.close()#关闭浏览器
