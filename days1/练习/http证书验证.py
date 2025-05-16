import requests

try:
    # 发送请求并进行证书验证
    response = requests.get('https://www.baidu.com', verify=True)#验证证书
    # 检查响应状态码
    response.raise_for_status()
    print("请求成功，证书验证通过！")
    print(response.text)
except requests.exceptions.SSLError as ssl_error:
    print(f"SSL 错误: {ssl_error}")
except requests.exceptions.HTTPError as http_error:
    print(f"HTTP 错误: {http_error}")
except requests.exceptions.RequestException as req_error:
    print(f"请求发生错误: {req_error}")