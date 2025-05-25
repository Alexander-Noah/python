from playwright.sync_api import sync_playwright
import time  # 新增等待
import os  # 新增路径处理
import re
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 使用绝对路径更可靠
    html_path = os.path.abspath(os.path.join("selenium", "E:\java\python\days1\JavaScript动态页面爬取\selenium\测试.html"))


    def modify_response(route, request):
        try:
            # 用本地HTML文件替换响应
            route.fulfill(
                path=html_path,
                status=200,
                headers={"Content-Type": "text/html"}
            )
        except Exception as e:
            print(f"路由处理失败: {e}")
            route.continue_()  # 失败时继续原始请求


    # 更精确的路由匹配
    page.route(re.compile(r"https://spa6\.scrape\.center/?$"), modify_response)

    page.goto("https://spa6.scrape.center/")

    # 添加等待观察结果
    time.sleep(5)  # 暂停5秒查看页面
    page.screenshot(path="modified_page.png")  # 保存截图

    browser.close()
