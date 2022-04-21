from rest_framework import serializers, routers, viewsets

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    user_email = serializers.EmailField(max_length=100)
    user_password = serializers.CharField(max_length=100)
    user_access_level = serializers.CharField(max_length=100)
    user_status = serializers.CharField(max_length=100)
    user_posts = serializers.ListField(child=serializers.CharField(max_length=100))
    user_comments = serializers.ListField(child=serializers.CharField(max_length=100))
    user_points = serializers.IntegerField()
    user_profile_picture = serializers.CharField(max_length=100)
    user_no_of_bans = serializers.IntegerField()
    user_is_banned = serializers.BooleanField()
    