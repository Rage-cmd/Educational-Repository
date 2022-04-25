import sys
sys.path.append("..")

import databaseInterfaces.mongoDB_interface as mongoDB_interface

def get_posts(user_id, post_type="uploads"):
    """
    Get all the specific type of posts of a user. The function expects a user id and a post type. 
    
    Post type can be : 
                'uploads', 'likes' or 'saved'.
    
    The default post type is 'uploads'.
    The function returns a list of posts.

    Parameters:
        user_id (str)   : The user id of the user.
        post_type (str) : The type of posts to be returned. Default is 'uploads'. Can either be 'uploads', 'likes' or 'saved'.

    Returns:
        posts (list) : A list of posts.

    """
    
    user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})

    if post_type == "uploads":
        post_ids = user["posts"]
    elif post_type == "likes":
        post_ids = user["liked_posts"]
    else:
        post_ids = user["saved_posts"]
    
    user_posts = []
    for post_id in post_ids:
        post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
        user_posts.append(post)
    return user_posts

def get_comments(user_id):
    """
    Get all the comments of a user. The function expects a user id. 
    
    The function returns a list of comments.

    Parameters:
        user_id (str) : The user id of the user.

    Returns:
        comments (list) : A list of comments.

    """
    
    user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
    comment_ids = user["comments"]
    user_comments = []
    for comment_id in comment_ids:
        comment = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":comment_id})
        user_comments.append(comment)
    return user_comments

