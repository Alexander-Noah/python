import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}
cookies = {
    'cookie': '__mta=188071447.1742908690864.1745311271452.1745311300668.19; uuid_n_v=v1; uuid=96745880097B11F09359351BBC9DA35CD77A2B7FDFD1490ABB87874375799BBB; _lxsdk_cuid=195cd740e46c8-0d198635575362-4c657b58-1bcab9-195cd740e46c8; __mta=188071447.1742908690864.1742908690864.1742908697488.2; ci=70%2C%E9%95%BF%E6%B2%99; _lxsdk=96745880097B11F09359351BBC9DA35CD77A2B7FDFD1490ABB87874375799BBB; _csrf=38081b0843e4f1c868d2a228e5b53f1b624fbeeffd5d5eb5c1229a22c2cf406d; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_s=1965c9c37fd-f2a-e94-6bf%7C%7C8'
}
for i in range(0, 100, 10):
    url = 'https://www.maoyan.com/board/4?offset={i}'.format(i=i)
# url='https://www.maoyan.com/board/4?offset=0'
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.status_code)
    host = []
    html = etree.HTML(response.text)
    home = html.xpath('.//dl/dd/div/div/div')
    for homes in home:
        title = homes.xpath('.//p/a/text()')
        protagonist = homes.xpath('.//p[2]/text()')
        time = homes.xpath('.//p[3]/text()')
        eg = {
            '标题': title,
            '主演': protagonist,
            '上映时间': time,
        }
        host.append(eg)
    print(host)

# print(response.text)
