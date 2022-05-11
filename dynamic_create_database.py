import hashlib
from backend.educationalRepository.databaseInterfaces.mongoDB_interface import *
from backend.educationalRepository.databaseInterfaces.drive_api import *
from backend.educationalRepository.repositoryAPI.Caching.cache_impl import *


# users = [
#     {
#         'id': 'u2',
#         'name': 'John Doe',
#         'email': 'user@example.com',
#         'password': 'password',
#         'access_level': 'user',
#         'status': 'active',
#         'posts': ['p1'],
#         'comments': ['c1', 'c2'],
#         'saved_posts': ['p2'],
#         'liked_posts': ['p2', 'p3'],
#         'points': 100,
#         'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'notifications': [],
#         'no_of_bans': 0,
#         'requested_reports': [],
#         'is_banned': True
#     },
#     {
#         'id': 'u3',
#         'name': 'Jane Doe',
#         'email': 'user2@example.com',
#         'password': 'password',
#         'access_level': 'user',
#         'status': 'active',
#         'posts': ['p2', 'p3'],
#         'comments': [],
#         'saved_posts': ['p1'],
#         'liked_posts': ['p1', 'p6'],
#         'points': 100,
#         'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'notifications': [],
#         'no_of_bans': 0,
#         'requested_reports': [],
#         'is_banned': False
#     },
#     {
#         'id': 'u4',
#         'name': 'Nathan Smith',
#         'email': 'user3@example.com',
#         'password': 'password',
#         'access_level': 'moderator',
#         'status': 'inactive',
#         'posts': ['p4'],
#         'comments': [],
#         'saved_posts': ['p3'],
#         'liked_posts': ['p3', 'p2'],
#         'points': 114,
#         'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'notifications': [],
#         'no_of_bans': 0,
#         'requested_reports': [],
#         'is_banned': False
#     },
#     {
#         'id': 'u5',
#         'name': 'Henry Sullivan',
#         'email': 'user4@example.com',
#         'password': 'password',
#         'access_level': 'moderator',
#         'status': 'active',
#         'posts': ['p5'],
#         'comments': ['c3'],
#         'saved_posts': ['p4', 'p6'],
#         'liked_posts': ['p3', 'p1', 'p2'],
#         'points': 100,
#         'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'notifications': [],
#         'no_of_bans': 0,
#         'requested_reports': [],
#         'is_banned': False
#     },
#     {
#         'id': 'u1',
#         'name': 'John Smith',
#         'email': 'user5@example.com',
#         'password': 'password',
#         'access_level': 'admin',
#         'status': 'active',
#         'posts': ['p6'],
#         'comments': [],
#         'saved_posts': ['p6'],
#         'liked_posts': ['p2', 'p5'],
#         'points': 100,
#         'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'notifications': [],
#         'no_of_bans': 0,
#         'requested_reports': [],
#         'is_banned': False
#     },
# ]

# posts = [
#     {
#         'id': 'p1',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P1 Caption',
#         'text': 'This is a test post',
#         'options': ['option1', 'option2', 'option3', 'option4'],
#         'author': 'u2',
#         'upvotes': 35,
#         'image_url': '',
#         'is_answered': False,
#         'is_approved': True,
#         'comments': ['c1'],
#         'reports': 2
#     },
#     {
#         'id': 'p2',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P2 Caption',
#         'text': 'P2 Text',
#         'author': 'u3',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': True,
#         'comments': [],
#         'reports': 2
#     },
#     {
#         'id': 'p3',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P3 Caption',
#         'text': 'P3 Text',
#         'author': 'u3',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': False,
#         'comments': ['c3'],
#         'reports': 2
#     },
#     {
#         'id': 'p4',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P4 Caption',
#         'text': 'P4 Text',
#         'author': 'u4',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': True,
#         'comments': [],
#         'reports': 2
#     },
#     {
#         'id': 'p5',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P5 Caption',
#         'text': 'P5 Text',
#         'author': 'u5',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': True,
#         'comments': [],
#         'reports': 2
#     },
#     {
#         'id': 'p7',
#         'type': 'image',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P7 Caption',
#         'text': 'P7 Text',
#         'author': 'u4',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': False,
#         'comments': [],
#         'reports': 2
#     },
#     {
#         'id': 'p8',
#         'type': 'text',
#         'time': '2020-01-01T00:00:00Z',
#         'tags': ['t4', 't5'],
#         'caption': 'P8 Caption',
#         'text': 'P8 Text',
#         'author': 'u1',
#         'upvotes': 35,
#         'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
#         'is_answered': False,
#         'is_approved': False,
#         'comments': [],
#         'reports': 2
#     }

# ]

