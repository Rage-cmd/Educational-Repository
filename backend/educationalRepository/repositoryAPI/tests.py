from django.test import TestCase

# Create your tests here.
from Search.searchAlgorithms import *

post = search_post_by_ID('p12')
print(post)

post_caption = search_post_by_name('caption')
print(post_caption)