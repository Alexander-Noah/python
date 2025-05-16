# html = '''
#     "<div>"
#         <ul>
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="Link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>e
#     </div>'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))


# from pyquery import PyQuery as pq
# import requests
# url ='https://www.baidu.com'
# response =requests.get(url)
# response.encoding="utf8"
# doc=pq(response.text)
# print(doc('title').text())


html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

from pyquery import PyQuery as pq
import requests
url='https://www.baidu.com'
response  = requests.get(url)
html_content = response.content.decode('utf-8')
doc = pq(html_content)
print(doc('title').text())
print(response.headers.get('Content-Type'))















