# comments = [
#     {
#         'id': 'c1',
#         'author': 'u2',
#         'post_id': 'p1',
#         'time': '2020-01-01T00:00:00Z',
#         'text': 'This is a test comment',
#         'upvotes': 35,
#         'reports': 2,
#         'is_verified': True
#     },
#     {
#         'id': 'c2',
#         'author': 'u2',
#         'post_id': 'p6',
#         'time': '2020-01-01T00:00:00Z',
#         'text': 'This is the second test comment',
#         'upvotes': 3,
#         'reports': 0,
#         'is_verified': False
#     },
#     {
#         'id': 'c3',
#         'author': 'u4',
#         'post_id': 'p3',
#         'time': '2020-01-01T00:00:00Z',
#         'text': 'This is the third test comment',
#         'upvotes': 3,
#         'reports': 0,
#         'is_verified': False
#     },
# ]

# tags = [
#     {
#         'id': 't0',
#         'name': 'Tag 0',
#         'path_to_tag': [],
#     },
#     {
#         'id': 't1',
#         'name': 'Tag 1',
#         'path_to_tag': ['t0'],
#     },
#     {
#         'id': 't2',
#         'name': 'Tag 2',
#         'path_to_tag': ['t0','t1'],
#     },
#     {
#         'id': 't3',
#         'name': 'Tag 3',
#         'path_to_tag':  ['t0','t1'],
#     },
#     {
#         'id': 't4',
#         'name': 'Tag 4',
#         'path_to_tag': ['t0','t1', 't3'],
#     },
#     {
#         'id': 't5',
#         'name': 'Tag 5',
#         'path_to_tag': ['t0','t1', 't3'],
#     },
#     {
#         'id': 't6',
#         'name': 'Tag 6',
#         'path_to_tag': ['t0','t6'],
#     }
# ]

# main_tree = [
#     {
#         'id': 't0',
#         'name': 'Main 0',
#         'children_tags': ['t1', 't6'],
#         'children_posts': [],
#         'drive_id': '1oh-Sl3rBHJNXAFt8bdBaXN7BaVEXvU3S'
#     },
#     {
#         'id': 't1',
#         'name': 'Main 1',
#         'type': 'tag',
#         'children_tags': ['t2', 't3'],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 't2',
#         'name': 'Main 2',
#         'type': 'tag',
#         'children_tags': [],
#         'children_posts': ['p1', 'p2'],
#         'drive_id': '12'
#     },
#     {
#         'id': 't3',
#         'name': 'Main 3',
#         'type': 'tag',
#         'children_tags': ['t4', 't5'],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 't4',
#         'name': 'Main 4',
#         'type': 'tag',
#         'children_tags': [],
#         'children_posts': ['p3'],
#         'drive_id': '12'
#     },
#     {
#         'id': 't5',
#         'name': 'Main 5',
#         'type': 'tag',
#         'children_tags': [],
#         'children_posts': ['p4', 'p5', 'p6'],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p1',
#         'name': 'Main 6',
#         'type': 'post', 
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p2',
#         'name': 'Main 7',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p3',
#         'name': 'Main 8',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p4',
#         'name': 'Main 9',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p5',
#         'name': 'Main 10',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p6',
#         'name': 'Main 11',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 't6',
#         'name': 'Main 12',
#         'type': 'tag',
#         'children_tags': [],
#         'children_posts': ['p7','p8'],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p7',
#         'name': 'Main 13',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     },
#     {
#         'id': 'p8',
#         'name': 'Main 14',
#         'type': 'post',
#         'children_tags': [],
#         'children_posts': [],
#         'drive_id': '12'
#     }
# ]

# # delete database
# deleteDatabase("test_db")


# # creating the database and the collections
# test_db = createDatabase("test_db")
# user_collection = getCollection("test_db","users_collection")
# post_collection = getCollection("test_db","posts_collection")
# comments_collection = getCollection("test_db","comments_collection")
# tagtree_collection = getCollection("test_db","tagtree_collection")
# maintree_collection = getCollection("test_db","maintree_collection")

# # inserting the documents in the collections
# saveMultipleDocuments("test_db", "users_collection", users)
# saveMultipleDocuments("test_db", "posts_collection", posts)
# saveMultipleDocuments("test_db", "comments_collection", comments)
# saveMultipleDocuments("test_db", "tagtree_collection", tags)
# saveMultipleDocuments("test_db", "maintree_collection", main_tree)

# make password hash
def make_password_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


# retrieve password from hash
def retrieve_password(password_hash):
    return hashlib.sha256(password_hash.encode('utf-8')).hexdigest()



