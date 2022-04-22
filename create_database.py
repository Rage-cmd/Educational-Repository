from backend.educationalRepository.databaseInterfaces.mongoDB_interface import *

users = [
    {
        'id': 'u2',
        'name': 'John Doe',
        'email': 'user@example.com',
        'password': 'password',
        'access_level': 'user',
        'status': 'active',
        'posts': ['p12', 'p52'],
        'comments': ['c13', 'c66'],
        'points': 100,
        'profile_picture': 'https://example.com/profile.png',
        'no_of_bans': 0,
        'is_banned': False
    },
    {
        'id': 'u3',
        'name': 'Jane Doe',
        'email': 'user2@example.com',
        'password': 'password',
        'access_level': 'user',
        'status': 'active',
        'posts': ['p17', 'p32'],
        'comments': ['c53', 'c67'],
        'points': 100,
        'profile_picture': 'https://example.com/profile2.png',
        'no_of_bans': 0,
        'is_banned': False
    },
    {
        'id': 'u4',
        'name': 'Nathan Smith',
        'email': 'user3@example.com',
        'password': 'password',
        'access_level': 'moderator',
        'status': 'inactive',
        'posts': ['p18', 'p33'],
        'comments': ['c54', 'c68'],
        'points': 114,
        'profile_picture': 'https://example.com/profile3.png',
        'no_of_bans': 0,
        'is_banned': False
    },
    {
        'id': 'u5',
        'name': 'Henry Sullivan',
        'email': 'user4@example.com',
        'password': 'password',
        'access_level': 'moderator',
        'status': 'active',
        'posts': ['p19', 'p34'],
        'comments': ['c55', 'c69'],
        'points': 100,
        'profile_picture': 'https://example.com/profile4.png',
        'no_of_bans': 0,
        'is_banned': False
    },
    {
        'id': 'u1',
        'name': 'John Smith',
        'email': 'user5@example.com',
        'password': 'password',
        'access_level': 'admin',
        'status': 'active',
        'posts': ['p20', 'p35'],
        'comments': ['c56', 'c70'],
        'points': 100,
        'profile_picture': 'https://example.com/profile5.png',
        'no_of_bans': 0,
        'is_banned': False
    },
]

posts = [
    {
        'id': 'p1',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'This is a caption',
        'text': 'This is a test post',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
    {
        'id': 'p2',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P2 Caption',
        'text': 'P2 Text',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
    {
        'id': 'p3',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P3 Caption',
        'text': 'P3 Text',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
    {
        'id': 'p4',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P4 Caption',
        'text': 'P4 Text',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
    {
        'id': 'p5',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P5 Caption',
        'text': 'P5 Text',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
    {
        'id': 'p6',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': 'P6 Caption',
        'text': 'P6 Text',
        'author': 'u2',
        'upvotes': 35,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    }

]

comments = [
    {
        'id': 'c13',
        'author': 'u2',
        'post_id': 'p12',
        'time': '2020-01-01T00:00:00Z',
        'text': 'This is a test comment',
        'upvotes': 35,
        'reports': 2,
        'is_verified': True
    },
    {
        'id': 'c66',
        'author': 'u3',
        'post_id': 'p12',
        'time': '2020-01-01T00:00:00Z',
        'text': 'This is the second test comment',
        'upvotes': 3,
        'reports': 0,
        'is_verified': False
    }
]

tags = [
    {
        'id': 't1',
        'name': 'Tag 1',
        'path_to_tag': [],
    },
    {
        'id': 't2',
        'name': 'Tag 2',
        'path_to_tag': ['t1'],
    },
    {
        'id': 't3',
        'name': 'Tag 3',
        'path_to_tag': ['t1'],
    },
    {
        'id': 't4',
        'name': 'Tag 4',
        'path_to_tag': ['t1', 't3'],
    },
    {
        'id': 't5',
        'name': 'Tag 5',
        'path_to_tag': ['t1', 't3'],
    },
]

main_tree = [
    {
        'id': 'm1',
        'name': 'Main 1',
        'type': 'tag',
        'children_tags': ['t2', 't3'],
        'children_posts': []
    },
    {
        'id': 'm2',
        'name': 'Main 2',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p1', 'p2']
    },
    {
        'id': 'm3',
        'name': 'Main 3',
        'type': 'tag',
        'children_tags': ['t4', 't5'],
        'children_posts': []
    },
    {
        'id': 'm4',
        'name': 'Main 4',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p3']
    },
    {
        'id': 'm5',
        'name': 'Main 5',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p4', 'p5', 'p6']
    },
    {
        'id': 'm6',
        'name': 'Main 6',
        'type': 'post', 
        'children_tags': [],
        'children_posts': []
    },
    {
        'id': 'm7',
        'name': 'Main 7',
        'type': 'post',
        'children_tags': [],
        'children_posts': []
    },
    {
        'id': 'm8',
        'name': 'Main 8',
        'type': 'post',
        'children_tags': [],
        'children_posts': []
    },
    {
        'id': 'm9',
        'name': 'Main 9',
        'type': 'post',
        'children_tags': [],
        'children_posts': []
    },
    {
        'id': 'm10',
        'name': 'Main 10',
        'type': 'post',
        'children_tags': [],
        'children_posts': []
    },
    {
        'id': 'm11',
        'name': 'Main 11',
        'type': 'post',
        'children_tags': [],
        'children_posts': []
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



