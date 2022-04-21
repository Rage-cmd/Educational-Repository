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
    }
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
        'image_url': 'https://example.com/image.png',
        'is_accepted': False,
        'comments': ['c13', 'c66'],
        'reports': 2
    },
]

# delete database
deleteDatabase("test_db")

test_db = createDatabase("test_db")
user_collection = getCollection("test_db","users_collection")
post_collection = getCollection("test_db","posts_collection")

saveMultipleDocuments("test_db", "users_collection", users)
saveMultipleDocuments("test_db", "posts_collection", posts)


