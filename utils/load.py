import json
from pymongo import MongoClient
client = MongoClient()
db = client.test
businessMongoData = db.businessMongoData
fin = open('/home/ec2-user/restaurants_recommendation/data／businessMongoData.json','r')
for eachLine in fin:
    line = eachLine.strip().decode('utf-8')
    line = line.strip(',')
    try:
        js = json.loads(line)
    except Exception, e:
        continue
    businessMongoData.insert_one(js)
