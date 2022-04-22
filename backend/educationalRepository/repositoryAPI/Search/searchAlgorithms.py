
import sys
sys.path.append("..")
import databaseInterfaces.mongoDB_interface as mongoDB_interface

def post_search(post_id):
    post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
    return post