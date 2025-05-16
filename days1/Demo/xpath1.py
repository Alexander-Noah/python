text = \
"""
<ul class="ullist" padding="1" spacing="1">
    <li>
        <div id="top">
            <span class="position" width="350">职位名称</span>
            <span>职位类别</span>
            <span>人数</span>
            <span>地点</span>
            <span>发布时间</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
            </span>
            <span>技术类</span>
            <span>4</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
    </li>
</ul>
"""
#from lxml import etree
# html = etree.HTML(text)
# div = html.xpath('//div')
# for div in div:
#     DIV=etree.tostring(div,encoding='utf8').decode('utf8')
#     print(DIV)
#     print("*"*50)

#html = etree.HTML(text)
# div =html.xpath('//div[5]')[0]
# DIV=etree.tostring(div,encoding='utf8').decode('utf8')
# print(DIV)


# div=html.xpath('//div[@id="even"]')
# for div in div:
#     DIV=etree.tostring(div,encoding='utf-8').decode('utf8')
#     print(DIV)
#     print("*"*50)

# div=html.xpath('//div/span')
# for div in div:
#     Div = etree.tostring(div,encoding = 'utf8').decode('utf8')
#     print(Div)
#     print("*"*50)

from lxml import etree
html = etree.HTML(text)
divs  =html.xpath('//div')[1:]
works=[]#空列表
for div in divs:
    work={#空字典

    }
    url=div.xpath('.//a/@href')[0]
    position = div.xpath('.//a/text()')[0]
    work_type=div.xpath('.//span[2]/text()')[0]
    work_num = div.xpath('.//span[3]/text()')[0]
    area=div.xpath('.//span[3]/text()')[0]
    time =div.xpath('.//span[4]/text()')[0]
    work={
        'url':url,
        'position':position,
        'work_type':work_type,
        'work_num':work_num,
        'area':area,
        'time':time,
    }
    works.append(work)
print(works)

