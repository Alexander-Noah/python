# 导入Playwright的同步API
from playwright.sync_api import sync_playwright
# 使用sync_playwright上下文管理器，自动处理初始化和清理
with sync_playwright() as p:
    # 遍历三种浏览器类型：Chromium、Firefox和WebKit
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # 启动浏览器实例（非无头模式，即显示浏览器窗口）
        browser = browser_type.launch(headless=False)
        # 在浏览器中新建一个页面/标签页
        page = browser.new_page()
        # 导航到百度首页
        page.goto('https://www.baidu.com')
        # 截取页面截图，并以浏览器类型命名文件
        # 生成的文件名如：screenshot-chromium.png、screenshot-firefox.png等
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        # 打印当前页面的标题（浏览器标签页上显示的标题）
        print(page.title())
        # 关闭浏览器实例
        browser.close()