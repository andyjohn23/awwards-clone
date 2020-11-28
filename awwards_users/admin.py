from django.contrib import admin
from awwards_users.models import UserAccount, Profile

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Profile)