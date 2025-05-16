import requests
from lxml import etree
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}

cookies = {
    '__mta': '188071447.1742908690864.1745405315952.1745405568408.26',
    'uuid_n_v': 'v1',
    # ... 保留你的其他cookies
}

base_url = 'https://www.maoyan.com'
target_url = 'https://www.maoyan.com/board/4?offset=0'

try:
    response = requests.get(target_url, headers=headers, cookies=cookies)
    response.raise_for_status()  # 检查请求是否成功

    html = etree.HTML(response.text)

    # 更精确的XPath选择器
    movie_links = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@href')

    # 过滤空值并拼接完整URL
    full_urls = [urljoin(base_url, link) for link in movie_links if link]

    # 打印结果
    for i, url in enumerate(full_urls, 1):
        print(f"{i}. {url}")


except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")