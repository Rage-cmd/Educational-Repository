from django.urls import include, path
from repositoryAPI import views

urlpatterns = [
    path('user', views.UserView.as_view()),
]
