from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import random
import numpy as np


def init_stealth_browser():
    """初始化隐藏自动化特征的浏览器"""
    options = Options()

    # 基本配置
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')

    # 随机User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    # 隐藏自动化特征
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # 初始化浏览器
    driver = webdriver.Chrome(
        service=Service(r"D:\chrome\chromedriver-win64\chromedriver.exe"),
        options=options
    )

    # 注入JavaScript隐藏WebDriver特征
    with open('stealth.min.js', 'r') as f:
        js = f.read()
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})

    return driver


def human_like_drag_and_drop(driver, slider, track):
    """模拟人类滑动滑块"""
    action = ActionChains(driver)
    action.click_and_hold(slider).perform()

    # 模拟人类滑动轨迹
    for x in track:
        action.move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(random.uniform(0.01, 0.05))

    # 小幅回滑模拟人类抖动
    action.move_by_offset(xoffset=-3, yoffset=0).perform()
    time.sleep(random.uniform(0.1, 0.3))
    action.move_by_offset(xoffset=3, yoffset=0).perform()

    # 释放滑块
    time.sleep(random.uniform(0.2, 0.5))
    action.release().perform()


def solve_slider_captcha(driver):
    """解决滑块验证码"""
    try:
        # 等待滑块元素加载
        slider = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.JDJRV-slide-inner.JDJRV-slide-btn'))
        )

        # 计算滑块轨道长度
        slider_bg = driver.find_element(By.CSS_SELECTOR, '.JDJRV-slide-inner.JDJRV-slide-bg')
        bg_width = slider_bg.size['width']

        # 生成滑动轨迹 (先快后慢)
        total_distance = bg_width - 10  # 留有余量
        track = []
        current = 0
        mid = total_distance * 0.7

        while current < total_distance:
            if current < mid:
                step = random.uniform(2, 5)
            else:
                step = random.uniform(0.5, 2)
            track.append(step)
            current += step

        # 执行滑动
        human_like_drag_and_drop(driver, slider, track)

        # 验证是否成功
        time.sleep(2)
        if '验证成功' in driver.page_source or 'passport.jd.com' not in driver.current_url:
            return True

        # 失败重试
        print("滑块验证失败，尝试再次滑动...")
        return False

    except Exception as e:
        print(f"滑块验证异常: {str(e)}")
        return False


def jd_login(driver, username, password, max_retry=3):
    """京东登录(带滑块验证处理)"""
    for attempt in range(max_retry):
        try:
            driver.get('https://passport.jd.com/new/login.aspx')

            # 切换到账号密码登录
            switch_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'login-tab-r'))
            )
            switch_btn.click()
            time.sleep(random.uniform(1, 2))

            # 输入用户名
            username_input = driver.find_element(By.ID, 'loginname')
            username_input.clear()
            for char in username:
                username_input.send_keys(char)
                time.sleep(random.uniform(0.1, 0.3))

            # 输入密码
            password_input = driver.find_element(By.ID, 'nloginpwd')
            password_input.clear()
            for char in password:
                password_input.send_keys(char)
                time.sleep(random.uniform(0.1, 0.3))

            # 点击登录
            login_btn = driver.find_element(By.ID, 'loginsubmit')
            login_btn.click()

            # 处理滑块验证码
            time.sleep(2)
            if '验证码' in driver.page_source:
                print("检测到滑块验证码，尝试自动解决...")
                if solve_slider_captcha(driver):
                    print("滑块验证成功!")
                else:
                    print("滑块验证失败，请手动完成验证")
                    input("手动完成验证后按回车键继续...")

            # 等待登录成功
            WebDriverWait(driver, 15).until(
                lambda d: 'www.jd.com' in d.current_url
            )
            print("登录成功!")
            return True

        except Exception as e:
            print(f"登录尝试 {attempt + 1}/{max_retry} 失败: {str(e)}")
            if attempt < max_retry - 1:
                time.sleep(random.uniform(3, 5))

    return False


# 使用示例
if __name__ == '__main__':
    # 初始化防检测浏览器
    driver = init_stealth_browser()

    try:
        # 京东登录
        if jd_login(driver, "你的京东账号", "你的密码"):
            # 登录成功后访问商品页
            product_url = 'https://item.jd.com/100143658518.html'
            driver.get(product_url)

            # 确保进入商品页
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'detail'))
            )
            print("成功访问商品页面!")

            # 这里可以添加爬取评论的代码
            # ...

        else:
            print("登录失败，请检查账号或手动登录")

        # 保持浏览器打开
        input("按回车键退出...")

    finally:
        driver.quit()