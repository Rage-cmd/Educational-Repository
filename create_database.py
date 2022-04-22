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
        'id': 'u6',
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
        'id': 'p12',
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
        'id': 'p52',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t4', 't5'],
        'caption': ''
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

# delete database
deleteDatabase("test_db")

test_db = createDatabase("test_db")
user_collection = getCollection("test_db","users_collection")
post_collection = getCollection("test_db","posts_collection")
comments_collection = getCollection("test_db","comments_collection")

saveMultipleDocuments("test_db", "users_collection", users)
saveMultipleDocuments("test_db", "posts_collection", posts)
saveMultipleDocuments("test_db", "comments_collection", comments)


