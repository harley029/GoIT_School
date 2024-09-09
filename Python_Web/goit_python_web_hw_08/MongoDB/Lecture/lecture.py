from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.book

# --------------------------------------- insert one document
# result_one = db.cats.insert_one(
#     {
#         "name": "Laska",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )
# print(result_one.inserted_id)

# --------------------------------------- insert several documents
# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)

# --------------------------------------- find one document by id
# result = db.cats.find_one({"_id": ObjectId("663b5e56ecc2d734058d44d3")})
# print(result)

# --------------------------------------- find severul documents
# result = db.cats.find({})
# for el in result:
#     print(el)

# --------------------------------------- update one documents
# db.cats.update_one({"name": "Laska"}, {"$set": {"age": 4}})
# result = db.cats.find_one({"name": "Laska"})
# print(result)

# --------------------------------------- delete one documents
# db.cats.delete_one({"name": "Liza"})
# result = db.cats.find_one({"name": "Liza"})
# print(result)

