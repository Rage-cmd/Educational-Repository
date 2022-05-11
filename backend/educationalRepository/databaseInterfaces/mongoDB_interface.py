import sys

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
    col.insert_one(object)
    return object['id']

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

def getNextSequenceValue(Database, collection, offset = 1):
    """
    Gets the next sequential value of the collection.

    :param Database: The database to be used
    :param collection: The collection to be used
    :return: The next sequential value
    
    Example:
        getNextSequentialValue("test_db", "users_collection")
    """
    col = getCollection(Database, collection)
    object = col.find().sort([("id", pymongo.DESCENDING)]).limit(1)
    for doc in object:
        return int(doc["id"][1:]) + 1
    return offset

def updateDocument(Database, collection, filterObject, updateObject):
    """
    Updates a document in the collection. If the document does not exist, it will be created.

    :param Database: The database to be used
    :param collection: The collection to be used
    :param filterObject: The filter object to be used
    :param updateObject: The update object to be used
    :return: The objectId of the updated document
    
    Example:
        updateDocument("test_db", "users_collection", {"id": "u1"}, {"$set": {"name": "test"}})
    """
    col = getCollection(Database, collection)
    object = col.update_one(filterObject, updateObject)
    return object

client = MongoClient()
