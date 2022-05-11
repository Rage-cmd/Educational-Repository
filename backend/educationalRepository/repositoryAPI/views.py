from gettext import find
import hashlib
import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

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
            "notifications": [],
            "no_of_bans": 0,
            "is_banned": False,
        }

        result = saveSingleDocument("test_db","users_collection",user_document)
        return JsonResponse(json.loads(json.dumps(user_document, default=str)), safe=False, status=200)
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
@api_view(['POST'])
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
        print("------------------------------------------------------------------")
        user_id = request.data['user_id']

        post_details = {
            "text" : request.data['text'],
            "caption" : request.data['caption'],
            "tag" : json.loads(request.data['tags']),
        }
        
        print(request.data.keys())

        if 'image' in request.data.keys():
            if request.data['image'] == '':
                post_details['type'] = 'text'
            else:
                post_details['type'] = 'image'
                post_details['image_url'] = request.FILES['image']
        elif 'video' in request.data.keys():
            if request.data['video'] == '':
                post_details['type'] = 'text'
            else:
                post_details['type'] = 'video'
                post_details['video_url'] = request.FILES['video']

        print(post_details)

        # try:
        uploaded_post = upload_post(user_id, post_details,cache)
        return JsonResponse(json.loads(json.dumps(uploaded_post,default=str)), safe=False, status=200)
        # except Exception as e:
            # return HttpResponse("Post upload failed. The error is: " + str(e))
    else:
        return HttpResponse("Invalid request")


@csrf_exempt
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

