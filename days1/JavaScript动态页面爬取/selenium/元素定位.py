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
a1.get('https://www.baidu.com')
#元素定位-CSS_SELECTOR
#1，#id = 井号+id值 通过id定位
# 2，.class = 点+class值 通过class定位
#3，不加修饰符=标签头通过标签头定位
#4，通过任意类型定位："[类型='精准值']"
#5，通过任意类型定位："［类型*=‘模糊值'］"
#6，通过任意类型定位：＂[类型^='开头值']"
#7，通过任意类型定位："[类型$＇结尾值']"

#以上这些方法都属于理论定位法
#8，更简单的定位方式：在谷歌控制台直接复制  SELECTOR    (个别元素定位值会比较长)
a2=a1.find_element(By.CSS_SELECTOR,'a').click()
a3=a1.find_element(By.NAME,'q')
s4=a1.find_element(By.ID,'wk')
a5=a1.find_element(By.TAG_NAME,'span')#同css定位一样寻找标签头定位
a6=a1.find_element(By.CLASS_NAME,'bw')
#元素定位-LINK_TEXT
#通过精准链接文本找到标签a的元素
#有重复的文本，需要切片
a7=a1.find_element(By.LINK_TEXT,'nk').click()#元素定位 ,文本链接
#元素定位-PARTIAL_LINK_TEXT
#通过模糊链接文本找到标签a的元素[模糊文本定位]
#有重复文本，需要切片
a8=a1.find_element(By.PARTIAL_LINK_TEXT,'图').click()

#元素定位XPTH
#1,复制谷歌浏览器Xpath（通过属性+路径定位，属性如果是随机的，可能定位不到）
#1,复制谷歌浏览器完整Xpath（缺点是定位值比较长，有点是基本100%准确）
a9=a1.find_element(By.XPATH,'//*[@id="kw"]')
print(a2)

