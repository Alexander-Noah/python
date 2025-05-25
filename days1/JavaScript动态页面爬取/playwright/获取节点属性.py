# 导入Playwright的同步API模块
from playwright.sync_api import sync_playwright
# 使用Playwright的上下文管理器（自动资源清理）
with sync_playwright() as p:
    # 启动Chromium浏览器实例，headless=False表示显示浏览器窗口（可视化模式）
    browser = p.chromium.launch(headless=False)
    # 创建一个新的浏览器页面（相当于打开新标签页）
    page = browser.new_page()
    # 导航到目标网址（电影数据网站）
    page.goto('https://spa6.scrape.center/')
    # 等待页面加载到"networkidle"状态（所有网络请求完成）
    page.wait_for_load_state('networkidle')
    # 尝试获取<a>标签（class包含"name"）的href属性值
    href = page.get_attribute('a.name', 'href')
    # 打印获取到的href值
    print(href)
    # 关闭浏览器实例
    browser.close()