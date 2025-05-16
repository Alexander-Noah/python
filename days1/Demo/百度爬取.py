import requests
from pyquery import PyQuery as pq
url = 'https://www.baidu.com/'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
response = requests.get(url,headers=headers)
print(response.text)
doc =pq(response.text)
print(doc('title').text())