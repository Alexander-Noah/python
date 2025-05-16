# import csv
# with open('data1.csv','r',encoding='utf-8')as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


#pandas
# import pandas as pd
# df = pd.read_csv(r'E:\java\python\days1\Demo\results\7号房的礼物 - 7번방의 선물.json')
# print(df)

# 转换列表读取
import pandas as pd
df= pd.read_csv('data1.csv')
data=df.values.tolist()
print(data)


















































