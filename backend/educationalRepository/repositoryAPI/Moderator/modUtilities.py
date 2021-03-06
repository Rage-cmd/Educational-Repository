import sys

sys.path.append("..")

import databaseInterfaces.mongoDB_interface as mongoDB_interface
# import Caching.cache_impl as cache_impl
import datetime

def ban_user_mod(user_id):
    """
    Ban a user. The function expects a user id. 

    Parameters:
        user_id (str) : The user id of the user.
    
    Returns:
        Boolean : True if the user is banned, False otherwise.
    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        # ban user for ban duration
        # if user["access_level"] == "user":
        user["is_banned"] = True
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"is_banned":True}})
        return True
    except:
        return False
    

def unban_user_mod(user_id):
    """
    Unban a user. The function expects a user id.

    Parameters:
        user_id (str) : The user id of the user.

    Returns:
        Boolean : True if the user is unbanned, False otherwise.
    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        # unban user
        # if user["access_level"] == "user":
        user["is_banned"] = False
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"is_banned":False}})
        return True
    except:
        return False


def approve_post(post_id,cache):
    """
    Approve a post. The function expects a user id and a post id. 

    Parameters:
        post_id (str) : The id of the post.
    
    Returns:
        Boolean : True if the post is approved, False otherwise.
    """
    try:
        post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
        post["is_approved"] = True
        mongoDB_interface.updateDocument("test_db","posts_collection",{"id":post_id},{"$set": {"is_approved":post['is_approved']}})
        
        notification = "Your post " + post["caption"] + " has been approved."
        user_id = post['author']
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$push": {"notifications":notification}})
        
        cache.addItem_recent_cache(post,datetime.datetime.now())

        return True
    except:
        print("Error in approving post. Check if the post with the id: " + post_id + " exists.")
        return False


def unapprove_post(post_id):
    """
    Unapprove a post. The function expects a user id and a post id. 

    Parameters:
        post_id (str) : The id of the post.
    
    Returns:
        Boolean : True if the post is unapproved, False otherwise.
    """
    try:
        post = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":post_id})
        post["is_approved"] = False
        mongoDB_interface.updateDocument("test_db","posts_collection",{"id":post_id},{"$set": {"is_approved":post['is_approved']}})

        notification = "Your post " + post["caption"] + " has been rejected!."
        user_id = post['author']
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$push": {"notifications":notification}})
        return True
    except:
        print("Error in unapproving post. Check if the post with the id: " + post_id + " exists.")
        return False


def get_pending_approvals():
    """
    Get all the posts that are pending approval. 

    Parameters:
        None
    
    Returns:
        List : A list of all the posts that are pending approval.
    """
    try:
        post_ids = mongoDB_interface.findAllDocument("test_db","posts_collection",{"is_approved":False})
        posts = []
        for post in post_ids:
            posts.append(post)
        return posts
    except:
        print("Error in getting pending approvals.")
        return []