from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData = db.businessMongoData
userMongoData = db.userMongoDatauser
c1 = businessMongoData.count()
c2 = userMongoDatauser.count()
print c1
print c2
