from django.urls import path
from .views import PostCreateView, ProfileList
from . import views


urlpatterns = [
    path('', ProfileList.as_view(), name='index'),
    path('site/submission/', PostCreateView.as_view(), name="post-create"),
]