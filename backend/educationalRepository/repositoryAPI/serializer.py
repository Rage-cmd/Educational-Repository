from unittest.util import _MAX_LENGTH
from rest_framework import serializers, routers, viewsets

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    access_level = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    posts = serializers.ListField(child=serializers.CharField(max_length=100))
    comments = serializers.ListField(child=serializers.CharField(max_length=100))
    saved_posts = serializers.ListField(child=serializers.CharField(max_length=100))
    liked_posts = serializers.ListField(child=serializers.CharField(max_length=100))
    points = serializers.IntegerField()
    profile_picture = serializers.CharField(max_length=100)
    no_of_bans = serializers.IntegerField()
    is_banned = serializers.BooleanField()

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    time = serializers.TimeField()
    tags = serializers.ListField(child=serializers.CharField(max_length=100))
    caption = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)
    options = serializers.ListField(required = False, child=serializers.CharField(max_length=100))
    image_url = serializers.CharField(required = False, max_length=100)
    video_url = serializers.CharField(required = False,max_length=100)
    upvotes = serializers.IntegerField()
    is_answered = serializers.BooleanField()
    reports = serializers.IntegerField()
    comments = serializers.ListField(child=serializers.CharField(max_length=100))

class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    post_id = serializers.CharField(max_length=100)
    time = serializers.TimeField()
    text = serializers.CharField(max_length=100)
    upvotes = serializers.IntegerField()
    reports = serializers.IntegerField()
    is_verified = serializers.BooleanField()

class MainTreeSerializer(serializers.Serializer):
    tree_type = serializers.CharField(max_length=100)
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    children_tags = serializers.ListField(child=serializers.CharField(max_length=100))
    children_posts = serializers.ListField(child=serializers.CharField(max_length=100))

class TagTreeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    path_to_tag = serializers.ListField(child=serializers.CharField(max_length=100))
    