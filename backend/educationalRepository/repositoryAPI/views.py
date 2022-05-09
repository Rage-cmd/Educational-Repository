from gettext import find
import hashlib
import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import sys
sys.path.append("..")


import json

from django.http import HttpResponse,JsonResponse

from databaseInterfaces.mongoDB_interface import *
from databaseInterfaces.drive_api import *

from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from repositoryAPI.serializer import *
from repositoryAPI.User.userUtilities import *
from repositoryAPI.Caching.cache_impl import *
from repositoryAPI.Moderator.modUtilities import *
from repositoryAPI.Admin.adminUtilities import *
from repositoryAPI.Suggestion.suggestions import *
from repositoryAPI.Search.searchAlgorithms import *


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
        email = data['email']
        password = data['password']
        # hashed_password = make_password_hash(password)
        user_document = findSingleDocument("test_db","users_collection",{"email":email,"password":password})

        if user_document['is_banned']:
            return HttpResponse("User is banned", status=400)

        if user_document:
            return JsonResponse(json.loads(json.dumps(user_document, default=str)), safe=False, status=200)
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
@csrf_exempt
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

        all_users = findAllDocument("test_db","users_collection",{})
        emails = []
        for user in all_users:
            emails.append(user['email'])
        
        if email in emails:
            return HttpResponse("Email already exists.", status=400)

        user_document = {
            "id": 'u' + str(getNextSequenceValue("test_db","users_collection")),
            "name": name,
            "password": hashed_password,
            "email": email,
            "access_level": "user",
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
        return JsonResponse(json.loads(json.dumps(user_document, default=str)), safe=False, status=200)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
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
            return JsonResponse(json.loads(json.dumps(saved_posts, default=str)), safe=False, status=200)
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
            return JsonResponse(json.loads(json.dumps(user_doc,default=str)),status="200")
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
                post_doc = findSingleDocument("test_db","users_collection",{"id":post['author']})
                post['author'] = {
                    "id" : post_doc['id'],
                    "name" : post_doc['name'],
                    "profile_picture" : post_doc['profile_picture']
                }
                posts.append(post)
            return JsonResponse(json.loads(json.dumps(posts, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch posts. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)
    

def update_user_role(request, user_id, role):
    """
    Updates the user id of a user.
    The request should contain the admin id and the user id.
    """
    if request.method == 'POST':
        try:
            user_doc = findSingleDocument("test_db","users_collection",{"id":user_id})
            assign_role(user_doc['id'], role)
            return HttpResponse("User role updated successfully.", status=200)
        except Exception as e:
            return HttpResponse("User role update failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_post(request, post_id):
    """
    Fetches a post.
    The request should contain the post id.
    """
    if request.method == 'GET':
        comments = []
        post = findSingleDocument("test_db","posts_collection",{"id":post_id})
        author = findSingleDocument("test_db","users_collection",{"id":post['author']})
        post['author'] = {
            "id" : author['id'],
            "name" : author['name'],
            "profile_picture" : author['profile_picture'],
        }
        
        for comment_id in post['comments']:
            comment = findSingleDocument("test_db","comments_collection",{"id":comment_id})
            comments.append(comment)

        for comment in comments:
            comment_author = findSingleDocument("test_db","users_collection",{"id":comment['author']})
            comment['author'] = {
                "id" : comment_author['id'],
                "name" : comment_author['name'],
                "profile_picture" : comment_author['profile_picture'],
            }
        
        post['comments'] = comments

        if post:
            return JsonResponse(json.loads(json.dumps(post,default=str)), safe=False)
        else:
            return HttpResponse("Invalid post id")
    else:
        return HttpResponse("Invalid request")


def fetch_comments(request, post_id):
    """
    Fetches the comments of a post.
    The request should contain the post id.
    
    Example::
    
        data ={
            "post_id" : <post_id>
        }
    """
    if request.method == 'GET':
        try:
            comment_ids = findSingleDocument("test_db","posts_collection",{"id":post_id})['comments']
            comments = []
            for comment_id in comment_ids:
                comment = findSingleDocument("test_db","comments_collection",{"id":comment_id})
                comment['author'] = findSingleDocument("test_db","users_collection",{"id":comment["id"]})
                comments.append(comment)
            return JsonResponse(json.loads(json.dumps(comments, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch comments. The error is: " + str(e), status=500)
        
    else:
        return HttpResponse("Invalid request", status=400)


def suggest(request):
    """
    Suggests a post/tag.
    The request should be as follows:
    
    Example::
    
        data = {
            "search_type" : <search_type>,
            "search_term" : <search_term>,
        }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_type = data['search_type']
        search_term = data['search_term']
        try:
            if search_type == "post":
                results = post_suggestions(search_term)
            elif search_type == "tag":
                results = tag_suggestions(search_term)
            return JsonResponse(json.loads(json.dumps(results, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Suggestion failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def search(request):
    """
    Searches for posts,tags or users.
    The request should be as follows:

    Example::

        data = {
            "search_type" : <search_type>,
            "search_term" : <search_term>,
        }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_type = data['search_type']
        search_term = data['search_term']
        try:
            if search_type == "post by ID":
                results = post_ID_search(search_term)
            elif search_type == "post by name":
                results = post_name_search(search_term)
            elif search_type == "tag by ID":
                results = tag_ID_search(search_term)
        
            return JsonResponse(json.loads(json.dumps(results, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Search failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def get_all_users(request):
    if request.method == "GET":
        try:
            users = findAllDocument("test_db","users_collection",{})
            users_doc = []
            for user in users:
                users_doc.append(user)
            return JsonResponse(json.loads(json.dumps(users_doc, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch users. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


cache = CacheImpl(10)


# test upload
# {
#     "user_id": "u1",
#     "post_details": {
#         "type": "text",
#         "text": "This post has been uploaded using postman!!",
#         "caption": "My first Postman Post!",
#         "tags":["t1","t2"],
#     }
# }