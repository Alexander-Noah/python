import requests
url='https://www.google.com/intl/en_uk/chrome/'
# url='https://www.baidu.com/get'
response = requests.get(url)
print(response.headers)