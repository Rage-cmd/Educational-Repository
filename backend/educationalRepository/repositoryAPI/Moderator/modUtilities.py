import sys

sys.path.append("..")

import databaseInterfaces.mongoDB_interface as mongoDB_interface

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
        print(user)
        if user["access_level"] == "user":
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
        if user["access_level"] == "user":
            user["is_banned"] = False
            mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"is_banned":False}})
            return True
    except:
        return False


def approve_post(post_id):
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
        return True
    except:
        print("Error in approving post. Check if the post with the id: " + post_id + " exists.")
        return False

    