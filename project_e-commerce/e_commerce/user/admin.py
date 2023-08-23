from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .permissionandgroup import UserAdmin
from .models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Useraddress)
admin.site.register(OTPToken)
admin.site.register(CustomUser, UserAdmin)

