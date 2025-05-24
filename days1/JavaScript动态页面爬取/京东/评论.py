"""
[课程内容]: Python实现京东商品评论数据信息采集, 实现简单可视化 https://item.jd.com/10088121691070.html
[授课老师]: 青灯教育-自游  [上课时间]: 20:05 可以点歌 可以问问题
[授课环境]:
    Python 3.10
    Pycharm
[模块使用]:
- 采集数据模块
    - DrissionPage -> pip install DrissionPage
    - csv 内置模块 不需要安装
    - time
- 数据可视化
    - pandas -> pip install pandas
    - pyecharts -> pip install pyecharts
    - jieba -> pip install jieba
    - wordcloud -> pip install wordcloud
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信python10080领取

"""
# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入自动化模块, 动作链方法
from DrissionPage.common import Actions
# 导入时间模块
import time
# 导入csv模块
import csv

# 创建文件对象
f = open('data.csv', mode='w', encoding='utf-8', newline='')
# 字典写入方法
csv_writer = csv.DictWriter(f, fieldnames=[
    '昵称',
    '评分',
    '产品',
    '日期',
    '评论',
])
# 写入表头
csv_writer.writeheader()
# 打开浏览器
dp = ChromiumPage()
# 实例化动作链对象
ac = Actions(dp)
# 访问网站
dp.get('https://item.jd.com/10088121691070.html')
# 设置延时等待
# time.sleep(2)
# 监听数据
dp.listen.start('client.action')
# 点击加载全部评论
dp.ele('css:.all-btn .arrow').click()
# 构建循环
for page in range(1, 21):
    print(f'正在采集第{page}页的数据内容')
    # 等待数据包加载
    r = dp.listen.wait()
    # 获取响应数据 -> 字典数据
    json_data = r.response.body
    print(json_data)
    """解析数据"""
    # 字典取值, 提取评论信息所在列表
    comment_list = json_data['result']['floors'][2]['data']
    # for循环遍历, 提取列表里面的元素
    for index in comment_list:
        """提取具体每条评论信息"""
        # 判断这个 commentInfo 键是否存在
        if 'commentInfo' in [i for i in index.keys()]:
            dit = {
                '昵称': index['commentInfo']['userNickName'],
                '评分': index['commentInfo']['commentScore'],
                '产品': index['commentInfo']['productSpecifications'].replace('已购 ', ''),
                '日期': index['commentInfo']['commentDate'],
                '评论': index['commentInfo']['commentData'],
            }
            # 写入数据
            csv_writer.writerow(dit)
            print(dit)
        else:
            pass
    # 定位窗口标签
    tab = dp.ele('css:div.ReactVirtualized__Grid.ReactVirtualized__List')
    # 下滑 元素对象
    tab.scroll.to_bottom()
    # dp 打开浏览器对象
    dp.scroll.to_bottom()


# 导入数据处理模块
# import pandas as pd
# # 导入结巴模块
# import jieba
# # 导入词云模块
# import wordcloud
# # 读取csv文件
# df = pd.read_csv('data.csv')
# # 获取评论内容
# content = ' '.join([i for i in df['评论']])
# # 分词处理
# string = ' '.join(jieba.lcut(content))
# print(string)
# # 配置词云图
# wc = wordcloud.WordCloud(
#     height=700, # 高
#     width=1000, # 宽
#     font_path='C:/Windows/Fonts/SimHei.ttf', # 字体文件
#     background_color='white', # 背景颜色
#     stopwords={'也', '这', '很', '都', '的', '就', '了'}
#
# )
# # 导入词汇
# wc.generate(string)
# # 导出词云图
# wc.to_file('cy.png')


