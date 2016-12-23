from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData1 = db.businessMongoData1
userMongoData = db.userMongoData
userTag = db.userTag
c1 = businessMongoData1.count()
c2 = userMongoData.count()
c3 = userTag.count()
print c1
print c2
print c3
