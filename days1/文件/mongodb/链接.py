import pymongo
from pymongo import MongoClient
# 连接数据库

#
# # client = pymongo.MongoClient(host='localhost',port=27017)
client = MongoClient('mongodb://localhost:27017/')
#
#
# # 指定数据库
# db=client.test
db=client['test']
# # 指定集合
#
#
# collection=db.students
collection=db['students']


# 插入数据
# student={
#     'id':'20170105',
#     'name':'Kevin',
#     'age': 20,
#     'gender':'male',
# }
# # 插入单个文档（字典）
# result = collection.insert_one(student)  # 返回 InsertOneResult 对象
# print(result.inserted_id)  # 打印插入的文档ID


# # 插入多个文档（列表)
# student1 ={
#     'id':'20170104',
#     'name':'jingb',
#     'age': 25,
#     'gender': 'male'
# }
# student2={
#     'id':'20170202',
#     'name':'Mike',
#     'age':24,
#     'gender':'male',
# }
# result = collection.insert_many([student1,student2])  # 返回 InsertManyResult 对象
# print(result.inserted_ids)  # 打印所有插入的文档ID
#
# #查询
# result = collection.find_one({'name':'Mike'})
# print(type(result))
# print(result)

# from bson.objectid import ObjectId
# result=collection.find_one({'_id':ObjectId('593278c115c2601667ec6bae')})
# print(result)
#查询多条数据
# result=collection.find({'age':{'$gt':20}})
# print(result)
# for result in result:
#     print(result)

# 排序
# results= collection.find().sort('name',pymongo.ASCENDING)
# results= collection.find().sort('name',pymongo.DESCENDING)
# print([result['name']for result in results])

# 偏移
# results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)#skip(偏移量忽略的元素个数)limit(要的结果数)
# print([result['name'] for result in results])
# from bson.objectid import ObjectId
# collection.find({'_id':{'$gt':ObjectId('67fa3a68b16f8258e18acb9a')}})

# 更新
# condition={'name':'Kevin'}
# student = collection.find_one(condition)
# student['age']=66
# result=collection.update_many(condition, {'$set':student})
# print(result)
# print(result.matched_count,result.modified_count)#获得匹配的数据条数，和修改的数据条数
# 更新所有数据
# condition={'age':{'$gt':20}}
# result = collection.update_many(condition,{'$inc':{'age':1}})#age的值加一
# print(result)
# print(result.matched_count,result.modified_count)

# 删除单个数据
result = collection.delete_one({'name':'Kevin'})
print(result)
print(result.deleted_count)

#删除所有符合条件的数据
result= collection.delete_many({'name':'Kenvin'})
print(result.deleted_count)





