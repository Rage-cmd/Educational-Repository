from cgi import test
import pymongo
from pymongo import MongoClient


def getCollection(Database, collection):
    db = client[Database]
    col = db[collection]
    return col

# takes up the document and saves into mongoDB
def saveSingleDocument(Database, collection, object):
    db = client[Database]
    col = db[collection]
    objectId = col.insert_one(object).inserted_id
    return objectId

def saveMultipleDocuments(Database, collections, objects):
    col = getCollection(Database,collections)
    objectIds = col.insert_many(objects).inserted_ids
    return objectIds

def findSingleDocument(Database, collection, filterObject):
    col = getCollection(Database, collection)
    object = col.find_one(filterObject)
    return object

def findAllDocument(Database, collection, filterObject):
    col = getCollection(Database, collection)
    object = col.find(filterObject)
    return object

def deleteDocument(Database, collection, filterObject):
    col = getCollection(Database, collection)
    object = col.delete_one(filterObject)
    return object

# saveDocument("test_db","test_col",{"name":"asda", "age":10})
# print(findAllDocument("test_db", "test_col", {"name":"asda"}))


# create a mongodb database

# test_db = client["test_db"]
# users_col = test_db["users"]

# users = [
#     {
#         'user_name': 'John Doe',
#         'user_email': 'user@example.com',
#         'user_password': 'password',
#         'user_access_level': 'user',
#         'user_status': 'active',
#         'user_posts': ['p12', 'p52'],
#         'user_comments': ['c13', 'c66'],
#         'user_points': 100,
#         'user_profile_picture': 'https://example.com/profile.png',
#         'user_no_of_bans': 0,
#         'user_is_banned': False
#     },
#     {
#         'user_name': 'Jane Doe',
#         'user_email': 'user2@example.com',
#         'user_password': 'password',
#         'user_access_level': 'user',
#         'user_status': 'active',
#         'user_posts': ['p17', 'p32'],
#         'user_comments': ['c53', 'c67'],
#         'user_points': 100,
#         'user_profile_picture': 'https://example.com/profile2.png',
#         'user_no_of_bans': 0,
#         'user_is_banned': False
#     },
#     {
#         'user_name': 'Nathan Smith',
#         'user_email': 'user3@example.com',
#         'user_password': 'password',
#         'user_access_level': 'moderator',
#         'user_status': 'inactive',
#         'user_posts': ['p18', 'p33'],
#         'user_comments': ['c54', 'c68'],
#         'user_points': 114,
#         'user_profile_picture': 'https://example.com/profile3.png',
#         'user_no_of_bans': 0,
#         'user_is_banned': False
#     }
# ]

# saveMultipleDocuments("test_db", "users_col", users)

# if __name__ == "__main__":
client = MongoClient()

users = findAllDocument("test_db", "users_col", {})

for doc in users:
    print(doc)