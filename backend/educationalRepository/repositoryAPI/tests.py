from django.test import TestCase

# Create your tests here.
from Search.searchAlgorithms import *
from Suggestion.suggestions import *

# post = post_ID_search('p12')
# print(post)

# post_caption = post_name_search('caption')
# print(post_caption)

# posts = tag_ID_search('t5')

# for post in posts:
#     print(post['caption'])

suggested_posts = post_suggestions('4')

for post in suggested_posts:
    print(post['caption'])