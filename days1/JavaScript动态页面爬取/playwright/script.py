import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("黄景乐")
    page.get_by_role("button", name="百度一下").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="湖南景荣电力工程有限公司(公司) - 百度百科").click()
    page1 = page1_info.value
    page1.locator(".mainContent_qV1LO").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
