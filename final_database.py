from backend.educationalRepository.databaseInterfaces.mongoDB_interface import *
from backend.educationalRepository.repositoryAPI.Caching.cache_impl import *
# from backend.educationalRepository.repositoryAPI.User.userUtilities import *


users = [
    {
        'id': 'u1',
        'name': 'John Doe',
        'email': 'user1@example.com',
        'password': 'password1',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u2',
        'name': 'Jane Doe',
        'email': 'user2@example.com',
        'password': 'password2',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u3',
        'name': 'Harsh Anand',
        'email': 'user3@example.com',
        'password': 'password3',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u4',
        'name': 'Stephen Strange',
        'email': 'user4@example.com',
        'password': 'password4',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u5',
        'name': 'Harry Potter',
        'email': 'user5@example.com',
        'password': 'password5',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u6',
        'name': 'Hermione Granger',
        'email': 'user6@example.com',
        'password': 'password6',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u7',
        'name': 'Ronald Weasley',
        'email': 'user7@example.com',
        'password': 'password7',
        'access_level': 'user',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u8',
        'name': 'Draco Malfoy',
        'email': 'user8@example.com',
        'password': 'password8',
        'access_level': 'moderator',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u9',
        'name': 'Severus Snape',
        'email': 'user9@example.com',
        'password': 'password9',
        'access_level': 'moderator',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u10',
        'name': 'Rubeus Hagrid',
        'email': 'user10@example.com',
        'password': 'password10',
        'access_level': 'moderator',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u11',
        'name': 'Minerva McGonagall',
        'email': 'user11@example.com',
        'password': 'password11',
        'access_level': 'moderator',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u12',
        'name': 'Peter Pettigrew',
        'email': 'user12@example.com',
        'password': 'password12',
        'access_level': 'moderator',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u13',
        'name': 'Ginny Weasley',
        'email': 'user13@example.com',
        'password': 'password13',
        'access_level': 'admin',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u14',
        'name': 'Theodore Nott',
        'email': 'user14@example.com',
        'password': 'password14',
        'access_level': 'admin',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    },
    {
        'id': 'u15',
        'name': 'Cedric Diggory',
        'email': 'user15@example.com',
        'password': 'password15',
        'access_level': 'admin',
        'status': 'active',
        'posts': [],
        'comments': [],
        'saved_posts': [],
        'liked_posts': [],
        'points': 10,
        'profile_picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'notifications': [],
        'no_of_bans': 0,
        'requested_reports': [],
        'is_banned': False
    }
]

posts = [
    {
        'id': 'p1',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0','t1','t4','t7'],
        'caption': 'Can anybody explain me the concepts of Congestion Control?',
        'text': 'I have studied congestion control recently and I am very interested in it.  Can anybody explain me the concepts of congestion control?',
        'author': 'u1',
        'upvotes': 15,
        'image_url': '',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 2
    },
    {
        'id': 'p2',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't1', 't4'],
        'caption': 'Transport Layer Security',
        'text': 'Why Does Mod Ssl Stop With The Error "failed To Generate Temporary 512 Bit Rsa Private Key" When I Start Apache?',
        'author': 'u2',
        'upvotes': 12,
        'image_url': '',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p3',
        'type': 'image',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't1', 't5'],
        'caption': 'Application Layer Protocol Encryption',
        'text': 'I am trying to understand the application layer protocol encryption and I am stuck in the middle of it. Can anybody help me?',
        # Application layer encryption is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers.
        'author': 'u1',
        'upvotes': 10,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p4',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't1', 't5'],
        'caption': 'What are the three main advantages of having an Application Layer?',
        'text': 'We already have a lot of advantages of having a network layer. What are the three main advantages of having an application layer?',
        'author': 'u1',
        'upvotes': 31,
        'image_url': '',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p5',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't1', 't6'],
        'caption': 'What are the responsibilities of network layer?',
        'text': 'As far as I have been briefed, the network layer helps us to establish a connection between two computers. It also helps us to send data between the computers. What are the responsibilities of the network layer?',
        'author': 'u3',
        'upvotes': 15,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p6',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't1'],
        'caption': 'What are the different types of network?',
        'text': 'I have just started my journey in the field of network and I am very interested in the different types of network. What are the different types of network?',
        'author': 'u4',
        'upvotes': 42,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': True,
        'comments': [],
        'reports': 5
    },
    {
        'id': 'p7',
        'type': 'image',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't2'],
        'caption': 'Can someone explain why travelling salesman problem is NP-complete?',
        'text': 'I am new to DSA. I was going through the definitions of NP-complete and came across the Travelling Salesman Problem, I wondered what is a proper justification of TSP being NP-complete',
        'author': 'u5',
        'upvotes': 12,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 3
    },
    {
        'id': 'p8',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't2'],
        'caption': 'Name the strongly connected components in the given graphs.',
        'text': 'The Strongly connected components can be calculated using DFS and reversing the edge directions.',
        'author': 'u6',
        'upvotes': 15,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        "id": "p9",
        "type": "video",
        "time": "2020-01-01T00:00:00Z",
        "tags": ["t0","t2"],
        "caption": "Array Data Structure",
        "text": "An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).",
        "author": "u7",
        "comments": [],
        "is_answered": False,
        "is_approved": False,
        "upvotes": 0,
        "reports": 0,
        "video_url": "https://drive.google.com/file/d/1tuSqTltmlAT-0-hVtJJqV8JpsQkZ-lDc/preview",
        "_id": "627b9a55cdf58c7d3c8c9dd3"
    },
    {
        'id': 'p10',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't3'],
        'caption': 'What are different types of RAID?',
        'text': 'I have been studying DBMS RAID concept recently. I just want to confirm if the content I am reading is dependable.',
        'author': 'u8',
        'upvotes': 31,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p11',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't3'],
        'caption': '1st Normal Form',
        'text': 'If a relation contains a composite or multi-valued attribute, it violates the first normal form, or the relation is in first normal form if it does not contain any composite or multi-valued attribute. A relation is in first normal form if every attribute in that relation is singled valued attribute.',
        'author': 'u9',
        'upvotes': 11,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p12',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't3'],
        'caption': 'B+ Tree Concept',
        'text': 'A B+ tree is an m-ary tree with a variable but often large number of children per node. A B+ tree consists of a root, internal nodes and leaves.[1] The root may be either a leaf or a node with two or more children.',
        'author': 'u7',
        'upvotes': 21,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
    {
        'id': 'p13',
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': ['t0', 't3'],
        'caption': ' Hospital Management System',
        'text': 'Hospitals interact with a lot of people in a day and there are various activities involved in day to day operations of hospitals, for example booking of appointments, managing doctor schedules, managing patient diagnoses, managing medical histories of patients, etc. The aim of this project is to show how data related to these tasks can be made easier to manage using databases.',
        'author': 'u10',
        'upvotes': 25,
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': False,
        'is_approved': False,
        'comments': [],
        'reports': 0
    },
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
        'name': 'Computer Networks',
        'path_to_tag': ['t0'],
    },
    {
        'id': 't2',
        'name': 'DSA',
        'path_to_tag': ['t0'],
    },
    {
        'id': 't3',
        'name': 'DBMS',
        'path_to_tag':  ['t0'],
    },
    {
        'id': 't4',
        'name': 'Transport Layer',
        'path_to_tag': ['t0','t1'],
    },
    {
        'id': 't5',
        'name': 'Application Layer',
        'path_to_tag': ['t0','t1'],
    },
    {
        'id': 't6',
        'name': 'Network Layer',
        'path_to_tag': ['t0','t1'],
    },
    {
        'id': 't7',
        'name': 'Congestion Control',
        'path_to_tag': ['t0','t1','t4'],
    }
]

