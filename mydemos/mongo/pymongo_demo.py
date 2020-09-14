# coding=utf-8
'''
DATE: 2020/09/14
AUTHOR: Yanxi Li
'''

from pymongo import MongoClient

mc = MongoClient("127.0.0.1", 27017)

MC = MongoClient("127.0.0.1", 27017)  # 创连接 创建MongoDB客户端
db = MC["S22"]  # 选择或创建数据库 （内存）  # show databases

player_info = {
    "nickname": "钱雨",
    "atc": 5,
    "def": 99,
    "hp": 500,
    "skill": [
        {
            "name": "铁头功",
            "def": 50
        },
        {
            "name": "见义勇为",
            "hp": 999
        }
    ]
}
# 增加数据
res = db.player.insert_one(player_info)    # player 有数据后，player为表名
print(res.inserted_id,type(res.inserted_id))  # 当前新增数据的 ObjectId
# res = db.player.insert_many([player_info])
# print(res.inserted_ids) # 当前新增数据们的 Object
# class 'bson.objectid.ObjectId' 不能被JSON序列化 但是 可以转成字符串


# 查询数据
# res = db.player.find({})
# for i in res:
#     print(i)
# res = db.player.find_one({"nickname":"钱雨"}) # 查询符合条件的第一条数据
# print(res)
# res = db.player.find_one({"nickname":"钱雨","def":{"$gt":80}}) # 查询符合条件的第一条数据
# print(res)
# res["_id"] = str(res.get("_id")) # ObjectId 不能被 JSON 序列化 转换成字符串即可
# res_json = json.dumps(res)
# print(res_json)

# 更新数据 update
# res = db.player.update_one({"nickname":"程根"},{"$set":{"hp":350}})
# print(res)
# db.player.update_many({},{"$inc":{"atc":20}})

# 删除数据
# from bson.objectid import ObjectId
# res = db.player.delete_one({"_id":ObjectId("5d902bca19ccfed36f87e62f")})
# print(res.deleted_count)

# 排序 选取 跳过
# from pymongo import ASCENDING,DESCENDING
# res = db.player.find({}).limit(2).skip(2).sort("_id",DESCENDING)
# for i in res:
#     print(i)
