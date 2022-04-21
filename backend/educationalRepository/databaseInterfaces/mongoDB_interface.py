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

def deleteDatabase(Database):
    client.drop_database(Database)

def createDatabase(Database):
    db = client[Database]
    return db

client = MongoClient()
