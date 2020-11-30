from django.urls import path
from .views import PostListView, PostCreateView, UserPostListView, PostUpdateView, PostDetailView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('site/submission/', PostCreateView.as_view(), name="post-create"),
    path('user-details/', UserPostListView.as_view(), name="user-details"),
    path('project/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('project/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
]