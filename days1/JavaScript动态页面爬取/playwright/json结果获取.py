# 导入 Playwright 的同步 API
from playwright.sync_api import sync_playwright
# 定义响应处理函数
def on_response(response):
    # 检查 URL 是否包含 '/api/movie' 且状态码为 200
    if '/api/movie' in response.url and response.status == 200:
        # 打印 JSON 格式的响应内容
        print(response.json())
# 使用 Playwright 的上下文管理器
with sync_playwright() as p:
    # 启动 Chromium 浏览器（非无头模式，即显示浏览器界面）
    browser = p.chromium.launch(headless=False)
    # 创建一个新页面
    page = browser.new_page()
    # 监听页面的所有响应，并将它们传递给 on_response 函数处理
    page.on('response', on_response)
    # 导航到目标网站
    page.goto('https://spa6.scrape.center/')
    # 等待页面加载到网络空闲状态（确保所有请求完成）
    page.wait_for_load_state('networkidle')
    # 关闭浏览器
    browser.close()