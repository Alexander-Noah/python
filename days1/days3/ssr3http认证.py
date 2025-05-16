import requests
from requests.auth import HTTPBasicAuth

# 目标网页的 URL
url = "https://ssr3.scrape.center/"  # 替换为实际需要爬取的网页 URL
# 用户名和密码
username = "admin"  # 替换为实际用户名
password = "admin"  # 替换为实际密码

# 创建 HTTPBasicAuth 对象
auth = HTTPBasicAuth(username, password)

# 发送 GET 请求，并带上认证信息
response = requests.get(url, auth=auth)

# 检查响应状态码
if response.status_code == 200:
    print("请求成功，网页内容如下：")
    print(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")