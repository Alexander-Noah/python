# 导入Playwright同步API和正则模块
from playwright.sync_api import sync_playwright
import re
# 启动Playwright上下文管理器
with sync_playwright() as p:
    # 启动Chromium浏览器（可视化模式）
    browser = p.chromium.launch(headless=False)
    # 创建新页面
    page = browser.new_page()
    # 定义请求拦截函数
    def cancel_request(route, request):
        """拦截并中止图片请求"""
        route.abort()  # 中止当前请求
    # 使用正则匹配.png和.jpg结尾的URL，并注册拦截器
    page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
    try:
        # 导航到目标网站
        page.goto("https://spa6.scrape.center/")
        # 等待页面网络空闲状态
        page.wait_for_load_state('networkidle')
        # 保存页面截图（不含图片）
        page.screenshot(path='no_picture.png')
    except Exception as e:
        print(f"发生错误: {str(e)}")
    finally:
        # 确保浏览器关闭（手动关闭）
        browser.close()