# 导入Playwright的同步API模块
from playwright.sync_api import sync_playwright
# 使用Playwright的上下文管理器（自动管理资源）
with sync_playwright() as p:
    # 启动Chromium浏览器实例，设置headless=False表示显示浏览器界面
    browser = p.chromium.launch(headless=False)
    # 在浏览器中创建一个新页面/标签页
    page = browser.new_page()
    # 导航到目标网址
    page.goto('https://spa6.scrape.center/')
    # 等待页面达到"networkidle"状态（网络空闲，即没有正在进行的网络请求）
    page.wait_for_load_state('networkidle')
    # 获取当前页面的完整HTML内容（包含JavaScript渲染后的结果）
    html = page.content()
    # 打印获取到的HTML内容
    print(html)
    # 关闭浏览器实例
    browser.close()
# 上下文管理器结束时会自动清理Playwright资源