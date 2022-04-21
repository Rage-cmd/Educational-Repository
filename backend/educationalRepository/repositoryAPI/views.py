import imp
from django.shortcuts import render

# Create your views here.
import sys
sys.path.append("..")

from databaseInterfaces.mongoDB_interface import *
from django.http import HttpResponse,JsonResponse
from rest_framework import views
from rest_framework.response import Response

from repositoryAPI.serializer import UserSerializer, PostSerializer
from rest_framework.parsers import JSONParser

class UserView(views.APIView):
    def get(self, request):
        cursor = findAllDocument("test_db", "users_collection", {})
        user_data = []
        for doc in cursor:
            user_data.append(doc)
        result = UserSerializer(user_data, many=True).data
        return JsonResponse(result, safe=False)
        # return JsonResponse(result)
    
    def post(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db", "users_collection", data)
        return JsonResponse(result)
        
    def put(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db", "users_collection", data)
        return JsonResponse(result)
    
    def delete(self, request):
        data = JSONParser().parse(request)
        result = deleteDocument("test_db", "users_collection", data)
        return JsonResponse(result)


class PostView(views.APIView):
    def get(self, request):
        cursor = findAllDocument("test_db", "posts_collection", {})
        post_data = []
        for doc in cursor:
            post_data.append(doc)
        result = PostSerializer(post_data, many=True).data
        return JsonResponse(result, safe=False)
        # return JsonResponse(result)
    
    def post(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db", "posts_collection", data)
        return JsonResponse(result)
        
    def put(self, request):
        data = JSONParser().parse(request)
        result = saveSingleDocument("test_db", "posts_collection", data)
        return JsonResponse(result)
    
    def delete(self, request):
        data = JSONParser().parse(request)
        result = deleteDocument("test_db", "posts_collection", data)
        return JsonResponse(result)
