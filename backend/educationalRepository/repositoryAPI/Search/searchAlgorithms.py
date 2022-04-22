
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
    main_tree_node = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":tag_id})
    post_nodes = []
    queue = [main_tree_node]
    while queue:
        node = queue.pop(0)
        if node['type'] == 'post':
            post_nodes.append(node)
        for child in node['children_tags']:
            queue.append(mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":child}))
        for child in node['children_posts']:
            queue.append(mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":child}))
    
    result = []
    for post in post_nodes:
        result.append(mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post['id']}))
    return result
    
