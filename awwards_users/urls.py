from django.urls import path
from .views import CategoryListView, PostDeleteView, PostListView, PostCreateView, PersonalPostListView, UserPostListView, PostUpdateView, PostDetailView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('rates/', views.rating_project, name='rating'),
    path('site/submission/', PostCreateView.as_view(), name="post-create"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-details"),
    path('user/details/', PersonalPostListView.as_view(), name="user-detail"),
    path('project/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('project/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('project/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('category/<category>/', views.CategoryListView.as_view(), name="category"),
    path('search/', views.project_search, name='project-search'),
]

