from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element(By.CSS_SELECTOR,'#draggable')#拖曳节点
target = browser.find_element(By.CSS_SELECTOR,'#droppable')#拖曳目标节点
actions = ActionChains(browser)
actions.drag_and_drop(source,target)#声明拖曳对象和目标
actions.perform()#执行动作