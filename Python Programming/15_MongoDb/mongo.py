import pymongo

client = pymongo.MongoClient("mongodb+srv://akhilsharmaa:akhilsharmaa@cluster0.akyiqt8.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)