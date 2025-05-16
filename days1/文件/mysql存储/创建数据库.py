# 链接数据库
# import pymysql
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root')
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)#输出版本号
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")#创建数据库
# db.close()

# 创建表
# import pymysql
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='sinahot')
# cursor=db.cursor()
# sql='CREATE TABLE IF NOT EXISTS hot1(id VARCHAR(255) NOT NULL ,hots VARCHAR(255) NOT NULL ,Link VARCHAR(1024) NOT NULL,PRIMARY KEY(ID))'
# cursor.execute(sql)
# db.close()

# 插入数据
# import pymysql
# id='2022187323'
# user='BOb'
# age=20
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='spiders')
# cursor=db.cursor()
# sql='INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()


# 通用插入方法
# import pymysql
#
# data = {
#     'id': '2022187325',
#     'name': 'xiaoming',
#     'age': 18
# }
#
# try:
#     # 尝试连接数据库
#     db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='sinahot')
#     cursor=db.cursor()
#     table = 'students'
#     keys = ','.join(data.keys())
#     values = ','.join(['%s'] * len(data))
#     cursor = db.cursor()
#     sql = f'INSERT INTO {table}({keys}) VALUES ({values})'
#     try:
#         # 尝试执行 SQL 插入语句
#         result = cursor.execute(sql, tuple(data.values()))
#         if result:
#             print('Successful')
#             db.commit()
#     except pymysql.Error as e:
#         # 打印插入操作的异常信息
#         print(f'Insert operation failed: {e}')
#         db.rollback()
# except pymysql.Error as e:
#     # 打印数据库连接的异常信息
#     print(f'Database connection failed: {e}')
# finally:
#     if 'db' in locals() and db.open:
#         db.close()

# 更新数据库
# import pymysql
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='sinahot')
# cursor=db.cursor()
# sql='UPDATE students SET age=%s WHERE name=%s'
# try:
#     cursor.execute(sql,(25,'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()


#灵活更新mysql数据
# import pymysql
#
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='spiders')
# cursor=db.cursor()
# data={
#         'id':'2022187326',
#         'name':'bjk',
#         'age':32,
#     }
# try:
#     table='students'
#     keys=','.join(data.keys())
#     values=','.join(['%s'] * len(data))
#     sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'
#     update = ', '.join([f'{key} = VALUES({key})' for key in data])
#     sql += f' ON DUPLICATE KEY UPDATE {update}'
#     try:
#         if cursor.execute(sql, tuple(data.values())):
#             db.commit()
#     except pymysql.Error as e:
#         print(f'insert operation failed:{e}')
#         db.rollback()
# except pymysql.err.OperationalError as e:
#     print(f"Database operation failed: {e}")
# finally:
#     if 'db' in locals() and db.open:
#         db.close()

# 删除数据
# import pymysql
# db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='spiders')
# cursor=db.cursor()
# table='students'
# condition='age>20'#删除条件
# sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()


# 查询数据
import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='spiders')
cursor=db.cursor()
sql='SELECT* FROM students WHERE age>=20'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row=cursor.fetchone()
    while row:
        print('Row:',row)
        row=cursor.fetchone()
except:
    print('Error')




















