# install
# $ python -m pip install pymongo
import os

import pymongo

print("========== connect ==============")
# myclient = pymongo.MongoClient(os.getenv("DATABASE_URL"))
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["desafio_21_dias_python"]

print("========== use colection ==============")
mycol = mydb["usuarios"]

print("========== insert ==============")
mydoc = { 
  "nome": "danilo",
  "email": "danilo@torneseumprogramador.com.br",
  "endereco": "Rua teste 123"
}

mycol.insert_one(mydoc)

docs = [
    { "nome": "John1", "endereco": "Highway 38" },
    { "nome": "John2", "endereco": "Highway 39" },
    { "nome": "John3", "endereco": "Highway 40" },
    { "nome": "John4", "endereco": "Highway 41" },
]
mycol.insert_many(docs)


print("========== one ==============")
one = mycol.find_one()
print(one)

print("========== filter ==============")
myquery = { "endereco": "Rua teste 123" }
docs = mycol.find(myquery)
for doc in docs:
  print(doc)

print("========== many ==============")
docs = mycol.find()
for doc in docs:
  print(doc)

print("========== sort ==============")
docs = mycol.find().sort("nome")
for doc in docs:
  print(doc)

print("========== sort desc ==============")
docs = mycol.find().sort([("nome", pymongo.DESCENDING)])
for doc in docs:
  print(doc)

print("========== update ==============")
myquery = { "endereco": "Valley 345" }
newvalues = { "$set": { "endereco": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
for doc in mycol.find():
  print(doc)

print("========== delete ==============")
myquery = { "endereco": "Mountain 21" }
mycol.delete_one(myquery)


print("========== find limit ==============")
docs = mycol.find().limit(5)
for doc in docs:
  print(doc)


print("========== drop collection ==============")
mycol.drop()
