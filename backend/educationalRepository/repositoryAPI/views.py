import imp
import re
from django.shortcuts import render

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
    
