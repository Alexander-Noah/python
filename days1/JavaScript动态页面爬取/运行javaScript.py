from time import sleep
from selenium import webdriver;
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")#javascript到底部
browser.execute_script('alert("To Bottom")')#弹窗提示
sleep(5)#5秒后关闭