import sys
sys.path.append("..")

import databaseInterfaces.mongoDB_interface as mongoDB_interface

def assign_role(user_id, role="user"):
    """
    Assigns a role to a user.

    Parameters:
        user_id (str): The user's id.
        role (str): The role to assign. Default is "user".

    """
    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        user["access_level"] = role
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set":{'access_level':role}})
    except:
        print("Cannot assign role. User not found.")


def ban_user(user_id):
    """
    Bans a user.

    Parameters:
        user_id (str): The user's id.   
    """

    try:
        user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
        user["is_banned"] = True
        mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set":{'is_banned':True}})
    except:
        print("Cannot ban user. User not found.")


def get_all_users():
    """
    Returns all users.

    Returns:
        list: A list of all users.
    """
    users = mongoDB_interface.findAllDocument("test_db","users_collection",{})
    return users