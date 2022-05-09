import hashlib
import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import sys
sys.path.append("..")

from databaseInterfaces.mongoDB_interface import *
from django.http import HttpResponse,JsonResponse
from rest_framework import views
from rest_framework.response import Response

from repositoryAPI.serializer import *
from rest_framework.parsers import JSONParser
from databaseInterfaces.drive_api import *

from repositoryAPI.User.userUtilities import *
from repositoryAPI.Caching.cache_impl import *
from repositoryAPI.Moderator.modUtilities import *
from repositoryAPI.Admin.adminUtilities import *

serializers = {
    'users_collection' : UserSerializer,
    'posts_collection' : PostSerializer,
    'comments_collection': CommentSerializer,
    'main_tree_collection': MainTreeSerializer
}

class GenericView(views.APIView):
    collection = None

    def __init__(self, collection):
        self.collection = collection
    
    def get(self, request):
        cursor = findAllDocument("test_db",self.collection,{})
        data = []
        for document in cursor:
            data.append(document)
        result =  serializers[self.collection](data, many=True).data
        return JsonResponse(result, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db",self.collection,data)
        return JsonResponse(result, safe=False)
    
    def put(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db",self.collection,data)
        return JsonResponse(result, safe=False)
    
    def delete(self, request):
        data = JSONParser().parse(request)
        result = deleteDocument("test_db",self.collection,data)
        return JsonResponse(result, safe=False)
    
@csrf_exempt
def login_creds(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = data['username']
        password = data['password']
        hashed_password = make_password_hash(password)
        user_document = findSingleDocument("test_db","users_collection",{"username":user,"password":hashed_password})
        if user_document:
            return JsonResponse(user_document, safe=False, status=200)
        else:
            return HttpResponse("Invalid Username or Password", status=400)
    else:
        return HttpResponse("Invalid request", status=400)
    
# make password hash
def make_password_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# retrieve password from hash
def retrieve_password(password_hash):
    return hashlib.sha256(password_hash.encode('utf-8')).hexdigest()

# saves the new user in the database
def sign_up(request):
    """
    Sign up a new user.

    The function expects a dictionary consisting of the following keys:
        username (str) : The username of the user.
        password (str) : The password of the user.
        email (str) : The email of the user.
    
    Example::

        data = {
            "username" : <username>,
            "password" : <password>,
            "email" : <email>
        }

    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['username']
        hashed_password = make_password_hash(data['password'])
        email = data['email']
        user_document = {
            'id': getNextSequenceValue("test_db","users_collection"),
            "name": name,
            "password": hashed_password,
            "email": email,
            "account_type": "user",
            "status": "active",
            "posts": [],
            "comments": [],
            "saved_posts": [],
            "liked_posts": [],
            "points": 0,
            "profile_picture": "",
            "no_of_bans": 0,
            "is_banned": False,
        }

        result = saveSingleDocument("test_db","users_collection",user_document)
        return JsonResponse(user_document, safe=False, status=200)
    else:
        return HttpResponse("Invalid request", status=400)


def upload_user_post(request):
    """
    Upload a post. The function expects a user id and a dictionary consisiting of post details.

    The dictionary should contain the following keys:
        type (str) : The type of the post.
        text (str) : The text of the post.
        caption (str) : The caption of the post.
        tags (list) : A list of tag IDs. The tag IDs should be in the order of tree heirarchy i.e [root, first child, second child, ...].

    Optional keys:
        image_url (str) : The url of the image.
        video_url (str) : The url of the video.
        new_tag (str) : The name of the new tag. The new tag will be created if it does not exist. Use this key only if the tag is not in the tags list. 
    
    Just using the tags list will create a post with the tags present in the list (the order of tags in the list is important).
    Using tags with the new_tags field will create a post under the tags list with the new tag.

    The function returns a boolean value indicating if the post was uploaded successfully.

    Hence, the HTTP Post request should be of the following format: 
    Example::

        data ={
            "user_id" : <user_id>,
            "post_details" : {
                "type" : <post_type>,
                "text" : <post_text>,
                "caption" : <post_caption>,
                "tags" : [<tag_id_1>, <tag_id_2>, ...], // The order "must" be [root, first child, second child, ...]
                "image_url" : <image_url>,  // OPTIONAL
                "video_url" : <video_url>,  // OPTIONAL
                "new_tag" : <new_tag_name>  // OPTIONAL
            }
        }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_id = data['user_id']
        post_details = data['post_details']
        try:
            uploaded_post = upload_post(user_id, post_details,cache)
            return JsonResponse(uploaded_post,"Post uploaded successfully.")
        except Exception as e:
            return HttpResponse("Post upload failed. The error is: " + str(e))
    else:
        return HttpResponse("Invalid request")


def approve_user_post(request):
    """
    Approves a post.

    The function expects a post id.

    Upon successful approval, the function returns HTTP response with status 200.

    Example::
        
        data ={
            "post_id" : <post_id>
        }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        post_id = data['post_id']
        try:
            approve_post(post_id)
            return HttpResponse("Post approved successfully.", status=200)
        except Exception as e:
            return HttpResponse("Post approval failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def ban_user(request):
    """
    Bans a user.
    The request should contain the user id.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_id = data['user_id']
        try:
            ban_user(user_id)
            return HttpResponse("User banned successfully.", status=200)
        except Exception as e:
            return HttpResponse("User ban failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_watchlist(request, user_id):
    """
    Fetches the watchlist of a user.
    The request should contain the user id.
    """
    if request.method == 'GET':
        try:
            saved_post_ids = findSingleDocument("test_db","users_collection",{"id":user_id})['saved_posts']
            saved_posts = []
            for post_id in saved_post_ids:
                saved_posts.append(findSingleDocument("test_db","posts_collection",{"id":post_id}))
            return JsonResponse(saved_posts, safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch watchlist. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_user_details(request, user_id):
    """
    Fetches the details of a user.
    The request should contain the user id.
    """

    if request.method == 'GET':
        try:
            user_doc = findSingleDocument("test_db","users_collection",{"id":user_id})
            return JsonResponse(user_doc,status="200")
        except Exception as e:
            return HttpResponse('Could not fetch user details. The error is: ' + str(e))
        
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_user_posts(request, user_id):
    """
    Fetches the posts of a user.
    The request should contain the user id.
    """
    if request.method == 'GET':
        try:
            user_posts = findSingleDocument("test_db","users_collection",{"id":user_id})['posts']
            posts = []
            for post_id in user_posts:
                post = findSingleDocument("test_db","posts_collection",{"id":post_id})
                post['author'] = findSingleDocument("test_db","users_collection",{"id":post['author']})
                posts.append()
            return JsonResponse(posts, safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch posts. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)
    

def fetch_post(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        post_id = data['post_id']
        post = findSingleDocument("test_db","posts_collection",{"id":post_id})
        if post:
            return JsonResponse(post, safe=False)
        else:
            return HttpResponse("Invalid post id")
    else:
        return HttpResponse("Invalid request")


def fetch_comments(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        post_id = data['comment_id']
        comments = findSingleDocument("test_db","comments_collection",{"id":post_id})
        if comments:
            return JsonResponse(comments, safe=False)
        else:
            return HttpResponse("Invalid comment id")
    else:
        return HttpResponse("Invalid request")

cache = CacheImpl(10)
