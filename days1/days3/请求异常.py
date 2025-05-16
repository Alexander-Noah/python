from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import socket

url = "https://www.example.com/404"

try:
    # urllib的timeout参数是全局超时（单位：秒）
    response = urlopen(url, timeout=10)
    print("请求成功，内容长度:", len(response.read()))

except HTTPError as e:
    # 捕获HTTP错误
    print(f"[urllib] HTTP错误 {e.code}: {e.reason}")
    if e.code == 404:
        print("⚠️ 页面不存在，请检查URL路径")

except URLError as e:
    # 捕获URL相关错误
    if isinstance(e.reason, socket.timeout):
        print("⌛ 请求超时")
    elif isinstance(e.reason, socket.gaierror):
        print("🌐 域名解析失败")
    else:
        print(f"🔗 URL错误: {e.reason}")

except Exception as e:
    print(f"意外错误: {type(e).__name__} - {str(e)}")