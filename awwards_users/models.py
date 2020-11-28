from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image

# Create your models here.


class ManagerAccount(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('users must have an emailaddress')
        if not username:
            raise ValueError('users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username = models.CharField(max_length=70, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = ManagerAccount()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(default='default-avatar.jpg')
    url = models.URLField(max_length=300, blank=True)
    description = models.TextField(max_length=200, blank=True)
    Freelance = 'Fl'
    Agency = 'Ag'
    Studio = 'St'

    CAREER_CHOICES = [
        (Freelance, 'Freelance'),
        (Agency, 'Agency-More than 10 people'),
        (Studio, 'Studio-10 people or fewer'),
    ]
    career = models.CharField(
        default='Freelance', choices=CAREER_CHOICES, max_length=100, blank=False)
    twitter = models.URLField(
        default='https://twitter.com/', max_length=200, blank=True)
    facebook = models.URLField(
        default='https://www.facebook.com/', max_length=200, blank=True)
    linkedin = models.URLField(
        default='https://linkedin.com/', max_length=200, blank=True)
    instagram = models.URLField(
        default='https://instagram.com/', max_length=200, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-date_joined',)
