import datetime
import os
import sys
sys.path.append("..")


import databaseInterfaces.mongoDB_interface as mongoDB_interface
import databaseInterfaces.drive_api as drive_api
import repositoryAPI.Caching.cache_impl as cache_impl

creds = drive_api.get_credentials('/Users/rajeevgoyal/Academics/Sem 8/Educational Repository/OAuth keys/credentials.json')
service = drive_api.build('drive', 'v3', credentials=creds)

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


def like_post(user_id, post_id, cache):
    """
    Like a post. The function expects a user id and a post id. 
    
    The function returns a boolean value.

    Parameters:
        user_id (str) : The user id of the user.
        post_id (str) : The id of the post.
        cache (obj)   : The cache object for the application.

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

        cache.addItem_upvote_cache(post_id, post['upvotes'])

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
    

def upload_post(user_id, post_details, cache):
    """
    Upload a post. The function expects a user id and a dictionary consisiting of post details.

    The dictionary should contain the following keys:
        type (str) : The type of the post.
        text (str) : The text of the post.
        caption (str) : The caption of the post.
        tags (list) : A list of tag IDs. The tag IDs should be in the order of tree heirarchy i.e [root, first child, second child, ...].

    Optional keys:
        image_url (str) : The url of the image.
        video_url (str) : The url of the video.
        new_tag (str) : The name of the new tag. The new tag will be created if it does not exist. Use this key only if the tag is not in the tags list. 
    
    Just using the tags list will create a post with the tags present in the list (the order of tags in the list is important).
    Using tags with the new_tags field will create a post under the tags list with the new tag.

    The function returns a boolean value indicating if the post was uploaded successfully.

    Parameters:
        user_id (str) : The user id of the user.
        post_details (dict) : The details of the post.
        cache (dict) : The cache for storing post ids.

    Returns:
        The document of the created post.
    """
    try:
        post_doc = {
            "id": 'p' + str(mongoDB_interface.getNextSequenceValue("test_db","posts_collection")),
            "type": post_details["type"],
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tags": post_details["tags"],
            "caption": post_details["caption"],
            "text": post_details["text"],
            "author": user_id,
            "comments": [],
            "is_answered": False,
            "is_approved": False,
            "upvotes": 0,
            "reports": 0,
        }

    except:
        print("The post details are not in the correct format.")
    
    # if new_tag is not None create a new tag
    if "new_tag" in post_details:
        new_tag_id = insert_tag(post_details["new_tag"], post_details["tags"])
        post_doc["tags"].append(new_tag_id)
    
    if post_details["tags"] == []:
        post_doc["tags"] = ["root"]
    
    parent_folder = post_details['tags'][-1]
    
    drive_id = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":parent_folder})["drive_id"]
    uploaded_file_id = None
    fields = ["id", "name", 'mimeType', 'webViewLink', 'webContentLink']
    fields = ",".join(fields)
    
    if post_details["type"] == "image":
        file_name, file_extension = os.path.splitext(post_details["image_url"])
        upload_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S ") + post_details['caption'] + file_extension
        uploaded_file_id = drive_api.upload_file( upload_name,
                                                  post_details["image_url"], 
                                                  fields=fields, 
                                                  parent_folder_id=[drive_id]) 
        post_doc["image_url"] = uploaded_file_id["webContentLink"]

    elif post_details["type"] == "video":
        file_name, file_extension = os.path.splitext(post_details["video_url"])
        upload_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S ") + post_details['caption'] + file_extension
        uploaded_file_id = drive_api.upload_file(upload_name, 
                                                    post_details["video_url"], 
                                                    fields=fields, 
                                                    parent_folder_id=[drive_id])
        post_doc["video_url"] = uploaded_file_id["webContentLink"]


    mongoDB_interface.saveSingleDocument("test_db","posts_collection",post_doc)
    mongoDB_interface.updateDocument("test_db","maintree_collection",{"id":parent_folder},{"$push": {"children_posts":post_doc["id"]}})

    maintree_child_doc = {
        "id": post_doc["id"],
        "name": post_doc["caption"],
        "type": "post",
        "children_tags": [],
        "children_posts": [],
        "drive_id": uploaded_file_id["id"],
    }

    mongoDB_interface.saveSingleDocument("test_db","maintree_collection",maintree_child_doc)

    user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
    user["posts"].append(post_doc["id"])
    mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"posts":user["posts"]}})

    cache.addItem_recent_cache(post_doc['id'],datetime.now())

    return post_doc
    

def insert_tag(tag_name, parents):
    """
    Inserts a tag in the tag_tree collection. It also adds the tag ID in the main_tree collection.

    Parameters:
        tag_name (str) : The name of the tag.
        parents (list) : The list of parent tag IDs.

    Returns:
        tag_id (str) : The id of the tag.

    """

    try :
        tag_id = 't' + str(mongoDB_interface.getNextSequenceValue("test_db","tagtree_collection"))
        tag_doc = {
            "id": tag_id,
            "name": tag_name,
            "path_to_tag": parents,
        }

        mongoDB_interface.saveSingleDocument("test_db","tagtree_collection",tag_doc)
        mongoDB_interface.updateDocument("test_db","maintree_collection",{"id":parents[-1]},{"$push": {"children_tags":tag_id}})

        parent_folder_id = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":parents[-1]})["drive_id"]

        file = drive_api.create_folder(tag_name,[parent_folder_id])

        main_tree_node_doc = {
            "id": tag_id,
            "name": tag_name,
            "type" : "tag",
            "children_tags": [],
            "children_posts": [],
            'drive_id': file['id'],
        }

        mongoDB_interface.saveSingleDocument("test_db","maintree_collection",main_tree_node_doc)
        return tag_id
    except:
        print("Could not insert tag. Check if the parents are valid.")
        return None


def verify_comment(user_id, comment_id):
    """
    Marks the comment as the accepted answer.

    Parameters:
        user_id (str) : The user id of the user.
        comment_id (str) : The id of the comment.

    Returns:
        The document of the comment.
    """
    try:
        comment_doc = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":comment_id})
        if comment_doc["author"] == user_id:
            mongoDB_interface.updateDocument("test_db","posts_collection",{"id":comment_doc["post_id"]},{"$set": {"is_answered":True}})
            mongoDB_interface.updateDocument("test_db","comments_collection",{"id":comment_id},{"$set": {"is_verified":True}})
            return comment_doc
        else:
            return None
    except:
        print("Could not verify comment. Check if the comment id is valid.") 
        return None
 
