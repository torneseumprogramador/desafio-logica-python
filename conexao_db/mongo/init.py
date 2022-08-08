# install
# $ python -m pip install pymongo
import pymongo

print("========== connect ==============")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

print("========== use colection ==============")
mycol = mydb["customers"]

print("========== insert ==============")
mydoc = { "name": "John", "address": "Highway 37" }
mycol.insert_one(mydoc)

docs = [
    { "name": "John1", "address": "Highway 38" },
    { "name": "John2", "address": "Highway 39" },
    { "name": "John3", "address": "Highway 40" },
    { "name": "John4", "address": "Highway 41" },
]
mycol.insert_many(docs)


print("========== one ==============")
one = mycol.find_one()
print(one)

print("========== filter ==============")
myquery = { "address": "Park Lane 38" }
docs = mycol.find(myquery)
for doc in docs:
  print(doc)

print("========== many ==============")
docs = mycol.find()
for doc in docs:
  print(doc)

print("========== sort ==============")
docs = mycol.find().sort("name")
for doc in docs:
  print(doc)

print("========== sort desc ==============")
docs = mycol.find().sort([("name", pymongo.DESCENDING)])
for doc in docs:
  print(doc)

print("========== update ==============")
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
for doc in mycol.find():
  print(doc)

print("========== delete ==============")
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)


print("========== find limit ==============")
docs = mycol.find().limit(5)
for doc in docs:
  print(doc)


print("========== drop collection ==============")
mycol.drop()
