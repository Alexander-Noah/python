import requests
import json
import time
from pathlib import Path

# 请求头设置
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'referer': 'https://spa1.scrape.center/'
}

# 创建存储目录
output_dir = Path('./movie_data')
output_dir.mkdir(exist_ok=True)  # 如果目录不存在则创建

# 存储所有电影数据的列表
all_movies = []

try:
    # 分页爬取，每页10条，共10页
    for i in range(0, 100, 10):
        # 构造API请求URL
        url = f"https://spa1.scrape.center/api/movie/?limit=10&offset={i}"

        print(f"正在抓取第 {i // 10 + 1} 页数据...")

        # 发送请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 解析JSON数据
        data = response.json()

        # 获取当前页的电影列表
        current_page_movies = data.get("results", [])

        # 将当前页电影添加到总列表
        all_movies.extend(current_page_movies)

        # 打印当前页电影数量（用于监控进度）
        print(f"获取到 {len(current_page_movies)} 条电影数据")

        # 添加延迟，避免请求过于频繁
        time.sleep(1)

    # 准备存储的文件路径
    json_path = output_dir / 'movies.json'

    # 将数据保存为JSON文件
    with open(json_path, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 保证中文正常显示
        # indent=4 使JSON文件格式化，便于阅读
        json.dump(all_movies, f, ensure_ascii=False, indent=4)

    print(f"所有数据已成功保存到 {json_path}")
    print(f"共爬取 {len(all_movies)} 条电影数据")

except requests.exceptions.RequestException as e:
    print(f"网络请求出错: {e}")

except json.JSONDecodeError as e:
    print(f"JSON解析失败: {e}")
    print("返回内容:", response.text[:200])  # 打印部分响应内容帮助调试

except Exception as e:
    print(f"发生未知错误: {e}")

finally:
    # 如果中途出错，也保存已获取的数据
    if all_movies:
        temp_path = output_dir / 'movies_partial.json'
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(all_movies, f, ensure_ascii=False, indent=4)
        print(f"已保存已获取的 {len(all_movies)} 条数据到 {temp_path}")