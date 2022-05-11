
import sys
from time import monotonic
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
    tags = mongoDB_interface.findAllDocument("test_db","tagtree_collection",{"name": {"$regex": keyword, "$options": "i"}})
    result = []
    for tag in tags:
        result.append(tag)
    return result


def neighbour_suggestions(path):
    """
    This function expects a list of main_tree nodes (representing the path searched by the user) and returns the 
    immediate childrens of the last node.
    """
    last_node = None
    
    children_posts = []
    children_tags = []

    if path == "":
        last_node = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id": "t0"})
    else:
        last_node_id = path
        last_node = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id": last_node_id})

    print("last_node: ", last_node)

    for post_id in last_node['children_posts']:
        children_posts.append(mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id}))
    
    for tag_id in last_node['children_tags']:
        children_tags.append(mongoDB_interface.findSingleDocument("test_db","tagtree_collection",{"id":tag_id}))
    
    return children_posts, children_tags

    