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

saved_posts = get_posts('u5','saved')

for post in saved_posts:
    print(post['caption'])

uploaded_posts = get_posts('u5','uploads')

for post in uploaded_posts:
    print(post['caption'])