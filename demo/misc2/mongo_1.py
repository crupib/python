import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["products"]

myquery = { "title": "Hammer" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
