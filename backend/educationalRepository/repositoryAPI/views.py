import imp
from django.shortcuts import render

# Create your views here.
import sys
sys.path.append("..")

from databaseInterfaces.mongoDB_interface import *
from django.http import HttpResponse,JsonResponse
from rest_framework import views
from rest_framework.response import Response

from repositoryAPI.serializer import UserSerializer
from rest_framework.parsers import JSONParser

class UserView(views.APIView):
    def get(self, request):
        cursor = findAllDocument("test_db", "users_col", {'user_points': 100})
        user_data = []
        for doc in cursor:
            user_data.append(doc)
        result = UserSerializer(user_data, many=True).data
        return Response(result)
        # return JsonResponse(result)
        