from django.contrib import admin
from awwards_users.models import UserAccount, Profile, Category, Projects, Rates

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Rates)