def insert_tag(tag_name, parents):
    """
    Inserts a tag in the tag_tree collection. It also adds the tag ID in the main_tree collection.

    Parameters:
        tag_name (str) : The name of the tag.
        parents (list) : The list of parent tag IDs.

    Returns:
        tag_id (str) : The id of the tag.

    """
    print('---------------------------')
    print(tag_name, parents)
    try :
        tag_id = 't' + str(getNextSequenceValue("test_db","tagtree_collection",offset=0))
        tag_doc = {
            "id": tag_id,
            "name": tag_name,
            "path_to_tag": parents,
        }

        saveSingleDocument("test_db","tagtree_collection",tag_doc)
        
        if parents == []:
            parent_folder_id = None
        else:
            updateDocument("test_db","maintree_collection",{"id":parents[-1]},{"$push": {"children_tags":tag_id}})
            print(parents[-1])
            p_doc = findSingleDocument("test_db","maintree_collection",{"id":parents[-1]})
            print(p_doc)
            parent_folder_id = [findSingleDocument("test_db","maintree_collection",{"id":parents[-1]})["drive_id"]]

        file = create_folder(tag_name,parent_folder_id)

        main_tree_node_doc = {
            "id": tag_id,
            "name": tag_name,
            "type" : "tag",
            "children_tags": [],
            "children_posts": [],
            'drive_id': file['id'],
        }

        print(main_tree_node_doc)

        saveSingleDocument("test_db","maintree_collection",main_tree_node_doc)
        return tag_id
    except:
        print("Could not insert tag. Check if the parents are valid.")
        return None


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
        # file_name, file_extension = os.path.splitext(post_details["image_url"])
        file_name = post_details["image_url"].name
        file_extension = post_details["image_url"].name.split(".")[-1]
        upload_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S ") + post_details['caption'] + "." + file_extension
        print(upload_name)
        uploaded_file_id = drive_api.upload_file_IO( upload_name,
                                                     post_details["image_url"],
                                                     fields=fields,
                                                     parent_folder_id=['1oh-Sl3rBHJNXAFt8bdBaXN7BaVEXvU3S'])
        
        post_doc["image_url"] = uploaded_file_id["webContentLink"]

    elif post_details["type"] == "video":
        file_name, file_extension = os.path.splitext(post_details["video_url"])
        upload_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S ") + post_details['caption'] + file_extension
        uploaded_file_id = drive_api.upload_file(upload_name, 
                                                    post_details["video_url"], 
                                                    fields=fields, 
                                                    parent_folder_id=[drive_id])
        post_doc["video_url"] = uploaded_file_id["webContentLink"]

    print("Done till  IF ELSE statement")

    mongoDB_interface.saveSingleDocument("test_db","posts_collection",post_doc)
    mongoDB_interface.updateDocument("test_db","maintree_collection",{"id":parent_folder},{"$push": {"children_posts":post_doc["id"]}})

    maintree_child_doc = {
        "id": post_doc["id"],
        "name": post_doc["caption"],
        "type": "post",
        "children_tags": [],
        "children_posts": []
    }

    if post_doc["type"] == "image" or post_doc["type"] == "video":
        maintree_child_doc['drive_id'] = uploaded_file_id['id']
    else:
        maintree_child_doc['drive_id'] = None

    print("CREATED MAIN TREE NODE")

    mongoDB_interface.saveSingleDocument("test_db","maintree_collection",maintree_child_doc)
    user = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":user_id})
    user["posts"].append(post_doc["id"])
    mongoDB_interface.updateDocument("test_db","users_collection",{"id":user_id},{"$set": {"posts":user["posts"]}})

    cache.addItem_recent_cache(post_doc,datetime.datetime.now())

    return post_doc


def create_users(name,password,email):
    user_document = {
            "id": 'u' + str(getNextSequenceValue("test_db","users_collection")),
            "name": name,
            "password": make_password_hash(password),
            "email": email,
            "access_level": "user",
            "status": "active",
            "posts": [],
            "comments": [],
            "saved_posts": [],
            "liked_posts": [],
            "points": 0,
            "profile_picture": "",
            "notifications": [],
            "no_of_bans": 0,
            "is_banned": False,
        }

    result = saveSingleDocument("test_db","users_collection",user_document)
#----------------------

deleteDatabase("test_db")

# creating users
create_users("user1","password","user1@example.com")
create_users("user2","password","user2@example.com")
create_users("user3","password","user3@example.com")
create_users("user4","password","user4@example.com")
create_users("user5","password","user5@example.com")


# creating the tag tree/ main tree and drive tree
insert_tag('t0',[])   # -------> root node
insert_tag('t1',['t0'])
insert_tag('t2',['t0','t1'])
insert_tag('t3',['t0','t1'])
insert_tag('t4',['t0','t1','t3'])
insert_tag('t5',['t0','t1','t3'])
insert_tag('t6',['t0'])

all_nodes = findAllDocument("test_db","maintree_collection",{})

for node in all_nodes:
    print(node["id"],node["drive_id"])