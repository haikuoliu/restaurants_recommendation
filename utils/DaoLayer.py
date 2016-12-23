# for userCollection:
from pymongo import MongoClient
client = MongoClient()
# client set up
db = client.test
userCollection = db.userMongoData

from bson.objectid import ObjectId
def getByUser_id(findId):
    # the userColllection like the table which store the data of user
    try:
        document = userCollection.find_one({"user_id":findId})
        return document
    except Exception:
        return "id incorrect"
def getByEmail(email):
    # the userColllection like the table which store the data of user
    print "findtheemail  "
    print email
    try:
        document = userCollection.find_one({"email": email})
        return document
    except Exception:
        return "Email incorrect"
def insertData(data):
    # you should assign an id at first or MongDB will assign a random one for you.
    try:
        post_id = userCollection.insert_one(data).inserted_id
        return post_id
    except Exception:
        return "insert fail"

def updateData(user_id, target,value):
    # target is the name of attribute and value is the assigned value
    update = userCollection.find_one({"user_id": user_id})
    try:
        update[target] = value
        return "update correct"
    except Exception:
        return "update fail"



s = getByUser_id("4U9kSBLuBDU391x6bxU-YA")
print s


# print getByUser_id("18kPq7GPye-YQ3LyKyAZPw")
#
# print ""
#
# print getByEmail("2@gmail.com")


data = {
    "password": "x",
    "u'user_id": "xx",
    "name": "n",
    "email": "x"
}

print getByEmail("3@gmail.com")


print insertData(data)
print getByUser_id("xx")
#
#
#
# print updateData("")
