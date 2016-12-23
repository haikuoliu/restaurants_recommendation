from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData1 = db.businessMongoData1
userMongoData = db.userMongoData
c1 = businessMongoData1.count()
c2 = userMongoDatauser.count()
print c1
print c2
