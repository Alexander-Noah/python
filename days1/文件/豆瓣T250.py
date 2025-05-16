import requests

proxies = {
    'http': 'http://127.0.0.1 :8888',  # 如 192.168.1.100:8888
    'https': 'http://127.0.0.1 :8888',
}

response = requests.get("https://ssr1.scrape.center/", proxies=proxies)
print(response.text)