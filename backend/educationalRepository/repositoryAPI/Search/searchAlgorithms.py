
import sys
sys.path.append("..")
import databaseInterfaces.mongoDB_interface as mongoDB_interface

def search_post_by_ID(post_id):
    post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
    return post

def search_post_by_name(post_name):
    post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"caption":"/"+post_name+"/"})
    return post

# def search_post_by_tag(tag):
#     post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"tags":tag})
#     return post