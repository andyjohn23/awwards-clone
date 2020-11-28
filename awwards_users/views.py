from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import UserAccount


# Create your views here.


def index(request):
    return render(request, 'awwards-users/index.html')


def register(request, *arg, **kwargs):

    return render(request, 'awwards-users/register.html')


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("index")


def login_user(request, *args, **kwargs):
    return render(request, 'awwards-users/login.html')


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))

    return redirect
