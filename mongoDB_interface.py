import pymongo
from pymongo import MongoClient

client = MongoClient()

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

def saveMultipleDocuments(Database, collection, objects):
    col = getCollection(Database,collection)
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

# saveDocument("test_db","test_col",{"name":"asda", "age":10})
# print(findAllDocument("test_db", "test_col", {"name":"asda"}))