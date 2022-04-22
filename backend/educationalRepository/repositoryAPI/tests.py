from django.test import TestCase

# Create your tests here.
from Search.searchAlgorithms import *

# post = post_ID_search('p12')
# print(post)

# post_caption = post_name_search('caption')
# print(post_caption)

posts = tag_ID_search('t5')

for post in posts:
    print(post['caption'])