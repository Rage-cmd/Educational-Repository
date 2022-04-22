
import sys
sys.path.append("..")
import databaseInterfaces.mongoDB_interface as mongoDB_interface

def post_ID_search(post_id):
    post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
    return post

def post_name_search(post_name):
    posts = mongoDB_interface.findAllDocument("test_db","posts_collection",{"caption": {"$regex": post_name}})
    result = []
    for post in posts:
        result.append(post)
    return result

def tag_ID_search(tag_id):
    tag = mongoDB_interface.findSingleDocument("test_db","tags_collection",{"id":tag_id})
    path = tag['path_to_tag']
    
