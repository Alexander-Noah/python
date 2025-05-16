#获取属性
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# logo = browser.find_element(By.CLASS_NAME,'logo-image')
# print(logo)
# print(logo.get_attribute('src'))
#
# 获取文本值
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# input = browser.find_element(By.CLASS_NAME,'logo-title')
# print(input.text)

#获取id、位置、标签名、和大小
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
url= 'https://spa2.scrape.center/'
browser.get(url)
input=browser.find_element(By.CLASS_NAME,'logo-title')
print(input.id)#打印该元素的内部 ID（Selenium 分配给元素的唯一标识符）。
print(input.location)#打印该元素在页面中的位置（坐标），返回一个字典，包含 'x' 和 'y' 键，表示元素左上角相对于整个页面的坐标。
print(input.tag_name)#打印该元素的 HTML 标签名称（如 'div', 'a', 'img' 等）
print(input.size)#打印该元素的大小，返回一个字典，包含 'width' 和 'height' 键，表示元素的宽度和高度（以像素为单位）。