@csrf_exempt
def unapprove_user_post(request):
    """
    Unapproves a post.

    The function expects a post id.

    Upon successful unapproval, the function returns HTTP response with status 200.

    Example::

        data ={
            "post_id" : <post_id>
        }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        post_id = data['post_id']
        try:
            unapprove_post(post_id)
            return HttpResponse("Post unapproved successfully.", status=200)
        except Exception as e:
            return HttpResponse("Post unapproval failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def ban_user(request):
    """
    Bans a user.
    The request should contain the user id.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_id = data['user_id']

        if(ban_user_mod(user_id)):
            return HttpResponse("User banned successfully.", status=200)
        else:
            return HttpResponse("User ban failed. Check the user access level.", status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def unban_user(request):
    """
    Unbans a user.
    The request should contain the user id.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_id = data['user_id']
        
        if(unban_user_mod(user_id)):
            return HttpResponse("User ban lifted", status=200)
        else:
            return HttpResponse("User unban failed. Check the user access level.", status=500)
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
                post = get_detailed_post(post_id)
                saved_posts.append(post)

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
            user = findSingleDocument("test_db","users_collection",{"id":user_id})
            for post_id in user_posts:
                post = get_detailed_post(post_id)
                posts.append(post)

            return JsonResponse(json.loads(json.dumps(posts, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch posts. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)
    

@csrf_exempt
def update_user_role(request):
    """
    Updates the user id of a user.
    The request should contain the admin id and the user id.

    Example::

        data ={
            "user_id" : <user_id>,
            "role" : <role>
        }
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user_id = data['user_id']
            role = data['role']
            assign_role(user_id, role)
            user_doc = findSingleDocument("test_db","users_collection",{"id":user_id})
            return JsonResponse(json.loads(json.dumps(user_doc,default=str)),status="200")
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
        # comments = []
        try:
            post = get_detailed_post(post_id)
            return JsonResponse(json.loads(json.dumps(post,default=str)), safe=False)
        except Exception as e:
            return HttpResponse("Cannot fetch post. Check the post id. The error is " + str(e), status=500)
    else:
        return HttpResponse("Invalid request")


def fetch_pending_approvals(request):
    """
    Fetches the pending approvals.
    """
    if request.method == 'GET':
        try:
            posts = get_pending_approvals()
            for post in posts:
                author = findSingleDocument("test_db","users_collection",{"id":post['author']})
                post['author'] = {
                    "id" : author['id'],
                    "name" : author['name'],
                    "profile_picture" : author['profile_picture'],
                }
            # sort posts by date
            posts.sort(key=lambda x: x['date'], reverse=True)
            return JsonResponse(json.loads(json.dumps(posts, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch pending approvals. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


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


@csrf_exempt
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
            results = None
            if search_type == "post":
                results = post_suggestions(search_term)
                posts =[]

                for post in results:
                    post = get_detailed_post(post['id'])
                    posts.append(post)

                return JsonResponse(json.loads(json.dumps(posts[:10], default=str)), safe=False, status=200)

            elif search_type == "tag":
                results = tag_suggestions(search_term)
                tags = []
                for tag in results:
                    tag_ids = tag['path_to_tag']
                    path_to_tag_docs = []
                    for tag_id in tag_ids:
                        tag_doc = findSingleDocument("test_db","tagtree_collection",{"id":tag_id})
                        path_to_tag_docs.append(tag_doc)
                    tag['path_to_tag'] = path_to_tag_docs
                    tags.append(tag)
                return JsonResponse(json.loads(json.dumps(tags[:10], default=str)), safe=False, status=200)
            elif search_type == "child_search":
                results = neighbour_suggestions(search_term)
                response = {
                    "posts": results[0],
                    "tags": results[1]
                }
                return JsonResponse(json.loads(json.dumps(response, default=str)), safe=False, status=200)
            
        except Exception as e:
            return HttpResponse("Suggestion failed. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
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
            results = None
            if search_type == "post":
                post = post_ID_search(search_term)
                results = get_detailed_post(post['id'])
            # elif search_type == "post":
            #     results = post_name_search(search_term)
            elif search_type == "tag":
                posts = tag_ID_search(search_term)
                results = []
                for post in posts:
                    comments = []
                    for comment_id in post['comments']:
                        comment = findSingleDocument("test_db","comments_collection",{"id":comment_id})
                        author = findSingleDocument("test_db","users_collection",{"id":comment["author"]})
                        comment['author'] = {
                            "id" : author['id'],
                            "name" : author['name'],
                            "profile_picture" : author['profile_picture'],
                        }
                        comments.append(comment)
                    post['comments'] = comments
                    results.append(post)
        
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


@csrf_exempt
def like_user_post(request):
    """
    Likes a post.
    The request should contain the user id as well as the post id.
    
    Example::
    
        data = {
            "user_id" : <user_id>,
            "post_id" : <post_id>,
            }
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        post_id = data['post_id']
        
        try:
            like_post(user_id,post_id,cache)
            post = findSingleDocument("test_db","posts_collection",{"id":post_id})
            response = {
                "status" : "success",
                "likes": post["upvotes"]
            }
            return JsonResponse(json.loads(json.dumps(response, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to like post. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def save_user_post(request):
    """
    Saves a post.
    The request should contain the user id as well as the post id.
    
    Example::
    
        data = {
            "user_id" : <user_id>,
            "post_id" : <post_id>,
            }
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        post_id = data['post_id']
        result = save_post(user_id,post_id)
        if result == 1:
            return HttpResponse("Saved successfully", status=200)
        elif result == -1:
            return HttpResponse("Unsaved successfully", status=200)
        else:
            return HttpResponse("Failed to save post", status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def verify_user_comment(request):
    """
    Verifies the user's comment.
    The request should contain the user id as well as the comment id.
    
    Example::
    
        data = {
            "user_id" : <user_id>,
            "comment_id" : <comment_id>,
            }
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        comment_id = data['comment_id']
        try:
            if verify_comment(user_id, comment_id):
                return HttpResponse("Verified successfully", status=200)
            else:
                return HttpResponse("Cannot verify comment. Check if the user is the author of the post the comment was written for.", status=200)
        except Exception as e:
            return HttpResponse("Failed to verify comment. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def report_user_comment(request):
    """
    Reports a comment.
    The request should contain the user id as well as the comment id.
    
    Example::
    
        data = {
            "user_id" : <user_id>,
            "comment_id" : <comment_id>,
            }
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        comment_id = data['comment_id']
        try:
            result = report_comment(user_id,comment_id)
            if result == 1:
                return HttpResponse("Comment Reported", status=200)
            elif result == -1:
                return HttpResponse("Comment already reported", status=200)
            else:
                return HttpResponse("Failed to report comment. Check comment ID.", status=200)
        except Exception as e:
            return HttpResponse("Failed to report comment. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


@csrf_exempt
def report_user_post(request):
    """
    Reports a post.
    The request should contain the user id as well as the post id.
    
    Example::
    
        data = {
            "user_id" : <user_id>,
            "post_id" : <post_id>,
            }
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        post_id = data['post_id']
        try:
            result = report_post(user_id,post_id)
            if result == 1:
                return HttpResponse("Post Reported", status=200)
            elif result == -1:
                return HttpResponse("Post already reported", status=200)
            else:
                return HttpResponse("Failed to report post. Check post ID.", status=200)
        except Exception as e:
            return HttpResponse("Failed to report post. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_latest_posts(request):
    # cache.clear_cache()

    if request.method == "GET":
        try:
            posts = cache.getAllItems_recent_cache()
            response_posts = []
    
            for post in posts:
                post = get_detailed_post(post['id'])
                response_posts.append(post)

            return JsonResponse(json.loads(json.dumps(response_posts, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch posts. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_most_commented_posts(request):
    # cache.clear_cache()
    if request.method == "GET":
        try:
            posts = cache.getAllItems_comment_cache()
            response_posts = []
            for post in posts:
                print(post['id'])
                post = get_detailed_post(post['id'])
                response_posts.append(post)
            return JsonResponse(json.loads(json.dumps(response_posts, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to fetch posts. The error is: " + str(e), status=500)


@csrf_exempt
def upload_user_comment(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_id = data['user_id']
        post_id = data['post_id']
        comment_text = data['text']
        try:
            comment = comment_post(user_id,post_id,comment_text, cache)
            if not comment:
                return HttpResponse("Failed to comment on post. Check post ID.", status=200)
            # print(comments)
            # for comment in comments:
            comment_author = findSingleDocument("test_db","users_collection",{"id":comment['author']})
            comment['author'] = {
                "id" : comment_author['id'],
                "name" : comment_author['name'],
                "profile_picture" : comment_author['profile_picture'],
            }

            return JsonResponse(json.loads(json.dumps(comment, default=str)), safe=False, status=200)
        except Exception as e:
            return HttpResponse("Failed to upload comment. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
def create_user_tags(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        tag_name = data['name']
        tag_id = data['tag']
        try:
            path_to_tag = findSingleDocument("test_db","tagtree_collection",{"id":tag_id})['path_to_tag']
            path_to_tag.append(tag_id)
            result = insert_tag(tag_name,path_to_tag)
            if result:
                return HttpResponse("Tags created successfully", status=200)
            else:
                return HttpResponse("Failed to create tags. Check if the parent exists.", status=200)
        except Exception as e:
            return HttpResponse("Failed to create tags. The error is: " + str(e), status=500)
    else:
        return HttpResponse("Invalid request", status=400)


def fetch_reported_post(request):
    if request.method == "GET":
        try:
            # reports = findAllDocument("test_db","reports_collection",{})
            reports = findAllDocument("test_db","posts_collection",{"reports" : {"$gt" : 0}})
            posts = []
            for report in reports:
                post = get_detailed_post(report['id'])
                posts.append(post)
            
            # sort posts by number of reports
            posts.sort(key=lambda x: x['reports'], reverse=True)

            return JsonResponse(json.loads(json.dumps(posts, default=str)), safe=False, status=200)
        
        except Exception as e:
            return HttpResponse("Failed to fetch reports. The error is: " + str(e), status=500)
    else:    
        return HttpResponse("Invalid request", status=400)


# def fetch_reported_comment(request):
#     if request.method == "GET":
#         try:
#             reports = findAllDocument("test_db","reports_collection",{})
#             comments = []
#             for report in reports:
#                 if report['type'] == 'comment':
#                     comment = get_detailed_comment(report['comment_id'])
#                     comments.append(comment)
#             return JsonResponse(json.loads(json.dumps(comments, default=str)), safe=False, status=200)
#         except Exception as e:
#             return HttpResponse("Failed to fetch reports. The error is: " + str(e), status=500)
#     else:    
#         return HttpResponse("Invalid request", status=400)

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