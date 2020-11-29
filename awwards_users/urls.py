from django.urls import path
from .views import PostCreateView, ProfileList, UserPostListView
from . import views


urlpatterns = [
    path('', ProfileList.as_view(), name='index'),
    path('site/submission/', PostCreateView.as_view(), name="post-create"),
    path('user-details/', UserPostListView.as_view(), name="user-details"),
]