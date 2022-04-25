from re import I
from django.test import TestCase

# Create your tests here.
from Search.searchAlgorithms import *
from Suggestion.suggestions import *
from User.userUtilities import *

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

comment_doc = comment_post('u2', 'p2', 'This is my first Comment!')
user_2 = mongoDB_interface.findSingleDocument("test_db","users_collection",{"id":'u2'})
comments = user_2["comments"]
print(comments)

print(comment_doc)