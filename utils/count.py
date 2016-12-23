from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData = db.businessMongoData
# userMongoData = db.userMongoData
c1 = businessMongoData.count()
# c2 = userMongoDatauser.count()
print c1
# print c2
