from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm, AuthenticationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import UserAccount, Projects, Category, Rates, Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProjectSearchForm, RatesForm
from .serializer import userSerializer, projectSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class PostListView(ListView):
    model = Projects
    template_name = 'awwards_users/index.html'
    context_object_name = 'projects'
    ordering = ['-created']


class PostDetailView(DetailView):
    model = Projects


def register(request, *arg, **kwargs):
    user = request.user

    if user.is_authenticated:
        return HttpResponse('You are already authenticated as { user.email }.')
    context = {}

    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('index')
        else:
            context['register_form'] = form

    return render(request, 'awwards_users/register.html', context)


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("index")


def login_user(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('index')

        else:
            context['login_form'] = form

    return render(request, 'awwards_users/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))

    return redirect


@login_required(login_url='login')
def profile_edit(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            user_form.save()
            form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect('profile-edit')

    else:
        user_form = UserUpdateForm(instance=request.user)
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'form': form,
    }

    return render(request, 'awwards_users/profile-edit.html', context)


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Projects
    fields = ['sitename', 'siteurl', 'siteimage',
              'description', 'category', 'technology', 'country']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.profile = self.request.user.profile
        form.instance.object_relation_assume = self.request.user.profile
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PersonalPostListView(ListView):
    model = Projects
    template_name = 'awwards_users/personal-projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Projects.objects.filter(profile=self.request.user.profile).distinct()


@method_decorator(login_required, name='dispatch')
class UserPostListView(ListView):
    model = Projects
    template_name = 'awwards_users/personal-profile.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(
            UserAccount, username=self.kwargs.get('username'))
        return Projects.objects.filter(profile=user.profile).order_by('-created')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Projects
    fields = ['sitename', 'siteurl', 'siteimage',
              'description', 'category', 'technology', 'country']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user.profile == project.profile:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Projects
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user.profile == project.profile:
            return True
        return False


class CategoryListView(ListView):
    template_name = 'awwards_users/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'description': self.kwargs['category'],
            'projects': Projects.objects.filter(category__name=self.kwargs['category'])
        }
        return content


def category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return context


def project_search(request):
    form = ProjectSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = ProjectSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Projects.objects.filter(sitename__icontains=q)

    return render(request, 'awwards_users/search.html', {'form': form, 'q': q, 'results': results})


@login_required(login_url='login')
def rating_project(request, id):
    project = Projects.objects.get(id=id)
    rate = Rates.objects.filter(
        user=request.user.profile, project=project).first()
    rate_status = None
    if rate is None:
        rate_status = False
    else:
        rate_status = True
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user.profile
            rate.project = project
            rate.save()
            project_rates = Rates.objects.filter(project=project)

            design_rates = [design.design for design in project_rates]
            design_average = sum(design_rates) / len(design_rates)

            usability_rates = [
                usability.usability for usability in project_rates]
            usability_average = sum(usability_rates) / len(usability_rates)

            creativity_rates = [creat.creativity for creat in project_rates]
            creativity_average = sum(creativity_rates) / len(creativity_rates)

            content_rates = [content.content for content in project_rates]
            content_average = sum(content_rates) / len(content_rates)

            score = (design_average + usability_average +
                     content_average + creativity_average) / 4
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.creativity_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatesForm()
    params = {
        'project': project,
        'rate_form': form,
        'rate_status': rate_status

    }
    return render(request, 'awwards_users/project_rate.html', params)

class userList(APIView):
    def get(self, request):
        user = Profile.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class projectList(APIView):
    def get(self, request):
        project = Projects.objects.all()
        serializer = projectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self):
        pass

