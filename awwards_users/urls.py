from django.urls import path
from .views import PostCreateView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('site/submission/', PostCreateView.as_view(), name="post-create"),
]