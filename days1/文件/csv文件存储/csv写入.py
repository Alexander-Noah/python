# 数据写入
# import csv
# with open('data.csv','w')as csvfile:#以写的方式打开文件data.csv，如果没有这个文件就创建文件
#     writer = csv.writer(csvfile,delimiter=',')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','mike',20])
#     writer.writerow(['12321','bob',32])
#     writer.writerow(['12323','jiaj',23])

# 多行写入
# import csv
# with open('data.csv','w')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','gender','birthday'])
#     writer.writerows([['10001','mike',20],['12321','bob',32],['12323','jiaj',23]])

# 字典方式写入
# import csv
# with open('data.csv','w',encoding='utf-8')as csvfile:
#     fieldnames = ['id','name','age']#字段
#     writer=csv.DictWriter(csvfile,fieldnames = fieldnames)
#     writer.writeheader()
#     writer.writerow({'id':'1001','name':'李四','age':'19'})
#     writer.writerow({'id':'1002','name':'张三','age':'20'})
#     writer.writerow({'id':'1003','name':'王五','age':'25'})

# 追加
# import csv
# with open('data.csv','a',encoding='utf-8')as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writerow({'id':'1004','name':'张三丰','age':'23'})

import pandas as pd
data=[
    {'id':'1001','name':'李四','age':'19'},
    {'id':'1002','name':'张三','age':'20'},
    {'id':'1003','name':'王五','age':'25'},
]

df=pd.DataFrame(data)
df.to_csv('data1.csv',index=False)


















