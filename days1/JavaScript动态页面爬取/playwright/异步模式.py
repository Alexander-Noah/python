# 导入异步库
import asyncio
# 导入Playwright的异步API（注意这里是async_api）
from playwright.async_api import async_playwright
# 定义主异步函数
async def main():
    # 使用异步上下文管理器初始化Playwright
    async with async_playwright() as p:
        # 遍历三种浏览器引擎：Chromium/Firefox/WebKit
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # 启动浏览器实例（默认headless=True，无界面模式）
            browser = await browser_type.launch()
            # 创建一个新页面/标签页
            page = await browser.new_page()
            # 导航到百度首页（await等待页面加载完成）
            await page.goto('https://www.baidu.com')
            # 截取屏幕截图并保存
            # 文件名示例：screenshot-chromium.png
            await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            # 获取并打印页面标题（需await等待结果）
            print(await page.title())
            # 关闭浏览器实例
            await browser.close()
# 运行主函数（Python 3.7+的异步执行方式）
asyncio.run(main())