from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData2 = db.businessMongoData2
userMongoData = db.userMongoData
userTag = db.userTag
businessMongoData3 = db.businessMongoData3
c1 = businessMongoData2.count()
c2 = userMongoData.count()
c3 = userTag.count()
c4 = businessMongData3.count()
print "the number of businessMongoData: "
print c1
print '\n'
print "the number of businessMongoData: "
print c2
print '\n'
print "the number of businessMongoData: "
print c3
print '\n'
print "the number of businessMongoData: "
print c4
print '\n'
