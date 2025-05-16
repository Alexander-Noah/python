import xlwt
import random

#创建excel表文件
workbook = xlwt.Workbook(encoding = 'utf-8')


#添加sheet
sheet1 = workbook.add_sheet('sheet1')
sheet2 = workbook.add_sheet('热度榜单')

#写入数据
sheet2.write(0,0,'chinese')
sheet2.write(0,1,'match')
sheet2.write(0,2,'english')


for row in range(1,51,1):
    for col in range(0,3,1):
        sheet2.write(row,col,random.randint(50,100))
#保存excel
workbook.save(r'新浪热搜爬取.xls')
