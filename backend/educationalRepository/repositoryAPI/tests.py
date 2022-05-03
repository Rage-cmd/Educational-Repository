from re import I
from django.test import TestCase

# Create your tests here.
from Search.searchAlgorithms import *
from Suggestion.suggestions import *
from User.userUtilities import *

def print_main():
    main_tree = mongoDB_interface.findAllDocument("test_db","maintree_collection",{})
    for node in main_tree:
        if node["type"] == "tag":
            print(node['id'], "--->", node["children_posts"], node["children_tags"])


def print_tag():
    tag_tree = mongoDB_interface.findAllDocument("test_db","tagtree_collection",{})
    for node in tag_tree:
        print(node['id'], "--->", node["path_to_tag"])

# post = post_ID_search('p12')
# print(post)

# post_caption = post_name_search('caption')
# print(post_caption)

# posts = tag_ID_search('t5')

# for post in posts:
#     print(post['caption'])

# suggested_posts = post_suggestions('4')

# for post in suggested_posts:
#     print(post['caption'])

# node = mongoDB_interface.findSingleDocument("test_db","maintree_collection",{"id":'t5'})
# n_posts, n_tags = neighbour_suggestions([node])

# for node in n_posts:
#     print(node['caption'])

# for node in n_tags:
#     print(node['name'])

# saved_posts = get_posts('u5','saved')

# for post in saved_posts:
#     print(post['caption'])

# uploaded_posts = get_posts('u5','uploads')

# for post in uploaded_posts:
#     print(post['caption'])


# print(like_post('u2','p3'))
# user_2 = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'})
# liked_posts = user_2["liked_posts"]
# print(liked_posts)

# post_3 = mongoDB_interface.findSingleDocument("test_db","posts_collection",{"id":'p3'})
# print(post_3['upvotes'])

# save_post('u2','p2')
# user_2 = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'})
# saved_posts = user_2["saved_posts"]
# print(saved_posts)

# comment_doc = comment_post('u2', 'p2', 'This is my first Comment!')
# user_2 = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'})
# comments = user_2["comments"]
# print(comments)


# delete_comment('u2', 'c5')
# user_2 = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'})
# comments = user_2["comments"]
# print(comments)

# print("BEFORE: ")
# comment_6 = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":'c6'})
# print(comment_6['text'])
# edit_comment('u2', 'c6', 'THE CONTENT OF THE COMMENT HAS BEEN EDITED AGAINNNNN!')
# comment_6 = mongoDB_interface.findSingleDocument("test_db","comments_collection",{"id":'c6'})
# print(comment_6['text'])


# print("BEFORE---------------------\n")
# print_main()
# post_details = {
#     'type': 'image',
#     'caption': 'This is my first post!',
#     'tags':['t1'],
#     'text': "How are you all guys doing?!",
#     "image_url": "/Users/rajeevgoyal/Downloads/images/cat_sleep.jpg"
# }

# upload_post('u2',post_details=post_details)

# print("AFTER---------------------\n")
# print_main()



# post_details = {
#     'type': 'image',
#     'caption': 'This is my first post!',
#     'tags':['t1'],
#     'text': "How are you all guys doing?!",
#     "image_url": "/Users/rajeevgoyal/Downloads/images/cat_sleep.jpg",
#     "new_tag": 't9'
# }
# print_main()
# print("--")
# print_tag()


# upload_post('u2', post_details=post_details)

# print("AFTER---------------------\n")
# print_main()
# print("--")
# print_tag()

# print("\n\n")

# print(mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'}))

post_details = {
    'type': 'video',
    'caption': 'This is my first video post!',
    'tags':['t1','t6'],
    'text': "What do you think about it?",
    "video_url": "/Users/rajeevgoyal/Downloads/images/sample_movie.mov",
}
print_main()
print("--")
print_tag()


upload_post('u2', post_details=post_details)

print("AFTER---------------------\n")
print_main()
print("--")
print_tag()

print("\n\n")

print(mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'}))