from django.urls import include, path
from repositoryAPI import views

urlpatterns = [
    path('user', views.GenericView.as_view(collection='users_collection')),
    path('post', views.GenericView.as_view(collection='posts_collection')),
    path('comment', views.GenericView.as_view(collection='comments_collection')),
    path('login', views.login_creds),
    path('signup', views.sign_up),
    path('uploads/<str:user_id>', views.fetch_user_posts), 
    path('uploadpost',views.upload_user_post),
    path('approvepost',views.approve_user_post),
    path('unapprovepost',views.unapprove_user_post),
    path('banuser',views.ban_user),
    path('saved/<str:user_id>',views.fetch_watchlist),
    path('user/<str:user_id>',views.fetch_user_details),
    path('updaterole/<str:user_id>/<str:role>',views.update_user_role),
    path('post/<str:post_id>',views.fetch_post),
    path('comments/<str:post_id>',views.fetch_comments),
    path('suggest',views.suggest),
    path('search',views.search),
    path('users',views.get_all_users),
    path('unbanuser',views.unban_user),
    path('pendingapprovals',views.fetch_pending_approvals),
    path('likepost',views.like_user_post),
    path('savepost',views.save_user_post),
]
