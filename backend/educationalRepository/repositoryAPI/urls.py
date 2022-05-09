from django.urls import include, path
from repositoryAPI import views

urlpatterns = [
    # path('user', views.GenericView.as_view(collection='users_collection')),
    # path('post', views.GenericView.as_view(collection='posts_collection')),
    # path('comment', views.GenericView.as_view(collection='comments_collection')),
    path('user', views.GenericView.as_view(collection='users_collection')),
    path('post', views.GenericView.as_view(collection='posts_collection')),
    path('comment', views.GenericView.as_view(collection='comments_collection')),
    path('login', views.login_creds),
    path('signup', views.sign_up),
    path('uploads\<str:user_id>', views.fetch_user_posts),    
]
