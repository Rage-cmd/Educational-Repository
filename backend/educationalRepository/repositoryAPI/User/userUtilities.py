import datetime

import sys
sys.path.append("..")


import databaseInterfaces.mongoDB_interface as mongoDB_interface

# TODO:
## def upload_post

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


def like_post(user_id, post_id):
    """
    Like a post. The function expects a user id and a post id. 
    
    The function returns a boolean value.

    Parameters:
        user_id (str) : The user id of the user.
        post_id (str) : The id of the post.

    Returns:
        success (bool) : A boolean value.

    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})

        if post_id in user["liked_posts"]:
            # remove post_id from liked posts if it is already liked
            user["liked_posts"].remove(post_id)
            post['upvotes'] -= 1
            
        else:
            user["liked_posts"].append(post_id)
            post['upvotes'] += 1

        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"liked_posts":user["liked_posts"]}})
        mongoDB_interface.updateDocument("test_db","posts_collection",{"id":post_id},{"$set": {"upvotes":post['upvotes']}})

        return True
    
    except:
        return False


def save_post(user_id, post_id):
    """
    Save a post. The function expects a user id and a post id. 
    
    The function returns a boolean value.

    Parameters:
        user_id (str) : The user id of the user.
        post_id (str) : The id of the post.

    Returns:
        success (bool) : A boolean value.

    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})

        if post_id in user["saved_posts"]:
            # remove post_id from saved posts if it is already saved
            user["saved_posts"].remove(post_id)
        else:
            user["saved_posts"].append(post_id)

        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"saved_posts":user["saved_posts"]}})

        return True
    except:
        return False


def comment_post(user_id, post_id, comment_text):
    """
    Comment on a post. The function expects a user id, a post id and a comment text. 
    Parameters:
        user_id (str) : The user id of the user.
        post_id (str) : The id of the post.
        comment_text (str) : The text of the comment.

    Returns:
        success (bool) : A boolean value.

    """
    # try:
    user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
    post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})

    comment_doc = {
        "id": 'c' + str(mongoDB_interface.getNextSequenceValue("test_db","comments_collection")),
        "author": user_id,
        "post_id": post_id,
        "time": datetime.datetime.now(),
        "text": comment_text,
        "upvotes": 0,
        "reports": 0,
        "is_verified": False
    }

    comment_id = mongoDB_interface.saveSingleDocument("test_db","comments_collection",comment_doc)

    post['comments'].append(comment_id)
    mongoDB_interface.updateDocument("test_db","posts_collection",{"id":post_id},{"$set": {"comments":post['comments']}})

    user['comments'].append(comment_id)
    mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"comments":user['comments']}})

    return comment_doc



# to be implemented
# def delete_post(user_id, post_id):
#     """
#     Delete a post. The function expects a user id and a post id. 
    
#     The function returns a boolean value.

#     Parameters:
#         user_id (str) : The user id of the user.
#         post_id (str) : The id of the post.


#     """
#     user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})

#     user["posts"].remove(post_id)
#     mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"posts":user["posts"]}})

#     mongoDB_interface.deleteDocument("test_db","posts_collection",{"id":post_id})


def delete_comment(user_id, comment_id):
    """
    Delete a comment. The function expects a user id and a comment id. 
    
    The function returns a boolean value.

    Parameters:
        user_id (str) : The user id of the user.
        comment_id (str) : The id of the comment.

    Returns:
        success (bool) : True if the comment was deleted, False otherwise.

    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        comment = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":comment_id})
        post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":comment["post_id"]})

        user["comments"].remove(comment_id)
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"comments":user["comments"]}})

        post["comments"].remove(comment_id)
        mongoDB_interface.updateDocument("test_db","posts_collection",{"id":comment["post_id"]},{"$set": {"comments":post["comments"]}})

        mongoDB_interface.deleteDocument("test_db","comments_collection",{"id":comment_id})
        return True
    except:
        return False


def edit_comment(user_id, comment_id, comment_text):
    """
    Edit a comment. The function expects a user id, a comment id and a comment text. 
    
    The function returns a boolean value.

    Parameters:
        user_id (str) : The user id of the user.
        comment_id (str) : The id of the comment.
        comment_text (str) : The text of the comment.

    Returns:
        success (bool) : True if the comment was edited successfully. False otherwise.

    """
    try:
        comment = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":comment_id})
        comment["text"] = comment_text
        mongoDB_interface.updateDocument("test_db","comments_collection",{"id":comment_id},{"$set": {"text":comment["text"]}})
        return True

    except:
        return False
    