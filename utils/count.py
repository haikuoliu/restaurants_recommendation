from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData1 = db.businessMongoData1
userMongoData = db.userMongoData
c1 = businessMongoData1.count()
c2 = userMongoData.count()
s= "4U9kSBLuBDU391x6bxU-YA"
c3 = userMongoData.find_one({"user_id": s})
print c1
print c2
print c3
