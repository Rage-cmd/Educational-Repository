
import sys
sys.path.append("..")
import databaseInterfaces.mongoDB_interface as mongoDB_interface
from collections import defaultdict


def post_suggestions(keyword):
    posts = mongoDB_interface.findAllDocument("test_db","posts_collection",{"caption": {"$regex": keyword, "$options": "i"}})
    result = []
    for post in posts:
        result.append(post)
    return result

def tag_suggestions(keyword):
    tags = mongoDB_interface.findAllDocument("test_db","maintree_collection",{"name": {"$regex": keyword, "$options": "i"}})
    result = []
    for tag in tags:
        result.append(tag)
    return result