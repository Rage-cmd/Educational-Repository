from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=100)
#     user_email = models.EmailField(max_length=100)
#     user_password = models.CharField(max_length=100)
#     user_access_level = models.CharField(max_length=100)
#     user_status = models.CharField(max_length=100)
#     user_posts = ArrayField(models.CharField(max_length=100))
#     user_comments = ArrayField(models.CharField(max_length=100))
#     user_points = models.IntegerField()
#     user_profile_picture = models.CharField(max_length=100)
#     user_no_of_bans = models.IntegerField()
#     user_is_banned = models.BooleanField()
    