main_tree = [
    {
        'id': 't0',
        'name': 'root_node',
        'children_tags': ['t1', 't2','t3'],
        'children_posts': [],
        'drive_id': '165aa6hCifTTb0uclKjiLgH-ZLXpmN0pJ'
    },
    {
        'id': 't1',
        'name': 'Main 1',
        'type': 'tag',
        'children_tags': ['t4', 't5', 't6'],
        'children_posts': ['p6'],
        'drive_id': '18O-yCRO5G5dIrTZsuDrHyrAmjqL8s4SQ'
    },
    {
        'id': 't2',
        'name': 'Main 2',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p7', 'p8', 'p9'],
        'drive_id': '1oPAEzp7c9uoNKQ0hQC0iCQLjYjGIDYLn'
    },
    {
        'id': 't3',
        'name': 'Main 3',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p10', 'p11', 'p12', 'p13'],
        'drive_id': '1_JzUJ_Pj0Yjmab4q9oz8VsWmdd-I3xXJ'
    },
    {
        'id': 't4',
        'name': 'Main 4',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p2'],
        'drive_id': '1gMFCCNQlVBpa16brkutWs8MQ_EIvIBZm'
    },
    {
        'id': 't5',
        'name': 'Main 5',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p3', 'p4'],
        'drive_id': '171omo8WmSDp8gwR3F-8y5YgtSVs7DHwh'
    },
    {
        'id': 't6',
        'name': 'Main 6',
        'type': 'tag', 
        'children_tags': [],
        'children_posts': ['p5'],
        'drive_id': '1f6elz5lZKp8a5muFVYk4hGBwUFvXeMAa'
    },
    {
        'id': 't7',
        'name': 'Main 7',
        'type': 'tag',
        'children_tags': [],
        'children_posts': ['p1'],
        'drive_id': '1PHI_57LHc1vZXW9whQ0KHmMKkHOVET1B'
    },
    {
        'id': 'p1',
        'name': 'Main 8',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p2',
        'name': 'Main 9',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p3',
        'name': 'Main 10',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p4',
        'name': 'Main 11',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p5',
        'name': 'Main 12',
        'type': 'tag',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p6',
        'name': 'Main 13',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p7',
        'name': 'Main 14',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p8',
        'name': 'Main 15',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p9',
        'name': 'Main 16',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p10',
        'name': 'Main 17',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p11',
        'name': 'Main 18',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p12',
        'name': 'Main 19',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
    },
    {
        'id': 'p13',
        'name': 'Main 20',
        'type': 'post',
        'children_tags': [],
        'children_posts': [],
        'drive_id': ''
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
# saveMultipleDocuments("test_db", "comments_collection", comments)
saveMultipleDocuments("test_db", "tagtree_collection", tags)
saveMultipleDocuments("test_db", "maintree_collection", main_tree)



