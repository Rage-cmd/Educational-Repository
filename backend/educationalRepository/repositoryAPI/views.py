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
