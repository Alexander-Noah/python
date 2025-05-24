from playwright.sync_api import sync_playwright
import json
import pandas as pd
import time

# —— 配置区 —— #
SKU_ID      = "100143658518"
PAGE_START  = 0
PAGE_END    = 5     # 抓取前 5 页（根据需要调整）
PAGE_SIZE   = 10

# ← 在这里粘入你从浏览器复制的京东登录 Cookie
JD_COOKIE   = "__jdv=76161171|direct|-|none|-|1747630928913; __jdu=17476309284212004349143; o2State={%22webp%22:true%2C%22avif%22:true}; areaId=18; ipLoc-djd=18-1482-0-0; PCSYCityID=CN_430000_430100_0; shshshfpa=a6953e61-d857-9c93-1c42-9ec05ad64319-1747630931; shshshfpx=a6953e61-d857-9c93-1c42-9ec05ad64319-1747630931; 3AB9D23F7A4B3C9B=EZ62H5CO4MQBBEW4O6P4XGTR7LX4Z7MU3O7CRGDIYH6JZA6YM2SYLXIOHXIKJ7MA3FPMFDYHCEVH3MJUBQEWIRELIM; unpl=JF8EAKBnNSttDUkAVhxVHEURTF5XW1pbH0QBaW8NVVxcHgQMGgEdRRl7XlVdWRRKEx9sZRRUW1NKUw4bAysSEHteVVxcDEsRA21uNWRVUCVXSBtsGHwQBhAZbl4IexcCX2cDUVtfSVUNGAseERBIXFVbXw1DFwZtVwRkXV57ZDUaMhoiEXsWOl8QCE0SBWhlBFxeUU5XBRgDGhcSTlVUW184SicA; TrackID=1JfhpDsHSu_btV_jpGHhxum0AfdUaaMoTrHOPqCbne-yHjXkrGbVWv_hPb-7Yz7haHSUJmJmw1UCwUU6n3BVjM_o4VNb6EdD_TzZp2z1hzcs; thor=5CB659D6EDB7B6F97FE9C032A0DA5727B35281F23F560AA638F1625F110064F512A153C6867251B15852BD34F7555A3FEADB4ACBD1DA9F94BFBB802027F44A105A21E23F72472B71E0126B5C570C2C388E31BEC9CC8C5B336FF28C173552958869C2949F362FC2BD915C5B4017E83AB177FFC14723AF162A30062193118528DCCA0D8E0550393ABBF551255C93CD3A7313795B5AFE00E90C945BF751863E6C9A; light_key=AASBKE7rOxgWQziEhC_QY6yavc4WrqJhG5kFb84hWe7lDzWh-z9M7rnvAmGEjTvImPzncKnp; pinId=QqGuqgudGctt-kV48xLaDA; pin=jd_OKaDnqHNwqKi; unick=6o2w9w6z1a1u43; ceshi3.com=000; _tp=AMPnEuWnC0VKR7aZozUe7Q%3D%3D; _pst=jd_OKaDnqHNwqKi; __jda=76161171.17476309284212004349143.1747630928.1747630929.1747991175.2; __jdc=76161171; UseCorpPin=jd_OKaDnqHNwqKi; 3AB9D23F7A4B3CSS=jdd03EZ62H5CO4MQBBEW4O6P4XGTR7LX4Z7MU3O7CRGDIYH6JZA6YM2SYLXIOHXIKJ7MA3FPMFDYHCEVH3MJUBQEWIRELIMAAAAMW7RTJAMYAAAAACB5T2OESY24M34X; shshshfpb=BApXSQA9u__NAY5BxKhByJ66L97fhEPLDBgUiDh5p9xJ1MuaAN462; flash=3_pdcfd2Hy9jn9S26vgK7wbyX0wUXRxGhus6X4KbWsixSnQ30M6m5NNU0zRMBItGkPU6QITEPyI3oGtmOwibhcyPurMICSx5MAuvGS4mYtPIaD4iKJNyDHapVy6CcvieDdgzO4dhuiKBxBix-MHwjz06QpSTFxCbfF3sYVSy1ocG9dQzMWjF-h; __jdb=76161171.14.17476309284212004349143|2.1747991175"

# 自定义请求头
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": f"https://item.jd.com/{SKU_ID}.html",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://item.jd.com",
    "Cookie": JD_COOKIE,
}


def build_comment_url(page_num: int) -> str:
    return (
        "https://club.jd.com/comment/productPageComments.action"
        f"?productId={SKU_ID}"
        "&score=0"
        "&sortType=6"
        f"&page={page_num}"
        f"&pageSize={PAGE_SIZE}"
        "&isShadowSku=0"
        "&fold=1"
    )

def crawl_comments():
    all_comments = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 创建一个带有 APIRequestContext 的浏览器上下文
        context = browser.new_context()
        api_request = context.request

        for page_num in range(PAGE_START, PAGE_END):
            url = build_comment_url(page_num)
            print(f"抓取第 {page_num+1} 页评论: {url}")

            try:
                # 直接用 APIRequestContext 发 GET
                response = api_request.get(url, headers=HEADERS, timeout=15000)
                data = response.json()
            except Exception as e:
                print(f"  → 请求或 JSON 解析失败: {e}")
                time.sleep(2)
                continue

            comments = data.get("comments", [])
            if comments:
                print(f"  → 成功获取 {len(comments)} 条评论")
                all_comments.extend(comments)
            else:
                print("  → 本页无评论或接口没返回 data.comments")

            time.sleep(1)  # 放缓节奏，避免被限流

        browser.close()
    return all_comments

def save_to_csv(comments, filename):
    if not comments:
        print("没有可保存的评论数据。")
        return
    rows = []
    for c in comments:
        rows.append({
            "用户昵称":    c.get("nickname",""),
            "评分":       c.get("score",""),
            "评论时间":    c.get("creationTime",""),
            "评论内容":    c.get("content",""),
            "商品规格":    f"{c.get('productColor','')} / {c.get('productSize','')}",
            "有用数":     c.get("usefulVoteCount",0),
            "回复数":     c.get("replyCount",0),
        })
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ 评论已保存到：{filename}")

if __name__ == "__main__":
    comments = crawl_comments()
    save_to_csv(comments, f"{SKU_ID}_comments.csv")
