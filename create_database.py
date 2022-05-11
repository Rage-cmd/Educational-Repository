from backend.educationalRepository.databaseInterfaces.mongoDB_interface import *
from backend.educationalRepository.repositoryAPI.Caching.cache_impl import *
# from backend.educationalRepository.repositoryAPI.User.userUtilities import *


users = [
    {
        'id': 'u2',
        'name': 'John Doe',
        'email': 'user@example.com',
        'password': 'password',
        'access_level': 'user',
        'status': 'active',
        'posts': ['p1'],
        'comments': ['c1', 'c2'],
        'saved_posts': ['p2'],
        'liked_posts': ['p2', 'p3'],
        'points': 100,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': True
    },
    {
        'id': 'u3',
        'name': 'Jane Doe',
        'email': 'user2@example.com',
        'password': 'password',
        'access_level': 'user',
        'status': 'active',
        'posts': ['p2', 'p3'],
        'comments': [],
        'saved_posts': ['p1'],
        'liked_posts': ['p1', 'p6'],
        'points': 100,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u4',
        'name': 'Nathan Smith',
        'email': 'user3@example.com',
        'password': 'password',
        'access_level': 'moderator',
        'status': 'inactive',
        'posts': ['p4'],
        'comments': [],
        'saved_posts': ['p3'],
        'liked_posts': ['p3', 'p2'],
        'points': 114,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u5',
        'name': 'Henry Sullivan',
        'email': 'user4@example.com',
        'password': 'password',
        'access_level': 'moderator',
        'status': 'active',
        'posts': ['p5'],
        'comments': ['c3'],
        'saved_posts': ['p4', 'p6'],
        'liked_posts': ['p3', 'p1', 'p2'],
        'points': 100,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u1',
        'name': 'John Smith',
        'email': 'user5@example.com',
        'password': 'password',
        'access_level': 'admin',
        'status': 'active',
        'posts': ['p6'],
        'comments': [],
        'saved_posts': ['p6'],
        'liked_posts': ['p2', 'p5'],
        'points': 100,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
]

posts = [
    {
        'id': 'p1',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P1 Caption',
        'text': 'This is a test post',
        'options': ['option1', 'option2', 'option3', 'option4'],
        'author': 'u2',
        'upvotes': 35,
        'image_url': '',
        'is_answered': False,
        'is_approved': True,
        'comments': ['c1'],
        'reports': 2
    },
    {
        'id': 'p2',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P2 Caption',
        'text': 'P2 Text',
        'author': 'u3',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': True,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p3',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P3 Caption',
        'text': 'P3 Text',
        'author': 'u3',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': ['c3'],
        'reports': 2
    },
    {
        'id': 'p4',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P4 Caption',
        'text': 'P4 Text',
        'author': 'u4',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': True,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p5',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P5 Caption',
        'text': 'P5 Text',
        'author': 'u5',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': True,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p6',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P5 Caption',
        'text': 'P5 Text',
        'author': 'u1',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': True,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p7',
        'type': 'image',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P7 Caption',
        'text': 'P7 Text',
        'author': 'u4',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p8',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P8 Caption',
        'text': 'P8 Text',
        'author': 'u1',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 2
    }

]

comments = [
    {
        'id': 'c1',
        'author': 'u2',
        'post_id': 'p1',
        'time': '2020-01-01T00:00:00Z',
        'text': 'This is a test comment',
        'upvotes': 35,
        'reports': 2,
        'is_verified': True
    },
    {
        'id': 'c2',
        'author': 'u2',
        'post_id': 'p6',
        'time': '2020-01-01T00:00:00Z',
        'text': 'This is the second test comment',
        'upvotes': 3,
        'reports': 0,
        'is_verified': False
    },
    {
        'id': 'c3',
        'author': 'u4',
        'post_id': 'p3',
        'time': '2020-01-01T00:00:00Z',
        'text': 'This is the third test comment',
        'upvotes': 3,
        'reports': 0,
        'is_verified': False
    },
]

tags = [
    {
        'id': 't0',
        'name': 'Tag 0',
        'path_to_tag': [],
    },
    {
        'id': 't1',
        'name': 'Tag 1',
        'path_to_tag': ['t0'],
    },
    {
        'id': 't2',
        'name': 'Tag 2',
        'path_to_tag': ['t0','t1'],
    },
    {
        'id': 't3',
        'name': 'Tag 3',
        'path_to_tag':  ['t0','t1'],
    },
    {
        'id': 't4',
        'name': 'Tag 4',
        'path_to_tag': ['t0','t1', 't3'],
    },
    {
        'id': 't5',
        'name': 'Tag 5',
        'path_to_tag': ['t0','t1', 't3'],
    },
    {
        'id': 't6',
        'name': 'Tag 6',
        'path_to_tag': ['t0'],
    }
]

main_tree = [
    {
        'id': 't0',
        'name': 'Main 0',
        'children_tags': ['t1', 't6'],
        'children_posts': [],
        'drive_id': '1bCsM4D4cnCA30hF-0myr96Xzw_3oLEcw'
    },
    {
        'id': 't1',
        'name': 'Main 1',
        'type': 'tag',
        'children_tags': ['t2', 't3'],
        'children_posts': [],
        'drive_id': '1mqiX2ujEe6DAb1pWjhb-VlxnXXAHHZos'
    },
    {
        'id': 't2',
        'name': 'Main 2',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p1', 'p2'],
        'drive_id': '1iUAueUD0sYpbE95n4AJUp_98YpchG-gP'
    },
    {
        'id': 't3',
        'name': 'Main 3',
        'type': 'tag',
        'children_tags': ['t4', 't5'],
        'children_posts': [],
        'drive_id': '1MjWWyflk5T6SmiH83FtPnmvDO2miwQEF'
    },
    {
        'id': 't4',
        'name': 'Main 4',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p3'],
        'drive_id': '1cE0zPYMLiCNJ_6zHnCPPKaE-vqmjdzok'
    },
    {
        'id': 't5',
        'name': 'Main 5',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p4', 'p5', 'p6'],
        'drive_id': '1VbxcbhYdk6Kgkl6e_XwBZ7kiGrGOEXlp'
    },
    {
        'id': 'p1',
        'name': 'Main 6',
        'type': 'post', 
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p2',
        'name': 'Main 7',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p3',
        'name': 'Main 8',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p4',
        'name': 'Main 9',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p5',
        'name': 'Main 10',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p6',
        'name': 'Main 11',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 't6',
        'name': 'Main 12',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p7','p8'],
        'drive_id': '1UwSh_Hl-0yjmd7V4sJFjp_u6NPuLLpVZ'
    },
    {
        'id': 'p7',
        'name': 'Main 13',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    },
    {
        'id': 'p8',
        'name': 'Main 14',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': '12'
    }
]

# delete database
deleteDatabase("test_db")


# creating the database and the collections
test_db = createDatabase("test_db")
user_collection = getCollection("test_db","users_collection")
post_collection = getCollection("test_db","posts_collection")
comments_collection = getCollection("test_db","comments_collection")
tagtree_collection = getCollection("test_db","tagtree_collection")
maintree_collection = getCollection("test_db","maintree_collection")

# inserting the documents in the collections
saveMultipleDocuments("test_db", "users_collection", users)
saveMultipleDocuments("test_db", "posts_collection", posts)
saveMultipleDocuments("test_db", "comments_collection", comments)
saveMultipleDocuments("test_db", "tagtree_collection", tags)
saveMultipleDocuments("test_db", "maintree_collection", main_tree)



