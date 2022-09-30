from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# admin.site.register(User, UserAdmin)
admin.site.register(Profile)



admin.site.register(MyUser)




